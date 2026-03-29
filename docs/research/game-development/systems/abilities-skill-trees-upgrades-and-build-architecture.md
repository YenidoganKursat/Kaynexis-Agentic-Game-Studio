# Abilities, Skill Trees, Upgrades, and Build Architecture

## Date
- 2026-03-27

## Summary
- Ability and upgrade systems scale better when they distinguish between:
  - authored ability or upgrade definitions
  - runtime grants and unlock state
  - temporary run-specific modifiers
  - durable meta progression
  - UI projection of choices and cooldowns
- Short-run upgrade systems, long-term skill trees, and permanently equipped passives are related but not identical. They should not all mutate the same data path by accident.
- Engine-native data models matter here. Godot often benefits from `Resource`-backed ability or upgrade definitions plus script-owned runtime state. Unity often benefits from `ScriptableObject` definitions plus runtime wrappers, state machines, and explicit UI projection. Unreal already offers a high-end ability stack in GAS when the feature set grows systemic, but simpler games may stay on bespoke components and Data Assets for a while.
- Upgrade systems become brittle when:
  - temporary run upgrades are saved like permanent profile unlocks
  - cooldown state lives in authored assets
  - the ability trigger path is mixed with UI choice logic
  - combat math, presentation, and progression all mutate the same objects
- A healthy ability or upgrade design should state:
  - definition data location
  - grant/unlock authority
  - runtime cooldown or charge owner
  - stacking rules
  - persistence boundary
  - validation path

## Primary sources
- [Godot Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html)
- [Godot AnimationTree](https://docs.godotengine.org/en/stable/classes/class_animationtree.html)
- [Godot saving games](https://docs.godotengine.org/en/stable/tutorials/io/saving_games.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity animation state machines](https://docs.unity3d.com/6000.1/Documentation/Manual/AnimationStateMachines.html)
- [Unity StateMachineBehaviour](https://docs.unity3d.com/6000.1/Documentation/Manual/StateMachineBehaviours.html)
- [Unreal Gameplay Ability System](https://dev.epicgames.com/documentation/unreal-engine/gameplay-ability-system-for-unreal-engine)
- [Using Gameplay Abilities in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-gameplay-abilities-in-unreal-engine)
- [Unreal UPrimaryDataAsset](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/Engine/UPrimaryDataAsset)
- [Saving and Loading Your Game in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/saving-and-loading-your-game-in-unreal-engine)

## Why this matters to this repo
- Tasks mentioning skill tree, upgrade, perk, passive, active ability, cooldown, build variety, or meta unlock should no longer be treated as generic gameplay notes. They are a junction between combat, save architecture, UI, and content data.
- Agents should explicitly say:
  - what is authored data
  - what is current-run mutable state
  - what is permanent progression
  - who applies the effect
  - who shows it in UI
- This repo already treats research as durable design memory. Abilities and upgrades are one of the easiest places for systems to become tangled if the repo does not keep those boundaries explicit.

## Decision impact
- Route and checklist output should surface this note for tasks mentioning abilities, upgrades, skill trees, perks, passives, boons, cooldowns, meta unlocks, or build variety.
- Future combat, progression, and UI docs should classify every ability-related field as authored, run-state, or durable state.
