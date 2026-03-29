# Interactions, Pickups, and World Object Architecture

## Date
- 2026-03-27

## Summary
- World interaction systems are easier to scale when they separate:
  - interactable or pickup definition
  - detection and candidate selection
  - interaction validation
  - world-state mutation
  - inventory or reward projection
  - UI prompt and feedback
- Interactions become messy when prompts, collision checks, loot grants, quest updates, and save flags all happen in one trigger callback.
- Engine-native authoring patterns differ. Godot often uses Areas, groups, signals, and reusable scenes/resources. Unity often uses trigger/query sensing, components, prefabs, and shared data assets. Unreal often uses Actors, Components, collision channels, interfaces, and UMG prompts layered over the world.
- Pickups and switches should name:
  - how the player detects them
  - how the player chooses the target if several overlap
  - what authority says the interaction is allowed
  - what happens to the world object after use
  - whether the result must persist
- A good interaction model also decides whether it is:
  - proximity only
  - aim or facing constrained
  - line-of-sight constrained
  - hold-to-use
  - one-shot
  - reusable

## Primary sources
- [Godot input examples](https://docs.godotengine.org/en/stable/tutorials/inputs/input_examples.html)
- [Godot groups](https://docs.godotengine.org/en/stable/tutorials/scripting/groups.html)
- [Godot using Area2D](https://docs.godotengine.org/en/stable/tutorials/physics/using_area_2d.html)
- [Godot Control](https://docs.godotengine.org/en/stable/classes/class_control.html)
- [Unity trigger colliders](https://docs.unity3d.com/ja/current/Manual/collider-interactions-create-trigger.html)
- [Unity OnTrigger events](https://docs.unity3d.com/ja/2023.2/Manual/collider-interactions-ontrigger.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity runtime UI event system](https://docs.unity3d.com/ja/6000.0/Manual/UIE-Runtime-Event-System.html)
- [Unreal collision overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview)
- [Unreal AActor::TakeDamage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/TakeDamage)
- [Unreal UMG UI Designer Quick Start Guide](https://dev.epicgames.com/documentation/en-us/unreal-engine/umg-ui-designer-quick-start-guide-in-unreal-engine?application_version=5.6)

## Why this matters to this repo
- Interaction and pickup tasks often look small but quietly cross gameplay, UI, save, and inventory boundaries. This repo should make those links visible before implementation.
- Agents should explicitly state:
  - candidate selection rule
  - validation rule
  - world mutation rule
  - reward projection rule
  - persistence expectation
- This matters for designers too. Interaction systems usually become content authoring surfaces quickly, so the repo should not hide the authoring contract.

## Decision impact
- Route and checklist output should surface this note for tasks mentioning interact, prompt, pickup, trigger, lever, chest, dialogue prompt, usable object, or world object.
- Future feature briefs for interactable mechanics should require:
  - selection rule
  - feedback rule
  - persistence rule
  - content authoring rule
