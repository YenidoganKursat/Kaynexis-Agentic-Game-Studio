# State

## Summary
- State architecture is about phase flow, mode changes, and what transitions are legal.
- It covers boss phases, encounter modes, menus, mission stages, AI state graphs, and gameplay flow that must not be hand-waved.

## Primary sources
- Godot state machine concepts - https://docs.godotengine.org/en/stable/tutorials/math/finite_state_machine.html
- Godot autoloads - https://docs.godotengine.org/en/stable/tutorials/best_practices/autoloads.html
- Unity execution order - https://docs.unity3d.com/6000.1/Documentation/Manual/ExecutionOrder.html
- Unreal StateTree - https://dev.epicgames.com/documentation/en-us/unreal-engine/statetree-in-unreal-engine
- Unreal gameplay framework - https://dev.epicgames.com/documentation/en-us/unreal-engine/gameplay-framework-in-unreal-engine

## Why this matters to this repo
- State architecture is the bridge between combat, UI, save, AI, and progression.
- If the repo cannot name the current state and the transition rules, the agent will drift into ad hoc branching.

## Decision impact
- Use a state graph or state machine when phase changes matter.
- Use explicit transition rules rather than implicit boolean flags.
- Keep the state owner and the projection owner separate.

## Common patterns
- Godot: a node or autoload drives the authoritative phase, while children react through signals.
- Unity: a coordinator or state service owns the current phase; scenes and UI react to it.
- Unreal: StateTree, gameplay state, or a dedicated component owns the phase graph depending on scope.

## What to watch out for
- Do not let animation frames define gameplay phases.
- Do not let one giant enum hide a graph that should have been documented.
- Do not add more states without naming the transition budget.

## Validation expectations
- The task should name the current state, legal transitions, and the failure or recovery path.
- The implementation should prove at least one transition path end to end.
