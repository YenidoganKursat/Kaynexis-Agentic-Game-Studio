# Agent Speed Pack

## Summary

Use this guide when the task needs the fastest safe start.
The speed pack keeps single-specialist mode visible, gives the agent the smallest useful bundle, and only opens heavier layers when the task actually needs them.
If the work should be reopened later, pair this guide with the prompt journal, transcript, or execution packet as needed, but do not add those layers by default.

## Primary sources

- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- AutoGen: https://arxiv.org/abs/2308.08155
- CAMEL: https://arxiv.org/abs/2303.17760
- HuggingGPT: https://arxiv.org/abs/2303.17580
- MetaGPT: https://arxiv.org/abs/2308.00352
- ChatDev: https://arxiv.org/abs/2307.07924
- [OpenAI Developers](https://developers.openai.com/)
- [Agents SDK](https://platform.openai.com/docs/guides/agents-sdk)
- [Evaluation best practices](https://platform.openai.com/docs/guides/evaluation-best-practices)

## Why this matters to this repo

- The repo already has route, checklist, packet, journal, transcript, and validation surfaces.
- A speed pack prevents the first answer from becoming a long operating-model detour.
- It keeps the user-facing summary short while still giving the agent enough to start.
- It makes the fastest safe path explicit instead of relying on a vague "be quick" instruction.

## Decision impact

- Start with the speed pack when the ask is urgent, narrow, or needs a crisp first pass.
- Keep single specialist mode visible unless proof rows say otherwise.
- Use execution packets only when work should be reopened later or needs a durable pre-flight contract.
- Use prompt journal or transcript only when later review matters.
- Keep validation short: one route, one checklist, one proof path.

## Fast path bundle

- route
- one checklist
- one active doc if needed
- one proof path
- packet, journal, or transcript only when necessary

## Speed rules

- If the task can fit in one owner, keep it there.
- If the task needs multiple lanes, use the smallest panel that can answer safely.
- If the task is only a quick answer, do not fan out into history artifacts unless asked.
- If you need later review, add the history trail as part of the same change.

## How to use it

- Use `python3 scripts/codex_studio.py next "<task>"` for the fastest route.
- Use `python3 scripts/codex_studio.py checklist --task "<task>"` to collect only the needed proof items.
- Open `docs/setup/quick-access.md` when you want the one-page launcher.
- Open `docs/reference/agent-system.md` when the work may branch into multiple lanes.
- Open `docs/reference/agent-execution.md` only if the task needs a durable packet.

## Example prompts for the agent

- "Give me the speed pack for a short UI fix and keep the proof path minimal."
- "Route this task through the fastest safe path and keep the summary short."
- "Prepare the smallest bundle the agent needs for a narrow gameplay slice."

## Validation

A good speed-pack pass should leave behind:

- one route
- one checklist
- one proof path
- one short user summary
- one durable doc update only if repo behavior changed
- prompt history, transcript, and execution packet only when later review actually matters

## Related docs

- `docs/setup/quick-access.md`
- `docs/reference/studio-map.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-execution.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
- `docs/examples/agent-speedpack-example.md`
- `docs/research/game-development/foundations/agent-speedpack.md`
- `studio/checklists/discipline/speedpack.toml`
- `studio/docs/active/eval-agent-speedpack.md`
