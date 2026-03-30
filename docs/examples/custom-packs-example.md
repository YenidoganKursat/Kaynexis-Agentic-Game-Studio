# Custom Packs Example

## Scope

A project-specific inventory feature pack that combines one fixed combat rule, one overrideable progression rule, and one opt-in UI hook pack.

## Baseline

- canonical combat ownership stays in the standard architecture lane
- the project wants a reusable way to add custom feature bundles without chat-only tribal knowledge
- the pack needs a registry entry, not just a one-off rule note

## Decision order

1. canonical architecture
2. custom rule contract
3. pack type
4. hook points
5. fallback behavior

## Example pack manifest

```toml
id = "inventory_feature_pack"
name = "Inventory Feature Pack"
type = "feature"
enabled = true
owner = "technical_director"
scope = "Project-specific inventory rules, UI hooks, and balancing overrides"
depends_on = ["custom-architecture", "extensions"]
fixed_rules = ["combat ownership", "canonical item ids"]
override_rules = ["rarity weights", "progression thresholds"]
hook_points = ["inventory_ui", "loot_filters", "debug_overlay"]
override_points = ["sort_order", "visible_groups", "tooltip_copy"]
fallback = "core inventory flow"
validation = "Run the custom packs checklist and one narrow smoke path."
```

## Example pack registry row

| Pack id | Type | Owner | Fallback |
| --- | --- | --- | --- |
| `inventory_feature_pack` | feature | `technical_director` | `core inventory flow` |

## Good agent prompts

- "Design a custom pack registry for project-specific inventory and UI overrides."
- "Define a feature pack that keeps canonical combat ownership outside the pack."
- "Build a custom pack that can be disabled cleanly without changing the core save contract."

## Validation

- Name the fixed rules and the overrideable rules.
- Name the pack owner, type, and fallback.
- Keep the guide, checklist, research note, and eval plan synchronized.

## Related docs

- `docs/reference/custom-packs.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/extensions-guide.md`
- `docs/research/game-development/foundations/custom-packs.md`
- `studio/docs/templates/custom-packs.md`
- `studio/docs/active/custom-packs-adr.md`
- `studio/docs/active/eval-custom-packs.md`
