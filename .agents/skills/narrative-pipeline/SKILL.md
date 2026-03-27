---
name: narrative-pipeline
description: Organize story beats, dialogue production, branching constraints, and implementation-ready narrative docs. Use for narrative-heavy features or content pipelines.
---

# Narrative Pipeline

## When to use
Organize story beats, dialogue production, branching constraints, and implementation-ready narrative docs. Use for narrative-heavy features or content pipelines.

## Inputs to gather
- story goals
- content volume
- branching complexity
- loc targets

## Recommended roles
- `narrative_director`
- `quest_designer`
- `localization_lead`

## Primary docs / outputs
- `studio/docs/templates/quest-brief.md`
- `studio/docs/templates/localization-glossary.md`

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
- narrative brief
- content pipeline notes
- string constraints
- review cadence

## Validation bar
- acceptance criteria present
- risks/dependencies surfaced
- next implementation or test path clear
