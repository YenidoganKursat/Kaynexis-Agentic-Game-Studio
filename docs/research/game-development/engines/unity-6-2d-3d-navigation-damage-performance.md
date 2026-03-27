# Unity 6 2D/3D, Navigation, Damage, and Performance Patterns

## Date
- 2026-03-27

## Summary
- Unity treats 2D and 3D as separate physics worlds. The manual explicitly distinguishes built-in 2D physics, built-in 3D physics, and data-oriented physics packages. Repo guidance should therefore force every feature to pick its primary simulation stack instead of casually mixing 2D and 3D assumptions.
- For authored movement over walkable surfaces, Unity's AI Navigation package is the high-level default. It supports navmesh building at edit time and runtime, dynamic obstacles, and navigation links. For grid tactics, board logic, or explicit graph traversal, a custom graph may still be better than forcing the problem into navmesh terms.
- Unity's performance guidance strongly emphasizes measurement first, collision filtering, collider choice, and memory discipline. The practical repo rule is to profile before tuning, reduce contact pairs with the layer collision matrix, prefer simpler colliders where possible, and avoid avoidable allocations in high-frequency queries.
- Unity exposes direct high-frequency optimization levers that matter for gameplay systems:
  - `ObjectPool<T>` for short-lived repeated objects
  - `Physics.RaycastNonAlloc` and `Physics2D.OverlapCircleNonAlloc` for query-heavy systems
  - layer collision matrix rules to reduce overlap work
  - DOTS packages such as Entities, Burst, and Unity Physics when the problem is truly data-oriented and large-scale
- For damage and hit detection, Unity's trigger and collision model should be explicit. Trigger colliders are the clean authored option for hitboxes, hurtboxes, and zones; layer rules decide what can interact; immutable tuning data should stay in authored assets such as `ScriptableObject`s instead of being scattered through scene instances.

## Primary sources
- [Unity Physics overview](https://docs.unity3d.com/es/2019.4/Manual/PhysicsSection.html)
- [Unity AI Navigation package](https://docs.unity3d.com/ja/6000.0/Manual/com.unity.ai.navigation.html)
- [Unity ObjectPool<T>](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Pool.ObjectPool_1.html)
- [Unity Physics.RaycastNonAlloc](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Physics.RaycastNonAlloc.html)
- [Unity Physics2D.OverlapCircleNonAlloc](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Physics2D.OverlapCircleNonAlloc.html)
- [Unity optimize physics performance](https://docs.unity3d.com/jp/current/Manual/physics-optimization.html)
- [Unity layer collision matrix guidance](https://docs.unity3d.com/jp/current/Manual/physics-optimization-cpu-collision-layers.html)
- [Unity collider types and performance](https://docs.unity3d.com/kr/6000.0/Manual/physics-optimization-cpu-collider-types.html)
- [Unity trigger colliders](https://docs.unity3d.com/ja/current/Manual/collider-interactions-create-trigger.html)
- [Unity OnTrigger events](https://docs.unity3d.com/ja/2023.2/Manual/collider-interactions-ontrigger.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity Entities package docs](https://docs.unity3d.com/Packages/com.unity.entities@latest)
- [Unity Physics package docs](https://docs.unity3d.com/Packages/com.unity.physics@latest)
- [Unity Burst package docs](https://docs.unity3d.com/Packages/com.unity.burst@latest)

## Why this matters to this repo
- Unity tasks should always state which runtime stack owns the feature:
  - built-in 2D physics
  - built-in 3D physics
  - data-oriented runtime with Entities and related packages
- Agents should treat AI Navigation as the default answer for authored navmesh movement, not immediately reinvent pathfinding in user code. Custom graphs should be justified by the world model, not habit.
- High-frequency combat and sensing systems should describe how they avoid accidental allocation churn. Unity offers explicit non-alloc query APIs and pooling helpers, so the repo should surface them before teams normalize per-frame array churn or repeated instantiate/destroy loops.
- Damage architecture should keep three boundaries explicit:
  - authored contact surface -> trigger or collision setup plus layers
  - gameplay reaction -> runtime component logic
  - reusable tuning -> `ScriptableObject` or other authored assets
- For large swarms, many projectiles, or heavy AI populations, agents should discuss whether the feature still belongs in classic `GameObject`/`MonoBehaviour` form or whether the scale justifies a DOTS path.

## Decision impact
- Unity engine guidance should require agents to name:
  - world stack: 2D, 3D, or DOTS-oriented
  - pathfinding model: AI Navigation navmesh versus custom graph/grid
  - damage routing: triggers, collisions, or direct physics queries
  - scale lever: classic object model with pooling, or data-oriented migration
- The Unity engine checklist should add explicit checks for stack choice, nav/pathfinding choice, damage/query discipline, and high-scale representation.
- Routing and checklist resolution should treat `damage`, `pathfinding`, `navmesh`, `pooling`, `alloc`, `Burst`, and `ECS` as deliberate system-design signals rather than generic implementation detail.
