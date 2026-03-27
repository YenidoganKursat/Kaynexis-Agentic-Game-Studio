# Combat, Damage, and Effects Architecture

## Date
- 2026-03-27

## Summary
- A healthy combat architecture separates four concerns that often get tangled together:
  - contact detection
  - rules and damage resolution
  - attributes or mutable combat state
  - audiovisual feedback and effect presentation
- Official engine guidance points toward explicit contact surfaces and explicit data flow. Godot uses areas, collisions, and signals or physics queries; Unity uses triggers, collisions, layer filtering, and non-alloc queries; Unreal uses collision channels, `TakeDamage`, or the Gameplay Ability System when combat grows more systemic.
- The higher the scope, the more valuable it is to keep "what happened" separate from "what it looked like." This matters for readability, networking, replays, save/load, and debugging. A combat event should be representable as a small piece of durable logic, even if multiple VFX, sounds, hit flashes, or UI widgets react to it.
- The more a combat system adds status effects, cooldowns, scaling attributes, or content-authored abilities, the more it should be data-driven. That does not mean every prototype needs a giant effect framework, but it does mean hard-coding every interaction into scene or actor scripts scales poorly.

## Primary sources
- [Godot Area2D](https://docs.godotengine.org/en/stable/classes/class_area2d.html)
- [Godot using Area2D](https://docs.godotengine.org/en/stable/tutorials/physics/using_area_2d.html)
- [Godot SceneTree](https://docs.godotengine.org/en/latest/classes/class_scenetree.html)
- [Unity trigger colliders](https://docs.unity3d.com/ja/current/Manual/collider-interactions-create-trigger.html)
- [Unity OnTrigger events](https://docs.unity3d.com/ja/2023.2/Manual/collider-interactions-ontrigger.html)
- [Unity layer collision matrix guidance](https://docs.unity3d.com/jp/current/Manual/physics-optimization-cpu-collision-layers.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unreal AActor::TakeDamage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/TakeDamage)
- [Unreal collision overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview)
- [Gameplay Ability System for Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/gameplay-ability-system-for-unreal-engine)
- [Using Gameplay Abilities in Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/using-gameplay-abilities-in-unreal-engine)

## Why this matters to this repo
- Combat features in this repo should explicitly name the layer boundaries:
  - detection surface
  - resolution logic
  - data/tuning source
  - feedback output
- Agents should stop defaulting to "put all damage code where the collision happens." That is fast for the first prototype and brittle for everything after it.
- The active docs and feature briefs should describe whether a damage system is still "simple local combat" or is crossing into "effect framework / attribute framework / ability framework" territory.
- This repo wants strong readability and iteration. A combat architecture that keeps rules and feedback separate makes tuning easier and prevents VFX or animation changes from silently becoming rules bugs.

## Decision impact
- Combat-oriented recommendations should describe the damage pipeline in order:
  - contact source
  - authority for validating the hit
  - state mutation point
  - downstream feedback listeners
- Checklist bundles should continue to surface world stack, contact model, and scale risk for combat tasks.
- As the project grows, a future durable template for combat features should include an explicit "damage/effect architecture" section instead of leaving it implied.
