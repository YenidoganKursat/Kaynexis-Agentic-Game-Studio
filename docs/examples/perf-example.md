# Perf Example

## Scope
- Survivorlike prototype spike from 200 to 900 active enemies

## Baseline
- Avg frame time: 28 ms
- Worst spike: 43 ms
- Repro: 6-minute survival arena with projectile-heavy build

## Decision order
- Confirm whether the bottleneck is simulation count, contact cost, or rendering density
- Keep the current representation if it can hit budget
- Move to pooling, non-alloc queries, or batching before tuning hot loops
- Only escalate to DOTS, Mass, or server-style representation when the measurement proves it

## Likely bottlenecks
- per-enemy update overhead
- projectile allocation churn
- expensive overlap checks at peak density
- repeated visual instances that should be batched instead of simulated

## Engine-shaped examples

### Godot 4
- Keep player and enemy logic on `Node` / `CharacterBody2D` or `CharacterBody3D`.
- Pool projectiles and use `Area` / `NavigationServer` only when the contact and movement model are clear.
- Promote repeated decoration or projectile visuals to `MultiMesh` once node overhead is the real limit.

### Unity 6
- Keep the room prototype on classic `GameObject` / Component / Prefab / `ScriptableObject` ownership first.
- Pool projectiles before changing the AI model.
- Use `NonAlloc` queries and layer filtering before moving to DOTS.

### Unreal 5
- Keep the encounter on `AActor` / `UActorComponent` / Data Asset ownership first.
- Use simple damage and collision channels before introducing GAS.
- Use instancing or Mass only if repeated objects or entity counts prove Actor-per-entity is too expensive.

## Genre-shaped companion

If the bottleneck is clearly shaped by the genre rather than the engine, switch to `docs/reference/genre-perf-guide.md` and `docs/examples/genre-perf-example.md` so the first lever is tied to the genre family instead of a generic FPS rule.

If the bottleneck turns out to be culling, partitioning, batching, instancing, or job systems, switch to `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` so the first lever is tied to the algorithm family instead of a generic FPS rule.

## Smallest high-impact fixes
- pool projectiles before touching AI behavior
- reduce per-frame expensive queries for off-screen enemies
- separate visual swarm density from full simulation count
- choose engine-native batching or instancing before a data-oriented rewrite

## Good agent prompts

- "Optimize the survivorlike by proving whether node count or projectile churn is the bottleneck."
- "Compare pooling versus a representation change for the enemy swarm before touching combat logic."
- "Choose the first FPS lever for Unity projectile spam and justify why DOTS is or is not the next step."

## Validation
- Re-run the same 6-minute scenario
- Capture frame time before and after
- Reject changes that improve perf but break dodge readability
