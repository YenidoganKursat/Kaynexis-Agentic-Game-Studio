---
name: tools-pipeline
description: Design or implement a small internal tool, import/export helper, or editor workflow improvement. Use when content production is blocked by manual repetitive work.
---

# Tools Pipeline

## When to use
Design or implement a small internal tool, import/export helper, or editor workflow improvement. Use when content production is blocked by manual repetitive work.

## Inputs to gather
- pain point
- source/target formats
- frequency
- failure cost

## Recommended roles
- `tools_programmer`
- `technical_artist`
- `producer`

## Primary docs / outputs
- `studio/docs/templates/content-pipeline.md`
- `studio/docs/templates/build-pipeline.md`

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
- tool spec
- workflow change
- operator instructions
- maintenance notes

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
