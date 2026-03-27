---
name: architecture-decision
description: Write or revise an ADR for technical decisions with significant maintenance, performance, or pipeline impact. Do not use for tiny local refactors.
---

# Architecture Decision

## When to use
Write or revise an ADR for technical decisions with significant maintenance, performance, or pipeline impact. Do not use for tiny local refactors.

## Inputs to gather
- decision to make
- options
- constraints
- evidence

## Recommended roles
- `technical_director`
- `lead_programmer`
- `docs_researcher`

## Primary docs / outputs
- `studio/docs/templates/adr.md`
- `studio/docs/active/decision-log.md`

## Workflow
1. Inspect the current repo/docs state first and cite concrete evidence.
2. Choose the smallest useful output that moves the project forward.
3. Express the work as a feature, mechanic, or content contract that engineering and QA can consume.
4. Update or create durable docs when the result should persist.
5. Recommend the next best role or skill if more work remains.

## Category rules
- Lead with player outcome, then define scope, acceptance criteria, and edge cases.
- Keep mechanics and content contracts buildable by engineering and testable by QA.
- Surface tradeoffs among clarity, depth, scope, and production cost.

## Deliverables
- ADR
- tradeoff summary
- rejected options
- validation/follow-up

## Validation bar
- acceptance criteria present
- risks/dependencies surfaced
- next implementation or test path clear
