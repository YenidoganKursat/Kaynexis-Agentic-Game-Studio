#!/usr/bin/env python3
from __future__ import annotations

import sys

from codex_studio import main


if __name__ == "__main__":
    argv = sys.argv[1:]
    if argv and argv[0] not in {"init", "next", "checklist", "research", "doctor", "engine"}:
        argv = ["init", *argv]
    elif not argv:
        argv = ["init"]
    sys.argv = [sys.argv[0], *argv]
    raise SystemExit(main())
