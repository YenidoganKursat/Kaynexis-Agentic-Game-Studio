# Events

## Summary
- Event architecture separates what happened from who reacts to it.
- It is useful when combat, UI, audio, telemetry, quests, and saves all need the same signal without directly depending on one another.

## Primary sources
- Godot signals - https://docs.godotengine.org/en/stable/classes/class_signal.html
- Godot Object class architecture - https://docs.godotengine.org/en/stable/engine_details/architecture/object_class.html
- Unity execution order - https://docs.unity3d.com/6000.1/Documentation/Manual/ExecutionOrder.html
- Unity ScriptableObject manual - https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html
- Unreal Gameplay Ability System - https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine

## Why this matters to this repo
- The repo already routes tasks by system ownership. Event architecture keeps those systems decoupled after the task is implemented.
- Good event design avoids hidden dependencies and makes QA and telemetry easier to add later.

## Decision impact
- Use events for notification and orchestration, not for hiding ownership.
- Name payloads and event owners explicitly.
- Document whether the event is local-only, scene-wide, or crosses a save/network boundary.

## Common patterns
- Godot: signals from nodes or resources, with one owner deciding whether the signal is just a notification or a gameplay trigger.
- Unity: explicit event channels or dispatcher services where runtime data is projected into UI, audio, or telemetry.
- Unreal: gameplay tags, delegates, or ability events tied to a clear authority owner.

## What to watch out for
- Event buses can become invisible spaghetti if nobody can say who owns the source.
- Do not replace state ownership with an event stream.
- Do not let UI subscribe to raw gameplay internals if a projection layer would be safer.

## Validation expectations
- The task should name the event source, the listener set, and the failure case.
- The implementation should prove one event path with a small smoke or test.
