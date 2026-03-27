#!/usr/bin/env python3
from __future__ import annotations

import argparse

from _studio_common import ACTIVE_DIR, load_template, slugify, write_text

def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold bug triage docs into studio/docs/active/")
    parser.add_argument("bug_name")
    parser.add_argument("--slug", help="Optional custom slug.")
    args = parser.parse_args()

    slug = args.slug or slugify(args.bug_name)
    replacements = {"BUG_NAME": args.bug_name}

    bug_report = ACTIVE_DIR / f"bug-{slug}.md"
    crash_report = ACTIVE_DIR / f"crash-triage-{slug}.md"

    write_text(bug_report, load_template("bug-report.md", replacements))
    write_text(crash_report, load_template("crash-triage.md", replacements))

    print("Created:")
    print(f"- {bug_report}")
    print(f"- {crash_report}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
