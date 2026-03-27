#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from _studio_common import REPO_ROOT, write_text

UNITY_STUB = REPO_ROOT / "tools" / "engine-stubs" / "unity" / "Unity"
UNREAL_STUB = REPO_ROOT / "tools" / "engine-stubs" / "unreal" / "RunUAT.sh"


def commands_for_engine(engine: str) -> list[list[str]]:
    commands: dict[str, list[list[str]]] = {
        "godot-4": [
            [sys.executable, str(REPO_ROOT / "scripts" / "validate_engine_kits.py"), "--engine", "godot-4"],
            [sys.executable, str(REPO_ROOT / "scripts" / "godot_smoke.py"), "--json", "--static-only"],
        ],
        "unity-6": [
            [sys.executable, str(REPO_ROOT / "scripts" / "validate_engine_kits.py"), "--engine", "unity-6"],
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
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "unity_adapter.py"),
                "build",
                "--project-path",
                str(REPO_ROOT / "studio" / "starter-kits" / "unity-6" / "scaffold"),
                "--unity-path",
                str(UNITY_STUB),
                "--dry-run",
                "--json",
            ],
        ],
        "unreal-5": [
            [sys.executable, str(REPO_ROOT / "scripts" / "validate_engine_kits.py"), "--engine", "unreal-5"],
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
        ],
    }
    return commands[engine]


def render_markdown(engine: str, records: list[dict[str, object]], failures: list[str]) -> str:
    lines = [f"# Starter Kit Contract Smoke — {engine}", ""]
    for record in records:
        status = "PASS" if record["returncode"] == 0 else "FAIL"
        lines.append(f"- [{status}] {' '.join(record['command'])}")
    if failures:
        lines += ["", "## Failures"]
        for failure in failures:
            lines.append(f"- {failure}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Run starter-kit contract smoke checks for a specific engine family.")
    parser.add_argument("--engine", required=True, choices=["godot-4", "unity-6", "unreal-5"])
    parser.add_argument("--output-dir")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    records: list[dict[str, object]] = []
    failures: list[str] = []
    for command in commands_for_engine(args.engine):
        result = subprocess.run(command, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        record = {
            "command": command[1:] if command and command[0] == sys.executable else command,
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
        records.append(record)
        if result.returncode != 0:
            failures.append(f"{args.engine}: command failed: {' '.join(record['command'])}")

    payload = {"engine": args.engine, "failures": failures, "records": records}

    if args.output_dir:
        output_dir = Path(args.output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        write_text(output_dir / f"{args.engine}-contract-smoke.json", json.dumps(payload, indent=2))
        write_text(output_dir / f"{args.engine}-contract-smoke.md", render_markdown(args.engine, records, failures))

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(render_markdown(args.engine, records, failures))
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
