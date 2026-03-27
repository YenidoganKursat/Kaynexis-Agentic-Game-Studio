# AI, Navigation, and Entity Scale Architecture

## Date
- 2026-03-27

## Summary
- AI architecture breaks down more cleanly when teams separate three different problems:
  - movement over navigable space
  - decision logic or state flow
  - large-scale representation and simulation cost
- Official engine docs already expose this split. Godot distinguishes nav-region navigation from explicit A* graphs. Unity distinguishes authored navmesh workflows from custom graphs and also exposes pooling plus data-oriented packages for scale. Unreal splits navmesh traversal, EQS spatial reasoning, StateTree decision flow, and Mass or instancing for large-scale populations.
- The most expensive AI mistakes often come from solving all three problems with one abstraction. A custom pathfinding system is not automatically a behavior system. A behavior tree or state machine is not automatically a scalable crowd representation. A large crowd rendered as full gameplay entities may still need a different visual or simulation representation.
- For many games, the best architecture is layered:
  - traversable-space model
  - local decision framework
  - authored tuning or archetype data
  - scale strategy for high-count entities and repeated visuals

## Primary sources
- [Godot 2D navigation introduction](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_2d.html)
- [Godot 3D navigation introduction](https://docs.godotengine.org/en/stable/tutorials/navigation/navigation_introduction_3d.html)
- [Godot AStarGrid2D](https://docs.godotengine.org/en/stable/classes/class_astargrid2d.html)
- [Godot AStar3D](https://docs.godotengine.org/en/stable/classes/class_astar3d.html)
- [Godot MultiMesh](https://docs.godotengine.org/en/stable/classes/class_multimesh.html)
- [Unity AI Navigation package](https://docs.unity3d.com/ja/6000.0/Manual/com.unity.ai.navigation.html)
- [Unity ObjectPool<T>](https://docs.unity3d.com/6000.1/Documentation/ScriptReference/Pool.ObjectPool_1.html)
- [Unity Entities package docs](https://docs.unity3d.com/Packages/com.unity.entities@latest)
- [Unity Physics package docs](https://docs.unity3d.com/Packages/com.unity.physics@latest)
- [Basic Navigation in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/basic-navigation-in-unreal-engine)
- [Navigation System in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/navigation-system-in-unreal-engine)
- [Environment Query System in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-in-unreal-engine)
- [StateTree in Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/state-tree-in-unreal-engine)
- [Mass Entity in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/mass-entity-in-unreal-engine)
- [Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)

## Why this matters to this repo
- Any AI or enemy-system feature should stop and declare:
  - navigation representation
  - decision model
  - spatial query model
  - high-count scale plan
- Agents should avoid reaching for custom pathfinding or full ECS/Mass migration when the problem is actually simpler, but they should also stop pretending a high-count simulation can stay on heavyweight authored entities forever just because it starts small.
- This repo is meant to help iterative design. That means the chosen AI architecture should leave room for tuning enemy roles, crowd size, and encounter readability without a total rewrite.

## Decision impact
- AI and enemy-oriented recommendations should specify which layer each concern belongs to instead of collapsing them into one monolithic "AI system."
- The repo should keep surfacing performance and engine system notes whenever tasks mention pathfinding, navmesh, EQS, StateTree, crowd, swarm, or Mass-like scale.
- A future enemy-archetype or combat template should include navigation, decision, and representation fields explicitly.
