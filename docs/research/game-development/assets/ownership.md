# Asset Ownership

## Summary
Asset ownership answers who owns the truth: runtime object, authored data, or editor/import tool.

## Primary sources
- [Godot Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html)
- [Godot PackedScene](https://docs.godotengine.org/en/stable/classes/class_packedscene.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity AssetDatabase](https://docs.unity3d.com/6000.1/Documentation/Manual/AssetDatabase.html)
- [Unreal Data Assets](https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine)
- [Unreal Asset Management](https://dev.epicgames.com/documentation/en-us/unreal-engine/asset-management-in-unreal-engine)

## Why this matters to this repo
- This repo routes asset-heavy work through explicit ownership and import boundaries.
- The agent should not blur source art, shared tuning, runtime state, and editor tooling into one answer.
- Durable docs need a stable ownership story so asset work remains reviewable and testable.

## Decision impact
- Runtime owners should own live counters, per-run state, and interaction state.
- Authored data owners should own shared tuning and reusable defaults.
- Editor owners should own conversion, batch edits, and validation.
- The selected owner should be named before content scales.

## Runtime owner
- scene object
- prefab instance
- actor
- runtime component or service

Runtime owners keep mutable state, per-run changes, and live gameplay counters.

## Authored data owner
- Godot `Resource`
- Unity `ScriptableObject`
- Unreal Data Asset / `PrimaryDataAsset`

Authored data owners keep shared tuning, definitions, and reusable defaults.

## Editor owner
- import plugin
- inspector
- custom editor
- asset manager or validation tool

Editor owners keep batch edits, conversion, and validation out of gameplay logic.

## Boundary rules
- Shared tuning does not own live run state.
- Live run state does not own import settings.
- Editor tooling does not become gameplay authority.
- Reusable hierarchies do not silently store mutable progression.

## Common mistakes
- storing stacks, cooldowns, or lock state in shared assets
- making UI images own gameplay flags
- hard-coding asset paths when designer-facing defaults would be clearer
- collapsing source art, import settings, and runtime ownership into one script

## Validation
- Name the runtime owner.
- Name the authored-data owner.
- Name the editor owner.
- Name the first smoke test or review step.
