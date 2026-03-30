# Save

## Date
- 2026-03-27

## Summary
- Save architecture goes wrong when teams fail to separate session state, durable player progression, and authored content data. Engines provide different storage surfaces, but the architectural split is consistent across them.
- Godot's saving guidance uses groups and line-by-line serialized dictionaries to persist selected runtime objects, while autoloads and the scene tree often hold cross-scene state during play. Unity's serialization system and `ScriptableObject` assets make a strong distinction between authored data and runtime state, and the Inspector itself is built on serialized fields. Unreal's `USaveGame` workflow separates saved data from the currently active world objects, while the gameplay framework distinguishes world state from player state and rule ownership.
- Good save architecture names at least three classes of data:
  - authored data that ships with the build
  - runtime state for the current session or run
  - persistent save data that survives process restarts
- This also affects progression design. Meta progression, unlocked content, and profile options should not live in the same mutation path as per-run temporary combat state just because both are "player data."

## Primary sources
- [Godot saving games](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html)
- [Godot singletons (autoload)](https://docs.godotengine.org/en/4.0/tutorials/scripting/singletons_autoload.html)
- [Godot autoloads versus regular nodes](https://docs.godotengine.org/en/4.3/tutorials/best_practices/autoloads_versus_internal_nodes.html)
- [Unity script serialization](https://docs.unity3d.com/kr/6000.0/Manual/script-serialization.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity prefabs introduction](https://docs.unity3d.com/6000.1/Documentation/Manual/prefabs-introduction.html)
- [Unreal saving and loading your game](https://dev.epicgames.com/documentation/es-es/unreal-engine/saving-and-loading-your-game-in-unreal-engine)
- [Unreal Engine terminology](https://dev.epicgames.com/documentation/en-us/unreal-engine/unreal-engine-terminology)
- [AGameStateBase](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AGameStateBase)

## Why this matters to this repo
- Features that touch persistence, progression, or profile state should explicitly classify every field they introduce:
  - authored immutable content
  - run/session mutable state
  - durable save/profile data
- Agents should avoid treating globally reachable runtime objects as if they are the save format. Autoloads, scene managers, singleton components, or gameplay framework objects may own live state, but they should not automatically become the long-term persistence boundary.
- The repo's active docs should keep progression and save architecture visible early, especially if the game grows from a single run-based prototype into a roguelite with meta unlocks.

## Decision impact
- Save and progression recommendations should always explain where the source of truth lives during play and where it is serialized for persistence.
- Future save-system and metaprogression templates should include a mandatory split between authored data, run state, and durable save state.
- Risk reviews should treat "unclear persistence boundary" as a production risk because it affects migrations, debugging, and content authoring.
