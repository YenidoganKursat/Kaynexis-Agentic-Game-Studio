# Authority

## Summary
- Authority architecture decides who owns the canonical truth for gameplay state, and who only projects or observes that state.
- This is the first question for boss phases, combat rules, save/progression boundaries, replication, and any system that can otherwise turn into a shared-mutable-state tangle.

## Primary sources
- Godot Object class architecture - https://docs.godotengine.org/en/stable/engine_details/architecture/object_class.html
- Godot autoloads - https://docs.godotengine.org/en/stable/tutorials/best_practices/autoloads.html
- Unity ScriptableObject manual - https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html
- Unreal gameplay framework - https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine
- Unreal StateTree - https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine

## Why this matters to this repo
- The repo already separates runtime, data, editor, and UI in its class atlases. Authority extends that idea to gameplay behavior.
- If authority is vague, every other system becomes harder to test, harder to save, and harder to scale.

## Decision impact
- Define a single owner for canonical state before building the rest of the slice.
- Keep UI, animation, and content data as projections unless they truly own the truth.
- If multiple systems can mutate the same data, write down the conflict rule before implementation.

## Common patterns
- Godot: an autoload or dedicated authority node owns canonical state, while scene nodes listen through signals.
- Unity: a runtime service or scene coordinator owns state, while ScriptableObjects hold shared authored data and UI reads projections.
- Unreal: GameMode, GameState, PlayerState, or a dedicated subsystem owns the truth depending on network scope.

## What to watch out for
- Do not let UI decide rules.
- Do not let animation own logic unless the game explicitly wants that as the truth source.
- Do not split authority across too many scripts just to reduce one file size.

## Validation expectations
- The task should name the owner, the boundary, and the failure case.
- The implementation should prove the canonical state path with one narrow smoke or test.
