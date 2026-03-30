# Godot Classes

## Date
- 2026-03-27

## Summary
- Godot's most-used gameplay primitives are scene-tree primitives. In practice, most feature choices start with whether the responsibility belongs in a `Node2D`, `Node3D`, `CharacterBody`, `Area`, `RigidBody`, `Camera`, `AnimationTree`, or a reusable `Resource`.
- The safest mechanic design path in Godot is to keep authored hierarchy, shared data, and editor tooling separate. The engine is flexible enough to blur those boundaries, but repo guidance should resist that unless there is a clear gain.
- GDScript and Godot scene authoring both reward explicit ownership. A feature is easier to scale when the repo can answer three questions quickly:
  - which node owns the behavior
  - which resource owns the tuning
  - which scene owns the reusable hierarchy

## Primary sources
- [GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html)
- [Node2D](https://docs.godotengine.org/en/stable/classes/class_node2d.html)
- [Node3D](https://docs.godotengine.org/en/stable/classes/class_node3d.html)
- [CharacterBody2D](https://docs.godotengine.org/en/stable/classes/class_characterbody2d.html)
- [CharacterBody3D](https://docs.godotengine.org/en/stable/classes/class_characterbody3d.html)
- [Area2D](https://docs.godotengine.org/en/stable/classes/class_area2d.html)
- [Area3D](https://docs.godotengine.org/en/stable/classes/class_area3d.html)
- [RigidBody2D](https://docs.godotengine.org/en/stable/classes/class_rigidbody2d.html)
- [RigidBody3D](https://docs.godotengine.org/en/stable/classes/class_rigidbody3d.html)
- [Camera2D](https://docs.godotengine.org/en/stable/classes/class_camera2d.html)
- [Camera3D](https://docs.godotengine.org/en/stable/classes/class_camera3d.html)
- [AnimationTree](https://docs.godotengine.org/en/stable/classes/class_animationtree.html)
- [TileMap](https://docs.godotengine.org/en/stable/classes/class_tilemap.html)
- [GridMap](https://docs.godotengine.org/en/stable/classes/class_gridmap.html)

## Why this matters to this repo
- Godot tasks in this repo should not jump straight from "new mechanic" to "new script." The more durable question is which built-in node or resource should own the mechanic.
- Agent guidance needs a shared answer for common mechanic primitives such as player movement, trigger volumes, spawned hazards, camera rigs, animation state, and reusable tuning data.
- Repo users need a practical map for 2D and 3D work that is more concrete than the architecture note and less performance-heavy than the navigation/damage/performance note.

## Decision impact
- Godot engine-specific recommendations should cite this guide when choosing between `CharacterBody`, `Area`, `RigidBody`, `Camera`, `AnimationTree`, and `Resource` ownership.
- Feature briefs and mechanic docs should explicitly name the node and resource layer used by the mechanic.
- Checklists and agent outputs should treat 2D/3D primitive choice as a first-class design decision, not an implementation afterthought.

## 2D building blocks

### `Node2D`
- Purpose: generic spatial 2D parent for transforms, hierarchy, and authored placement.
- Use it for: lightweight transform roots, markers, spawn points, grouping nodes, and presentation-only helpers.
- Watch out for: putting motion, collision, authored data, and combat logic into a generic `Node2D` when a more specific body or area type should own the feature.

### `CharacterBody2D`
- Purpose: kinematic-style controlled character movement in 2D.
- Use it for: player avatars, enemies with authored locomotion, dash systems, and intentional ground/air motion.
- Watch out for: mixing it with rigid-body expectations; it is usually the right choice for authored combat movement, not for fully simulated physics toys.

### `Area2D`
- Purpose: overlap-driven detection and space influence in 2D.
- Use it for: hitboxes, hurtboxes, pickups, trigger zones, proximity prompts, interaction volumes, and authored damage rings.
- Watch out for: overloading one `Area2D` to mean both sensing and damage if the mechanic becomes hard to read; use separate areas or clear signal ownership.

### `RigidBody2D`
- Purpose: physics-driven body in 2D.
- Use it for: objects that should be simulated by the physics engine, such as knockable props, rolling hazards, or physics puzzles.
- Watch out for: forcing precise player or enemy control through a rigid body when a `CharacterBody2D` would be simpler and more stable.

### `Camera2D`
- Purpose: authored 2D camera framing and follow behavior.
- Use it for: player follow, room framing, smoothing, screen limits, and simple juice such as camera shake helpers.
- Watch out for: burying game-state logic into the camera node; the camera should react to state more often than own it.

### `TileMap`
- Purpose: grid-authored 2D level content.
- Use it for: board layouts, collision-backed tile worlds, and dense hand-authored 2D environments.
- Watch out for: turning tile data into the only gameplay authority if the mechanic needs richer authored objects, metadata, or runtime state.

## 3D building blocks

### `Node3D`
- Purpose: generic spatial 3D parent for transforms and hierarchy.
- Use it for: locators, sockets, simple grouping nodes, and presentation roots.
- Watch out for: hiding gameplay responsibility in a generic 3D node when the repo should be explicit about player body, trigger, or data ownership.

### `CharacterBody3D`
- Purpose: controlled 3D locomotion with authored movement.
- Use it for: player characters, AI movers, dodge systems, mantling prototypes, and controller-friendly combat movement.
- Watch out for: blending hand-authored movement with raw rigid-body expectations without a clear contract for slopes, grounding, and step handling.

### `Area3D`
- Purpose: overlap-driven detection and zone logic in 3D.
- Use it for: melee ranges, interaction zones, aggro checks, pickup volumes, and hazard regions.
- Watch out for: vague collision layers and masks; 3D projects get messy faster when area filtering is not explicit.

### `RigidBody3D`
- Purpose: fully simulated 3D body.
- Use it for: props, dynamic hazards, vehicles or physical toys, and situations where force response matters more than authored locomotion.
- Watch out for: using it as the default character base because it feels more "physical." In most action games it complicates control and tuning.

### `Camera3D`
- Purpose: 3D viewpoint ownership.
- Use it for: player follow cameras, orbit cameras, room cameras, and authored perspective control.
- Watch out for: tying input, targeting, and camera rig math together in one script when a small rig hierarchy would be clearer.

### `GridMap`
- Purpose: grid-authored 3D environments.
- Use it for: blockout-like 3D spaces, modular grid-heavy levels, and experiments that benefit from snap-aligned assembly.
- Watch out for: keeping it too long once the level needs richer metadata, traversal markup, or non-grid interaction rules.

## Common mechanic patterns

### Player movement
- 2D default: `CharacterBody2D` plus clear movement state owned in one script.
- 3D default: `CharacterBody3D` with explicit input-to-motion flow and a small camera rig.
- Prefer this when: the mechanic should feel authored, responsive, and designer-tunable.
- Escalate away when: the mechanic is truly physics-first.

### Contact and damage
- Use `Area2D` / `Area3D` for readable authored hitboxes, hurtboxes, pickups, and hazard zones.
- Use body collisions when physical blocking and impact ownership really belong to the same surface.
- Use direct space-state queries when the mechanic is query-heavy, frame-specific, or should not depend on scene callbacks alone.
- Watch out for: mixing all three contact models in one feature without documenting which one is authoritative.

### Camera rigs
- 2D: prefer `Camera2D` plus limit/smoothing configuration and a separate event source for shake.
- 3D: prefer a small rig tree such as pivot -> spring/offset helper -> `Camera3D`.
- Watch out for: camera scripts that also own combat target selection, pause flow, or UI behavior.

### Animation and state
- Use `AnimationTree` when the feature needs structured state blending or parameter-driven animation control.
- Keep animation state as a presentation partner to gameplay state, not the single source of truth for damage, invulnerability, or room progression.
- Watch out for: gameplay rules hidden only inside animation callbacks.

### Spawnable authored content
- Prefer separate `.tscn` scenes for repeated runtime hierarchies such as projectiles, enemies, interactables, and VFX carriers.
- Prefer `Resource` assets for shared tuning such as enemy archetypes, mechanic stats, and reusable authored parameters.
- Watch out for: duplicating exported values across many scene instances when the data is really shared.

## Writing style and naming

### Engine-native style
- Follow the GDScript style guide for script structure and naming.
- Practical repo rule:
  - `PascalCase` for engine classes and named types
  - `snake_case` for functions, variables, and file names
  - `SCREAMING_SNAKE_CASE` for constants
- Keep exported tuning values grouped near the top of the script and runtime-only caches lower down.

### Scene and script ownership style
- Prefer one clear runtime responsibility per script.
- Prefer short node-path assumptions and explicit child names over deep, fragile `$A/B/C/D` chains.
- When a scene is reusable, give it its own `.tscn` rather than hiding a spawn hierarchy inside a parent scene script.

### Editor-facing style
- Only introduce `@tool` when live editor behavior is truly part of the feature.
- If a designer should tune data in many places, prefer a `Resource` asset over copying exported values scene by scene.

## What to watch out for
- Overusing generic `Node2D` or `Node3D` where a more specific body, area, or data asset would make the feature clearer.
- Letting signal wiring become the only way to understand mechanic flow; major contact rules should also be documented in the feature note.
- Putting shared tuning into scene instances instead of `Resource` assets.
- Driving game authority from animation alone.
- Using rigid bodies for authored player control just because the mechanic includes impacts or knockback.

## Additional structural families

### `StaticBody2D` and `StaticBody3D`
- Purpose: immovable collision surfaces.
- Use it for: walls, floors, blockers, world geometry, and authored collision that should not simulate.
- Watch out for: using a static body when the object should actually move or respond physically.

### `TileMap` and `TileMapLayer`
- Purpose: tile-authored world structure.
- Use it for: grid rooms, terrain, dungeon layouts, and dense authored level data.
- Watch out for: treating tile data as the only gameplay authority when richer object state is needed.

### `Timer`
- Purpose: lightweight delayed or repeated timing helper.
- Use it for: cooldowns, delays, spawn pacing, and simple state transitions.
- Watch out for: spreading timing state across many unrelated nodes when one timing owner would be clearer.

### `ResourceLoader` and `ResourceSaver`
- Purpose: load and save authored resources.
- Use it for: persistence plumbing, content import, and reusable data pipelines.
- Watch out for: turning load helpers into gameplay systems.

### `Viewport` and `SubViewport`
- Purpose: render and isolate drawing surfaces.
- Use it for: mini-maps, 3D-in-UI panels, separated view layers, or special render spaces.
- Watch out for: using viewports to hide unclear ownership instead of modeling the boundary explicitly.

### `AudioStreamPlayer2D` and `AudioStreamPlayer3D`
- Purpose: spatial or non-spatial audio playback.
- Use it for: one-shot feedback, ambient layers, spatial cues, and effect sounds.
- Watch out for: building gameplay logic that depends on audio nodes firing in a particular order.

### `EditorPlugin`
- Purpose: editor extension surface.
- Use it for: custom import rules, validation tools, and workflow helpers.
- Watch out for: shipping editor-only logic in runtime scenes.
