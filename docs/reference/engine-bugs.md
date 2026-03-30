# Engine Bugs Guide

## Summary

Use this guide when the user wants the most common bug families and first checks for Godot 4, Unity 6, or Unreal 5.
It is the bug atlas for recurring engine errors, not a single bug report.
If the task already has one reproducible bug, use the bugfix bundle instead and keep this page as the classification map.

## Primary sources

- Godot troubleshooting: <https://docs.godotengine.org/en/stable/tutorials/troubleshooting.html>
- Godot debugger panel: <https://docs.godotengine.org/en/stable/tutorials/scripting/debug/debugger_panel.html>
- Godot warning system: <https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/warning_system.html>
- Unity Null Reference Exception: <https://docs.unity3d.com/kr/2018.3/Manual/NullReferenceException.html>
- Unity script execution order: <https://docs.unity3d.com/kr/6000.0/Manual/script-execution-order.html>
- Unity prefab overrides: <https://docs.unity3d.com/jp/current/Manual/prefabs-override.html>
- Unity Addressables: <https://docs.unity3d.com/kr/6000.0/Manual/com.unity.addressables.html>
- Unreal actor lifecycle: <https://dev.epicgames.com/documentation/unreal-engine/unreal-engine-actor-lifecycle>
- Unreal logging: <https://dev.epicgames.com/documentation/en-us/unreal-engine/logging-in-unreal-engine>
- Unreal live coding: <https://dev.epicgames.com/documentation/en-us/unreal-engine/using-live-coding-to-recompile-unreal-engine-applications-at-runtime?application_version=5.6>
- Unreal garbage collection: <https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/CoreUObject/UObject/FGCObjectInfo>

## Why this matters to this repo

- Engine bugs are easier to route when the agent can name the symptom family before it edits anything.
- The most common failures in this repo are ownership bugs, lifecycle bugs, serialization bugs, packaging bugs, and debugging-surface blind spots.
- A shared bug atlas keeps bug reports, crash triage, and troubleshooting notes from becoming a pile of one-off anecdotes.

## Decision impact

- Use this guide when the task is about recurring engine bug families or common errors.
- Use `studio/docs/templates/bug-report.md` and `studio/docs/templates/crash-triage.md` when the task is a concrete bug with a repro.
- The first question should be "which engine surface is failing?" not "what patch feels clever?"
- Separate runtime, editor, and packaged-build behavior before proposing a fix.

## Bug family map

| Family | What it usually looks like | First check |
| --- | --- | --- |
| ownership / missing reference | null reference, missing node, destroyed object, stale pointer | Inspect the owning scene, prefab, or UObject and verify the reference is still valid at the time of use |
| lifecycle / execution order | first-frame bugs, order-dependent state, race-like behavior, callbacks firing before initialization | Check the engine lifecycle hooks and make the execution order explicit |
| serialization / asset boundary | data disappears after save, rename, copy, reload, or prefab/scene edit | Check whether the data belongs to authored data, runtime state, or persistence |
| packaging / build / cook / export | works in editor but fails in build or export | Compare editor behavior with packaged behavior and inspect the build logs |
| debug-surface blind spots | the bug is real but there is no stack trace, console output, or debugger clue | Capture the right log, debugger, or profiler surface before changing code |
| network / authority / sync | one client sees the wrong state, desync, ghost state, or replay mismatch | Check authority ownership, replication boundaries, and sync timing |
| performance / stutter / memory | spikes, GC churn, editor hitching, or device-specific slowdown | Measure first and identify whether the issue is CPU, GPU, GC, or asset-bound |

## Godot 4 bug families

Most recurring Godot issues in this repo fall into a few buckets:

- signal wiring or disconnect mistakes
- node-path assumptions that stop being true after scene edits
- resource-versus-scene ownership confusion
- warnings that were visible but not treated as blockers
- export or startup issues that only appear outside the editor
- editor slowdown caused by a heavy redraw path or a noisy viewport

First checks:

- open the Debugger panel and inspect the Stack Trace tab
- read the GDScript warning system output when the project compiles but still behaves oddly
- use the Troubleshooting page when the problem is editor-startup, export, or platform specific
- verify whether the failing state belongs in a `Node`, a `Scene`, or a `Resource`

## Unity 6 bug families

Most recurring Unity issues in this repo fall into a few buckets:

- `NullReferenceException` from unassigned, destroyed, or moved serialized references
- prefab override drift after scene or variant edits
- script execution order assumptions that only fail in some builds or on some machines
- `Addressables` or asset-loading assumptions that differ from direct scene references
- serialization issues where the Inspector shows one thing but runtime state uses another

First checks:

- open the Console and follow the first meaningful stack trace line
- decide whether the reference is a scene reference, prefab reference, or runtime lookup
- inspect script execution order if the bug changes with startup timing or scene load order
- check prefab instance overrides if the bug appears after prefab edits or nested prefab changes
- compare Addressables loading against direct references before changing the gameplay code

## Unreal 5 bug families

Most recurring Unreal issues in this repo fall into a few buckets:

- `UObject` lifetime and garbage collection mistakes
- `AActor` lifecycle bugs, especially around `BeginPlay`, `EndPlay`, and `Destroy`
- Blueprint compile or Live Coding issues that look like gameplay bugs but are really iteration-path bugs
- cook, package, or build failures that only appear outside the editor
- log blindness, where the Output Log would have shown the root cause much earlier

First checks:

- open the Output Log and capture the first warning or error that actually explains the failure
- verify whether the state lives on a `UObject`, `AActor`, `UActorComponent`, or transient runtime copy
- compare editor, PIE, and packaged behavior before editing the gameplay logic
- use Live Coding for iteration, but remember that constructor defaults and existing instances do not always refresh the way you expect
- inspect garbage-collection assumptions when an object disappears or becomes invalid unexpectedly

## First checks by symptom

| Symptom | Likely family | First check |
| --- | --- | --- |
| null, missing, or destroyed reference | ownership / missing reference | verify the owner and lifetime of the object or asset |
| only breaks after a scene reload or level transition | lifecycle / execution order | inspect load, init, and teardown hooks |
| only breaks in build or export | packaging / build / cook / export | inspect packaged logs and compare editor vs build behavior |
| only breaks after a rename or prefab edit | serialization / asset boundary | inspect prefab, scene, or resource overrides |
| only breaks on one device or platform | performance / platform / toolchain | check runtime logs and platform-specific constraints |
| only breaks with multiplayer or multiple clients | network / authority / sync | inspect authority, replication, and timing assumptions |

## Example prompts for the agent

- "Summarize the most common bug families for Godot 4, Unity 6, and Unreal 5 and tell me the first check for each."
- "Turn this vague engine bug into a troubleshooting map before we patch anything."
- "Classify the bug as ownership, lifecycle, serialization, packaging, or networking and then point me at the right starting docs."
- "Show me the engine-specific debug surface I should inspect first for this crash."

## Validation

A good engine-bugs pass should leave behind:

- one bug family map
- one engine-specific first-check list
- one source-backed research note
- one checklist that keeps the classification path narrow
- one eval plan that proves the lane routes cleanly
- one bugfix bundle if the task becomes a concrete repro

## Related docs

- `docs/examples/engine-bugs-example.md`
- `docs/research/game-development/foundations/engine-bugs.md`
- `studio/checklists/discipline/engine_bugs.toml`
- `studio/docs/active/eval-engine-bugs.md`
- `docs/reference/bugfix` templates in `studio/docs/templates/`
- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/system-atlas.md`
- `docs/reference/agent-guide.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
