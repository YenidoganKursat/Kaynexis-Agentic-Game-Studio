---
name: accessibility-audit
description: Audit a feature or build for control, readability, timing, color, subtitle, and assist-option risks. Use during feature review or release prep.
---

# Accessibility Audit

## When to use
Audit a feature or build for control, readability, timing, color, subtitle, and assist-option risks. Use during feature review or release prep.

## Inputs to gather
- feature/build to inspect
- target audience
- platform/input methods

## Recommended roles
- `accessibility_specialist`
- `ux_designer`
- `qa_lead`

## Primary docs / outputs
- `studio/docs/templates/accessibility-pass.md`
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
- accessibility findings
- priority fixes
- assist options
- test follow-up

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
