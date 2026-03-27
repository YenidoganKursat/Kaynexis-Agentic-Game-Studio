---
name: localization-pass
description: Prepare text, UI, formatting, glossary, and extraction workflow for localization. Use before shipping in multiple languages or when text structure changes heavily.
---

# Localization Pass

## When to use
Prepare text, UI, formatting, glossary, and extraction workflow for localization. Use before shipping in multiple languages or when text structure changes heavily.

## Inputs to gather
- target languages
- string sources
- UI constraints
- voice/text policy

## Recommended roles
- `localization_lead`
- `ux_designer`
- `community_manager`

## Primary docs / outputs
- `studio/docs/templates/localization-glossary.md`
- `studio/docs/templates/feature-brief.md`

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
- loc readiness notes
- glossary
- text expansion risks
- pipeline steps

## Validation bar
- severity or readiness clearly stated
- evidence or repro captured
- owner/next action explicit
