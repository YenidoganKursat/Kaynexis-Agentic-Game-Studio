---
name: porting-plan
description: Map a PC/console/mobile/web port into concrete deltas for input, performance, compliance, assets, and release sequencing. Use before or during porting work.
---

# Porting Plan

## When to use
Map a PC/console/mobile/web port into concrete deltas for input, performance, compliance, assets, and release sequencing. Use before or during porting work.

## Inputs to gather
- source platform
- target platform
- current bottlenecks
- submission goals

## Recommended roles
- `porting_engineer`
- `certification_manager`
- `performance_analyst`

## Primary docs / outputs
- `studio/docs/templates/platform-targets.md`
- `studio/docs/templates/cert-checklist.md`
- `studio/docs/templates/perf-pass.md`

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
- porting delta map
- critical risks
- performance/cert gates
- priority plan

## Validation bar
- touched files/systems identified
- tests or manual validation listed
- follow-up work clearly scoped
