# Master Mind Example

## Scope

A broad request that needs orchestration, not just implementation:

- coordinate a multi-step engine and genre research task
- keep the user-facing summary simple
- hand off specialist work internally

## Example input

> Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs.

## Output shape

The master mind should answer in this order:

1. one simple user summary
2. one control plan
3. one list of specialist handoffs
4. one validation path
5. one risk note

## Good control-plan shape

- Read the current repo state and the relevant docs first.
- Pick the smallest specialist set that can answer the task.
- Delegate only the narrow subproblem that each worker owns.
- Keep the user summary short and plain.
- Verify the output against docs, tests, or commands before closing the loop.

## Example answer sketch

User summary:

- "I turned the broad request into a Kaynexis control plan so we can keep the user output simple and route the specialist work cleanly."

Control plan:

1. Read the relevant guide and research note.
2. Hand off architecture, genre, and validation subtasks to the right specialists.
3. Verify the routed docs and checklist output.
4. Write the durable decision if the repo behavior changes.

Validation:

- `python3 scripts/codex_studio.py next "<task>"`
- `python3 scripts/codex_studio.py checklist --task "<task>"`
- the matching doc or test command for the actual change

## What good looks like

- The user never has to parse internal worker chatter.
- Each worker knows its owner, evidence, and validation path.
- The final summary is short enough to act on immediately.

## Related docs

- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-guide.md`
- `docs/reference/workflow-recipes.md`
