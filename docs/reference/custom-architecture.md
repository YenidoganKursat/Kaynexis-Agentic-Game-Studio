# Custom Architecture Guide

## Summary

Use this guide when the task needs project-specific architecture, house rules, or overrideable request contracts that are not covered by the standard authority, event, state, and projection families.
If the request is really about a reusable pack registry or broader custom feature bundle, start with `docs/reference/custom-packs.md` first.

## Primary sources

- `docs/reference/architecture-guide.md`
- `docs/reference/custom-packs.md`
- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
- `studio/checklists/discipline/custom.toml`
- `studio/checklists/custom/README.md`

## Why this matters to this repo

- The repo already has clear architecture families for authority, events, state, and projection.
- Some tasks need a project-specific contract on top of those families instead of a new runtime system.
- Some tasks need a reusable pack registry above the narrower custom contract.
- A dedicated custom lane keeps house rules, overrides, and request contracts reviewable instead of leaving them in chat.

## Decision impact

- Use custom architecture only when the standard architecture guide is too broad.
- Keep fixed rules separate from overrideable rules.
- Name the owner, the request contract, the precedence order, and the fallback behavior before implementation.
- Do not let custom rules silently replace canonical architecture.

## Custom process

1. Classify the request as custom architecture, custom rule pack, or custom request.
2. Name the canonical owner and the part that can be overridden.
3. Define the request contract: fixed inputs, allowed overrides, and forbidden overrides.
4. Write the rule precedence order and the fallback behavior.
5. Add one validation path and one durable note.
6. Keep the guide, example, checklist, and eval plan aligned.

## Request contract model

- fixed rules
- overrideable rules
- request source
- owner
- fallback
- validation path

## Example prompts for the agent

- "Design a custom architecture and rule pack for project-specific inventory overrides."
- "Define a custom request contract that lets designers change pacing rules without changing canonical combat ownership."
- "Build a custom rule layer for a mod-friendly UI flow while keeping the projection boundary explicit."

## Validation

- Name fixed versus overrideable rules.
- Name the owner and the fallback.
- Name the precedence order.
- Run one narrow smoke, test, or review pass that proves the contract works.

## Related docs

- `docs/examples/custom-architecture-example.md`
- `docs/examples/custom-packs-example.md`
- `docs/research/game-development/foundations/custom-architecture.md`
- `docs/research/game-development/foundations/custom-packs.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/custom-packs.md`
- `docs/reference/extensions-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `studio/checklists/discipline/custom.toml`
- `studio/checklists/custom/README.md`
- `studio/docs/active/eval-custom-architecture.md`
- `studio/docs/active/custom-packs-adr.md`
- `studio/docs/active/eval-custom-packs.md`
