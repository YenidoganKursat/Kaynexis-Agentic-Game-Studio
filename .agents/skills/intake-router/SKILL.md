---
name: intake-router
description: Triage an incoming request and recommend the best next skill, agents, docs, and validation plan. Use first when the task is ambiguous, broad, or cross-functional. Do not use for already well-scoped single-step edits.
---

# Intake Router

## When to use
Triage an incoming request and recommend the best next skill, agents, docs, and validation plan. Use first when the task is ambiguous, broad, or cross-functional. Do not use for already well-scoped single-step edits.

## Inputs to gather
- user goal
- repo context
- engine/platform clues
- time/risk sensitivity

## Recommended roles
- `producer`
- `technical_director`
- `game_designer`

## Primary docs / outputs
- `studio/docs/active/current-sprint.md`
- `studio/docs/active/risk-register.md`

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
- recommended skill sequence
- suggested agents
- touched files/docs
- first validation step

## Validation bar
- updated active docs
- recommended next skill
- critical unknowns listed
