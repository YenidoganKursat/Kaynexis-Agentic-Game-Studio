#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _studio_common import ACTIVE_DIR, REPO_ROOT, list_markdown_files, unresolved_placeholders
from studio_core import configured_project_name

REQUIRED_FILES = {
    "game-brief.md": ["## High concept", "## Player fantasy", "## Core pillars", "## Scope guardrails"],
    "genre-starter.md": ["## Selected preset", "## Default assumptions", "## Must-watch risks", "## Suggested first slice", "## Reference games", "## Design focus"],
    "engine-profile.md": ["## Engine", "## Repository layout", "## Build targets"],
    "current-sprint.md": ["## Sprint goal", "## In scope", "## Definition of done"],
    "milestones.md": ["## Milestones"],
    "risk-register.md": ["## Risk table"],
    "decision-log.md": ["## Recent decisions"],
}

PROJECT_SCOPED_DOCS = {
    "art-direction-lite.md",
    "audio-direction-lite.md",
    "build-pipeline.md",
    "content-pipeline.md",
    "current-sprint.md",
    "decision-log.md",
    "engine-profile.md",
    "game-brief.md",
    "localization-glossary.md",
    "milestones.md",
    "monetization-guardrails.md",
    "platform-targets.md",
    "risk-register.md",
    "telemetry-schema.md",
}

DOC_SENTINELS = {
    "art-direction-lite.md": ["- Pillar 1", "- Pillar 2", "- Pillar 3"],
    "audio-direction-lite.md": ["- Pillar 1", "- Pillar 2", "- Pillar 3"],
    "content-pipeline.md": ["- Who edits what and how it enters the game"],
    "telemetry-schema.md": ["- What business/design/quality questions matter"],
    "monetization-guardrails.md": ["- Patterns aligned with player trust"],
    "localization-glossary.md": ["| Example | Meaning | Context | No |"],
}

USER_GUIDE_FILES = {
    "docs/README.md": [
        "## Start Here",
        "setup/first-hour-walkthrough.md",
        "reference/engine-selection-guide.md",
        "reference/workflow-recipes.md",
        "reference/task-prompt-examples.md",
        "reference/lorebook-methodology.md",
        "research/game-development/genre/genre-advanced-development-framework.md",
        "research/game-development/narrative/README.md",
    ],
    "docs/setup/first-hour-walkthrough.md": [
        "## Step 1: Choose the engine family",
        "## Step 8: End the hour with health checks",
        "## Common mistakes",
    ],
    "docs/reference/engine-selection-guide.md": [
        "## Pick Godot 4 when",
        "## Pick Unity 6 when",
        "## Pick Unreal 5 when",
        "## What “support” means in this repo",
    ],
    "docs/reference/workflow-recipes.md": [
        "## Recipe: Start a new game baseline",
        "## Recipe: Validate the engine contract before real work",
        "## Recipe: New contributor handoff",
    ],
    "docs/reference/task-prompt-examples.md": [
        "## Strong task patterns",
        "## Lorebook and narrative",
        "## Good `next` examples",
        "## When to make a feature brief first",
    ],
    "docs/reference/engine-examples.md": [
        "## Example slices by engine",
        "## Same mechanic, three engine examples",
        "## Example validation paths",
    ],
    "docs/reference/handoff-contracts.md": [
        "## Required fields",
        "## Good handoff behavior",
        "## Minimum contract",
    ],
    "docs/reference/feature-traceability.md": [
        "## Use the template",
        "## Why this matters",
        "## Good traceability",
    ],
    "docs/reference/doc-sync-audit.md": [
        "## Command",
        "## What it does",
        "## What it does not do",
    ],
    "docs/reference/balance-simulator.md": [
        "## Command",
        "## What it estimates",
        "## When to use it",
    ],
    "docs/reference/lorebook-methodology.md": [
        "## What a lorebook is in this repo",
        "## Core rule",
        "## Recommended workflow",
        "## Good lorebook entry shape",
        "## Validation questions",
    ],
    "docs/examples/README.md": [
        "feature-brief-golden-example.md",
        "adr-golden-example.md",
        "handoff-contract-golden-example.md",
        "genre-starter-golden-example.md",
        "lorebook-brief-golden-example.md",
    ],
    "docs/research/game-development/narrative/README.md": [
        "Recommended starting notes",
        "lorebook-world-state-and-canon-architecture.md",
    ],
}

RESEARCH_GUIDE_FILES = {
    "docs/research/game-development/foundations/README.md": [
        "Recommended starting notes",
        "design-frameworks-mda-gameflow-and-sdt.md",
        "game-feel-usability-and-accessibility-foundations.md",
        "ai-pathfinding-and-decision-foundations.md",
        "difficulty-balance-and-adaptation-foundations.md",
    ],
    "docs/research/game-development/narrative/README.md": [
        "Recommended starting notes",
        "lorebook-world-state-and-canon-architecture.md",
    ],
    "docs/research/game-development/foundations/design-frameworks-mda-gameflow-and-sdt.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## Practical framing",
    ],
    "docs/research/game-development/foundations/game-feel-usability-and-accessibility-foundations.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## Practical framing",
    ],
    "docs/research/game-development/foundations/ai-pathfinding-and-decision-foundations.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## Practical framing",
    ],
    "docs/research/game-development/foundations/difficulty-balance-and-adaptation-foundations.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## Practical framing",
    ],
    "docs/research/game-development/README.md": [
        "Game Development Research",
        "foundations/",
        "engines/",
        "systems/",
        "narrative/",
        "genre/",
        "genre/genre-advanced-development-framework.md",
        "production/",
    ],
    "docs/research/game-development/genre/README.md": [
        "Recommended starting notes",
        "genre-development-playbook.md",
        "genre-advanced-development-framework.md",
        "auto-battler-architecture.md",
        "deckbuilder-roguelike-architecture.md",
        "survivorlike-architecture.md",
        "grand-strategy-architecture.md",
        "stealth-architecture.md",
        "colony-sim-architecture.md",
        "city-builder-architecture.md",
        "life-sim-architecture.md",
        "hero-shooter-architecture.md",
        "soulslike-architecture.md",
        "factory-automation-architecture.md",
        "metroidvania-architecture.md",
    ],
    "docs/research/game-development/genre/genre-development-playbook.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## How to use this playbook",
        "## Shared development sequence for every genre",
        "## Genre-by-genre guidance",
    ],
    "docs/research/game-development/genre/genre-advanced-development-framework.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## How to use this framework",
        "## Maturity ladder",
        "## Genre family support map",
    ],
    "docs/research/game-development/narrative/lorebook-world-state-and-canon-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## Architecture guidance",
        "## What to watch out for",
        "## Validation expectations",
    ],
    "docs/reference/lorebook-methodology.md": [
        "## What a lorebook is in this repo",
        "## Core rule",
        "## Recommended workflow",
        "## Good lorebook entry shape",
        "## Validation questions",
    ],
    "docs/research/game-development/genre/genre-design-pattern-catalog.md": [
        "### Auto-battler",
        "### Deckbuilder roguelike",
        "### Survivorlike",
        "### Grand strategy",
        "### Stealth",
        "### Colony sim",
        "### City-builder",
        "### Life sim",
        "### Hero shooter",
        "### Factory automation",
        "### Metroidvania",
        "### Soulslike",
    ],
    "docs/research/game-development/genre/genre-example-matrix.md": [
        "`auto-battler`",
        "`deckbuilder-roguelike`",
        "`survivorlike`",
        "`grand-strategy`",
        "`stealth`",
        "`colony-sim`",
        "`city-builder`",
        "`life-sim`",
        "`hero-shooter`",
        "`factory-automation`",
        "`metroidvania`",
        "`soulslike`",
    ],
    "docs/research/game-development/genre/deckbuilder-roguelike-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/auto-battler-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/survivorlike-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/grand-strategy-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/stealth-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/colony-sim-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/city-builder-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/life-sim-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/hero-shooter-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/soulslike-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/factory-automation-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/genre/metroidvania-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/production/platform-readiness-pc-web-mobile-console.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/production/incident-hotfix-and-rollback.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/systems/crafting-recipes-and-resource-flow-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/systems/dialogue-conversation-and-quest-state-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/systems/party-companion-and-squad-architecture.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
    ],
    "docs/research/game-development/engines/README.md": [
        "Recommended read order for an engine-specific task",
        "*-2d-3d-class-and-mechanic-guide.md",
        "*-systems-playbook.md",
        "*-visuals-animation-playbook.md",
    ],
    "docs/research/game-development/engines/godot-4-2d-3d-class-and-mechanic-guide.md": [
        "## Summary",
        "## 2D building blocks",
        "## 3D building blocks",
        "## Common mechanic patterns",
        "## Writing style and naming",
        "## What to watch out for",
    ],
    "docs/research/game-development/engines/godot-4-systems-playbook.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## Input and controls",
    ],
    "docs/research/game-development/engines/godot-4-visuals-animation-playbook.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## 2D visuals",
        "## 3D visuals",
        "## Animation and presentation",
        "## UI image ownership",
        "## VFX and particles",
        "## Common mistakes",
    ],
    "docs/research/game-development/engines/unity-6-2d-3d-class-and-mechanic-guide.md": [
        "## Summary",
        "## 2D building blocks",
        "## 3D building blocks",
        "## Common mechanic patterns",
        "## Writing style and naming",
        "## What to watch out for",
    ],
    "docs/research/game-development/engines/unity-6-systems-playbook.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## Input and controls",
    ],
    "docs/research/game-development/engines/unity-6-visuals-animation-playbook.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## 2D visuals",
        "## 3D visuals",
        "## Animation and presentation",
        "## UI image ownership",
        "## VFX and particles",
        "## Common mistakes",
    ],
    "docs/research/game-development/engines/unreal-5-2d-3d-class-and-mechanic-guide.md": [
        "## Summary",
        "## 2D building blocks",
        "## 3D building blocks",
        "## Common mechanic patterns",
        "## Writing style and naming",
        "## What to watch out for",
    ],
    "docs/research/game-development/engines/unreal-5-systems-playbook.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## Input and controls",
    ],
    "docs/research/game-development/engines/unreal-5-visuals-animation-playbook.md": [
        "## Summary",
        "## Primary sources",
        "## Why this matters to this repo",
        "## Decision impact",
        "## 2D visuals",
        "## 3D visuals",
        "## Animation and presentation",
        "## UI image ownership",
        "## VFX and particles",
        "## Common mistakes",
    ],
}


def collect_doc_findings(active_dir: Path = ACTIVE_DIR) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    project_name = configured_project_name("Untitled Project")

    for name, required_sections in REQUIRED_FILES.items():
        path = active_dir / name
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

    active_docs = list_markdown_files(active_dir)
    if not active_docs:
        errors.append("No active docs found.")
        return errors, warnings

    for path in active_docs:
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        first_line = lines[0] if lines else ""

        if "Untitled Project" in text:
            errors.append(f"Active doc still contains 'Untitled Project': {path}")

        if path.name in PROJECT_SCOPED_DOCS and project_name not in first_line:
            errors.append(f"Project-scoped doc heading does not match studio.toml project name '{project_name}': {path}")

        for sentinel in DOC_SENTINELS.get(path.name, []):
            if sentinel in text:
                errors.append(f"Active doc still contains template-default content '{sentinel}': {path}")

        if path.name.startswith("qa-matrix-") and "TBD" in text:
            errors.append(f"QA matrix still contains unresolved 'TBD' notes: {path}")

    for rel_path, required_markers in USER_GUIDE_FILES.items():
        path = REPO_ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing user-facing guide: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"User-facing guide missing top-level heading: {path}")
        for marker in required_markers:
            if marker not in text:
                errors.append(f"Missing user-guide marker '{marker}' in {path}")

    for rel_path, required_markers in RESEARCH_GUIDE_FILES.items():
        path = REPO_ROOT / rel_path
        if not path.exists():
            errors.append(f"Missing research guide: {path}")
            continue
        text = path.read_text(encoding="utf-8")
        if not text.startswith("# "):
            errors.append(f"Research guide missing top-level heading: {path}")
        for marker in required_markers:
            if marker not in text:
                errors.append(f"Missing research-guide marker '{marker}' in {path}")

    return errors, warnings

def main() -> int:
    parser = argparse.ArgumentParser(description="Validate active studio docs, critical user-facing guides, and engine research guides.")
    parser.add_argument("--strict", action="store_true", help="Fail on warnings such as unresolved placeholders.")
    args = parser.parse_args()

    errors, warnings = collect_doc_findings()

    for line in errors:
        print(f"ERROR: {line}")
    for line in warnings:
        print(f"WARNING: {line}")

    if not errors and not warnings:
        print("Docs validation passed.")
    return 1 if errors or (args.strict and warnings) else 0

if __name__ == "__main__":
    raise SystemExit(main())
