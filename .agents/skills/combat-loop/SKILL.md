---
name: combat-loop
description: Design or tune a combat loop including enemy roles, feedback, pacing, damage model, and skill expression. Use for combat-heavy slices and balance passes.
---

# Combat Loop

## When to use
Design or tune a combat loop including enemy roles, feedback, pacing, damage model, and skill expression. Use for combat-heavy slices and balance passes.

## Inputs to gather
- combat goals
- weapons/abilities
- enemy roster
- performance constraints

## Recommended roles
- `combat_designer`
- `encounter_designer`
- `gameplay_programmer`

## Primary docs / outputs
- `studio/docs/templates/enemy-archetype.md`
- `studio/docs/templates/boss-fight-brief.md`
- `studio/docs/templates/perf-pass.md`
- `docs/research/game-development/systems/enemy-roster-behavior-and-encounter-architecture.md`
- `docs/research/game-development/systems/abilities-skill-trees-upgrades-and-build-architecture.md`
- `docs/research/game-development/systems/character-controller-ability-and-state-architecture.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Read the matching combat systems notes first when the task changes enemy roles, player abilities, or character-state boundaries.
3. Choose the smallest useful output that moves the project forward.
4. Express the work as a feature, mechanic, or content contract that engineering and QA can consume.
5. Update or create durable docs when the result should persist.
6. Recommend the next best role or skill if more work remains.

## Category rules
- Lead with player outcome, then define scope, acceptance criteria, and edge cases.
- Keep mechanics and content contracts buildable by engineering and testable by QA.
- Surface tradeoffs among clarity, depth, scope, and production cost.

## Deliverables
- combat loop brief
- enemy role notes
- tuning plan
- playtest questions

## Validation bar
- acceptance criteria present
- risks/dependencies surfaced
- next implementation or test path clear
