# Enemy Roster, Behavior, and Encounter Architecture

## Date
- 2026-03-27

## Summary
- Enemy architecture scales better when it distinguishes between three different questions:
  - what the enemy is
  - how the enemy decides
  - what role the enemy plays in an encounter
- A healthy enemy stack usually separates:
  - archetype or authored data
  - sensing and target selection
  - locomotion and navigation
  - action execution
  - damage and status interaction
  - encounter pacing or spawn orchestration
- Enemy systems break down when one script, actor, or node does all of these at once. That makes tuning slower, reuse weaker, and debugging harder.
- Engine-native AI stacks differ, but the design principle is stable. Godot often combines `CharacterBody`, `NavigationAgent`, `Area` sensors, signals, and resources. Unity often combines `NavMeshAgent` or custom pathing, trigger/query sensing, animator state, and `ScriptableObject` archetypes. Unreal strongly encourages explicit AI boundaries through `AIController`, Blackboard, Behavior Trees or StateTree, EQS, perception, and optionally GAS for ability-driven enemies.
- Enemy design should also state roster intent, not just implementation detail. Every enemy type should say what pressure it adds:
  - movement pressure
  - spacing pressure
  - burst threat
  - attrition threat
  - disruption or support
  - encounter pacing or teaching role

## Primary sources
- [Godot CharacterBody2D](https://docs.godotengine.org/en/stable/classes/class_characterbody2d.html)
- [Godot CharacterBody3D](https://docs.godotengine.org/en/stable/classes/class_characterbody3d.html)
- [Godot NavigationAgent2D](https://docs.godotengine.org/en/stable/classes/class_navigationagent2d.html)
- [Godot NavigationAgent3D](https://docs.godotengine.org/en/stable/classes/class_navigationagent3d.html)
- [Godot groups](https://docs.godotengine.org/en/stable/tutorials/scripting/groups.html)
- [Godot AnimationTree](https://docs.godotengine.org/en/stable/classes/class_animationtree.html)
- [Unity AI Navigation package](https://docs.unity3d.com/6000.0/Documentation/Manual/com.unity.ai.navigation.html)
- [Unity NavMeshAgent](https://docs.unity3d.com/ScriptReference/AI.NavMeshAgent.html)
- [Unity ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)
- [Unity Physics.RaycastNonAlloc](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Physics.RaycastNonAlloc.html)
- [Unreal Behavior Trees in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/behavior-trees-in-unreal-engine)
- [Unreal AI Perception in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/ai-perception-in-unreal-engine)
- [Unreal StateTree in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/state-tree-in-unreal-engine)
- [Environment Query System in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-in-unreal-engine)
- [Enemy Characters in Parrot for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/enemy-characters-in-parrot-for-unreal-engine)
- [Gameplay Ability System for Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-ability-system-for-unreal-engine)

## Why this matters to this repo
- Enemy tasks in this repo should describe both behavior architecture and encounter purpose. "Add an enemy" is too vague; the repo wants to know what the enemy teaches, pressures, or counters.
- Agents should explicitly call out:
  - archetype data location
  - sensing model
  - pathing/navigation owner
  - decision model
  - action execution layer
  - encounter role
- This matters across Godot, Unity, and Unreal because AI stacks differ drastically. The repo should not recommend a generic update loop if the chosen engine already has a better native fit.
- Enemy changes usually cascade into combat readability, progression pacing, content authoring, and performance. Treating enemy work as "just another actor script" hides those dependencies.

## Decision impact
- Future enemy and encounter docs should require a clear split between:
  - enemy archetype data
  - behavior or brain model
  - combat contact/damage model
  - encounter orchestration
- Route and checklist output should surface this note for tasks mentioning enemies, bosses, patrols, aggro, perception, or encounter AI.
- If enemy count or AI complexity grows, this note should be paired with navigation/performance guidance before implementation starts.
