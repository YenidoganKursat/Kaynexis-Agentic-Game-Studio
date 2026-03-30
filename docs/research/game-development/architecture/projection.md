# Projection

## Summary
- Projection architecture maps canonical runtime state into UI, save data, telemetry, or network state.
- It answers how the game shows truth without letting the presentation layer become the truth.

## Primary sources
- Godot Resource and object architecture - https://docs.godotengine.org/en/stable/engine_details/architecture/object_class.html
- Unity ScriptableObject manual - https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html
- Unity UI Toolkit manual - https://docs.unity3d.com/6000.1/Documentation/Manual/UIElements.html
- Unreal UMG - https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-in-unreal-engine
- Unreal data assets - https://dev.epicgames.com/documentation/en-us/unreal-engine/data-assets-in-unreal-engine

## Why this matters to this repo
- The repo already separates UI, save, and runtime state in its system notes. Projection makes that separation operational.
- Projection architecture is what keeps HUDs, menus, and save files from becoming hidden logic owners.

## Decision impact
- Treat UI as a view of runtime state, not a second source of truth.
- Treat save data as a snapshot or migration target, not live gameplay state.
- Treat telemetry as a projection of outcomes, not the place where rules live.

## Common patterns
- Godot: a scene or UI layer listens to signals and projects state into Control nodes.
- Unity: a UI presenter reads runtime state and projects it into UGUI or UI Toolkit.
- Unreal: a widget projects state from GameState, PlayerState, or a view model-like bridge.

## What to watch out for
- UI should not mutate canonical state directly unless the architecture explicitly wants that.
- Save files should not accumulate runtime-only noise.
- Network state and UI state should not be treated as the same thing.

## Validation expectations
- The task should name the canonical source and each projection target.
- The implementation should prove that one projection path stays one-way.
