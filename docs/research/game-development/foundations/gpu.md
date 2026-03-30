# GPU

## Date
- 2026-03-29

## Summary

- GPU optimization is mostly about ownership and bandwidth, not magic speed.
- The useful questions are: which work stays on the CPU, which work moves to the GPU, which data can be batched, and which data should never come back every frame.
- GPU-heavy work usually fails first because of draw-call pressure, shader cost, overdraw, upload churn, or synchronization, not because the code is "slow" in the abstract.
- This note gives the repo a durable theory layer for CPU-GPU communication, render ownership, and GPU-friendly representation choices.

## Primary sources

- Godot RenderingDevice - https://docs.godotengine.org/en/stable/classes/class_renderingdevice.html
- Godot RenderingServer - https://docs.godotengine.org/en/stable/classes/class_renderingserver.html
- Godot MultiMesh - https://docs.godotengine.org/en/stable/classes/class_multimesh.html
- Godot MultiMeshInstance3D - https://docs.godotengine.org/en/stable/classes/class_multimeshinstance3d.html
- Godot Using compute shaders - https://docs.godotengine.org/en/stable/tutorials/shaders/compute_shaders.html
- Unity GraphicsBuffer - https://docs.unity3d.com/6000.1/Documentation/ScriptReference/GraphicsBuffer.html
- Unity ComputeShader - https://docs.unity3d.com/6000.1/Documentation/ScriptReference/ComputeShader.html
- Unity GPU instancing manual - https://docs.unity3d.com/6000.1/Documentation/Manual/GPUInstancing.html
- Unity GPU occlusion culling in URP - https://docs.unity3d.com/6000.0/Manual/urp/gpu-culling.html
- Unreal Nanite Virtualized Geometry - https://dev.epicgames.com/documentation/unreal-engine/nanite-virtualized-geometry-in-unreal-engine
- Unreal Instanced Static Mesh Component - https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine
- Unreal Introduction to Performance Profiling and Configuration - https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine?application_version=5.6
- Unreal Using RenderDoc with Unreal Engine - https://dev.epicgames.com/documentation/en-us/unreal-engine/using-renderdoc-with-unreal-engine

## Why this matters to this repo

- The repo already has engine maps, performance notes, and advanced optimization notes. GPU work needs its own foundation because the CPU-GPU boundary changes how code, assets, and communication are owned.
- A game can be "too slow" because the wrong side owns the wrong work. This note helps the repo name that boundary early.
- Codex should be able to explain not only what is rendered, but who owns the data path that gets it rendered.

## Decision impact

- Prefer GPU work when the workload is uniform, repeated, or highly parallel.
- Prefer CPU ownership when the logic is branchy, simulation-heavy, or needs constant round trips back from the GPU.
- Prefer buffer-driven or instanced representation before writing a custom render path.
- Avoid per-frame readbacks unless the feature truly needs them.

## Practical framing

- **CPU owns rules.** Gameplay authority, inventory, quest logic, AI decisions, and most state transitions stay on the CPU.
- **GPU owns expansion.** Repeated visuals, culling of uniform instances, particles, post-processing, and similar parallel work are good GPU candidates.
- **Buffers are contracts.** If the GPU needs data, define the buffer shape, ownership, and update cadence explicitly.
- **Readbacks are expensive.** If the CPU needs GPU results every frame, the design may need to change.

## Communication patterns

### CPU -> GPU stream
- Best for instance data, mesh transforms, material parameters, and compute inputs.
- Prefer this when the GPU can do the same work for many objects.

### GPU -> CPU snapshot
- Best for summaries, counters, or rare queries.
- Avoid this when the CPU wants to treat the GPU like a regular branchy service.

### GPU-only loop
- Best for particles, post-processing, and other presentation-only work.
- The gameplay loop should not depend on it unless absolutely necessary.

### Double buffering / staged updates
- Best when uploads happen repeatedly but the CPU should not stall on the GPU.
- Good for indirect draws, compute-driven transforms, and stable frame pacing.

## What to watch out for

- Do not confuse "GPU code" with "fast code."
- Do not move branchy game logic to the GPU just because a shader exists.
- Do not read back every frame if a summary, a delayed readback, or a CPU-owned approximation is enough.
- Do not jump to a render rewrite before proving the bottleneck is actually render-side.

## Repo impact

- The repo should route GPU-heavy tasks to the GPU guide and engine GPU notes before tuning code.
- Future performance notes should link back to this page when they need a theory layer for CPU-GPU communication or render ownership.

