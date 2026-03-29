#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json

from _studio_common import detect_active_genre, parse_preset_metadata, preset_path
from studio_core import (
    build_match_context,
    infer_engine_from_text,
    keyword_matches_context,
    primary_engine_slug,
    related_research_refs,
    resolve_checklists,
    starter_kit_summary,
)

ROUTES = [
    {
        "name": "engine / tooling / packaging",
        "priority": 3,
        "keywords": [
            "starter kit",
            "starter-kit",
            "engine setup",
            "build pipeline",
            "artifact",
            "packaging",
            "package",
            "export",
            "batchmode",
            "buildcookrun",
            "uat",
            "asmdef",
            "manifest",
            "module",
            "plugin",
            "uproject",
        ],
        "discipline": "build-release",
        "skills": ["engine-setup", "build-pipeline", "tools-pipeline"],
        "agents": ["technical_director", "build_release_engineer", "engine_programmer"],
        "docs": ["studio/docs/active/engine-profile.md", "studio/docs/active/build-pipeline.md"],
        "validation_steps": ["Generate the exact engine command before implementation.", "Keep the command mirrored in docs and CI once it is real."],
    },
    {
        "name": "bug / crash / regression",
        "priority": 0,
        "keywords": ["bug", "crash", "soft lock", "regression", "issue", "broken", "freeze", "hotfix", "rollback", "incident", "live issue"],
        "discipline": "bugfix",
        "skills": ["bug-triage", "patch-hotfix", "qa-matrix"],
        "agents": ["qa_tester", "qa_lead", "lead_programmer"],
        "docs": ["studio/docs/templates/bug-report.md", "studio/docs/templates/crash-triage.md", "studio/docs/templates/release-checklist.md"],
        "validation_steps": [
            "Reproduce the bug first.",
            "Name the smallest safe rollback or hotfix path before broad implementation.",
            "Document the smallest validation loop after the fix lands.",
        ],
    },
    {
        "name": "performance",
        "keywords": [
            "fps",
            "frame",
            "perf",
            "performance",
            "memory",
            "hitch",
            "stutter",
            "battery",
            "thermal",
            "alloc",
            "allocation",
            "pool",
            "pooling",
            "instancing",
            "multimesh",
            "ecs",
            "dots",
            "burst",
            "mass",
        ],
        "discipline": "performance",
        "skills": ["perf-pass", "mobile-optimization", "web-build-readiness"],
        "agents": ["performance_analyst", "technical_director", "rendering_programmer"],
        "docs": ["studio/docs/templates/perf-pass.md"],
        "validation_steps": [
            "Capture one baseline measurement before tuning.",
            "Check whether representation choice is the real bottleneck before micro-optimizing.",
            "Record the expected perf target in the active docs.",
        ],
    },
    {
        "name": "multiplayer / backend",
        "keywords": ["multiplayer", "coop", "co-op", "netcode", "backend", "lobby", "server", "matchmaking", "sync"],
        "discipline": "backend",
        "skills": ["multiplayer-slice", "backend-foundation", "security-threat-model"],
        "agents": ["network_programmer", "backend_engineer", "security_engineer"],
        "docs": ["studio/docs/templates/feature-brief.md", "studio/docs/templates/telemetry-schema.md"],
        "validation_steps": ["State the authority model.", "Define the narrowest sync test before broad implementation."],
    },
    {
        "name": "save / persistence",
        "keywords": ["save", "checkpoint", "load", "profile", "migration", "cloud save"],
        "discipline": "save",
        "skills": ["save-system", "qa-matrix", "security-threat-model"],
        "agents": ["save_system_engineer", "qa_lead", "security_engineer"],
        "docs": ["studio/docs/templates/save-migration-plan.md", "studio/docs/templates/test-plan.md"],
        "validation_steps": ["Define the save/load happy path.", "Cover one corruption or migration failure mode."],
    },
    {
        "name": "combat / gameplay",
        "keywords": [
            "combat",
            "enemy",
            "boss",
            "character",
            "player",
            "avatar",
            "ability",
            "skill",
            "skills",
            "skill tree",
            "skill trees",
            "upgrade",
            "upgrades",
            "perk",
            "perks",
            "passive",
            "passives",
            "cooldown",
            "cooldowns",
            "boon",
            "boons",
            "unlock",
            "unlocks",
            "meta unlock",
            "meta unlocks",
            "weapon",
            "movement",
            "mechanic",
            "damage",
            "health",
            "hitbox",
            "hurtbox",
            "projectile",
            "pathfinding",
            "navigation",
            "navmesh",
            "astar",
            "raycast",
            "eqs",
            "state tree",
            "state-tree",
            "gameplay ability system",
            "gas",
            "take damage",
            "interact",
            "interaction",
            "pickup",
            "pickups",
            "loot",
            "craft",
            "crafting",
            "recipe",
            "recipes",
            "gathering",
            "workbench",
            "forge",
            "chest",
            "lever",
            "prompt",
            "world object",
            "companion",
            "companions",
            "follower",
            "followers",
            "squad",
            "formation",
        ],
        "discipline": "gameplay",
        "skills": ["combat-loop", "mechanic-design", "gameplay-slice"],
        "agents": ["combat_designer", "gameplay_programmer", "qa_tester"],
        "docs": ["studio/docs/templates/feature-brief.md", "studio/docs/templates/enemy-archetype.md"],
        "validation_steps": [
            "Write down the readable input-to-feedback loop.",
            "State the world stack, navigation model, and damage/contact model before scaling the slice.",
            "Keep one manual or automated proof path for the slice.",
        ],
    },
    {
        "name": "narrative / lorebook",
        "keywords": ["lorebook", "lore book", "world bible", "story bible", "canon", "codex", "archive", "bestiary", "world knowledge"],
        "discipline": "narrative",
        "skills": ["narrative-pipeline", "quest-flow", "content-pipeline"],
        "agents": ["narrative_director", "quest_designer", "localization_lead"],
        "docs": [
            "docs/reference/lorebook-methodology.md",
            "studio/docs/templates/lorebook-brief.md",
            "docs/examples/lorebook-brief-golden-example.md",
            "studio/docs/templates/quest-brief.md",
        ],
        "validation_steps": [
            "Define the canon scope and the systems that own it.",
            "Separate unlock rules from the text entries themselves.",
            "Verify one lookup path, one unlock path, and one save/load resume path.",
        ],
    },
    {
        "name": "narrative / world graph",
        "priority": 2,
        "keywords": [
            "world graph",
            "relationship graph",
            "faction network",
            "history network",
            "timeline",
            "chronology",
            "lineage",
            "biography",
            "organization",
            "org chart",
            "social graph",
            "history",
            "histories",
            "event chain",
            "canon map",
            "map state",
        ],
        "discipline": "narrative",
        "skills": ["narrative-pipeline", "content-pipeline", "quest-flow"],
        "agents": ["narrative_director", "quest_designer", "technical_director"],
        "docs": [
            "docs/reference/world-graph-methodology.md",
            "studio/docs/templates/world-graph-brief.md",
            "docs/examples/world-graph-brief-golden-example.md",
            "studio/docs/templates/lorebook-brief.md",
            "studio/docs/templates/quest-brief.md",
        ],
        "validation_steps": [
            "Define the canonical node and edge types before adding content.",
            "Specify which history beats are append-only and which are snapshot-backed.",
            "Name the cached or indexed read path for the common graph query.",
        ],
    },
    {
        "name": "narrative / quest",
        "keywords": ["narrative", "story", "dialogue", "quest", "mission", "cutscene", "branching conversation"],
        "discipline": "narrative",
        "skills": ["narrative-pipeline", "quest-flow", "localization-pass"],
        "agents": ["narrative_director", "quest_designer", "localization_lead"],
        "docs": ["studio/docs/templates/quest-brief.md", "studio/docs/templates/localization-glossary.md"],
        "validation_steps": ["Define branching or state rules up front.", "Verify one happy path and one recovery path."],
    },
    {
        "name": "ui / ux / accessibility",
        "keywords": [
            "ui",
            "hud",
            "menu",
            "ux",
            "settings",
            "tutorial",
            "accessibility",
            "subtitle",
            "input",
            "controls",
            "controller",
            "gamepad",
            "keyboard",
            "mouse",
            "remap",
            "rebind",
            "pause",
            "camera",
            "focus",
            "navigation",
            "screen",
            "onboarding",
        ],
        "discipline": "ui-ux",
        "skills": ["ui-flow", "tutorial-onboarding", "accessibility-audit"],
        "agents": ["ux_designer", "ui_programmer", "accessibility_specialist"],
        "docs": ["studio/docs/templates/accessibility-pass.md", "studio/docs/templates/feature-brief.md"],
        "validation_steps": ["List all intended states.", "Confirm the critical player prompt remains readable."],
    },
    {
        "name": "visuals / animation / presentation",
        "keywords": [
            "sprite",
            "sprites",
            "sprite sheet",
            "spritesheet",
            "texture",
            "textures",
            "image",
            "images",
            "icon",
            "icons",
            "animation",
            "animated",
            "flipbook",
            "particle",
            "particles",
            "vfx",
            "visual effect",
            "visual effects",
        ],
        "discipline": "content-pipeline",
        "skills": ["art-style-pack", "content-pipeline", "ui-flow"],
        "agents": ["art_director", "technical_artist", "ui_programmer"],
        "docs": ["studio/docs/templates/art-direction-lite.md", "studio/docs/templates/content-pipeline.md"],
        "validation_steps": [
            "State the source art, the playback owner, and whether the presentation is world-facing or UI-facing.",
            "Document the import, atlas, or animation ownership before implementation.",
        ],
    },
    {
        "name": "art / audio / content pipeline",
        "keywords": ["art", "style", "vfx", "audio", "sound", "pipeline", "import", "content"],
        "discipline": "content-pipeline",
        "skills": ["art-style-pack", "audio-style-pack", "content-pipeline"],
        "agents": ["art_director", "audio_director", "technical_artist"],
        "docs": ["studio/docs/templates/art-direction-lite.md", "studio/docs/templates/content-pipeline.md"],
        "validation_steps": ["Define the content handoff path.", "Validate naming or import assumptions before scale grows."],
    },
    {
        "name": "handoff / traceability / doc sync",
        "keywords": [
            "handoff",
            "handover",
            "traceability",
            "doc sync",
            "docs sync",
            "sync docs",
            "refresh docs",
            "release note",
            "release notes",
        ],
        "discipline": "research",
        "skills": ["feature-brief", "qa-matrix", "project-radar"],
        "agents": ["producer", "technical_director", "qa_lead"],
        "docs": ["studio/docs/templates/handoff-contract.md", "studio/docs/templates/feature-traceability.md"],
        "validation_steps": [
            "Link scope, evidence, risk, validation, owner, blockers, and next step.",
            "Verify the feature maps to decision, implementation, tests, and release impact.",
        ],
    },
    {
        "name": "release / storefront / marketing",
        "keywords": ["release", "launch", "store", "steam", "festival", "marketing", "announcement", "wishlist"],
        "discipline": "release",
        "skills": ["storefront-launch", "marketing-beat-brief", "release-gate"],
        "agents": ["release_manager", "community_manager", "art_director"],
        "docs": ["studio/docs/templates/storefront-checklist.md", "studio/docs/templates/marketing-brief.md", "studio/docs/templates/release-checklist.md"],
        "validation_steps": ["Confirm the artifact path.", "Write down known issues and the go/no-go gate."],
    },
    {
        "name": "console / compliance / porting",
        "keywords": ["console", "cert", "submission", "port", "switch", "playstation", "xbox", "compliance", "rating"],
        "discipline": "porting",
        "skills": ["porting-plan", "console-cert-readiness", "compliance-age-rating"],
        "agents": ["porting_engineer", "certification_manager", "release_manager"],
        "docs": ["studio/docs/templates/cert-checklist.md", "studio/docs/templates/platform-targets.md"],
        "validation_steps": ["Document the target platform delta.", "Capture one cert-risk or compliance assumption."],
    },
    {
        "name": "mobile",
        "keywords": ["mobile", "ios", "android", "touch", "battery", "thermal", "free to play", "f2p"],
        "discipline": "mobile",
        "skills": ["mobile-optimization", "monetization-guardrails", "data-telemetry"],
        "agents": ["porting_engineer", "monetization_guardian", "analytics_engineer"],
        "docs": ["studio/docs/templates/monetization-guardrails.md", "studio/docs/templates/telemetry-schema.md"],
        "validation_steps": ["Define the session and input assumptions.", "Confirm battery or monetization risks are documented."],
    },
]


def build_result(route: dict[str, object], include_genre: bool, engine_slug: str) -> dict[str, object]:
    discipline = str(route.get("discipline", "research"))
    engine_summary = starter_kit_summary(engine_slug)
    task_text = str(route.get("task_text", ""))
    result = {
        "route": route["name"],
        "skills": route["skills"],
        "agents": route["agents"],
        "docs": route["docs"],
        "checklists": resolve_checklists(engine_slug=engine_slug, disciplines=[discipline]),
        "engine_kit": engine_summary,
        "engine_actions": engine_summary["smoke_commands"] + engine_summary["export_commands"],
        "research_refs": related_research_refs([discipline], engine_slug=engine_slug, task_text=task_text),
        "validation_steps": route.get("validation_steps", []),
    }
    if include_genre:
        active_genre = detect_active_genre()
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
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Recommend likely skills, agents, and docs for a given task description.")
    parser.add_argument("task", help="Natural language task description.")
    parser.add_argument("--engine", help="Optional engine slug override.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = parser.parse_args()

    match_context = build_match_context(args.task)
    scores = []
    for route in ROUTES:
        score = sum(1 for kw in route["keywords"] if keyword_matches_context(match_context, kw))
        if score:
            scores.append((score, route.get("priority", 1), route))
    scores.sort(key=lambda item: (item[0], item[1]), reverse=True)

    resolved_engine = args.engine or infer_engine_from_text(args.task) or primary_engine_slug()
    if not scores:
        engine_summary = starter_kit_summary(resolved_engine)
        result = {
            "route": "fallback",
            "skills": ["intake-router", "project-radar", "feature-brief"],
            "agents": ["producer", "technical_director", "game_designer"],
            "docs": ["studio/docs/active/current-sprint.md", "studio/docs/active/risk-register.md"],
            "checklists": resolve_checklists(engine_slug=resolved_engine, disciplines=["research"]),
            "engine_kit": engine_summary,
            "engine_actions": engine_summary["smoke_commands"] + engine_summary["export_commands"],
            "research_refs": related_research_refs(["research"], engine_slug=resolved_engine, task_text=args.task),
            "validation_steps": ["Clarify the task into one buildable slice.", "Link the task to a feature brief or active doc before implementation."],
        }
    else:
        selected = dict(scores[0][2])
        selected["task_text"] = args.task
        result = build_result(selected, include_genre=True, engine_slug=resolved_engine)

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
        print("Checklists:")
        for item in result["checklists"]:
            print(f"- [{item['severity']}] {item['title']} ({item['source']})")
        print("Engine actions:")
        for item in result["engine_actions"]:
            print(f"- {item}")
        print("Research refs:")
        for item in result["research_refs"]:
            print(f"- {item}")
        print("Validation steps:")
        for item in result["validation_steps"]:
            print(f"- {item}")
        if "genre" in result:
            print("Genre docs:")
            for item in result["genre"]["docs"]:
                print(f"- {item}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
