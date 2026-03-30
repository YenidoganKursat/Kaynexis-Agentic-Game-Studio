# Advanced Perf Guide

Use this page when the optimization problem is no longer just "reduce waste" but "choose the right algorithmic shape for scale."

The rule is simple: measure first, name the algorithm family, and then pick the smallest lever that can prove or disprove the bottleneck.

If the task is genre-shaped, read `docs/reference/genre-perf-guide.md` first. If it is engine-shaped, read `docs/reference/perf-guide.md` first. Use this guide when the remaining question is culling, partitioning, batching, instancing, job systems, or state compression.
If the task is GPU-shaped instead of algorithm-shaped, pair this page with `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` before implementation.

## Summary

- This guide turns advanced optimization choices into a readable order of operations.
- It exists because the repo supports large-scale swarm, sim, strategy, stealth, and co-op shapes that often fail first for structural reasons.
- The repo should not jump to ECS, Mass, Nanite, Burst, or another large-scale system before the algorithmic bottleneck is named.

## Primary sources

- [Godot Internal rendering architecture](https://docs.godotengine.org/en/stable/contributing/development/core_and_modules/internal_rendering_architecture.html)
- [Godot RenderingServer](https://docs.godotengine.org/en/stable/classes/class_renderingserver.html)
- [Godot MultiMeshInstance3D](https://docs.godotengine.org/en/stable/classes/class_multimeshinstance3d.html)
- [Unity GPU occlusion culling in URP](https://docs.unity3d.com/ja/6000.0/Manual/urp/gpu-culling.html)
- [Unity LOD Group reference](https://docs.unity3d.com/jp/current/Manual/class-LODGroup.html)
- [Unity Burst](https://docs.unity3d.com/ja/current/Manual/script-compilation-burst.html)
- [Unity Jobs](https://docs.unity3d.com/es/2019.4/Manual/com.unity.jobs.html)
- [Unity Entities](https://docs.unity3d.com/cn/2019.4/Manual/com.unity.entities.html)
- [Unreal Nanite Virtualized Geometry](https://dev.epicgames.com/documentation/unreal-engine/nanite-virtualized-geometry-in-unreal-engine)
- [Unreal HLOD overview](https://dev.epicgames.com/documentation/pt-br/unreal-engine/hierarchical-level-of-detail-overview-in-unreal-engine)
- [Unreal Mass Gameplay overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-mass-gameplay-in-unreal-engine)
- [Unreal Instanced Static Mesh Component](https://dev.epicgames.com/documentation/es-mx/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Unreal UMG optimization guidelines](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine)

## Why this matters to this repo

- The repo already knows how to route engine choice, genre shape, and library choice. Advanced optimization needs the same treatment for spatial partitioning, culling, batching, and large-scale simulation.
- Many "performance" bugs are actually algorithm-selection bugs. A game can be fast in one representation and slow in another even before low-level tuning begins.
- Codex should be able to say which algorithm family it is choosing, why that family beats the alternatives, and what it would try next if the measurement disagrees.

## Decision impact

- Feature briefs should identify the algorithm family before implementation.
- Advanced optimization tasks should state the baseline, the entity or world count, the expected scale pressure, and the first algorithmic lever.
- Checklists should ask whether the true bottleneck is spatial lookup, visibility, batching, update frequency, state projection, or data-oriented execution.

## How to use this guide

1. Identify the scale problem.
2. Name the algorithm family.
3. Pick the smallest lever that can prove or disprove the bottleneck.
4. Keep readability, fairness, and recovery intact while tuning.
5. Escalate to engine-native batching, instancing, job systems, or data-oriented paths only if measurement proves the need.

## Algorithm families

### Spatial partitioning and broadphase

Use when many objects or agents are spending time in the same query space.

Examples:

- uniform grids
- spatial hashes
- quadtrees
- octrees
- BVH-style candidate reduction
- sweep and prune broadphase

Prefer:

- smaller candidate sets
- dirty-region updates
- query-local work instead of whole-world scans

Avoid:

- a full data-oriented rewrite when a narrower candidate set solves the real cost
- global recomputation when only a local slice changes

### Culling, LOD, and instancing

Use when rendering cost, draw calls, or occluded geometry dominate the frame.

Examples:

- frustum culling
- occlusion culling
- LOD / HLOD
- instancing
- batching
- Nanite-style high-count geometry handling

Prefer:

- representation that keeps visible work proportional to what the camera can actually see
- repeated-visual aggregation before per-object simulation

Avoid:

- manual object-per-object scale when the scene is mostly repeated shapes
- enabling a large-scale rendering system before proving that draw cost is the real bottleneck

### Job systems and data-oriented execution

Use when the same work repeats across many objects and the update is structurally uniform.

Examples:

- Unity Jobs
- Unity Burst
- Unity Entities
- Unreal Mass Gameplay
- lower-level server or rendering APIs when the scene tree or actor model is the measured bottleneck

Prefer:

- uniform batch work
- explicit data layout
- measurable work splitting

Avoid:

- moving to a data-oriented stack just because it is fashionable
- changing the entire game architecture when pooling, batching, or culling already solve the measured issue

### Dirty-region updates and state compression

Use when the world or campaign is too large to recompute wholesale.

Examples:

- dirty-region simulation
- diff-based state projection
- delta compression
- batched event logs
- interest management

Prefer:

- partial recomputation
- snapshot projection only for the data that changed
- compressed state for UI, save, replication, or campaign views

Avoid:

- full redraws of a world map or city when only a district changed
- pushing every state change through a single monolithic update loop

### Streaming and residency control

Use when memory, IO, or residency thrash becomes the bottleneck.

Examples:

- chunk streaming
- async loading
- visibility range control
- asset residency windows
- streaming pools or derived data caches

Prefer:

- the smallest loaded set that still supports the current view
- predictable streaming windows

Avoid:

- loading the whole world when only a room, district, or encounter is active

## Engine anchors

| Family | Godot 4 anchor | Unity 6 anchor | Unreal 5 anchor |
| --- | --- | --- | --- |
| Spatial partitioning | `NavigationServer`, `AStarGrid2D` / `AStar3D`, `RenderingServer` queries | Jobs plus custom grids or broadphase helpers | navmesh, custom query grids, or Mass when the scale proof exists |
| Culling and LOD | `MultiMeshInstance3D`, `OccluderInstance3D`, visibility range | LOD Group, GPU occlusion culling, instancing | Nanite, HLOD, Instanced Static Mesh Component |
| Data-oriented execution | lower-level server APIs when the scene tree is the bottleneck | Jobs, Burst, Entities | Mass Gameplay |
| Dirty-region / diff state | `Resource` / `ConfigFile` projections, scene-local updates | diffed runtime state, virtualized UI, serialization helpers | compressed campaign state, batched UI, Blueprint/C++ split |
| Streaming / residency | render server and resource boundaries | loading and residency windows, asset bundles or addressable-style patterns | Nanite streaming, HLOD, content chunking, async loading |

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Research advanced optimization algorithms for a Godot 4 survivorlike and decide whether spatial hashing, MultiMesh, or occlusion culling is the first lever"
python3 scripts/codex_studio.py next "Compare Unity Burst jobs, GPU occlusion culling, and LODGroup for a dense city-builder before rewriting simulation code"
python3 scripts/codex_studio.py next "Choose between Unreal HLOD, Instanced Static Meshes, and Mass for a grand-strategy map before increasing world detail"
python3 scripts/codex_studio.py next "For a co-op survival game, compare interest management, replication grouping, and chunked state updates before increasing actor count"
```

## Validation

When the agent is done, it should report:

- the baseline
- the algorithm family chosen
- the first lever tried
- the before and after measurement
- the fallback if the first lever did not move the needle
- why the chosen algorithm beat the alternatives

## Related docs

- `docs/reference/perf-guide.md`
- `docs/reference/gpu-guide.md`
- `docs/reference/genre-perf-guide.md`
- `docs/examples/perf-example.md`
- `docs/examples/gpu-example.md`
- `docs/examples/genre-perf-example.md`
- `docs/examples/advanced-perf-example.md`
- `docs/research/game-development/foundations/perf-algorithms.md`
- `docs/research/game-development/engines/godot-performance.md`
- `docs/research/game-development/engines/unity-performance.md`
- `docs/research/game-development/engines/unreal-performance.md`
- `docs/reference/agent-guide.md`
