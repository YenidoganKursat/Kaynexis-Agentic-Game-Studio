#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re

from _studio_common import REPO_ROOT

CONFIG_PATH = REPO_ROOT / ".codex" / "config.toml"


def update_hooks_flag(enabled: bool) -> None:
    text = CONFIG_PATH.read_text(encoding="utf-8")
    replacement = f"codex_hooks = {'true' if enabled else 'false'}"

    if re.search(r"(?m)^codex_hooks\s*=\s*(true|false)\s*$", text):
        text = re.sub(r"(?m)^codex_hooks\s*=\s*(true|false)\s*$", replacement, text)
    else:
        marker = "[features]\n"
        if marker not in text:
            raise RuntimeError("Could not find [features] section in .codex/config.toml")
        text = text.replace(marker, marker + replacement + "\n", 1)

    CONFIG_PATH.write_text(text, encoding="utf-8")


def read_hooks_flag() -> str:
    text = CONFIG_PATH.read_text(encoding="utf-8")
    match = re.search(r"(?m)^codex_hooks\s*=\s*(true|false)\s*$", text)
    return match.group(1) if match else "unset"


def main() -> int:
    parser = argparse.ArgumentParser(description="Enable or disable optional Codex hooks for this repo.")
    parser.add_argument("--enable", action="store_true")
    parser.add_argument("--disable", action="store_true")
    parser.add_argument("--status", action="store_true")
    args = parser.parse_args()

    if sum(1 for flag in (args.enable, args.disable, args.status) if flag) != 1:
        parser.error("Choose exactly one of --enable, --disable, or --status.")

    if args.status:
        print(read_hooks_flag())
        return 0

    update_hooks_flag(args.enable)
    print("enabled" if args.enable else "disabled")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
