# Eval Plan: Extensions Routing

## Goal

Verify that custom extension or plugin-pack tasks surface the extension guide, example, research note, checklist, and repo structure before implementation starts.

## Scope

- custom extension packs
- plugin-like add-ons
- opt-in hook packs
- project-specific manifests

## Expected behavior

- The router should surface `docs/reference/extensions-guide.md` and `docs/examples/extensions-example.md` for extension-pack prompts.
- The checklist resolver should surface `studio/checklists/discipline/extensions.toml` for extension-pack work.
- The guidance should keep the canonical architecture, the custom rule contract, and the extension pack separate.

## Validation

- Run one route query for an extension-pack prompt.
- Run one checklist query for the same prompt.
- Confirm the extension guide explains manifest fields, hook points, and fallback behavior.
- Confirm the extension example shows a small manifest and a narrow proof path.

## Exit criteria

- Extension tasks resolve to the correct lane.
- The docs index, checklist index, and route output all point at the same extension pack contract.
- The validation path is narrow and repeatable.
