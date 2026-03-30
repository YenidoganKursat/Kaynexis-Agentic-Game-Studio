# Custom Architecture

## Date

2026-03-30

## Summary

Project-specific architecture work should keep the canonical owner, fixed rules, overrideable rules, and fallback behavior explicit before implementation starts.
If the work is really a registry of reusable custom feature bundles, start with `docs/reference/custom-packs.md` first.

## Primary sources

- https://martinfowler.com/articles/scaling-architecture-conversationally.html
- https://platform.openai.com/docs/guides/agents-sdk
- `docs/reference/custom-packs.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
- `docs/examples/custom-architecture-example.md`
- `studio/checklists/discipline/custom.toml`
- `studio/checklists/custom/README.md`

## Why this matters to this repo

- The repo already has architecture families, agent lanes, and review trails.
- Custom requests and house rules need a durable shape so they can be reviewed later.
- A broader custom pack registry sits above the narrower custom request contract.
- A custom lane keeps project-specific rules separate from the canonical architecture families.

## Decision impact

- Treat a custom request as a contract, not a chat note.
- Keep fixed rules separate from overrideable rules.
- Name the precedence order and fallback path before implementation.
- Record the rule pack in docs so future tasks can reopen it quickly.

## Custom process

1. Classify the work as custom architecture, custom rule pack, or custom request.
2. Name the canonical owner and the override owner.
3. Define the request contract and the precedence order.
4. Decide what falls back to the standard architecture when a custom rule is missing.
5. Capture one validation path and one review trail.

## Request and rule pack shape

- request source
- fixed rules
- override hooks
- precedence order
- fallback
- proof path

## Repo impact

- Route and checklist surfaces can now point to a dedicated custom lane.
- Project-specific overrides can live in `studio/checklists/custom/` without replacing the shared discipline contract.

## Related docs

- `docs/reference/custom-architecture.md`
- `docs/reference/custom-packs.md`
- `docs/examples/custom-architecture-example.md`
- `docs/examples/custom-packs-example.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `studio/docs/active/custom-packs-adr.md`
- `studio/docs/active/eval-custom-architecture.md`
- `studio/docs/active/eval-custom-packs.md`
