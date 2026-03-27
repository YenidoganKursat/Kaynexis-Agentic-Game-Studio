#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

from _studio_common import REPO_ROOT
from studio_core import resolve_tool_path

DEFAULT_PLATFORM = "Win64"
DEFAULT_CONFIG = "Development"
DEFAULT_ARCHIVE_DIR = REPO_ROOT / "build" / "unreal"


def normalize_tool_path(candidate: str) -> str:
    path = Path(candidate).expanduser()
    if not path.is_absolute():
        path = (REPO_ROOT / path).resolve()
    return str(path)


def resolve_uat_path(explicit: str | None = None) -> str | None:
    if explicit:
        return normalize_tool_path(explicit)

    uat = resolve_tool_path(config_key="unreal_uat", env_keys=["UNREAL_UAT"])
    if uat:
        return normalize_tool_path(uat)

    editor = resolve_tool_path(config_key="unreal_editor", env_keys=["UNREAL_EDITOR"])
    if not editor:
        return None

    editor_path = Path(editor)
    parts = editor_path.parts
    if "Engine" not in parts:
        return None

    engine_root = Path(*parts[: parts.index("Engine") + 1])
    batch_dir = engine_root / "Build" / "BatchFiles"
    for candidate in ("RunUAT.sh", "RunUAT.command", "RunUAT.bat"):
        path = batch_dir / candidate
        if path.exists():
            return str(path)
    return None


def validate_tool_path(tool_path: str) -> list[str]:
    path = Path(tool_path)
    if not path.exists():
        return [f"Unreal UAT path does not exist: {tool_path}"]
    if path.is_dir():
        return [f"Unreal UAT path points to a directory, expected a script or executable file: {tool_path}"]
    return []


def find_uproject(project_path: Path) -> Path | None:
    matches = sorted(project_path.glob("*.uproject"))
    return matches[0] if matches else None


def validate_unreal_project(project_path: Path, uproject_path: Path | None) -> list[str]:
    failures: list[str] = []
    for rel in ("Config", "Content", "Source"):
        if not (project_path / rel).exists():
            failures.append(f"Missing Unreal project marker: {project_path / rel}")
    if uproject_path is None:
        failures.append("No .uproject file found in the selected project path.")
    return failures


def build_package_command(uat_path: str, uproject_path: Path, platform: str, client_config: str, archive_dir: Path) -> list[str]:
    return [
        uat_path,
        "BuildCookRun",
        f"-project={uproject_path}",
        f"-platform={platform}",
        f"-clientconfig={client_config}",
        "-build",
        "-cook",
        "-stage",
        "-package",
        "-archive",
        f"-archivedirectory={archive_dir}",
        "-unattended",
        "-NoCompileEditor",
    ]


def emit_payload(command: list[str], project_path: Path, uproject_path: Path, tool_path: str, validation_failures: list[str]) -> None:
    print(
        json.dumps(
            {
                "action": "package",
                "project_path": str(project_path),
                "uproject": str(uproject_path),
                "tool_path": tool_path,
                "tool_path_exists": not any("Unreal UAT path" in item for item in validation_failures),
                "command": command,
                "validation_failures": validation_failures,
            },
            indent=2,
        )
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate or run Unreal packaging commands through a repo-level adapter.")
    parser.add_argument("action", choices=["package"])
    parser.add_argument("--project-path", default=str(REPO_ROOT))
    parser.add_argument("--uproject")
    parser.add_argument("--uat-path")
    parser.add_argument("--platform", default=DEFAULT_PLATFORM)
    parser.add_argument("--client-config", default=DEFAULT_CONFIG)
    parser.add_argument("--archive-dir", default=str(DEFAULT_ARCHIVE_DIR))
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.uat_path:
        os.environ["UNREAL_UAT"] = args.uat_path
    uat_path = resolve_uat_path(args.uat_path)
    if not uat_path:
        message = "Unreal UAT path is not configured. Set UNREAL_UAT, UNREAL_EDITOR, or tools.unreal_uat in studio.toml."
        if args.json:
            print(json.dumps({"action": "package", "error": message}, indent=2))
        else:
            print(f"ERROR: {message}")
        return 1

    project_path = Path(args.project_path).resolve()
    uproject_path = Path(args.uproject).resolve() if args.uproject else find_uproject(project_path)
    failures = validate_unreal_project(project_path, uproject_path)
    failures.extend(validate_tool_path(uat_path))

    command = build_package_command(
        uat_path=uat_path,
        uproject_path=uproject_path or Path("Missing.uproject"),
        platform=args.platform,
        client_config=args.client_config,
        archive_dir=Path(args.archive_dir).resolve(),
    )

    if args.json:
        emit_payload(command, project_path, uproject_path or Path("Missing.uproject"), uat_path, failures)
    if failures:
        if not args.json:
            for item in failures:
                print(f"ERROR: {item}")
        return 1
    if args.dry_run:
        if not args.json:
            emit_payload(command, project_path, uproject_path or Path("Missing.uproject"), uat_path, failures)
        return 0
    return subprocess.run(command, cwd=REPO_ROOT, check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
