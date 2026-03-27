#!/usr/bin/env python3
from __future__ import annotations

import argparse

from _studio_common import ACTIVE_DIR, load_template, slugify, write_text


def main() -> int:
    parser = argparse.ArgumentParser(description="Scaffold an eval plan into studio/docs/active/")
    parser.add_argument("title", help="Human-readable eval topic.")
    parser.add_argument("--slug", help="Optional custom slug.")
    args = parser.parse_args()

    slug = args.slug or slugify(args.title)
    replacements = {"EVAL_NAME": args.title}

    target = ACTIVE_DIR / f"eval-plan-{slug}.md"
    write_text(target, load_template("eval-plan.md", replacements))
    print(target)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
