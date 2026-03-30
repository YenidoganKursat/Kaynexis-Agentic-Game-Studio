# Unity Classes

## Date
- 2026-03-27

## Summary
- Unity's most-used gameplay primitives come from composition: `GameObject` as container, Components as behavior, Prefabs as reusable hierarchy, and `ScriptableObject` as reusable authored data.
- The highest-value early decision in Unity is not "which script do we write first," but "does this feature belong in built-in 2D, built-in 3D, or a larger-scale data-oriented path?"
- Unity projects stay healthy when runtime code, editor tooling, scene/prefab hierarchy, and authored data assets remain intentionally separated.

## Primary sources
- [GameObjects](https://docs.unity3d.com/6000.1/Documentation/Manual/class-GameObject.html)
- [Using Components](https://docs.unity3d.com/6000.1/Documentation/Manual/UsingComponents.html)
- [Transform](https://docs.unity3d.com/6000.1/Documentation/Manual/class-Transform.html)
- [Rigidbody](https://docs.unity3d.com/6000.1/Documentation/Manual/class-Rigidbody.html)
- [Rigidbody 2D](https://docs.unity3d.com/6000.1/Documentation/Manual/class-Rigidbody2D.html)
- [Character Controller](https://docs.unity3d.com/6000.1/Documentation/Manual/class-CharacterController.html)
- [Animator](https://docs.unity3d.com/6000.1/Documentation/Manual/class-Animator.html)
- [Prefabs](https://docs.unity3d.com/6000.1/Documentation/Manual/prefabs-introduction.html)
- [ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [AI Navigation package](https://docs.unity3d.com/ja/6000.0/Manual/com.unity.ai.navigation.html)
- [NavMeshAgent API](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/AI.NavMeshAgent.html)
- [ObjectPool<T>](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Pool.ObjectPool_1.html)
- [Physics.RaycastNonAlloc](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Physics.RaycastNonAlloc.html)
- [Physics2D.OverlapCircleNonAlloc](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Physics2D.OverlapCircleNonAlloc.html)

## Why this matters to this repo
- Unity tasks in this repo should start from composition choices and stack choices, not generic C# coding habits.
- Repo users need a practical reference for which Unity primitives typically own movement, sensing, camera, prefab reuse, authored data, and editor tooling in 2D and 3D projects.
- Agent outputs need a common way to say whether a mechanic belongs in a `MonoBehaviour`, `ScriptableObject`, Prefab, custom Editor surface, or a broader data-oriented runtime.

## Decision impact
- Unity recommendations should cite this guide when choosing between `Rigidbody`, `Rigidbody2D`, `CharacterController`, trigger/collider flows, Prefab ownership, or `ScriptableObject` data ownership.
- Feature docs should declare both the runtime stack and the reusable data shape before implementation.
- Checklists and routing should surface the difference between classic GameObject-scale work and data-oriented scale work more explicitly.

## 2D building blocks

### `GameObject` + `Transform`
- Purpose: the base authored object and hierarchy container.
- Use it for: scene roots, spawn points, effect carriers, and logical grouping.
- Watch out for: adding too many responsibilities to a single scene object just because Components make it easy.

### `Rigidbody2D`
- Purpose: 2D physics-driven motion and collision participation.
- Use it for: bodies that should respect 2D physics simulation, forces, and collision callbacks.
- Watch out for: using it for precision platforming or authored combat movement when the mechanic really wants tighter control.

### `Collider2D` and trigger colliders
- Purpose: collision and overlap surfaces in 2D.
- Use them for: pickups, hurtboxes, hitboxes, sensors, doors, and zone logic.
- Watch out for: weak layer discipline; trigger-heavy projects become expensive and confusing when every layer can talk to every other layer.

#### Input/output contract
- Inputs:
  - physics overlap or collision events from `Collider2D`
  - explicit layer and trigger filtering
  - optional non-alloc queries when the mechanic needs a pull-based check instead of a callback
  - authored contact rules from the scene, prefab, or `ScriptableObject`
- Outputs:
  - gameplay signals such as damage, pickup, aggro, interaction, or door-open requests
  - state changes on the owning `MonoBehaviour` or gameplay service
  - feedback events for animation, sound, or VFX
  - UI projection when the contact changes what the player can do
- Agent rule: name the collider owner, the trigger or collision source, the layer mask, and the exact output the contact produces before implementing the mechanic.

### `Animator`
- Purpose: animation state and transitions.
- Use it for: sprite animation state flow, blend-like transitions, and event timing when the mechanic benefits from authored animation graphs.
- Watch out for: hiding mechanic truth only in animation transitions rather than treating animation as a partner to gameplay state.

## 3D building blocks

### `CharacterController`
- Purpose: authored 3D locomotion without full rigid-body simulation.
- Use it for: first-person and third-person controllers, dash/mobility work, and gameplay where precise input response matters.
- Watch out for: assuming it behaves like a `Rigidbody`; you still need to own motion, grounding, and push/interaction rules clearly.

### `Rigidbody`
- Purpose: physics-driven 3D body.
- Use it for: props, knockable hazards, vehicles, physical toys, and situations where force response is the mechanic.
- Watch out for: using it as the default player controller just because the game is 3D.

### `Collider` and trigger colliders
- Purpose: blocking and overlap surfaces in 3D.
- Use them for: interaction zones, hit checks, melee ranges, pickups, and environmental hazards.
- Watch out for: broad primitive overlap spam and avoidable allocations when sensing becomes frequent.

### `NavMeshAgent`
- Purpose: authored navmesh-driven movement.
- Use it for: AI that moves through walkable spaces defined by navmesh data.
- Watch out for: forcing grid or board-style traversal into navmesh terms when the mechanic is really graph-based.

### `Camera`
- Purpose: viewpoint ownership.
- Use it for: follow cameras, room cameras, orbit rigs, and authored framing.
- Watch out for: burying player input, target selection, and UI responsibility into one camera script.

## Shared authored-data building blocks

### Prefabs
- Purpose: reusable authored hierarchy and spawnable scene object.
- Use them for: enemies, projectiles, interactables, environment set pieces, and HUD widgets with stable structure.
- Watch out for: using scene-local objects for repeated things that should be prefabs, or turning one prefab into a dumping ground for many unrelated behaviors.

### `ScriptableObject`
- Purpose: shared serializable authored data.
- Use it for: enemy archetypes, weapon configs, damage tables, encounter packs, and global tuning sets.
- Watch out for: mutating shared assets at runtime when the feature really needs per-instance state.

## Common mechanic patterns

### Player movement
- 2D default: choose between authored motion with a simple component stack or physics-driven motion with `Rigidbody2D`; do not mix the two casually.
- 3D default: choose `CharacterController` for authored action movement, or `Rigidbody` only when full physical response is the point.
- Watch out for: mixing force-based motion, direct transform edits, and navmesh ownership in one controller.

### Contact and damage
- Use trigger colliders for readable authored contact surfaces.
- Use collision callbacks where physical collision itself is the mechanic.
- Use `NonAlloc` queries for frequent sight, projectile, or area scans that would otherwise allocate every frame.
- Watch out for: damage systems that skip layer ownership, pooling, or query discipline.

#### Contact ownership checklist
- If the mechanic begins with a touch, list the collider type and whether it is trigger or blocking.
- If the mechanic begins with a query, list the exact query type and why a callback would be worse.
- If the mechanic ends with a gameplay reaction, name the object that owns the reaction and whether it mutates runtime state, emits UI, or spawns effects.
- Keep the collider as the detection input, not the entire mechanic.

### Camera and framing
- 2D: keep camera follow separate from combat or interaction authority.
- 3D: prefer a small camera rig with explicit follow/pivot state over one giant controller script.
- Watch out for: camera code owning too much gameplay truth.

### Spawn and reuse
- Use Prefabs for repeated runtime hierarchy.
- Use `ObjectPool<T>` when repeated instantiate/destroy churn becomes part of the mechanic loop.
- Use `ScriptableObject` for shared tuning and authored templates.
- Watch out for: storing mutable runtime state inside shared tuning assets.

### Animation and state
- Use `Animator` as the animation control surface, not the only authority for hit confirmation, invulnerability, or encounter progression.
- Keep gameplay state readable in runtime code even when animation events are used.

## Writing style and naming

### Repo operating style
- This is repo guidance built on Unity's component model and common C# practice rather than a single Unity naming law.
- Practical repo rule:
  - `PascalCase` for types, public methods, and asset-facing class names
  - keep each `MonoBehaviour` narrow in purpose
  - keep shared tuning in `ScriptableObject` assets instead of static scattered constants
- Prefer file names that match the class they contain.

### Runtime vs editor style
- Keep `UnityEditor` code in editor-only assemblies or folders.
- Keep scene/prefab composition readable by avoiding "god components" that own combat, movement, animation, and UI state all at once.
- Serialize authored fields that designers must tune; keep transient caches and runtime state out of the inspector unless there is a debugging reason.

## What to watch out for
- Treating `Transform` edits, rigid-body motion, and navmesh motion as interchangeable.
- Letting Prefabs and scene instances drift until the project has no stable reusable source of truth.
- Using `ScriptableObject` as mutable runtime save state instead of shared authored data.
- Ignoring layer rules and then paying for noisy collision/trigger behavior later.
- Building giant `MonoBehaviour` classes because Unity makes it easy to keep adding fields forever.

## Additional structural families

### `Canvas`, `RectTransform`, `UIDocument`, `VisualElement`, and `TextMeshProUGUI`
- Purpose: screen-space and UI Toolkit presentation surfaces.
- Use them for: HUDs, menus, inventory panels, settings screens, and readable text-heavy interfaces.
- Watch out for: making UI the owner of gameplay truth instead of a projection of runtime state.

### `Camera`
- Purpose: viewpoint and framing.
- Use it for: follow cameras, room cameras, split views, and authored framing.
- Watch out for: mixing camera ownership with combat, input routing, or scene authority.

### `AudioSource` and `AudioMixer`
- Purpose: sound playback and audio routing.
- Use them for: one-shots, looping ambience, mixer groups, and scene audio control.
- Watch out for: turning audio playback into a hidden gameplay system.

### `SpriteRenderer` and `ParticleSystem`
- Purpose: 2D presentation and visual feedback.
- Use them for: sprites, hit flashes, VFX, and repeated feedback layers.
- Watch out for: encoding rules only in visual state changes.

### `Grid` and `Tilemap`
- Purpose: authored tile/grid level structure.
- Use them for: tactics boards, tile-based worlds, layout-driven level design, and board helpers.
- Watch out for: one MonoBehaviour per cell when the tile system can do the job.

### `Scene`, `Addressables`, and `InputActionAsset`
- Purpose: scene loading, asset addressing, and input map ownership.
- Use them for: content orchestration, reusable load flows, and central input definitions.
- Watch out for: putting runtime state inside load or input definition assets.

### `NavMeshAgent`
- Purpose: authored navmesh movement.
- Use it for: pathing AI in walkable spaces.
- Watch out for: using it where a custom grid or board walker is the real mechanic.
