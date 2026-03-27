from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from studio_core import available_starter_kits, load_studio_config, research_notes, resolve_checklists
from _studio_common import build_genre_replacements


def run_json(*command: str) -> dict[str, object] | list[object]:
    result = subprocess.run(
        [sys.executable, *command],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    return json.loads(result.stdout)


def test_studio_config_defaults() -> None:
    config = load_studio_config()
    assert config["project"]["primary_engine"] == "godot-4"
    assert set(config["project"]["supported_engines"]) == {"godot-4", "unity-6", "unreal-5"}
    assert config["ux"]["mode"] == "wizard-first"


def test_starter_kit_contracts_exist() -> None:
    assert available_starter_kits() == ["godot-4", "unity-6", "unreal-5"]
    payload = run_json("scripts/validate_engine_kits.py", "--json")
    assert payload == {"godot-4": [], "unity-6": [], "unreal-5": []}


def test_unity_and_unreal_starter_kits_include_sample_architecture_files() -> None:
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Scripts/Runtime/CombatRoomDirector.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Tests/EditMode/CombatRoomDirectorTests.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Source/StarterKit/StarterKitGameModeBase.h").exists()
    assert (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Source/StarterKit/StarterKitEnemyArchetype.h").exists()


def test_checklist_resolution_merges_layers() -> None:
    items = resolve_checklists(engine_slug="godot-4", disciplines=["gameplay"], milestone="prototype", agent_name="gameplay_programmer")
    item_ids = {item["id"] for item in items}
    assert {"repo-health-doctor", "gameplay-readability", "prototype-proves-core-loop"}.issubset(item_ids)


def test_codex_studio_dry_run_interfaces() -> None:
    init_payload = run_json(
        "scripts/codex_studio.py",
        "init",
        "--project-name",
        "Demo",
        "--engine",
        "godot-4",
        "--platform",
        "pc-premium",
        "--genre",
        "action-roguelite",
        "--dry-run",
        "--json",
    )
    command = init_payload["command"]
    assert "scripts/setup_repo.py" in " ".join(command)

    research_payload = run_json(
        "scripts/codex_studio.py",
        "research",
        "--category",
        "systems",
        "--title",
        "Combat Readability Baseline",
        "--dry-run",
        "--json",
    )
    assert str(research_payload["path"]).endswith("docs/research/game-development/systems/combat-readability-baseline.md")


def test_genre_guidance_includes_reference_games_and_design_focus() -> None:
    payload = build_genre_replacements("action-roguelite")
    assert "Dead Cells" in payload["GENRE_REFERENCE_GAMES"]
    assert "Dominant loop" in payload["GENRE_DESIGN_FOCUS"]


def test_route_task_contract_surface() -> None:
    payload = run_json("scripts/route_task.py", "Implement the first combat room", "--json")
    for key in ("route", "skills", "agents", "docs", "checklists", "engine_kit", "research_refs", "validation_steps"):
        assert key in payload
    assert payload["engine_kit"]["id"] == "godot-4"
    assert any(item["id"] == "gameplay-readability" for item in payload["checklists"])
    assert "docs/research/game-development/systems/combat-damage-and-effects-architecture.md" in payload["research_refs"]


def test_route_task_engine_inference() -> None:
    payload = run_json("scripts/route_task.py", "Plan the next Unity starter kit task", "--json")
    assert payload["route"] == "engine / tooling / packaging"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/research/game-development/engines/unity-6-class-editor-object-map.md" in payload["research_refs"]


def test_route_task_keeps_gameplay_route_when_engine_is_mentioned() -> None:
    payload = run_json("scripts/route_task.py", "Implement Unity combat room", "--json")
    assert payload["route"] == "combat / gameplay"
    assert payload["engine_kit"]["id"] == "unity-6"


def test_route_task_surfaces_engine_system_note_for_navigation_and_damage() -> None:
    payload = run_json("scripts/route_task.py", "Design a Unity navmesh and damage system", "--json")
    assert payload["route"] == "combat / gameplay"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/research/game-development/engines/unity-6-2d-3d-navigation-damage-performance.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert "unity-navigation-choice" in item_ids
    assert "unity-damage-query-contract" in item_ids


def test_route_task_uses_performance_route_for_pooling_and_alloc_work() -> None:
    payload = run_json("scripts/route_task.py", "Optimize Unity projectile pooling and allocations", "--json")
    assert payload["route"] == "performance"
    assert payload["engine_kit"]["id"] == "unity-6"
    item_ids = {item["id"] for item in payload["checklists"]}
    assert "perf-representation-choice" in item_ids
    assert "docs/research/game-development/engines/unity-6-2d-3d-navigation-damage-performance.md" in payload["research_refs"]


def test_checklist_task_infers_build_release_for_packaging_work() -> None:
    payload = run_json("scripts/codex_studio.py", "checklist", "--task", "Plan the next UE5 packaging task", "--json")
    assert "build-release" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert "build-command-deterministic" in item_ids
    assert "docs/research/game-development/engines/unreal-5-architecture.md" in payload["research_refs"]
    assert "docs/research/game-development/production/release-validation.md" in payload["research_refs"]


def test_engine_adapters_dry_run_surface() -> None:
    unity_payload = run_json(
        "scripts/unity_adapter.py",
        "test",
        "--project-path",
        "studio/starter-kits/unity-6/scaffold",
        "--unity-path",
        "/Applications/Unity/Hub/Editor/6000.0.0f1/Unity",
        "--dry-run",
        "--json",
    )
    assert "-runTests" in " ".join(unity_payload["command"])
    assert unity_payload["validation_failures"] == []

    unreal_payload = run_json(
        "scripts/unreal_adapter.py",
        "package",
        "--project-path",
        "studio/starter-kits/unreal-5/scaffold",
        "--uat-path",
        "/Applications/Epic/UE_5.5/Engine/Build/BatchFiles/RunUAT.sh",
        "--dry-run",
        "--json",
    )
    assert "BuildCookRun" in " ".join(unreal_payload["command"])
    assert unreal_payload["validation_failures"] == []


def test_save_tasks_surface_save_architecture_research() -> None:
    payload = run_json("scripts/codex_studio.py", "checklist", "--task", "Design save and progression boundaries", "--json")
    assert "save" in payload["disciplines"]
    assert "docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md" in payload["research_refs"]


def test_research_notes_seeded() -> None:
    notes = research_notes()
    assert notes
    assert any(path.name == "genre-design-pattern-catalog.md" for path in notes)
    assert any(path.name == "genre-example-matrix.md" for path in notes)
    assert any(path.name == "godot-4-architecture.md" for path in notes)
    assert any(path.name == "godot-4-class-editor-object-map.md" for path in notes)
    assert any(path.name == "godot-4-2d-3d-navigation-damage-performance.md" for path in notes)
    assert any(path.name == "gameplay-loop-state-and-update-architecture.md" for path in notes)
    assert any(path.name == "combat-damage-and-effects-architecture.md" for path in notes)
    assert any(path.name == "ai-navigation-and-entity-scale-architecture.md" for path in notes)
    assert any(path.name == "save-progression-and-runtime-data-architecture.md" for path in notes)
    assert any(path.name == "unity-6-class-editor-object-map.md" for path in notes)
    assert any(path.name == "unity-6-2d-3d-navigation-damage-performance.md" for path in notes)
    assert any(path.name == "unreal-5-class-editor-object-map.md" for path in notes)
    assert any(path.name == "unreal-5-2d-3d-navigation-damage-performance.md" for path in notes)
