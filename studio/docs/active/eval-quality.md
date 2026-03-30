# Quality Eval

## Change under test

- `docs/reference/quality-guide.md` defines the quality rubric for code quality, maintainability, and optimization criteria.
- `docs/examples/quality-example.md` shows the same rubric in a concrete reviewable format.
- `scripts/studio_core.py` and `scripts/route_task.py` should surface that guidance when a task is quality-focused or optimization-aware.
- `studio/checklists/discipline/quality.toml` should require ownership, validation, and measured optimization criteria.

## Goal

- Make quality tasks name the ownership model before refactoring.
- Make optimization tasks state a baseline, first lever, and fallback lever before tuning code.
- Keep quality and optimization guidance visible in routing output instead of burying it in generic review language.

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| "Review code quality and optimization criteria for a Unity 6 inventory HUD before refactoring" | Tests the new quality route | Routing may stay generic | `quality-guide.md`, `quality-example.md`, and code-review guidance are surfaced |
| "Refactor a Godot combat room so ownership boundaries are explicit" | Tests ownership and maintainability language | Agent may only mention gameplay | Runtime/data/editor ownership and the quality checklist are surfaced |
| "Compare Unreal Actor, component, and data asset ownership before tuning a horde encounter" | Tests quality plus optimization criteria | Agent may jump straight to tuning | Quality guide plus perf guidance are surfaced with a clear first lever |

## Rubric

- Correctness
- Evidence quality
- Instruction compliance
- Validation honesty
- Optimization baseline visibility

## Run notes

- Date / operator / model / config
- Commands used
- Links to transcripts, screenshots, or artifacts

## Regression watchlist

- Quality routing should not become noisy or overbroad.
- Existing gameplay, bugfix, performance, and engine-routing cases should still pass.
- The quality guide should stay short enough to use during a live review pass.

## Exit criteria

- `route_task.py` and `codex_studio.py checklist` surface the quality guide and example on representative prompts.
- `studio/checklists/discipline/quality.toml` requires ownership, validation, and optimization criteria.
- Repo validation and local evals stay green.
