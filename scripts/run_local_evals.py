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


def run_checklist_eval() -> list[str]:
    failures: list[str] = []
    items = resolve_checklists(engine_slug="godot-4", disciplines=["gameplay"], milestone="prototype", agent_name="gameplay_programmer")
    item_ids = {item["id"] for item in items}
    for required in ("repo-health-doctor", "gameplay-readability", "prototype-proves-core-loop"):
        if required not in item_ids:
            failures.append(f"resolved checklist bundle is missing '{required}'")
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
                "/Applications/Unity/Hub/Editor/6000.0.0f1/Unity",
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
                "/Applications/Epic/UE_5.5/Engine/Build/BatchFiles/RunUAT.sh",
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


def run_route_task_engine_eval() -> list[str]:
    failures: list[str] = []
    cases = [
        ("Plan the next Unity starter kit task", "engine / tooling / packaging", "unity-6"),
        ("Plan the next UE5 packaging task", "engine / tooling / packaging", "unreal-5"),
        ("Implement Unity combat room", "combat / gameplay", "unity-6"),
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


def run_research_surface_eval() -> list[str]:
    failures: list[str] = []
    notes = research_notes()
    if not notes:
        failures.append("research knowledge base has no notes")
        return failures
    for note in notes:
        failures.extend(validate_research_note(note))
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
        "engine_adapters": run_engine_adapter_eval(),
        "route_task_engines": run_route_task_engine_eval(),
        "checklists": run_checklist_eval(),
        "research_surface": run_research_surface_eval(),
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
