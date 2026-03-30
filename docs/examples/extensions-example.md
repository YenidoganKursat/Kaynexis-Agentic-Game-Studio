# Extensions Example

## Scope

A project-specific inventory and UI hook pack that adds optional filters, debug overlays, and editor-side helpers without changing the canonical combat or save contract.

## Baseline

- canonical inventory ownership stays in the core system
- the extension is opt-in and can be disabled without breaking the core flow
- the pack only touches the named hook points

## Decision order

1. canonical architecture
2. custom request contract
3. extension manifest
4. hook points
5. project-specific override

## Example extension manifest

```toml
id = "inventory_extension_pack"
name = "Inventory Extension Pack"
enabled = false
owner = "technical_director"
scope = "Project-specific inventory filters, UI helpers, and debug overlays"
depends_on = ["custom-architecture"]
hook_points = ["inventory_ui", "loot_filters", "debug_overlay"]
override_points = ["sort_order", "visible_groups", "tooltip_copy"]
fallback = "core inventory flow"
validation = "Run the extensions checklist and one narrow smoke path."
```

## Good agent prompts

- "Design an extension pack for inventory filter hooks and editor panels."
- "Define a plugin-like add-on that can be disabled without touching canonical combat state."
- "Build a manifest for a UI hook pack and keep the fallback explicit."

## Validation

- Name the fixed core behavior.
- Name the hook points and the fallback.
- Confirm the pack can be enabled and disabled without changing the canonical path.

## Related docs

- `docs/reference/extensions-guide.md`
- `docs/reference/custom-architecture.md`
- `docs/research/game-development/foundations/extensions.md`
- `studio/extensions/custom/eval-plan.md`
- `studio/checklists/discipline/extensions.toml`
- `studio/extensions/README.md`
- `studio/extensions/custom/README.md`
