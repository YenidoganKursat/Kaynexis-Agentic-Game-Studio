#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

from _studio_common import REPO_ROOT
from studio_core import resolve_tool_path

DEFAULT_RESULTS_PATH = REPO_ROOT / "build" / "unity" / "test-results.xml"
DEFAULT_BUILD_TARGET = "StandaloneWindows64"
DEFAULT_EXECUTE_METHOD = "BuildPipelineEntry.Build"


def normalize_tool_path(candidate: str) -> str:
    path = Path(candidate).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return str(path)


def unity_cli_path(explicit: str | None = None) -> str | None:
    if explicit:
        return normalize_tool_path(explicit)
    configured = resolve_tool_path(config_key="unity_cli", env_keys=["UNITY_CLI"])
    return normalize_tool_path(configured) if configured else None


def validate_tool_path(tool_path: str) -> list[str]:
    path = Path(tool_path)
    if not path.exists():
        return [f"Unity CLI path does not exist: {tool_path}"]
    if path.is_dir():
        return [f"Unity CLI path points to a directory, expected an executable file: {tool_path}"]
    return []


def validate_unity_project(project_path: Path) -> list[str]:
    failures: list[str] = []
    for rel in ("Assets", "Packages/manifest.json", "ProjectSettings/ProjectVersion.txt"):
        if not (project_path / rel).exists():
            failures.append(f"Missing Unity project marker: {project_path / rel}")
    return failures


def build_test_command(project_path: Path, unity_path: str, test_platform: str, results_path: Path, log_file: str) -> list[str]:
    return [
        unity_path,
        "-batchmode",
        "-quit",
        "-projectPath",
        str(project_path),
        "-runTests",
        "-testPlatform",
        test_platform,
        "-testResults",
        str(results_path),
        "-logFile",
        log_file,
    ]


def build_build_command(project_path: Path, unity_path: str, build_target: str, execute_method: str, log_file: str) -> list[str]:
    return [
        unity_path,
        "-batchmode",
        "-quit",
        "-projectPath",
        str(project_path),
        "-buildTarget",
        build_target,
        "-executeMethod",
        execute_method,
        "-logFile",
        log_file,
    ]


def emit_payload(action: str, command: list[str], project_path: Path, tool_path: str, validation_failures: list[str]) -> None:
    print(
        json.dumps(
            {
                "action": action,
                "project_path": str(project_path),
                "tool_path": tool_path,
                "tool_path_exists": not any("Unity CLI path" in item for item in validation_failures),
                "command": command,
                "validation_failures": validation_failures,
            },
            indent=2,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate or run Unity CLI commands through a repo-level adapter.")
    subparsers = parser.add_subparsers(dest="action", required=True)

    test_parser = subparsers.add_parser("test", help="Generate or run the Unity batchmode test command.")
    test_parser.add_argument("--project-path", default=str(REPO_ROOT))
    test_parser.add_argument("--unity-path")
    test_parser.add_argument("--test-platform", default="EditMode")
    test_parser.add_argument("--results-path", default=str(DEFAULT_RESULTS_PATH))
    test_parser.add_argument("--log-file", default="-")
    test_parser.add_argument("--dry-run", action="store_true")
    test_parser.add_argument("--json", action="store_true")

    build_parser = subparsers.add_parser("build", help="Generate or run the Unity batchmode build command.")
    build_parser.add_argument("--project-path", default=str(REPO_ROOT))
    build_parser.add_argument("--unity-path")
    build_parser.add_argument("--build-target", default=DEFAULT_BUILD_TARGET)
    build_parser.add_argument("--execute-method", default=DEFAULT_EXECUTE_METHOD)
    build_parser.add_argument("--log-file", default="-")
    build_parser.add_argument("--dry-run", action="store_true")
    build_parser.add_argument("--json", action="store_true")

    args = parser.parse_args()
    project_path = Path(args.project_path).resolve()
    unity_path = unity_cli_path(args.unity_path)
    if args.unity_path:
        os.environ["UNITY_CLI"] = args.unity_path

    if not unity_path:
        message = "Unity CLI path is not configured. Set UNITY_CLI or tools.unity_cli in studio.toml."
        if args.json:
            print(json.dumps({"action": args.action, "error": message}, indent=2))
        else:
            print(f"ERROR: {message}")
        return 1

    failures = validate_unity_project(project_path)
    failures.extend(validate_tool_path(unity_path))

    if args.action == "test":
        command = build_test_command(project_path, unity_path, args.test_platform, Path(args.results_path).resolve(), args.log_file)
    else:
        command = build_build_command(project_path, unity_path, args.build_target, args.execute_method, args.log_file)

    if args.json:
        emit_payload(args.action, command, project_path, unity_path, failures)
    if failures:
        if not args.json:
            for item in failures:
                print(f"ERROR: {item}")
        return 1
    if args.dry_run:
        if not args.json:
            emit_payload(args.action, command, project_path, unity_path, failures)
        return 0
    return subprocess.run(command, cwd=REPO_ROOT, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
