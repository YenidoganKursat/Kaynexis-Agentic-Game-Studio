# Genre Perf Example

## Scope

- Survivorlike wave spike, city-builder sim tick, and factory throughput pass

## Baseline

| Genre | Baseline symptom | Repro |
| --- | --- | --- |
| Survivorlike | Avg frame time spikes to 30 ms when enemy count reaches 800 | 6-minute arena run with projectile-heavy upgrade path |
| City-builder | Sim tick jumps above budget when a district crosses 40k agents | One district with traffic, service coverage, and zoning pressure |
| Factory-automation | Throughput falls behind once conveyor graphs get dense | One production chain with long belt loops and multiple machine hops |
| Grand-strategy | UI stalls when campaign state and event logs get large | One realm turn with diplomacy, policy, and event churn |

## Decision order

- Confirm whether the bottleneck is entity count, simulation tick cost, state churn, or UI projection cost.
- Keep the genre's core readability intact while you tune.
- Reduce the genre's dominant cost before touching low-level engine code.
- Only escalate to engine-native batching, instancing, or data-oriented systems when the measurement proves the need.

## Likely bottlenecks

- Survivorlike: projectile churn, pickup spam, contact cost, and visual clutter
- City-builder: dirty-region updates, pathing, and city-scale UI redraws
- Factory-automation: conveyor graph cost, throughput tracing, and broad simulation ticks
- Grand-strategy: campaign-state size, event batching, and map/UI redraw pressure
- Co-op survival: replication overhead, authority confusion, and pooled network events

## Engine-shaped examples

### Godot 4

- Survivorlike: keep the room on `Node` / `CharacterBody2D`, pool projectiles, and move repeated visuals to `MultiMesh` only after node overhead is proven.
- City-builder: prefer chunked `Resource`-backed state and update only dirty regions before adding more navigation or graph logic.
- Factory-automation: keep throughput tracing separate from presentation, and use server APIs only if the scale proves the scene tree is the bottleneck.

### Unity 6

- Survivorlike: keep combat on `GameObject` / `MonoBehaviour` / `Prefab`, pool bullets and pickups, and use `NonAlloc` queries before DOTS.
- City-builder: virtualize dense UI panels and chunk simulation state before spreading logic across more scripts.
- Factory-automation: profile update frequency and cache the production graph before increasing machine count or switching to DOTS.

### Unreal 5

- Survivorlike: keep the arena on `AActor` / `UActorComponent`, pool repeated effects, and use instancing before moving to Mass.
- City-builder: compress campaign state and batch UI updates before broadening the simulation framework.
- Factory-automation: keep the production graph readable in Blueprint or component form before escalating to larger-scale systems.

## Smallest high-impact fixes

- cap active enemies or agents before increasing the spawn budget
- pool repeated projectiles, pickups, or effects
- chunk simulation or update only dirty regions
- virtualize dense UI before adding more detail
- compress or diff state before expanding branching content

## Good agent prompts

- "Run a performance pass on a survivorlike and prove whether projectile churn or enemy density is the bottleneck."
- "Run a performance pass on a city-builder and chunk simulation before adding more AI detail."
- "Run a performance pass on a factory-automation game and trace throughput bottlenecks before increasing machine count."
- "Run a performance pass on a grand-strategy game and compress campaign state before adding more diplomacy."
- "Run a performance pass on a co-op survival game and tighten replication ownership before changing combat."
- "Run a performance pass on a stealth game and cache visibility before adding patrol complexity."

## Validation

- Re-run the same genre-specific spike or session.
- Capture baseline and after measurements.
- Reject changes that improve perf but break readability, fairness, or recovery.
- If the first lever did not matter, name the fallback lever and explain why.

If the genre lever still does not move the needle and the bottleneck is really culling, partitioning, batching, or job systems, switch to `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` before rewriting the whole architecture.
