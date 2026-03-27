# Source Code Instructions

These instructions apply to runtime code and engine-facing implementation under `src/`.

## Priorities
- Favor behaviorally clear, reviewable patches.
- Respect engine-native patterns already present in the repo.
- Prefer incremental extension over broad architecture surgery.

## Minimum expectations
- Identify the exact systems/files touched before editing.
- Preserve or improve debuggability.
- Add or update tests when practical; otherwise spell out manual validation.
- Call out save, network, perf, and content-pipeline side effects explicitly.

## Avoid
- Broad refactors without direct player-facing or maintenance payoff
- Mixing architecture redesign with new gameplay in one opaque patch
- Silent magic constants without context
