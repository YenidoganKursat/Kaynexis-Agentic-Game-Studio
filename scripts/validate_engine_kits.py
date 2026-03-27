#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import shlex
import sys
from pathlib import Path

from _studio_common import REPO_ROOT
from studio_core import available_starter_kits, load_starter_kit_manifest

REQUIRED_KEYS = (
    "id",
    "engine",
    "version_family",
    "required_markers",
    "bootstrap_command",
    "smoke_commands",
    "export_commands",
    "supported_platforms",
    "seed_docs",
    "validation_steps",
)

KIT_DEEP_MARKERS: dict[str, tuple[str, ...]] = {
    "godot-4": (
        "project.godot",
        "src/main.tscn",
        "src/main.gd",
    ),
    "unity-6": (
        "Assets/Scenes/CombatRoom.unity",
        "Assets/Prefabs/README.md",
        "Assets/ScriptableObjects/README.md",
        "Assets/Scripts/Runtime/StarterKit.Runtime.asmdef",
        "Assets/Scripts/Runtime/CombatRoomDirector.cs",
        "Assets/Scripts/Runtime/EnemyArchetype.cs",
        "Assets/Scripts/Runtime/Health.cs",
        "Assets/Scripts/Runtime/PlayerAvatar.cs",
        "Assets/Scripts/Runtime/PulseEnemy.cs",
        "Assets/Scripts/Editor/BuildPipelineEntry.cs",
        "Assets/Scripts/Editor/StarterKit.Editor.asmdef",
        "Assets/Tests/EditMode/StarterKit.EditMode.asmdef",
        "Assets/Tests/EditMode/CombatRoomDirectorTests.cs",
        "Assets/Tests/EditMode/HealthTests.cs",
    ),
    "unreal-5": (
        "Config/DefaultEngine.ini",
        "Config/DefaultInput.ini",
        "Content/Blueprints/README.md",
        "Source/StarterKit/StarterKitGameModeBase.h",
        "Source/StarterKit/StarterKitGameModeBase.cpp",
        "Source/StarterKit/StarterKitEnemyArchetype.h",
        "Source/StarterKit/StarterKitCharacter.h",
        "Source/StarterKit/StarterKitCharacter.cpp",
        "Source/StarterKit/StarterKitEnemyActor.h",
        "Source/StarterKit/StarterKitEnemyActor.cpp",
        "Source/StarterKit/StarterKitHealthComponent.h",
        "Source/StarterKit/StarterKitHealthComponent.cpp",
        "Content/Maps/README.md",
    ),
}

FILE_CONTENT_MARKERS: dict[str, dict[str, tuple[str, ...]]] = {
    "unity-6": {
        "Assets/Scripts/Runtime/CombatRoomDirector.cs": ("PlayerAvatar", "PulseEnemy", "DescribeNextExpansion"),
        "Assets/Scripts/Runtime/EnemyArchetype.cs": ("attackWindupSeconds", "pulseRadius"),
        "Assets/Scripts/Runtime/Health.cs": ("ApplyDamage", "ResetHealth"),
        "Assets/Scripts/Runtime/PlayerAvatar.cs": ("DashDistance", "DescribeControlSurface"),
        "Assets/Scripts/Runtime/PulseEnemy.cs": ("Configure", "DescribePressureProfile"),
        "Assets/Scripts/Editor/BuildPipelineEntry.cs": ("Build()", "Debug.Log"),
        "Assets/Tests/EditMode/HealthTests.cs": ("ApplyDamage_ClampsToZero",),
    },
    "unreal-5": {
        "Source/StarterKit/StarterKitGameModeBase.h": ("DefaultPlayerClass", "DefaultEnemyClass"),
        "Source/StarterKit/StarterKitGameModeBase.cpp": ("AStarterKitCharacter::StaticClass()", "AStarterKitEnemyActor::StaticClass()"),
        "Source/StarterKit/StarterKitEnemyArchetype.h": ("PulseWindupSeconds", "PulseRadius"),
        "Source/StarterKit/StarterKitCharacter.h": ("ACharacter", "DashDistance"),
        "Source/StarterKit/StarterKitEnemyActor.h": ("UStarterKitHealthComponent", "PulseRadius"),
        "Source/StarterKit/StarterKitHealthComponent.h": ("ApplyDamage", "IsAlive"),
        "Config/DefaultInput.ini": ("ActionName=\"Dash\"", "AxisName=\"MoveForward\""),
        "Config/DefaultEngine.ini": ("GameDefaultMap=/Game/Maps/CombatRoom",),
    },
}


def validate_command_references(engine_slug: str, manifest: dict[str, object]) -> list[str]:
    failures: list[str] = []
    commands: list[str] = []
    bootstrap_command = manifest.get("bootstrap_command")
    if isinstance(bootstrap_command, str) and bootstrap_command.strip():
        commands.append(bootstrap_command)
    for key in ("smoke_commands", "export_commands"):
        values = manifest.get(key, [])
        if isinstance(values, list):
            commands.extend(str(value) for value in values if str(value).strip())

    if not commands:
        failures.append(f"{engine_slug}: manifest has no executable command references")
        return failures

    for command in commands:
        try:
            parts = shlex.split(command)
        except ValueError as exc:
            failures.append(f"{engine_slug}: command is not shell-parseable '{command}': {exc}")
            continue
        if len(parts) >= 2 and parts[0].startswith("python") and parts[1].startswith("scripts/"):
            script_path = REPO_ROOT / parts[1]
            if not script_path.exists():
                failures.append(f"{engine_slug}: command references missing script '{parts[1]}'")

    for path_str in manifest.get("seed_docs", []):
        seed_path = REPO_ROOT / str(path_str)
        if not seed_path.exists():
            failures.append(f"{engine_slug}: seed doc path is missing '{path_str}'")

    return failures


def validate_kit(engine_slug: str) -> list[str]:
    failures: list[str] = []
    manifest = load_starter_kit_manifest(engine_slug)
    for key in REQUIRED_KEYS:
        if key not in manifest:
            failures.append(f"{engine_slug}: missing manifest key '{key}'")

    scaffold_dir = Path(manifest["path"]).parent / "scaffold"
    if not scaffold_dir.exists():
        failures.append(f"{engine_slug}: scaffold directory is missing")
        return failures

    for marker in manifest.get("required_markers", []):
        marker_path = scaffold_dir / marker
        if not marker_path.exists():
            failures.append(f"{engine_slug}: scaffold is missing marker '{marker}'")

    for marker in KIT_DEEP_MARKERS.get(engine_slug, ()):
        marker_path = scaffold_dir / marker
        if not marker_path.exists():
            failures.append(f"{engine_slug}: deep validation missing '{marker}'")

    for relative_path, markers in FILE_CONTENT_MARKERS.get(engine_slug, {}).items():
        file_path = scaffold_dir / relative_path
        if not file_path.exists():
            continue
        text = file_path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"{engine_slug}: '{relative_path}' is missing expected content marker '{marker}'")

    failures.extend(validate_command_references(engine_slug, manifest))

    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate starter-kit manifests and scaffold markers.")
    parser.add_argument("--engine", help="Validate only one engine slug.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    engines = [args.engine] if args.engine else available_starter_kits()
    failures: dict[str, list[str]] = {engine: validate_kit(engine) for engine in engines}
    total = sum(len(items) for items in failures.values())

    if args.json:
        print(json.dumps(failures, indent=2))
    else:
        print("Starter Kit Validation")
        print("======================")
        for engine, items in failures.items():
            if items:
                print(f"[FAIL] {engine}")
                for item in items:
                    print(f"- {item}")
            else:
                print(f"[PASS] {engine}")
    return 1 if total else 0


if __name__ == "__main__":
    raise SystemExit(main())
