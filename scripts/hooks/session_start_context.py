#!/usr/bin/env python3
from __future__ import annotations

import json
import sys


def main() -> int:
    payload = json.load(sys.stdin)
    source = payload.get("source", "startup")
    context = (
        "Review docs/reference/code-review.md for review expectations, "
        "docs/reference/eval-strategy.md for shared-behavior changes, and "
        "docs/setup/optional-codex-hooks.md if hooks are enabled."
    )
    print(
        json.dumps(
            {
                "hookSpecificOutput": {
                    "hookEventName": "SessionStart",
                    "additionalContext": f"Session source: {source}. {context}",
                }
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
