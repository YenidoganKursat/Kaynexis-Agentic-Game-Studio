---
name: gameplay-slice
description: Implement one validated gameplay slice with acceptance criteria, touched files, and explicit validation. Use for scoped mechanics, interactions, or player-facing feature work.
---

# Gameplay Slice

## When to use
Implement one validated gameplay slice with acceptance criteria, touched files, and explicit validation. Use for scoped mechanics, interactions, or player-facing feature work.

## Inputs to gather
- feature brief
- touched systems
- engine/runtime context
- validation requirements

## Recommended roles
- `lead_programmer`
- `gameplay_programmer`
- `qa_tester`

## Primary docs / outputs
- `studio/docs/active/current-sprint.md`
- `studio/docs/templates/test-plan.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Choose the smallest useful output that moves the project forward.
3. If code changes are involved, keep the patch tight and validate the changed behavior.
4. Update or create durable docs when the result should persist.
5. Recommend the next best role or skill if more work remains.

## Category rules
- Map the actual files/systems first, then choose the smallest viable implementation slice.
- Prefer reversible, reviewable patches over broad speculative refactors.
- Report commands, tests, and manual checks honestly.

## Deliverables
- small working slice
- changed files summary
- tests/manual checks
- follow-up tasks

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
