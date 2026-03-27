#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

from _studio_common import REPO_ROOT

REQUIRED_PATHS = [
    "AGENTS.md",
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "SUPPORT.md",
    "CODE_OF_CONDUCT.md",
    ".env.example",
    "Makefile",
    ".github",
    ".github/CODEOWNERS",
    ".github/ISSUE_TEMPLATE",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/bug-report.yml",
    ".github/ISSUE_TEMPLATE/feature-request.yml",
    ".github/ISSUE_TEMPLATE/infra-routing-change.yml",
    ".github/ISSUE_TEMPLATE/genre-preset-update.yml",
    ".github/pull_request_template.md",
    ".github/workflows",
    ".github/workflows/repo-validate.yml",
    ".github/workflows/docker-smoke.yml",
    ".github/dependabot.yml",
    "export_presets.cfg",
    ".codex/config.toml",
    ".codex/hooks.json",
    ".codex/agents",
    ".codex/agents/reviewer.toml",
    ".agents/skills",
    "docs/README.md",
    "docs/setup",
    "docs/setup/github-maintainer-setup.md",
    "docs/setup/optional-codex-hooks.md",
    "docs/setup/secrets-and-env.md",
    "docs/reference",
    "docs/reference/code-review.md",
    "docs/reference/codex-compatibility.md",
    "docs/reference/eval-strategy.md",
    "docs/reference/genre-presets.md",
    "docs/research",
    "docs/research/openai-codex-infra-findings.md",
    "evals",
    "evals/doctor_surface/required_checks.json",
    "evals/godot_surface/expectations.json",
    "evals/route_task/cases.json",
    "evals/genre_guidance/cases.json",
    "scripts",
    "scripts/hooks",
    "scripts/godot_export.py",
    "scripts/godot_smoke.py",
    "scripts/hooks/pre_tool_use_policy.py",
    "scripts/hooks/session_start_context.py",
    "scripts/run_local_evals.py",
    "scripts/seed_project_baseline.py",
    "scripts/toggle_codex_hooks.py",
    "scripts/start_game_studio.py",
    "scripts/scaffold_eval_plan.py",
    "studio/docs/templates",
    "studio/docs/templates/eval-plan.md",
    "studio/docs/templates/genre-starter.md",
    "studio/docs/active",
    "src",
    "tests",
    "tests/test_godot_surface.py",
    "assets",
    "prototypes",
    "tools",
]

def main() -> int:
    missing = []
    for rel in REQUIRED_PATHS:
        path = REPO_ROOT / rel
        if not path.exists():
            missing.append(rel)
    if missing:
        for rel in missing:
            print(f"ERROR: Missing path: {rel}")
        return 1
    print("Repo layout validation passed.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
