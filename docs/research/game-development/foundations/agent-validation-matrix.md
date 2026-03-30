# Agent Validation Matrix

## Date

2026-03-30

## Summary

- Multi-agent control needs a durable matrix that proves when to stay single, when to pair, and when to fan out.
- The repo already has separate durable records for prompt history and agent transcript, so the validation matrix should point at both instead of copying them.
- The matrix should stay small enough that another operator can replay it without re-reading the full chat.

## Primary sources

- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- AutoGen: https://arxiv.org/abs/2308.08155
- CAMEL: https://arxiv.org/abs/2303.17760
- HuggingGPT: https://arxiv.org/abs/2303.17580
- MetaGPT: https://arxiv.org/abs/2308.00352
- ChatDev: https://arxiv.org/abs/2307.07924

## Why this matters to this repo

- This repo already uses role matrices, command trees, prompt journals, and transcripts to keep broad tasks reviewable.
- A validation matrix gives those structures one compact proof path.
- The matrix also makes lane-specific model overrides easier to justify later.

## Decision impact

- Single specialist mode stays visible and remains the default.
- A validation matrix is the right output when the question is "how do we prove this operating model choice?"
- The matrix should separate mode, ownership, evidence, and review trail.

## Matrix families

| Family | What it answers | Typical owner | Repo impact |
| --- | --- | --- | --- |
| Operating mode matrix | Stay single, pair, or panel? | producer | Keeps internal fan-out small |
| Role matrix | Which lane owns what? | technical_director | Keeps ownership narrow |
| Hierarchy matrix | Who reports to whom? | mastermind | Keeps async packets explicit |
| Transcript matrix | What gets recorded for later review? | docs_researcher | Keeps assignments and replies durable |
| Model matrix | Which lane uses which model? | technical_director | Keeps tradeoffs visible |
| Review matrix | Which command proves the decision? | qa_lead | Keeps the proof path small |

## Repo impact

- Add a routable guide, example, checklist, and eval plan for agent validation matrices.
- Keep the new matrix catalog linked from the agent system, portfolio, hierarchy, and prompt/transcript docs.
- Keep validation short: one command, one doc, one artifact, one summary.

## Related docs

- `docs/reference/agent-validation-matrix.md`
- `docs/examples/agent-validation-matrix-example.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/research/openai-codex-models.md`
