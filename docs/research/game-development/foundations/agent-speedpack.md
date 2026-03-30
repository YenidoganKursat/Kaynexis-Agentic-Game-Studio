# Research Note: Agent Speed Pack

## Date

2026-03-30

## Summary

The fastest safe agent work in this repo comes from shrinking the first bundle, not from skipping validation.
A speed pack gives the agent one route, one checklist, one proof path, and only the durable extras that the task actually needs.

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

- Broad prompts get slower when the first contract is vague.
- The speed pack keeps the single-specialist path visible while still giving the agent enough context to start.
- The repo already has controller, packet, journal, transcript, and validation surfaces, so the speed pack should choose the smallest useful subset instead of repeating all of them every time.
- A fast path keeps the user-facing answer short and the review path legible.

## Decision impact

- Add a dedicated fast-path guide, example, checklist, and eval plan.
- Keep speed-pack requests routed separately from the heavier controller, packet, and history lanes.
- Keep prompt journal and transcript as opt-in when the task should be reopened later.
- Keep validation short enough that the first pass still feels fast.

## Repo impact

- Route tasks that ask for the fastest safe start to a dedicated speed-pack lane.
- Keep the quick-access page, studio map, agent-system guide, and execution-packet guide aligned with the lane.
- Keep validators checking the speed-pack guide, example, research note, checklist, and eval plan together.

## Related docs

- `docs/reference/agent-speedpack.md`
- `docs/examples/agent-speedpack-example.md`
- `docs/setup/quick-access.md`
- `docs/reference/studio-map.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-execution.md`
- `studio/checklists/discipline/speedpack.toml`
- `studio/docs/active/eval-agent-speedpack.md`
