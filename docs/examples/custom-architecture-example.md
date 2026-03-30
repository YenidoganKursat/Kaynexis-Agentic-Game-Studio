# Custom Architecture Example

## Scope

A project-specific inventory rule pack with one fixed combat model and one overrideable progression rule set.

## Baseline

- canonical combat ownership stays in the standard architecture lane
- the project owner wants inventory and upgrade overrides
- the request needs a durable contract instead of a one-off chat answer

## Decision order

1. fixed versus overrideable
2. owner
3. precedence
4. fallback
5. validation

## Example custom request contract

- fixed: combat truth, save ownership, canonical item ids
- overrideable: item rarity weights, loadout slots, progression thresholds
- forbidden: changing canonical save ownership or making UI the source of truth

## Example rule pack

- keep combat outcome canonical
- allow project-specific item balance overrides
- keep override names short and deterministic
- fall back to the default architecture when a rule is missing

## Good agent prompts

- "Design a custom architecture and rule pack for project-specific inventory overrides."
- "Define a custom request contract that lets designers change pacing rules without changing canonical combat ownership."
- "Add a project-specific house-rule layer that keeps override points explicit and reviewable."

## Validation

- Name the fixed rules and the overrideable rules.
- Name the owner and the fallback.
- Confirm the precedence order is written down.
- Keep the guide, checklist, research note, and active eval aligned.

## Related docs

- `docs/reference/custom-architecture.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/agent-system.md`
- `docs/research/game-development/foundations/custom-architecture.md`
