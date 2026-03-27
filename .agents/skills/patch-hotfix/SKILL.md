---
name: patch-hotfix
description: Frame and execute a minimal-risk hotfix with rollback posture, targeted validation, and communication notes. Use for urgent crashes, blockers, or severe regressions.
---

# Patch Hotfix

## When to use
Frame and execute a minimal-risk hotfix with rollback posture, targeted validation, and communication notes. Use for urgent crashes, blockers, or severe regressions.

## Inputs to gather
- hot issue
- impact
- suspected fix area
- deadline/patch window

## Recommended roles
- `release_manager`
- `lead_programmer`
- `qa_lead`

## Primary docs / outputs
- `studio/docs/templates/bug-report.md`
- `studio/docs/templates/release-checklist.md`

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
- hotfix plan
- minimal patch scope
- validation list
- comms/rollback notes

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
