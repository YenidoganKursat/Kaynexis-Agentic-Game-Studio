# Unreal Performance

## Date
- 2026-03-27

## Summary
- Unreal's default gameplay vocabulary is Actor, Component, Blueprint, and navigation over generated navmesh, but the engine also supports 2D and hybrid 2D/3D workflows through Paper 2D. Repo guidance should force each slice to say whether it is Paper2D-driven, standard 3D gameplay-framework driven, or a controlled hybrid.
- Unreal's navigation system is navmesh-based and tile-oriented. Official docs describe localized rebuilding, polygon costs, and the `NavMeshBoundsVolume` workflow. That makes the default recommendation clear: use the engine navigation system for world traversal unless the problem is a deliberately abstract graph.
- Unreal's AI stack includes higher-level orchestration tools such as StateTree and EQS. Repo guidance should steer agents to those tools for decision flow and spatial querying before they invent bespoke decision graphs inside random Actors.
- Unreal exposes two important scale levers for high-entity scenarios:
  - `InstancedStaticMeshComponent` for many repeated visuals
  - Mass Entity when the simulation scale exceeds what full Actor-per-entity gameplay can support efficiently
- For damage systems, Unreal offers a light built-in path through `AActor::TakeDamage`, collision/overlap channels, and Blueprint/C++ events. When the design needs attributes, cost/cooldown systems, asynchronous abilities, or network-aware gameplay abilities, the Gameplay Ability System becomes the stronger long-term contract.
- If the real bottleneck is GPU ownership or CPU-GPU communication rather than actor scale alone, pair this note with `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` before tuning.

## Recommended order
- Measure one baseline first.
- Keep Actor / Component / Data Asset / Blueprint ownership if it can still hit budget.
- Prefer navmesh, EQS, and StateTree before custom graphs or bespoke AI plumbing.
- Use collision channels, simple damage, and instancing before reaching for GAS or Mass.
- Move to GAS or Mass only when ability complexity or entity count is the proven bottleneck.

## Primary sources
- [Paper 2D overview in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/paper-2d-overview-in-unreal-engine)
- [Basic Navigation in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/basic-navigation-in-unreal-engine)
- [Navigation System in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/navigation-system-in-unreal-engine)
- [StateTree in Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/state-tree-in-unreal-engine)
- [Environment Query System in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/environment-query-system-in-unreal-engine)
- [Mass Entity in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/mass-entity-in-unreal-engine)
- [Instanced Static Mesh Component](https://dev.epicgames.com/documentation/en-us/unreal-engine/instanced-static-mesh-component-in-unreal-engine)
- [Gameplay Ability System for Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/gameplay-ability-system-for-unreal-engine)
- [Using Gameplay Abilities in Unreal Engine](https://dev.epicgames.com/documentation/unreal-engine/using-gameplay-abilities-in-unreal-engine)
- [AActor::TakeDamage](https://dev.epicgames.com/documentation/en-us/unreal-engine/API/Runtime/Engine/GameFramework/AActor/TakeDamage)
- [Collision overview in Unreal Engine](https://dev.epicgames.com/documentation/en-us/unreal-engine/collision-in-unreal-engine---overview)

## Why this matters to this repo
- Unreal tasks should explicitly choose the world representation:
  - Paper2D / sprite-driven 2D
  - standard 3D gameplay framework
  - hybrid 2D/3D with limited crossings
- Agents should default to the built-in navigation system for traversing world geometry. They should only recommend custom A* or graph code when the navigation problem is not really a navmesh problem.
- Unreal gameplay planning should separate three layers of reasoning:
  - traversal over navigable space -> Navigation System
  - spatial selection / contextual query -> EQS
  - stateful decision flow -> StateTree or another explicit behavior layer
- Scale decisions need to be deliberate much earlier in Unreal than teams often expect. Thousands of fully scripted Actors are not the same as instanced visuals or Mass entities, so the repo should force agents to name the representation choice before a crowd or projectile system grows.
- Damage guidance should stay proportional to feature scope. Small local combat can use collision plus `TakeDamage`; a more systemic action RPG or multiplayer ability game should at least evaluate GAS before hard-coding a parallel framework.

## Decision impact
- Unreal engine guidance should require agents to name:
  - world stack: Paper2D, 3D gameplay framework, or hybrid
  - navigation stack: navmesh only, navmesh plus EQS/StateTree, or justified custom graph
  - damage framework: simple damage pipeline or GAS-backed ability/attribute system
  - scale lever: Actor, instanced component, or Mass-based representation
- The Unreal engine checklist should add explicit items for stack choice, AI/navigation model, damage-framework choice, and large-scale representation.
- Routing and research refs should surface these notes whenever a task mentions `pathfinding`, `navmesh`, `StateTree`, `EQS`, `damage`, `GAS`, `crowd`, or `Mass`.
- The shared perf guide at `docs/reference/perf-guide.md` should be read before micro-optimizing the slice, and the matching example at `docs/examples/perf-example.md` should be used as the agent's concrete prompt model.
