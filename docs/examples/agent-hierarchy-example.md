# Agent Hierarchy Example

## Scope

A broad request that needs a clear controller, explicit titles, and a small async command tree while still keeping single specialist mode available:

- decide whether the request should stay single-agent or fan out
- assign the Kaynexis controller title and scientist public titles like Alan Turing and Rosalind Franklin to the specialist lanes
- keep every lane narrow and accountable

## Example input

> Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane, but keep the single specialist option available if the scope shrinks.

## Output shape

The controller should answer in this order:

1. one simple user summary
2. one operating mode decision
3. one command tree with public titles
4. one async packet map
5. one validation path

## Good control-plan shape

- Read the master mind guide first.
- Use the agent hierarchy to name the controller, director, lead, specialist, and validator tiers.
- Keep single specialist mode as the default if one lane can safely own the work.
- Assign one owner to each lane and name what that lane does not own.
- Verify the mode against docs, checklists, or a narrow test path.

## Example answer sketch

User summary:

- "I split the request into a controller and a small async tree so each lane stays narrow and the single specialist path remains available."

Mode decision:

- `multi-agent panel`

Command tree:

- `mastermind`: Kaynexis, controller, summary, validation order
- `technical_director`: Alan Turing, software architect, boundaries, feasibility
- `ui_programmer`: Grace Hopper, creator lead for the UI lane
- `qa_lead`: Rosalind Franklin, quality controller, validation and evidence

Async packet:

- `title`: `Alan Turing` / software architect
- `owner`: `technical_director`
- `reports_to`: `mastermind`
- `scope`: UI projection boundary and data ownership
- `blockers`: unresolved engine constraint or missing UI contract
- `evidence`: doc link, command output, or screenshot
- `next_action`: narrow implementation slice
- `status`: `ready` / `blocked` / `done`

Validation:

- `python3 scripts/route_task.py "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane, but keep the single specialist option available if the scope shrinks" --json`
- `python3 scripts/codex_studio.py checklist --task "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane, but keep the single specialist option available if the scope shrinks" --json`

## What good looks like

- Each lane has one obvious owner.
- The controller stays simple and readable.
- The user gets the summary, not the internal chatter.
- The single specialist option is still visible when the task is actually narrow.

## Related docs

- `docs/reference/agent-hierarchy.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-guide.md`
