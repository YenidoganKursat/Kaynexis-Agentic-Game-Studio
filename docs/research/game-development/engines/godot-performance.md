# Godot Performance

## Date
- 2026-03-27

## Summary
- Godot exposes separate 2D and 3D scene, physics, and navigation stacks. For repo decisions, that means each gameplay slice should declare whether it is fundamentally `Node2D` or `Node3D` driven before systems start spreading across both.
- For pathfinding, Godot offers two different families of tools. Use the NavigationServer-backed 2D/3D navigation stack for authored traversable worlds and agent movement over nav regions. Use `AStarGrid2D` or `AStar3D` when the problem is a custom graph or grid with explicit nodes, not a general walkable surface.
- For hit detection and damage routing, Godot's area and collision systems are best treated as the authored contact layer. `Area2D` and the equivalent 3D area/collision stack work well for hitboxes, hurtboxes, trigger volumes, and proximity checks. The docs note that overlap lists update during physics processing and recommend signals when immediate event-style reactions matter.
- For scale, Godot's own performance guidance points toward lower-level server APIs and `MultiMesh` when the project needs to render or manage large numbers of similar objects. The repo implication is to keep normal node-based composition by default, then promote to server or instancing patterns only when node overhead becomes the measured bottleneck.
- For collision performance, Godot's physics docs and shape references reinforce a simple rule: prefer simple shapes and authored collision boundaries over expensive or overly detailed runtime geometry when the goal is fast gameplay checks.
- If the real bottleneck is GPU ownership or CPU-GPU communication rather than generic scale, pair this note with `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` before tuning.

## Recommended order
- Measure one baseline first.
- Keep `Node` / scene-tree composition if it is still within budget.
- Reduce collision and query cost before rewriting movement or AI.
- Prefer `NavigationServer` for normal walkable worlds; use `AStarGrid2D` / `AStar3D` only for explicit grid or graph traversal.
- Promote repeated visuals or swarm density to `MultiMesh` or server APIs only when node overhead is the real bottleneck.

## Primary sources
- [Godot 2D tutorials index](https://docs.godotengine.org/en/stable/tutorials/2d/index.html)
- [Godot introduction to 3D](https://docs.godotengine.org/en/stable/tutorials/3d/introduction_to_3d.html)
- [Godot 2D navigation introduction](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_2d.html)
- [Godot 3D navigation introduction](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html)
- [Godot AStarGrid2D](https://docs.godotengine.org/en/stable/classes/class_astargrid2d.html)
- [Godot AStar3D](https://docs.godotengine.org/en/stable/classes/class_astar3d.html)
- [Godot using servers for optimization](https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html)
- [Godot MultiMesh](https://docs.godotengine.org/en/stable/classes/class_multimesh.html)
- [Godot Area2D](https://docs.godotengine.org/en/stable/classes/class_area2d.html)
- [Godot Using Area2D](https://docs.godotengine.org/en/stable/tutorials/physics/using_area_2d.html)
- [Godot BoxShape3D](https://docs.godotengine.org/en/stable/classes/class_boxshape3d.html)
- [Godot SphereShape3D](https://docs.godotengine.org/en/stable/classes/class_sphereshape3d.html)
- [Godot PhysicsShapeQueryParameters3D](https://docs.godotengine.org/en/stable/classes/class_physicsshapequeryparameters3d.html)

## Why this matters to this repo
- Every Godot gameplay task should declare the world stack up front: `2D`, `3D`, or an intentionally limited bridge. The repo should treat mixed stacks as an exception, not a default.
- Agents should not recommend custom A* first for normal movement in authored levels. If the world is continuous and surface-based, the NavigationServer-backed workflow should be the default. If the problem is tile, board, lane, or abstract graph logic, `AStarGrid2D` or `AStar3D` is the better fit.
- Damage systems in Godot should describe their contact model explicitly: authored overlap areas, physics queries, or direct body collision callbacks. For designer-facing hitboxes and hurtboxes, area signals plus collision masks are the safest baseline.
- Performance-sensitive Godot work should begin with representation choice before micro-optimization:
  - normal authored gameplay entity -> scene + nodes
  - repeated visual swarm / crowd decoration / bullet field -> `MultiMesh` or server-driven representation
  - transient queries -> direct space-state / shape query instead of persistent heavyweight node graphs when appropriate
- Checklist and routing guidance should flag scale decisions early so a feature does not silently grow from a few nodes into thousands of script-heavy objects.

## Decision impact
- Godot engine guidance should force agents to name four choices for system-heavy work:
  - world stack: `2D`, `3D`, or limited bridge
  - navigation model: nav regions/agents versus explicit A* graph or grid
  - damage routing: area signals, body collision callbacks, or direct physics queries
  - scale lever: plain nodes, `MultiMesh`, or server APIs
- The Godot engine checklist should gain explicit items for 2D/3D stack choice, navigation choice, damage routing, and high-scale representation.
- Task routing should treat `pathfinding`, `navigation`, `navmesh`, `AStar`, `damage`, `hitbox`, and `hurtbox` work as first-class gameplay system tasks so the new research note is surfaced before implementation.
- The shared perf guide at `docs/reference/perf-guide.md` should be read before micro-optimizing the slice, and the matching example at `docs/examples/perf-example.md` should be used as the agent's concrete prompt model.
