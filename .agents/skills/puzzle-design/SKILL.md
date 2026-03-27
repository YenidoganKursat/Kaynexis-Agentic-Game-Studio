---
name: puzzle-design
description: Design puzzle logic, affordances, hinting, failure recovery, and readability. Use for spatial, systemic, or sequence puzzles.
---

# Puzzle Design

## When to use
Design puzzle logic, affordances, hinting, failure recovery, and readability. Use for spatial, systemic, or sequence puzzles.

## Inputs to gather
- puzzle goal
- mechanics involved
- hint philosophy
- target audience

## Recommended roles
- `game_designer`
- `level_designer`
- `ux_designer`

## Primary docs / outputs
- `studio/docs/templates/feature-brief.md`
- `studio/docs/templates/test-plan.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Choose the smallest useful output that moves the project forward.
3. Express the work as a feature, mechanic, or content contract that engineering and QA can consume.
4. Update or create durable docs when the result should persist.
5. Recommend the next best role or skill if more work remains.

## Category rules
- Lead with player outcome, then define scope, acceptance criteria, and edge cases.
- Keep mechanics and content contracts buildable by engineering and testable by QA.
- Surface tradeoffs among clarity, depth, scope, and production cost.

## Deliverables
- puzzle spec
- hint plan
- failure loops
- QA matrix seeds

## Validation bar
- acceptance criteria present
- risks/dependencies surfaced
- next implementation or test path clear
