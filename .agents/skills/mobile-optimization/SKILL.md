---
name: mobile-optimization
description: Adapt a feature or build for mobile performance, controls, memory, battery, and session design. Use for iOS/Android releases or mobile-focused slices.
---

# Mobile Optimization

## When to use
Adapt a feature or build for mobile performance, controls, memory, battery, and session design. Use for iOS/Android releases or mobile-focused slices.

## Inputs to gather
- mobile target devices
- current bottlenecks
- touch/UI demands
- session length goals

## Recommended roles
- `porting_engineer`
- `performance_analyst`
- `ux_designer`

## Primary docs / outputs
- `studio/docs/templates/perf-pass.md`
- `studio/docs/templates/platform-targets.md`

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
- mobile optimization plan
- device risk list
- input/UI changes
- validation targets

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
