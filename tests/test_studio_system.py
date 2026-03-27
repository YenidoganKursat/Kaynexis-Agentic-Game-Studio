from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from studio_core import available_starter_kits, load_studio_config, research_notes, resolve_checklists
from _studio_common import build_genre_replacements, default_engine_version, detect_engine
from validate_docs import RESEARCH_GUIDE_FILES, USER_GUIDE_FILES, collect_doc_findings

UNITY_STUB = REPO_ROOT / "tools" / "engine-stubs" / "unity" / "Unity"
UNREAL_STUB = REPO_ROOT / "tools" / "engine-stubs" / "unreal" / "RunUAT.sh"


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


def run_process(*command: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *command],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )


def test_studio_config_defaults() -> None:
    config = load_studio_config()
    assert config["project"]["primary_engine"] == "godot-4"
    assert set(config["project"]["supported_engines"]) == {"godot-4", "unity-6", "unreal-5"}
    assert config["ux"]["mode"] == "wizard-first"
    assert config["project"]["name"] == "Codex Game Studio Pro Max"


def test_engine_version_defaults_are_engine_aware() -> None:
    assert default_engine_version("godot-4") == "4.x"
    assert default_engine_version("unity-6") == "6000.x"
    assert default_engine_version("unreal-5") == "5.x"


def test_starter_kit_contracts_exist() -> None:
    assert available_starter_kits() == ["godot-4", "unity-6", "unreal-5"]
    payload = run_json("scripts/validate_engine_kits.py", "--json")
    assert payload == {"godot-4": [], "unity-6": [], "unreal-5": []}


def test_unity_and_unreal_starter_kits_include_sample_architecture_files() -> None:
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Scripts/Runtime/CombatRoomDirector.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Scripts/Runtime/Health.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Scripts/Runtime/PlayerAvatar.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Scripts/Runtime/PulseEnemy.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Scripts/Editor/BuildPipelineEntry.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Tests/EditMode/CombatRoomDirectorTests.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Tests/EditMode/HealthTests.cs").exists()
    assert (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Source/StarterKit/StarterKitGameModeBase.h").exists()
    assert (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Source/StarterKit/StarterKitEnemyArchetype.h").exists()
    assert (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Source/StarterKit/StarterKitCharacter.h").exists()
    assert (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Source/StarterKit/StarterKitEnemyActor.h").exists()
    assert (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Source/StarterKit/StarterKitHealthComponent.h").exists()


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
    assert command[command.index("--engine-version") + 1] == "4.x"

    unreal_init_payload = run_json(
        "scripts/codex_studio.py",
        "init",
        "--project-name",
        "Demo",
        "--engine",
        "unreal-5",
        "--platform",
        "console-premium",
        "--genre",
        "co-op-survival",
        "--dry-run",
        "--json",
    )
    unreal_command = unreal_init_payload["command"]
    assert unreal_command[unreal_command.index("--engine-version") + 1] == "5.x"

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


def test_active_docs_have_no_semantic_template_defaults() -> None:
    errors, warnings = collect_doc_findings()
    assert errors == []
    assert warnings == []


def test_user_facing_guides_are_part_of_doc_validation_surface() -> None:
    expected = {
        "docs/README.md",
        "docs/setup/first-hour-walkthrough.md",
        "docs/reference/engine-selection-guide.md",
        "docs/reference/workflow-recipes.md",
        "docs/reference/task-prompt-examples.md",
    }
    assert expected.issubset(USER_GUIDE_FILES.keys())


def test_engine_research_guides_are_part_of_doc_validation_surface() -> None:
    expected = {
        "docs/research/game-development/engines/README.md",
        "docs/research/game-development/engines/godot-4-2d-3d-class-and-mechanic-guide.md",
        "docs/research/game-development/engines/unity-6-2d-3d-class-and-mechanic-guide.md",
        "docs/research/game-development/engines/unreal-5-2d-3d-class-and-mechanic-guide.md",
    }
    assert expected.issubset(RESEARCH_GUIDE_FILES.keys())


def test_route_task_contract_surface() -> None:
    payload = run_json("scripts/route_task.py", "Implement the first combat room", "--json")
    for key in ("route", "skills", "agents", "docs", "checklists", "engine_kit", "research_refs", "validation_steps"):
        assert key in payload
    assert payload["engine_kit"]["id"] == "godot-4"
    assert any(item["id"] == "gameplay-readability" for item in payload["checklists"])
    assert "docs/research/game-development/systems/combat-damage-and-effects-architecture.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/godot-4-2d-3d-class-and-mechanic-guide.md" in payload["research_refs"]


def test_route_task_engine_inference() -> None:
    payload = run_json("scripts/route_task.py", "Plan the next Unity starter kit task", "--json")
    assert payload["route"] == "engine / tooling / packaging"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/research/game-development/engines/unity-6-class-editor-object-map.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unity-6-2d-3d-class-and-mechanic-guide.md" in payload["research_refs"]


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


def test_route_task_avoids_false_positive_substring_matches() -> None:
    party_payload = run_json("scripts/route_task.py", "Party invite flow", "--json")
    assert party_payload["route"] == "fallback"

    starter_payload = run_json("scripts/route_task.py", "Research starter task flow", "--json")
    assert starter_payload["route"] == "fallback"


def test_checklist_task_infers_build_release_for_packaging_work() -> None:
    payload = run_json("scripts/codex_studio.py", "checklist", "--task", "Plan the next UE5 packaging task", "--json")
    assert "build-release" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert "build-command-deterministic" in item_ids
    assert "docs/research/game-development/engines/unreal-5-architecture.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unreal-5-2d-3d-class-and-mechanic-guide.md" in payload["research_refs"]
    assert "docs/research/game-development/production/release-validation.md" in payload["research_refs"]


def test_engine_adapters_dry_run_surface() -> None:
    unity_payload = run_json(
        "scripts/unity_adapter.py",
        "test",
        "--project-path",
        "studio/starter-kits/unity-6/scaffold",
        "--unity-path",
        str(UNITY_STUB),
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
        str(UNREAL_STUB),
        "--dry-run",
        "--json",
    )
    assert "BuildCookRun" in " ".join(unreal_payload["command"])
    assert unreal_payload["validation_failures"] == []


def test_unity_and_unreal_starter_kits_expose_richer_sample_slice_markers() -> None:
    unity_director = (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Scripts/Runtime/CombatRoomDirector.cs").read_text(encoding="utf-8")
    assert "DescribeNextExpansion" in unity_director
    assert "PlayerAvatar" in unity_director
    assert "PulseEnemy" in unity_director

    unity_build_entry = (REPO_ROOT / "studio/starter-kits/unity-6/scaffold/Assets/Scripts/Editor/BuildPipelineEntry.cs").read_text(encoding="utf-8")
    assert "Build()" in unity_build_entry

    unreal_game_mode = (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Source/StarterKit/StarterKitGameModeBase.h").read_text(encoding="utf-8")
    assert "DefaultPlayerClass" in unreal_game_mode
    assert "DefaultEnemyClass" in unreal_game_mode

    unreal_input = (REPO_ROOT / "studio/starter-kits/unreal-5/scaffold/Config/DefaultInput.ini").read_text(encoding="utf-8")
    assert "ActionName=\"Dash\"" in unreal_input


def test_engine_adapters_fail_when_tool_path_is_missing() -> None:
    result = run_process(
        "scripts/unity_adapter.py",
        "test",
        "--project-path",
        "studio/starter-kits/unity-6/scaffold",
        "--unity-path",
        "tools/engine-stubs/unity/missing-Unity",
        "--dry-run",
        "--json",
    )
    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["validation_failures"]


def test_save_tasks_surface_save_architecture_research() -> None:
    payload = run_json("scripts/codex_studio.py", "checklist", "--task", "Design save and progression boundaries", "--json")
    assert "save" in payload["disciplines"]
    assert "docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md" in payload["research_refs"]


def test_detect_engine_prefers_configured_engine_over_root_file_clues(tmp_path: Path) -> None:
    (tmp_path / "studio.toml").write_text('[project]\nprimary_engine = "unreal-5"\n', encoding="utf-8")
    (tmp_path / "project.godot").write_text("; clue only\n", encoding="utf-8")
    assert detect_engine(tmp_path) == "unreal"


def test_research_notes_seeded() -> None:
    notes = research_notes()
    assert notes
    assert (REPO_ROOT / "docs/research/game-development/engines/README.md").exists()
    assert any(path.name == "genre-design-pattern-catalog.md" for path in notes)
    assert any(path.name == "genre-example-matrix.md" for path in notes)
    assert any(path.name == "godot-4-architecture.md" for path in notes)
    assert any(path.name == "godot-4-class-editor-object-map.md" for path in notes)
    assert any(path.name == "godot-4-2d-3d-class-and-mechanic-guide.md" for path in notes)
    assert any(path.name == "godot-4-2d-3d-navigation-damage-performance.md" for path in notes)
    assert any(path.name == "gameplay-loop-state-and-update-architecture.md" for path in notes)
    assert any(path.name == "combat-damage-and-effects-architecture.md" for path in notes)
    assert any(path.name == "ai-navigation-and-entity-scale-architecture.md" for path in notes)
    assert any(path.name == "save-progression-and-runtime-data-architecture.md" for path in notes)
    assert any(path.name == "unity-6-class-editor-object-map.md" for path in notes)
    assert any(path.name == "unity-6-2d-3d-class-and-mechanic-guide.md" for path in notes)
    assert any(path.name == "unity-6-2d-3d-navigation-damage-performance.md" for path in notes)
    assert any(path.name == "unreal-5-class-editor-object-map.md" for path in notes)
    assert any(path.name == "unreal-5-2d-3d-class-and-mechanic-guide.md" for path in notes)
    assert any(path.name == "unreal-5-2d-3d-navigation-damage-performance.md" for path in notes)
