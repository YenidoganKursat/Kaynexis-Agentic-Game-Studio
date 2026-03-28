#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

from _studio_common import (
    ACTIVE_DIR,
    REPO_ROOT,
    engine_detection_report,
    find_godot_binary,
    find_unity_cli,
    find_unity_hub,
    find_unreal_editor,
    find_unreal_uat,
    load_root_studio_config,
    repo_summary,
    unresolved_placeholders,
)
from studio_core import STUDIO_CONFIG_PATH, available_starter_kits, configured_project_name, research_notes, validate_research_note
from validate_docs import collect_doc_findings
from validate_repo_layout import REQUIRED_PATHS

HOOKS = ("pre-commit", "pre-push", "commit-msg")
ROOT_AGENTS_PATH = REPO_ROOT / "AGENTS.md"
PROJECT_CONFIG_PATH = REPO_ROOT / ".codex" / "config.toml"
REVIEW_GUIDE_PATH = REPO_ROOT / "docs" / "reference" / "code-review.md"
EVAL_STRATEGY_PATH = REPO_ROOT / "docs" / "reference" / "eval-strategy.md"
RESEARCH_NOTES_PATH = REPO_ROOT / "docs" / "research" / "openai-codex-infra-findings.md"
EVAL_TEMPLATE_PATH = REPO_ROOT / "studio" / "docs" / "templates" / "eval-plan.md"
REVIEWER_AGENT_PATH = REPO_ROOT / ".codex" / "agents" / "reviewer.toml"
CODEX_STUDIO_CLI_PATH = REPO_ROOT / "scripts" / "codex_studio.py"
STARTER_KITS_PATH = REPO_ROOT / "studio" / "starter-kits"
CHECKLISTS_PATH = REPO_ROOT / "studio" / "checklists"
RESEARCH_KB_PATH = REPO_ROOT / "docs" / "research" / "game-development"
GENRE_REFERENCE_PATH = REPO_ROOT / "docs" / "reference" / "genre-presets.md"
GENRE_TEMPLATE_PATH = REPO_ROOT / "studio" / "docs" / "templates" / "genre-starter.md"
START_SCRIPT_PATH = REPO_ROOT / "scripts" / "start_game_studio.py"
CODEOWNERS_PATH = REPO_ROOT / ".github" / "CODEOWNERS"
WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"
ISSUE_TEMPLATE_DIR = REPO_ROOT / ".github" / "ISSUE_TEMPLATE"
ISSUE_TEMPLATE_FILES = [
    ISSUE_TEMPLATE_DIR / "config.yml",
    ISSUE_TEMPLATE_DIR / "bug-report.yml",
    ISSUE_TEMPLATE_DIR / "feature-request.yml",
    ISSUE_TEMPLATE_DIR / "infra-routing-change.yml",
    ISSUE_TEMPLATE_DIR / "genre-preset-update.yml",
]
COMMUNITY_FILES = [
    REPO_ROOT / "CONTRIBUTING.md",
    REPO_ROOT / "SECURITY.md",
    REPO_ROOT / "SUPPORT.md",
    REPO_ROOT / "CODE_OF_CONDUCT.md",
]
LOCAL_EVALS_PATH = REPO_ROOT / "scripts" / "run_local_evals.py"
ENGINE_KIT_VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_engine_kits.py"
WORKFLOW_VALIDATOR_PATH = REPO_ROOT / "scripts" / "validate_workflows.py"
CI_ARTIFACT_REPORT_PATH = REPO_ROOT / "scripts" / "ci_artifact_report.py"
STARTER_KIT_SMOKE_PATH = REPO_ROOT / "scripts" / "starter_kit_contract_smoke.py"
UNITY_ADAPTER_PATH = REPO_ROOT / "scripts" / "unity_adapter.py"
UNREAL_ADAPTER_PATH = REPO_ROOT / "scripts" / "unreal_adapter.py"
EVALS_DIR = REPO_ROOT / "evals"
HOOKS_CONFIG_PATH = REPO_ROOT / ".codex" / "hooks.json"
ENV_EXAMPLE_PATH = REPO_ROOT / ".env.example"
SECRETS_DOC_PATH = REPO_ROOT / "docs" / "setup" / "secrets-and-env.md"
CODEX_COMPAT_DOC_PATH = REPO_ROOT / "docs" / "reference" / "codex-compatibility.md"
CI_CD_ARCHITECTURE_DOC_PATH = REPO_ROOT / "docs" / "reference" / "ci-cd-architecture.md"
BASELINE_SCRIPT_PATH = REPO_ROOT / "scripts" / "seed_project_baseline.py"
GODOT_SMOKE_SCRIPT_PATH = REPO_ROOT / "scripts" / "godot_smoke.py"
GODOT_EXPORT_SCRIPT_PATH = REPO_ROOT / "scripts" / "godot_export.py"
GODOT_EXPORT_PRESETS_PATH = REPO_ROOT / "export_presets.cfg"
AGENTS_LINE_WARN_THRESHOLD = 220


def make_check(name: str, status: str, detail: str, required: bool = False, next_step: str | None = None) -> dict[str, object]:
    return {
        "name": name,
        "status": status,
        "detail": detail,
        "required": required,
        "next_step": next_step,
    }


def summarize_placeholders() -> dict[str, list[str]]:
    unresolved: dict[str, list[str]] = {}
    if not ACTIVE_DIR.exists():
        return unresolved
    for path in sorted(ACTIVE_DIR.glob("*.md")):
        placeholders = unresolved_placeholders(path.read_text(encoding="utf-8"))
        if placeholders:
            unresolved[path.name] = placeholders
    return unresolved


def load_project_config() -> dict[str, object]:
    if not PROJECT_CONFIG_PATH.exists():
        return {}
    return tomllib.loads(PROJECT_CONFIG_PATH.read_text(encoding="utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser(description="Check local tooling and repo health for the studio operating system.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    args = parser.parse_args()

    checks: list[dict[str, object]] = []

    if sys.version_info >= (3, 11):
        checks.append(make_check("python", "pass", f"Python {sys.version.split()[0]} detected.", required=True))
    else:
        checks.append(make_check("python", "fail", f"Python {sys.version.split()[0]} detected; 3.11+ is required.", required=True, next_step="Install a newer Python and rerun doctor."))

    missing_paths = [rel for rel in REQUIRED_PATHS if not (REPO_ROOT / rel).exists()]
    if missing_paths:
        checks.append(make_check("repo-layout", "fail", f"Missing required paths: {', '.join(missing_paths)}", required=True, next_step="Restore the missing files or rerun repo setup."))
    else:
        checks.append(make_check("repo-layout", "pass", "All required layout paths are present.", required=True))

    checks.append(
        make_check(
            "studio-config",
            "pass" if STUDIO_CONFIG_PATH.exists() else "warn",
            "Root studio.toml is present." if STUDIO_CONFIG_PATH.exists() else "Root studio.toml is missing.",
            next_step=None if STUDIO_CONFIG_PATH.exists() else "Create studio.toml so the shared config surface is explicit.",
        )
    )
    checks.append(
        make_check(
            "codex-studio-cli",
            "pass" if CODEX_STUDIO_CLI_PATH.exists() else "warn",
            "Front-door Codex Studio CLI is present." if CODEX_STUDIO_CLI_PATH.exists() else "Front-door Codex Studio CLI is missing.",
            next_step=None if CODEX_STUDIO_CLI_PATH.exists() else "Restore scripts/codex_studio.py.",
        )
    )
    checks.append(
        make_check(
            "review-guide",
            "pass" if REVIEW_GUIDE_PATH.exists() else "warn",
            "Review guide is present." if REVIEW_GUIDE_PATH.exists() else "Dedicated review guide is missing.",
            next_step=None if REVIEW_GUIDE_PATH.exists() else "Restore docs/reference/code-review.md so review expectations stay explicit.",
        )
    )
    checks.append(
        make_check(
            "eval-surface",
            "pass" if EVAL_STRATEGY_PATH.exists() and EVAL_TEMPLATE_PATH.exists() else "warn",
            "Eval strategy doc and template are present."
            if EVAL_STRATEGY_PATH.exists() and EVAL_TEMPLATE_PATH.exists()
            else "Eval strategy or eval template is missing.",
            next_step=None
            if EVAL_STRATEGY_PATH.exists() and EVAL_TEMPLATE_PATH.exists()
            else "Restore docs/reference/eval-strategy.md and studio/docs/templates/eval-plan.md.",
        )
    )
    checks.append(
        make_check(
            "research-notes",
            "pass" if RESEARCH_NOTES_PATH.exists() else "warn",
            "Research-backed Codex infrastructure notes are present."
            if RESEARCH_NOTES_PATH.exists()
            else "Research notes are missing.",
            next_step=None if RESEARCH_NOTES_PATH.exists() else "Restore docs/research/openai-codex-infra-findings.md.",
        )
    )
    checks.append(
        make_check(
            "reviewer-agent",
            "pass" if REVIEWER_AGENT_PATH.exists() else "warn",
            "Focused reviewer agent is present." if REVIEWER_AGENT_PATH.exists() else "Focused reviewer agent is missing.",
            next_step=None if REVIEWER_AGENT_PATH.exists() else "Restore .codex/agents/reviewer.toml for narrow review passes.",
        )
    )
    checks.append(
        make_check(
            "starter-kits",
            "pass" if STARTER_KITS_PATH.exists() and len(available_starter_kits()) >= 3 else "warn",
            f"Starter-kit parity surface is present for: {', '.join(available_starter_kits())}."
            if STARTER_KITS_PATH.exists() and len(available_starter_kits()) >= 3
            else "Starter-kit parity surface is incomplete.",
            next_step=None if STARTER_KITS_PATH.exists() and len(available_starter_kits()) >= 3 else "Restore studio/starter-kits/ with Godot, Unity, and Unreal manifests.",
        )
    )
    checks.append(
        make_check(
            "layered-checklists",
            "pass" if CHECKLISTS_PATH.exists() else "warn",
            "Layered checklist manifests are present." if CHECKLISTS_PATH.exists() else "Layered checklist manifests are missing.",
            next_step=None if CHECKLISTS_PATH.exists() else "Restore studio/checklists/ and its manifests.",
        )
    )
    checks.append(
        make_check(
            "genre-quickstart",
            "pass" if GENRE_REFERENCE_PATH.exists() and GENRE_TEMPLATE_PATH.exists() and START_SCRIPT_PATH.exists() else "warn",
            "Genre quickstart docs, template, and wizard are present."
            if GENRE_REFERENCE_PATH.exists() and GENRE_TEMPLATE_PATH.exists() and START_SCRIPT_PATH.exists()
            else "Genre quickstart surface is incomplete.",
            next_step=None
            if GENRE_REFERENCE_PATH.exists() and GENRE_TEMPLATE_PATH.exists() and START_SCRIPT_PATH.exists()
            else "Restore docs/reference/genre-presets.md, studio/docs/templates/genre-starter.md, and scripts/start_game_studio.py.",
        )
    )
    checks.append(
        make_check(
            "community-health",
            "pass" if CODEOWNERS_PATH.exists() and all(path.exists() for path in COMMUNITY_FILES) and all(path.exists() for path in ISSUE_TEMPLATE_FILES) else "warn",
            "Community health files, CODEOWNERS, and issue templates are present."
            if CODEOWNERS_PATH.exists() and all(path.exists() for path in COMMUNITY_FILES) and all(path.exists() for path in ISSUE_TEMPLATE_FILES)
            else "Community health surface is incomplete.",
            next_step=None
            if CODEOWNERS_PATH.exists() and all(path.exists() for path in COMMUNITY_FILES) and all(path.exists() for path in ISSUE_TEMPLATE_FILES)
            else "Restore CODEOWNERS, issue templates, and the root community policy files.",
        )
    )
    checks.append(
        make_check(
            "github-automation",
            "pass" if WORKFLOWS_DIR.exists() and (WORKFLOWS_DIR / "repo-validate.yml").exists() and (WORKFLOWS_DIR / "docker-smoke.yml").exists() else "warn",
            "GitHub workflows are present."
            if WORKFLOWS_DIR.exists() and (WORKFLOWS_DIR / "repo-validate.yml").exists() and (WORKFLOWS_DIR / "docker-smoke.yml").exists()
            else "GitHub automation workflows are missing.",
            next_step=None
            if WORKFLOWS_DIR.exists() and (WORKFLOWS_DIR / "repo-validate.yml").exists() and (WORKFLOWS_DIR / "docker-smoke.yml").exists()
            else "Restore .github/workflows/repo-validate.yml and .github/workflows/docker-smoke.yml.",
        )
    )
    checks.append(
        make_check(
            "local-evals",
            "pass" if LOCAL_EVALS_PATH.exists() and EVALS_DIR.exists() and ENGINE_KIT_VALIDATOR_PATH.exists() else "warn",
            "Local eval runner, fixtures, and engine-kit validator are present."
            if LOCAL_EVALS_PATH.exists() and EVALS_DIR.exists() and ENGINE_KIT_VALIDATOR_PATH.exists()
            else "Local eval runner, fixtures, or engine-kit validator are missing.",
            next_step=None if LOCAL_EVALS_PATH.exists() and EVALS_DIR.exists() and ENGINE_KIT_VALIDATOR_PATH.exists() else "Restore scripts/run_local_evals.py, scripts/validate_engine_kits.py, and the evals/ directory.",
        )
    )
    checks.append(
        make_check(
            "workflow-validator",
            "pass" if WORKFLOW_VALIDATOR_PATH.exists() else "warn",
            "Workflow validator script is present." if WORKFLOW_VALIDATOR_PATH.exists() else "Workflow validator script is missing.",
            next_step=None if WORKFLOW_VALIDATOR_PATH.exists() else "Restore scripts/validate_workflows.py.",
        )
    )
    checks.append(
        make_check(
            "ci-reporting",
            "pass" if CI_ARTIFACT_REPORT_PATH.exists() and STARTER_KIT_SMOKE_PATH.exists() and CI_CD_ARCHITECTURE_DOC_PATH.exists() else "warn",
            "CI artifact reporting, starter-kit smoke, and CI/CD docs are present."
            if CI_ARTIFACT_REPORT_PATH.exists() and STARTER_KIT_SMOKE_PATH.exists() and CI_CD_ARCHITECTURE_DOC_PATH.exists()
            else "CI/CD reporting surface is incomplete.",
            next_step=None
            if CI_ARTIFACT_REPORT_PATH.exists() and STARTER_KIT_SMOKE_PATH.exists() and CI_CD_ARCHITECTURE_DOC_PATH.exists()
            else "Restore scripts/ci_artifact_report.py, scripts/starter_kit_contract_smoke.py, and docs/reference/ci-cd-architecture.md.",
        )
    )
    checks.append(
        make_check(
            "engine-adapters",
            "pass" if UNITY_ADAPTER_PATH.exists() and UNREAL_ADAPTER_PATH.exists() else "warn",
            "Unity and Unreal adapter scripts are present."
            if UNITY_ADAPTER_PATH.exists() and UNREAL_ADAPTER_PATH.exists()
            else "Unity or Unreal adapter script is missing.",
            next_step=None if UNITY_ADAPTER_PATH.exists() and UNREAL_ADAPTER_PATH.exists() else "Restore scripts/unity_adapter.py and scripts/unreal_adapter.py.",
        )
    )
    checks.append(
        make_check(
            "env-surface",
            "pass" if ENV_EXAMPLE_PATH.exists() and SECRETS_DOC_PATH.exists() else "warn",
            "Environment template and secrets doc are present." if ENV_EXAMPLE_PATH.exists() and SECRETS_DOC_PATH.exists() else "Secrets/environment setup surface is incomplete.",
            next_step=None if ENV_EXAMPLE_PATH.exists() and SECRETS_DOC_PATH.exists() else "Restore .env.example and docs/setup/secrets-and-env.md.",
        )
    )
    checks.append(
        make_check(
            "codex-compatibility",
            "pass" if CODEX_COMPAT_DOC_PATH.exists() and BASELINE_SCRIPT_PATH.exists() else "warn",
            "Codex compatibility doc and baseline seeding script are present."
            if CODEX_COMPAT_DOC_PATH.exists() and BASELINE_SCRIPT_PATH.exists()
            else "Codex compatibility surface is incomplete.",
            next_step=None if CODEX_COMPAT_DOC_PATH.exists() and BASELINE_SCRIPT_PATH.exists() else "Restore docs/reference/codex-compatibility.md and scripts/seed_project_baseline.py.",
        )
    )
    research_files = research_notes()
    research_failures: list[str] = []
    for note in research_files:
        research_failures.extend(validate_research_note(note))
    checks.append(
        make_check(
            "research-knowledge-base",
            "pass" if RESEARCH_KB_PATH.exists() and not research_failures else "warn",
            f"Research knowledge base is present with {len(research_files)} notes."
            if RESEARCH_KB_PATH.exists() and not research_failures
            else "Research knowledge base is missing or notes are incomplete.",
            next_step=None if RESEARCH_KB_PATH.exists() and not research_failures else "Restore docs/research/game-development and ensure notes include the required sections and source links.",
        )
    )

    git_path = shutil.which("git")
    if git_path:
        checks.append(make_check("git", "pass", f"Git found at {git_path}."))
    else:
        checks.append(make_check("git", "warn", "Git is not installed or not on PATH.", next_step="Install Git if you want version control and hooks."))

    git_dir = REPO_ROOT / ".git"
    if git_dir.exists():
        hooks_dir = git_dir / "hooks"
        missing_hooks = [name for name in HOOKS if not (hooks_dir / name).exists()]
        if missing_hooks:
            checks.append(make_check("git-hooks", "warn", f"Repo is initialized, but hooks are missing: {', '.join(missing_hooks)}.", next_step="Run ./scripts/install_git_hooks.sh"))
        else:
            checks.append(make_check("git-hooks", "pass", "Recommended git hooks are installed."))

        remote_result = subprocess.run(
            ["git", "remote"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        remotes = [line.strip() for line in remote_result.stdout.splitlines() if line.strip()]
        checks.append(
            make_check(
                "git-remote",
                "pass" if remotes else "warn",
                f"Configured git remotes: {', '.join(remotes)}." if remotes else "No git remote is configured yet.",
                next_step=None if remotes else "Create the GitHub repo, then run git remote add origin <url> and push main.",
            )
        )

        history_result = subprocess.run(
            ["git", "rev-parse", "--verify", "HEAD"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        checks.append(
            make_check(
                "git-history",
                "pass" if history_result.returncode == 0 else "warn",
                "Git history exists locally." if history_result.returncode == 0 else "No commit exists yet on this repository.",
                next_step=None if history_result.returncode == 0 else "Create the first commit after reviewing the current baseline.",
            )
        )
    else:
        checks.append(make_check("git-hooks", "warn", "No .git directory detected; hooks were not installed.", next_step="Initialize git or rerun setup later with hooks enabled."))

    node_path = shutil.which("node")
    checks.append(
        make_check(
            "node",
            "pass" if node_path else "warn",
            f"Node found at {node_path}." if node_path else "Node.js not found.",
            next_step=None if node_path else "Install Node.js if you plan to install the Codex CLI locally.",
        )
    )

    codex_path = shutil.which("codex")
    checks.append(
        make_check(
            "codex-cli",
            "pass" if codex_path else "warn",
            f"Codex CLI found at {codex_path}." if codex_path else "Codex CLI not found on PATH.",
            next_step=None if codex_path else "Install with: npm i -g @openai/codex",
        )
    )

    docker_requested = (REPO_ROOT / "Dockerfile").exists() and (REPO_ROOT / "docker-compose.yml").exists()
    docker_path = shutil.which("docker")
    if docker_requested:
        checks.append(
            make_check(
                "docker",
                "pass" if docker_path else "warn",
                f"Docker found at {docker_path}." if docker_path else "Docker workflow files exist, but Docker is not installed.",
                next_step=None if docker_path else "Install Docker if you want the optional isolated helper environment.",
            )
        )

    config = load_root_studio_config()
    project = config.get("project", {}) if isinstance(config.get("project"), dict) else {}
    supported_engines = [str(item) for item in project.get("supported_engines", [])] if isinstance(project.get("supported_engines"), list) else []

    if "unity-6" in supported_engines:
        unity_cli = find_unity_cli()
        unity_hub = find_unity_hub()
        if unity_cli:
            checks.append(make_check("unity-cli", "pass", f"Unity editor CLI found at {unity_cli}."))
        elif unity_hub:
            checks.append(
                make_check(
                    "unity-cli",
                    "warn",
                    f"Unity Hub is installed at {unity_hub}, but no Unity editor CLI is configured.",
                    next_step="Install a Unity editor version and set UNITY_CLI or tools.unity_cli in studio.toml for engine-backed validation.",
                )
            )
        else:
            checks.append(
                make_check(
                    "unity-cli",
                    "warn",
                    "No Unity editor CLI found.",
                    next_step="Install Unity via Unity Hub and set UNITY_CLI or tools.unity_cli in studio.toml for engine-backed validation.",
                )
            )

    if "unreal-5" in supported_engines:
        unreal_uat = find_unreal_uat()
        unreal_editor = find_unreal_editor()
        if unreal_uat:
            checks.append(make_check("unreal-cli", "pass", f"Unreal UAT found at {unreal_uat}."))
        elif unreal_editor:
            checks.append(
                make_check(
                    "unreal-cli",
                    "warn",
                    f"Unreal editor found at {unreal_editor}, but RunUAT was not resolved.",
                    next_step="Set UNREAL_UAT or tools.unreal_uat in studio.toml so packaging validation can run reliably.",
                )
            )
        else:
            checks.append(
                make_check(
                    "unreal-cli",
                    "warn",
                    "No Unreal editor or UAT install found.",
                    next_step="Install Unreal Engine and set UNREAL_UAT or UNREAL_EDITOR for engine-backed packaging validation.",
                )
            )

    engine_report = engine_detection_report()
    engine = str(engine_report["resolved_engine"])
    engine_detail = f"Resolved engine: {engine} via {engine_report['source']}."
    if engine_report["configured_slug"]:
        engine_detail = f"Primary engine: {engine_report['configured_slug']} -> {engine}. Source: {engine_report['source']}."
    if engine_report["mismatch"]:
        engine_detail += f" Repo clues still look like {engine_report['clue_engine']}."
    checks.append(
        make_check(
            "engine-detection",
            "pass" if engine != "unknown" and not engine_report["mismatch"] else "warn",
            engine_detail if engine != "unknown" else "Engine is still unknown from studio.toml and repo clues.",
            next_step=None if engine != "unknown" and not engine_report["mismatch"] else "Align studio.toml with the real primary engine or remove stale engine-native files that now act as misleading clues.",
        )
    )

    if engine == "godot":
        if GODOT_SMOKE_SCRIPT_PATH.exists():
            smoke_result = subprocess.run(
                [sys.executable, str(GODOT_SMOKE_SCRIPT_PATH), "--json", "--static-only"],
                cwd=REPO_ROOT,
                check=False,
                capture_output=True,
                text=True,
            )
            if smoke_result.returncode == 0:
                checks.append(make_check("godot-static-smoke", "pass", "Godot scene, scripts, and export presets pass static smoke checks."))
            else:
                detail = smoke_result.stderr.strip() or smoke_result.stdout.strip() or "Static smoke failed."
                checks.append(make_check("godot-static-smoke", "fail", detail, required=True, next_step="Fix the Godot slice files or rerun scripts/godot_smoke.py --json --static-only for details."))
        else:
            checks.append(make_check("godot-static-smoke", "warn", "Godot smoke script is missing.", next_step="Restore scripts/godot_smoke.py."))

        export_surface_ready = GODOT_EXPORT_PRESETS_PATH.exists() and GODOT_EXPORT_SCRIPT_PATH.exists()
        checks.append(
            make_check(
                "godot-export-surface",
                "pass" if export_surface_ready else "warn",
                "Godot export presets and helper script are present." if export_surface_ready else "Godot export surface is incomplete.",
                next_step=None if export_surface_ready else "Restore export_presets.cfg and scripts/godot_export.py.",
            )
        )

        godot_bin = find_godot_binary()
        checks.append(
            make_check(
                "godot-cli",
                "pass" if godot_bin else "warn",
                f"Godot binary found at {godot_bin}." if godot_bin else "No local Godot binary found.",
                next_step=None if godot_bin else "Install Godot 4.x locally or set GODOT_BIN to run runtime smoke and export commands.",
            )
        )

    doc_errors, doc_warnings = collect_doc_findings()
    if doc_errors:
        checks.append(
            make_check(
                "active-doc-quality",
                "warn",
                f"Active docs have semantic issues: {doc_errors[0]}",
                next_step="Run python3 scripts/validate_docs.py and resolve stale titles, template text, or unresolved QA notes.",
            )
        )
    elif doc_warnings:
        checks.append(
            make_check(
                "active-doc-quality",
                "warn",
                f"Active docs have warnings: {doc_warnings[0]}",
                next_step="Resolve remaining placeholder warnings and rerun validate_docs.py.",
            )
        )
    else:
        checks.append(make_check("active-doc-quality", "pass", "Active docs match the configured project identity and contain no template-default text."))

    readme_heading = REPO_ROOT.joinpath("README.md").read_text(encoding="utf-8").splitlines()[0].strip() if (REPO_ROOT / "README.md").exists() else ""
    project_name = configured_project_name(REPO_ROOT.name)
    identity_status = "pass" if project_name in readme_heading else "warn"
    identity_detail = (
        f"README and studio.toml agree on project identity: {project_name}."
        if identity_status == "pass"
        else f"README heading does not reflect the configured project name '{project_name}'."
    )
    checks.append(
        make_check(
            "project-identity",
            identity_status,
            identity_detail,
            next_step=None if identity_status == "pass" else "Align README and active docs with studio.toml so the repo has one authoritative identity.",
        )
    )

    codex_config = load_project_config()
    agents_config = codex_config.get("agents", {}) if isinstance(codex_config.get("agents"), dict) else {}
    features_config = codex_config.get("features", {}) if isinstance(codex_config.get("features"), dict) else {}
    max_depth = agents_config.get("max_depth")
    if isinstance(max_depth, int):
        if max_depth <= 1:
            checks.append(make_check("agent-depth", "pass", f"agents.max_depth is {max_depth}, matching the conservative default."))
        else:
            checks.append(
                make_check(
                    "agent-depth",
                    "warn",
                    f"agents.max_depth is {max_depth}; deeper recursive delegation can be expensive and harder to predict.",
                    next_step="Prefer max_depth = 1 unless a documented workflow truly needs recursive delegation.",
                )
            )

    root_agents_lines = ROOT_AGENTS_PATH.read_text(encoding="utf-8").splitlines() if ROOT_AGENTS_PATH.exists() else []
    if root_agents_lines:
        if len(root_agents_lines) <= AGENTS_LINE_WARN_THRESHOLD:
            checks.append(make_check("root-agents-size", "pass", f"AGENTS.md is {len(root_agents_lines)} lines, still reasonably compact."))
        else:
            checks.append(
                make_check(
                    "root-agents-size",
                    "warn",
                    f"AGENTS.md is {len(root_agents_lines)} lines; root instructions may be getting too large.",
                    next_step="Move detailed checklists into docs/reference/ or studio/docs/active/ and keep AGENTS.md focused on stable routing rules.",
                )
            )

    hooks_enabled = features_config.get("codex_hooks")
    if HOOKS_CONFIG_PATH.exists():
        if hooks_enabled is True:
            checks.append(make_check("codex-hooks", "pass", "Optional Codex hooks are installed and enabled."))
        else:
            checks.append(make_check("codex-hooks", "pass", "Optional Codex hooks are installed and disabled by default.", next_step="Run python3 scripts/toggle_codex_hooks.py --enable if you want to opt in."))
    else:
        checks.append(make_check("codex-hooks", "warn", "Optional Codex hooks config is missing.", next_step="Restore .codex/hooks.json and scripts/hooks/ if you want repo-local hook support."))

    summary = repo_summary()
    payload = {"summary": summary, "checks": checks}

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print("Repo Doctor")
        print("===========")
        for check in checks:
            status = str(check["status"]).upper()
            print(f"[{status}] {check['name']}: {check['detail']}")
            if check.get("next_step"):
                print(f"  Next: {check['next_step']}")
        print()
        print("Summary")
        for key, value in summary.items():
            print(f"- {key}: {value}")

    failures = [check for check in checks if check["status"] == "fail"]
    warnings = [check for check in checks if check["status"] == "warn"]
    if failures or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
