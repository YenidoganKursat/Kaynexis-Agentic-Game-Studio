# Godot GPU

## Date
- 2026-03-29

## Summary
- Godot GPU work should stay scene-tree-first by default and move to `RenderingServer`, `RenderingDevice`, or `MultiMesh` only when the measured bottleneck says the scene tree is the wrong scale boundary.
- For this repo, the practical default is: use `RenderingServer` for render-side control and `RenderingDevice` for lower-level compute or buffer work; use `MultiMesh` / `MultiMeshInstance3D` when repeated visuals become the real problem.
- Godot's compute-shader flow is explicit about the CPU-GPU boundary: data is prepared on the CPU, uploaded to a buffer, executed on the GPU, and only read back when the feature really needs a result.

## Primary sources
- [Godot RenderingServer](https://docs.godotengine.org/en/stable/classes/class_renderingserver.html)
- [Godot RenderingDevice](https://docs.godotengine.org/en/stable/classes/class_renderingdevice.html)
- [Godot MultiMesh](https://docs.godotengine.org/en/stable/classes/class_multimesh.html)
- [Godot MultiMeshInstance3D](https://docs.godotengine.org/en/stable/classes/class_multimeshinstance3d.html)
- [Godot Using compute shaders](https://docs.godotengine.org/en/stable/tutorials/shaders/compute_shaders.html)
- [Godot Using servers for optimization](https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html)
- [Godot Variable rate shading](https://docs.godotengine.org/en/stable/tutorials/3d/variable_rate_shading.html)

## Why this matters to this repo
- Godot slices can become GPU-bound either because the scene tree is too heavy or because the visual workload is too dense for per-node composition.
- Agents need a stable answer to "stay on the scene tree, move to MultiMesh, or go lower-level with RenderingServer/RenderingDevice" before they start rewriting code.
- The repo should keep gameplay authority separate from render ownership, especially when compute shaders or render-side batching enter the picture.

## Decision impact
- Use `Node` / scene-tree composition for normal gameplay objects.
- Use `MultiMesh` / `MultiMeshInstance3D` for large repeated visual counts.
- Use `RenderingServer` when the render-side API is the right ownership boundary.
- Use `RenderingDevice` when compute shaders, low-level buffers, or more direct GPU control are the right fit.
- Avoid CPU→GPU→CPU round-trips unless the feature really needs the feedback.

## Core GPU ownership notes

### `RenderingServer`
- Owns the render-side API backend for visible content.
- Good for: bypassing the scene tree when render-side control or optimization is the real bottleneck.
- Watch out for: using it when the GPU is already the bottleneck and the problem is really content weight or shader cost.

### `RenderingDevice`
- Owns lower-level access to modern graphics APIs and compute-shader style work.
- Good for: GPU compute, buffer-driven work, advanced render control, and separate-thread GPU tasks.
- Watch out for: using it before the team can explain the buffer shape, synchronization, and readback policy.

### `MultiMesh` / `MultiMeshInstance3D`
- Owns repeated rendering for many instances of the same mesh.
- Good for: trees, grass, debris, bullet fields, repeated props, large repeated visuals.
- Watch out for: trying to use it as a general gameplay owner; it is a render-scale representation, not a gameplay framework.

### `Shader` / `ShaderMaterial`
- Owns visual and effect behavior at the material level.
- Good for: material-driven GPU behavior, screen effects, and small compute-adjacent visual logic.
- Watch out for: hiding gameplay truth only in shader state.

## CPU-GPU communication model

- Prepare data on the CPU as a shared authored resource, packed array, or instance list.
- Upload the smallest useful slice to the GPU.
- Dispatch compute or render work on the GPU.
- Avoid `sync()` / readback unless the feature genuinely needs the result on the CPU.
- If the data is changing every frame, ask whether a `MultiMesh` or a render-side representation would shrink the problem first.

## Common mistakes to avoid

- Replacing normal node-based gameplay with `RenderingDevice` because it sounds advanced.
- Using one node per repeated visual when `MultiMesh` would be the honest answer.
- Creating GPU compute work that immediately waits on CPU readback.
- Mixing gameplay authority into render-side helpers.

## Repo impact

- Route `gpu`, `compute`, `shader`, `rendering`, `buffer`, `readback`, and `instancing` tasks here before code changes.
- Pair this note with the GPU guide, the Godot performance note, and the engine atlas when the task is GPU-heavy.

