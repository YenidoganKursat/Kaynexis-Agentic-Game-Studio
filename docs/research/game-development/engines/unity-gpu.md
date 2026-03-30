# Unity GPU

## Date
- 2026-03-29

## Summary
- Unity GPU work should stay composition-first by default and move to `GraphicsBuffer`, `ComputeShader`, or indirect instancing only when the measured bottleneck says the classic object model is the wrong scale boundary.
- For this repo, the practical default is: use `GraphicsBuffer` for data that must live in GPU-friendly buffers, `ComputeShader` for highly parallel work, and instancing / indirect draws for repeated visuals before a data-oriented rewrite.
- Unity's GPU model is strongest when CPU-owned gameplay, asset-owned tuning, and GPU-owned rendering data are kept clearly separate.

## Primary sources
- [Unity GraphicsBuffer](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/GraphicsBuffer.html)
- [Unity ComputeShader](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/ComputeShader.html)
- [Unity GPU instancing manual](https://docs.unity3d.com/6000.1/Documentation/Manual/GPUInstancing.html)
- [Unity GPU occlusion culling in URP](https://docs.unity3d.com/6000.0/Manual/urp/gpu-culling.html)
- [Unity ObjectPool<T>](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Pool.ObjectPool_1.html)

## Why this matters to this repo
- Unity tasks often become GPU-bound when repeated visuals, buffer churn, or shader cost are the real problem.
- Agents need to know whether a feature should remain on GameObjects and Components, move data into GPU-friendly buffers, or change its render representation.
- The repo should make CPU-GPU data flow explicit so that instancing, culling, and compute are chosen for the right reason instead of by habit.

## Decision impact
- Keep `GameObject` / `MonoBehaviour` composition for normal gameplay logic.
- Use `GraphicsBuffer` when the GPU needs structured data that is more naturally represented as a buffer than as many scene objects.
- Use `ComputeShader` when the work is uniform, parallel, and worth moving off the CPU.
- Use indirect instancing or GPU culling when repeated visuals dominate and the CPU should stop authoring every instance.
- Avoid readbacks unless the gameplay truly needs GPU results on the CPU.

## Core GPU ownership notes

### `GraphicsBuffer`
- Owns GPU-friendly structured data.
- Good for: instance data, geometry data, and compute buffers that need explicit low-level control.
- Watch out for: treating it as a generic gameplay model when the CPU should still own the rules.

### `ComputeShader`
- Owns GPU-side parallel compute.
- Good for: culling, expansion, transforms, simulation-like uniform work, and other parallel transforms.
- Watch out for: dispatching compute work that still waits on the CPU every frame.

### GPU instancing / indirect draw
- Owns repeated rendering of the same mesh with different transforms or parameters.
- Good for: bullet fields, prop swarms, repeated enemies, foliage, and dense repeated visuals.
- Watch out for: one GameObject per repeated object when the same mesh and material can be instanced instead.

### URP GPU occlusion culling
- Owns GPU-side visibility reduction in render-heavy scenes.
- Good for: dense scenes where visibility and draw cost are the real bottleneck.
- Watch out for: using it before the team has measured whether the frame is truly render-bound.

## CPU-GPU communication model

- Keep gameplay state on the CPU.
- Compress the render or simulation slice into the smallest useful GPU buffer.
- Choose whether the GPU writes only final visual output or whether it also produces a compact summary.
- Avoid per-frame buffer churn if the data can be updated in batches.
- Avoid per-frame GPU readback when the gameplay can accept a delayed or approximate result.

## Common mistakes to avoid

- Leaving repeated objects as separate scene instances when instancing would be the honest answer.
- Moving logic into compute shaders before proving that the CPU path is the real bottleneck.
- Using GPU buffers without a clear update cadence or ownership split.
- Mixing editor tooling and runtime code just to make GPU setup easier.

## Repo impact

- Route `gpu`, `compute`, `graphicsbuffer`, `instancing`, `drawmeshinstancedindirect`, `culling`, `readback`, and `shader` tasks here before code changes.
- Pair this note with the GPU guide, the Unity class atlas, and the Unity performance note when the task is GPU-heavy.

