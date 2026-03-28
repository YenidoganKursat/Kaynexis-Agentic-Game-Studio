#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from _studio_common import REPO_ROOT

DOC_RULES = [
    {
        "prefixes": ("src/", "project.godot", "export_presets.cfg"),
        "docs": [
            "studio/docs/active/game-brief.md",
            "studio/docs/active/current-sprint.md",
            "studio/docs/active/engine-profile.md",
        ],
        "reason": "runtime or root game surface changed",
    },
    {
        "prefixes": ("scripts/", ".github/workflows/", "Makefile", "Dockerfile", "docker-compose.yml"),
        "docs": [
            "studio/docs/active/build-pipeline.md",
            "docs/reference/ci-cd-architecture.md",
            "docs/setup/github-maintainer-setup.md",
        ],
        "reason": "tooling or CI surface changed",
    },
    {
        "prefixes": ("studio/presets/genre/", "docs/research/game-development/genre/"),
        "docs": [
            "docs/reference/genre-presets.md",
            "studio/docs/active/genre-starter.md",
            "docs/research/game-development/genre/README.md",
        ],
        "reason": "genre guidance surface changed",
    },
    {
        "prefixes": ("studio/starter-kits/", "scripts/unity_adapter.py", "scripts/unreal_adapter.py", "scripts/godot_smoke.py", "scripts/godot_export.py"),
        "docs": [
            "studio/docs/active/engine-profile.md",
            "studio/docs/active/build-pipeline.md",
            "docs/reference/engine-selection-guide.md",
        ],
        "reason": "engine contract or starter-kit surface changed",
    },
    {
        "prefixes": ("studio/checklists/", ".codex/agents/", ".agents/skills/"),
        "docs": [
            "docs/reference/engine-agent-guidelines.md",
            "docs/reference/workflow-recipes.md",
            "docs/reference/task-prompt-examples.md",
        ],
        "reason": "agent, skill, or checklist behavior changed",
    },
    {
        "prefixes": ("studio/docs/templates/", "docs/examples/"),
        "docs": [
            "docs/examples/README.md",
            "docs/reference/feature-traceability.md",
            "docs/reference/handoff-contracts.md",
        ],
        "reason": "template or example surface changed",
    },
]


def changed_paths_from_git() -> list[str]:
    result = subprocess.run(
        ["git", "status", "--short"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return []
    paths: list[str] = []
    for line in result.stdout.splitlines():
        if not line.strip():
            continue
        path = line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1].strip()
        paths.append(path)
    return paths


def resolve_recommendations(paths: list[str]) -> list[dict[str, object]]:
    recommendations: dict[str, dict[str, object]] = {}
    for path in paths:
        normalized = path.replace("\\", "/")
        for rule in DOC_RULES:
            if any(normalized.startswith(prefix) or normalized == prefix for prefix in rule["prefixes"]):
                for doc in rule["docs"]:
                    entry = recommendations.setdefault(
                        doc,
                        {"doc": doc, "reasons": set(), "triggered_by": set()},
                    )
                    entry["reasons"].add(str(rule["reason"]))
                    entry["triggered_by"].add(normalized)
    output: list[dict[str, object]] = []
    for doc in sorted(recommendations):
        item = recommendations[doc]
        output.append(
            {
                "doc": item["doc"],
                "reasons": sorted(item["reasons"]),
                "triggered_by": sorted(item["triggered_by"]),
            }
        )
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description="Suggest which docs may need refresh based on changed repo paths.")
    parser.add_argument("paths", nargs="*", help="Explicit changed paths. If omitted, uses git status.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    paths = args.paths or changed_paths_from_git()
    payload = {
        "paths": paths,
        "recommendations": resolve_recommendations(paths),
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        if not paths:
            print("No changed paths found.")
            return 0
        print("Changed paths:")
        for path in paths:
            print(f"- {path}")
        if not payload["recommendations"]:
            print("No doc recommendations.")
            return 0
        print("Suggested docs to review:")
        for item in payload["recommendations"]:
            print(f"- {item['doc']}")
            for reason in item["reasons"]:
                print(f"  reason: {reason}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
