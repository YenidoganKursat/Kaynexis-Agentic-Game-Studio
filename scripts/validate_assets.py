#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

from _studio_common import REPO_ROOT

ASSET_ROOT = REPO_ROOT / "assets"
VALID_NAME = re.compile(r"^[a-z0-9_./-]+$")

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate asset naming and obvious hygiene issues.")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as failures.")
    parser.add_argument("--max-size-mb", type=int, default=100, help="Warn if a single asset exceeds this size.")
    args = parser.parse_args()

    warnings: list[str] = []
    errors: list[str] = []

    if not ASSET_ROOT.exists():
        print("Assets directory missing; skipping.")
        return 0

    for path in ASSET_ROOT.rglob("*"):
        if path.is_dir():
            continue
        rel = path.relative_to(ASSET_ROOT).as_posix()
        if path.name in {".gitkeep", "AGENTS.md"}:
            continue
        if not VALID_NAME.match(rel):
            warnings.append(f"Non-normalized asset name: {rel}")
        size_mb = path.stat().st_size / (1024 * 1024)
        if size_mb > args.max_size_mb:
            warnings.append(f"Large asset ({size_mb:.1f} MB): {rel}")
        if path.suffix.lower() in {".tmp", ".bak", ".psd~", ".blend1"}:
            errors.append(f"Temporary or backup asset committed: {rel}")

    for line in errors:
        print(f"ERROR: {line}")
    for line in warnings:
        print(f"WARNING: {line}")

    if not errors and not warnings:
        print("Asset validation passed.")
    return 1 if errors or (args.strict and warnings) else 0

if __name__ == "__main__":
    raise SystemExit(main())
