# Character Controller, Ability, and State Architecture

## Date
- 2026-03-27

## Summary
- Character architecture is healthier when it treats the player avatar as a collaboration between several layers instead of one giant controller script or class:
  - input interpretation
  - locomotion and physical movement
  - combat or ability execution
  - animation and presentation
  - camera and targeting
  - stats, equipment, and persistence projection
- Engine-native character stacks differ in shape, but the same architectural split matters everywhere. Godot usually centers player locomotion on `CharacterBody2D` or `CharacterBody3D`, with animation and data split into sibling nodes and resources. Unity usually chooses between `CharacterController`, `Rigidbody`, or a more data-oriented runtime path, with `Animator` and shared data separated from movement authority. Unreal gives a strong default split with `ACharacter`, `CharacterMovementComponent`, controllers, animation blueprints, and optional Gameplay Ability System layers.
- Character code becomes expensive when it owns too much of everything:
  - direct input reads plus all combat rules
  - all animation transitions
  - all inventory mutation
  - all save projection
  - all camera behavior
- Abilities and locomotion need a clear ownership boundary. A dash, jump, parry, interact, or spell should name:
  - who can request it
  - who validates it
  - who changes movement or attributes
  - who drives feedback and animation
- Character state should distinguish between:
  - authored archetype or class data
  - runtime mutable avatar state
  - temporary combat state
  - persistent profile or loadout state

## Primary sources
- [Godot CharacterBody2D](https://docs.godotengine.org/en/stable/classes/class_characterbody2d.html)
- [Godot CharacterBody3D](https://docs.godotengine.org/en/stable/classes/class_characterbody3d.html)
- [Godot AnimationTree](https://docs.godotengine.org/en/stable/classes/class_animationtree.html)
- [Godot Resource](https://docs.godotengine.org/en/stable/classes/class_resource.html)
- [Unity Character Controller component reference](https://docs.unity3d.com/6000.1/Documentation/Manual/class-CharacterController.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity animation state machines](https://docs.unity3d.com/6000.1/Documentation/Manual/AnimationStateMachines.html)
- [Unity StateMachineBehaviour](https://docs.unity3d.com/6000.1/Documentation/Manual/StateMachineBehaviours.html)
- [Unreal ACharacter](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/ACharacter)
- [Gameplay Framework in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine)
- [Gameplay Ability System for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine)
- [Using Gameplay Abilities in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/using-gameplay-abilities-in-unreal-engine)

## Why this matters to this repo
- Character tasks in this repo should stop at the right architectural layer. A movement tweak does not automatically justify a whole new ability framework, and a scalable ability framework should not be hidden inside animation callbacks.
- Agents should explicitly say whether the task changes:
  - the avatar's locomotion model
  - the input-to-action mapping
  - the combat/ability layer
  - the animation/presentation layer
  - the character's durable or authored data
- The repo aims to support Godot, Unity, and Unreal without flattening them into one fake pattern. Character recommendations should therefore use the engine-native stack rather than forcing the same controller shape across all three.
- Character changes often touch equipment, inventory, enemy interactions, and save state. Those links should be named in feature briefs and route output instead of left implicit.

## Decision impact
- Character-related recommendations should always describe:
  - movement owner
  - ability/rule owner
  - animation owner
  - camera/targeting owner
  - data/persistence owner
- When a task mentions dash, jump, locomotion, avatar, player state, or class data, route and checklist output should surface this note in addition to engine-specific mechanic notes.
- Future mechanic, feature, and save templates should include a mandatory "character state boundary" section whenever the player avatar is touched.
