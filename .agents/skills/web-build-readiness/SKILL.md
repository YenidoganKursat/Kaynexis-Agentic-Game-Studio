---
name: web-build-readiness
description: Prepare a build for web delivery, browser constraints, load-time budgets, input quirks, and CDN/embedding assumptions. Use for demos, marketing beats, or web-first products.
---

# Web Build Readiness

## When to use
Prepare a build for web delivery, browser constraints, load-time budgets, input quirks, and CDN/embedding assumptions. Use for demos, marketing beats, or web-first products.

## Inputs to gather
- web target
- browser/device support
- asset weight
- embed/distribution plan

## Recommended roles
- `porting_engineer`
- `build_release_engineer`
- `performance_analyst`

## Primary docs / outputs
- `studio/docs/templates/platform-targets.md`
- `studio/docs/templates/build-pipeline.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Choose the smallest useful output that moves the project forward.
3. Make the highest-risk issue, blocker, or readiness gap unambiguous.
4. Update or create durable docs when the result should persist.
5. Recommend the next best role or skill if more work remains.

## Category rules
- Prioritize severe player-facing, security, certification, and release risks over cosmetic issues.
- Make evidence, repro, and owner/action clarity explicit.
- Return a clear go/no-go or priority recommendation when the task is evaluative.

## Deliverables
- web readiness plan
- load/perf risks
- browser quirks
- release checklist

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
