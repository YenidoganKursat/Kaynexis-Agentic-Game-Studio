# Perf Algorithms

## Date
- 2026-03-29

## Summary

- Advanced performance work is usually about shrinking the amount of work, not merely making the same work faster.
- The most useful families are spatial partitioning, visibility reduction, batching and instancing, job systems, dirty-region updates, and state compression.
- A game can feel slow because it is doing too much work per frame, because it is asking the wrong questions per frame, or because it is recomputing whole-world state when only a local slice changed.
- This note turns those algorithmic choices into a durable research layer for the repo.

## Primary sources

- Godot internal rendering architecture - https://docs.godotengine.org/en/stable/contributing/development/core_and_modules/internal_rendering_architecture.html
- Godot RenderingServer - https://docs.godotengine.org/en/stable/classes/class_renderingserver.html
- Godot MultiMeshInstance3D - https://docs.godotengine.org/en/stable/classes/class_multimeshinstance3d.html
- Unity GPU occlusion culling in URP - https://docs.unity3d.com/ja/6000.0/Manual/urp/gpu-culling.html
- Unity LOD Group reference - https://docs.unity3d.com/jp/current/Manual/class-LODGroup.html
- Unity Burst - https://docs.unity3d.com/ja/current/Manual/script-compilation-burst.html
- Unity Jobs - https://docs.unity3d.com/es/2019.4/Manual/com.unity.jobs.html
- Unity Entities - https://docs.unity3d.com/cn/2019.4/Manual/com.unity.entities.html
- Unreal Nanite Virtualized Geometry - https://dev.epicgames.com/documentation/unreal-engine/nanite-virtualized-geometry-in-unreal-engine
- Unreal HLOD overview - https://dev.epicgames.com/documentation/pt-br/unreal-engine/hierarchical-level-of-detail-overview-in-unreal-engine
- Unreal Mass Gameplay overview - https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-mass-gameplay-in-unreal-engine
- Unreal Instanced Static Mesh Component - https://dev.epicgames.com/documentation/es-mx/unreal-engine/instanced-static-mesh-component-in-unreal-engine

## Why this matters to this repo

- The repo supports multiple engines and multiple genres, so "performance" cannot stay at the level of generic FPS advice.
- The same game shape may need a different algorithm family in different engines, even if the player-facing goal is identical.
- Codex needs a theory layer that tells it when to choose partitioning, culling, batching, jobs, or compressed state before it starts changing code.

## Decision impact

- Feature briefs should name the algorithm family before implementation.
- Perf tasks should record the baseline, the candidate set size, the visible set size, the update rate, or the state size that makes the algorithm necessary.
- Checklists should ask whether the bottleneck is spatial lookup, visibility, uniform batch work, or whole-world recomputation.

## Practical framing

- Use spatial partitioning when the candidate set is too large.
- Use culling, LOD, or instancing when visible work is too large.
- Use Burst, Jobs, Entities, or Mass when the same work repeats across many entities.
- Use dirty-region updates and state compression when a world or campaign should not be recomputed wholesale.
- Use streaming or residency control when memory or IO thrash is the real issue.

## What to watch out for

- Do not adopt an advanced algorithm because it sounds modern.
- Do not trade debugging clarity for scale unless measurement says the current model is the problem.
- Many "performance" failures are actually representation failures or state ownership failures.
- If the team cannot explain the algorithm family in one sentence, it probably is not ready to ship yet.

## Repo impact

- The repo should route advanced optimization tasks to `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md`.
- Existing engine performance notes remain the first stop for basic FPS work; this note is the deeper algorithm layer above them.
- Future performance or genre research notes should link back to this page when they need the durable theory layer.
