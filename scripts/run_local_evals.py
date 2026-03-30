#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from _studio_common import REPO_ROOT, build_genre_replacements
from studio_core import resolve_checklists, research_notes, validate_research_note

EVALS_DIR = REPO_ROOT / "evals"
UNITY_STUB = REPO_ROOT / "tools" / "engine-stubs" / "unity" / "Unity"
UNREAL_STUB = REPO_ROOT / "tools" / "engine-stubs" / "unreal" / "RunUAT.sh"


def load_cases(path: Path) -> list[dict[str, object]]:
    return json.loads(path.read_text(encoding="utf-8"))


def run_route_task_eval() -> list[str]:
    failures: list[str] = []
    cases = load_cases(EVALS_DIR / "route_task" / "cases.json")
    script = REPO_ROOT / "scripts" / "route_task.py"

    for case in cases:
        result = subprocess.run(
            [sys.executable, str(script), str(case["task"]), "--json"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            failures.append(f"route_task failed for case '{case['task']}': {result.stderr.strip()}")
            continue

        payload = json.loads(result.stdout)
        if payload.get("route") != case["expected_route"]:
            failures.append(
                f"route_task route mismatch for '{case['task']}': expected {case['expected_route']}, got {payload.get('route')}"
            )
        for skill in case.get("expected_skills", []):
            if skill not in payload.get("skills", []):
                failures.append(f"route_task missing skill '{skill}' for '{case['task']}'")
        for doc in case.get("expected_docs", []):
            if doc not in payload.get("docs", []):
                failures.append(f"route_task missing doc '{doc}' for '{case['task']}'")

    return failures


def run_genre_guidance_eval() -> list[str]:
    failures: list[str] = []
    cases = load_cases(EVALS_DIR / "genre_guidance" / "cases.json")

    for case in cases:
        payload = build_genre_replacements(str(case["genre"]))
        if payload.get("GENRE_NAME") != case["expected_name"]:
            failures.append(
                f"genre guidance name mismatch for '{case['genre']}': expected {case['expected_name']}, got {payload.get('GENRE_NAME')}"
            )
        if payload.get("GENRE_FIRST_FEATURE") != case["expected_first_feature"]:
            failures.append(
                f"genre guidance first feature mismatch for '{case['genre']}': expected {case['expected_first_feature']}, got {payload.get('GENRE_FIRST_FEATURE')}"
            )
        if not str(payload.get("GENRE_MATURITY", "")).endswith("genre-maturity.md"):
            failures.append(f"genre guidance missing advanced framework guide for '{case['genre']}'")
        skills_block = str(payload.get("GENRE_SKILLS", ""))
        for skill in case.get("required_skills", []):
            if skill not in skills_block:
                failures.append(f"genre guidance missing skill '{skill}' for '{case['genre']}'")

    return failures


def run_doctor_surface_eval() -> list[str]:
    failures: list[str] = []
    required_checks = load_cases(EVALS_DIR / "doctor_surface" / "required_checks.json")
    script = REPO_ROOT / "scripts" / "doctor.py"

    result = subprocess.run(
        [sys.executable, str(script), "--json"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        failures.append(f"doctor failed during eval: {result.stderr.strip()}")
        return failures

    payload = json.loads(result.stdout)
    check_names = {check["name"] for check in payload.get("checks", [])}
    for name in required_checks:
        if name not in check_names:
            failures.append(f"doctor surface missing check '{name}'")

    return failures


def run_engine_kits_eval() -> list[str]:
    failures: list[str] = []
    script = REPO_ROOT / "scripts" / "validate_engine_kits.py"
    result = subprocess.run(
        [sys.executable, str(script), "--json"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        payload = json.loads(result.stdout or "{}")
        for engine, items in payload.items():
            for item in items:
                failures.append(item)
    return failures


def run_workflow_surface_eval() -> list[str]:
    failures: list[str] = []
    expected = load_cases(EVALS_DIR / "workflow_surface" / "expected_workflows.json")
    script = REPO_ROOT / "scripts" / "validate_workflows.py"
    result = subprocess.run(
        [sys.executable, str(script), "--json"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        payload = json.loads(result.stdout or "{}")
        failures.extend(payload.get("failures", []))
        return failures

    payload = json.loads(result.stdout)
    summaries = payload.get("workflows", {})
    for workflow_name, expected_jobs in expected.items():
        if workflow_name not in summaries:
            failures.append(f"workflow surface missing '{workflow_name}'")
            continue
        actual_jobs = set(summaries[workflow_name].get("jobs", []))
        missing_jobs = sorted(set(expected_jobs) - actual_jobs)
        if missing_jobs:
            failures.append(f"{workflow_name} missing expected jobs: {', '.join(missing_jobs)}")
    return failures


def run_checklist_eval() -> list[str]:
    failures: list[str] = []
    gameplay_items = resolve_checklists(engine_slug="godot-4", disciplines=["gameplay"], milestone="prototype", agent_name="gameplay_programmer")
    gameplay_ids = {item["id"] for item in gameplay_items}
    for required in ("repo-health-doctor", "gameplay-readability", "prototype-proves-core-loop"):
        if required not in gameplay_ids:
            failures.append(f"resolved checklist bundle is missing '{required}'")

    engine_eval_items = resolve_checklists(engine_slug="unity-6", disciplines=["engine_eval"], milestone="prototype", agent_name="technical_director")
    engine_eval_ids = {item["id"] for item in engine_eval_items}
    for required in (
        "engine-source-hierarchy",
        "engine-family-split",
        "engine-build-contract",
        "engine-test-contract",
        "engine-performance-baseline",
        "engine-toolchain-readiness",
        "engine-scorecard-artifact",
        "engine-doc-sync",
    ):
        if required not in engine_eval_ids:
            failures.append(f"resolved engine eval bundle is missing '{required}'")
    for required in ("ci-short-names", "benchmark-family", "quality-owner", "quality-process", "perf-first-lever", "research-primary-sources"):
        if required not in engine_eval_ids:
            failures.append(f"resolved engine eval support bundle is missing '{required}'")

    engine_fit_items = resolve_checklists(engine_slug="unity-6", disciplines=["engine_fit"], milestone="prototype", agent_name="technical_director")
    engine_fit_ids = {item["id"] for item in engine_fit_items}
    for required in (
        "engine-profile-named",
        "engine-language-fit",
        "engine-collaboration-fit",
        "engine-platform-fit",
        "engine-tooling-fit",
        "engine-proof-path",
        "engine-tradeoff-matrix",
        "engine-doc-sync",
    ):
        if required not in engine_fit_ids:
            failures.append(f"resolved engine fit bundle is missing '{required}'")
    for required in ("research-primary-sources", "research-repo-impact"):
        if required not in engine_fit_ids:
            failures.append(f"resolved engine fit support bundle is missing '{required}'")

    custom_items = resolve_checklists(engine_slug="unity-6", disciplines=["custom"], milestone="prototype", agent_name="technical_director")
    custom_ids = {item["id"] for item in custom_items}
    for required in ("custom-intake", "custom-owner", "custom-rulepack", "custom-validation", "custom-doc-sync"):
        if required not in custom_ids:
            failures.append(f"resolved custom checklist bundle is missing '{required}'")
    if not any(item["source"].endswith("studio/checklists/discipline/custom.toml") for item in custom_items):
        failures.append("resolved custom checklist bundle missing source 'studio/checklists/discipline/custom.toml'")

    extension_items = resolve_checklists(engine_slug="unity-6", disciplines=["extensions"], milestone="prototype", agent_name="technical_director")
    extension_ids = {item["id"] for item in extension_items}
    for required in ("extension-intake", "extension-manifest", "extension-boundary", "extension-validation", "extension-doc-sync"):
        if required not in extension_ids:
            failures.append(f"resolved extensions checklist bundle is missing '{required}'")
    if not any(item["source"].endswith("studio/checklists/discipline/extensions.toml") for item in extension_items):
        failures.append("resolved extensions checklist bundle missing source 'studio/checklists/discipline/extensions.toml'")

    theory_items = resolve_checklists(engine_slug="unity-6", disciplines=["theory"], milestone="prototype", agent_name="game_designer")
    theory_ids = {item["id"] for item in theory_items}
    for required in ("theory-outcome", "theory-lens-stack", "theory-evidence", "theory-boundary", "theory-validation", "theory-doc-sync"):
        if required not in theory_ids:
            failures.append(f"resolved theory checklist bundle is missing '{required}'")
    if not any(item["source"].endswith("studio/checklists/discipline/theory.toml") for item in theory_items):
        failures.append("resolved theory checklist bundle missing source 'studio/checklists/discipline/theory.toml'")

    role_cases = [
        ("producer", {"producer-summary", "producer-scope", "producer-handoffs", "producer-risk"}, "studio/checklists/discipline/producer.toml"),
        ("technical_director", {"tech-boundary", "tech-feasibility", "tech-tradeoff", "tech-validation"}, "studio/checklists/discipline/technical_director.toml"),
        ("qa_lead", {"qa-criteria", "qa-matrix", "qa-go-no-go", "qa-evidence"}, "studio/checklists/discipline/qa_lead.toml"),
        ("release_manager", {"release-freeze", "release-artifacts", "release-rollback", "release-note"}, "studio/checklists/discipline/release_manager.toml"),
        ("build_release_engineer", {"build-deterministic", "build-env", "build-artifacts", "build-smoke"}, "studio/checklists/discipline/build_release_engineer.toml"),
        ("docs_researcher", {"research-primary", "research-claims", "research-note", "research-implication"}, "studio/checklists/discipline/docs_researcher.toml"),
        ("performance_analyst", {"perf-baseline", "perf-budget", "perf-first-lever", "perf-fallback"}, "studio/checklists/discipline/performance_analyst.toml"),
        ("engine_programmer", {"engine-owner", "engine-toolchain", "engine-class", "engine-smoke"}, "studio/checklists/discipline/engine_programmer.toml"),
        ("gameplay_programmer", {"gameplay-owner", "gameplay-slice", "gameplay-state", "gameplay-validation"}, "studio/checklists/discipline/gameplay_programmer.toml"),
        ("game_designer", {"design-outcome", "design-loop", "design-pacing", "design-validation"}, "studio/checklists/discipline/game_designer.toml"),
        ("ui_programmer", {"ui-screen-flow", "ui-projection", "ui-accessibility", "ui-validation"}, "studio/checklists/discipline/ui_programmer.toml"),
        ("narrative_director", {"narrative-beat", "narrative-branch", "narrative-graph", "narrative-validation"}, "studio/checklists/discipline/narrative_director.toml"),
        ("art_director", {"art-pillars", "art-readability", "art-pipeline", "art-validation"}, "studio/checklists/discipline/art_director.toml"),
        ("audio_director", {"audio-pillars", "audio-mix", "audio-implementation", "audio-validation"}, "studio/checklists/discipline/audio_director.toml"),
    ]
    for role, required_ids, source_suffix in role_cases:
        items = resolve_checklists(engine_slug="unity-6", disciplines=[role], milestone="prototype", agent_name=role)
        item_ids = {item["id"] for item in items}
        for required in required_ids:
            if required not in item_ids:
                failures.append(f"resolved {role} checklist bundle is missing '{required}'")
        if not any(item["source"].endswith(source_suffix) for item in items):
            failures.append(f"resolved {role} checklist bundle missing source '{source_suffix}'")

    versioning_items = resolve_checklists(engine_slug="unity-6", disciplines=["versioning"], milestone="release", agent_name="release_manager")
    versioning_ids = {item["id"] for item in versioning_items}
    for required in ("version-source", "version-changelog", "version-tag", "version-artifact", "version-doc-sync", "version-commit"):
        if required not in versioning_ids:
            failures.append(f"resolved versioning checklist bundle is missing '{required}'")
    if not any(item["source"].endswith("studio/checklists/discipline/versioning.toml") for item in versioning_items):
        failures.append("resolved versioning checklist bundle missing source 'studio/checklists/discipline/versioning.toml'")
    return failures


def run_engine_adapter_eval() -> list[str]:
    failures: list[str] = []
    cases = [
        (
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "unity_adapter.py"),
                "test",
                "--project-path",
                str(REPO_ROOT / "studio" / "starter-kits" / "unity-6" / "scaffold"),
                "--unity-path",
                str(UNITY_STUB),
                "--dry-run",
                "--json",
            ],
            "-runTests",
        ),
        (
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "unreal_adapter.py"),
                "package",
                "--project-path",
                str(REPO_ROOT / "studio" / "starter-kits" / "unreal-5" / "scaffold"),
                "--uat-path",
                str(UNREAL_STUB),
                "--dry-run",
                "--json",
            ],
            "BuildCookRun",
        ),
    ]
    for command, expected_token in cases:
        result = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        if result.returncode != 0:
            failures.append(f"engine adapter dry-run failed: {' '.join(command[1:3])}")
            continue
        payload = json.loads(result.stdout)
        joined = " ".join(payload.get("command", []))
        if expected_token not in joined:
            failures.append(f"engine adapter command missing expected token '{expected_token}'")
        if payload.get("validation_failures"):
            failures.append(f"engine adapter reported unexpected validation failures: {payload['validation_failures']}")
    return failures


def run_agent_metadata_eval() -> list[str]:
    failures: list[str] = []
    script = REPO_ROOT / "scripts" / "validate_agent_metadata.py"
    result = subprocess.run(
        [sys.executable, str(script), "--json"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        payload = json.loads(result.stdout or "{}")
        failures.extend(payload.get("errors", []))
    return failures


def run_route_task_engine_eval() -> list[str]:
    failures: list[str] = []
    cases = [
        ("Plan the next Unity starter kit task", "engine / tooling / packaging", "unity-6"),
        ("Plan the next UE5 packaging task", "engine / tooling / packaging", "unreal-5"),
        ("Implement Unity combat room", "combat / gameplay", "unity-6"),
        ("Compare Unity 6 and Unreal 5 in an engine evaluation scorecard for build, test, performance, and toolchain readiness", "engine / evaluation / scorecard", "unity-6"),
    ]
    script = REPO_ROOT / "scripts" / "route_task.py"
    for task, expected_route, expected_engine in cases:
        result = subprocess.run([sys.executable, str(script), task, "--json"], cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        if result.returncode != 0:
            failures.append(f"route_task failed for '{task}'")
            continue
        payload = json.loads(result.stdout)
        if payload.get("route") != expected_route:
            failures.append(f"route_task route mismatch for '{task}': expected {expected_route}, got {payload.get('route')}")
        if payload.get("engine_kit", {}).get("id") != expected_engine:
            failures.append(f"route_task engine mismatch for '{task}': expected {expected_engine}, got {payload.get('engine_kit', {}).get('id')}")
    return failures


def run_route_task_engine_fit() -> list[str]:
    failures: list[str] = []
    cases = [
        ("Which engine fits a beginner solo developer building a small 2D game in Godot 4?", "engine / developer fit / recommendation", "godot-4"),
        ("Which engine fits a C# tools-heavy team building a simulation in Unity 6?", "engine / developer fit / recommendation", "unity-6"),
        ("Which engine fits a designer-first Blueprint-heavy team in Unreal 5?", "engine / developer fit / recommendation", "unreal-5"),
    ]
    script = REPO_ROOT / "scripts" / "route_task.py"
    for task, expected_route, expected_engine in cases:
        result = subprocess.run([sys.executable, str(script), task, "--json"], cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        if result.returncode != 0:
            failures.append(f"route_task failed for '{task}'")
            continue
        payload = json.loads(result.stdout)
        if payload.get("route") != expected_route:
            failures.append(f"route_task route mismatch for '{task}': expected {expected_route}, got {payload.get('route')}")
        if payload.get("engine_kit", {}).get("id") != expected_engine:
            failures.append(f"route_task engine mismatch for '{task}': expected {expected_engine}, got {payload.get('engine_kit', {}).get('id')}")
        docs = set(payload.get("docs", []))
        for required in (
            "docs/reference/engine-fit.md",
            "docs/examples/engine-fit-example.md",
            "docs/research/game-development/foundations/engine-fit.md",
            "studio/checklists/discipline/engine_fit.toml",
            "studio/docs/active/engine-fit.md",
            "studio/docs/active/eval-engine-fit.md",
        ):
            if required not in docs:
                failures.append(f"route_task missing doc '{required}' for '{task}'")
    return failures


def run_research_surface_eval() -> list[str]:
    failures: list[str] = []
    notes = research_notes()
    if not notes:
        failures.append("research knowledge base has no notes")
        return failures
    for note in notes:
        failures.extend(validate_research_note(note))
    return failures


def run_ci_report_eval() -> list[str]:
    failures: list[str] = []
    script = REPO_ROOT / "scripts" / "ci_artifact_report.py"
    output_dir = REPO_ROOT / "build" / "ci" / "eval"
    result = subprocess.run(
        [sys.executable, str(script), "--output-dir", str(output_dir), "--json"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        failures.append(f"ci_artifact_report failed during eval: {result.stderr.strip() or result.stdout.strip()}")
        return failures
    payload = json.loads(result.stdout)
    for key in ("json", "markdown"):
        path = Path(payload[key])
        if not path.exists():
            failures.append(f"ci artifact report missing generated file: {path}")
    return failures


def run_version_eval() -> list[str]:
    failures: list[str] = []
    script = REPO_ROOT / "scripts" / "version_guard.py"
    result = subprocess.run(
        [sys.executable, str(script), "--output-dir", str(REPO_ROOT / "build" / "ci" / "version"), "--json"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        failures.append(f"version_guard failed during eval: {result.stderr.strip() or result.stdout.strip()}")
        return failures
    payload = json.loads(result.stdout)
    if payload.get("status") not in {"version-ready", "release-ready"}:
        failures.append(f"version guard returned unexpected status: {payload.get('status')}")
    if not payload.get("version"):
        failures.append("version guard did not report a version")
    if payload.get("failures"):
        failures.extend(payload["failures"])
    for key in ("json", "markdown"):
        path = Path(payload[key])
        if not path.exists():
            failures.append(f"version eval missing artifact: {path}")
    return failures


def run_doc_sync_eval() -> list[str]:
    failures: list[str] = []
    script = REPO_ROOT / "scripts" / "doc_sync_audit.py"
    result = subprocess.run(
        [sys.executable, str(script), "src/main.gd", "scripts/route_task.py", "studio/presets/genre/metroidvania.md", "--json"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        failures.append(f"doc_sync_audit failed during eval: {result.stderr.strip() or result.stdout.strip()}")
        return failures
    payload = json.loads(result.stdout)
    docs = {item["doc"] for item in payload.get("recommendations", [])}
    expected = {"docs/reference/ci-cd.md", "docs/reference/genre-presets.md"}
    missing = expected - docs
    if missing:
        failures.append(f"doc sync audit missing expected docs: {', '.join(sorted(missing))}")
    return failures


def run_benchmark_eval() -> list[str]:
    failures: list[str] = []
    script = REPO_ROOT / "scripts" / "run_bench.py"
    output_dir = REPO_ROOT / "build" / "bench" / "eval"
    result = subprocess.run(
        [sys.executable, str(script), "--output-dir", str(output_dir), "--json"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    try:
        payload = json.loads(result.stdout or "{}")
    except json.JSONDecodeError:
        failures.append(f"run_bench failed during eval: {result.stderr.strip() or result.stdout.strip()}")
        return failures

    summary = payload.get("summary", {}) if isinstance(payload, dict) else {}
    if result.returncode != 0 or int(summary.get("failure_count", 0) or 0) > 0:
        for case in payload.get("cases", []) if isinstance(payload, dict) else []:
            task = case.get("task", "unknown task")
            for failure in case.get("failures", []):
                failures.append(f"benchmark case '{task}': {failure}")
        if not failures:
            failures.append(f"benchmark surface reported failures: {summary}")
        return failures

    if summary.get("readiness") != "benchmark-ready":
        failures.append(f"benchmark readiness is not benchmark-ready: {summary.get('readiness')}")
    if int(summary.get("score", 0) or 0) < 90:
        failures.append(f"benchmark score below threshold: {summary.get('score')}")

    artifacts = payload.get("artifacts", {}) if isinstance(payload, dict) else {}
    for key in ("json", "markdown"):
        path = Path(artifacts.get(key, ""))
        if not path.exists():
            failures.append(f"benchmark eval missing artifact: {path}")
    return failures


def run_godot_surface_eval() -> list[str]:
    failures: list[str] = []
    expectations = load_cases(EVALS_DIR / "godot_surface" / "expectations.json")
    script = REPO_ROOT / "scripts" / "godot_smoke.py"

    result = subprocess.run(
        [sys.executable, str(script), "--json", "--static-only"],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        failures.append(f"godot_smoke failed during eval: {result.stderr.strip() or result.stdout.strip()}")
        return failures

    payload = json.loads(result.stdout)
    scene_nodes = set(payload.get("static", {}).get("scene_nodes", []))
    presets = set(payload.get("static", {}).get("presets", []))
    scripts = set(payload.get("static", {}).get("scripts", []))

    for node_name in expectations.get("required_scene_nodes", []):
        if node_name not in scene_nodes:
            failures.append(f"godot surface missing scene node '{node_name}'")
    for preset_name in expectations.get("required_presets", []):
        if preset_name not in presets:
            failures.append(f"godot surface missing export preset '{preset_name}'")
    for script_path in expectations.get("required_scripts", []):
        if script_path not in scripts:
            failures.append(f"godot surface missing script '{script_path}'")

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Run local regression-style evals for repo workflows.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    failures = {
        "route_task": run_route_task_eval(),
        "genre_guidance": run_genre_guidance_eval(),
        "doctor_surface": run_doctor_surface_eval(),
        "engine_kits": run_engine_kits_eval(),
        "workflow_surface": run_workflow_surface_eval(),
        "engine_adapters": run_engine_adapter_eval(),
        "agent_metadata": run_agent_metadata_eval(),
        "route_task_engines": run_route_task_engine_eval(),
        "route_task_engine_fit": run_route_task_engine_fit(),
        "checklists": run_checklist_eval(),
        "research_surface": run_research_surface_eval(),
        "versioning": run_version_eval(),
        "ci_report": run_ci_report_eval(),
        "doc_sync": run_doc_sync_eval(),
        "benchmark": run_benchmark_eval(),
        "godot_surface": run_godot_surface_eval(),
    }
    total_failures = sum(len(items) for items in failures.values())

    if args.json:
        print(json.dumps(failures, indent=2))
    else:
        print("Local Evals")
        print("===========")
        for suite, items in failures.items():
            if items:
                print(f"[FAIL] {suite}")
                for item in items:
                    print(f"- {item}")
            else:
                print(f"[PASS] {suite}")

    return 1 if total_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
