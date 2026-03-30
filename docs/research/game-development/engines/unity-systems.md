# Unity Systems

## Date
- 2026-03-28

## Summary
- Unity works best when scene objects, reusable data, UI, and editor tooling each keep a clear ownership boundary.
- For this repo, the practical default is: use the Input System for player verbs, `GameObject` plus Components for scene presence, `ScriptableObject` for shared authored data, prefabs for repeated hierarchies, and the UI stack that best fits the project before mixing runtime and editor concerns.
- Performance-sensitive gameplay should stay allocation-aware. When a system becomes query-heavy or swarm-heavy, the repo should force a decision between pooling, non-alloc queries, and a data-oriented path instead of letting per-frame garbage creep in.

## Primary sources
- [Input System](https://docs.unity3d.com/es/2019.4/Manual/com.unity.inputsystem.html)
- [Input documentation for Unity 6](https://docs.unity3d.com/jp/current/Manual/Input.html)
- [ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [UI Toolkit package](https://docs.unity3d.com/es/2021.1/Manual/UIToolkits.html)
- [uGUI package](https://docs.unity3d.com/es/2020.2/Manual/com.unity.ugui.html)
- [Animator controller](https://docs.unity3d.com/Manual/AnimatorController.html)
- [Unity AI Navigation package](https://docs.unity3d.com/ja/6000.0/Manual/com.unity.ai.navigation.html)
- [ObjectPool<T>](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Pool.ObjectPool_1.html)
- [Physics.RaycastNonAlloc](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Physics.RaycastNonAlloc.html)
- [Physics2D.OverlapCircleNonAlloc](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Physics2D.OverlapCircleNonAlloc.html)

## Why this matters to this repo
- Unity tasks should not collapse input, UI, gameplay, and authoring data into one MonoBehaviour by habit.
- The repo needs a stable answer to "is this a scene object, prefab, asset, or editor tool" because that affects iteration speed and testability.
- Shared tuning data and per-run state should stay separate so the project can grow from a prototype into a multi-session game without rewriting the whole structure.

## Decision impact
- Use this playbook when designing controls, menus, HUD, inventory, skill trees, enemy behavior, save flows, or performance-sensitive combat systems.
- Prefer explicit boundaries:
  - input intent -> Input System action assets and player mappings
  - world presence -> `GameObject`
  - behavior -> Component / `MonoBehaviour`
  - shared authored data -> `ScriptableObject`
  - repeated hierarchies -> Prefab
  - editor tooling -> `Editor` / `EditorWindow`

## Input and controls
- Default owner: Input System action assets and player input layers.
- Use action maps for verbs like `Move`, `Dash`, `Interact`, `Pause`, `MenuAccept`, and `MenuBack`.
- Keep remapping and device-specific concerns separate from combat or interaction code.
- Watch out for: depending on old-style per-frame polling when the Input System package is a better fit.

## UI, HUD, and menu flow
- Choose the UI stack deliberately:
  - UI Toolkit for editor and data-driven UI workflows
  - uGUI when the project already depends on it or the runtime UI is built around it
- Keep HUD and menu state separate from gameplay state, then bind from view models or projection components.
- Watch out for: UI scripts that mutate gameplay systems directly instead of sending intent to a gameplay layer.

## Inventory, equipment, and authored data
- Default owner: `ScriptableObject` for item definitions, equipment templates, and balance data.
- Keep runtime stacks, slots, and loadout state on scene/runtime components, not inside the shared asset.
- Prefabs can carry repeated pick-up or equipment visuals, but the shared definition should stay in an asset.
- Watch out for: stuffing mutable progression into the shared tuning object.

## Abilities, upgrades, and build variety
- Default owner: data assets plus gameplay Components.
- Use assets for ability definitions, cooldown tuning, and upgrade tables.
- Use runtime Components or service objects for current cooldowns, charges, and temporary buffs.
- Watch out for: building an upgrade system entirely inside one giant MonoBehaviour with no data boundary.

## Enemy behavior and encounter design
- Default owner: enemy prefab plus Components, with archetype data in `ScriptableObject`s.
- Use explicit prefabs for repeated enemies and place behavior on reusable Components.
- For large numbers of spawned enemies or projectiles, measure whether pooling or a more data-oriented solution is needed before shipping.
- Watch out for: mixing decision state, sensing state, and UI feedback on the same component.

## Collider and contact flow
- Default owner: `Collider2D`, `Collider`, trigger surfaces, or ray/overlap queries depending on the mechanic.
- Treat the collider as the input surface and the gameplay system as the output surface.
- Typical inputs:
  - `OnTriggerEnter`, `OnTriggerStay`, `OnTriggerExit`
  - `OnCollisionEnter`, `OnCollisionStay`, `OnCollisionExit`
  - `RaycastNonAlloc` or `Physics2D.OverlapCircleNonAlloc` when the mechanic is query-driven
  - layer and trigger filtering
- Typical outputs:
  - damage, pickup, aggro, or door/open requests
  - animation, audio, or VFX signals
  - UI prompts or projected availability state
  - pooled spawn requests for hit effects or projectiles
- Watch out for: letting the collider own both detection and business logic when a cleaner runtime owner should receive the contact event.

## Save and progression
- Default owner: runtime save projection plus shared data assets.
- Save only the state needed to restore the run or profile, then reconstruct scene objects from authored data and prefab references.
- Keep persistence and projection separate from the definitions that produced the state.
- Watch out for: serializing every scene object field as if that were a stable save format.

## Performance and scale
- Use `ObjectPool<T>` for repeated short-lived objects such as projectiles or hit effects.
- Use non-alloc physics queries and layer collision filtering when a system is query-heavy.
- Use DOTS/Entities/Burst only when the problem is truly scale-driven, not as a default architecture choice.
- Watch out for: hidden allocations in hot paths and premature `Instantiate`/`Destroy` churn.

## Editor workflow
- Use custom inspectors for object-specific editing.
- Use `EditorWindow` for workflow tools, reports, or content browsers.
- Keep editor-only dependencies out of runtime assemblies.
- Watch out for: tools that break undo, prefab overrides, or multi-object editing.

## Best-fit first slice
- For a compact action slice, start with:
  - Input System action maps
  - a prefab-based player and enemy setup
  - `ScriptableObject`-driven upgrades or item definitions
  - a UI Toolkit or uGUI HUD
  - pooling for repeated combat objects

## Common mistakes to avoid
- Treating GameObjects as the place where all logic should live.
- Putting shared tuning into prefabs or MonoBehaviours instead of a `ScriptableObject`.
- Ignoring layer collision filtering and non-alloc query APIs in combat or sensing code.
- Mixing UI and gameplay authority in one script.
- Moving to DOTS before the project proves it needs that scale path.
