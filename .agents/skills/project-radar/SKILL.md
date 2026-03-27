---
name: project-radar
description: Scan the repository for the highest-impact gaps across code, docs, tests, build pipeline, and release risk. Use when you need a fast health check before starting work.
---

# Project Radar

## When to use
Scan the repository for the highest-impact gaps across code, docs, tests, build pipeline, and release risk. Use when you need a fast health check before starting work.

## Inputs to gather
- repo tree
- current docs
- test/build status

## Recommended roles
- `producer`
- `lead_programmer`
- `qa_lead`

## Primary docs / outputs
- `studio/docs/active/current-sprint.md`
- `studio/docs/active/risk-register.md`
- `studio/docs/active/decision-log.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Choose the smallest useful output that moves the project forward.
3. Update or create durable docs when the result should persist.
4. Recommend the next best role or skill if more work remains.

## Category rules
- Inspect the repo, existing docs, and engine clues before asking for more information.
- Use minimal clarifying questions only when a missing fact blocks a good recommendation.
- Write or update durable docs when the output should survive chat history.

## Deliverables
- priority findings
- missing artifacts
- suggested skill queue
- severity ranking

## Validation bar
- updated active docs
- recommended next skill
- critical unknowns listed
