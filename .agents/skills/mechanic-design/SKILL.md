---
name: mechanic-design
description: Specify a single player mechanic with verbs, inputs, feedback, tuning surfaces, edge cases, and testability. Use for movement, abilities, interactions, or systemic verbs.
---

# Mechanic Design

## When to use
Specify a single player mechanic with verbs, inputs, feedback, tuning surfaces, edge cases, and testability. Use for movement, abilities, interactions, or systemic verbs.

## Inputs to gather
- mechanic concept
- player fantasy
- control scheme
- existing systems

## Recommended roles
- `game_designer`
- `combat_designer`
- `gameplay_programmer`

## Primary docs / outputs
- `studio/docs/templates/feature-brief.md`
- `studio/docs/templates/test-plan.md`
- `docs/research/game-development/systems/character.md`
- `docs/research/game-development/systems/skills.md`
- `docs/research/game-development/systems/interactions.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Read the matching systems note first when the task touches character state, abilities/upgrades, or interactions.
3. Choose the smallest useful output that moves the project forward.
4. Express the work as a feature, mechanic, or content contract that engineering and QA can consume.
5. Update or create durable docs when the result should persist.
6. Recommend the next best role or skill if more work remains.

## Category rules
- Lead with player outcome, then define scope, acceptance criteria, and edge cases.
- Keep mechanics and content contracts buildable by engineering and testable by QA.
- Surface tradeoffs among clarity, depth, scope, and production cost.

## Deliverables
- mechanic spec
- tuning knobs
- failure cases
- prototype path

## Validation bar
- acceptance criteria present
- risks/dependencies surfaced
- next implementation or test path clear
