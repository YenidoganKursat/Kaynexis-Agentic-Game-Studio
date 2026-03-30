#!/usr/bin/env python3
from __future__ import annotations

import argparse

from _studio_common import ACTIVE_DIR, load_template, slugify, write_text

def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold bug triage docs into studio/docs/active/")
    parser.add_argument("bug_name")
    parser.add_argument("--slug", help="Optional custom slug.")
    parser.add_argument("--with-test-plan", action="store_true", help="Also create a test plan stub.")
    parser.add_argument("--with-eval-plan", action="store_true", help="Also create an eval plan stub.")
    args = parser.parse_args()

    slug = args.slug or slugify(args.bug_name)
    replacements = {
        "BUG_NAME": args.bug_name,
        "SYSTEM_ATLAS_REF": "docs/reference/system-atlas.md",
        "ENGINE_ATLAS_REF": "docs/reference/engine-atlas.md",
        "ENGINE_MAP_REF": "docs/reference/engine-map.md",
        "ENGINE_MINI_ATLAS_NOTE": "Godot / Unity / Unreal",
    }

    bug_report = ACTIVE_DIR / f"bug-{slug}.md"
    crash_report = ACTIVE_DIR / f"crash-triage-{slug}.md"

    write_text(bug_report, load_template("bug-report.md", replacements))
    write_text(crash_report, load_template("crash-triage.md", replacements))

    if args.with_test_plan:
        test_plan = ACTIVE_DIR / f"test-plan-{slug}.md"
        write_text(test_plan, load_template("test-plan.md", replacements))
    else:
        test_plan = None

    if args.with_eval_plan:
        eval_plan = ACTIVE_DIR / f"eval-plan-{slug}.md"
        write_text(eval_plan, load_template("eval-plan.md", replacements))
    else:
        eval_plan = None

    print("Created:")
    print(f"- {bug_report}")
    print(f"- {crash_report}")
    if test_plan:
        print(f"- {test_plan}")
    if eval_plan:
        print(f"- {eval_plan}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
