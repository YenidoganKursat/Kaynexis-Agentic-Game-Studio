# Agent Speed Pack Example

## Scope

- Keep a narrow UI fix or gameplay adjustment moving with the shortest safe bundle.

## Baseline

- The route should stay narrow.
- The user summary should stay short.
- The proof path should stay explicit.
- Extra history artifacts should stay out unless later review is needed.

## Decision order

1. Pick a single specialist if one owner can finish safely.
2. Surface only the docs needed to start.
3. Use one checklist bundle.
4. Add a packet, journal, or transcript only if the task should be reopened later.

## Example speed pack

- Task: Keep the inventory badge from clipping in a small HUD slot.
- Owner: technical_director
- Mode: single-specialist
- Fast bundle: quick-access, agent speed pack, UI guide, quality guide
- Proof path: one UI smoke plus one screenshot plus one short note
- Later review: prompt journal only if the fix should be reopened later

## Good agent prompts

- "Give me the speed pack for a short HUD polish and keep the proof path minimal."
- "Route the task through the fastest safe bundle and do not fan out unless needed."
- "Prepare the smallest reviewable bundle for a narrow gameplay fix."

## Validation

- One route
- One checklist
- One proof path
- One short user summary
- One durable doc update only if repo behavior changed

## Related docs

- `docs/reference/agent-speedpack.md`
- `docs/setup/quick-access.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-execution.md`
- `docs/reference/workflow-recipes.md`
- `studio/checklists/discipline/speedpack.toml`
