#!/usr/bin/env python3
from __future__ import annotations

import json

from _studio_common import ACTIVE_DIR, repo_summary, unresolved_placeholders

def main() -> int:
    summary = repo_summary()
    unresolved = {}
    for path in ACTIVE_DIR.glob("*.md"):
        placeholders = unresolved_placeholders(path.read_text(encoding="utf-8"))
        if placeholders:
            unresolved[path.name] = placeholders

    print("Studio Status")
    print("=============")
    for key, value in summary.items():
        print(f"{key}: {value}")
    print()
    if unresolved:
        print("Docs with unresolved placeholders:")
        for name, placeholders in unresolved.items():
            print(f"- {name}: {', '.join(placeholders)}")
    else:
        print("No unresolved placeholders in active docs.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
