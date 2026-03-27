#!/usr/bin/env python3
from __future__ import annotations

import argparse

from _studio_common import ACTIVE_DIR, load_template, slugify, write_text

def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold feature docs into studio/docs/active/")
    parser.add_argument("feature_name", help="Human-readable feature name.")
    parser.add_argument("--slug", help="Optional custom slug.")
    parser.add_argument("--with-adr", action="store_true", help="Also create an ADR stub.")
    parser.add_argument("--with-test-plan", action="store_true", help="Also create a test plan stub.")
    parser.add_argument("--with-eval-plan", action="store_true", help="Also create an eval plan stub.")
    args = parser.parse_args()

    slug = args.slug or slugify(args.feature_name)
    replacements = {
        "FEATURE_NAME": args.feature_name,
        "TEST_SCOPE": args.feature_name,
        "DECISION_NAME": args.feature_name,
        "EVAL_NAME": args.feature_name,
    }

    targets = []
    feature_path = ACTIVE_DIR / f"feature-{slug}.md"
    write_text(feature_path, load_template("feature-brief.md", replacements))
    targets.append(feature_path)

    if args.with_adr:
        adr_path = ACTIVE_DIR / f"adr-{slug}.md"
        write_text(adr_path, load_template("adr.md", replacements))
        targets.append(adr_path)

    if args.with_test_plan:
        test_path = ACTIVE_DIR / f"test-plan-{slug}.md"
        write_text(test_path, load_template("test-plan.md", replacements))
        targets.append(test_path)

    if args.with_eval_plan:
        eval_path = ACTIVE_DIR / f"eval-plan-{slug}.md"
        write_text(eval_path, load_template("eval-plan.md", replacements))
        targets.append(eval_path)

    print("Created:")
    for path in targets:
        print(f"- {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
