# Engine Map

Use this page when an agent needs the fastest possible answer to:

- which engine class or object should own the feature
- which 2D or 3D stack is the right default
- which editor or authored-data surface should be used
- which example slice should be studied first

This page is intentionally denser than the other engine docs. It is the "first ten seconds" map for engine-aware agents.

## Read order

If the task is engine-specific, read in this order:

1. `studio/docs/active/engine-profile.md`
2. `docs/reference/engine-selection-guide.md`
3. `docs/reference/engine-examples.md`
4. `docs/reference/engine-fit.md` and `docs/examples/engine-fit-example.md` when the real question is developer profile, team shape, or workflow appetite across engines
5. `docs/reference/engine-eval.md` and `docs/examples/engine-eval-example.md` when the real question is build, test, performance, or toolchain readiness across engines
6. `docs/research/game-development/engines/README.md`
7. The matching `*-class-editor-object-map.md`
8. The matching `*-2d-3d-class-and-mechanic-guide.md`
9. The matching `*-systems-playbook.md`
10. `docs/reference/ui-guide.md` and the matching `*-ui.md`
11. The matching `*-presentation.md`
12. The matching `*-visuals-animation-playbook.md`
13. The matching `*-2d-3d-navigation-damage-performance.md`
14. The matching engine checklist in `studio/checklists/engine/`
15. `docs/reference/asset-guide.md` and `docs/examples/asset-example.md` when the task is about source art, imported assets, shared tuning, or loading boundaries
16. `docs/reference/architecture-guide.md` and `docs/examples/architecture-example.md` when the task is about authority, events, state graphs, or projection boundaries; use the diagrams first if the boundary is still fuzzy

## One-line ownership summary

| Engine | Runtime owner | Shared data owner | Editor owner | Best default use |
|---|---|---|---|---|
| Godot 4 | `Node`, `Node2D`, `Node3D` | `Resource` | Inspector, `@tool`, editor plugins | fast first-playable slice, scene-tree-driven work |
| Unity 6 | `GameObject` + Components | `ScriptableObject` | `Editor`, `EditorWindow`, custom inspectors | composition-heavy tools, prefab/data-driven work |
| Unreal 5 | `AActor`, `ACharacter`, `UActorComponent`, `UObject` | Data Asset / `UObject`-backed assets | Details panel, Blueprint editor, PIE/SIE | gameplay-framework-first 3D and packaging-heavy work |

## Canonical object families

### Godot 4

#### 2D
- `Node2D` for transform roots and light grouping
- `CharacterBody2D` for authored movement
- `Area2D` for hitboxes, pickups, triggers, and sensing
- `Camera2D` for framing and follow
- `AnimationTree` and `AnimatedSprite2D` for stateful presentation
- `TileMap` for grid-authored 2D worlds
- `Resource` for shared authored data

#### 3D
- `Node3D` for transform roots and presentation grouping
- `CharacterBody3D` for authored locomotion
- `Area3D` for overlap logic
- `Camera3D` for viewpoint control
- `RigidBody3D` for physically simulated objects
- `GridMap` for grid-authored 3D blockout
- `MultiMesh` when repeated visuals become the real scale bottleneck

#### Use first when
- the project needs a scene-tree-first runtime
- the mechanic is readable in compact slices
- the feature needs explicit scene/resource separation

#### Fast example slice
- one room, one enemy role, one upgrade choice, one clear win state

#### Agent prompt style
- name the node owner
- name the resource owner
- name the scene owner
- name the validation command

### Unity 6

#### 2D
- `GameObject` for hierarchy and identity
- `MonoBehaviour` for scene-bound behavior
- `Rigidbody2D` and `Collider2D` for physics/contact
- `Animator` for presentation state
- `ScriptableObject` for shared authored data
- `Prefab` for reusable hierarchies

#### 3D
- `GameObject` for scene identity
- `MonoBehaviour` for behavior
- `Rigidbody` or `CharacterController` for locomotion depending on control style
- `Collider` and trigger colliders for contact
- `Animator` for presentation state
- `ScriptableObject` for shared data
- `ObjectPool<T>` when spawn churn matters

#### Use first when
- the project benefits from prefab composition and editor tooling
- the mechanic should be tuned through shared data assets
- the team expects editor-driven iteration and validation

#### Fast example slice
- a room-based prototype with prefab enemies, `ScriptableObject` upgrades, and a UI layer

#### Agent prompt style
- name the scene object owner
- name the prefab owner
- name the `ScriptableObject` owner
- name the editor surface

### Unreal 5

#### 2D
- Paper2D sprites and flipbooks for 2D presentation
- `AActor` for world entities
- collision components for contact
- Blueprint for designer-facing assembly
- Data Assets for shared tuning

#### 3D
- `ACharacter` for standard embodied player/enemy movement
- `APawn` for custom possession-based units
- `UActorComponent` for reusable behavior
- `UObject` and Data Assets for shared data
- `UUserWidget` / UMG for UI
- GAS, StateTree, EQS, or Mass only when the project truly needs them

#### Use first when
- gameplay framework structure matters
- designer-facing iteration matters
- the project expects stronger packaging or larger 3D systems

#### Fast example slice
- a gameplay-framework encounter with a character, enemy actor, health component, and UMG overlay

#### Agent prompt style
- name the Actor owner
- name the Component owner
- name the data asset owner
- name the editor validation loop

## Mechanics by pattern

| Mechanic | Godot 4 default | Unity 6 default | Unreal 5 default |
|---|---|---|---|
| Player movement | `CharacterBody2D` or `CharacterBody3D` | `CharacterController` or `Rigidbody`/`Rigidbody2D` | `ACharacter` or `APawn` |
| Contact / damage | `Area2D` / `Area3D` or direct queries | `Collider2D` / `Collider` plus non-alloc queries | collision components or `TakeDamage` / GAS |
| Camera | `Camera2D` / `Camera3D` | camera rig or virtual camera system | camera component plus spring arm or custom rig |
| Shared tuning | `Resource` | `ScriptableObject` | Data Asset / `UObject`-backed asset |
| Reusable hierarchy | `.tscn` scene | Prefab | Blueprint / Actor template |
| UI / HUD | `Control` / `CanvasLayer` | UI Toolkit or uGUI | UMG / Viewmodel |
| Pathfinding | NavigationServer or `AStarGrid2D` / `AStar3D` | AI Navigation or custom graph/grid | navmesh, EQS, StateTree, or custom graph |
| High-count visuals | `MultiMesh` / server APIs | pooling / instancing / data-oriented path | instancing / Mass |
| GPU / render scale | `RenderingServer` / `RenderingDevice` / `MultiMesh` | `GraphicsBuffer` / `ComputeShader` / instanced indirect draw | Instanced Static Meshes / Nanite / HLOD |

## Example pairs to study first

### Godot 4
- `Node2D` + `CharacterBody2D` for player movement
- `Area2D` for pickups and damage rings
- `Control` + `CanvasLayer` for HUD and menus
- `Resource` for shared item or upgrade tuning
- `PackedScene` for reusable enemies or projectiles

### Unity 6
- `GameObject` + `MonoBehaviour` for authored behavior
- `Prefab` for repeated enemies or props
- `ScriptableObject` for item, enemy, or ability definitions
- `EditorWindow` for workflow tools
- `ObjectPool<T>` for combat projectiles or effects

### Unreal 5
- `ACharacter` or `APawn` for player embodiment
- `UActorComponent` for health, targeting, or interaction helpers
- Data Asset for item/enemy/ability definitions
- `UUserWidget` for HUD and menus
- Blueprint for designer-friendly assembly

## What an agent should say before implementation

Every engine-aware recommendation should include:

1. the runtime owner
2. the reusable data owner
3. the editor owner
4. the 2D or 3D stack choice
5. the smallest validation loop
6. the first thing that breaks at scale

For architecture-heavy work, also name the canonical owner, event source, state graph, projection targets, and the narrow proof path.

## Recommended use cases

Use this page when the task is:

- a new mechanic
- a new UI flow
- a new UI flow or template-selection task
- an engine comparison or scorecard task
- a new inventory or save system
- a new enemy or character architecture
- a state, authority, event, or projection architecture decision
- a quality or optimization-criteria pass that needs ownership, validation, and first-lever clarity before refactoring
- a new visuals or animation ownership question
- a new audio or animation presentation question
- an asset ownership, import, or packaging decision
- a performance pass that needs the fastest ownership summary before tuning
- a benchmark or measurement pass that needs the family, baseline, threshold, and artifact before comparison
- a genre-shaped performance pass that needs the first genre lever before tuning
- an advanced optimization pass that needs the algorithm family before tuning
- a GPU / render communication pass that needs the CPU owner, GPU owner, and first render lever before tuning
- a library or package selection pass that needs the smallest official stack before tuning
- a new engine decision for a slice or prototype
- a developer-profile or team-fit decision before the slice starts

For system-heavy work, pair this page with `docs/reference/system-atlas.md` before the slice grows.
For developer-fit work, pair this page with `docs/reference/engine-fit.md` and `docs/examples/engine-fit-example.md` before the slice grows.
For UI or template-heavy work, also pair it with `docs/reference/ui-guide.md` and `docs/examples/ui-example.md`.
For audio or animation presentation work, also pair it with `docs/reference/audio-animation-guide.md` and `docs/examples/audio-animation-example.md`.
For asset-heavy work, also pair it with `docs/reference/asset-guide.md` and `docs/examples/asset-example.md`.
For benchmark or measurement work, also pair it with `docs/reference/benchmark-guide.md` and `docs/examples/benchmark-example.md`.
For genre-shaped performance work, also pair it with `docs/reference/genre-perf-guide.md` and `docs/examples/genre-perf-example.md`.
For advanced optimization work, also pair it with `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md`.
For quality or optimization-criteria work, also pair it with `docs/reference/quality-guide.md` and `docs/examples/quality-example.md`.
For library or package selection work, pair it with `docs/reference/library-guide.md` and `docs/examples/library-example.md`.
For architecture-heavy work, pair it with `docs/reference/architecture-guide.md` and `docs/examples/architecture-example.md`, and use the diagrams first if the owner/boundary map is still fuzzy.

## Related docs

- `docs/reference/engine-selection-guide.md`
- `docs/reference/perf-guide.md`
- `docs/reference/benchmark-guide.md`
- `docs/reference/genre-perf-guide.md`
- `docs/reference/advanced-perf-guide.md`
- `docs/reference/quality-guide.md`
- `docs/reference/library-guide.md`
- `docs/reference/asset-guide.md`
- `docs/reference/engine-eval.md`
- `docs/reference/gpu-guide.md`
- `docs/reference/architecture-guide.md` and its diagrams
- `docs/reference/engine-examples.md`
- `docs/examples/engine-eval-example.md`
- `docs/examples/asset-example.md`
- `docs/examples/benchmark-example.md`
- `docs/examples/architecture-example.md`
- `docs/reference/agent-guide.md`
- `docs/research/game-development/engines/README.md`
- the matching engine research notes in `docs/research/game-development/engines/`
