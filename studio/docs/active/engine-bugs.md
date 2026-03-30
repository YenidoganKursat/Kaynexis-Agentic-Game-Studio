# Engine Bugs Guide

## Summary

Active notes for recurring engine bug families, first checks, and debug surfaces.

## Primary sources

- `docs/reference/engine-bugs.md`
- `docs/examples/engine-bugs-example.md`
- `docs/research/game-development/foundations/engine-bugs.md`

## Why this matters to this repo

- Keep Godot, Unity, and Unreal bug families easy to classify before patching.
- Keep the first debug surface explicit.
- Separate editor-only, runtime-only, and packaged-build-only failures.

## Decision impact

- Use the bug atlas before proposing a fix.
- Switch to a bugfix bundle only after the bug family and debug surface are named.
- Keep the review trail attached to one deterministic repro or failing surface.

## Bug family map

- ownership / missing reference
- lifecycle / execution order
- serialization / asset boundary
- packaging / build / export
- debug-surface blindness
- network / authority / sync
- performance / stutter / memory

## Godot 4 bug families

- signal wiring mistakes
- node-path drift after scene edits
- scene versus resource ownership confusion

## Unity 6 bug families

- `NullReferenceException` from unassigned, destroyed, or moved references
- prefab override drift after nested prefab or variant edits
- script execution order assumptions

## Unreal 5 bug families

- `UObject` lifetime and garbage-collection mistakes
- `AActor` lifecycle bugs around `BeginPlay`, `EndPlay`, and `Destroy`
- Blueprint compile or Live Coding issues that look like gameplay bugs

## First checks by symptom

- open the Debugger panel or Output Log first
- compare editor, PIE, and packaged behavior before editing gameplay logic
- inspect ownership and lifetime boundaries when values disappear or become invalid

## Example prompts for the agent

- "Classify recurring Godot signal and node-path bugs before patching anything."
- "Separate Unity null reference and prefab override bugs from generic crash fixes before editing code."
- "Tell me the first debug surface for a packaged Unreal failure before deciding on a fix."

## Validation

- Confirm the engine family first.
- Name the likely bug family before proposing a patch.
- Separate editor-only, runtime-only, and packaged-build-only behavior.
- Capture one deterministic repro or one failing surface that should pass after the fix.

## Related docs

- `studio/checklists/discipline/engine_bugs.toml`
- `studio/docs/active/eval-engine-bugs.md`
- `docs/reference/repo-tour.md`
- `docs/reference/agent-guide.md`
- `docs/reference/workflow-recipes.md`
