# Engine Agent Guidelines

This guide tells Codex-facing agents how to use the engine knowledge base in this repo before making engine-specific recommendations or patches.

## Required read order

When a task is engine-specific, the agent should read in this order:

1. `studio/docs/active/engine-profile.md`
2. The engine architecture baseline in `docs/research/game-development/engines/`
3. The matching engine class/editor/object map in `docs/research/game-development/engines/`
4. The matching 2D/3D class and mechanic guide in `docs/research/game-development/engines/`
5. The matching 2D/3D, navigation, damage, and performance note in `docs/research/game-development/engines/`
6. The matching systems playbook in `docs/research/game-development/engines/`
7. The matching visuals, images, and animation playbook in `docs/research/game-development/engines/`
8. The matching engine checklist in `studio/checklists/engine/`
9. The relevant active docs such as `build-pipeline.md`, `current-sprint.md`, or `content-pipeline.md`

When a task is system-specific, add the matching systems note before implementation:

- inventory, loot, equipment, quick bar, or loadout -> `docs/research/game-development/systems/inventory-equipment-and-item-architecture.md`
- avatar, player controller, locomotion, dash, jump, or ability boundary -> `docs/research/game-development/systems/character-controller-ability-and-state-architecture.md`
- enemy, boss, patrol, aggro, perception, or encounter behavior -> `docs/research/game-development/systems/enemy-roster-behavior-and-encounter-architecture.md`
- input, controller support, remapping, pause, or camera -> `docs/research/game-development/systems/input-controls-camera-and-remapping-architecture.md`
- HUD, menu, settings, pause flow, inventory screen, or onboarding UI -> `docs/research/game-development/systems/ui-hud-menu-and-screen-flow-architecture.md`
- abilities, upgrades, perks, skill trees, cooldowns, or build variety -> `docs/research/game-development/systems/abilities-skill-trees-upgrades-and-build-architecture.md`
- interactables, pickups, prompts, levers, chests, or world objects -> `docs/research/game-development/systems/interactions-pickups-and-world-object-architecture.md`
- persistence or progression interaction -> `docs/research/game-development/systems/save-progression-and-runtime-data-architecture.md`

## Engine-specific knowledge index

### Godot 4
- Architecture: `docs/research/game-development/engines/godot-4-architecture.md`
- Class/editor/object map: `docs/research/game-development/engines/godot-4-class-editor-object-map.md`
- Common classes/mechanics: `docs/research/game-development/engines/godot-4-2d-3d-class-and-mechanic-guide.md`
- Systems/performance: `docs/research/game-development/engines/godot-4-2d-3d-navigation-damage-performance.md`
- Visuals/animation: `docs/research/game-development/engines/godot-4-visuals-animation-playbook.md`
- Checklist: `studio/checklists/engine/godot-4.toml`

### Unity 6
- Architecture: `docs/research/game-development/engines/unity-6-architecture.md`
- Class/editor/object map: `docs/research/game-development/engines/unity-6-class-editor-object-map.md`
- Common classes/mechanics: `docs/research/game-development/engines/unity-6-2d-3d-class-and-mechanic-guide.md`
- Systems/performance: `docs/research/game-development/engines/unity-6-2d-3d-navigation-damage-performance.md`
- Visuals/animation: `docs/research/game-development/engines/unity-6-visuals-animation-playbook.md`
- Checklist: `studio/checklists/engine/unity-6.toml`

### Unreal 5
- Architecture: `docs/research/game-development/engines/unreal-5-architecture.md`
- Class/editor/object map: `docs/research/game-development/engines/unreal-5-class-editor-object-map.md`
- Common classes/mechanics: `docs/research/game-development/engines/unreal-5-2d-3d-class-and-mechanic-guide.md`
- Systems/performance: `docs/research/game-development/engines/unreal-5-2d-3d-navigation-damage-performance.md`
- Visuals/animation: `docs/research/game-development/engines/unreal-5-visuals-animation-playbook.md`
- Checklist: `studio/checklists/engine/unreal-5.toml`

## Shared rules for all engine-specialized agents

- Do not start from generic engine memory when the repo has a matching research note. Read the repo note first.
- State the ownership model before implementation:
  - what is the runtime unit
  - what is the reusable data unit
  - what is the editor-facing unit
  - what is the validation loop
- For system-heavy gameplay work, also state:
  - what world stack is in charge: `2D`, `3D`, or limited hybrid
  - which engine-native classes or object families own movement, contact, camera, animation, and authored data
  - what navigation model is in charge: native navmesh/server stack versus explicit graph/grid
  - what damage/contact model is in charge: overlaps, collision callbacks, direct queries, or ability/effect framework
  - what scale lever is in charge: ordinary authored objects versus instancing, pooling, servers, DOTS, or Mass
- For controls, UI, inventory, abilities, and save work, also state:
  - what input owner is in charge: engine action maps, input assets, or a bespoke remap layer
  - what UI owner is in charge: HUD widgets, menu screens, editor windows, or overlay canvases
  - what authored-data owner is in charge: `Resource`, `ScriptableObject`, `Data Asset`, or another shared asset type
  - what persistence owner is in charge: live object state versus save projection versus meta progression
- For inventory tasks, explicitly separate:
  - item definition data
  - runtime slot or stack state
  - equipment or loadout state
  - UI projection
  - persistence projection
- For character tasks, explicitly separate:
  - input interpretation
  - locomotion authority
  - combat or ability authority
  - animation/presentation authority
  - camera/targeting authority
  - persistence/data authority
- For enemy tasks, explicitly separate:
  - archetype data
  - sensing/perception
  - navigation or locomotion
  - decision model
  - action execution
  - encounter role
- For control tasks, explicitly separate:
  - physical device input
  - action mapping
  - gameplay consumers
  - UI consumers
  - camera response
  - remap persistence
- For UI tasks, explicitly separate:
  - screen or HUD state
  - projected gameplay data
  - focus/navigation behavior
  - blocked gameplay state
  - copy/accessibility expectations
- For visuals, image, sprite, animation, texture, or VFX tasks, explicitly separate:
  - source art or texture asset
  - world versus UI presentation
  - animation playback owner
  - particle or VFX owner
  - material or shader owner
  - runtime projection versus authored data
- For ability and upgrade tasks, explicitly separate:
  - authored definition data
  - current-run granted state
  - durable progression state
  - cooldown or charge owner
  - UI projection
- For interaction tasks, explicitly separate:
  - candidate selection
  - validation rule
  - world mutation
  - reward or inventory projection
  - persistence expectation
- Keep runtime code and editor-only code conceptually separate.
- Prefer the engine's native composition model over forcing the same pattern across all three engines.
- When a feature affects designer iteration, explain which editor surface is used and what the operator will see there.

## Godot-specific operating rules

- Inspect the scene tree before touching node paths, signals, or groups.
- Distinguish scene reuse from data reuse:
  - reusable hierarchy -> scene / `PackedScene`
  - shared authored data -> `Resource`
- For 2D/3D system work, explicitly choose between NavigationServer-driven movement and custom `AStarGrid2D` / `AStar3D` graphs.
- For hit or damage systems, say whether authored areas, collision callbacks, or direct space-state queries own contact detection.
- For high-entity counts, say when the feature should stay node-based and when it should move toward `MultiMesh` or lower-level server APIs.
- Use `@tool` only when the editor itself must react live.
- If the task is editor tooling, say whether it should be a tool script, an inspector plugin, or a dock/plugin.

## Unity-specific operating rules

- Distinguish container, behavior, and data:
  - container -> `GameObject`
  - behavior -> Component / `MonoBehaviour`
  - shared authored data -> `ScriptableObject`
- Prefer prefabs for repeated hierarchies and spawnable authored objects.
- For 2D/3D system work, explicitly choose between built-in 2D, built-in 3D, and data-oriented runtime paths.
- For nav and sensing systems, say whether AI Navigation, a custom graph/grid, or a DOTS-oriented solution is responsible.
- For damage and combat queries, say how layers, triggers/collisions, non-alloc queries, and pooling are used to avoid hidden cost.
- Keep `UnityEditor` usage inside editor-only code.
- Choose the editor surface deliberately:
  - object-specific editing -> custom `Editor`
  - workflow/tool window -> `EditorWindow`

## Unreal-specific operating rules

- Distinguish object, world entity, and reusable behavior:
  - reflected/supporting object -> `UObject`
  - placeable/spawned world thing -> `AActor`
  - reusable sub-behavior -> Component
- State whether a value should be edited in C++, Blueprint defaults, or the Details panel.
- For 2D/3D system work, explicitly choose between Paper2D, standard 3D gameplay framework, or a constrained hybrid.
- For AI and traversal, say whether navmesh, EQS, StateTree, or a justified custom graph owns the problem.
- For combat systems, say whether simple damage or the Gameplay Ability System owns attributes, abilities, and effect flow.
- For high-scale representations, say whether the feature should remain Actor-based or move toward instancing or Mass.
- Prefer PIE/SIE and Blueprint compile loops as the first validation path for gameplay/editor changes.
- Avoid hard-coded asset ownership when the task is clearly designer-facing.

## What every engine-aware recommendation should include

1. Current engine evidence from the repo
2. The chosen ownership model
3. The chosen world stack and system model for gameplay-heavy work
4. The editor surface involved, if any
5. The narrowest validation loop
6. The main risk if the change grows
