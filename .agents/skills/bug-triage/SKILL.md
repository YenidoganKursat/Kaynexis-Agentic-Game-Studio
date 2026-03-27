---
name: bug-triage
description: Convert a vague bug into reproducible steps, hypotheses, severity, owner, and next action. Use for crash, regression, UI, gameplay, or content bugs.
---

# Bug Triage

## When to use
Convert a vague bug into reproducible steps, hypotheses, severity, owner, and next action. Use for crash, regression, UI, gameplay, or content bugs.

## Inputs to gather
- bug report
- expected vs actual
- logs/evidence
- build/platform

## Recommended roles
- `qa_tester`
- `qa_lead`
- `lead_programmer`

## Primary docs / outputs
- `studio/docs/templates/bug-report.md`
- `studio/docs/templates/crash-triage.md`

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
- bug report
- severity and owner
- repro steps
- suspected areas

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
