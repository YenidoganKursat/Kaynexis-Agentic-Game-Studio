# Agent Portfolio Example

## Scope

A broad request that needs a clear controller and a small multi-agent panel, while keeping single specialist mode available:

- decide whether a task should stay single-agent or fan out
- keep the user summary simple
- assign each specialist a narrow lane and a scientist public title

## Example input

> Define a role matrix for the agent system so each agent stays narrow, and show when to use single specialist versus multi-agent panel mode.

## Output shape

The controller should answer in this order:

1. one simple user summary
2. one operating mode decision
3. one specialist role matrix
4. one handoff map
5. one validation path

## Good control-plan shape

- Read the master mind guide first.
- Use the agent portfolio to choose single specialist, paired specialist, or panel mode.
- Assign one owner to each lane and name what that lane does not own.
- Keep the internal delegation explicit and the user-facing summary short.
- Verify the mode against docs, checklists, or a narrow test path.

## Example answer sketch

User summary:

- "I split the request into a controller and specialist lanes so we can keep each agent narrow and the summary simple."

Mode decision:

- `single specialist`

Role matrix:

- `mastermind`: Kaynexis, control loop, handoffs, summary
- `producer`: Marie Curie, sequence, dependencies, risk
- `technical_director`: Alan Turing, boundaries, feasibility, architecture
- `docs_researcher`: Charles Darwin, evidence and primary sources

Single specialist baseline:

- `mastermind`: Kaynexis, control loop, handoffs, summary

Validation:

- `python3 scripts/route_task.py "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode" --json`
- `python3 scripts/codex_studio.py checklist --task "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode" --json`

## What good looks like

- Each agent has one obvious lane.
- The controller stays simple and readable.
- The user gets the summary, not the internal chatter.

## Related docs

- `docs/reference/agent-portfolio.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-guide.md`
