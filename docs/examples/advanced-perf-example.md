# Advanced Perf Example

## Scope

- Godot 4 survivorlike swarm pass
- Unity 6 city-builder chunking pass
- Unreal 5 repeated-geometry pass

## Baseline

| Case | Baseline symptom | Repro |
| --- | --- | --- |
| Survivorlike | frame time spikes once bullet density and enemy density overlap | 6-minute arena run with high projectile churn |
| City-builder | sim tick and UI redraw cost grow together as the map fills | one district with traffic, services, and zoning pressure |
| Unreal horde / strategy | geometry and crowd density push draw cost and memory together | one large encounter or map quadrant with repeated props |

## Decision order

- confirm the algorithm family before changing code
- keep the core readability of the game intact
- prove whether culling, partitioning, batching, or job systems beat simpler pooling first
- do not escalate to a data-oriented rewrite until measurement proves it
- keep the fallback lever explicit if the first algorithm does not matter

## Likely algorithm families

- spatial partitioning and broadphase for proximity-heavy logic
- culling, LOD, and instancing for repeated visuals or hidden geometry
- job systems and data-oriented execution for uniform repeated work
- dirty-region updates and diff-based projection for large maps or campaigns
- streaming and residency control for memory or IO thrash

## Engine-shaped examples

### Godot 4

- Use `RenderingServer` and `MultiMeshInstance3D` when repeated visuals are the main cost.
- Use `OccluderInstance3D` and visibility ranges when hidden geometry is the main cost.
- Keep `NavigationServer` or explicit grid logic only if the spatial candidate set is still the issue after culling and batching.

### Unity 6

- Use `Jobs` and `Burst` when the cost is uniform repeated work across many agents or tiles.
- Use `LODGroup` and GPU occlusion culling when rendering cost is the issue.
- Keep `Entities` for cases where the scale proof shows classic object ownership is not enough.

### Unreal 5

- Use `Nanite` and `HLOD` when geometry scale and occlusion are the main cost.
- Use `Instanced Static Mesh Component` when repeated static objects dominate the scene.
- Use `Mass Gameplay` only when the agent count or uniform simulation cost clearly needs it.

## Existing repo examples to compare against

- survivorlike: cap active enemies, partition nearby targets, pool projectiles, and batch repeated visuals
- city-builder: chunk the map, update dirty regions only, and virtualize dense UI
- factory-automation: partition the production graph and batch throughput updates instead of recomputing the whole network
- grand-strategy: compress campaign state and batch event logs before broadening diplomacy logic
- stealth: cache visibility and room state before broadening patrol or perception logic
- co-op survival: tighten replication ownership and interest management before increasing actor count

## Good agent prompts

- "Research advanced optimization algorithms for a Godot survivorlike and prove whether spatial hashing or MultiMesh is the first lever."
- "For Unity, compare Burst jobs, LODGroup, and GPU occlusion culling before touching the simulation loop."
- "For Unreal, choose between HLOD, instancing, and Mass for a repeated-geometry map before raising the content budget."
- "For a stealth game, decide whether visibility caching beats any broad rewrite of patrol AI."

## Validation

- rerun the same representative spike or session
- capture baseline and after measurements
- reject changes that help perf but break readability or fairness
- if the first algorithm did not matter, name the fallback and explain why
