---
name: data-telemetry
description: Define event schemas, funnels, metrics, and privacy-safe instrumentation. Use when a feature needs measurement, balancing data, or live observation.
---

# Data Telemetry

## When to use
Define event schemas, funnels, metrics, and privacy-safe instrumentation. Use when a feature needs measurement, balancing data, or live observation.

## Inputs to gather
- questions to answer
- feature/system
- platform/privacy constraints

## Recommended roles
- `analytics_engineer`
- `game_designer`
- `security_engineer`

## Primary docs / outputs
- `studio/docs/templates/telemetry-schema.md`
- `studio/docs/templates/feature-brief.md`

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
- event catalog
- metric definitions
- privacy notes
- validation queries

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
