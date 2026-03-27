# Asset Instructions

These instructions apply under `assets/`.

## Goals
- Keep asset naming deterministic and machine-friendly.
- Preserve runtime readability and memory/perf awareness.
- Note any import, compression, or pipeline changes that affect builds.

## Conventions
- Prefer lower_snake_case names where the engine permits it.
- Avoid spaces and ambiguous suffixes.
- If a binary asset changes for a gameplay or UI reason, note the reason in docs or commit context.
