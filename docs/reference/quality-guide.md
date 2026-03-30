# Quality Guide

Use this page when the task is about code quality, maintainability, reviewability, or optimization criteria before implementation.

If you need the operating loop instead of only the rubric, pair this page with `docs/reference/quality-process.md` and `docs/examples/quality-process-example.md`.

The rule is simple: name the ownership model, name the validation path, and only then decide whether optimization is actually required.

## Summary

- This guide gives Codex a concrete quality rubric instead of vague "clean it up" advice.
- It exists because code quality, optimization criteria, and refactor safety are related but not the same thing.
- The repo should not treat readability, ownership, testability, and performance proof as separate afterthoughts.

## Primary sources

- [Godot code style guidelines](https://docs.godotengine.org/en/stable/community/contributing/code_style_guidelines.html)
- [Godot using servers for optimization](https://docs.godotengine.org/en/stable/tutorials/performance/using_servers.html)
- [Unity scripting optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/scripting-optimization.html)
- [Unity physics optimization](https://docs.unity3d.com/6000.0/Documentation/Manual/physics-optimization.html)
- [Unreal C++ coding standard](https://dev.epicgames.com/documentation/en-us/unreal-engine/epic-cplusplus-coding-standard-for-unreal-engine)
- [Unreal UMG optimization guidelines](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine)

## Why this matters to this repo

- The repo already routes features, research, performance, and library selection. Quality work needs the same explicit treatment so refactors do not turn into untracked architecture changes.
- Without a quality guide, an agent can call something "maintainable" without naming the owner, the test path, or the first optimization lever.
- This guide keeps code review, naming, refactoring, and optimization criteria in one readable place so the agent can reason from evidence instead of vibes.
- The process doc keeps the control loop, evidence path, and go/no-go gate in one place so the quality rubric does not drift away from actual execution.

## Decision impact

- Quality tasks should state the runtime owner, shared data owner, editor owner, and validation path before implementation.
- If optimization is in scope, the task should also state the baseline, the first lever, and the fallback lever before tuning begins.
- When a change would alter durable behavior, the matching active doc, traceability note, or example should be updated in the same change.
- For quality-control work, the review bundle should also name the process step, the evidence artifact, and the go/no-go decision that will be used.

## Quality control process

Use `docs/reference/quality-process.md` when the work needs an explicit control loop instead of only a rubric. That page turns quality work into a repeatable sequence: frame the change, name ownership, choose proof, gather evidence, decide whether optimization belongs, and keep the docs globally aligned.

## Quality criteria

### Ownership
- The runtime owner is explicit.
- The reusable data owner is explicit.
- The editor-facing owner is explicit.
- No single object owns runtime, data, UI, and tooling unless the engine contract genuinely requires it.

### Readability
- Names are short, canonical, and obvious.
- Control flow is easy to follow without hidden side effects.
- Public surfaces say what they own and what they do not own.

### Testability
- One narrow validation path exists for the change.
- The agent can name the test, smoke, or manual loop that proves the work.
- Failing cases are observable instead of hidden behind implicit state.

### Refactor safety
- The change is reversible in small steps.
- The docs that describe the behavior change with the code.
- The review bundle is concrete enough that another operator can continue the work.

## Optimization criteria

Optimization is part of quality only when it is justified by measurement.

Prefer this order:

1. Capture a baseline or reproducible symptom.
2. Remove unnecessary work before changing architecture.
3. Reduce allocations, queries, invalidations, or contact churn.
4. Pool or reuse repeated short-lived objects.
5. Batch, instance, cache, or chunk repeated work.
6. Escalate to data-oriented, server, or large-scale systems only when measurement proves the need.

When the task is already about large-scale optimization, read:

- `docs/reference/perf-guide.md`
- `docs/reference/genre-perf-guide.md`
- `docs/reference/advanced-perf-guide.md`

If the task is about GPU ownership, render-side representation, buffer shape, or CPU-GPU communication, pair this page with:

- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`

## Engine-specific criteria

### Godot 4
- Keep scene ownership, `Resource` ownership, and editor-tool ownership separate.
- Use typed variables and explicit scene/resource boundaries when the ownership line matters.
- Use `@tool` only when the editor must react live.
- Treat server APIs and `MultiMesh` as measured scale choices, not default cleanup tools.

### Unity 6
- Keep `GameObject`, `MonoBehaviour`, `ScriptableObject`, and editor-only code in their proper lanes.
- Prefer prefabs and shared data assets before creating bespoke state containers.
- Avoid allocation churn in hot paths.
- Use `NonAlloc` queries, pooling, and official packages before reaching for DOTS or Burst.

### Unreal 5
- Keep `AActor`, `UActorComponent`, `UObject`, and Data Asset ownership clear.
- Prefer Blueprint or Details-panel tuning when the task is designer-facing.
- Keep C++ readable and consistent with the engine coding standard.
- Use instancing, Mass, or GAS only when the scale or authority problem is proven.

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Review code quality and optimization criteria for a Unity 6 inventory HUD before refactoring"
python3 scripts/codex_studio.py next "Refactor a Godot combat room so runtime ownership, data ownership, and optimization criteria are explicit"
python3 scripts/codex_studio.py next "Compare Unreal Actor, component, and data asset ownership before tuning a horde encounter"
python3 scripts/codex_studio.py next "Do not optimize until the baseline and first lever are named for this Godot system pass"
```

## Validation

When the agent is done, it should report:

- the ownership model
- the quality-control process step used
- the validation path
- the baseline, if optimization was part of the task
- the first lever and fallback lever, if optimization was part of the task
- the reason the chosen path beat the alternatives

## Related docs

- `docs/reference/quality-process.md`
- `docs/examples/quality-process-example.md`
- `docs/examples/quality-example.md`
- `docs/reference/code-review.md`
- `docs/reference/perf-guide.md`
- `docs/reference/genre-perf-guide.md`
- `docs/reference/advanced-perf-guide.md`
- `docs/reference/gpu-guide.md`
- `docs/examples/gpu-example.md`
- `docs/reference/engine-map.md`
- `docs/reference/system-atlas.md`
- `docs/reference/agent-guide.md`
- `docs/research/game-development/foundations/quality.md`
