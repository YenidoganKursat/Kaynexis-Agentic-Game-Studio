---
name: multiplayer-slice
description: Design or implement one multiplayer feature slice with authority model, sync expectations, latency assumptions, and desync validation. Use for online or co-op work.
---

# Multiplayer Slice

## When to use
Design or implement one multiplayer feature slice with authority model, sync expectations, latency assumptions, and desync validation. Use for online or co-op work.

## Inputs to gather
- feature behavior
- host/client topology
- state ownership
- match/session flow

## Recommended roles
- `network_programmer`
- `backend_engineer`
- `qa_lead`

## Primary docs / outputs
- `studio/docs/templates/feature-brief.md`
- `studio/docs/templates/test-plan.md`
- `studio/docs/templates/telemetry-schema.md`

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
- network slice plan
- authority model
- desync risks
- validation matrix

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
