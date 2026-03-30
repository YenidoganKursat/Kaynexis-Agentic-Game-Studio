# Unreal GPU

## Date
- 2026-03-29

## Summary
- Unreal GPU work should keep gameplay ownership on gameplay classes and use the renderer's own scale tools for repeated geometry, visibility reduction, and profiling before the project invents a parallel system.
- For this repo, the practical default is: profile first with Unreal's GPU tools, use instancing or Nanite for repeated geometry, and only escalate into deeper render-side work when the measurement proves it.
- Unreal's render scale choices are often representation choices: Actor-per-thing, instanced mesh, HLOD, or Nanite-supported geometry are not equivalent.

## Primary sources
- [Unreal Introduction to Performance Profiling and Configuration](https://dev.epicgames.com/documentation/en-us/unreal-engine/introduction-to-performance-profiling-and-configuration-in-unreal-engine?application_version=5.6)
- [Unreal Using RenderDoc with Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-renderdoc-with-unreal-engine)
- [Unreal Designing Visuals, Rendering, and Graphics](https://dev.epicgames.com/documentation/unreal-engine/designing-visuals-rendering-and-graphics-with-unreal-engine)
- [Unreal Nanite Virtualized Geometry](https://dev.epicgames.com/documentation/unreal-engine/nanite-virtualized-geometry-in-unreal-engine)
- [Unreal Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Unreal HLOD overview](https://dev.epicgames.com/documentation/pt-br/unreal-engine/hierarchical-level-of-detail-overview-in-unreal-engine)

## Why this matters to this repo
- Unreal slices often become GPU-heavy because repeated geometry, visibility, and material cost grow faster than the gameplay code.
- Agents need a stable way to choose between Actor scale, instancing, HLOD, Nanite, or a deeper renderer-driven optimization path.
- GPU-bound work in Unreal should not be handled as a generic gameplay task; it needs a render-side representation decision and a proof path.

## Decision impact
- Keep gameplay rules in Actors, Components, and gameplay systems.
- Use instancing when the same static mesh repeats many times.
- Use HLOD or Nanite when visibility or virtualized geometry is the real scale question.
- Use RenderDoc and GPU profiling before changing architecture.
- Avoid Actor-per-instance scale when the render representation could be more compact.

## Core GPU ownership notes

### Instanced Static Mesh Component
- Owns repeated mesh rendering with shared material and collision properties.
- Good for: repeated props, foliage, groups of the same mesh, and other repeated visuals.
- Watch out for: turning every repeated object into a separate Actor when one instanced representation would do the job.

### Nanite
- Owns high-count geometry representation and virtualized detail.
- Good for: detail-heavy meshes, high object counts, and scenes where traditional draw-call thinking is no longer the right boundary.
- Watch out for: assuming Nanite replaces the need to think about the rest of the render budget.

### HLOD
- Owns larger-scale visibility and representation reduction.
- Good for: world-scale scenes, distant aggregation, and content that does not need full per-object fidelity at every distance.
- Watch out for: using it when the scene is not actually large enough to need it.

### GPU profiling tools
- Owns proof of where the GPU time is going.
- Good for: separating renderer cost, scene cost, and content cost before tuning code.
- Watch out for: shipping a GPU optimization without a capture or timing path.

## CPU-GPU communication model

- Keep gameplay and state mutation on the game thread and gameplay classes.
- Let the renderer own repeated geometry and visibility reduction.
- Prefer batch-friendly representation over per-instance scripting where possible.
- Use GPU captures and profiling to prove the chosen representation actually improved the frame.

## Common mistakes to avoid

- Using one Actor per repeated mesh when instancing or Nanite would be the honest answer.
- Treating GPU profiling as optional once the scene "looks fine."
- Building custom render behavior before measuring the renderer's built-in options.
- Moving gameplay authority into the rendering layer just because the visual work is heavy.

## Repo impact

- Route `gpu`, `renderdoc`, `stat gpu`, `nanite`, `hlod`, `instancing`, `rendering`, `visibility`, and `draw call` tasks here before code changes.
- Pair this note with the GPU guide, the Unreal class atlas, and the Unreal performance note when the task is GPU-heavy.

