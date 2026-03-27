---
name: console-cert-readiness
description: Audit a build and process for certification-style requirements, submission evidence, and likely blockers. Use for console or tightly regulated platform releases.
---

# Console Cert Readiness

## When to use
Audit a build and process for certification-style requirements, submission evidence, and likely blockers. Use for console or tightly regulated platform releases.

## Inputs to gather
- target platform
- current build status
- known issues
- submission date

## Recommended roles
- `certification_manager`
- `qa_lead`
- `porting_engineer`

## Primary docs / outputs
- `studio/docs/templates/cert-checklist.md`
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
- cert readiness checklist
- high-risk gaps
- evidence needed
- owner list

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
