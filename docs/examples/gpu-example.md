# GPU Example

## Scope
- a GPU-heavy slice where repeated visuals, compute work, or buffer-driven rendering matters more than another gameplay refactor

## Baseline
- target hardware: a mid-range PC or the slowest shipped platform
- measure the current frame time split, draw-call pressure, upload churn, and any readback cost
- record whether the feature is CPU-bound, GPU-bound, or mixed before tuning

## Decision order

1. name the CPU owner and the GPU owner
2. decide whether the data should be streamed, instanced, computed, or just rendered normally
3. reduce uploads, draw calls, and readbacks before touching shader micro-details
4. only escalate to a deeper render path if the baseline proves the smaller lever was not enough

## Engine-shaped examples

### Godot 4
- Use `RenderingServer` or `RenderingDevice` when the scene tree is not the right scale boundary.
- Use `MultiMesh` / `MultiMeshInstance3D` for many repeated visuals before inventing a custom per-node swarm.
- Keep gameplay state on the CPU; send only the render or compute data the GPU needs.

### Unity 6
- Use `GraphicsBuffer` for buffer-driven geometry or compute data.
- Use `ComputeShader` when the work is uniform and parallel enough to justify GPU execution.
- Use instanced indirect drawing for repeated visuals before moving the whole slice to a data-oriented rewrite.

### Unreal 5
- Use instanced static meshes for repeated geometry before increasing Actor count.
- Use Nanite or HLOD when the world is mainly a rendering scale problem.
- Use profiling tools first so the team knows whether the renderer, the content, or the representation is the bottleneck.

## Good agent prompts

- "Research a GPU communication model for a Godot 4 bullet field and decide whether `MultiMesh` or `RenderingDevice` should own the first pass."
- "Compare Unity `GraphicsBuffer`, `ComputeShader`, and indirect instancing for a city-builder prop field before changing gameplay code."
- "Decide whether an Unreal crowd scene should stay Actor-based or move to instancing, Nanite, or HLOD."
- "Design a CPU-to-GPU upload path that keeps the simulation on the CPU but moves repeated visuals to the GPU."

## Validation

- one before measurement
- one chosen ownership split
- one GPU profiling or capture path
- one explicit readback policy
- one explanation for why the chosen GPU path beat the alternatives

