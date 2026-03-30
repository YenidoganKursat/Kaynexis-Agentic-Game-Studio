# Engine Bugs Guide

## Date

2026-03-30

## Summary

Most recurring engine bugs come from ownership boundaries, lifecycle order, serialization drift, packaging or cook differences, and weak debug visibility.
This note keeps the bug atlas source-backed so the agent can classify the symptom before it starts patching.

## Primary sources

- Godot troubleshooting: <https://docs.godotengine.org/en/stable/tutorials/troubleshooting.html>
- Godot debugger panel: <https://docs.godotengine.org/en/stable/tutorials/scripting/debug/debugger_panel.html>
- Godot warning system: <https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/warning_system.html>
- Unity NullReferenceException: <https://docs.unity3d.com/kr/2018.3/Manual/NullReferenceException.html>
- Unity script execution order: <https://docs.unity3d.com/kr/6000.0/Manual/script-execution-order.html>
- Unity prefab overrides: <https://docs.unity3d.com/jp/current/Manual/prefabs-override.html>
- Unity Addressables: <https://docs.unity3d.com/kr/6000.0/Manual/com.unity.addressables.html>
- Unreal actor lifecycle: <https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-actor-lifecycle>
- Unreal logging: <https://dev.epicgames.com/documentation/en-us/unreal-engine/logging-in-unreal-engine>
- Unreal live coding: <https://dev.epicgames.com/documentation/en-us/unreal-engine/using-live-coding-to-recompile-unreal-engine-applications-at-runtime?application_version=5.6>
- Unreal garbage collection: <https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/FGCObjectInfo>

## Why this matters to this repo

- Bug triage is faster when the agent can classify the symptom into a common engine family before it edits code.
- The repo already separates runtime ownership, authored data, editor tooling, and validation paths; the bug atlas should mirror those boundaries.
- A bug atlas helps keep crash triage, repro notes, and bugfix bundles reviewable later.

## Decision impact

- Use this note when the task is about recurring engine bug families or common errors.
- Use bugfix templates when the task already has a concrete repro path.
- Separate editor-only, runtime-only, and packaged-build-only failures before choosing a fix.
- Capture the debug surface first, then decide whether the bug is actually an ownership, lifecycle, serialization, packaging, or networking problem.

## Bug family map

| Family | Core failure mode | Best first check |
| --- | --- | --- |
| ownership / missing reference | the object, node, or asset is gone or never owned the data | inspect the owner and lifetime boundary |
| lifecycle / execution order | the code runs before initialization or after teardown | inspect the engine lifecycle hook order |
| serialization / asset boundary | data changes in the editor but not in runtime or after reload | inspect scene, prefab, resource, or UObject persistence |
| packaging / build / export | editor behavior differs from packaged behavior | inspect build logs and packaged runtime logs |
| debug-surface blindness | the symptom is visible, but the log, debugger, or profiler is not being used | capture the output, debugger, or profiler surface before changing code |
| network / authority / sync | clients disagree or state diverges | inspect authority and replication boundaries |
| performance / stutter / memory | frame spikes, GC churn, or device-specific slowdown | measure first and classify the bottleneck |

## Godot 4 bug families

### Common bug families

- signal wiring mistakes
- node-path drift after scene edits
- scene versus resource ownership confusion
- warnings that could have prevented the bug
- export or startup issues that only appear outside the editor
- editor slowdown caused by redraw-heavy nodes or large viewports

### First checks

- open the Debugger panel and read the Stack Trace tab
- inspect the warning system before assuming the logic is correct
- use the Troubleshooting page for startup, export, or platform-specific behavior
- verify whether the responsibility belongs in a `Node`, a `Scene`, or a `Resource`

### Repo impact

Most Godot bugs in this repo become easier to fix once the owner boundary is explicit.

## Unity 6 bug families

### Common bug families

- `NullReferenceException` from unassigned, destroyed, or moved references
- prefab override drift after nested prefab or variant edits
- script execution order assumptions
- `Addressables` and direct-reference loading mismatches
- serialization issues where the Inspector and runtime disagree

### First checks

- open the Console and follow the first useful stack trace line
- inspect script execution order when the bug changes with startup timing
- inspect prefab overrides when the bug appears after prefab edits
- compare `Addressables` loading with direct references before changing the gameplay logic

### Repo impact

Many Unity bugs in this repo are really ownership or serialization bugs wearing an exception message.

## Unreal 5 bug families

### Common bug families

- `UObject` lifetime and garbage-collection mistakes
- `AActor` lifecycle bugs around `BeginPlay`, `EndPlay`, and `Destroy`
- Blueprint compile or Live Coding issues that look like gameplay bugs
- cook, package, or build failures that only appear outside the editor
- log blindness when the Output Log would have shown the root cause sooner

### First checks

- open the Output Log first
- compare editor, PIE, and packaged behavior before editing gameplay logic
- inspect `UObject` ownership and lifetime when values disappear or become invalid
- use Live Coding for iteration, but do not assume constructor defaults refresh existing instances

### Repo impact

Many Unreal bugs in this repo are lifecycle or packaging issues, not core gameplay logic failures.

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

## Repo impact

- Bug reports should name the engine, the failing surface, and the likely bug family.
- A bugfix bundle should include one deterministic repro or one failure surface that would pass after the fix.
- If the task turns out to be a recurring bug family rather than a single repro, keep it in the engine-bugs lane.

## Related docs

- `docs/reference/engine-bugs.md`
- `docs/examples/engine-bugs-example.md`
- `studio/checklists/discipline/engine_bugs.toml`
- `studio/docs/active/eval-engine-bugs.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/system-atlas.md`
- `docs/reference/agent-guide.md`
- `docs/reference/task-prompt-examples.md`
- `docs/reference/workflow-recipes.md`
- `studio/docs/templates/bug-report.md`
- `studio/docs/templates/crash-triage.md`
