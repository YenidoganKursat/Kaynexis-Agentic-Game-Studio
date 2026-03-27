#!/usr/bin/env python3
from __future__ import annotations

import argparse

from _studio_common import ACTIVE_DIR, slugify, write_text

def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a lightweight QA matrix markdown file.")
    parser.add_argument("title", help="Feature or milestone under test.")
    parser.add_argument("--criterion", action="append", default=[], help="Repeatable acceptance criterion.")
    parser.add_argument("--slug", help="Optional custom slug.")
    args = parser.parse_args()

    slug = args.slug or slugify(args.title)
    criteria = args.criterion or [
        "Core happy path works",
        "Settings/save/load path works",
        "Controller / alternate input path works",
        "Failure / retry path works",
        "Known edge case remains stable",
    ]

    lines = [f"# QA Matrix — {args.title}", "", "## Test cases", "", "| Case | Type | Expected | Notes |", "|---|---|---|---|"]
    for i, criterion in enumerate(criteria, start=1):
        lines.append(f"| {i}. {criterion} | Smoke / Regression | Pass | Record observed result, build, and evidence |")
    lines += ["", "## Environment notes", "- Build / platform / locale / save state", "", "## Exit criteria", "- All critical cases pass or accepted risks are documented"]
    target = ACTIVE_DIR / f"qa-matrix-{slug}.md"
    write_text(target, "\n".join(lines))
    print(target)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
