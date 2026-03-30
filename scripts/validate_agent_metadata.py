#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import tomllib
from pathlib import Path

from _studio_common import REPO_ROOT

AGENTS_DIR = REPO_ROOT / ".codex" / "agents"
CHECKLISTS_DIR = REPO_ROOT / "studio" / "checklists"

REQUIRED_KEYS = {
    "name",
    "description",
    "public_title",
    "model",
    "sandbox_mode",
    "nickname_candidates",
    "domains",
    "engine_tags",
    "milestone_tags",
    "default_checklist_layers",
    "developer_instructions",
}

ALLOWED_ENGINE_TAGS = {"shared", "godot-4", "unity-6", "unreal-5"}
ALLOWED_MILESTONE_TAGS = {"prototype", "vertical-slice", "demo", "launch"}


def validate_agent(path: Path) -> list[str]:
    errors: list[str] = []
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    missing = sorted(REQUIRED_KEYS - set(data.keys()))
    for key in missing:
        errors.append(f"{path.name}: missing required key '{key}'")

    name = str(data.get("name", "")).strip()
    if name != path.stem:
        errors.append(f"{path.name}: name '{name}' does not match file stem '{path.stem}'")

    for list_key in ("nickname_candidates", "domains", "engine_tags", "milestone_tags", "default_checklist_layers"):
        value = data.get(list_key)
        if not isinstance(value, list) or not value:
            errors.append(f"{path.name}: '{list_key}' must be a non-empty list")

    for tag in data.get("engine_tags", []):
        if str(tag) not in ALLOWED_ENGINE_TAGS:
            errors.append(f"{path.name}: unknown engine tag '{tag}'")

    for tag in data.get("milestone_tags", []):
        if str(tag) not in ALLOWED_MILESTONE_TAGS:
            errors.append(f"{path.name}: unknown milestone tag '{tag}'")

    for layer in data.get("default_checklist_layers", []):
        checklist_path = CHECKLISTS_DIR / f"{layer}.toml"
        if not checklist_path.exists():
            errors.append(f"{path.name}: missing checklist layer '{layer}' -> {checklist_path.relative_to(REPO_ROOT)}")

    instructions = str(data.get("developer_instructions", "")).strip()
    if len(instructions) < 80:
        errors.append(f"{path.name}: developer_instructions look too small to be useful")

    public_title = str(data.get("public_title", "")).strip()
    if not public_title:
        errors.append(f"{path.name}: public_title must be a non-empty string")

    return errors


def collect_errors() -> list[str]:
    errors: list[str] = []
    seen_titles: dict[str, Path] = {}
    for path in sorted(AGENTS_DIR.glob("*.toml")):
        data = tomllib.loads(path.read_text(encoding="utf-8"))
        title = str(data.get("public_title", "")).strip()
        if title:
            previous = seen_titles.get(title)
            if previous is None:
                seen_titles[title] = path
            else:
                errors.append(
                    f"{path.name}: public_title '{title}' duplicates '{previous.name}'"
                )
        errors.extend(validate_agent(path))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Codex agent metadata consistency.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    errors = collect_errors()
    if args.json:
        print(json.dumps({"errors": errors}, indent=2))
    else:
        if errors:
            for item in errors:
                print(f"ERROR: {item}")
        else:
            print("Agent metadata validation passed.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
