---
name: content-pipeline
description: Shape how assets, scripts, dialogue, or level content move from authoring into the game safely and repeatably. Use when content throughput or consistency is weak.
---

# Content Pipeline

## When to use
Shape how assets, scripts, dialogue, or level content move from authoring into the game safely and repeatably. Use when content throughput or consistency is weak.

## Inputs to gather
- content types
- authors
- import steps
- validation needs

## Recommended roles
- `technical_artist`
- `tools_programmer`
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
- pipeline map
- naming/validation rules
- ownership notes
- automation opportunities

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
