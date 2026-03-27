#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _studio_common import ACTIVE_DIR, PRESET_DIR, append_preset_pack, build_bootstrap_replacements, copy_template_to_active, default_engine_version, sync_active_doc_titles
from studio_core import configured_project_name

DEFAULT_PROJECT_NAME = configured_project_name(Path.cwd().name)

CORE_DOCS = [
    "game-brief.md",
    "genre-starter.md",
    "engine-profile.md",
    "current-sprint.md",
    "milestones.md",
    "risk-register.md",
    "decision-log.md",
    "platform-targets.md",
    "art-direction-lite.md",
    "audio-direction-lite.md",
    "telemetry-schema.md",
    "localization-glossary.md",
    "monetization-guardrails.md",
    "build-pipeline.md",
    "content-pipeline.md",
]

def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap live studio docs from templates.")
    parser.add_argument("--project-name", default=DEFAULT_PROJECT_NAME)
    parser.add_argument("--engine", default="unknown", help="Preset slug under studio/presets/engine (e.g. godot-4)")
    parser.add_argument("--engine-version")
    parser.add_argument("--platform", default="pc-premium", help="Preset slug under studio/presets/platform")
    parser.add_argument("--genre", default="action-roguelite", help="Preset slug under studio/presets/genre")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing active docs.")
    parser.add_argument("--all-templates", action="store_true", help="Copy every template into active docs.")
    args = parser.parse_args()
    args.engine_version = args.engine_version or default_engine_version(args.engine)

    replacements = build_bootstrap_replacements(args.project_name, args.engine, args.engine_version, args.platform, args.genre)

    docs = CORE_DOCS
    if args.all_templates:
        docs = sorted(p.name for p in (ACTIVE_DIR.parent / "templates").glob("*.md"))

    created = []
    for name in docs:
        created.append(copy_template_to_active(name, replacements, overwrite=args.overwrite))
    created.extend(sync_active_doc_titles(args.project_name))

    preset_target = ACTIVE_DIR / "preset-pack.md"
    if args.overwrite or not preset_target.exists():
        preset_target = append_preset_pack(
            engine=args.engine if (PRESET_DIR / "engine" / f"{args.engine}.md").exists() else None,
            platform=args.platform if (PRESET_DIR / "platform" / f"{args.platform}.md").exists() else None,
            genre=args.genre if (PRESET_DIR / "genre" / f"{args.genre}.md").exists() else None,
            replace=True,
        )

    print("Bootstrapped docs:")
    for path in created:
        print(f"- {path.relative_to(Path.cwd()) if path.is_relative_to(Path.cwd()) else path}")
    print(f"- {preset_target.relative_to(Path.cwd()) if preset_target.is_relative_to(Path.cwd()) else preset_target}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
