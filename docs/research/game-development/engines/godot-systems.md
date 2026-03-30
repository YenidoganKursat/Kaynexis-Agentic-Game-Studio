# Godot Systems

## Date
- 2026-03-28

## Summary
- Godot is strongest when gameplay, UI, and authored data stay split along engine-native boundaries instead of being collapsed into one scene script.
- For this repo, the practical rule is: use `InputMap` for intent, `Control`/`CanvasLayer` for UI, `Resource` for shared authored data, `AnimationTree`/`AnimationPlayer` for stateful presentation, and `SaveGame`-style serialization only after the object ownership model is explicit.
- If a feature starts growing beyond a handful of nodes, decide early whether the bottleneck is representation, contact routing, or navigation, because Godot has a clean path from regular nodes to servers, `AStarGrid2D`/`AStar3D`, and `MultiMesh`.

## Primary sources
- [InputMap](https://docs.godotengine.org/en/4.0/classes/class_inputmap.html)
- [Listening to player input](https://docs.godotengine.org/en/4.4/getting_started/step_by_step/scripting_player_input.html)
- [Control](https://docs.godotengine.org/en/4.0/classes/class_control.html)
- [CanvasLayer](https://docs.godotengine.org/en/stable/classes/class_canvaslayer.html)
- [Saving games](https://docs.godotengine.org/en/4.0/tutorials/io/saving_games.html)
- [Runtime file loading and saving](https://docs.godotengine.org/en/4.4/tutorials/io/runtime_file_loading_and_saving.html)
- [AnimationNodeStateMachinePlayback](https://docs.godotengine.org/en/4.4/classes/class_animationnodestatemachineplayback.html)

## Why this matters to this repo
- Godot tasks in this repo should distinguish gameplay intent, HUD state, authored data, and persistence state before implementation starts.
- Input remapping, UI layering, inventory projection, and save projection are common failure points if they are all left inside one controller script.
- The repo should surface a clear answer for "what belongs in a scene, what belongs in a Resource, what belongs in UI, and what belongs in save data" because that answer strongly affects iteration speed.

## Decision impact
- Use this playbook when designing control schemes, HUD flows, inventory screens, ability bars, save/load flows, or stateful animation ownership.
- Prefer explicit boundaries:
  - input intent -> `InputMap` + input callbacks
  - world presence -> `Node` / `Node2D` / `Node3D`
  - shared authored data -> `Resource`
  - UI -> `Control` / `CanvasLayer`
  - stateful animation -> `AnimationTree` / `AnimationPlayer`
  - persistence -> dedicated save objects or serialized data projections

## Input and controls
- Default owner: `InputMap` for action naming, node callbacks for reacting, `Input` singleton for per-frame polling when needed.
- Use actions for verbs such as `move`, `dash`, `interact`, `pause`, `menu_accept`, and `menu_back`.
- Keep remapping separate from gameplay so controller and keyboard support can change without rewriting core logic.
- Watch out for: reading raw keys in many scripts instead of binding to shared actions.

## UI, HUD, and menu flow
- Default owner: `Control` for widgets and `CanvasLayer` for HUD layering.
- Use `Control` for menus, pause panels, inventory windows, and settings screens because it gives focus, anchoring, and theme support.
- Use a dedicated `CanvasLayer` for HUD or overlay elements that should stay above the world.
- Watch out for: placing world logic inside UI scripts or letting UI nodes own combat state directly.

## Inventory, equipment, and authored data
- Default owner: `Resource` for item definitions, equipment templates, tuning, and shared authored data.
- Keep runtime slot state in a separate scene/controller layer, and project that state into the UI rather than making the UI the source of truth.
- If the same item definition appears across many runs or saves, keep the definition in a `Resource` and serialize only the runtime instance state.
- Watch out for: duplicating item stats across scenes or storing mutable progression directly in the authored definition asset.

## Abilities, upgrades, and build variety
- Default owner: explicit ability or upgrade scenes/scripts plus `Resource`-backed definitions.
- Use `AnimationTree` or `AnimationPlayer` for presentation, but keep cooldowns, charges, and unlock state out of the animation layer.
- Make build variety readable by separating granted state, current-run state, and durable meta state.
- Watch out for: combining unlock logic, cooldown logic, and UI badges in one controller node.

## Enemy behavior and encounter design
- Default owner: a dedicated enemy scene per archetype plus reusable data resources for tuning.
- Keep sensing, navigation, and action selection separate so an enemy can be tuned without rewriting every behavior hook.
- If encounter density grows, measure whether node-based composition is still sufficient before moving to lower-level representations.
- Watch out for: hard-coded enemy roles buried in the room controller instead of the enemy archetype itself.

## Save and progression
- Default owner: a dedicated persistence layer that collects runtime projections from gameplay objects.
- Use save data to store projections of gameplay state, not live scene hierarchies.
- Use `Resource` or structured serializable data for durable templates, then reconstruct scene state from those templates on load.
- Watch out for: directly serializing the entire active scene tree as if it were a reliable progression format.

## Performance and scale
- Default default: regular scenes and nodes.
- Escalate to `MultiMesh` or server-oriented APIs when the entity count becomes the real bottleneck.
- For pathfinding, prefer navigation regions/agents when the level is a walkable surface; use `AStarGrid2D` or `AStar3D` for board, lane, or abstract graph behavior.
- For hit detection, decide whether authored areas, body collision, or direct physics queries own the contact model before optimizing.

## Editor workflow
- Use `@tool` only when live editor feedback is necessary.
- Prefer editor plugins or custom inspectors when the operator needs a deliberate tool surface.
- Keep editor-side mutation and runtime logic conceptually separate so the repo remains recoverable when a tool script changes a scene.

## Best-fit first slice
- For a compact action slice, start with:
  - `InputMap` actions for movement, dash, interact, and pause
  - a `Control`-driven HUD and upgrade screen
  - a `Resource`-backed item or upgrade definition
  - a dedicated enemy scene with clear contact routing
  - a save projection layer that writes only durable progression

## Common mistakes to avoid
- Letting UI own gameplay authority.
- Storing mutable runtime state inside shared authored `Resource` data.
- Mixing input remap logic into many unrelated scripts.
- Treating save data as a mirror of the live scene tree.
- Scaling with more nodes before checking whether `MultiMesh` or a server API would be the real fix.
