---
name: qa-matrix
description: Create a lean but meaningful test matrix from a feature or milestone. Use before calling a feature done or preparing a playtest/release.
---

# QA Matrix

## When to use
Create a lean but meaningful test matrix from a feature or milestone. Use before calling a feature done or preparing a playtest/release.

## Inputs to gather
- feature or milestone scope
- platforms
- known risks
- save/network/perf considerations

## Recommended roles
- `qa_lead`
- `qa_tester`
- `producer`

## Primary docs / outputs
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
- test matrix
- smoke/regression list
- priority bugs to watch
- coverage gaps

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
