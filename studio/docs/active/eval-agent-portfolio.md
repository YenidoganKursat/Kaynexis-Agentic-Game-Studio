# Eval Plan: Agent Portfolio

## Change under test

- Add a repo-wide agent portfolio that lets the controller choose single specialist, paired specialist, or multi-agent panel mode.

## Goal

- Ensure broad requests can be mapped to a small specialist panel instead of a generic catch-all agent.
- Ensure the user-facing answer stays simple even when the internal plan fans out.

## Cases

1. `Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode`
2. `Keep the agent summary simple while assigning producer, technical director, docs researcher, and qa roles`
3. `Break a broad request into specialist lanes and name what each role does not own`
4. `Use the agent portfolio to decide whether one specialist or a paired handoff is enough`

## Success criteria

- The route or checklist output names the controller and specialist lanes.
- The summary stays short and plain-language.
- The role matrix is explicit enough to tell ownership apart.
- The validation path is narrow.

## Related docs

- `docs/reference/agent-portfolio.md`
- `docs/reference/mastermind-guide.md`
- `docs/examples/agent-portfolio-example.md`
- `docs/research/game-development/foundations/agent-portfolio.md`
