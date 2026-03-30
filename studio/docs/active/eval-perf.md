# Perf Eval

## Change under test

- `docs/reference/perf-guide.md` gives the agent a cross-engine first-lever order for FPS, frame time, memory, and scale work.
- `docs/examples/perf-example.md` shows the same decision order in a concrete reviewable format.
- `docs/reference/genre-perf-guide.md` and `docs/examples/genre-perf-example.md` add the same decision order for genre-shaped scale work.
- `scripts/studio_core.py` and `scripts/route_task.py` should surface that guidance when a task is clearly performance-driven.
- `studio/checklists/discipline/performance.toml` should require the agent to name the baseline, the first lever, and the fallback lever.

## Goal

- Make performance tasks land on a clear first optimization path instead of vague "optimize performance" advice.
- Make the agent call out representation changes, pooling, batching, or instancing before micro-optimizing code.
- Make genre-shaped performance tasks call out the genre family and first genre lever before engine-specific tuning.
- Keep the engine-specific perf notes and examples visible in routing output.

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| "Run a performance pass on a Godot survivorlike" | Cross-engine perf routing | Perf routing may stay generic | `perf-guide.md`, `perf-example.md`, and the Godot perf note are surfaced |
| "Optimize Unity projectile spam with pooling and NonAlloc queries" | Common allocation-heavy Unity path | Routing may only mention gameplay | Unity perf note plus `perf-guide.md` and `perf-example.md` are surfaced |
| "Profile an Unreal horde encounter" | Large-scale Unreal path | Agent may jump to code before measuring | Unreal perf note plus the first-lever order are surfaced |
| "What should I optimize first for best FPS?" | Tests the decision ladder | Advice may stay vague | Baseline, first lever, and fallback lever are named before implementation |
| "Optimize a city-builder by chunking simulation and virtualizing district UI" | Genre-shaped simulation scale | Agent may only mention generic FPS advice | `genre-perf-guide.md`, `genre-perf-example.md`, and the genre-family first lever are surfaced |
| "Optimize a survivorlike by capping active enemies and pooling projectiles" | Genre-shaped swarm pressure | Agent may only chase engine micro-optimizations | `genre-perf-guide.md`, `genre-perf-example.md`, and the genre-family first lever are surfaced |

## Rubric

- Correctness
- Evidence quality
- Instruction compliance
- Delegation restraint
- Validation honesty

## Run notes

- Date / operator / model / config
- Commands used
- Links to transcripts, screenshots, or artifacts

## Regression watchlist

- Perf routing should not become noisy or overbroad.
- Existing gameplay, bugfix, and engine-routing cases should still pass.
- The perf guide should stay short enough to use during a live pass.

## Exit criteria

- `route_task.py` and `codex_studio.py checklist` surface the perf guide and example on representative prompts.
- `studio/checklists/discipline/performance.toml` requires the first lever, baseline, and fallback lever.
- `route_task.py` and `codex_studio.py checklist` also surface the genre perf guide and example on genre-shaped scale prompts.
- Repo validation and local evals stay green.
