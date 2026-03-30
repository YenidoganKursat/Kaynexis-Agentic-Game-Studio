# Engine Atlas

This page is the deeper companion to `engine-map.md`.

Use it when the agent needs more than a one-line owner summary and must reason about:

- which class family owns runtime state
- which object family owns shared authored data
- which editor surface owns tuning and validation
- which input/output contract a mechanic should expose
- which example slice is the best one to inspect before coding

This is not an exhaustive catalog of every class in every engine.
It is a **core class atlas** for the classes and object families that matter most in gameplay, UI, tools, persistence, and high-scale visuals.

## How to read this page

When implementing a feature, read in this order:

1. Find the engine
2. Find the class family
3. Identify runtime owner, data owner, and editor owner
4. Identify the mechanic input and output
5. Verify the smallest example slice

If the feature is still vague after that, go back to:

- `docs/reference/engine-map.md`
- `docs/reference/system-atlas.md`
- `docs/reference/godot-atlas.md`
- `docs/reference/unity-atlas.md`
- `docs/reference/unreal-atlas.md`
- the matching engine mechanic guide in `docs/research/game-development/engines/`
- the matching systems note in `docs/research/game-development/systems/`

## Godot 4 core atlas

### Scene graph and transform family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `Node` | generic lifecycle and tree membership | scene enter/exit, signals, child events | orchestration, delegation, cleanup | do not overload it with raw gameplay state |
| `Node2D` | 2D transform and scene grouping | 2D positioning, child attachment | 2D hierarchy, parent-relative motion | keep it as structure, not logic sink |
| `Node3D` | 3D transform and scene grouping | 3D positioning, child attachment | 3D hierarchy, parent-relative motion | do not use it as a generic global object |
| `Control` | UI layout and interaction | focus, input, data projection | UI updates, callbacks, menu flow | separate presentation from game state |
| `CanvasLayer` | screen-space UI stacking | HUD/menu layering requests | visible UI overlays | do not let it own gameplay logic |

### Movement, contact, and navigation family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `CharacterBody2D` | authored 2D locomotion | input vectors, gravity, slope data | motion, floor state, collisions | keep combat, camera, and animation separate |
| `CharacterBody3D` | authored 3D locomotion | input vectors, gravity, slope data | motion, floor state, collisions | do not make it a combat catch-all |
| `Area2D` | 2D overlap detection | trigger bodies, query signals | pickups, damage zones, aggro probes | it is a detection input, not a system by itself |
| `Area3D` | 3D overlap detection | trigger bodies, query signals | pickups, damage zones, sensing | same rule: detect, then hand off |
| `RayCast2D` | line-of-sight and hit checks | ray queries | hit results, interaction checks | do not hide repeated expensive queries in `_process` |
| `RayCast3D` | line-of-sight and hit checks | ray queries | hit results, interaction checks | cache and throttle when possible |
| `NavigationAgent2D` | 2D path intent | target points, nav space | steering hints, path progress | keep high-level intent separate from movement execution |
| `NavigationAgent3D` | 3D path intent | target points, nav space | steering hints, path progress | same separation principle |

### Data, scene, and persistence family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `Resource` | shared authored data | editor-tuned values, imported content | item defs, upgrade defs, tuning tables | do not store per-run mutable state here |
| `PackedScene` | reusable scene blueprint | authored scene content | instance creation | keep instance state outside the blueprint |
| `SceneTree` | runtime tree coordination | scene changes, global flow | current active scene graph | avoid turning it into a project-wide dumping ground |

### Presentation and scale family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `AnimationPlayer` | explicit animation playback | state changes, timeline triggers | animation state, callbacks, events | do not encode gameplay rules only in animation |
| `AnimationTree` | animation state logic | locomotion or combat state | blended animation output | keep it in the presentation lane |
| `AnimatedSprite2D` | frame-based 2D visual playback | sprite frames, state events | visible sprite animation | use it for clarity, not systemic ownership |
| `Sprite2D` | 2D image presentation | texture and transform updates | visible 2D art | keep art input separate from gameplay state |
| `Camera2D` / `Camera3D` | viewpoint control | player follow, cutscene commands | frame composition | do not let it own input or combat state |
| `MultiMesh` | repeated visual scale | many repeated instances | batched high-count rendering | use when repetition becomes the bottleneck |

### GPU and render-scale family

| Engine | Render-side owner | Shared data owner | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| Godot 4 | `RenderingServer`, `RenderingDevice`, `MultiMesh` | `Resource` | buffer-driven rendering, compute, repeated visuals | do not turn render helpers into gameplay owners |
| Unity 6 | `GraphicsBuffer`, `ComputeShader`, instanced indirect draw | `ScriptableObject` or plain model | GPU compute, instancing, culling, repeated visuals | avoid readback-first designs and per-object churn |
| Unreal 5 | Instanced Static Meshes, Nanite, HLOD | Data Asset | repeated geometry, high-count rendering, visibility reduction | do not confuse representation choice with gameplay ownership |

### GPU ownership contract

- state the CPU owner
- state the GPU owner
- state the buffer shape and update cadence
- state the readback policy
- state the first render lever before tuning

### Best first examples

- `Node2D` + `CharacterBody2D` for readable 2D movement
- `Area2D` + `Resource` for pickup/damage/upgrade interaction
- `Control` + `CanvasLayer` for HUD and menus
- `AnimationPlayer` for explicit attack windups and feedback

## Unity 6 core atlas

### Identity, hierarchy, and runtime family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `GameObject` | scene identity and composition container | scene placement, prefab instantiation | component host, hierarchy structure | do not put shared data directly on the object shell |
| `Transform` | spatial hierarchy | position, rotation, parenting | world/local coordinates | treat it as geometry, not state logic |
| `MonoBehaviour` | scene-bound behavior | Unity lifecycle, input, events | gameplay behavior, orchestration | keep it focused and avoid giant god-classes |
| `Prefab` | reusable hierarchy blueprint | authored prefab setup | repeatable scene instances | avoid making every prefab a unique one-off singleton |
| `Scene` | level/runtime composition | load/unload, startup flow | active play space | do not use scenes as a substitute for modular data |

### Shared data and persistence family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `ScriptableObject` | shared authored tuning | inspector-edited data | item defs, upgrades, configs | do not store per-run mutable state here |
| `DontDestroyOnLoad` objects | cross-scene persistence | bootstrapping, services | persistent runtime services | keep them minimal and explicit |
| Plain C# model / service | runtime data and logic | gameplay events | inventory state, progression, rules | separate from scene bindings |

### Contact, physics, and locomotion family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `Collider2D` | 2D contact input | trigger/collision callbacks, layer rules, queries | damage, pickup, aggro, interaction | collider is detection, not full gameplay logic |
| `Collider` | 3D contact input | trigger/collision callbacks, layer rules, queries | damage, pickup, aggro, interaction | same principle as 2D |
| `Rigidbody2D` | simulated 2D motion | forces, velocity, contact resolution | physical movement, knockback | do not mix with direct transform warping unless intentional |
| `Rigidbody` | simulated 3D motion | forces, velocity, contact resolution | physical movement, knockback | keep high-frequency queries pooled or non-alloc |
| `CharacterController` | authored 3D control movement | input vectors, ground checks | responsive locomotion | not a physics body; design around that difference |
| `Physics2D` / `Physics` | query and collision API | raycasts, overlaps, sweeps | hit/contact results | use non-alloc patterns when scale matters |

### UI, animation, and tooling family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `UI Toolkit` | editor/runtime UI framework | data binding, style, events | menus, tools, HUD panels | choose the right UI stack intentionally |
| `uGUI` | runtime HUD and menus | input events, anchors, state data | screen overlay UI | do not overbuild editor tooling inside runtime UI |
| `Animator` | animation state machine | gameplay state, triggers, parameters | visible animation output | keep logic and presentation distinct |
| `SpriteRenderer` | 2D art presentation | sprite updates, sorting, tinting | visible 2D visuals | keep game rules elsewhere |
| `ParticleSystem` | VFX playback | effect triggers, tuning | combat feedback, ambiance | pool or reuse when effect spam is high |
| `EditorWindow` | custom editor tool | authoring commands, data scans | tooling panels, batch actions | keep it editor-only and shippable-safe |
| `Editor` / `CustomEditor` | inspector customization | serialized objects, validation | targeted inspector UX | avoid turning every inspector into a mini app |

### Best first examples

- `GameObject` + `MonoBehaviour` for authored behavior
- `ScriptableObject` for upgrades, items, and enemy definitions
- `Collider2D` or `Collider` for contact input that hands off to gameplay
- `EditorWindow` for batch authoring tools
- `ObjectPool<T>` for projectiles or repeated effects

## Unreal 5 core atlas

### Runtime and gameplay framework family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `UObject` | base authored/runtime object | asset data, system references | reusable runtime or asset-backed logic | do not use it as a catch-all for every stateful thing |
| `AActor` | world entity | world placement, components, gameplay events | spawned entities, interaction, world presence | keep data ownership explicit |
| `APawn` | possession-based embodiment | possession, control input | controllable unit presence | use when control is not standard character movement |
| `ACharacter` | embodied movement standard | movement input, animation/state data | locomotion, collision, gameplay presence | do not overload with UI or editor concerns |
| `UActorComponent` | reusable behavior module | owner actor, component events | health, targeting, sensing, interaction | split behavior into clear components, not giant monoliths |
| `USceneComponent` | transform-bearing component | parent transform, attachment rules | spatial attachment and positioning | keep it structural unless it truly owns behavior |
| `UWorld` | active world context | level load, gameplay state | runtime world and subsystem context | do not treat it as a generic singleton replacement |
| `APlayerController` | input and possession control | player input, UI control state | pawn control, cursor/UI routing | keep it between input and embodiment |
| `AGameModeBase` / `AGameStateBase` / `APlayerState` | match rules and state separation | startup rules, replicated state | authority, match, player state | keep server/client ownership clear |
| `UGameInstance` | game-wide persistent runtime context | startup flow, services | cross-level session context | keep it thin and explicit |

### Data, assets, and persistence family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `UDataAsset` / `UPrimaryDataAsset` | shared authored data | designer-authored tuning | item defs, ability defs, encounter defs | do not store per-run mutable state here |
| `USaveGame` | save projection | runtime snapshot, migration data | saved profile/state | keep it projection-oriented, not full live state |
| Blueprint assets | designer-assembled gameplay | class graphs, variables, event graphs | assembly, prototyping, content behavior | keep architecture readable; avoid hidden tangles |

### UI, animation, and system family

| Class / family | What it owns | Typical input | Typical output | Watch out |
| --- | --- | --- | --- | --- |
| `UUserWidget` / UMG | runtime UI | data model updates, input | HUD, menus, overlays | keep UI as projection, not authority |
| `AnimInstance` / Animation Blueprint | animation logic | movement/state parameters | animated character output | do not let animation become a stealth gameplay rules engine |
| `SkeletalMeshComponent` | animated visible body | animation set, pose updates | character visuals | keep visuals decoupled from combat rules |
| `Niagara` | particle/VFX system | effect triggers, parameters | scalable VFX output | use it as a feedback layer, not a gameplay owner |
| `Blueprint` editor | designer assembly surface | graph editing, property tuning | gameplay assembly, data wiring | watch for logic scattering across too many blueprints |

### Systems that matter when the project scales

- `Gameplay Ability System` for ability-heavy, effect-heavy, or status-heavy gameplay
- `StateTree` for structured AI/state orchestration
- `Behavior Tree` for readable AI behavior composition
- `EQS` for environment-aware tactical queries
- Navmesh and AI Perception for movement and sensing

### Best first examples

- `ACharacter` + `UActorComponent` for player movement and combat helpers
- `UPrimaryDataAsset` for item, enemy, or upgrade definitions
- `UUserWidget` for HUD and menus
- Blueprint for designer-friendly assembly
- GAS only when the rules really need it

## Additional structural families

These are the next structures to reach for when the core atlas is not enough yet.

| Engine | Family | Representative classes | When to reach for it | Watch out |
| --- | --- | --- | --- | --- |
| Godot 4 | Physics bodies | `StaticBody2D` / `StaticBody3D`, `RigidBody2D` / `RigidBody3D` | hard blockers, simulation, physical props | do not use them as the default authored character body |
| Godot 4 | Scene and blueprint flow | `PackedScene`, `SceneTree`, `Viewport` / `SubViewport` | reusable hierarchies, orchestration, render islands | do not turn them into live mutable state containers |
| Godot 4 | Presentation helpers | `Sprite2D` / `Sprite3D`, `AudioStreamPlayer2D` / `AudioStreamPlayer3D`, `Timer` | visible feedback, timing, audio cues | keep gameplay authority in gameplay nodes |
| Godot 4 | Load/save helpers | `FileAccess`, `ResourceLoader`, `ResourceSaver` | import, load, save, persistence plumbing | do not hide mechanic truth inside file or load helpers |
| Godot 4 | Editor extension | `EditorPlugin`, `EditorInspectorPlugin` | import rules, validation, authoring tools | keep editor-only behavior out of runtime scenes |
| Unity 6 | UI and projection | `Canvas`, `RectTransform`, `UIDocument`, `VisualElement`, `TextMeshProUGUI` | HUDs, menus, layout, rich UI projection | do not let UI own gameplay authority |
| Unity 6 | Motion and framing | `Camera`, `Rigidbody`, `CharacterController`, `NavMeshAgent` | authored movement, framing, AI motion | do not mix force motion, authored motion, and navmesh motion casually |
| Unity 6 | Visual feedback | `SpriteRenderer`, `Animator`, `AnimatorOverrideController`, `ParticleSystem` | 2D/3D visuals, animation, effects | do not encode rules only in animation or VFX state |
| Unity 6 | Content and load flow | `Scene`, `Addressables`, `InputActionAsset`, `AudioSource`, `AudioMixer` | scene loading, content lookup, input maps, audio routing | keep runtime state separate from authored load data |
| Unity 6 | Board / tile structure | `Grid`, `Tilemap` | grid worlds, tactics boards, dense tile layouts | do not overbuild per-cell MonoBehaviours when a tile system fits |
| Unreal 5 | Collision and mesh bodies | `UPrimitiveComponent`, `UStaticMeshComponent`, `USkeletalMeshComponent`, `UCharacterMovementComponent` | collision, visible bodies, locomotion bodies | do not bury combat or persistence inside a mesh component |
| Unreal 5 | Camera rig | `UCameraComponent`, `USpringArmComponent` | follow rigs, framing, offsets | do not mix camera ownership with input or match state |
| Unreal 5 | UI projection | `UWidgetComponent`, `UUserWidget` | world widgets, HUDs, menus | keep widgets as projections, not authority |
| Unreal 5 | Input and control | `UEnhancedInputComponent`, `UInputAction`, `UInputMappingContext`, `UEnhancedInputLocalPlayerSubsystem` | modern input mapping and possession-aware input flow | do not hard-code input routing into the pawn |
| Unreal 5 | Systems and data | `UGameInstanceSubsystem`, `UWorldSubsystem`, `ULocalPlayerSubsystem`, `UDataTable`, `UTimelineComponent` | session services, world services, authored tables, timed logic | keep data assets and subsystems distinct from runtime actors |
| Unreal 5 | AI and VFX | `UBehaviorTree`, `UBlackboardComponent`, `UNiagaraComponent` | readable AI structure and scalable VFX | do not let AI helpers or VFX components become the real gameplay owner |

## Cross-engine mechanic ownership cheat sheet

| Mechanic | Godot 4 owner | Unity 6 owner | Unreal 5 owner |
| --- | --- | --- | --- |
| Player body | `CharacterBody2D` / `CharacterBody3D` | `CharacterController` / `Rigidbody` | `ACharacter` / `APawn` |
| Contact detection | `Area2D` / `Area3D` | `Collider2D` / `Collider` | collision component / overlap / damage events |
| Shared tuning | `Resource` | `ScriptableObject` | Data Asset |
| UI layer | `Control` / `CanvasLayer` | UI Toolkit / uGUI | UMG / `UUserWidget` |
| Tooling surface | editor plugin / `@tool` / Inspector | `EditorWindow` / `Editor` | Blueprint editor / Details panel / editor utility |
| High-count visuals | `MultiMesh` | pooling / instancing | instancing / Mass / Niagara |
| Pathfinding | nav server / graph | AI Navigation / custom grid | navmesh / EQS / StateTree / custom graph |
| GPU / render scale | `RenderingServer` / `RenderingDevice` | `GraphicsBuffer` / `ComputeShader` | instancing / Nanite / HLOD |

## What to tell the agent before implementation

Every engine-aware implementation plan should state:

1. the runtime owner
2. the shared data owner
3. the editor owner
4. the mechanic input and output
5. the first scale risk
6. the smallest validation loop
7. for GPU-heavy work, the CPU owner, GPU owner, buffer shape, readback policy, and first lever

## Example task prompts

### Unity 6

- "Build a `Collider2D`-driven pickup that emits UI, sound, and inventory state changes without letting the collider own the inventory model."
- "Create a `ScriptableObject` item definition flow and a runtime inventory model projection."
- "Add a pooled projectile system with explicit collision inputs and clear damage outputs."
- "Compare Unity `GraphicsBuffer`, `ComputeShader`, and indirect instancing for a dense projectile field before changing gameplay code."

### Godot 4

- "Implement `Area2D` pickup detection, but keep item definition data in `Resource` and keep HUD projection separate."
- "Build a `CharacterBody2D` dodge that does not conflate motion, camera, and combat state."
- "Add a `Control` HUD for upgrade choice that only reads projected state."
- "Research the GPU communication path for a Godot 4 survivorlike and decide whether `MultiMesh` or `RenderingDevice` is the first lever."

### Unreal 5

- "Use `ACharacter` for movement, `UActorComponent` for health, and `UPrimaryDataAsset` for enemy tuning."
- "Build a UMG HUD that only projects state and never owns combat authority."
- "Plan a Blueprint-friendly encounter slice with clear actor/component/data ownership."
- "Choose between Unreal Instanced Static Meshes, Nanite, and HLOD for repeated world objects before scaling Actor count."

## Related docs

- `docs/reference/engine-map.md`
- `docs/reference/agent-guide.md`
- `docs/reference/engine-examples.md`
- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`
- the matching engine research notes in `docs/research/game-development/engines/`
