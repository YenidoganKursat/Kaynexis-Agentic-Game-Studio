# Perf Guide

Use this page when an agent needs the first, highest-value answer for FPS, frame time, memory, or scale work.

The rule is simple: measure first, name the first lever, and only then tune code.

If the bottleneck is genre-shaped instead of engine-shaped, pair this page with `docs/reference/genre-perf-guide.md` and `docs/examples/genre-perf-example.md`.
If the bottleneck is algorithmic instead of just representational, pair this page with `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md`.
If the bottleneck is GPU-side, or the real question is CPU-GPU ownership and communication, pair this page with `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md`.

## What to decide first

Before touching implementation, an agent should state:

1. target hardware and frame budget
2. the baseline measurement or reproducible spike
3. the likely bottleneck class
4. the first lever to try
5. the fallback lever if the first one does not move the needle

## Preferred order of operations

When the task is "make it faster," prefer this order:

1. fix the representation problem before micro-optimizing code
2. reduce contact, query, and allocation churn
3. pool or reuse repeated short-lived objects
4. use engine-native batching or instancing for repeated visuals
5. move to data-oriented or large-scale simulation paths only when measurement proves the need

## Engine-specific guidance

### Godot 4

Prefer:

- `Node` / scene-tree composition by default
- simple collision shapes and explicit layers/masks
- `NavigationServer` for normal authored walkable spaces
- `MultiMesh` or lower-level server APIs when repeated visuals or node overhead are the measured bottleneck
- `AStarGrid2D` / `AStar3D` only for explicit grid or graph problems

Do not prefer:

- custom A* before checking whether the world is really a walkable-surface problem
- raw `_process` scanning when a signal, query, or server-backed path is enough
- `MultiMesh` before proving that node overhead is the actual cost

### Unity 6

Prefer:

- classic `GameObject` / Component / Prefab / `ScriptableObject` composition first
- the Input System and AI Navigation before bespoke control or path systems
- `ObjectPool<T>` for repeated projectiles, hits, and effects
- `Physics.RaycastNonAlloc` and `Physics2D.OverlapCircleNonAlloc` for query-heavy features
- DOTS / Burst / Unity Physics only when the scale problem is clearly data-oriented

Do not prefer:

- `Instantiate` / `Destroy` churn in a hot loop
- per-frame allocations from sensing or combat queries
- DOTS as a default architecture choice when pooling solves the measured problem

### Unreal 5

Prefer:

- `AActor` / `UActorComponent` / Data Asset / Blueprint ownership first
- navmesh, EQS, and StateTree before custom AI plumbing
- collision channels and simple damage flow before overbuilt combat frameworks
- instancing for repeated visuals before turning every repeated object into a full Actor
- GAS or Mass only when ability complexity or entity count is truly the problem

Do not prefer:

- Actor-per-entity scale when repeated visuals or swarms could be instanced
- custom graph code when navmesh or EQS already fits the world model
- GAS before the feature actually needs attributes, effects, or reusable ability flow

## When the lever is algorithmic

If the real issue is culling, partitioning, batching, instancing, job systems, or state compression, stop and choose the algorithm family before you tune low-level code.
Use `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` when the question is "which algorithm shape should own this scale problem?"

## Example scenarios

- Godot: a survivorlike or bullet-hell slice should ask whether node count or repeated visuals are the bottleneck before jumping to server APIs or MultiMesh.
- Unity: a projectile-heavy room shooter should pool projectiles and use NonAlloc queries before considering DOTS.
- Unreal: a horde encounter should separate navmesh, decision flow, and representation before escalating to instancing or Mass.

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Optimize a Godot survivorlike by reducing node count before considering MultiMesh"
python3 scripts/codex_studio.py next "Optimize Unity projectile spam with pooling and NonAlloc queries before DOTS"
python3 scripts/codex_studio.py next "Optimize an Unreal horde encounter by choosing between Actor, instancing, and Mass"
```

## Validation

When the agent is done, it should report:

- the baseline
- the first lever tried
- the before and after measurement
- the reason the chosen path beat the alternatives

## Related docs

- `docs/examples/perf-example.md`
- `docs/reference/genre-perf-guide.md`
- `docs/reference/advanced-perf-guide.md`
- `docs/reference/gpu-guide.md`
- `docs/examples/genre-perf-example.md`
- `docs/examples/advanced-perf-example.md`
- `docs/examples/gpu-example.md`
- `docs/research/game-development/engines/godot-performance.md`
- `docs/research/game-development/engines/unity-performance.md`
- `docs/research/game-development/engines/unreal-performance.md`
- `docs/research/game-development/engines/README.md`
- `docs/reference/agent-guide.md`
