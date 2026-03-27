---
name: economy-balance
description: Design or rebalance currencies, sinks, progression prices, drop rates, and anti-exploit safeguards. Use for shops, crafting, meta loops, or F2P economies.
---

# Economy Balance

## When to use
Design or rebalance currencies, sinks, progression prices, drop rates, and anti-exploit safeguards. Use for shops, crafting, meta loops, or F2P economies.

## Inputs to gather
- economy goals
- sources/sinks
- retention or session length goals
- exploit concerns

## Recommended roles
- `economy_designer`
- `progression_designer`
- `analytics_engineer`

## Primary docs / outputs
- `studio/docs/templates/economy-tuning.md`
- `studio/docs/templates/telemetry-schema.md`

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
- economy model
- pricing assumptions
- telemetry needs
- risk flags

## Validation bar
- acceptance criteria present
- risks/dependencies surfaced
- next implementation or test path clear
