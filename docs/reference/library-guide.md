# Library Guide

Use this guide when the real question is not "how do I package or ship this?" but "which built-in API, official package, module, plugin, or SDK should own this case?"

The rule is simple: prefer the smallest official stack that solves the case, then prove the need for anything heavier.

## Summary

- This guide helps the agent choose the smallest useful library or package surface for common game cases.
- It exists because input, UI, navigation, persistence, networking, presentation, and scale problems do not need the same dependency shape.
- The repo should not default to third-party libraries or data-oriented packages before the built-in or official stack is proven insufficient.

## Primary sources

- [Godot InputEventAction](https://docs.godotengine.org/en/stable/classes/class_inputeventaction.html)
- [Godot NavigationServer2D](https://docs.godotengine.org/en/stable/classes/class_navigationserver2d.html)
- [Godot Navigation overview](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_2d.html)
- [Godot EditorPlugin](https://docs.godotengine.org/en/stable/classes/class_editorplugin.html)
- [Godot ConfigFile](https://docs.godotengine.org/en/stable/classes/class_configfile.html)
- [Godot MultiplayerAPIExtension](https://docs.godotengine.org/en/stable/classes/class_multiplayerapiextension.html)
- [Unity Input manual](https://docs.unity3d.com/kr/6000.0/Manual/Input.html)
- [Unity Input System installation](https://docs.unity3d.com/ja/Packages/com.unity.inputsystem%401.4/manual/Installation.html)
- [Unity AI Navigation package](https://docs.unity3d.com/ja/current/Manual/com.unity.ai.navigation.html)
- [Unity UI Toolkit](https://docs.unity3d.com/2023.2/Documentation/Manual/UIElements.html)
- [Unity Entities package](https://docs.unity3d.com/es/2019.3/Manual/com.unity.entities.html)
- [Unity Burst package](https://docs.unity3d.com/ja/Packages/com.unity.burst%401.8/manual/editor-burst-menu.html)
- [Unity TextMesh Pro package](https://docs.unity3d.com/ja/Packages/com.unity.textmeshpro%403.0/manual/index.html)
- [Unreal Enhanced Input](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/PluginIndex/EnhancedInput)
- [Unreal UMG](https://dev.epicgames.com/documentation/en-us/fortnite/umg)
- [Unreal UMG optimization guidelines](https://dev.epicgames.com/documentation/en-us/unreal-engine/optimization-guidelines-for-umg-in-unreal-engine)
- [Unreal CommonUI input fundamentals](https://dev.epicgames.com/documentation/zh-cn/unreal-engine/input-fundamentals-for-commonui-in-unreal-engine)
- [Unreal Niagara quick start](https://dev.epicgames.com/documentation/en-us/unreal-engine/quick-start-for-niagara-effects-in-unreal-engine?application_version=5.6)
- [Unreal MassGameplay overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-mass-gameplay-in-unreal-engine)
- [Unreal Gameplay Abilities](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-gameplay-abilities-in-unreal-engine)

## Why this matters to this repo

- Library choice changes ownership boundaries, validation cost, and release risk.
- If the agent picks the wrong package first, it often creates a larger dependency surface than the feature needed.
- The repo needs a guide that tells the agent when to use built-in APIs, when to use an official package, and when to stop before adding more.

## Decision impact

- Library tasks should name the case before implementation.
- The first choice should be the smallest official stack that fits the case.
- Third-party libraries should only enter the repo when the built-in or official stack cannot satisfy the requirement.

## How to use this guide

1. Identify the case.
2. Decide whether the answer should be built-in, official package, plugin, or SDK.
3. Name the smallest stack that can validate the slice.
4. Keep the fallback path explicit if the library choice turns out to be unnecessary.
5. Record the choice in the active docs if the dependency becomes part of the durable architecture.

## Case map

| Case | Godot 4 default | Unity 6 default | Unreal 5 default | What to watch first |
|---|---|---|---|---|
| Input and remapping | `InputMap`, `InputEventAction`, `Control` focus navigation | Input System package | Enhanced Input, then CommonUI if controller-first UI matters | action naming, remap persistence, UI focus |
| UI, HUD, and menus | `Control`, `CanvasLayer`, theme resources | UI Toolkit for new UI, uGUI/TMP when legacy overlay or world-space is the better fit | UMG, with CommonUI when controller-heavy flows need stronger UX contract | state churn, event-driven updates, layout invalidation |
| Navigation and pathfinding | `NavigationServer2D/3D`, `NavigationAgent2D/3D`, `AStarGrid2D/3D` | AI Navigation package | Navigation System / NavMesh, then EQS or StateTree if the decision layer grows | path cost, world representation, agent ownership |
| Camera and framing | `Camera2D`, `Camera3D`, `Tween` or scene-owned rigs | Cinemachine, or a simple camera rig if the slice is small | camera component, spring arm, or gameplay camera system as needed | feel, motion smoothing, follow rules |
| Save and persistence | `ConfigFile`, `Resource`, `FileAccess` | serialization helpers, `JsonUtility`, `ScriptableObject` for authored data | `SaveGame`, `GameInstance`, Data Assets | migration, corruption recovery, durable vs runtime ownership |
| Networking and multiplayer | `MultiplayerAPI`, `MultiplayerAPIExtension`, peer backends when required | Netcode for GameObjects + Unity Transport | built-in replication, OnlineSubsystem, and only then higher-level framework pieces | authority, relevancy, sync frequency |
| VFX and animation | `AnimationPlayer`, `AnimationTree`, `GPUParticles2D/3D` | Particle System, VFX Graph, TextMesh Pro for combat text | Niagara | readability, update cost, layout invalidation, spawn churn |
| Scale and performance | `MultiMesh`, server APIs, then GDExtension only if the measured bottleneck proves it | ObjectPool<T>, Burst, Entities, Physics | Instanced Static Mesh, Mass, GAS only when the project truly needs them | representation choice, batching, memory pressure |
| Editor and tooling | `EditorPlugin`, `@tool`, custom inspectors | `EditorWindow`, custom inspectors, editor scripts | Editor Utility Widgets, plugins, Details panel extensions | workflow cost, recovery path, editor/runtime boundary |

## Selection rules

- Default to built-in first.
- Prefer official packages or engine modules before third-party dependencies.
- Do not add DOTS, Mass, GAS, or other large-scale frameworks unless the measurement proves that the simpler stack is not enough.
- If the case is only a small slice, keep the library surface as small as possible.
- If the library changes the durable architecture, record the decision in the active docs.

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Choose the smallest official library set for a Unity 6 inventory HUD and controller remap flow"
python3 scripts/codex_studio.py next "Choose the smallest built-in or official stack for a Godot 4 stealth prototype with input, navigation, and save"
python3 scripts/codex_studio.py next "Choose the smallest package or plugin set for an Unreal 5 co-op combat slice with UI, input, and VFX"
python3 scripts/codex_studio.py next "Recommend the official navigation and UI stack for a city-builder before adding any third-party dependency"
```

## Validation

When the agent is done, it should report:

- the case
- the smallest chosen stack
- what built-in option was rejected and why
- what official package or plugin was adopted and why
- the validation path that proves the choice was enough

## Related docs

- `docs/examples/library-example.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-selection-guide.md`
- `docs/reference/engine-examples.md`
- `docs/reference/perf-guide.md`
- `docs/reference/genre-perf-guide.md`
- `docs/research/game-development/README.md`
- `docs/research/game-development/engines/README.md`
- `docs/research/game-development/systems/input.md`
- `docs/research/game-development/systems/ui.md`
- `docs/research/game-development/systems/navigation.md`
- `docs/research/game-development/systems/save.md`
