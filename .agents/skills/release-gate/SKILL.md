---
name: release-gate
description: Run a ship/no-ship review that aggregates quality, cert, performance, and communication readiness into a clear recommendation. Use before demo, beta, or launch.
---

# Release Gate

## When to use
Run a ship/no-ship review that aggregates quality, cert, performance, and communication readiness into a clear recommendation. Use before demo, beta, or launch.

## Inputs to gather
- target release
- known issues
- build/test status
- store/cert needs

## Recommended roles
- `release_manager`
- `qa_lead`
- `executive_producer`

## Primary docs / outputs
- `studio/docs/templates/release-checklist.md`
- `studio/docs/templates/risk-register.md`

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
- go/no-go memo
- blockers
- accepted risks
- required next actions

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
