#!/usr/bin/env python3
from __future__ import annotations

import datetime as dt
import json
import os
import re
import tomllib
from collections import OrderedDict
from pathlib import Path
from typing import Any

from _studio_common import REPO_ROOT, default_engine_version, detect_engine, write_text

STUDIO_CONFIG_PATH = REPO_ROOT / "studio.toml"
STARTER_KITS_DIR = REPO_ROOT / "studio" / "starter-kits"
CHECKLISTS_DIR = REPO_ROOT / "studio" / "checklists"
RESEARCH_DIR = REPO_ROOT / "docs" / "research" / "game-development"
RESEARCH_TEMPLATE_PATH = RESEARCH_DIR / "templates" / "research-note.md"
DEFAULT_MILESTONE = "prototype"

TASK_DISCIPLINE_KEYWORDS: dict[str, tuple[str, ...]] = {
    "bugfix": ("bug", "crash", "soft lock", "regression", "issue", "broken", "freeze"),
    "performance": (
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
    ),
    "backend": ("multiplayer", "coop", "co-op", "netcode", "backend", "lobby", "server", "matchmaking", "sync"),
    "build-release": (
        "starter kit",
        "starter-kit",
        "engine setup",
        "build pipeline",
        "artifact",
        "package",
        "packaging",
        "export",
        "batchmode",
        "buildcookrun",
        "uat",
        "asmdef",
        "manifest",
        "module",
        "plugin",
        "uproject",
    ),
    "save": ("save", "checkpoint", "load", "profile", "migration", "cloud save", "persistence"),
    "gameplay": (
        "combat",
        "enemy",
        "boss",
        "character",
        "player",
        "avatar",
        "interaction",
        "interact",
        "pickup",
        "trigger",
        "lever",
        "chest",
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
        "inventory",
        "item",
        "loot",
        "equipment",
        "equip",
        "loadout",
        "craft",
        "crafting",
        "recipe",
        "recipes",
        "gathering",
        "workbench",
        "forge",
        "resource node",
        "patrol",
        "aggro",
        "perception",
        "behavior tree",
        "blackboard",
        "locomotion",
        "companion",
        "companions",
        "follower",
        "followers",
        "squad",
        "formation",
    ),
    "narrative": ("narrative", "story", "dialogue", "quest", "mission", "cutscene"),
    "ui-ux": (
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
    ),
    "content-pipeline": ("art", "style", "vfx", "audio", "sound", "pipeline", "import", "content"),
    "release": ("release", "launch", "store", "steam", "festival", "marketing", "announcement", "wishlist"),
    "porting": ("console", "cert", "submission", "port", "switch", "playstation", "xbox", "compliance", "rating"),
    "mobile": ("mobile", "ios", "android", "touch", "free to play", "f2p"),
    "research": ("research", "architecture", "benchmark", "reference", "investigate"),
}

ENGINE_TEXT_HINTS: dict[str, tuple[str, ...]] = {
    "godot-4": ("godot", "godot 4"),
    "unity-6": ("unity", "unity 6", "unity 6000"),
    "unreal-5": ("unreal", "unreal 5", "ue5"),
}

MATCH_SPLIT_RE = re.compile(r"[^a-z0-9]+")

DISCIPLINE_RESEARCH_REFS: dict[str, list[str]] = {
    "bugfix": [
        "docs/research/game-development/production/incident-hotfix-and-rollback.md",
    ],
    "build-release": [
        "docs/research/game-development/production/release-validation.md",
        "docs/research/game-development/production/platform-readiness-pc-web-mobile-console.md",
        "docs/research/game-development/production/incident-hotfix-and-rollback.md",
    ],
    "gameplay": [
        "docs/research/game-development/systems/gameplay-loop-state-and-update-architecture.md",
        "docs/research/game-development/systems/combat-damage-and-effects-architecture.md",
        "docs/research/game-development/systems/ai-navigation-and-entity-scale-architecture.md",
        "docs/research/game-development/engines/godot-4-architecture.md",
        "docs/research/game-development/engines/unity-6-architecture.md",
        "docs/research/game-development/engines/unreal-5-architecture.md",
    ],
    "save": [
        "docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md",
    ],
    "performance": [
        "docs/research/game-development/systems/ai-navigation-and-entity-scale-architecture.md",
        "docs/research/game-development/foundations/ai-pathfinding-and-decision-foundations.md",
    ],
    "content-pipeline": [
        "docs/research/game-development/production/content-pipeline.md",
    ],
    "release": [
        "docs/research/game-development/production/release-validation.md",
        "docs/research/game-development/production/platform-readiness-pc-web-mobile-console.md",
        "docs/research/game-development/production/incident-hotfix-and-rollback.md",
    ],
    "porting": [
        "docs/research/game-development/production/platform-readiness-pc-web-mobile-console.md",
    ],
    "mobile": [
        "docs/research/game-development/production/platform-readiness-pc-web-mobile-console.md",
        "docs/research/game-development/production/incident-hotfix-and-rollback.md",
    ],
    "research": [
        "docs/research/game-development/README.md",
        "docs/research/game-development/foundations/README.md",
    ],
    "ui-ux": [
        "docs/research/game-development/systems/ui-hud-menu-and-screen-flow-architecture.md",
        "docs/research/game-development/systems/input-controls-camera-and-remapping-architecture.md",
        "docs/research/game-development/foundations/game-feel-usability-and-accessibility-foundations.md",
    ],
    "narrative": [
        "docs/reference/lorebook-methodology.md",
        "docs/reference/world-graph-methodology.md",
        "docs/research/game-development/narrative/lorebook-world-state-and-canon-architecture.md",
        "docs/research/game-development/narrative/world-graph-relationship-history-architecture.md",
        "docs/research/game-development/systems/dialogue-conversation-and-quest-state-architecture.md",
        "docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md",
    ],
}

TASK_CONTEXT_RESEARCH_REFS: dict[str, dict[str, Any]] = {
    "inventory": {
        "keywords": (
            "inventory",
            "item",
            "loot",
            "equipment",
            "equip",
            "loadout",
            "quick bar",
            "quickbar",
            "consumable",
            "stack",
        ),
        "refs": [
            "docs/research/game-development/systems/inventory-equipment-and-item-architecture.md",
            "docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md",
        ],
    },
    "character": {
        "keywords": (
            "character",
            "player",
            "avatar",
            "locomotion",
            "controller",
            "dash",
            "jump",
            "movement state",
            "ability",
            "class data",
        ),
        "refs": [
            "docs/research/game-development/systems/character-controller-ability-and-state-architecture.md",
            "docs/research/game-development/systems/gameplay-loop-state-and-update-architecture.md",
        ],
    },
    "enemy": {
        "keywords": (
            "enemy",
            "boss",
            "patrol",
            "aggro",
            "perception",
            "encounter",
            "behavior tree",
            "blackboard",
            "state tree",
            "state-tree",
            "eqs",
            "ai",
        ),
        "refs": [
            "docs/research/game-development/systems/enemy-roster-behavior-and-encounter-architecture.md",
            "docs/research/game-development/systems/ai-navigation-and-entity-scale-architecture.md",
            "docs/research/game-development/systems/combat-damage-and-effects-architecture.md",
        ],
    },
    "controls": {
        "keywords": (
            "input",
            "controls",
            "controller",
            "gamepad",
            "keyboard",
            "mouse",
            "remap",
            "rebind",
            "camera",
            "pause",
            "focus",
            "navigation",
        ),
        "refs": [
            "docs/research/game-development/systems/input-controls-camera-and-remapping-architecture.md",
            "docs/research/game-development/systems/ui-hud-menu-and-screen-flow-architecture.md",
        ],
    },
    "ui": {
        "keywords": (
            "hud",
            "menu",
            "settings",
            "screen",
            "overlay",
            "tooltip",
            "onboarding",
            "pause menu",
            "inventory ui",
            "upgrade screen",
            "ui",
        ),
        "refs": [
            "docs/research/game-development/systems/ui-hud-menu-and-screen-flow-architecture.md",
            "docs/research/game-development/systems/input-controls-camera-and-remapping-architecture.md",
        ],
    },
    "visuals": {
        "keywords": (
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
        ),
        "refs": [
            "docs/research/game-development/foundations/game-feel-usability-and-accessibility-foundations.md",
            "docs/research/game-development/engines/godot-4-visuals-animation-playbook.md",
            "docs/research/game-development/engines/unity-6-visuals-animation-playbook.md",
            "docs/research/game-development/engines/unreal-5-visuals-animation-playbook.md",
        ],
    },
    "abilities": {
        "keywords": (
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
            "active ability",
            "ability",
            "cooldown",
            "cooldowns",
            "boon",
            "boons",
            "meta unlock",
            "meta unlocks",
            "unlock",
            "unlocks",
            "build variety",
        ),
        "refs": [
            "docs/research/game-development/systems/abilities-skill-trees-upgrades-and-build-architecture.md",
            "docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md",
            "docs/research/game-development/systems/combat-damage-and-effects-architecture.md",
        ],
    },
    "interactions": {
        "keywords": (
            "interact",
            "interaction",
            "pickup",
            "prompt",
            "lever",
            "chest",
            "usable object",
            "trigger",
            "world object",
            "loot pickup",
        ),
        "refs": [
            "docs/research/game-development/systems/interactions-pickups-and-world-object-architecture.md",
            "docs/research/game-development/systems/inventory-equipment-and-item-architecture.md",
            "docs/research/game-development/systems/ui-hud-menu-and-screen-flow-architecture.md",
        ],
    },
    "crafting": {
        "keywords": (
            "craft",
            "crafting",
            "recipe",
            "recipes",
            "gather",
            "gathering",
            "harvest",
            "workbench",
            "forge",
            "refine",
            "resource flow",
            "production chain",
        ),
        "refs": [
            "docs/research/game-development/systems/crafting-recipes-and-resource-flow-architecture.md",
            "docs/research/game-development/systems/inventory-equipment-and-item-architecture.md",
            "docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md",
        ],
    },
    "dialogue": {
        "keywords": (
            "dialogue",
            "conversation",
            "branching",
            "quest stage",
            "quest",
            "mission",
            "cutscene",
            "approval",
            "relationship state",
            "scene state",
            "lorebook",
            "lore book",
            "world bible",
            "story bible",
            "canon",
            "codex",
            "archive",
            "bestiary",
            "world knowledge",
        ),
        "refs": [
            "docs/research/game-development/systems/dialogue-conversation-and-quest-state-architecture.md",
            "docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md",
        ],
    },
    "world_graph": {
        "keywords": (
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
        ),
        "refs": [
            "docs/reference/world-graph-methodology.md",
            "docs/research/game-development/narrative/world-graph-relationship-history-architecture.md",
            "docs/research/game-development/narrative/lorebook-world-state-and-canon-architecture.md",
            "docs/research/game-development/systems/dialogue-conversation-and-quest-state-architecture.md",
        ],
    },
    "lorebook": {
        "keywords": (
            "lorebook",
            "lore book",
            "world bible",
            "story bible",
            "canon",
            "codex",
            "archive",
            "bestiary",
            "world knowledge",
            "faction canon",
            "story canon",
        ),
        "refs": [
            "docs/reference/lorebook-methodology.md",
            "docs/research/game-development/narrative/lorebook-world-state-and-canon-architecture.md",
            "docs/research/game-development/systems/dialogue-conversation-and-quest-state-architecture.md",
        ],
    },
    "party": {
        "keywords": (
            "companion",
            "companions",
            "follower",
            "followers",
            "party member",
            "party members",
            "squad",
            "formation",
            "recruitable ally",
            "escort ai",
            "loyalty",
            "approval",
        ),
        "refs": [
            "docs/research/game-development/systems/party-companion-and-squad-architecture.md",
            "docs/research/game-development/systems/character-controller-ability-and-state-architecture.md",
            "docs/research/game-development/systems/enemy-roster-behavior-and-encounter-architecture.md",
        ],
    },
    "handoff": {
        "keywords": (
            "handoff",
            "handover",
            "traceability",
            "doc sync",
            "docs sync",
            "sync docs",
            "refresh docs",
            "release notes",
            "release note",
        ),
        "refs": [
            "docs/reference/handoff-contracts.md",
            "docs/reference/feature-traceability.md",
            "docs/research/game-development/production/incident-hotfix-and-rollback.md",
        ],
    },
    "hotfix": {
        "keywords": (
            "hotfix",
            "rollback",
            "roll back",
            "incident",
            "live issue",
            "live-issue",
            "known good build",
            "known-good build",
            "crash rollback",
        ),
        "refs": [
            "docs/research/game-development/production/incident-hotfix-and-rollback.md",
            "docs/research/game-development/production/release-validation.md",
        ],
    },
    "foundations_design": {
        "keywords": (
            "mda",
            "gameflow",
            "flow",
            "motivation",
            "engagement",
            "aesthetic",
            "aesthetics",
            "dynamics",
            "mechanics",
            "autonomy",
            "competence",
            "relatedness",
            "pens",
        ),
        "refs": [
            "docs/research/game-development/foundations/design-frameworks-mda-gameflow-and-sdt.md",
        ],
    },
    "foundations_feel": {
        "keywords": (
            "game feel",
            "feel",
            "readability",
            "feedback",
            "juiciness",
            "usability",
            "heuristic",
            "heuristics",
            "accessibility",
            "subtitle",
            "caption",
            "contrast",
        ),
        "refs": [
            "docs/research/game-development/foundations/game-feel-usability-and-accessibility-foundations.md",
        ],
    },
    "foundations_ai": {
        "keywords": (
            "a*",
            "astar",
            "heuristic search",
            "hpa*",
            "hpa",
            "goap",
            "planner",
            "planning",
            "behavior tree",
            "decision architecture",
            "utility ai",
        ),
        "refs": [
            "docs/research/game-development/foundations/ai-pathfinding-and-decision-foundations.md",
        ],
    },
    "foundations_difficulty": {
        "keywords": (
            "difficulty",
            "difficulty curve",
            "challenge curve",
            "balance",
            "adaptation",
            "dda",
            "dynamic difficulty",
            "rubber band",
            "rubber-banding",
            "pacing",
        ),
        "refs": [
            "docs/research/game-development/foundations/difficulty-balance-and-adaptation-foundations.md",
        ],
    },
    "genre_advanced": {
        "keywords": (
            "genre",
            "preset",
            "playbook",
            "contrast set",
            "contrast-set",
            "maturity",
            "scaling",
            "advanced genre",
            "genre support",
            "genre architecture",
            "genre model",
        ),
        "refs": [
            "docs/research/game-development/genre/genre-advanced-development-framework.md",
            "docs/research/game-development/genre/genre-development-playbook.md",
            "docs/research/game-development/genre/genre-design-pattern-catalog.md",
            "docs/research/game-development/genre/genre-example-matrix.md",
        ],
    },
}

ENGINE_RESEARCH_REFS: dict[str, list[str]] = {
    "godot-4": [
        "docs/research/game-development/engines/godot-4-architecture.md",
        "docs/research/game-development/engines/godot-4-class-editor-object-map.md",
        "docs/research/game-development/engines/godot-4-2d-3d-class-and-mechanic-guide.md",
        "docs/research/game-development/engines/godot-4-2d-3d-navigation-damage-performance.md",
        "docs/research/game-development/engines/godot-4-systems-playbook.md",
        "docs/research/game-development/engines/godot-4-visuals-animation-playbook.md",
    ],
    "unity-6": [
        "docs/research/game-development/engines/unity-6-architecture.md",
        "docs/research/game-development/engines/unity-6-class-editor-object-map.md",
        "docs/research/game-development/engines/unity-6-2d-3d-class-and-mechanic-guide.md",
        "docs/research/game-development/engines/unity-6-2d-3d-navigation-damage-performance.md",
        "docs/research/game-development/engines/unity-6-systems-playbook.md",
        "docs/research/game-development/engines/unity-6-visuals-animation-playbook.md",
    ],
    "unreal-5": [
        "docs/research/game-development/engines/unreal-5-architecture.md",
        "docs/research/game-development/engines/unreal-5-class-editor-object-map.md",
        "docs/research/game-development/engines/unreal-5-2d-3d-class-and-mechanic-guide.md",
        "docs/research/game-development/engines/unreal-5-2d-3d-navigation-damage-performance.md",
        "docs/research/game-development/engines/unreal-5-systems-playbook.md",
        "docs/research/game-development/engines/unreal-5-visuals-animation-playbook.md",
    ],
}

AGENT_FALLBACKS: dict[str, dict[str, Any]] = {
    "gameplay_programmer": {
        "domains": ["gameplay"],
        "engine_tags": ["shared"],
        "milestone_tags": ["prototype", "vertical-slice"],
        "default_checklist_layers": ["base/repo-health", "discipline/gameplay", "milestone/prototype"],
    },
    "game_designer": {
        "domains": ["gameplay", "systems"],
        "engine_tags": ["shared"],
        "milestone_tags": ["prototype", "vertical-slice"],
        "default_checklist_layers": ["base/feature-slice", "discipline/gameplay", "discipline/research"],
    },
    "godot_specialist": {
        "domains": ["engine-setup", "gameplay"],
        "engine_tags": ["godot-4"],
        "milestone_tags": ["prototype", "vertical-slice"],
        "default_checklist_layers": ["base/repo-health", "engine/godot-4", "discipline/gameplay"],
    },
    "unity_specialist": {
        "domains": ["engine-setup", "tools"],
        "engine_tags": ["unity-6"],
        "milestone_tags": ["prototype", "vertical-slice"],
        "default_checklist_layers": ["base/repo-health", "engine/unity-6", "discipline/content-pipeline"],
    },
    "unreal_specialist": {
        "domains": ["engine-setup", "build"],
        "engine_tags": ["unreal-5"],
        "milestone_tags": ["prototype", "vertical-slice"],
        "default_checklist_layers": ["base/repo-health", "engine/unreal-5", "discipline/build-release"],
    },
    "producer": {
        "domains": ["production", "planning"],
        "engine_tags": ["shared"],
        "milestone_tags": ["prototype", "vertical-slice", "demo", "launch"],
        "default_checklist_layers": ["base/feature-slice", "discipline/research", "milestone/prototype"],
    },
    "technical_director": {
        "domains": ["architecture", "build"],
        "engine_tags": ["shared"],
        "milestone_tags": ["prototype", "vertical-slice", "launch"],
        "default_checklist_layers": ["base/repo-health", "discipline/build-release", "discipline/research"],
    },
    "qa_tester": {
        "domains": ["qa", "validation"],
        "engine_tags": ["shared"],
        "milestone_tags": ["prototype", "vertical-slice", "demo", "launch"],
        "default_checklist_layers": ["base/repo-health", "discipline/ui-ux", "milestone/prototype"],
    },
    "reviewer": {
        "domains": ["review", "qa"],
        "engine_tags": ["shared"],
        "milestone_tags": ["prototype", "vertical-slice", "launch"],
        "default_checklist_layers": ["base/repo-health", "discipline/research", "milestone/vertical-slice"],
    },
}


def load_toml(path: Path) -> dict[str, Any]:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def load_studio_config() -> dict[str, Any]:
    if not STUDIO_CONFIG_PATH.exists():
        return {}
    return load_toml(STUDIO_CONFIG_PATH)


def configured_project_name(default: str | None = None) -> str:
    project = load_studio_config().get("project", {})
    if isinstance(project, dict):
        name = str(project.get("name", "")).strip()
        if name:
            return name
    return default or REPO_ROOT.name


def dump_inline_list(items: list[str]) -> str:
    return "[" + ", ".join(json.dumps(item) for item in items) + "]"


def sync_studio_config(project_name: str, engine: str, engine_version: str, platform: str, genre: str) -> None:
    engine_version = engine_version or default_engine_version(engine)
    config = load_studio_config()
    project = config.setdefault("project", {})
    project["name"] = project_name
    project["primary_engine"] = engine
    existing_supported = list(project.get("supported_engines", [])) if isinstance(project.get("supported_engines"), list) else []
    if engine not in existing_supported:
        existing_supported.append(engine)
    project["supported_engines"] = sorted(existing_supported)
    project["platform"] = platform
    project["genre"] = genre
    project["engine_version"] = engine_version

    lines = [
        "[project]",
        f'name = {json.dumps(str(project.get("name", "Untitled Project")))}',
        f'repo_role = {json.dumps(str(project.get("repo_role", "studio-os")))}',
        f'public_face = {json.dumps(str(project.get("public_face", "codex-first")))}',
        f'language = {json.dumps(str(project.get("language", "en")))}',
        f'primary_engine = {json.dumps(str(project.get("primary_engine", engine)))}',
        f'supported_engines = {dump_inline_list([str(item) for item in project.get("supported_engines", [engine])])}',
        f'platform = {json.dumps(str(project.get("platform", platform)))}',
        f'genre = {json.dumps(str(project.get("genre", genre)))}',
        f'engine_version = {json.dumps(str(project.get("engine_version", engine_version)))}',
        "",
    ]

    ux = config.get("ux", {})
    lines.extend(
        [
            "[ux]",
            f'mode = {json.dumps(str(ux.get("mode", "wizard-first")))}',
            "",
        ]
    )

    checklists = config.get("checklists", {})
    lines.extend(
        [
            "[checklists]",
            f'merge_order = {dump_inline_list([str(item) for item in checklists.get("merge_order", ["base", "engine", "discipline", "milestone", "custom"])])}',
            f'custom_dirs = {dump_inline_list([str(item) for item in checklists.get("custom_dirs", ["studio/checklists/custom"])])}',
            f'default_milestone = {json.dumps(str(checklists.get("default_milestone", DEFAULT_MILESTONE)))}',
            "",
        ]
    )

    research = config.get("research", {})
    lines.extend(
        [
            "[research]",
            f'knowledge_base_dir = {json.dumps(str(research.get("knowledge_base_dir", "docs/research/game-development")))}',
            f'policy = {json.dumps(str(research.get("policy", "official-first")))}',
            f'required_sections = {dump_inline_list([str(item) for item in research.get("required_sections", ["Summary", "Primary sources", "Why this matters to this repo", "Decision impact"])])}',
            "",
        ]
    )

    tools = config.get("tools", {})
    lines.extend(
        [
            "[tools]",
            f'python = {json.dumps(str(tools.get("python", "python3")))}',
            f'godot_bin = {json.dumps(str(tools.get("godot_bin", "")))}',
            f'unity_cli = {json.dumps(str(tools.get("unity_cli", "")))}',
            f'unreal_editor = {json.dumps(str(tools.get("unreal_editor", "")))}',
            f'unreal_uat = {json.dumps(str(tools.get("unreal_uat", "")))}',
        ]
    )
    write_text(STUDIO_CONFIG_PATH, "\n".join(lines))


def project_config_value(section: str, key: str, default: Any = None) -> Any:
    config = load_studio_config()
    data = config.get(section, {})
    if not isinstance(data, dict):
        return default
    return data.get(key, default)


def resolve_tool_path(*, config_key: str, env_keys: list[str]) -> str | None:
    for key in env_keys:
        candidate = os.environ.get(key, "").strip()
        if candidate:
            return candidate
    configured = project_config_value("tools", config_key, "")
    if isinstance(configured, str) and configured.strip():
        return configured.strip()
    return None


def primary_engine_slug() -> str:
    configured = project_config_value("project", "primary_engine")
    if isinstance(configured, str) and configured:
        return configured
    engine = detect_engine()
    return {"godot": "godot-4", "unity": "unity-6", "unreal": "unreal-5"}.get(engine, "godot-4")


def starter_kit_manifest_path(engine_slug: str) -> Path:
    return STARTER_KITS_DIR / engine_slug / "kit.toml"


def load_starter_kit_manifest(engine_slug: str) -> dict[str, Any]:
    path = starter_kit_manifest_path(engine_slug)
    if not path.exists():
        raise FileNotFoundError(f"Starter kit manifest not found: {path}")
    data = load_toml(path)
    data["path"] = path
    return data


def available_starter_kits() -> list[str]:
    if not STARTER_KITS_DIR.exists():
        return []
    return sorted(path.name for path in STARTER_KITS_DIR.iterdir() if path.is_dir() and (path / "kit.toml").exists())


def starter_kit_summary(engine_slug: str) -> dict[str, Any]:
    data = load_starter_kit_manifest(engine_slug)
    return {
        "id": data.get("id", engine_slug),
        "engine": data.get("engine", "unknown"),
        "version_family": data.get("version_family", "unknown"),
        "supported_platforms": list(data.get("supported_platforms", [])),
        "bootstrap_command": data.get("bootstrap_command", ""),
        "smoke_commands": list(data.get("smoke_commands", [])),
        "export_commands": list(data.get("export_commands", [])),
        "validation_steps": list(data.get("validation_steps", [])),
        "scaffold_dir": str((STARTER_KITS_DIR / engine_slug / "scaffold").relative_to(REPO_ROOT)),
    }


def checklist_layer_dir(layer: str) -> Path:
    return CHECKLISTS_DIR / layer


def checklist_manifest_path(layer: str, slug: str) -> Path:
    return checklist_layer_dir(layer) / f"{slug}.toml"


def load_checklist_manifest(path: Path) -> dict[str, Any]:
    data = load_toml(path)
    data["path"] = path
    data.setdefault("item", [])
    return data


def available_checklists(layer: str) -> list[str]:
    directory = checklist_layer_dir(layer)
    if not directory.exists():
        return []
    return sorted(path.stem for path in directory.glob("*.toml"))


def build_match_context(text: str) -> dict[str, object]:
    tokens = tuple(token for token in MATCH_SPLIT_RE.split(text.lower()) if token)
    return {"tokens": set(tokens), "normalized": " ".join(tokens)}


def keyword_matches_context(context: dict[str, object], keyword: str) -> bool:
    normalized_keyword = " ".join(token for token in MATCH_SPLIT_RE.split(keyword.lower()) if token)
    if not normalized_keyword:
        return False
    if " " in normalized_keyword:
        normalized_text = str(context["normalized"])
        return f" {normalized_keyword} " in f" {normalized_text} "
    return normalized_keyword in context["tokens"]


def count_keyword_matches(text: str, keywords: tuple[str, ...] | list[str]) -> int:
    context = build_match_context(text)
    return sum(1 for keyword in keywords if keyword_matches_context(context, keyword))


def infer_disciplines_from_task(task: str) -> list[str]:
    context = build_match_context(task)
    matches: list[str] = []
    for slug, keywords in TASK_DISCIPLINE_KEYWORDS.items():
        if any(keyword_matches_context(context, keyword) for keyword in keywords):
            matches.append(slug)
    if not matches:
        matches.append("research")
    if "gameplay" not in matches and keyword_matches_context(context, "mechanic"):
        matches.append("gameplay")
    return matches


def infer_engine_from_text(text: str) -> str | None:
    context = build_match_context(text)
    for slug, hints in ENGINE_TEXT_HINTS.items():
        if any(keyword_matches_context(context, hint) for hint in hints):
            return slug
    return None


def resolve_checklists(
    *,
    engine_slug: str | None = None,
    disciplines: list[str] | None = None,
    milestone: str | None = None,
    agent_name: str | None = None,
) -> list[dict[str, Any]]:
    engine_slug = engine_slug or primary_engine_slug()
    milestone = milestone or str(project_config_value("checklists", "default_milestone", DEFAULT_MILESTONE))
    disciplines = disciplines or []

    merge_order = project_config_value("checklists", "merge_order", ["base", "engine", "discipline", "milestone", "custom"])
    custom_dirs = [REPO_ROOT / path for path in project_config_value("checklists", "custom_dirs", ["studio/checklists/custom"])]

    requested: list[Path] = []
    if "base" in merge_order:
        for slug in ("repo-health", "feature-slice"):
            path = checklist_manifest_path("base", slug)
            if path.exists():
                requested.append(path)
    if "engine" in merge_order:
        engine_path = checklist_manifest_path("engine", engine_slug)
        if engine_path.exists():
            requested.append(engine_path)
    if "discipline" in merge_order:
        for discipline in disciplines:
            path = checklist_manifest_path("discipline", discipline)
            if path.exists():
                requested.append(path)
    if "milestone" in merge_order:
        milestone_path = checklist_manifest_path("milestone", milestone)
        if milestone_path.exists():
            requested.append(milestone_path)
    if agent_name:
        metadata = agent_metadata(agent_name)
        for ref in metadata.get("default_checklist_layers", []):
            if "/" not in ref:
                continue
            layer, slug = ref.split("/", 1)
            path = checklist_manifest_path(layer, slug)
            if path.exists():
                requested.append(path)
    if "custom" in merge_order:
        for directory in custom_dirs:
            if not directory.exists():
                continue
            for path in sorted(directory.glob("*.toml")):
                requested.append(path)

    merged: OrderedDict[str, dict[str, Any]] = OrderedDict()
    for path in requested:
        manifest = load_checklist_manifest(path)
        source_ref = str(path.relative_to(REPO_ROOT))
        for item in manifest.get("item", []):
            item_id = str(item.get("id", "")).strip()
            if not item_id:
                continue
            merged[item_id] = {
                "id": item_id,
                "title": str(item.get("title", item_id)),
                "severity": str(item.get("severity", "recommended")),
                "applies_when": str(item.get("applies_when", "Always")),
                "validation": str(item.get("validation", "")),
                "owner": str(item.get("owner", "shared")),
                "source": source_ref,
                "engine": str(item.get("engine", "")),
                "milestone": str(item.get("milestone", "")),
            }
    return list(merged.values())


def render_checklist_markdown(items: list[dict[str, Any]], title: str) -> str:
    lines = [f"# {title}", ""]
    if not items:
        lines.append("- No checklist items resolved.")
        return "\n".join(lines)
    for item in items:
        lines.append(
            f"- [{item['severity']}] {item['title']} | when: {item['applies_when']} | validation: {item['validation']} | source: `{item['source']}`"
        )
    return "\n".join(lines)


def agent_metadata(agent_name: str) -> dict[str, Any]:
    path = REPO_ROOT / ".codex" / "agents" / f"{agent_name}.toml"
    if path.exists():
        data = load_toml(path)
        metadata = {
            "domains": list(data.get("domains", [])),
            "engine_tags": list(data.get("engine_tags", [])),
            "milestone_tags": list(data.get("milestone_tags", [])),
            "default_checklist_layers": list(data.get("default_checklist_layers", [])),
        }
        if any(metadata.values()):
            return metadata
    return AGENT_FALLBACKS.get(
        agent_name,
        {
            "domains": ["research"],
            "engine_tags": ["shared"],
            "milestone_tags": [DEFAULT_MILESTONE],
            "default_checklist_layers": ["base/repo-health", "discipline/research", f"milestone/{DEFAULT_MILESTONE}"],
        },
    )


def related_research_refs(disciplines: list[str], engine_slug: str | None = None, task_text: str | None = None) -> list[str]:
    refs: OrderedDict[str, None] = OrderedDict()
    refs["docs/research/game-development/README.md"] = None
    if engine_slug and engine_slug in ENGINE_RESEARCH_REFS:
        for path in ENGINE_RESEARCH_REFS[engine_slug]:
            refs[path] = None
    for discipline in disciplines:
        for path in DISCIPLINE_RESEARCH_REFS.get(discipline, []):
            refs[path] = None
    if task_text:
        context = build_match_context(task_text)
        for item in TASK_CONTEXT_RESEARCH_REFS.values():
            if any(keyword_matches_context(context, keyword) for keyword in item["keywords"]):
                for path in item["refs"]:
                    refs[path] = None
        if any(
            keyword_matches_context(context, keyword)
            for keyword in ("genre", "preset", "playbook", "contrast set", "contrast-set", "maturity", "scaling", "genre support", "genre architecture")
        ):
            refs["docs/research/game-development/genre/genre-advanced-development-framework.md"] = None
    return list(refs.keys())


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "untitled"


def scaffold_research_note(category: str, title: str, sources: list[str] | None = None, slug: str | None = None) -> Path:
    slug = slug or slugify(title)
    target = RESEARCH_DIR / category / f"{slug}.md"
    today = dt.date.today().isoformat()
    source_lines = "\n".join(f"- {source}" for source in (sources or ["Add official primary source URL here."]))
    if RESEARCH_TEMPLATE_PATH.exists():
        template = RESEARCH_TEMPLATE_PATH.read_text(encoding="utf-8")
        body = template.format(
            TITLE=title,
            DATE=today,
            PRIMARY_SOURCES=source_lines,
            SUMMARY="- Capture the key architectural constraints and what changes in the repo because of them.",
            REPO_IMPACT="- Link the finding to a concrete repo decision, checklist, or starter-kit rule.",
            DECISION_IMPACT="- Document what should change in docs, starter kits, or workflows.",
        )
    else:
        body = f"# {title}\n\n## Date\n- {today}\n\n## Primary sources\n{source_lines}\n"
    write_text(target, body)
    return target


def validate_research_note(path: Path) -> list[str]:
    required_sections = project_config_value(
        "research",
        "required_sections",
        ["Summary", "Primary sources", "Why this matters to this repo", "Decision impact"],
    )
    text = path.read_text(encoding="utf-8")
    failures: list[str] = []
    for section in required_sections:
        if f"## {section}" not in text:
            failures.append(f"{path.relative_to(REPO_ROOT)} is missing section '{section}'.")
    if "https://" not in text:
        failures.append(f"{path.relative_to(REPO_ROOT)} does not contain a source link.")
    return failures


def research_notes() -> list[Path]:
    if not RESEARCH_DIR.exists():
        return []
    ignored = {"README.md", "policy.md"}
    return sorted(path for path in RESEARCH_DIR.rglob("*.md") if path.name not in ignored and "templates" not in path.parts)
