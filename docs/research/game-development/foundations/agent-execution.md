# Research Note: Agent Execution Packet

## Date

2026-03-30

## Summary

The repo already uses role matrices, command trees, prompt journals, transcripts, and validation matrices to keep agent work reviewable.
An execution packet adds the missing pre-flight contract: it says who owns the work, which mode is active, what the goal is, what inputs matter, what outputs are expected, what proof path will count, and which custom rules must stay visible.

## Why this matters to this repo

- Broad tasks get slower when the first contract is vague.
- A packet keeps single-specialist mode visible while still allowing paired or panel work when needed.
- The packet is durable enough to reopen later without rereading the whole conversation.
- The packet gives routing, checklist, journal, transcript, and validation one shared pre-flight frame.

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

## Why this matters

- Broad tasks slow down when the first contract is vague.
- A work packet reduces repeated interpretation and keeps the first proof path obvious.
- Custom rules, project overrides, and stop conditions stay visible instead of being scattered across chat messages.
- The packet is a durable artifact the user can reopen later without rereading the whole conversation.

## Decision impact

- Add a routable guide, example, checklist, and eval plan for execution packets.
- Keep the packet separate from prompt history, agent journal notes, transcripts, and validation matrices.
- Keep single-specialist mode visible even when the packet names a pair or a panel.
- Use the packet to front-load the owner, mode, proof path, and override rules before implementation starts.

## Packet families

| Family | Decision use |
| --- | --- |
| Single specialist packet | One narrow owner can finish the task |
| Paired packet | One doer plus one checker is enough |
| Panel packet | Several bounded lanes need explicit reporting lines |
| Handoff packet | Work moves between workers and needs a clear next owner |
| Custom rule packet | The task has project-specific overrides or house rules |

## Repo impact

- Route tasks that mention work packets or execution packets to a dedicated lane.
- Surface the packet guide in the agent system, hierarchy, transcript, and traceability docs.
- Keep the packet checklist aligned with the rest of the agent stack when routing behavior changes.

## Related docs

- `docs/reference/agent-execution.md`
- `docs/examples/agent-execution-example.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/agent-validation-matrix.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
