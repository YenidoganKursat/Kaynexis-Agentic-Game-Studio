#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

from _studio_common import REPO_ROOT, find_godot_binary

PROJECT_FILE = REPO_ROOT / "project.godot"
EXPORT_PRESETS_FILE = REPO_ROOT / "export_presets.cfg"
SCENE_FILE = REPO_ROOT / "src" / "main.tscn"
MAIN_SCRIPT = REPO_ROOT / "src" / "main.gd"
PLAYER_SCRIPT = REPO_ROOT / "src" / "player.gd"
WARDEN_SCRIPT = REPO_ROOT / "src" / "pulse_warden.gd"


def parse_scene_nodes(text: str) -> list[str]:
    return re.findall(r'^\[node name="([^"]+)"', text, flags=re.MULTILINE)


def parse_presets(text: str) -> list[str]:
    return re.findall(r'^name="([^"]+)"$', text, flags=re.MULTILINE)


def run_static_checks() -> tuple[list[str], dict[str, object]]:
    failures: list[str] = []

    required_files = [
        PROJECT_FILE,
        EXPORT_PRESETS_FILE,
        SCENE_FILE,
        MAIN_SCRIPT,
        PLAYER_SCRIPT,
        WARDEN_SCRIPT,
    ]
    for path in required_files:
        if not path.exists():
            failures.append(f"Missing required Godot file: {path.relative_to(REPO_ROOT)}")

    scene_nodes: list[str] = []
    presets: list[str] = []
    main_scene = ""
    main_script_text = ""

    if PROJECT_FILE.exists():
        project_text = PROJECT_FILE.read_text(encoding="utf-8")
        match = re.search(r'^run/main_scene="([^"]+)"$', project_text, flags=re.MULTILINE)
        if not match:
            failures.append("project.godot does not declare run/main_scene.")
        else:
            main_scene = match.group(1)
            if main_scene != "res://src/main.tscn":
                failures.append(f"Unexpected main scene: {main_scene}")

    if SCENE_FILE.exists():
        scene_text = SCENE_FILE.read_text(encoding="utf-8")
        scene_nodes = parse_scene_nodes(scene_text)
        for node_name in ("Player", "PulseWarden", "Hud", "ArenaBounds"):
            if node_name not in scene_nodes:
                failures.append(f"main.tscn is missing node '{node_name}'.")

    if EXPORT_PRESETS_FILE.exists():
        export_text = EXPORT_PRESETS_FILE.read_text(encoding="utf-8")
        presets = parse_presets(export_text)
        for preset_name in ("Linux/X11", "Windows Desktop"):
            if preset_name not in presets:
                failures.append(f"export_presets.cfg is missing preset '{preset_name}'.")

    if MAIN_SCRIPT.exists():
        main_script_text = MAIN_SCRIPT.read_text(encoding="utf-8")
        if "First combat room ready" not in main_script_text:
            failures.append("src/main.gd should print a stable smoke marker on startup.")

    payload = {
        "main_scene": main_scene,
        "scene_nodes": scene_nodes,
        "presets": presets,
        "scripts": [
            path.relative_to(REPO_ROOT).as_posix()
            for path in (MAIN_SCRIPT, PLAYER_SCRIPT, WARDEN_SCRIPT)
            if path.exists()
        ],
    }
    return failures, payload


def run_runtime_smoke(godot_bin: str) -> tuple[list[str], dict[str, object]]:
    failures: list[str] = []
    result = subprocess.run(
        [godot_bin, "--headless", "--path", str(REPO_ROOT), "--quit"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    output = (result.stdout + "\n" + result.stderr).strip()

    if result.returncode != 0:
        failures.append(f"Godot headless startup failed with exit code {result.returncode}.")

    return failures, {
        "command": [godot_bin, "--headless", "--path", str(REPO_ROOT), "--quit"],
        "returncode": result.returncode,
        "output": output,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run static and optional runtime smoke checks for the Godot slice.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable output.")
    parser.add_argument("--static-only", action="store_true", help="Skip the runtime Godot invocation.")
    parser.add_argument("--require-engine", action="store_true", help="Fail if a Godot binary is not available.")
    args = parser.parse_args()

    failures, static_payload = run_static_checks()
    warnings: list[str] = []
    runtime_payload: dict[str, object] = {"attempted": False}

    godot_bin = find_godot_binary()
    if args.static_only:
        pass
    elif godot_bin:
        runtime_failures, runtime_payload = run_runtime_smoke(godot_bin)
        runtime_payload["attempted"] = True
        runtime_payload["godot_bin"] = godot_bin
        failures.extend(runtime_failures)
    else:
        message = "No Godot binary found. Set GODOT_BIN or install Godot 4.x to run the runtime smoke."
        if args.require_engine:
            failures.append(message)
        else:
            warnings.append(message)

    payload = {
        "failures": failures,
        "warnings": warnings,
        "static": static_payload,
        "runtime": runtime_payload,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print("Godot Smoke")
        print("===========")
        if failures:
            for item in failures:
                print(f"[FAIL] {item}")
        else:
            print("[PASS] Static Godot surface is complete.")
        for item in warnings:
            print(f"[WARN] {item}")
        if runtime_payload.get("attempted"):
            print(f"[INFO] Runtime smoke exit code: {runtime_payload.get('returncode')}")

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
