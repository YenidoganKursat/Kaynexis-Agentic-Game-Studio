---
name: perf-pass
description: Frame a performance investigation or optimization pass with budgets, measurements, bottlenecks, and smallest high-impact fixes. Use for FPS, load times, memory, thermal, or battery issues.
---

# Performance Pass

## When to use
Frame a performance investigation or optimization pass with budgets, measurements, bottlenecks, and smallest high-impact fixes. Use for FPS, load times, memory, thermal, or battery issues.

## Inputs to gather
- symptom
- target hardware
- budgets
- existing profiling data

## Recommended roles
- `performance_analyst`
- `technical_director`
- `rendering_programmer`

## Primary docs / outputs
- `studio/docs/templates/perf-pass.md`
- `studio/docs/templates/test-plan.md`

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
- perf plan
- measurement targets
- bottleneck ranking
- optimization candidates

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
