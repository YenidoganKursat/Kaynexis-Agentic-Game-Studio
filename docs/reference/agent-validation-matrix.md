# Agent Validation Matrix Guide

Use this guide when you need a compact way to prove that an agent system decision, role map, hierarchy, transcript trail, or model override is actually safe to keep.

The goal is not to invent a giant benchmark. The goal is to make the smallest useful validation matrix that another operator can replay later.

## Summary

- Keep the single-specialist option visible unless the task truly needs a panel.
- Keep the controller title, role names, and lane ownership explicit.
- Keep prompt history, transcript history, and review evidence separate but linked.
- Use one matrix when you need to compare operating modes, lane ownership, or proof paths.

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

- The repo already has routing, role mapping, a command tree, prompt history, and agent transcript support.
- A validation matrix keeps those decisions reviewable instead of burying them in chat history.
- The same matrix vocabulary can be reused across mastermind, portfolio, hierarchy, model choice, and review-trail tasks.
- The matrix also makes it easier to explain why single-specialist mode was kept or why a panel was chosen.

## Decision impact

- Single specialist mode stays visible.
- A matrix is only used when the task benefits from explicit comparison rows.
- The matrix should name the controller, the lane, the proof path, and the evidence path.
- If the work fans out, the matrix should make the default lane model and any explicit override visible.

## Matrix catalog

| Matrix | Use when | Must prove | Good signal | Common failure |
| --- | --- | --- | --- | --- |
| Operating mode matrix | Choosing between single specialist, pair, or panel | The chosen mode matches the task size | One simple mode decision | Choosing panel mode by habit |
| Role matrix | Splitting work across specialist lanes | Each lane owns one narrow scope | Ownership and non-ownership are clear | Lanes overlap and blur responsibility |
| Hierarchy matrix | Reporting lines or async packets matter | Each lane reports to one parent | Titles, parent tiers, and packet shape are explicit | Sideways ownership appears |
| Model matrix | Lane-specific model overrides are needed | Defaults and overrides are visible | The selected model is named per lane | Overrides are hidden from the review trail |
| Prompt history matrix | The work should be easy to reopen later | Prompt history is preserved append-only | User prompt, route, and summary stay linked | Prompt notes are scattered in chat |
| Transcript matrix | Agent-to-agent assignments or replies matter | Assignment history and replies stay separate from prompt history | Speaker, target, and message are short and timestamped | Transcript grows into raw chat dumps |
| Controller matrix | The controller workflow itself changes | Controller, validation path, and review trail are explicit | Kaynexis title and control loop stay visible | Controller policy is vague |

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible"
python3 scripts/codex_studio.py checklist --task "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible"
python3 scripts/codex_studio.py next "Define the smallest validation matrix that still proves the controller, hierarchy, transcript, and model overrides are safe"
```

## Validation

A good agent-validation pass should leave behind:

- one simple user summary
- one matrix that names the operating mode or lane split
- one proof path
- one evidence path
- one durable doc update if the agent behavior changed repo behavior
- one prompt-history entry, one agent journal note, and one transcript entry if the work should be reopened later

## Related docs

- `docs/examples/agent-validation-matrix-example.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/codex-model-guide.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/research/game-development/foundations/agent-validation-matrix.md`
