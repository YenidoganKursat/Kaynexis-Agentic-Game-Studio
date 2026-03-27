#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
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
        "Assets/Scripts/Runtime/StarterKit.Runtime.asmdef",
        "Assets/Scripts/Runtime/CombatRoomDirector.cs",
        "Assets/Scripts/Runtime/EnemyArchetype.cs",
        "Assets/Tests/EditMode/StarterKit.EditMode.asmdef",
        "Assets/Tests/EditMode/CombatRoomDirectorTests.cs",
    ),
    "unreal-5": (
        "Source/StarterKit/StarterKitGameModeBase.h",
        "Source/StarterKit/StarterKitGameModeBase.cpp",
        "Source/StarterKit/StarterKitEnemyArchetype.h",
        "Content/Maps/README.md",
    ),
}


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
