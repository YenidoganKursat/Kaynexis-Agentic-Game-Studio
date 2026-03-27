#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path

from _studio_common import REPO_ROOT, find_godot_binary

EXPORT_PRESETS_PATH = REPO_ROOT / "export_presets.cfg"


def read_export_path(preset_name: str) -> str | None:
    text = EXPORT_PRESETS_PATH.read_text(encoding="utf-8")
    pattern = re.compile(
        r"\[preset\.\d+\]\s+name=\"(?P<name>[^\"]+)\".*?export_path=\"(?P<path>[^\"]+)\"",
        flags=re.DOTALL,
    )
    for match in pattern.finditer(text):
        if match.group("name") == preset_name:
            return match.group("path")
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Export the Godot project using export_presets.cfg.")
    parser.add_argument("--preset", default="Linux/X11", help="Preset name from export_presets.cfg.")
    parser.add_argument("--output", help="Optional override for the output path.")
    parser.add_argument("--dry-run", action="store_true", help="Print the resolved command without running it.")
    args = parser.parse_args()

    if not EXPORT_PRESETS_PATH.exists():
        raise SystemExit("export_presets.cfg is missing.")

    export_path = args.output or read_export_path(args.preset)
    if not export_path:
        raise SystemExit(f"Could not resolve export path for preset '{args.preset}'.")

    godot_bin = find_godot_binary()
    if not godot_bin and not args.dry_run:
        raise SystemExit("No Godot binary found. Set GODOT_BIN or install Godot 4.x before exporting.")

    output_path = Path(export_path)
    command = [
        godot_bin or "godot4",
        "--headless",
        "--path",
        str(REPO_ROOT),
        "--export-release",
        args.preset,
        str(output_path),
    ]

    if args.dry_run:
        print(" ".join(command))
        return 0

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(command, cwd=REPO_ROOT, check=False)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
