# Custom Packs Guide

## Summary

Use this guide when the task needs a reusable custom feature bundle that may combine fixed rules, overrideable rules, hook points, and fallback behavior.

Custom packs sit above the existing custom architecture and extension pack lanes. They are the umbrella shape for "more custom features" when a project wants a named registry instead of one-off chat instructions.

## Primary sources

- `docs/reference/custom-architecture.md`
- `docs/reference/extensions-guide.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/library-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
- `docs/research/game-development/foundations/custom-packs.md`
- `studio/checklists/discipline/custom_packs.toml`
- `studio/docs/active/custom-packs-adr.md`
- `studio/docs/templates/custom-packs.md`

## Why this matters to this repo

- The repo already separates canonical architecture from custom rule packs and extension packs.
- Some projects need a higher-level registry for custom feature bundles that can be reasoned about, enabled, disabled, and reviewed later.
- A pack registry keeps custom capabilities durable without turning every new request into a one-off exception.

## Decision impact

- Use a custom pack when the work needs a named bundle of custom rules, hooks, manifests, or override points.
- Keep the canonical architecture separate from the pack registry.
- Keep the pack owner, pack type, hook points, override points, and fallback explicit.
- Prefer a narrow pack that changes one feature family at a time.

## Pack families

| Pack family | What it is for | Examples |
| --- | --- | --- |
| rule pack | fixed versus overrideable behavior | inventory overrides, pacing overrides, project-specific rules |
| hook pack | opt-in attachment points around a canonical system | UI filters, debug overlays, editor helpers |
| feature pack | a named bundle that combines rules and hooks | inventory pack, accessibility pack, onboarding pack |
| tool pack | pipeline or editor helpers that accelerate custom work | pack registry, import helpers, review tools |

## Pack model

- `pack id`
- `pack type`
- `owner`
- `scope`
- `fixed rules`
- `overrideable rules`
- `hook points`
- `override points`
- `dependencies`
- `fallback`
- `validation path`

## Example prompts for the agent

- "Design a custom pack registry for project-specific inventory and UI overrides."
- "Define a feature pack that combines fixed combat rules with overrideable progression hooks."
- "Build a custom pack contract that keeps the fallback explicit when an optional hook is missing."

## Validation

- Name the pack type and the canonical owner.
- Name the fixed rules, overrideable rules, hook points, and fallback.
- Keep the guide, example, research note, checklist, and eval plan in sync.
- Run one narrow smoke, test, or review path that proves the pack works.

## Related docs

- `docs/examples/custom-packs-example.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/extensions-guide.md`
- `docs/reference/architecture-guide.md`
- `docs/research/game-development/foundations/custom-architecture.md`
- `docs/research/game-development/foundations/extensions.md`
- `studio/docs/templates/custom-packs.md`
- `studio/docs/active/custom-packs-adr.md`
- `studio/docs/active/eval-custom-packs.md`
