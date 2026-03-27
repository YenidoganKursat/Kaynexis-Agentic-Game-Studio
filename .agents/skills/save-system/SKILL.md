---
name: save-system
description: Design or implement save/load behavior, checkpoints, migrations, and corruption recovery. Use whenever state persistence changes.
---

# Save System

## When to use
Design or implement save/load behavior, checkpoints, migrations, and corruption recovery. Use whenever state persistence changes.

## Inputs to gather
- what must persist
- platform constraints
- migration risk
- rollback needs

## Recommended roles
- `save_system_engineer`
- `qa_lead`
- `security_engineer`

## Primary docs / outputs
- `studio/docs/templates/save-migration-plan.md`
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
- save model
- migration notes
- corruption handling
- test matrix

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
