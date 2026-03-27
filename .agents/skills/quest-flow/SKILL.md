---
name: quest-flow
description: Shape mission/quest structure with objectives, branching, dependencies, fail states, and recovery logic. Use for narrative or systemic missions.
---

# Quest Flow

## When to use
Shape mission/quest structure with objectives, branching, dependencies, fail states, and recovery logic. Use for narrative or systemic missions.

## Inputs to gather
- quest idea
- objective chain
- branching depth
- save/retry behavior

## Recommended roles
- `quest_designer`
- `game_designer`
- `qa_tester`

## Primary docs / outputs
- `studio/docs/templates/quest-brief.md`
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
- quest flow spec
- objective states
- failure/recovery paths
- QA focus

## Validation bar
- acceptance criteria present
- risks/dependencies surfaced
- next implementation or test path clear
