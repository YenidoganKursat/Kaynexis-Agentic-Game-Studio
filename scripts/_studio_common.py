#!/usr/bin/env python3
from __future__ import annotations

import argparse
import datetime as _dt
import json
import os
import re
import shutil
import tomllib
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = REPO_ROOT / "studio" / "docs" / "templates"
ACTIVE_DIR = REPO_ROOT / "studio" / "docs" / "active"
PRESET_DIR = REPO_ROOT / "studio" / "presets"
PLACEHOLDER_FILENAMES = {".gitkeep", "AGENTS.md"}
PROJECT_SCOPED_ACTIVE_DOCS = {
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

PLACEHOLDER_DEFAULTS = {
    "PROJECT_NAME": "Untitled Project",
    "ENGINE": "Unknown",
    "ENGINE_VERSION": "TBD",
    "PLATFORM": "PC",
    "GENRE": "unknown",
    "GENRE_NAME": "Unknown Genre",
    "GENRE_SUMMARY": "Genre guidance has not been selected yet.",
    "GENRE_DEFAULT_ASSUMPTIONS": "- Confirm the intended genre loop.",
    "GENRE_RISKS": "- Document the genre-specific top risks.",
    "GENRE_SKILLS": "- $studio-start",
    "GENRE_FIRST_SLICE": "- Define one small playable slice that proves the core loop.",
    "GENRE_FIRST_FEATURE": "First Genre Slice",
    "GENRE_ROUTE_EXAMPLE": "Describe the first genre-specific task",
    "GENRE_REFERENCE_GAMES": "- Add one or two contrast-set references.",
    "GENRE_DESIGN_FOCUS": "- Document the dominant loop and first failure risk.",
    "TODAY": _dt.date.today().isoformat(),
    "FEATURE_NAME": "Example Feature",
    "DECISION_NAME": "Example Decision",
    "TEST_SCOPE": "Example Scope",
    "RELEASE_NAME": "Example Release",
    "BUG_NAME": "Example Bug",
    "PLAYTEST_NAME": "Example Playtest",
    "PERF_SCOPE": "Example Performance Pass",
    "QUEST_NAME": "Example Quest",
    "ENEMY_NAME": "Example Enemy",
    "BOSS_NAME": "Example Boss",
    "EVENT_NAME": "Example Event",
    "EVAL_NAME": "Example Eval",
}

ENGINE_HINTS = {
    "godot": ["project.godot", ".tscn", ".tres", ".gd"],
    "unity": ["Assets", "ProjectSettings", "Packages/manifest.json"],
    "unreal": [".uproject", "Config", "Content", "Source"],
}

ENGINE_SLUG_TO_FAMILY = {
    "godot-4": "godot",
    "unity-6": "unity",
    "unreal-5": "unreal",
}

ENGINE_VERSION_DEFAULTS = {
    "godot-4": "4.x",
    "unity-6": "6000.x",
    "unreal-5": "5.x",
}

GENRE_STARTER_GUIDANCE = {
    "action-roguelite": {
        "GENRE_FIRST_SLICE": "- One combat room with one dodge or signature ability\n- Two enemy roles with readable telegraphs\n- One upgrade choice between encounters",
        "GENRE_FIRST_FEATURE": "First Combat Room",
        "GENRE_ROUTE_EXAMPLE": "Implement the first combat room with one upgrade choice",
    },
    "co-op-survival": {
        "GENRE_FIRST_SLICE": "- Two-player session join flow\n- One gather-craft-survive loop over a short night\n- Shared failure or extraction outcome",
        "GENRE_FIRST_FEATURE": "First Co-op Night",
        "GENRE_ROUTE_EXAMPLE": "Build the first two-player survive-the-night loop",
    },
    "cozy-sim": {
        "GENRE_FIRST_SLICE": "- One short daily routine\n- One place or relationship that visibly improves\n- One clear low-stress reward beat",
        "GENRE_FIRST_FEATURE": "First Cozy Day",
        "GENRE_ROUTE_EXAMPLE": "Design the first low-stress daily routine loop",
    },
    "extraction-lite": {
        "GENRE_FIRST_SLICE": "- One raid with loot pickup and one extraction point\n- Clear risk of loss on failure\n- One safe meta-bank or stash outcome",
        "GENRE_FIRST_FEATURE": "First Extraction Run",
        "GENRE_ROUTE_EXAMPLE": "Prototype the first raid with one extraction point and stash outcome",
    },
    "narrative-adventure": {
        "GENRE_FIRST_SLICE": "- One short chapter or scene\n- One branching conversation with a visible state change\n- One emotional payoff or reveal",
        "GENRE_FIRST_FEATURE": "First Narrative Scene",
        "GENRE_ROUTE_EXAMPLE": "Implement the first branching dialogue scene with one stateful consequence",
    },
    "platformer": {
        "GENRE_FIRST_SLICE": "- One movement verb worth mastering\n- One teach-test-twist obstacle sequence\n- One checkpoint and one recovery path",
        "GENRE_FIRST_FEATURE": "First Movement Gauntlet",
        "GENRE_ROUTE_EXAMPLE": "Build the first teach-test-twist movement gauntlet",
    },
    "puzzle": {
        "GENRE_FIRST_SLICE": "- One clearly taught rule\n- One test room and one twist room\n- One hint or recovery path for misunderstanding",
        "GENRE_FIRST_FEATURE": "First Puzzle Sequence",
        "GENRE_ROUTE_EXAMPLE": "Design the first teach-test-twist puzzle sequence",
    },
    "tactical-rpg": {
        "GENRE_FIRST_SLICE": "- One small skirmish with readable forecasted outcomes\n- One meaningful build or loadout choice\n- One terrain or positioning lesson",
        "GENRE_FIRST_FEATURE": "First Tactical Skirmish",
        "GENRE_ROUTE_EXAMPLE": "Implement the first tactical skirmish with readable damage forecasting",
    },
}

GENRE_REFERENCE_GUIDANCE = {
    "action-roguelite": {
        "GENRE_REFERENCE_GAMES": "- `Dead Cells` -> study repeat-run mastery, failure cadence, and readable combat pressure\n- `Risk of Rain 2` -> study scaling chaos, item-build variance, and escalation pacing",
        "GENRE_DESIGN_FOCUS": "- Dominant loop: survive encounter -> choose build growth -> repeat\n- Architecture watch: separate run state from meta progression early\n- First risk: variety collapse or permanent power trivializing mastery",
    },
    "co-op-survival": {
        "GENRE_REFERENCE_GAMES": "- `Don't Starve Together` -> study shared scarcity, role expression, and co-op recovery",
        "GENRE_DESIGN_FOCUS": "- Dominant loop: gather -> coordinate -> survive -> rebuild\n- Architecture watch: authority for inventory, resource state, and session failure\n- First risk: desync pain or ambiguous shared state",
    },
    "cozy-sim": {
        "GENRE_REFERENCE_GAMES": "- `Stardew Valley` -> study routine breadth, long-term attachment, and low-friction progression\n- `Animal Crossing: New Horizons` -> study persistent place-making and customization-driven reward texture",
        "GENRE_DESIGN_FOCUS": "- Dominant loop: daily routine -> visible improvement -> stronger attachment\n- Architecture watch: persistent world state, schedules, and friction-light UI\n- First risk: chores becoming grind or interface sprawl",
    },
    "extraction-lite": {
        "GENRE_REFERENCE_GAMES": "- `Hunt: Showdown` -> study extraction pressure, information play, and fair high-stakes loss",
        "GENRE_DESIGN_FOCUS": "- Dominant loop: gear up -> risk more -> extract or lose gains\n- Architecture watch: economy trust, loot authority, and extraction-state clarity\n- First risk: unfair loss or exploit-driven economy collapse",
    },
    "narrative-adventure": {
        "GENRE_REFERENCE_GAMES": "- `Life is Strange` -> study visible consequence framing and relationship state\n- `Pentiment` -> study authored scene flow and narrative content density",
        "GENRE_DESIGN_FOCUS": "- Dominant loop: advance scene -> choose -> pay off later\n- Architecture watch: state tracking, branch containment, and content throughput\n- First risk: branching explosion or hidden state bugs",
    },
    "platformer": {
        "GENRE_REFERENCE_GAMES": "- `Dead Cells` -> study movement-combat readability overlap and restart cadence",
        "GENRE_DESIGN_FOCUS": "- Dominant loop: read space -> execute movement -> fail fast -> retry cleaner\n- Architecture watch: movement feel, camera support, and checkpoint cadence\n- First risk: input latency, camera frustration, or unreadable landing zones",
    },
    "puzzle": {
        "GENRE_REFERENCE_GAMES": "- `Portal 2` -> study teach/test/twist sequencing and authored escalation",
        "GENRE_DESIGN_FOCUS": "- Dominant loop: observe rule -> test hypothesis -> learn hidden constraint\n- Architecture watch: rule clarity, misunderstanding recovery, and hint discipline\n- First risk: rule ambiguity or accidental solves",
    },
    "tactical-rpg": {
        "GENRE_REFERENCE_GAMES": "- `Fire Emblem Engage` -> study forecast clarity, turn consequence readability, and mobility-vs-tactics balance",
        "GENRE_DESIGN_FOCUS": "- Dominant loop: forecast -> commit turn -> absorb result -> grow options\n- Architecture watch: forecast UI, rule clarity, and complexity pacing\n- First risk: decision paralysis or opaque combat rules",
    },
}


def slugify(text: str) -> str:
    value = re.sub(r"[^a-zA-Z0-9]+", "-", text.strip().lower()).strip("-")
    return value or "untitled"


def humanize_slug(text: str) -> str:
    return re.sub(r"[-_]+", " ", text.strip()).title() or "Untitled"


def render_placeholders(text: str, replacements: dict[str, str] | None = None) -> str:
    values = dict(PLACEHOLDER_DEFAULTS)
    if replacements:
        values.update({k: str(v) for k, v in replacements.items() if v is not None})
    for key, value in values.items():
        text = text.replace("{" + key + "}", value)
    return text


def load_template(name: str, replacements: dict[str, str] | None = None) -> str:
    path = TEMPLATE_DIR / name
    if not path.exists():
        raise FileNotFoundError(f"Template not found: {path}")
    return render_placeholders(path.read_text(encoding="utf-8"), replacements)


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def copy_template_to_active(name: str, replacements: dict[str, str] | None = None, overwrite: bool = False) -> Path:
    dest = ACTIVE_DIR / name
    if dest.exists() and not overwrite:
        return dest
    write_text(dest, load_template(name, replacements))
    return dest


def list_markdown_files(directory: Path) -> list[Path]:
    return sorted(p for p in directory.rglob("*.md") if p.is_file())


def preset_path(group: str, slug: str) -> Path:
    return PRESET_DIR / group / f"{slug}.md"


def parse_preset_metadata(path: Path) -> dict[str, object]:
    lines = path.read_text(encoding="utf-8").splitlines()
    heading = ""
    heading_index = 0
    for index, line in enumerate(lines):
        if line.startswith("# "):
            heading = line[2:].strip()
            heading_index = index
            break

    summary_lines: list[str] = []
    for line in lines[heading_index + 1 :]:
        stripped = line.strip()
        if not stripped:
            if summary_lines:
                break
            continue
        if stripped.startswith("## "):
            break
        summary_lines.append(stripped)

    sections: dict[str, list[str]] = {}
    current_section: str | None = None
    for line in lines[heading_index + 1 :]:
        stripped = line.strip()
        if stripped.startswith("## "):
            current_section = stripped[3:].strip()
            sections[current_section] = []
            continue
        if current_section and stripped.startswith("- "):
            sections[current_section].append(stripped[2:].strip())

    display_name = heading
    match = re.match(r"^(?:Genre Preset|Platform Preset|Engine Pack)\s*[—:-]\s*(.+)$", heading)
    if match:
        display_name = match.group(1).strip()

    return {
        "heading": heading,
        "display_name": display_name or path.stem,
        "summary": " ".join(summary_lines).strip(),
        "sections": sections,
    }


def format_bullet_block(items: Iterable[str], fallback: str) -> str:
    values = [item.strip() for item in items if item and item.strip()]
    if not values:
        values = [fallback]
    return "\n".join(f"- {item}" for item in values)


def build_genre_replacements(genre: str | None) -> dict[str, str]:
    if not genre:
        return {}

    path = preset_path("genre", genre)
    if not path.exists():
        genre_name = humanize_slug(genre)
        return {
            "GENRE": genre,
            "GENRE_NAME": genre_name,
            "GENRE_SUMMARY": "No preset file exists yet for this genre.",
            "GENRE_DEFAULT_ASSUMPTIONS": "- Document the intended loop and audience.",
            "GENRE_RISKS": "- Capture the top genre-specific risks.",
            "GENRE_SKILLS": "- $studio-start",
            "GENRE_FIRST_SLICE": "- Define one playable slice that proves the core loop.",
            "GENRE_FIRST_FEATURE": f"First {genre_name} Slice",
            "GENRE_ROUTE_EXAMPLE": f"Plan the first {genre_name.lower()} slice",
            "GENRE_REFERENCE_GAMES": "- Add one or two contrast-set references.",
            "GENRE_DESIGN_FOCUS": "- Document the dominant loop and first failure risk.",
        }

    metadata = parse_preset_metadata(path)
    sections = metadata.get("sections", {})
    guidance = GENRE_STARTER_GUIDANCE.get(genre, {})
    reference_guidance = GENRE_REFERENCE_GUIDANCE.get(genre, {})
    genre_name = str(metadata.get("display_name") or humanize_slug(genre))

    return {
        "GENRE": genre,
        "GENRE_NAME": genre_name,
        "GENRE_SUMMARY": str(metadata.get("summary") or "No summary provided."),
        "GENRE_DEFAULT_ASSUMPTIONS": format_bullet_block(sections.get("Default assumptions", []), "Confirm the genre's default assumptions."),
        "GENRE_RISKS": format_bullet_block(sections.get("Must-watch risks", []), "Document the top genre risks."),
        "GENRE_SKILLS": format_bullet_block(sections.get("Recommended first skills", []), "$studio-start"),
        "GENRE_FIRST_SLICE": guidance.get("GENRE_FIRST_SLICE", "- Define one playable slice that proves the core loop."),
        "GENRE_FIRST_FEATURE": guidance.get("GENRE_FIRST_FEATURE", f"First {genre_name} Slice"),
        "GENRE_ROUTE_EXAMPLE": guidance.get("GENRE_ROUTE_EXAMPLE", f"Plan the first {genre_name.lower()} slice"),
        "GENRE_REFERENCE_GAMES": reference_guidance.get("GENRE_REFERENCE_GAMES", "- Add one or two contrast-set references."),
        "GENRE_DESIGN_FOCUS": reference_guidance.get("GENRE_DESIGN_FOCUS", "- Document the dominant loop and first failure risk."),
    }


def build_bootstrap_replacements(project_name: str, engine: str, engine_version: str, platform: str, genre: str) -> dict[str, str]:
    replacements = {
        "PROJECT_NAME": project_name,
        "ENGINE": engine,
        "ENGINE_VERSION": engine_version,
        "PLATFORM": platform,
    }
    replacements.update(build_genre_replacements(genre))
    return replacements


def sync_active_doc_titles(project_name: str) -> list[Path]:
    updated: list[Path] = []
    for path in sorted(ACTIVE_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        original = text

        if "Untitled Project" in text:
            text = text.replace("Untitled Project", project_name)

        if path.name in PROJECT_SCOPED_ACTIVE_DOCS:
            lines = text.splitlines()
            if lines and lines[0].startswith("# "):
                match = re.match(r"^(# [^—]+?)(?:\s+—\s+.+)?$", lines[0].strip())
                if match:
                    lines[0] = f"{match.group(1)} — {project_name}"
                    text = "\n".join(lines)

        if text != original:
            write_text(path, text)
            updated.append(path)
    return updated


def has_substantive_files(directory: Path, ignored_names: set[str] | None = None) -> bool:
    ignored_names = ignored_names or PLACEHOLDER_FILENAMES
    if not directory.exists():
        return False
    for path in directory.rglob("*"):
        if path.is_file() and path.name not in ignored_names:
            return True
    return False


def unresolved_placeholders(text: str) -> list[str]:
    return sorted(set(re.findall(r"\{[A-Z0-9_]+\}", text)))


def load_root_studio_config(root: Path | None = None) -> dict[str, object]:
    root = root or REPO_ROOT
    path = root / "studio.toml"
    if not path.exists():
        return {}
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except tomllib.TOMLDecodeError:
        return {}


def configured_engine_slug(root: Path | None = None) -> str | None:
    config = load_root_studio_config(root)
    project = config.get("project", {})
    if isinstance(project, dict):
        engine = str(project.get("primary_engine", "")).strip()
        if engine:
            return engine
    return None


def engine_family_from_slug(engine_slug: str | None) -> str:
    if not engine_slug:
        return "unknown"
    return ENGINE_SLUG_TO_FAMILY.get(engine_slug, "unknown")


def default_engine_version(engine_slug: str | None) -> str:
    if not engine_slug:
        return "TBD"
    return ENGINE_VERSION_DEFAULTS.get(engine_slug, "TBD")


def detect_engine_from_clues(root: Path | None = None) -> str:
    root = root or REPO_ROOT
    if (root / "project.godot").exists():
        return "godot"
    if (root / "Assets").exists() and (root / "ProjectSettings").exists():
        return "unity"
    if any(root.glob("*.uproject")) or ((root / "Config").exists() and (root / "Content").exists()):
        return "unreal"
    return "unknown"


def engine_detection_report(root: Path | None = None) -> dict[str, object]:
    root = root or REPO_ROOT
    configured_slug = configured_engine_slug(root)
    configured_family = engine_family_from_slug(configured_slug)
    clue_engine = detect_engine_from_clues(root)

    if configured_family != "unknown":
        resolved_engine = configured_family
        source = "studio.toml"
    else:
        resolved_engine = clue_engine
        source = "repo-clues"

    mismatch = configured_family != "unknown" and clue_engine != "unknown" and configured_family != clue_engine
    return {
        "configured_slug": configured_slug,
        "configured_family": configured_family,
        "clue_engine": clue_engine,
        "resolved_engine": resolved_engine,
        "source": source,
        "mismatch": mismatch,
    }


def detect_engine(root: Path | None = None) -> str:
    report = engine_detection_report(root)
    return str(report["resolved_engine"])


def find_godot_binary() -> str | None:
    env_candidate = os.environ.get("GODOT_BIN")
    candidates = [env_candidate] if env_candidate else []
    candidates += ["godot4", "godot", "godot4.4", "godot4.3", "godot4.2"]

    for candidate in candidates:
        if not candidate:
            continue
        path_candidate = Path(candidate).expanduser()
        if path_candidate.exists():
            return str(path_candidate.resolve())
        resolved = shutil.which(candidate)
        if resolved:
            return resolved

    mac_app = Path("/Applications/Godot.app/Contents/MacOS/Godot")
    if mac_app.exists():
        return str(mac_app)
    return None


def detect_active_genre(root: Path | None = None) -> str | None:
    root = root or REPO_ROOT
    path = root / "studio" / "docs" / "active" / "genre-starter.md"
    if not path.exists():
        return None
    text = path.read_text(encoding="utf-8")
    match = re.search(r"Preset slug:\s*`([^`]+)`", text)
    return match.group(1) if match else None


def read_preset(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()


def available_presets(group: str) -> list[str]:
    folder = PRESET_DIR / group
    if not folder.exists():
        return []
    return sorted(p.stem for p in folder.glob("*.md"))


def append_preset_pack(engine: str | None = None, platform: str | None = None, genre: str | None = None, replace: bool = False) -> Path:
    sections = []
    for group, value in [("engine", engine), ("platform", platform), ("genre", genre)]:
        if value:
            path = PRESET_DIR / group / f"{value}.md"
            if not path.exists():
                raise FileNotFoundError(f"Preset not found: {path}")
            sections.append((group.title(), value, read_preset(path)))
    if not sections:
        raise ValueError("No presets selected")
    lines = ["# Preset Pack", ""]
    for group, value, body in sections:
        lines.extend([f"## {group}: {value}", "", body, ""])
    target = ACTIVE_DIR / "preset-pack.md"
    if target.exists() and not replace:
        existing = target.read_text(encoding="utf-8").rstrip()
        merged = existing + "\n\n---\n\n" + "\n".join(lines)
        write_text(target, merged)
    else:
        write_text(target, "\n".join(lines))
    return target


def repo_summary() -> dict[str, object]:
    engine_report = engine_detection_report()
    return {
        "engine": engine_report["resolved_engine"],
        "engine_source": engine_report["source"],
        "configured_engine": engine_report["configured_slug"] or "",
        "engine_clue": engine_report["clue_engine"],
        "has_src": (REPO_ROOT / "src").exists(),
        "has_tests": (REPO_ROOT / "tests").exists(),
        "has_assets": (REPO_ROOT / "assets").exists(),
        "active_docs": len(list_markdown_files(ACTIVE_DIR)),
        "templates": len(list_markdown_files(TEMPLATE_DIR)),
        "skills": len(list((REPO_ROOT / ".agents" / "skills").glob("*/SKILL.md"))),
        "agents": len(list((REPO_ROOT / ".codex" / "agents").glob("*.toml"))),
    }


def parse_args_common(parser: argparse.ArgumentParser) -> argparse.ArgumentParser:
    parser.add_argument("--json", action="store_true", help="Emit JSON when supported.")
    return parser
