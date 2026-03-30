from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from studio_core import agent_public_title, available_starter_kits, load_studio_config, research_notes, resolve_checklists
from _studio_common import build_genre_replacements, default_engine_version, detect_engine
from validate_repo_layout import REQUIRED_PATHS as REQUIRED_LAYOUT_PATHS
from validate_docs import RESEARCH_GUIDE_FILES, USER_GUIDE_FILES, collect_doc_findings
from codex_studio import interactive_menu

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
    assert config["project"]["name"] == "Kaynexis Agentic Game Studio"


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


def test_naming_checklist_is_part_of_base_bundle() -> None:
    items = resolve_checklists(engine_slug="godot-4", disciplines=["gameplay"], milestone="prototype", agent_name="gameplay_programmer")
    item_ids = {item["id"] for item in items}
    assert {"short-canonical-names", "rename-sync"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/base/naming.toml") for item in items)


def test_ci_cd_checklist_surfaces_short_names() -> None:
    items = resolve_checklists(engine_slug="godot-4", disciplines=["build-release"], milestone="release", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert "ci-short-names" in item_ids
    assert any(item["source"].endswith("studio/checklists/discipline/build-release.toml") for item in items)


def test_versioning_checklist_includes_commit_notes() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["versioning"], milestone="release", agent_name="release_manager")
    item_ids = {item["id"] for item in items}
    assert {"version-source", "version-changelog", "version-commit"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/versioning.toml") for item in items)


def test_quality_checklist_includes_quality_and_perf_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["quality"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {"quality-owner", "quality-process", "quality-evidence", "quality-opt-baseline", "perf-first-lever"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/quality.toml") for item in items)


def test_route_task_surfaces_theory_stack_guidance() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Build a theory stack for a tactical RPG tutorial and name the MDA, flow, and motivation lenses",
        "--json",
    )
    assert payload["route"] == "theory / design lenses"
    assert {"feature-brief", "mechanic-design", "qa-matrix"}.issubset(set(payload.get("skills", [])))
    docs = set(payload.get("docs", []))
    assert {
        "docs/reference/theory-guide.md",
        "docs/examples/theory-example.md",
        "docs/research/game-development/foundations/theory.md",
        "docs/research/game-development/foundations/frameworks.md",
        "docs/research/game-development/foundations/ux.md",
        "docs/research/game-development/foundations/balance.md",
    }.issubset(docs)


def test_theory_checklist_includes_theory_and_support_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["theory"], milestone="prototype", agent_name="game_designer")
    item_ids = {item["id"] for item in items}
    assert {"theory-outcome", "theory-lens-stack", "theory-evidence", "theory-boundary", "theory-validation", "theory-doc-sync"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/theory.toml") for item in items)


def test_custom_architecture_route_surfaces_custom_lane_docs() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Design a custom architecture and rule pack for project-specific inventory overrides",
        "--json",
    )
    assert payload["route"] == "custom / architecture / rules"
    assert {"feature-brief", "architecture-decision", "qa-matrix"}.issubset(set(payload.get("skills", [])))
    docs = set(payload.get("docs", []))
    assert {
        "docs/reference/custom-architecture.md",
        "docs/examples/custom-architecture-example.md",
        "docs/research/game-development/foundations/custom-architecture.md",
        "docs/reference/architecture-guide.md",
    }.issubset(docs)


def test_custom_architecture_checklist_includes_custom_layer() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["custom"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {"custom-intake", "custom-owner", "custom-rulepack", "custom-validation", "custom-doc-sync"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/custom.toml") for item in items)


def test_custom_packs_route_surfaces_custom_registry_docs() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Design a custom pack registry for project-specific inventory and UI overrides",
        "--json",
    )
    assert payload["route"] == "custom packs / feature registry"
    assert {"feature-brief", "architecture-decision", "tools-pipeline", "qa-matrix"}.issubset(set(payload.get("skills", [])))
    docs = set(payload.get("docs", []))
    assert {
        "docs/reference/custom-packs.md",
        "docs/examples/custom-packs-example.md",
        "docs/research/game-development/foundations/custom-packs.md",
        "docs/reference/custom-architecture.md",
        "docs/reference/extensions-guide.md",
    }.issubset(docs)
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"custom-pack-intake", "custom-pack-model", "custom-pack-fallback", "custom-pack-registry", "custom-pack-validation", "custom-pack-doc-sync"}.issubset(item_ids)


def test_custom_packs_checklist_includes_custom_pack_layer() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["custom_packs"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {"custom-pack-intake", "custom-pack-model", "custom-pack-fallback", "custom-pack-registry", "custom-pack-validation", "custom-pack-doc-sync"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/custom_packs.toml") for item in items)


def test_extensions_route_surfaces_extension_pack_docs() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Design a custom extension pack for inventory hooks and UI panels",
        "--json",
    )
    assert payload["route"] == "extensions / plugin packs"
    assert {"feature-brief", "architecture-decision", "tools-pipeline", "qa-matrix"}.issubset(set(payload.get("skills", [])))
    docs = set(payload.get("docs", []))
    assert {
        "docs/reference/extensions-guide.md",
        "docs/examples/extensions-example.md",
        "docs/research/game-development/foundations/extensions.md",
        "docs/reference/custom-architecture.md",
        "docs/reference/library-guide.md",
    }.issubset(docs)


def test_extensions_checklist_includes_extension_layer() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["extensions"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {"extension-intake", "extension-manifest", "extension-boundary", "extension-validation", "extension-doc-sync"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/extensions.toml") for item in items)


def test_canonical_markdown_names_do_not_reintroduce_legacy_verbose_files() -> None:
    banned = {
        "adr-first-combat-room.md",
        "feature-first-combat-room.md",
        "qa-matrix-first-combat-room.md",
        "test-plan-first-combat-room.md",
        "eval-plan-bugfix-scaffold-atlas-aware.md",
        "eval-plan-system-atlas-routing.md",
        "eval-plan-world-graph-routing.md",
        "engine-agent-guidelines.md",
        "ci-cd-architecture.md",
        "engine-class-atlas.md",
        "engine-quick-map.md",
        "game-systems-atlas.md",
        "genre-advanced-development-framework.md",
        "lorebook-world-state-and-canon-architecture.md",
        "world-graph-relationship-history-architecture.md",
        "feature-brief-golden-example.md",
        "bug-report-golden-example.md",
        "eval-plan-golden-example.md",
        "genre-starter-golden-example.md",
        "handoff-contract-golden-example.md",
        "lorebook-brief-golden-example.md",
        "perf-pass-golden-example.md",
        "postmortem-golden-example.md",
        "qa-matrix-golden-example.md",
        "test-plan-golden-example.md",
        "feature-traceability-golden-example.md",
        "world-graph-brief-golden-example.md",
    }
    roots = [REPO_ROOT / "docs", REPO_ROOT / "studio" / "docs", REPO_ROOT / "studio" / "checklists"]
    current = {path.name for root in roots for path in root.rglob("*.md")}
    assert current.isdisjoint(banned)


def test_example_files_keep_canonical_suffix() -> None:
    example_names = {
        path.name
        for path in (REPO_ROOT / "docs" / "examples").glob("*.md")
        if path.name != "README.md"
    }
    assert example_names
    assert all(name.endswith("-example.md") for name in example_names)
    assert all("golden" not in name for name in example_names)


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
    assert payload["GENRE_MATURITY"].endswith("genre-maturity.md")

    deckbuilder_payload = build_genre_replacements("deckbuilder-roguelike")
    assert "Slay the Spire" in deckbuilder_payload["GENRE_REFERENCE_GAMES"]
    assert deckbuilder_payload["GENRE_FIRST_FEATURE"] == "First Deck Run"

    auto_battler_payload = build_genre_replacements("auto-battler")
    assert "Teamfight Tactics" in auto_battler_payload["GENRE_REFERENCE_GAMES"]
    assert "board" in auto_battler_payload["GENRE_DESIGN_FOCUS"]

    grand_strategy_payload = build_genre_replacements("grand-strategy")
    assert "Crusader Kings III" in grand_strategy_payload["GENRE_REFERENCE_GAMES"]
    assert "diplomacy" in grand_strategy_payload["GENRE_DESIGN_FOCUS"]

    metroidvania_payload = build_genre_replacements("metroidvania")
    assert "Metroid Dread" in metroidvania_payload["GENRE_REFERENCE_GAMES"]
    assert "world graph" in metroidvania_payload["GENRE_DESIGN_FOCUS"]

    city_builder_payload = build_genre_replacements("city-builder")
    assert "Cities: Skylines II" in city_builder_payload["GENRE_REFERENCE_GAMES"]
    assert "transport/pathing" in city_builder_payload["GENRE_DESIGN_FOCUS"]

    life_sim_payload = build_genre_replacements("life-sim")
    assert "The Sims 4" in life_sim_payload["GENRE_REFERENCE_GAMES"]
    assert "relationship graphs" in life_sim_payload["GENRE_DESIGN_FOCUS"]

    hero_shooter_payload = build_genre_replacements("hero-shooter")
    assert "Overwatch 2" in hero_shooter_payload["GENRE_REFERENCE_GAMES"]
    assert "objective" in hero_shooter_payload["GENRE_DESIGN_FOCUS"]

    stealth_payload = build_genre_replacements("stealth")
    assert "HITMAN World of Assassination" in stealth_payload["GENRE_REFERENCE_GAMES"]
    assert "detection" in stealth_payload["GENRE_DESIGN_FOCUS"]

    soulslike_payload = build_genre_replacements("soulslike")
    assert "ELDEN RING" in soulslike_payload["GENRE_REFERENCE_GAMES"]
    assert "telegraph" in soulslike_payload["GENRE_DESIGN_FOCUS"]


def test_active_docs_have_no_semantic_template_defaults() -> None:
    errors, warnings = collect_doc_findings()
    assert errors == []
    assert warnings == []


def test_commit_msg_hook_mentions_versioning_commit_notes() -> None:
    hook = (REPO_ROOT / ".githooks" / "commit-msg").read_text(encoding="utf-8")
    assert "Versioning and release commits should include a short body that says what changed." in hook
    assert "feat(versioning): record release-note summary for 2.1.0-dev" in hook


def test_user_facing_guides_are_part_of_doc_validation_surface() -> None:
    expected = {
        "docs/README.md",
        "docs/setup/quick-access.md",
        "docs/reference/agent-guide.md",
        "docs/reference/repo-tour.md",
        "docs/reference/engine-map.md",
        "docs/reference/engine-atlas.md",
        "docs/reference/asset-guide.md",
        "docs/reference/gpu-guide.md",
        "docs/reference/system-atlas.md",
        "docs/reference/godot-atlas.md",
        "docs/reference/unity-atlas.md",
        "docs/reference/unreal-atlas.md",
        "docs/setup/first-hour-walkthrough.md",
        "docs/setup/github-setup.md",
        "docs/reference/engine-selection-guide.md",
        "docs/reference/engine-eval.md",
        "docs/reference/engine-bugs.md",
        "docs/reference/engine-examples.md",
        "docs/reference/benchmark-guide.md",
        "docs/reference/audio-animation-guide.md",
        "docs/reference/platform-guide.md",
        "docs/reference/cross-platform-guide.md",
        "docs/reference/console-guide.md",
        "docs/examples/asset-example.md",
        "docs/examples/benchmark-example.md",
        "docs/examples/engine-eval-example.md",
        "docs/examples/engine-bugs-example.md",
        "docs/examples/gpu-example.md",
        "docs/examples/platform-example.md",
        "docs/examples/cross-platform-example.md",
        "docs/examples/console-example.md",
        "docs/reference/marketing-guide.md",
        "docs/examples/marketing-example.md",
        "docs/reference/quality-process.md",
        "docs/examples/quality-process-example.md",
        "docs/reference/ci-cd.md",
        "docs/reference/command-cheatsheet.md",
        "docs/reference/eval-strategy.md",
        "docs/reference/quality-guide.md",
        "docs/reference/perf-guide.md",
        "docs/reference/workflow-recipes.md",
        "docs/reference/task-prompt-examples.md",
        "docs/reference/lorebook-methodology.md",
        "docs/reference/world-graph-methodology.md",
        "docs/reference/steam-intel.md",
        "docs/reference/handoff-contracts.md",
        "docs/reference/feature-traceability.md",
        "docs/reference/agent-system.md",
        "docs/reference/mastermind-guide.md",
        "docs/reference/agent-portfolio.md",
        "docs/reference/agent-hierarchy.md",
        "docs/reference/agent-speedpack.md",
        "docs/reference/studio-map.md",
        "docs/reference/doc-sync-audit.md",
        "docs/reference/balance-simulator.md",
        "docs/research/game-development/foundations/engine-eval.md",
        "docs/research/game-development/foundations/engine-bugs.md",
        "docs/research/game-development/production/README.md",
        "docs/research/game-development/production/marketing.md",
        "docs/research/game-development/production/steam-intel.md",
        "docs/research/game-development/production/platform-compatibility.md",
        "docs/research/game-development/production/cross-platform.md",
        "docs/examples/README.md",
        "docs/examples/capabilities-example.md",
        "docs/examples/agent-system-example.md",
        "docs/examples/agent-speedpack-example.md",
        "docs/examples/mastermind-example.md",
        "docs/examples/agent-portfolio-example.md",
        "docs/examples/agent-hierarchy-example.md",
        "docs/reference/custom-packs.md",
        "docs/examples/custom-packs-example.md",
        "studio/docs/templates/custom-packs.md",
        "studio/checklists/discipline/speedpack.toml",
        "studio/docs/active/eval-agent-speedpack.md",
        "docs/examples/steam-intel-example.md",
        "studio/checklists/discipline/engine_eval.toml",
        "studio/docs/active/engine-eval.md",
        "studio/docs/active/eval-engine-eval.md",
        "studio/docs/active/eval-console.md",
    }
    assert expected.issubset(USER_GUIDE_FILES.keys())


def test_engine_research_guides_are_part_of_doc_validation_surface() -> None:
    expected = {
        "docs/research/game-development/foundations/README.md",
        "docs/research/game-development/foundations/frameworks.md",
        "docs/research/game-development/foundations/ux.md",
        "docs/research/game-development/foundations/ai.md",
        "docs/research/game-development/foundations/balance.md",
        "docs/research/game-development/foundations/gpu.md",
        "docs/research/game-development/foundations/benchmarks.md",
        "docs/research/game-development/foundations/mastermind.md",
        "docs/research/game-development/foundations/agent-system.md",
        "docs/research/game-development/foundations/agent-speedpack.md",
        "docs/research/game-development/foundations/agent-portfolio.md",
        "docs/research/game-development/foundations/agent-hierarchy.md",
        "docs/research/game-development/foundations/engine-eval.md",
        "docs/research/game-development/foundations/engine-bugs.md",
        "docs/research/game-development/foundations/README.md",
        "docs/research/game-development/foundations/custom-packs.md",
        "docs/research/game-development/README.md",
        "docs/research/game-development/production/console.md",
        "docs/research/game-development/assets/README.md",
        "docs/research/game-development/genre/README.md",
        "docs/research/game-development/genre/genre-guide.md",
        "docs/research/game-development/genre/genre-maturity.md",
        "docs/research/game-development/foundations/quality.md",
        "docs/research/game-development/narrative/README.md",
        "docs/research/game-development/narrative/lorebook.md",
        "docs/research/game-development/narrative/world-graph.md",
        "docs/research/game-development/assets/README.md",
        "docs/research/game-development/assets/alternatives.md",
        "docs/research/game-development/assets/ownership.md",
        "docs/research/game-development/assets/import.md",
        "docs/research/game-development/genre/genre-patterns.md",
        "docs/research/game-development/genre/genre-examples.md",
        "docs/research/game-development/genre/auto-battler.md",
        "docs/research/game-development/genre/deckbuilder.md",
        "docs/research/game-development/genre/survivorlike.md",
        "docs/research/game-development/genre/grand-strategy.md",
        "docs/research/game-development/genre/stealth.md",
        "docs/research/game-development/genre/colony-sim.md",
        "docs/research/game-development/genre/city-builder.md",
        "docs/research/game-development/genre/life-sim.md",
        "docs/research/game-development/genre/hero-shooter.md",
        "docs/research/game-development/genre/soulslike.md",
        "docs/research/game-development/genre/factory.md",
        "docs/research/game-development/genre/metroidvania.md",
        "docs/research/game-development/production/platform.md",
        "docs/research/game-development/production/incident.md",
        "docs/research/game-development/production/steam-intel.md",
        "docs/research/game-development/production/platform-compatibility.md",
        "docs/research/game-development/production/cross-platform.md",
        "docs/research/game-development/engines/README.md",
        "docs/research/game-development/engines/godot-classes.md",
        "docs/research/game-development/engines/godot-gpu.md",
        "docs/research/game-development/engines/godot-presentation.md",
        "docs/research/game-development/engines/unity-classes.md",
        "docs/research/game-development/engines/unity-gpu.md",
        "docs/research/game-development/engines/unity-presentation.md",
        "docs/research/game-development/engines/unreal-classes.md",
        "docs/research/game-development/engines/unreal-gpu.md",
        "docs/research/game-development/engines/unreal-presentation.md",
        "docs/research/game-development/engines/godot-systems.md",
        "docs/research/game-development/engines/godot-visuals.md",
        "docs/research/game-development/engines/unity-systems.md",
        "docs/research/game-development/engines/unity-visuals.md",
        "docs/research/game-development/engines/unreal-systems.md",
        "docs/research/game-development/engines/unreal-visuals.md",
    }
    assert expected.issubset(RESEARCH_GUIDE_FILES.keys())


def test_repo_layout_validation_includes_platform_compatibility_surface() -> None:
    expected = {
        "docs/reference/platform-guide.md",
        "docs/reference/cross-platform-guide.md",
        "docs/reference/console-guide.md",
        "docs/examples/platform-example.md",
        "docs/examples/cross-platform-example.md",
        "docs/examples/console-example.md",
        "docs/research/game-development/production/platform-compatibility.md",
        "docs/research/game-development/production/cross-platform.md",
        "docs/research/game-development/production/console.md",
        "studio/checklists/discipline/platform_compatibility.toml",
        "studio/checklists/discipline/console.toml",
        "studio/docs/active/platform-targets.md",
        "studio/docs/active/eval-platform-compatibility.md",
        "studio/docs/active/eval-console.md",
        "studio/docs/templates/platform-targets.md",
    }
    assert expected.issubset(set(REQUIRED_LAYOUT_PATHS))


def test_console_checklist_includes_console_lane() -> None:
    items = resolve_checklists(engine_slug="unreal-5", disciplines=["console"], milestone="prototype", agent_name="porting_engineer")
    item_ids = {item["id"] for item in items}
    assert {
        "console-source-hierarchy",
        "console-family-split",
        "console-input-model",
        "console-suspend-save",
        "console-cert-risk",
        "console-release-sequence",
        "console-doc-sync",
    }.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/console.toml") for item in items)


def test_repo_layout_validation_includes_custom_packs_surface() -> None:
    expected = {
        "docs/reference/custom-packs.md",
        "docs/examples/custom-packs-example.md",
        "docs/research/game-development/foundations/custom-packs.md",
        "studio/checklists/discipline/custom_packs.toml",
        "studio/docs/active/custom-packs-adr.md",
        "studio/docs/active/eval-custom-packs.md",
        "studio/docs/templates/custom-packs.md",
    }
    assert expected.issubset(set(REQUIRED_LAYOUT_PATHS))


def test_repo_layout_validation_includes_speedpack_surface() -> None:
    expected = {
        "docs/reference/agent-speedpack.md",
        "docs/examples/agent-speedpack-example.md",
        "docs/research/game-development/foundations/agent-speedpack.md",
        "studio/checklists/discipline/speedpack.toml",
        "studio/docs/active/eval-agent-speedpack.md",
        "docs/reference/studio-map.md",
    }
    assert expected.issubset(set(REQUIRED_LAYOUT_PATHS))


def test_route_task_surfaces_cross_platform_support_tier_guidance_for_release_order_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Map cross-platform support tiers for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS",
        "--json",
    )
    assert payload["route"] == "platform / compatibility / readiness"
    assert "docs/reference/cross-platform-guide.md" in payload["docs"]
    assert "docs/examples/cross-platform-example.md" in payload["docs"]
    assert "docs/research/game-development/production/cross-platform.md" in payload["docs"]
    assert "studio/docs/active/platform-targets.md" in payload["docs"]
    assert "studio/docs/active/eval-platform-compatibility.md" in payload["docs"]
    assert payload["agent_titles"][0] == "Kaynexis"
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"platform-support-tier", "platform-release-sequence", "platform-source-hierarchy", "platform-family-split", "platform-input-model", "platform-performance-envelope", "platform-policy-watch", "platform-visual-pack", "platform-doc-sync"}.issubset(item_ids)
    assert "docs/research/game-development/production/cross-platform.md" in payload["research_refs"]


def test_repo_layout_validation_includes_engine_eval_surface() -> None:
    expected = {
        "docs/reference/engine-eval.md",
        "docs/examples/engine-eval-example.md",
        "docs/research/game-development/foundations/engine-eval.md",
        "studio/checklists/discipline/engine_eval.toml",
        "studio/docs/active/engine-eval.md",
        "studio/docs/active/eval-engine-eval.md",
    }
    assert expected.issubset(set(REQUIRED_LAYOUT_PATHS))


def test_repo_layout_validation_includes_engine_bugs_surface() -> None:
    expected = {
        "docs/reference/engine-bugs.md",
        "docs/examples/engine-bugs-example.md",
        "docs/research/game-development/foundations/engine-bugs.md",
        "studio/checklists/discipline/engine_bugs.toml",
        "studio/docs/active/eval-engine-bugs.md",
    }
    assert expected.issubset(set(REQUIRED_LAYOUT_PATHS))


def test_repo_layout_validation_includes_engine_fit_surface() -> None:
    expected = {
        "docs/reference/engine-fit.md",
        "docs/examples/engine-fit-example.md",
        "docs/research/game-development/foundations/engine-fit.md",
        "studio/checklists/discipline/engine_fit.toml",
        "studio/docs/active/engine-fit.md",
        "studio/docs/active/eval-engine-fit.md",
    }
    assert expected.issubset(set(REQUIRED_LAYOUT_PATHS))


def test_scaffold_feature_creates_handoff_and_traceability_by_default(tmp_path: Path) -> None:
    payload = run_json(
        "scripts/scaffold_feature.py",
        "Parry Mechanic",
        "--output-dir",
        str(tmp_path),
        "--json",
    )
    created = {Path(path).name for path in payload["created"]}
    assert {"feature-parry-mechanic.md", "handoff-parry-mechanic.md", "traceability-parry-mechanic.md"}.issubset(created)


def test_route_task_contract_surface() -> None:
    payload = run_json("scripts/route_task.py", "Implement the first combat room", "--json")
    for key in ("route", "skills", "agents", "agent_titles", "docs", "checklists", "engine_kit", "research_refs", "validation_steps"):
        assert key in payload
    assert payload["engine_kit"]["id"] == "godot-4"
    assert any(item["id"] == "gameplay-readability" for item in payload["checklists"])
    assert "docs/research/game-development/systems/combat.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/godot-classes.md" in payload["research_refs"]


def test_route_task_surfaces_engine_fit_guidance_for_developer_profile_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Which engine fits a beginner solo developer building a small 2D game in Godot 4?",
        "--json",
    )
    assert payload["route"] == "engine / developer fit / recommendation"
    assert payload["engine_kit"]["id"] == "godot-4"
    assert "docs/reference/engine-fit.md" in payload["docs"]
    assert "docs/examples/engine-fit-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/engine-fit.md" in payload["research_refs"]
    assert "docs/reference/engine-selection-guide.md" in payload["research_refs"]
    assert "docs/reference/engine-map.md" in payload["research_refs"]
    assert "docs/reference/engine-examples.md" in payload["research_refs"]
    assert "docs/reference/engine-eval.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"engine-profile-named", "engine-language-fit", "engine-collaboration-fit", "engine-platform-fit", "engine-tooling-fit", "engine-proof-path", "engine-tradeoff-matrix", "engine-doc-sync"}.issubset(item_ids)
    assert {"research-primary-sources", "research-repo-impact"}.issubset(item_ids)


def test_codex_studio_checklist_surfaces_engine_fit_guidance() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Which engine fits a beginner solo developer building a small 2D game in Godot 4?",
        "--json",
    )
    assert "engine_fit" in payload["disciplines"]
    assert "research" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"engine-profile-named", "engine-language-fit", "engine-collaboration-fit", "engine-platform-fit", "engine-tooling-fit", "engine-proof-path", "engine-tradeoff-matrix", "engine-doc-sync"}.issubset(item_ids)
    assert "research-primary-sources" in item_ids
    assert "research-repo-impact" in item_ids
    assert "docs/reference/engine-fit.md" in payload["research_refs"]
    assert "docs/examples/engine-fit-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/engine-fit.md" in payload["research_refs"]


def test_route_task_surfaces_engine_bug_guidance_for_troubleshooting_requests() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Classify recurring Godot signal and node-path bugs before patching anything",
        "--json",
    )
    assert payload["route"] == "engine bugs / troubleshooting / common errors"
    assert payload["engine_kit"]["id"] == "godot-4"
    assert "docs/reference/engine-bugs.md" in payload["docs"]
    assert "docs/examples/engine-bugs-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/engine-bugs.md" in payload["docs"]
    assert "studio/docs/templates/bug-report.md" in payload["docs"]
    assert "studio/docs/templates/crash-triage.md" in payload["docs"]
    assert "docs/reference/engine-bugs.md" in payload["research_refs"]
    assert "docs/examples/engine-bugs-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/engine-bugs.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"engine-bugs-family", "engine-bugs-first-check", "engine-bugs-boundary", "engine-bugs-proof-path", "engine-bugs-doc-sync"}.issubset(item_ids)
    assert {"bugfix-repro", "bugfix-regression-proof", "qa-criteria", "qa-matrix"}.issubset(item_ids)


def test_codex_studio_checklist_surfaces_engine_bug_guidance_for_troubleshooting_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Classify recurring Unity null reference and prefab override bugs before patching anything",
        "--json",
    )
    assert "engine_bugs" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"engine-bugs-family", "engine-bugs-first-check", "engine-bugs-boundary", "engine-bugs-proof-path", "engine-bugs-doc-sync"}.issubset(item_ids)
    assert {"bugfix-repro", "bugfix-regression-proof", "qa-criteria", "qa-matrix"}.issubset(item_ids)
    assert "docs/reference/engine-bugs.md" in payload["research_refs"]
    assert "docs/examples/engine-bugs-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/engine-bugs.md" in payload["research_refs"]


def test_route_task_surfaces_speedpack_guidance_for_fast_path_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Give me the speed pack for a short HUD fix and keep the proof path minimal",
        "--json",
    )
    assert payload["route"] == "speed pack / fast path"
    docs = set(payload["docs"])
    assert {
        "docs/reference/agent-speedpack.md",
        "docs/examples/agent-speedpack-example.md",
        "docs/research/game-development/foundations/agent-speedpack.md",
        "docs/setup/quick-access.md",
        "docs/reference/studio-map.md",
    }.issubset(docs)
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"speedpack-owner", "speedpack-route", "speedpack-bundle", "speedpack-proof", "speedpack-summary", "speedpack-doc-sync"}.issubset(item_ids)


def test_codex_studio_checklist_surfaces_speedpack_guidance_for_fast_path_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Give me the speed pack for a short HUD fix and keep the proof path minimal",
        "--json",
    )
    assert "speedpack" in payload["disciplines"]
    assert "agents" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"speedpack-owner", "speedpack-route", "speedpack-bundle", "speedpack-proof", "speedpack-summary", "speedpack-doc-sync"}.issubset(item_ids)
    assert "docs/reference/agent-speedpack.md" in payload["research_refs"]
    assert "docs/examples/agent-speedpack-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/agent-speedpack.md" in payload["research_refs"]


def test_route_task_surfaces_mastermind_guidance_for_broad_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs",
        "--json",
    )
    assert payload["route"] == "agent orchestration / master mind"
    assert "docs/reference/mastermind-guide.md" in payload["docs"]
    assert "docs/reference/agent-system.md" in payload["docs"]
    assert "docs/examples/mastermind-example.md" in payload["docs"]
    assert "docs/examples/agent-system-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/mastermind.md" in payload["research_refs"]
    assert "Kaynexis" in payload["agent_titles"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"mastermind-summary", "mastermind-control-loop", "mastermind-handoffs", "mastermind-validation", "mastermind-doc-sync"}.issubset(item_ids)


def test_route_task_surfaces_openai_codex_guidance_for_agent_platform_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals",
        "--json",
    )
    assert payload["route"] == "openai / codex / agent platform"
    assert "docs/research/openai-codex-infra-findings.md" in payload["docs"]
    assert "docs/reference/codex-compatibility.md" in payload["docs"]
    assert "docs/reference/agent-system.md" in payload["docs"]
    assert "docs/reference/mastermind-guide.md" in payload["docs"]
    assert "docs/reference/quality-process.md" in payload["docs"]
    assert "docs/reference/benchmark-guide.md" in payload["docs"]
    assert "Kaynexis" in payload["agent_titles"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"openai-controller-policy", "openai-prompt-version", "openai-tool-access", "openai-eval-path", "openai-single-specialist", "openai-doc-sync"}.issubset(item_ids)
    assert "docs/research/openai-codex-infra-findings.md" in payload["research_refs"]
    assert "docs/reference/codex-compatibility.md" in payload["research_refs"]
    assert "docs/reference/eval-strategy.md" in payload["research_refs"]


def test_route_task_surfaces_openai_model_selection_guidance() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Choose the right Codex model and ChatGPT plan tier for a heavy multi-file refactor",
        "--json",
    )
    assert payload["route"] == "openai / codex / model selection"
    assert "docs/research/openai-codex-models.md" in payload["docs"]
    assert "docs/reference/codex-model-guide.md" in payload["docs"]
    assert "docs/examples/codex-model-guide-example.md" in payload["docs"]
    assert "studio/docs/active/eval-openai-models.md" in payload["docs"]
    assert "docs/research/openai-codex-models.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"openai-model-choice-explicit", "openai-smallest-model-first", "openai-plan-vs-api", "openai-model-doc-sync"}.issubset(item_ids)


def test_route_task_surfaces_agent_system_guidance_for_operating_model_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail",
        "--json",
    )
    assert payload["route"] == "agent system / operating model"
    assert "docs/reference/agent-system.md" in payload["docs"]
    assert "docs/examples/agent-system-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/agent-system.md" in payload["research_refs"]
    assert payload["agent_titles"][0] == "Kaynexis"
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"mastermind-summary", "agent-mode-picked", "hierarchy-single-specialist", "journal-prompt-history"}.issubset(item_ids)


def test_mastermind_public_title_is_kaynexis() -> None:
    assert agent_public_title("mastermind") == "Kaynexis"


def test_route_task_surfaces_agent_portfolio_guidance_for_role_matrix_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode",
        "--json",
    )
    assert payload["route"] == "agent portfolio / role matrix"
    assert "docs/reference/agent-portfolio.md" in payload["docs"]
    assert "docs/examples/agent-portfolio-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/agent-portfolio.md" in payload["research_refs"]
    assert payload["agent_titles"] == ["Marie Curie", "Alan Turing", "Charles Darwin"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"agent-mode-picked", "agent-role-owned", "agent-handoffs", "agent-validation", "agent-doc-sync"}.issubset(item_ids)


def test_route_task_surfaces_agent_model_overrides_for_role_matrix_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode",
        "--agent-model",
        "producer=gpt-5.4-pro",
        "--agent-model",
        "technical_director=gpt-5.4-mini",
        "--json",
    )
    assert payload["route"] == "agent portfolio / role matrix"
    assert payload["agent_model_overrides"] == {"producer": "gpt-5.4-pro", "technical_director": "gpt-5.4-mini"}
    models = {item["agent"]: item for item in payload["agent_models"]}
    assert models["producer"]["model"] == "gpt-5.4-pro"
    assert models["producer"]["source"] == "override"
    assert models["technical_director"]["model"] == "gpt-5.4-mini"
    assert models["technical_director"]["source"] == "override"
    assert models["docs_researcher"]["source"] == "profile"


def test_route_task_surfaces_agent_hierarchy_guidance_for_command_tree_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane, but keep the single specialist option available if the scope shrinks",
        "--json",
    )
    assert payload["route"] == "agent hierarchy / command tree"
    assert "docs/reference/agent-hierarchy.md" in payload["docs"]
    assert "docs/examples/agent-hierarchy-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/agent-hierarchy.md" in payload["research_refs"]
    assert payload["agent_titles"] == ["Marie Curie", "Alan Turing", "Rosalind Franklin"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"hierarchy-single-specialist", "hierarchy-title-picked", "hierarchy-command-tree", "hierarchy-async-packet", "hierarchy-doc-sync"}.issubset(item_ids)


def test_route_task_surfaces_agent_validation_guidance_for_validation_matrix_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Build validation matrices for operating mode, proof rows, transcript history, and model overrides while keeping single specialist fallback visible",
        "--json",
    )
    assert payload["route"] == "agent validation / matrix catalog"
    assert "docs/reference/agent-validation-matrix.md" in payload["docs"]
    assert "docs/examples/agent-validation-matrix-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/agent-validation-matrix.md" in payload["research_refs"]
    assert "docs/reference/agent-system.md" in payload["docs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"agent-validation-scope", "agent-validation-rows", "agent-validation-history", "agent-validation-models", "agent-validation-doc-sync"}.issubset(item_ids)


def test_route_task_engine_inference() -> None:
    payload = run_json("scripts/route_task.py", "Plan the next Unity starter kit task", "--json")
    assert payload["route"] == "engine / tooling / packaging"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/research/game-development/engines/unity-map.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unity-classes.md" in payload["research_refs"]


def test_route_task_keeps_gameplay_route_when_engine_is_mentioned() -> None:
    payload = run_json("scripts/route_task.py", "Implement Unity combat room", "--json")
    assert payload["route"] == "combat / gameplay"
    assert payload["engine_kit"]["id"] == "unity-6"


def test_route_task_surfaces_engine_system_note_for_navigation_and_damage() -> None:
    payload = run_json("scripts/route_task.py", "Design a Unity navmesh and damage system", "--json")
    assert payload["route"] == "combat / gameplay"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/research/game-development/engines/unity-performance.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unity-systems.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert "unity-navigation-choice" in item_ids
    assert "unity-damage-query-contract" in item_ids


def test_route_task_surfaces_engine_system_playbooks_for_ui_and_inventory() -> None:
    ui_payload = run_json("scripts/route_task.py", "Design a Godot HUD and menu screen flow", "--json")
    assert ui_payload["engine_kit"]["id"] == "godot-4"
    assert "docs/research/game-development/engines/godot-systems.md" in ui_payload["research_refs"]

    inventory_payload = run_json("scripts/route_task.py", "Implement a Unreal inventory and equipment screen", "--json")
    assert inventory_payload["engine_kit"]["id"] == "unreal-5"
    assert "docs/research/game-development/engines/unreal-systems.md" in inventory_payload["research_refs"]


def test_route_task_surfaces_engine_eval_guidance_for_engine_comparison() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Compare Unity 6 and Unreal 5 in an engine evaluation scorecard for build, test, performance, and toolchain readiness",
        "--json",
    )
    assert payload["route"] == "engine / evaluation / scorecard"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/reference/engine-eval.md" in payload["docs"]
    assert "docs/examples/engine-eval-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/engine-eval.md" in payload["docs"]
    assert "docs/reference/engine-selection-guide.md" in payload["docs"]
    assert "docs/reference/engine-map.md" in payload["docs"]
    assert "docs/reference/engine-examples.md" in payload["docs"]
    assert "docs/reference/benchmark-guide.md" in payload["docs"]
    assert "docs/reference/perf-guide.md" in payload["docs"]
    assert "docs/reference/quality-guide.md" in payload["docs"]
    assert "docs/reference/ci-cd.md" in payload["docs"]
    assert "studio/docs/active/engine-eval.md" in payload["docs"]
    assert "studio/docs/active/eval-engine-eval.md" in payload["docs"]
    assert "Kaynexis" in payload["agent_titles"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {
        "engine-source-hierarchy",
        "engine-family-split",
        "engine-build-contract",
        "engine-test-contract",
        "engine-performance-baseline",
        "engine-toolchain-readiness",
        "engine-scorecard-artifact",
        "engine-doc-sync",
    }.issubset(item_ids)
    assert {"ci-short-names", "benchmark-family", "quality-owner", "quality-process", "perf-first-lever"}.issubset(item_ids)


def test_route_task_surfaces_platform_compatibility_guidance_for_multi_platform_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Map platform compatibility for Windows, macOS, Linux/Steam Deck, web, Android/iOS, and TV/webOS",
        "--json",
    )
    assert payload["route"] == "platform / compatibility / readiness"
    assert "docs/reference/platform-guide.md" in payload["docs"]
    assert "docs/examples/platform-example.md" in payload["docs"]
    assert "docs/research/game-development/production/platform-compatibility.md" in payload["docs"]
    assert "studio/docs/active/platform-targets.md" in payload["docs"]
    assert "studio/docs/active/eval-platform-compatibility.md" in payload["docs"]
    assert payload["agent_titles"][0] == "Kaynexis"
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"platform-source-hierarchy", "platform-family-split", "platform-input-model", "platform-performance-envelope", "platform-policy-watch", "platform-visual-pack", "platform-doc-sync"}.issubset(item_ids)
    assert "docs/research/game-development/production/platform-compatibility.md" in payload["research_refs"]


def test_route_task_surfaces_console_guidance_for_ps5_like_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Plan PS5-like console premium readiness for a port",
        "--json",
    )
    assert payload["route"] == "console / compliance / porting"
    assert "docs/reference/console-guide.md" in payload["docs"]
    assert "docs/examples/console-example.md" in payload["docs"]
    assert "docs/research/game-development/production/console.md" in payload["docs"]
    assert "studio/checklists/discipline/console.toml" in payload["docs"]
    assert "studio/docs/active/eval-console.md" in payload["docs"]
    assert "docs/reference/platform-guide.md" in payload["research_refs"]
    assert "docs/reference/cross-platform-guide.md" in payload["research_refs"]
    assert "docs/research/game-development/production/console.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {
        "console-source-hierarchy",
        "console-family-split",
        "console-input-model",
        "console-suspend-save",
        "console-cert-risk",
        "console-release-sequence",
        "console-doc-sync",
    }.issubset(item_ids)


def test_route_task_surfaces_engine_visuals_playbooks_for_sprite_and_animation_work() -> None:
    payload = run_json("scripts/route_task.py", "Plan the sprite atlas and animation pass for Unity", "--json")
    assert payload["route"] == "visuals / animation / presentation"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/research/game-development/engines/unity-visuals.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/ux.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert "unity-visuals-animation-owner" in item_ids


def test_route_task_surfaces_audio_presentation_playbooks_for_timing_work() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Run an audio and animation pass on a Godot boss windup and keep the gameplay truth separate from presentation",
        "--json",
    )
    assert payload["route"] == "audio / animation / presentation"
    assert payload["engine_kit"]["id"] == "godot-4"
    assert "docs/reference/audio-animation-guide.md" in payload["docs"]
    assert "docs/examples/audio-animation-example.md" in payload["docs"]
    assert "docs/research/game-development/engines/godot-presentation.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"presentation-owner", "presentation-tier", "presentation-sync", "presentation-evidence", "presentation-doc-sync", "content-authoring-path"}.issubset(item_ids)


def test_route_task_surfaces_gpu_guide_for_render_communication_work() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Research the GPU communication path for a Godot 4 survivorlike and decide whether MultiMesh or RenderingDevice is the first lever",
        "--json",
    )
    assert payload["route"] == "gpu / rendering / communication"
    assert payload["engine_kit"]["id"] == "godot-4"
    assert "docs/reference/gpu-guide.md" in payload["docs"]
    assert "docs/examples/gpu-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/gpu.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/godot-gpu.md" in payload["research_refs"]


def test_route_task_surfaces_crafting_and_party_research_refs() -> None:
    crafting_payload = run_json("scripts/route_task.py", "Design a crafting bench and recipe unlock flow", "--json")
    assert crafting_payload["route"] == "combat / gameplay"
    assert "docs/research/game-development/systems/crafting.md" in crafting_payload["research_refs"]

    companion_payload = run_json("scripts/route_task.py", "Implement companion follower AI and squad formation rules", "--json")
    assert companion_payload["route"] == "combat / gameplay"
    assert "docs/research/game-development/systems/party.md" in companion_payload["research_refs"]


def test_route_task_surfaces_dialogue_and_quest_state_research_refs() -> None:
    payload = run_json("scripts/route_task.py", "Implement a branching dialogue scene with quest stage progression", "--json")
    assert payload["route"] == "narrative / quest"
    assert "docs/research/game-development/systems/dialogue.md" in payload["research_refs"]


def test_route_task_surfaces_lorebook_research_refs() -> None:
    payload = run_json("scripts/route_task.py", "Design a lorebook flow for faction canon and unlockable archive entries", "--json")
    assert payload["route"] == "narrative / lorebook"
    assert "docs/reference/lorebook-methodology.md" in payload["docs"]
    assert "docs/examples/lorebook-example.md" in payload["docs"]
    assert "docs/research/game-development/narrative/lorebook.md" in payload["research_refs"]


def test_route_task_surfaces_world_graph_research_refs() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Design a world graph for faction history, organization ties, and codex reads",
        "--json",
    )
    assert payload["route"] == "narrative / world graph"
    assert "docs/reference/world-graph-methodology.md" in payload["docs"]
    assert "docs/examples/world-graph-example.md" in payload["docs"]
    assert "docs/research/game-development/narrative/world-graph.md" in payload["research_refs"]
    assert "docs/research/game-development/narrative/lorebook.md" in payload["research_refs"]


def test_route_task_surfaces_prompt_journal_guidance_for_reviewable_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Record prompt history and an agent journal for later review",
        "--json",
    )
    assert payload["route"] == "prompt history / agent journal"
    assert "docs/reference/prompt-journal.md" in payload["docs"]
    assert "docs/examples/prompt-journal-example.md" in payload["docs"]
    assert "studio/docs/active/prompt-journal.md" in payload["docs"]
    assert "studio/docs/active/eval-prompt-journal.md" in payload["docs"]
    assert "docs/research/game-development/foundations/prompt-journal.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"journal-prompt-history", "journal-agent-step", "journal-review-path", "journal-doc-sync"}.issubset(item_ids)


def test_route_task_surfaces_agent_transcript_guidance_for_handoff_history() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Record agent-to-agent assignment history and conversation turns for later review",
        "--json",
    )
    assert payload["route"] == "agent transcript / conversation history"
    assert "docs/reference/agent-transcript.md" in payload["docs"]
    assert "docs/examples/agent-transcript-example.md" in payload["docs"]
    assert "studio/docs/active/agent-transcript.md" in payload["docs"]
    assert "studio/docs/active/eval-agent-transcript.md" in payload["docs"]
    assert "docs/research/game-development/foundations/agent-transcript.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"transcript-assignment", "transcript-conversation", "transcript-review-path", "transcript-doc-sync"}.issubset(item_ids)


def test_codex_studio_journal_prompt_dry_run() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "journal",
        "prompt",
        "--prompt",
        "Record this prompt for later review",
        "--route",
        "prompt history / agent journal",
        "--summary",
        "Captured the prompt in the review trail.",
        "--doc",
        "docs/reference/prompt-journal.md",
        "--dry-run",
        "--json",
    )
    assert payload["kind"] == "prompt"
    assert payload["path"] == "studio/docs/active/prompt-journal.md"
    assert "Record this prompt for later review" in payload["entry"]
    assert "Route: prompt history / agent journal" in payload["entry"]
    assert "Docs: docs/reference/prompt-journal.md" in payload["entry"]


def test_codex_studio_packet_dry_run() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "packet",
        "--task",
        "Build an execution packet for a UI refactor",
        "--owner",
        "Kaynexis",
        "--mode",
        "paired-specialist",
        "--goal",
        "Keep the refactor narrow",
        "--route",
        "agent execution / work packet",
        "--input",
        "current route output",
        "--input",
        "current checklist bundle",
        "--output",
        "one packet",
        "--output",
        "one proof path",
        "--proof-path",
        "python3 scripts/codex_studio.py packet --dry-run --json",
        "--rule",
        "Keep single-specialist fallback visible",
        "--stop-condition",
        "owner is ambiguous",
        "--stop-condition",
        "proof path is missing",
        "--next-step",
        "Hand this packet to the UI specialist",
        "--doc",
        "docs/reference/agent-execution.md",
        "--validation",
        "python3 scripts/codex_studio.py packet --dry-run --json",
        "--dry-run",
        "--json",
    )
    assert payload["kind"] == "packet"
    assert payload["path"] == "studio/docs/active/agent-execution.md"
    assert "Task: Build an execution packet for a UI refactor" in payload["entry"]
    assert "Owner: Kaynexis" in payload["entry"]
    assert "Mode: paired-specialist" in payload["entry"]
    assert "Goal: Keep the refactor narrow" in payload["entry"]
    assert "Route: agent execution / work packet" in payload["entry"]
    assert "Inputs: current route output, current checklist bundle" in payload["entry"]
    assert "Outputs: one packet, one proof path" in payload["entry"]
    assert "Proof path: python3 scripts/codex_studio.py packet --dry-run --json" in payload["entry"]
    assert "Custom rules: Keep single-specialist fallback visible" in payload["entry"]
    assert "Stop conditions: owner is ambiguous, proof path is missing" in payload["entry"]
    assert "Next step: Hand this packet to the UI specialist" in payload["entry"]


def test_codex_studio_interactive_menu_surfaces_execution_packet(monkeypatch) -> None:
    answers = iter(
        [
            "8",
            "Build an execution packet for a UI refactor",
            "Kaynexis",
            "single-specialist",
            "Keep the refactor narrow",
            "agent execution / work packet",
            "current route output, current checklist bundle",
            "one packet, one proof path",
            "python3 scripts/codex_studio.py packet --dry-run --json",
            "Keep single-specialist fallback visible",
            "owner is ambiguous, proof path is missing",
            "Hand this packet to the UI specialist",
        ]
    )
    monkeypatch.setattr("builtins.input", lambda prompt="": next(answers))
    args = interactive_menu()
    assert args.command == "packet"
    assert args.task == "Build an execution packet for a UI refactor"
    assert args.owner == "Kaynexis"
    assert args.mode == "single-specialist"
    assert args.goal == "Keep the refactor narrow"
    assert args.route == "agent execution / work packet"
    assert args.input == ["current route output", "current checklist bundle"]
    assert args.output == ["one packet", "one proof path"]
    assert args.proof_path == "python3 scripts/codex_studio.py packet --dry-run --json"
    assert args.rule == ["Keep single-specialist fallback visible"]
    assert args.stop_condition == ["owner is ambiguous", "proof path is missing"]
    assert args.next_step == "Hand this packet to the UI specialist"


def test_codex_studio_journal_transcript_assignment_dry_run() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "journal",
        "transcript",
        "--kind",
        "assignment",
        "--task",
        "Assign the combat slice to a worker",
        "--speaker",
        "Kaynexis",
        "--target",
        "engine_programmer",
        "--message",
        "Take the combat slice and keep the assignment history append-only.",
        "--result",
        "Worker acknowledged the task",
        "--doc",
        "docs/reference/agent-transcript.md",
        "--validation",
        "python3 scripts/journal.py transcript --kind assignment --dry-run --json",
        "--dry-run",
        "--json",
    )
    assert payload["kind"] == "transcript"
    assert payload["path"] == "studio/docs/active/agent-transcript.md"
    assert "Assign the combat slice to a worker" in payload["entry"]
    assert "Speaker: Kaynexis" in payload["entry"]
    assert "Target: engine_programmer" in payload["entry"]
    assert "Message: Take the combat slice and keep the assignment history append-only." in payload["entry"]
    assert "Result: Worker acknowledged the task" in payload["entry"]
    assert "Validation: python3 scripts/journal.py transcript --kind assignment --dry-run --json" in payload["entry"]


def test_codex_studio_journal_transcript_conversation_dry_run() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "journal",
        "transcript",
        "--kind",
        "conversation",
        "--speaker",
        "technical_director",
        "--target",
        "qa_lead",
        "--message",
        "The combat slice still needs one more review pass before merge.",
        "--next-step",
        "QA will validate the handoff and reopen if needed.",
        "--doc",
        "docs/reference/agent-transcript.md",
        "--validation",
        "python3 scripts/journal.py transcript --kind conversation --dry-run --json",
        "--dry-run",
        "--json",
    )
    assert payload["kind"] == "transcript"
    assert payload["path"] == "studio/docs/active/agent-transcript.md"
    assert "Kind: conversation" in payload["entry"]
    assert "Speaker: technical_director" in payload["entry"]
    assert "Target: qa_lead" in payload["entry"]
    assert "Message: The combat slice still needs one more review pass before merge." in payload["entry"]
    assert "Next step: QA will validate the handoff and reopen if needed." in payload["entry"]
    assert "Validation: python3 scripts/journal.py transcript --kind conversation --dry-run --json" in payload["entry"]


def test_codex_studio_journal_agent_dry_run() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "journal",
        "agent",
        "--step",
        "Draft the journal template and journal command",
        "--expected",
        "One active file with two append-only sections",
        "--found",
        "The repo had no durable history trail yet",
        "--improved",
        "Added a shared prompt journal file and append helper",
        "--evaluation",
        "The record is now easy to reopen later without reading the whole chat",
        "--doc",
        "docs/reference/prompt-journal.md",
        "--validation",
        "python3 scripts/journal.py prompt --dry-run --json",
        "--dry-run",
        "--json",
    )
    assert payload["kind"] == "agent"
    assert payload["path"] == "studio/docs/active/prompt-journal.md"
    assert "Step: Draft the journal template and journal command" in payload["entry"]
    assert "Expected: One active file with two append-only sections" in payload["entry"]
    assert "Validation: python3 scripts/journal.py prompt --dry-run --json" in payload["entry"]


def test_transcript_checklist_includes_transcript_and_support_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["transcript"], milestone="prototype", agent_name="producer")
    item_ids = {item["id"] for item in items}
    assert {"transcript-assignment", "transcript-conversation", "transcript-review-path", "transcript-doc-sync"}.issubset(item_ids)
    assert {"journal-prompt-history", "mastermind-summary"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/transcript.toml") for item in items)


def test_append_markdown_before_marker_inserts_before_marker(tmp_path: Path) -> None:
    from _studio_common import append_markdown_before_marker

    target = tmp_path / "journal.md"
    target.write_text("header\n<!-- prompt-history-append -->\n<!-- agent-journal-append -->\n", encoding="utf-8")
    append_markdown_before_marker(target, "prompt-history-append", "entry block", seed_text=target.read_text(encoding="utf-8"))
    text = target.read_text(encoding="utf-8")
    assert text.index("entry block") < text.index("<!-- prompt-history-append -->")
    assert "<!-- prompt-history-append -->" in text
    assert "<!-- agent-journal-append -->" in text


def test_route_task_surfaces_hotfix_and_rollback_research() -> None:
    payload = run_json("scripts/route_task.py", "Prepare a hotfix rollback plan for a crash", "--json")
    assert payload["route"] == "bug / crash / regression"
    assert "docs/research/game-development/production/incident.md" in payload["research_refs"]
    assert "studio/docs/templates/release-checklist.md" in payload["docs"]


def test_route_task_surfaces_quality_and_optimization_guidance() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Review code quality and optimization criteria for a Unity 6 inventory HUD before refactoring",
        "--json",
    )
    assert payload["route"] == "quality / optimization"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/reference/quality-guide.md" in payload["docs"]
    assert "docs/reference/quality-process.md" in payload["docs"]
    assert "docs/examples/quality-example.md" in payload["docs"]
    assert "docs/examples/quality-process-example.md" in payload["docs"]
    assert "docs/reference/code-review.md" in payload["docs"]
    assert "docs/reference/perf-guide.md" in payload["docs"]
    assert "docs/examples/perf-example.md" in payload["docs"]
    assert "docs/reference/advanced-perf-guide.md" in payload["docs"]
    assert "docs/examples/advanced-perf-example.md" in payload["docs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"quality-owner", "quality-process", "quality-evidence", "quality-opt-baseline", "perf-first-lever"}.issubset(item_ids)


def test_route_task_surfaces_quality_control_process_for_quality_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate",
        "--json",
    )
    assert payload["route"] == "quality / optimization"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/reference/quality-process.md" in payload["docs"]
    assert "docs/examples/quality-process-example.md" in payload["docs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"quality-owner", "quality-process", "quality-evidence"}.issubset(item_ids)


def test_route_task_surfaces_benchmark_measurement_refs() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio",
        "--json",
    )
    assert payload["route"] == "benchmark / measurement"
    assert "docs/reference/benchmark-guide.md" in payload["docs"]
    assert "docs/examples/benchmark-example.md" in payload["docs"]
    assert "docs/reference/eval-strategy.md" in payload["docs"]
    assert "docs/reference/benchmark-guide.md" in payload["research_refs"]
    assert "docs/examples/benchmark-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/benchmarks.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"benchmark-family", "benchmark-baseline", "benchmark-threshold", "benchmark-coverage", "benchmark-artifact", "benchmark-doc-sync"}.issubset(item_ids)


def test_benchmark_checklist_includes_benchmark_and_support_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["benchmark"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {"benchmark-family", "benchmark-baseline", "benchmark-threshold", "benchmark-coverage", "benchmark-artifact", "benchmark-doc-sync"}.issubset(item_ids)
    assert {"quality-owner", "quality-process", "perf-first-lever"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/benchmark.toml") for item in items)


def test_engine_eval_checklist_includes_engine_eval_and_support_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["engine_eval"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {
        "engine-source-hierarchy",
        "engine-family-split",
        "engine-build-contract",
        "engine-test-contract",
        "engine-performance-baseline",
        "engine-toolchain-readiness",
        "engine-scorecard-artifact",
        "engine-doc-sync",
    }.issubset(item_ids)
    assert {"ci-short-names", "benchmark-family", "quality-owner", "quality-process", "quality-evidence", "perf-first-lever"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/engine_eval.toml") for item in items)


def test_engine_fit_checklist_includes_engine_fit_and_research_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["engine_fit"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {
        "engine-profile-named",
        "engine-language-fit",
        "engine-collaboration-fit",
        "engine-platform-fit",
        "engine-tooling-fit",
        "engine-proof-path",
        "engine-tradeoff-matrix",
        "engine-doc-sync",
    }.issubset(item_ids)
    assert {"research-primary-sources", "research-repo-impact"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/engine_fit.toml") for item in items)


def test_route_task_surfaces_marketing_strategy_refs() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Build a marketing strategy for a Steam-first indie survival game",
        "--json",
    )
    assert payload["route"] == "marketing / strategy / measurement"
    assert "docs/reference/marketing-guide.md" in payload["docs"]
    assert "docs/examples/marketing-example.md" in payload["docs"]
    assert "docs/research/game-development/production/marketing.md" in payload["docs"]
    assert "studio/docs/templates/marketing-plan.md" in payload["docs"]
    assert "studio/docs/templates/storefront-checklist.md" in payload["docs"]
    assert "docs/reference/marketing-guide.md" in payload["research_refs"]
    assert "docs/examples/marketing-example.md" in payload["research_refs"]
    assert "docs/research/game-development/production/marketing.md" in payload["research_refs"]
    assert "docs/reference/sector-intel.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {
        "marketing-source-hierarchy",
        "marketing-objective",
        "marketing-audience-and-promise",
        "marketing-channel-fit",
        "marketing-asset-readiness",
        "marketing-metrics-and-baseline",
        "marketing-policy-watch",
        "marketing-doc-sync",
    }.issubset(item_ids)


def test_codex_studio_checklist_surfaces_marketing_guidance() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Build a marketing strategy for a Steam-first indie survival game",
        "--json",
    )
    assert "marketing" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {
        "marketing-source-hierarchy",
        "marketing-objective",
        "marketing-audience-and-promise",
        "marketing-channel-fit",
        "marketing-asset-readiness",
        "marketing-metrics-and-baseline",
        "marketing-policy-watch",
        "marketing-doc-sync",
    }.issubset(item_ids)
    assert "docs/reference/marketing-guide.md" in payload["research_refs"]
    assert "docs/examples/marketing-example.md" in payload["research_refs"]
    assert "docs/research/game-development/production/marketing.md" in payload["research_refs"]
    assert "docs/reference/sector-intel.md" in payload["research_refs"]


def test_steam_intel_checklist_includes_steam_and_support_layers() -> None:
    items = resolve_checklists(engine_slug="godot-4", disciplines=["steam_intel"], milestone="prototype", agent_name="producer")
    item_ids = {item["id"] for item in items}
    assert {
        "steam-source-hierarchy",
        "steam-current-window",
        "steam-signal-split",
        "steam-visual-pack",
        "steam-forum-themes",
        "steam-permissions",
        "steam-doc-sync",
    }.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/steam_intel.toml") for item in items)


def test_route_task_surfaces_steam_intel_refs() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Track Steam store traffic, wishlists, forum themes, and hardware mix for a Steam-first survival game",
        "--json",
    )
    assert payload["route"] == "steam / market intelligence"
    assert "docs/reference/steam-intel.md" in payload["docs"]
    assert "docs/examples/steam-intel-example.md" in payload["docs"]
    assert "docs/research/game-development/production/steam-intel.md" in payload["docs"]
    assert "docs/reference/sector-intel.md" in payload["docs"]
    assert "docs/reference/marketing-guide.md" in payload["docs"]
    assert "docs/research/game-development/production/README.md" in payload["docs"]
    assert "docs/reference/steam-intel.md" in payload["research_refs"]
    assert "docs/examples/steam-intel-example.md" in payload["research_refs"]
    assert "docs/research/game-development/production/steam-intel.md" in payload["research_refs"]
    assert "Kaynexis" in payload["agent_titles"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {
        "steam-source-hierarchy",
        "steam-current-window",
        "steam-signal-split",
        "steam-visual-pack",
        "steam-forum-themes",
        "steam-permissions",
        "steam-doc-sync",
    }.issubset(item_ids)


def test_route_task_surfaces_build_release_support_for_release_work() -> None:
    payload = run_json("scripts/route_task.py", "Prepare a release readiness bundle for the demo build", "--json")
    assert payload["route"] == "release / storefront / marketing"
    item_ids = {item["id"] for item in payload["checklists"]}
    assert "ci-short-names" in item_ids
    assert any(item["source"].endswith("studio/checklists/discipline/build-release.toml") for item in payload["checklists"])


def test_route_task_uses_performance_route_for_pooling_and_alloc_work() -> None:
    payload = run_json("scripts/route_task.py", "Optimize Unity projectile pooling and allocations", "--json")
    assert payload["route"] == "performance"
    assert payload["engine_kit"]["id"] == "unity-6"
    item_ids = {item["id"] for item in payload["checklists"]}
    assert "perf-representation-choice" in item_ids
    assert "perf-first-lever" in item_ids
    assert "docs/reference/perf-guide.md" in payload["docs"]
    assert "docs/examples/perf-example.md" in payload["docs"]
    assert "docs/reference/genre-perf-guide.md" in payload["docs"]
    assert "docs/examples/genre-perf-example.md" in payload["docs"]
    assert "docs/research/game-development/engines/unity-performance.md" in payload["research_refs"]


def test_route_task_surfaces_advanced_perf_guide_for_algorithmic_scale_work() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Research advanced optimization algorithms for a Unity 6 city-builder and compare Burst jobs with occlusion culling",
        "--json",
    )
    assert payload["route"] == "advanced performance / algorithms"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/reference/advanced-perf-guide.md" in payload["docs"]
    assert "docs/examples/advanced-perf-example.md" in payload["docs"]
    assert "docs/research/game-development/foundations/perf-algorithms.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"advanced-perf-owner", "advanced-perf-baseline", "perf-first-lever"}.issubset(item_ids)


def test_codex_studio_checklist_surfaces_perf_guide_for_performance_tasks() -> None:
    payload = run_json("scripts/codex_studio.py", "checklist", "--task", "Optimize a Godot survivorlike for fps and memory", "--json")
    assert "performance" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert "perf-first-lever" in item_ids
    assert "docs/reference/perf-guide.md" in payload["research_refs"]
    assert "docs/examples/perf-example.md" in payload["research_refs"]
    assert "docs/reference/genre-perf-guide.md" in payload["research_refs"]
    assert "docs/examples/genre-perf-example.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_quality_guidance_for_refactor_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Review code quality and optimization criteria for a Unity 6 inventory HUD before refactoring",
        "--json",
    )
    assert "quality" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"quality-owner", "quality-process", "quality-evidence", "quality-opt-baseline", "perf-first-lever"}.issubset(item_ids)
    assert "docs/reference/quality-guide.md" in payload["research_refs"]
    assert "docs/reference/quality-process.md" in payload["research_refs"]
    assert "docs/examples/quality-example.md" in payload["research_refs"]
    assert "docs/examples/quality-process-example.md" in payload["research_refs"]
    assert "docs/reference/code-review.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_quality_control_process_for_quality_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Run a quality control pass on a Unity 6 inventory HUD and name the go/no-go gate",
        "--json",
    )
    assert "quality" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"quality-owner", "quality-process", "quality-evidence"}.issubset(item_ids)
    assert "docs/reference/quality-guide.md" in payload["research_refs"]
    assert "docs/reference/quality-process.md" in payload["research_refs"]
    assert "docs/examples/quality-process-example.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_benchmark_guidance_for_measurement_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio",
        "--json",
    )
    assert "benchmark" in payload["disciplines"]
    assert "quality" in payload["disciplines"]
    assert "performance" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"benchmark-family", "benchmark-baseline", "benchmark-threshold", "benchmark-coverage", "benchmark-artifact", "benchmark-doc-sync"}.issubset(item_ids)
    assert {"quality-owner", "quality-process", "quality-evidence", "perf-first-lever"}.issubset(item_ids)
    assert "docs/reference/benchmark-guide.md" in payload["research_refs"]
    assert "docs/examples/benchmark-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/benchmarks.md" in payload["research_refs"]


def test_run_bench_contract_surface(tmp_path: Path) -> None:
    output_dir = tmp_path / "bench"
    payload = run_json("scripts/run_bench.py", "--output-dir", str(output_dir), "--json")
    summary = payload["summary"]
    assert summary["case_count"] >= 4
    assert summary["failure_count"] == 0
    assert summary["readiness"] == "benchmark-ready"
    assert summary["score"] >= 90
    assert any(family["name"] == "Repo-local" for family in payload["families"])
    assert Path(payload["artifacts"]["json"]).exists()
    assert Path(payload["artifacts"]["markdown"]).exists()


def test_codex_studio_checklist_surfaces_advanced_perf_guide_for_algorithmic_work() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Research advanced optimization algorithms for a Godot swarm and decide whether spatial hashing or MultiMesh is first lever",
        "--json",
    )
    assert "performance" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert "perf-first-lever" in item_ids
    assert "docs/reference/advanced-perf-guide.md" in payload["research_refs"]
    assert "docs/examples/advanced-perf-example.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_gpu_guidance_for_render_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Review GPU ownership and CPU-GPU communication for a Unity 6 projectile field",
        "--json",
    )
    assert "gpu" in payload["disciplines"]
    assert "performance" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"gpu-owner", "gpu-baseline", "gpu-communication", "gpu-representation", "gpu-validation"}.issubset(item_ids)
    assert "docs/reference/gpu-guide.md" in payload["research_refs"]
    assert "docs/examples/gpu-example.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unity-gpu.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_presentation_guidance_for_audio_animation_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Run an audio and animation pass on a Unity 6 inventory HUD and keep the gameplay truth separate from presentation",
        "--json",
    )
    assert "presentation" in payload["disciplines"]
    assert "content-pipeline" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"presentation-owner", "presentation-tier", "presentation-sync", "presentation-evidence", "presentation-doc-sync"}.issubset(item_ids)
    assert {"content-authoring-path", "content-naming"}.issubset(item_ids)
    assert "docs/reference/audio-animation-guide.md" in payload["research_refs"]
    assert "docs/examples/audio-animation-example.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unity-presentation.md" in payload["research_refs"]


def test_route_task_surfaces_genre_perf_guide_for_genre_scale_work() -> None:
    payload = run_json("scripts/route_task.py", "Run a performance pass on a city-builder by chunking simulation and virtualizing district UI", "--json")
    assert payload["route"] == "performance"
    assert "docs/reference/genre-perf-guide.md" in payload["docs"]
    assert "docs/examples/genre-perf-example.md" in payload["docs"]
    assert "docs/reference/perf-guide.md" in payload["docs"]


def test_route_task_surfaces_genre_pattern_catalog_for_genre_work() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Research genre software patterns and contrast sets for a deckbuilder roguelike before implementation",
        "--json",
    )
    assert payload["route"] == "genre / software patterns"
    assert "docs/reference/genre-plan.md" in payload["docs"]
    assert "docs/examples/genre-plan-example.md" in payload["docs"]
    assert "docs/research/game-development/genre/genre-plan.md" in payload["docs"]
    assert "docs/research/game-development/genre/genre-guide.md" in payload["docs"]
    assert "docs/research/game-development/genre/genre-patterns.md" in payload["docs"]
    assert "docs/research/game-development/genre/genre-examples.md" in payload["docs"]
    assert "docs/examples/genre-gallery-example.md" in payload["docs"]
    assert "docs/research/game-development/genre/genre-maturity.md" in payload["docs"]
    assert "docs/reference/genre-presets.md" in payload["docs"]
    assert any(item["source"].endswith("studio/checklists/discipline/genre.toml") for item in payload["checklists"])


def test_route_task_surfaces_genre_plan_schema_for_genre_planning_work() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Write a genre plan schema for a tactical RPG that names the player outcome and loop ladder",
        "--json",
    )
    assert payload["route"] == "genre / plan schema"
    assert "docs/reference/genre-plan.md" in payload["docs"]
    assert "docs/examples/genre-plan-example.md" in payload["docs"]
    assert "docs/research/game-development/genre/genre-plan.md" in payload["docs"]
    assert "docs/research/game-development/genre/genre-guide.md" in payload["docs"]
    assert any(item["source"].endswith("studio/checklists/discipline/genre.toml") for item in payload["checklists"])


def test_route_task_surfaces_library_selection_guide() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Choose the smallest official library set for a Unity 6 inventory HUD and controller remap flow",
        "--json",
    )
    assert payload["route"] == "libraries / dependencies"
    assert "docs/reference/library-guide.md" in payload["docs"]
    assert "docs/examples/library-example.md" in payload["docs"]
    assert "docs/reference/library-guide.md" in payload["research_refs"]
    assert "docs/examples/library-example.md" in payload["research_refs"]


def test_route_task_surfaces_asset_guidance_for_pipeline_work() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Decide asset ownership and import boundaries for a Unity 6 inventory HUD",
        "--json",
    )
    assert payload["route"] == "assets / content pipeline"
    assert payload["engine_kit"]["id"] == "unity-6"
    assert "docs/reference/asset-guide.md" in payload["docs"]
    assert "docs/examples/asset-example.md" in payload["docs"]
    assert "docs/research/game-development/assets/README.md" in payload["research_refs"]
    assert "docs/research/game-development/assets/alternatives.md" in payload["research_refs"]
    assert "docs/research/game-development/assets/ownership.md" in payload["research_refs"]
    assert "docs/research/game-development/assets/import.md" in payload["research_refs"]


def test_route_task_avoids_false_positive_substring_matches() -> None:
    party_payload = run_json("scripts/route_task.py", "Party invite flow", "--json")
    assert party_payload["route"] == "fallback"

    starter_payload = run_json("scripts/route_task.py", "Research starter task flow", "--json")
    assert starter_payload["route"] == "fallback"


def test_route_task_surfaces_handoff_and_traceability_route() -> None:
    payload = run_json("scripts/route_task.py", "Prepare a clean handoff and traceability packet for the next milestone", "--json")
    assert payload["route"] == "handoff / traceability / doc sync"
    assert "studio/docs/templates/handoff-contract.md" in payload["docs"]
    assert "docs/reference/feature-traceability.md" in payload["research_refs"]


def test_mastermind_checklist_includes_mastermind_and_support_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["mastermind"], milestone="prototype", agent_name="producer")
    item_ids = {item["id"] for item in items}
    assert {"mastermind-summary", "mastermind-control-loop", "mastermind-handoffs", "mastermind-validation", "mastermind-doc-sync"}.issubset(item_ids)
    assert {"research-primary-sources", "quality-owner", "quality-process"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/mastermind.toml") for item in items)


def test_agents_checklist_includes_role_matrix_controls() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["agents"], milestone="prototype", agent_name="mastermind")
    item_ids = {item["id"] for item in items}
    assert {"agent-mode-picked", "agent-role-owned", "agent-handoffs", "agent-validation", "agent-doc-sync"}.issubset(item_ids)
    assert {"research-primary-sources", "quality-owner", "quality-process"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/agents.toml") for item in items)


def test_agent_validation_checklist_includes_validation_matrix_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["agent_validation"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {"agent-validation-scope", "agent-validation-rows", "agent-validation-history", "agent-validation-models", "agent-validation-doc-sync"}.issubset(item_ids)
    assert {"mastermind-summary", "agent-mode-picked", "hierarchy-single-specialist", "journal-prompt-history", "transcript-assignment", "quality-owner", "benchmark-family", "openai-controller-policy", "openai-model-choice-explicit"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/agent_validation.toml") for item in items)


def test_role_checklists_include_role_specific_layers() -> None:
    cases = {
        "producer": {"producer-summary", "producer-scope", "producer-handoffs", "producer-risk"},
        "technical_director": {"tech-boundary", "tech-feasibility", "tech-tradeoff", "tech-validation"},
        "qa_lead": {"qa-criteria", "qa-matrix", "qa-go-no-go", "qa-evidence"},
        "release_manager": {"release-freeze", "release-artifacts", "release-rollback", "release-note"},
        "build_release_engineer": {"build-deterministic", "build-env", "build-artifacts", "build-smoke"},
        "docs_researcher": {"research-primary", "research-claims", "research-note", "research-implication"},
        "performance_analyst": {"perf-baseline", "perf-budget", "perf-first-lever", "perf-fallback"},
        "engine_programmer": {"engine-owner", "engine-toolchain", "engine-class", "engine-smoke"},
        "gameplay_programmer": {"gameplay-owner", "gameplay-slice", "gameplay-state", "gameplay-validation"},
        "game_designer": {"design-outcome", "design-loop", "design-pacing", "design-validation"},
        "ui_programmer": {"ui-screen-flow", "ui-projection", "ui-accessibility", "ui-validation"},
        "narrative_director": {"narrative-beat", "narrative-branch", "narrative-graph", "narrative-validation"},
        "art_director": {"art-pillars", "art-readability", "art-pipeline", "art-validation"},
        "audio_director": {"audio-pillars", "audio-mix", "audio-implementation", "audio-validation"},
    }
    for role, expected in cases.items():
        items = resolve_checklists(engine_slug="unity-6", disciplines=[role], milestone="prototype", agent_name=role)
        item_ids = {item["id"] for item in items}
        assert expected.issubset(item_ids), role
        assert any(item["source"].endswith(f"studio/checklists/discipline/{role}.toml") for item in items), role


def test_openai_codex_checklist_includes_controller_and_eval_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["openai_codex"], milestone="prototype", agent_name="mastermind")
    item_ids = {item["id"] for item in items}
    assert {"openai-controller-policy", "openai-prompt-version", "openai-tool-access", "openai-eval-path", "openai-single-specialist", "openai-doc-sync"}.issubset(item_ids)
    assert {"mastermind-summary", "mastermind-control-loop", "agent-mode-picked", "hierarchy-single-specialist", "journal-prompt-history", "quality-owner", "benchmark-family"}.issubset(item_ids)
    assert "research-primary-sources" in item_ids
    assert any(item["source"].endswith("studio/checklists/discipline/openai_codex.toml") for item in items)


def test_openai_models_checklist_includes_model_selection_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["openai_models"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {"openai-model-choice-explicit", "openai-smallest-model-first", "openai-hard-problems-pay-for-pro", "openai-plan-vs-api", "openai-compatibility-only", "openai-model-doc-sync"}.issubset(item_ids)
    assert {"openai-controller-policy", "openai-prompt-version", "openai-tool-access", "openai-eval-path", "openai-single-specialist", "openai-doc-sync"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/openai_models.toml") for item in items)


def test_architecture_tasks_surface_architecture_research() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Design a boss phase authority model with state graph and projection boundaries",
        "--json",
    )
    assert payload["route"] == "architecture / systems design"
    assert "docs/reference/architecture-guide.md" in payload["docs"]
    assert "docs/examples/architecture-example.md" in payload["docs"]
    assert "docs/research/game-development/architecture/README.md" in payload["research_refs"]
    assert "docs/research/game-development/architecture/authority.md" in payload["research_refs"]
    assert "docs/research/game-development/architecture/events.md" in payload["research_refs"]


def test_architecture_checklist_includes_architecture_and_research_layers() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Design a boss phase authority model with state graph and projection boundaries",
        "--json",
    )
    assert "architecture" in payload["disciplines"]
    assert "quality" in payload["disciplines"]
    assert "research" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"architecture-owner", "architecture-boundary", "architecture-validation"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/architecture.toml") for item in payload["items"])
    assert "docs/reference/architecture-guide.md" in payload["research_refs"]
    assert "docs/examples/architecture-example.md" in payload["research_refs"]


def test_checklist_task_infers_build_release_for_packaging_work() -> None:
    payload = run_json("scripts/codex_studio.py", "checklist", "--task", "Plan the next UE5 packaging task", "--json")
    assert "build-release" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert "build-command-deterministic" in item_ids
    assert "docs/research/game-development/engines/unreal.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unreal-classes.md" in payload["research_refs"]
    assert "docs/research/game-development/production/release-validation.md" in payload["research_refs"]


def test_checklist_task_surfaces_build_release_support_for_release_readiness() -> None:
    payload = run_json("scripts/codex_studio.py", "checklist", "--task", "Prepare a release readiness bundle for the demo build", "--json")
    assert "release" in payload["disciplines"]
    assert "build-release" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert "ci-short-names" in item_ids
    assert any(item["source"].endswith("studio/checklists/discipline/build-release.toml") for item in payload["items"])


def test_route_task_surfaces_release_hardening_for_protected_builds() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split",
        "--json",
    )
    assert payload["route"] == "release hardening / code protection"
    assert "docs/reference/release-hardening-guide.md" in payload["docs"]
    assert "docs/examples/release-hardening-example.md" in payload["docs"]
    assert "docs/research/game-development/production/release-hardening.md" in payload["docs"]
    assert "studio/docs/templates/release-hardening.md" in payload["docs"]
    assert "docs/reference/ci-cd.md" in payload["docs"]
    assert "docs/research/game-development/production/release-validation.md" in payload["docs"]
    assert "docs/reference/release-hardening-guide.md" in payload["research_refs"]
    assert "docs/examples/release-hardening-example.md" in payload["research_refs"]
    assert "docs/research/game-development/production/release-hardening.md" in payload["research_refs"]
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {
        "hardening-owner",
        "hardening-build-integrity",
        "hardening-code-protection",
        "hardening-symbol-policy",
        "hardening-trust-boundary",
        "hardening-server-split",
        "hardening-smoke",
        "hardening-doc-sync",
        "build-command-deterministic",
        "release-freeze",
        "version-source",
        "quality-owner",
        "platform-source-hierarchy",
    }.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/release_hardening.toml") for item in payload["checklists"])


def test_codex_studio_checklist_surfaces_release_hardening_for_multiplayer_builds() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split",
        "--json",
    )
    assert "release_hardening" in payload["disciplines"]
    assert "release" in payload["disciplines"]
    assert "build-release" in payload["disciplines"]
    assert "versioning" in payload["disciplines"]
    assert "quality" in payload["disciplines"]
    assert "platform_compatibility" in payload["disciplines"]
    assert "backend" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {
        "hardening-owner",
        "hardening-build-integrity",
        "hardening-code-protection",
        "hardening-symbol-policy",
        "hardening-trust-boundary",
        "hardening-server-split",
        "hardening-smoke",
        "hardening-doc-sync",
        "build-command-deterministic",
        "release-freeze",
        "version-source",
        "quality-owner",
        "platform-source-hierarchy",
    }.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/release_hardening.toml") for item in payload["items"])


def test_codex_studio_checklist_surfaces_versioning_commit_notes_for_version_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Prepare commit notes for a version bump and keep VERSION, CHANGELOG.md, and release tags aligned",
        "--json",
    )
    assert "versioning" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"version-source", "version-changelog", "version-commit"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/versioning.toml") for item in payload["items"])


def test_route_task_surfaces_versioning_guidance_for_commit_note_tasks() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Write commit notes for a version bump and keep VERSION, CHANGELOG.md, and release tags aligned",
        "--json",
    )
    assert payload["route"] == "versioning / release metadata"
    item_ids = {item["id"] for item in payload["checklists"]}
    assert {"version-source", "version-changelog", "version-commit"}.issubset(item_ids)
    assert "docs/reference/version-guide.md" in payload["docs"]
    assert "docs/examples/version-example.md" in payload["docs"]


def test_codex_studio_checklist_surfaces_mastermind_guidance_for_broad_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs",
        "--json",
    )
    assert "mastermind" in payload["disciplines"]
    assert "research" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"mastermind-summary", "mastermind-control-loop", "mastermind-handoffs", "mastermind-validation", "mastermind-doc-sync"}.issubset(item_ids)
    assert "docs/reference/mastermind-guide.md" in payload["research_refs"]
    assert "docs/examples/mastermind-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/mastermind.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_agent_portfolio_guidance_for_role_matrix_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode",
        "--json",
    )
    assert "agents" in payload["disciplines"]
    assert "mastermind" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"agent-mode-picked", "agent-role-owned", "agent-handoffs", "agent-validation", "agent-doc-sync"}.issubset(item_ids)
    assert "docs/reference/agent-portfolio.md" in payload["research_refs"]
    assert "docs/examples/agent-portfolio-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/agent-portfolio.md" in payload["research_refs"]


def test_codex_studio_next_allows_agent_model_overrides() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "next",
        "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode",
        "--agent-model",
        "producer=gpt-5.4-pro",
        "--agent-model",
        "technical_director=gpt-5.4-mini",
        "--json",
    )
    assert payload["route"] == "agent portfolio / role matrix"
    assert payload["agent_model_overrides"] == {"producer": "gpt-5.4-pro", "technical_director": "gpt-5.4-mini"}
    models = {item["agent"]: item for item in payload["agent_models"]}
    assert models["producer"]["model"] == "gpt-5.4-pro"
    assert models["technical_director"]["model"] == "gpt-5.4-mini"
    assert models["docs_researcher"]["source"] == "profile"


def test_codex_studio_checklist_surfaces_agent_hierarchy_guidance_for_command_tree_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane, but keep the single specialist option available if the scope shrinks",
        "--json",
    )
    assert "hierarchy" in payload["disciplines"]
    assert "agents" in payload["disciplines"]
    assert "mastermind" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"hierarchy-single-specialist", "hierarchy-title-picked", "hierarchy-command-tree", "hierarchy-async-packet", "hierarchy-doc-sync"}.issubset(item_ids)
    assert "docs/reference/agent-hierarchy.md" in payload["research_refs"]
    assert "docs/examples/agent-hierarchy-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/agent-hierarchy.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_agent_validation_guidance_for_validation_matrix_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Build validation matrices for operating mode, proof rows, transcript history, and model overrides while keeping single specialist fallback visible",
        "--json",
    )
    assert "agent_validation" in payload["disciplines"]
    assert {"agents", "mastermind", "hierarchy", "quality", "benchmark", "journal", "transcript", "openai_codex", "openai_models"}.issubset(set(payload["disciplines"]))
    item_ids = {item["id"] for item in payload["items"]}
    assert {"agent-validation-scope", "agent-validation-rows", "agent-validation-history", "agent-validation-models", "agent-validation-doc-sync"}.issubset(item_ids)
    assert "docs/reference/agent-validation-matrix.md" in payload["research_refs"]
    assert "docs/examples/agent-validation-matrix-example.md" in payload["research_refs"]
    assert "docs/research/game-development/foundations/agent-validation-matrix.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_openai_codex_guidance_for_agent_platform_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals",
        "--json",
    )
    assert "openai_codex" in payload["disciplines"]
    assert "mastermind" in payload["disciplines"]
    assert "agents" in payload["disciplines"]
    assert "hierarchy" in payload["disciplines"]
    assert "journal" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"openai-controller-policy", "openai-prompt-version", "openai-tool-access", "openai-eval-path", "openai-single-specialist", "openai-doc-sync"}.issubset(item_ids)
    assert {"mastermind-summary", "mastermind-control-loop", "agent-mode-picked", "hierarchy-single-specialist", "journal-prompt-history"}.issubset(item_ids)
    assert "docs/research/openai-codex-infra-findings.md" in payload["research_refs"]
    assert "docs/reference/codex-compatibility.md" in payload["research_refs"]
    assert "docs/reference/agent-system.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_role_pack_guidance_for_role_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Prepare a producer scope and handoff packet for the next milestone",
        "--json",
    )
    assert "producer" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"producer-summary", "producer-scope", "producer-handoffs", "producer-risk"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/producer.toml") for item in payload["items"])

    qa_payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Draft a QA lead validation plan for the release gate",
        "--json",
    )
    assert "qa_lead" in qa_payload["disciplines"]
    qa_item_ids = {item["id"] for item in qa_payload["items"]}
    assert {"qa-criteria", "qa-matrix", "qa-go-no-go", "qa-evidence"}.issubset(qa_item_ids)


def test_library_tasks_surface_library_selection_research() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Choose the smallest official library set for a Godot 4 stealth prototype with input, navigation, and save",
        "--json",
    )
    assert "library" in payload["disciplines"]
    assert "research" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"library-owner", "library-version-pin", "library-validation"}.issubset(item_ids)
    assert "research-primary-sources" in item_ids
    assert "docs/reference/library-guide.md" in payload["research_refs"]
    assert "docs/examples/library-example.md" in payload["research_refs"]


def test_library_checklist_includes_library_and_research_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["library"], milestone="prototype", agent_name="technical_director")
    item_ids = {item["id"] for item in items}
    assert {"library-owner", "library-version-pin", "library-validation"}.issubset(item_ids)
    assert "research-primary-sources" in item_ids
    assert any(item["source"].endswith("studio/checklists/discipline/library.toml") for item in items)


def test_genre_checklist_includes_genre_and_research_layers() -> None:
    items = resolve_checklists(engine_slug="godot-4", disciplines=["genre"], milestone="prototype", agent_name="game_designer")
    item_ids = {item["id"] for item in items}
    assert {"genre-loop", "genre-plan-schema", "genre-plan-fit", "genre-pattern-fit", "genre-contrast-set", "genre-state-boundary", "genre-validation", "genre-doc-sync"}.issubset(item_ids)
    assert "research-primary-sources" in item_ids
    assert any(item["source"].endswith("studio/checklists/discipline/genre.toml") for item in items)


def test_codex_studio_checklist_surfaces_genre_plan_guidance_for_plan_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Write a genre plan schema for a tactical RPG that names the player outcome and loop ladder",
        "--json",
    )
    assert "genre" in payload["disciplines"]
    assert "research" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"genre-loop", "genre-plan-schema", "genre-plan-fit", "genre-pattern-fit", "genre-contrast-set", "genre-state-boundary", "genre-validation", "genre-doc-sync"}.issubset(item_ids)
    assert "docs/reference/genre-plan.md" in payload["research_refs"]
    assert "docs/examples/genre-plan-example.md" in payload["research_refs"]
    assert "docs/examples/genre-gallery-example.md" in payload["research_refs"]
    assert "docs/research/game-development/genre/genre-plan.md" in payload["research_refs"]


def test_codex_studio_checklist_surfaces_genre_pattern_guidance_for_genre_tasks() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Research genre software patterns and contrast sets for a grand-strategy support pass",
        "--json",
    )
    assert "genre" in payload["disciplines"]
    assert "research" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"genre-loop", "genre-pattern-fit", "genre-contrast-set", "genre-state-boundary", "genre-validation", "genre-doc-sync"}.issubset(item_ids)
    assert "docs/research/game-development/genre/genre-guide.md" in payload["research_refs"]
    assert "docs/research/game-development/genre/genre-patterns.md" in payload["research_refs"]
    assert "docs/research/game-development/genre/genre-examples.md" in payload["research_refs"]
    assert "docs/examples/genre-gallery-example.md" in payload["research_refs"]
    assert "docs/research/game-development/genre/genre-maturity.md" in payload["research_refs"]
    assert "docs/reference/genre-plan.md" in payload["research_refs"]


def test_assets_checklist_includes_assets_and_support_layers() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Decide asset ownership and import boundaries for a Unity 6 inventory HUD",
        "--json",
    )
    assert "assets" in payload["disciplines"]
    assert "content-pipeline" in payload["disciplines"]
    assert "quality" in payload["disciplines"]
    item_ids = {item["id"] for item in payload["items"]}
    assert {"assets-owner", "assets-alternative", "assets-import-boundary", "assets-validation"}.issubset(item_ids)
    assert "docs/reference/asset-guide.md" in payload["research_refs"]
    assert "docs/examples/asset-example.md" in payload["research_refs"]


def test_assets_checklist_includes_assets_and_research_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["assets"], milestone="prototype", agent_name="technical_artist")
    item_ids = {item["id"] for item in items}
    assert {"assets-owner", "assets-alternative", "assets-import-boundary", "assets-validation"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/assets.toml") for item in items)


def test_advanced_performance_checklist_includes_advanced_and_perf_layers() -> None:
    items = resolve_checklists(engine_slug="unity-6", disciplines=["advanced_performance"], milestone="prototype", agent_name="performance_analyst")
    item_ids = {item["id"] for item in items}
    assert {"advanced-perf-owner", "advanced-perf-baseline", "perf-first-lever"}.issubset(item_ids)
    assert any(item["source"].endswith("studio/checklists/discipline/advanced_performance.toml") for item in items)


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


def test_doc_sync_audit_and_balance_simulator_surface() -> None:
    doc_sync_payload = run_json(
        "scripts/doc_sync_audit.py",
        "scripts/route_task.py",
        "studio/presets/genre/metroidvania.md",
        "--json",
    )
    suggested_docs = {item["doc"] for item in doc_sync_payload["recommendations"]}
    assert "docs/reference/ci-cd.md" in suggested_docs
    assert "docs/reference/genre-presets.md" in suggested_docs

    balance_payload = run_json(
        "scripts/balance_simulator.py",
        "--runs",
        "1000",
        "--success-rate",
        "0.55",
        "--reward-win",
        "18",
        "--reward-loss",
        "7",
        "--upgrade-cost",
        "90",
        "--seed",
        "42",
        "--json",
    )
    assert balance_payload["runs"] == 1000
    assert balance_payload["average_runs_to_afford"] >= 1


def test_agent_metadata_validator_passes() -> None:
    payload = run_json("scripts/validate_agent_metadata.py", "--json")
    assert payload == {"errors": []}


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
    assert "docs/research/game-development/systems/save.md" in payload["research_refs"]


def test_inventory_tasks_surface_inventory_and_save_research() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Design inventory and equipment persistence boundaries for the player loadout",
        "--json",
    )
    assert "gameplay" in payload["disciplines"]
    assert "save" in payload["disciplines"]
    assert "docs/research/game-development/systems/inventory.md" in payload["research_refs"]
    assert "docs/research/game-development/systems/save.md" in payload["research_refs"]


def test_character_tasks_surface_character_architecture_research() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Design the player character locomotion and ability ownership model for Unity",
        "--json",
    )
    assert payload["route"] == "combat / gameplay"
    assert "docs/research/game-development/systems/character.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unity-classes.md" in payload["research_refs"]


def test_enemy_tasks_surface_enemy_architecture_research() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Design enemy patrol, aggro, and encounter behavior for Unreal",
        "--json",
    )
    assert payload["route"] == "combat / gameplay"
    assert "docs/research/game-development/systems/enemy.md" in payload["research_refs"]
    assert "docs/research/game-development/engines/unreal-performance.md" in payload["research_refs"]


def test_route_task_surfaces_academic_foundations_for_ai_and_flow() -> None:
    ai_payload = run_json(
        "scripts/route_task.py",
        "Compare A* and behavior tree tradeoffs for enemy decision architecture",
        "--json",
    )
    assert "docs/research/game-development/foundations/ai.md" in ai_payload["research_refs"]

    flow_payload = run_json(
        "scripts/route_task.py",
        "Research motivation and flow goals for the core loop",
        "--json",
    )
    assert "docs/research/game-development/foundations/frameworks.md" in flow_payload["research_refs"]


def test_controls_tasks_surface_control_and_ui_research() -> None:
    payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Design controller remapping and pause flow for keyboard and gamepad parity",
        "--json",
    )
    assert "ui-ux" in payload["disciplines"]
    assert "docs/research/game-development/systems/input.md" in payload["research_refs"]
    assert "docs/research/game-development/systems/ui.md" in payload["research_refs"]


def test_checklist_surfaces_accessibility_and_difficulty_foundations() -> None:
    accessibility_payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Improve game feel, readability, and accessibility for combat feedback",
        "--json",
    )
    assert "docs/research/game-development/foundations/ux.md" in accessibility_payload["research_refs"]

    difficulty_payload = run_json(
        "scripts/codex_studio.py",
        "checklist",
        "--task",
        "Tune difficulty pacing and evaluate dynamic difficulty adaptation",
        "--json",
    )
    assert "docs/research/game-development/foundations/balance.md" in difficulty_payload["research_refs"]


def test_upgrade_tasks_surface_ability_upgrade_research() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Separate authored skill definitions, current-run upgrades, and durable meta unlocks",
        "--json",
    )
    assert payload["route"] == "combat / gameplay"
    assert "docs/research/game-development/systems/skills.md" in payload["research_refs"]
    assert "docs/research/game-development/systems/save.md" in payload["research_refs"]


def test_interaction_tasks_surface_interaction_research() -> None:
    payload = run_json(
        "scripts/route_task.py",
        "Design pickup prompts, interaction validation, and loot persistence for reward chests",
        "--json",
    )
    assert payload["route"] == "combat / gameplay"
    assert "docs/research/game-development/systems/interactions.md" in payload["research_refs"]
    assert "docs/research/game-development/systems/inventory.md" in payload["research_refs"]


def test_detect_engine_prefers_configured_engine_over_root_file_clues(tmp_path: Path) -> None:
    (tmp_path / "studio.toml").write_text('[project]\nprimary_engine = "unreal-5"\n', encoding="utf-8")
    (tmp_path / "project.godot").write_text("; clue only\n", encoding="utf-8")
    assert detect_engine(tmp_path) == "unreal"


def test_research_notes_seeded() -> None:
    notes = research_notes()
    assert notes
    assert (REPO_ROOT / "docs/research/game-development/engines/README.md").exists()
    assert any(path.name == "engine-eval.md" for path in notes)
    assert any(path.name == "authority.md" for path in notes)
    assert any(path.name == "events.md" for path in notes)
    assert any(path.name == "state.md" for path in notes)
    assert any(path.name == "projection.md" for path in notes)
    assert any(path.name == "genre-patterns.md" for path in notes)
    assert any(path.name == "genre-examples.md" for path in notes)
    assert any(path.name == "genre-maturity.md" for path in notes)
    assert any(path.name == "genre-plan.md" for path in notes)
    assert any(path.name == "lorebook.md" for path in notes)
    assert any(path.name == "world-graph.md" for path in notes)
    assert any(str(path).endswith("assets/alternatives.md") for path in notes)
    assert any(str(path).endswith("assets/ownership.md") for path in notes)
    assert any(str(path).endswith("assets/import.md") for path in notes)
    assert any(path.name == "godot.md" for path in notes)
    assert any(path.name == "godot-map.md" for path in notes)
    assert any(path.name == "godot-classes.md" for path in notes)
    assert any(path.name == "godot-performance.md" for path in notes)
    assert any(path.name == "loop.md" for path in notes)
    assert any(path.name == "combat.md" for path in notes)
    assert any(path.name == "navigation.md" for path in notes)
    assert any(path.name == "save.md" for path in notes)
    assert any(path.name == "inventory.md" for path in notes)
    assert any(path.name == "character.md" for path in notes)
    assert any(path.name == "enemy.md" for path in notes)
    assert any(path.name == "input.md" for path in notes)
    assert any(path.name == "ui.md" for path in notes)
    assert any(path.name == "skills.md" for path in notes)
    assert any(path.name == "interactions.md" for path in notes)
    assert any(path.name == "unity-map.md" for path in notes)
    assert any(path.name == "unity-classes.md" for path in notes)
    assert any(path.name == "unity-performance.md" for path in notes)
    assert any(path.name == "unreal-map.md" for path in notes)
    assert any(path.name == "unreal-classes.md" for path in notes)
    assert any(path.name == "unreal-performance.md" for path in notes)
    assert any(path.name == "frameworks.md" for path in notes)
    assert any(path.name == "ux.md" for path in notes)
    assert any(path.name == "ai.md" for path in notes)
    assert any(path.name == "balance.md" for path in notes)
    assert any(path.name == "gpu.md" for path in notes)
    assert any(path.name == "godot-gpu.md" for path in notes)
    assert any(path.name == "unity-gpu.md" for path in notes)
    assert any(path.name == "unreal-gpu.md" for path in notes)
    assert any(path.name == "mastermind.md" for path in notes)
    assert any(path.name == "agent-portfolio.md" for path in notes)
