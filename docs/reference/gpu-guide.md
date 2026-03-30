# GPU Guide

## Summary
- Use this page when the question is not just "how do we make it faster?" but "where should the work live: CPU, GPU, or a shared communication boundary?"
- Good GPU decisions name the bottleneck, the ownership split, the data path, the profiler, and the first lever before implementation.
- The repo should prefer the smallest GPU change that proves value: better representation, fewer uploads, fewer readbacks, or a clearer CPU-GPU contract before a deeper render rewrite.

## Primary sources
- [Godot RenderingDevice](https://docs.godotengine.org/en/stable/classes/class_renderingdevice.html)
- [Godot RenderingServer](https://docs.godotengine.org/en/stable/classes/class_renderingserver.html)
- [Godot MultiMesh](https://docs.godotengine.org/en/stable/classes/class_multimesh.html)
- [Godot MultiMeshInstance3D](https://docs.godotengine.org/en/stable/classes/class_multimeshinstance3d.html)
- [Godot Using compute shaders](https://docs.godotengine.org/en/stable/tutorials/shaders/compute_shaders.html)
- [Godot Using servers for optimization](https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html)
- [Unity GraphicsBuffer](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/GraphicsBuffer.html)
- [Unity ComputeShader](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/ComputeShader.html)
- [Unity GPU instancing manual](https://docs.unity3d.com/6000.1/Documentation/Manual/GPUInstancing.html)
- [Unity GPU occlusion culling in URP](https://docs.unity3d.com/6000.0/Manual/urp/gpu-culling.html)
- [Unreal Nanite Virtualized Geometry](https://dev.epicgames.com/documentation/unreal-engine/nanite-virtualized-geometry-in-unreal-engine)
- [Unreal Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Unreal Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine?application_version=5.6)
- [Unreal Using RenderDoc with Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-renderdoc-with-unreal-engine)
- [Unreal Designing Visuals, Rendering, and Graphics](https://dev.epicgames.com/documentation/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine)

## Why this matters to this repo
- GPU work in games is often a representation problem, a bandwidth problem, or a synchronization problem before it is a low-level code problem.
- The repo already has engine maps, performance guides, asset rules, and advanced optimization notes. GPU work needs a dedicated guide so agents can say whether a feature should stay on the CPU, move to the GPU, or split the boundary cleanly.
- Agents should be able to explain the CPU-GPU contract without burying it inside generic performance advice.

## Decision impact
- GPU-heavy tasks should state the CPU owner, the GPU owner, the upload path, the readback policy, and the profiler path before implementation.
- If the feature is mostly repeated visuals or uniform transforms, prefer instancing, batching, or buffer-driven rendering before changing game logic.
- If the feature needs compute-style work, prefer a GPU path only when the data flow is coherent and the CPU does not need the result back every frame.
- If the GPU is already the bottleneck, the next lever may be content reduction, shader simplification, or culling instead of a deeper communication rewrite.

## GPU decision model

1. Measure a baseline with a CPU/GPU breakdown.
2. Name whether the task is CPU-bound, GPU-bound, or mixed.
3. Choose the smallest ownership split that fits the data.
4. Minimize uploads, state changes, and readbacks.
5. Escalate to instancing, indirect draws, culling, compute, or a render-graph style path only if the baseline proves it is worth it.

## CPU-GPU communication patterns

### CPU owns simulation, GPU owns presentation
- Use this for repeated visuals, shader-driven presentation, particles, and large batches of the same mesh or effect.
- Keep gameplay authority on the CPU and send only the final visual or instance data the GPU needs.

### CPU streams a buffer, GPU expands work
- Use this when a `GraphicsBuffer`, storage buffer, or render buffer can carry the per-instance data the GPU needs.
- Good fit for crowds, bullet fields, indirect draws, and GPU-side culling.

### GPU computes, CPU only reads summaries
- Use this when the GPU is doing large uniform work and the CPU only needs a coarse result.
- Avoid per-frame readbacks unless the gameplay really depends on them.

### GPU work stays fully GPU-side
- Use this for particles, post-processing, repeated rendering, and similar presentation-only effects.
- Do not turn those systems into gameplay state owners by accident.

## Engine anchors

| Engine | Best default GPU owner | Good first lever | Watch out |
| --- | --- | --- | --- |
| Godot 4 | `RenderingServer`, `RenderingDevice`, `MultiMesh`, `MultiMeshInstance3D` | repeated visuals, compute shaders, server-backed batching | forcing a scene-tree solution to own a render-scaling problem |
| Unity 6 | `GraphicsBuffer`, `ComputeShader`, instanced indirect draw | buffer-driven rendering, GPU culling, instancing | per-frame `GameObject` churn or readback-heavy designs |
| Unreal 5 | Instanced Static Meshes, Nanite, HLOD, profiling tools | repeated geometry, virtualized detail, render profiling | Actor-per-instance scale when a render-side representation would work better |

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Research the GPU communication path for a Godot 4 survivorlike and decide whether MultiMesh or RenderingDevice is the first lever"
python3 scripts/codex_studio.py next "Compare Unity GraphicsBuffer, ComputeShader, and DrawMeshInstancedIndirect for a dense projectile field before changing gameplay logic"
python3 scripts/codex_studio.py next "Choose between Unreal Instanced Static Meshes, Nanite, and HLOD for repeated world objects before scaling Actor count"
python3 scripts/codex_studio.py next "Design a CPU-GPU data flow that avoids per-frame readbacks in a shader-heavy combat slice"
```

## Validation

When the agent is done, it should report:

- the baseline
- whether the bottleneck was CPU-bound, GPU-bound, or mixed
- the chosen ownership split
- the first lever tried
- the readback policy
- the before and after measurement
- the next lever if the first one does not hold

## Related docs

- `docs/reference/perf-guide.md`
- `docs/reference/advanced-perf-guide.md`
- `docs/examples/perf-example.md`
- `docs/examples/advanced-perf-example.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/engine-examples.md`
- `docs/research/game-development/engines/godot-gpu.md`
- `docs/research/game-development/engines/unity-gpu.md`
- `docs/research/game-development/engines/unreal-gpu.md`
