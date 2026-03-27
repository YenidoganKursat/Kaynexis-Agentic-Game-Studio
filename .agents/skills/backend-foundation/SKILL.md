---
name: backend-foundation
description: Frame service contracts, auth assumptions, matchmaking/persistence scope, and operational boundaries. Use before serious backend implementation or live features.
---

# Backend Foundation

## When to use
Frame service contracts, auth assumptions, matchmaking/persistence scope, and operational boundaries. Use before serious backend implementation or live features.

## Inputs to gather
- service needs
- trust boundaries
- latency expectations
- failure handling

## Recommended roles
- `backend_engineer`
- `security_engineer`
- `technical_director`

## Primary docs / outputs
- `studio/docs/templates/adr.md`
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
- service contract
- auth/trust model
- operational risks
- next implementation step

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
