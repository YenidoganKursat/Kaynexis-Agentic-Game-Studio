#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _studio_common import ACTIVE_DIR, list_markdown_files, unresolved_placeholders

REQUIRED_FILES = {
    "game-brief.md": ["## High concept", "## Player fantasy", "## Core pillars", "## Scope guardrails"],
    "genre-starter.md": ["## Selected preset", "## Default assumptions", "## Must-watch risks", "## Suggested first slice"],
    "engine-profile.md": ["## Engine", "## Repository layout", "## Build targets"],
    "current-sprint.md": ["## Sprint goal", "## In scope", "## Definition of done"],
    "milestones.md": ["## Milestones"],
    "risk-register.md": ["## Risk table"],
    "decision-log.md": ["## Recent decisions"],
}

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate active studio docs.")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings such as unresolved placeholders.")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    for name, required_sections in REQUIRED_FILES.items():
        path = ACTIVE_DIR / name
        if not path.exists():
            errors.append(f"Missing required doc: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"Doc missing top-level heading: {path}")
        for section in required_sections:
            if section not in text:
                errors.append(f"Missing section '{section}' in {path}")
        placeholders = unresolved_placeholders(text)
        if placeholders:
            warnings.append(f"Unresolved placeholders in {path}: {', '.join(placeholders)}")

    active_docs = list_markdown_files(ACTIVE_DIR)
    if not active_docs:
        errors.append("No active docs found.")

    for line in errors:
        print(f"ERROR: {line}")
    for line in warnings:
        print(f"WARNING: {line}")

    if not errors and not warnings:
        print("Docs validation passed.")
    return 1 if errors or (args.strict and warnings) else 0

if __name__ == "__main__":
    raise SystemExit(main())
