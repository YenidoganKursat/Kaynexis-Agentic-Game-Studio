#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _studio_common import REPO_ROOT
from doc_sync_audit import changed_paths_from_git, resolve_recommendations


def load_paths_from_file(path: Path) -> list[str]:
    if not path.exists():
        return []
    return [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def gather_paths(explicit_paths: list[str], paths_file: Path | None) -> list[str]:
    if paths_file is not None:
        return load_paths_from_file(paths_file)
    if explicit_paths:
        return explicit_paths
    return changed_paths_from_git()


def build_guard_payload(paths: list[str]) -> dict[str, object]:
    recommendations = resolve_recommendations(paths)
    changed = {path.replace("\\", "/") for path in paths}
    missing_docs: list[dict[str, object]] = []

    for item in recommendations:
        doc = str(item["doc"])
        if doc not in changed:
            missing_docs.append(
                {
                    "doc": doc,
                    "reasons": item["reasons"],
                    "triggered_by": item["triggered_by"],
                }
            )

    return {
        "paths": paths,
        "recommendations": recommendations,
        "missing_docs": missing_docs,
        "passed": not missing_docs,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Fail when code or content changes should have refreshed docs but did not.")
    parser.add_argument("paths", nargs="*", help="Explicit changed paths. If omitted, uses git status.")
    parser.add_argument("--paths-file", type=Path, help="Read changed paths from a newline-separated file.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    paths = gather_paths(args.paths, args.paths_file)
    payload = build_guard_payload(paths)

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        if not paths:
            print("No changed paths found.")
        elif payload["passed"]:
            print("Doc sync guard passed.")
        else:
            print("Doc sync guard failed:")
            for item in payload["missing_docs"]:
                print(f"- {item['doc']}")
                for reason in item["reasons"]:
                    print(f"  reason: {reason}")
    return 0 if payload["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
