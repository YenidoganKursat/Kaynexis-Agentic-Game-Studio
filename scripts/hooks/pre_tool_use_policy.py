#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys

DANGEROUS_PATTERNS = [
    (re.compile(r"\bgit\s+reset\s+--hard\b"), "Blocked destructive git reset."),
    (re.compile(r"\bgit\s+checkout\s+--\b"), "Blocked destructive git checkout."),
    (re.compile(r"\brm\s+-rf\s+/\b"), "Blocked destructive filesystem deletion."),
    (re.compile(r"\bsudo\b"), "Blocked sudo escalation from repo-local hook."),
    (re.compile(r"\bmkfs\b"), "Blocked disk formatting command."),
    (re.compile(r"\bdd\s+if=.*\s+of=/dev/"), "Blocked raw disk write command."),
    (re.compile(r":\(\)\s*\{\s*:\|:&\s*\};:"), "Blocked fork bomb pattern."),
]


def main() -> int:
    payload = json.load(sys.stdin)
    command = str(payload.get("tool_input", {}).get("command", ""))

    for pattern, reason in DANGEROUS_PATTERNS:
        if pattern.search(command):
            print(
                json.dumps(
                    {
                        "hookSpecificOutput": {
                            "hookEventName": "PreToolUse",
                            "permissionDecision": "deny",
                            "permissionDecisionReason": reason,
                        },
                        "systemMessage": reason,
                    }
                )
            )
            return 0

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
