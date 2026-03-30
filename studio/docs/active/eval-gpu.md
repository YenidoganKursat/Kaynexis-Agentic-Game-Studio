# Eval Plan: GPU

## Goal
- Verify that GPU-heavy tasks surface the GPU guide, GPU example, and engine GPU research before implementation.

## Scope
- GPU-bound rendering tasks
- CPU-GPU communication and buffer ownership questions
- instancing, compute, culling, and repeated-visual representation choices
- agent examples for GPU decisions

## Expected behavior
- The router should surface `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` for GPU-heavy tasks.
- The checklist path should include `gpu` and `performance` when the task is about render or compute scale.
- Tasks that also mention culling, batching, instancing, or data-oriented scale should still be able to surface the advanced performance path.

## Validation
- run one route query for a GPU-heavy rendering prompt
- confirm the returned docs include the GPU guide and example
- confirm the checklist path includes the GPU discipline
- confirm the research refs include the matching engine GPU note
- re-run repo validation after routing changes

## Exit criteria
- GPU tasks are discoverable by the router
- the examples index points to the GPU example
- the engine notes cover CPU-GPU ownership, buffers, instancing, and profiling
- the routing and checklist surfaces remain stable after the new context is added

