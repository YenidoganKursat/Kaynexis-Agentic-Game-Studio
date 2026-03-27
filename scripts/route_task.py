#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from collections import defaultdict

from _studio_common import detect_active_genre, parse_preset_metadata, preset_path

ROUTES = [
    {
        "name": "bug / crash / regression",
        "priority": 0,
        "keywords": ["bug", "crash", "soft lock", "regression", "issue", "broken", "freeze"],
        "skills": ["bug-triage", "patch-hotfix", "qa-matrix"],
        "agents": ["qa_tester", "qa_lead", "lead_programmer"],
        "docs": ["studio/docs/templates/bug-report.md", "studio/docs/templates/crash-triage.md"],
    },
    {
        "name": "performance",
        "keywords": ["fps", "frame", "perf", "performance", "memory", "hitch", "stutter", "battery", "thermal"],
        "skills": ["perf-pass", "mobile-optimization", "web-build-readiness"],
        "agents": ["performance_analyst", "technical_director", "rendering_programmer"],
        "docs": ["studio/docs/templates/perf-pass.md"],
    },
    {
        "name": "multiplayer / backend",
        "keywords": ["multiplayer", "coop", "co-op", "netcode", "backend", "lobby", "server", "matchmaking", "sync"],
        "skills": ["multiplayer-slice", "backend-foundation", "security-threat-model"],
        "agents": ["network_programmer", "backend_engineer", "security_engineer"],
        "docs": ["studio/docs/templates/feature-brief.md", "studio/docs/templates/telemetry-schema.md"],
    },
    {
        "name": "save / persistence",
        "keywords": ["save", "checkpoint", "load", "profile", "migration", "cloud save"],
        "skills": ["save-system", "qa-matrix", "security-threat-model"],
        "agents": ["save_system_engineer", "qa_lead", "security_engineer"],
        "docs": ["studio/docs/templates/save-migration-plan.md", "studio/docs/templates/test-plan.md"],
    },
    {
        "name": "combat / gameplay",
        "keywords": ["combat", "enemy", "boss", "ability", "weapon", "movement", "mechanic"],
        "skills": ["combat-loop", "mechanic-design", "gameplay-slice"],
        "agents": ["combat_designer", "gameplay_programmer", "qa_tester"],
        "docs": ["studio/docs/templates/feature-brief.md", "studio/docs/templates/enemy-archetype.md"],
    },
    {
        "name": "narrative / quest",
        "keywords": ["narrative", "story", "dialogue", "quest", "mission", "cutscene"],
        "skills": ["narrative-pipeline", "quest-flow", "localization-pass"],
        "agents": ["narrative_director", "quest_designer", "localization_lead"],
        "docs": ["studio/docs/templates/quest-brief.md", "studio/docs/templates/localization-glossary.md"],
    },
    {
        "name": "ui / ux / accessibility",
        "keywords": ["ui", "hud", "menu", "ux", "settings", "tutorial", "accessibility", "subtitle"],
        "skills": ["ui-flow", "tutorial-onboarding", "accessibility-audit"],
        "agents": ["ux_designer", "ui_programmer", "accessibility_specialist"],
        "docs": ["studio/docs/templates/accessibility-pass.md", "studio/docs/templates/feature-brief.md"],
    },
    {
        "name": "art / audio / content pipeline",
        "keywords": ["art", "style", "vfx", "audio", "sound", "pipeline", "import", "content"],
        "skills": ["art-style-pack", "audio-style-pack", "content-pipeline"],
        "agents": ["art_director", "audio_director", "technical_artist"],
        "docs": ["studio/docs/templates/art-direction-lite.md", "studio/docs/templates/content-pipeline.md"],
    },
    {
        "name": "release / storefront / marketing",
        "keywords": ["release", "launch", "store", "steam", "festival", "marketing", "announcement", "wishlist"],
        "skills": ["storefront-launch", "marketing-beat-brief", "release-gate"],
        "agents": ["release_manager", "community_manager", "art_director"],
        "docs": ["studio/docs/templates/storefront-checklist.md", "studio/docs/templates/marketing-brief.md"],
    },
    {
        "name": "console / compliance / porting",
        "keywords": ["console", "cert", "submission", "port", "switch", "playstation", "xbox", "compliance", "rating"],
        "skills": ["porting-plan", "console-cert-readiness", "compliance-age-rating"],
        "agents": ["porting_engineer", "certification_manager", "release_manager"],
        "docs": ["studio/docs/templates/cert-checklist.md", "studio/docs/templates/platform-targets.md"],
    },
    {
        "name": "mobile",
        "keywords": ["mobile", "ios", "android", "touch", "battery", "thermal", "free to play", "f2p"],
        "skills": ["mobile-optimization", "monetization-guardrails", "data-telemetry"],
        "agents": ["porting_engineer", "monetization_guardian", "analytics_engineer"],
        "docs": ["studio/docs/templates/monetization-guardrails.md", "studio/docs/templates/telemetry-schema.md"],
    },
]

def main() -> int:
    parser = argparse.ArgumentParser(description="Recommend likely skills, agents, and docs for a given task description.")
    parser.add_argument("task", help="Natural language task description.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    task = args.task.lower()
    scores = []
    for route in ROUTES:
        score = sum(1 for kw in route["keywords"] if kw in task)
        if score:
            scores.append((score, route.get("priority", 1), route))
    scores.sort(key=lambda item: (item[0], item[1]), reverse=True)
    active_genre = detect_active_genre()

    if not scores:
        result = {
            "route": "fallback",
            "skills": ["intake-router", "project-radar", "feature-brief"],
            "agents": ["producer", "technical_director", "game_designer"],
            "docs": ["studio/docs/active/current-sprint.md", "studio/docs/active/risk-register.md"],
        }
    else:
        top = scores[0][2]
        result = {
            "route": top["name"],
            "skills": top["skills"],
            "agents": top["agents"],
            "docs": top["docs"],
        }

    if active_genre:
        metadata = parse_preset_metadata(preset_path("genre", active_genre))
        sections = metadata.get("sections", {})
        result["genre"] = {
            "slug": active_genre,
            "name": metadata.get("display_name", active_genre),
            "summary": metadata.get("summary", ""),
            "skills": sections.get("Recommended first skills", []),
            "docs": ["studio/docs/active/genre-starter.md"],
        }

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Route: {result['route']}")
        if "genre" in result:
            print(f"Genre lens: {result['genre']['name']}")
            if result["genre"]["summary"]:
                print(f"- {result['genre']['summary']}")
            if result["genre"]["skills"]:
                print("Genre skills:")
                for item in result["genre"]["skills"]:
                    print(f"- {item}")
        print("Skills:")
        for item in result["skills"]:
            print(f"- ${item}")
        print("Agents:")
        for item in result["agents"]:
            print(f"- {item}")
        print("Docs:")
        for item in result["docs"]:
            print(f"- {item}")
        if "genre" in result:
            print("Genre docs:")
            for item in result["genre"]["docs"]:
                print(f"- {item}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
