#!/usr/bin/env python3
from __future__ import annotations

import argparse

from _studio_common import append_preset_pack, available_presets

def main() -> int:
    parser = argparse.ArgumentParser(description="Append selected engine/platform/genre presets into studio/docs/active/preset-pack.md")
    parser.add_argument("--engine", help=f"Available: {', '.join(available_presets('engine'))}")
    parser.add_argument("--platform", help=f"Available: {', '.join(available_presets('platform'))}")
    parser.add_argument("--genre", help=f"Available: {', '.join(available_presets('genre'))}")
    parser.add_argument("--replace", action="store_true", help="Replace existing preset-pack.md instead of appending.")
    args = parser.parse_args()

    target = append_preset_pack(engine=args.engine, platform=args.platform, genre=args.genre, replace=args.replace)
    print(f"Wrote preset pack: {target}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
