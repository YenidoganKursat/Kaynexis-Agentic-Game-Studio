# Agent System Example

## Scope

A task that needs the full operating model, not just one agent mode:

- keep the single specialist default visible
- make the `Kaynexis` controller title explicit
- keep the role matrix, hierarchy, and review trail aligned

## Example input

> Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail.

## Output shape

The controller should answer in this order:

1. one simple user summary
2. one operating mode decision
3. one role matrix or handoff map
4. one command tree if reporting lines matter
5. one review trail or prompt journal note
6. one validation path

## Good control-plan shape

- Read the agent-system guide first.
- Keep single specialist mode available unless the task truly needs a panel.
- Use `Kaynexis` for the controller title and keep specialist lanes narrow.
- Add the prompt journal when the work should be reviewable later.
- Verify the output against docs, checklist output, or a small command path.

## Example answer sketch

User summary:

- "I set up the agent operating model so the repo can stay single-specialist by default while still supporting a small multi-agent panel when needed."

Control plan:

1. Read the agent-system guide and the matching controller docs.
2. Keep the single specialist path visible.
3. Assign the controller title, role matrix, and command tree.
4. Record the prompt history and the agent journal trail.
5. Verify the routed docs and checklist output.

Validation:

- `python3 scripts/codex_studio.py next "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail" --json`
- `python3 scripts/codex_studio.py checklist --task "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, and review trail" --json`

## What good looks like

- The controller stays simple and readable.
- Single specialist mode is still available.
- The user gets one short summary, not internal worker chatter.
- The review trail makes the work easy to reopen later.

## Related docs

- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/prompt-journal.md`
