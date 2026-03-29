#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _studio_common import ACTIVE_DIR, load_template, slugify, write_text

def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold feature docs into studio/docs/active/")
    parser.add_argument("feature_name", help="Human-readable feature name.")
    parser.add_argument("--slug", help="Optional custom slug.")
    parser.add_argument("--output-dir", default=str(ACTIVE_DIR), help="Directory to write the scaffolded docs into.")
    parser.add_argument("--with-adr", action="store_true", help="Also create an ADR stub.")
    parser.add_argument("--with-test-plan", action="store_true", help="Also create a test plan stub.")
    parser.add_argument("--with-eval-plan", action="store_true", help="Also create an eval plan stub.")
    parser.add_argument("--no-handoff", action="store_true", help="Skip the default handoff contract document.")
    parser.add_argument("--no-traceability", action="store_true", help="Skip the default traceability document.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of plain text output.")
    args = parser.parse_args()

    slug = args.slug or slugify(args.feature_name)
    output_dir = Path(args.output_dir).resolve()
    replacements = {
        "FEATURE_NAME": args.feature_name,
        "TEST_SCOPE": args.feature_name,
        "DECISION_NAME": args.feature_name,
        "EVAL_NAME": args.feature_name,
    }

    targets = []
    feature_path = output_dir / f"feature-{slug}.md"
    write_text(feature_path, load_template("feature-brief.md", replacements))
    targets.append(feature_path)

    if not args.no_handoff:
        handoff_path = output_dir / f"handoff-{slug}.md"
        write_text(handoff_path, load_template("handoff-contract.md", replacements))
        targets.append(handoff_path)

    if not args.no_traceability:
        traceability_path = output_dir / f"traceability-{slug}.md"
        write_text(traceability_path, load_template("feature-traceability.md", replacements))
        targets.append(traceability_path)

    if args.with_adr:
        adr_path = output_dir / f"adr-{slug}.md"
        write_text(adr_path, load_template("adr.md", replacements))
        targets.append(adr_path)

    if args.with_test_plan:
        test_path = output_dir / f"test-plan-{slug}.md"
        write_text(test_path, load_template("test-plan.md", replacements))
        targets.append(test_path)

    if args.with_eval_plan:
        eval_path = output_dir / f"eval-plan-{slug}.md"
        write_text(eval_path, load_template("eval-plan.md", replacements))
        targets.append(eval_path)

    if args.json:
        print(
            json.dumps(
                {
                    "feature_name": args.feature_name,
                    "slug": slug,
                    "output_dir": str(output_dir),
                    "created": [str(path) for path in targets],
                },
                indent=2,
            )
        )
    else:
        print("Created:")
        for path in targets:
            print(f"- {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
