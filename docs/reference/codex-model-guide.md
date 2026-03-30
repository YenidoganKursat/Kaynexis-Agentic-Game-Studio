# Codex Model Guide

This guide is the short operational companion to `docs/research/openai-codex-models.md`.

Use it when an agent needs to answer one of these questions:

- Which OpenAI model should I use for this task?
- Which ChatGPT / Codex plan tier is the practical fit?
- What is the smallest model that still keeps the task safe?
- When is a harder model worth the extra cost and latency?

## Default ladder

| Model or plan | Best use | Weak spot | Repo rule |
| --- | --- | --- | --- |
| `gpt-5.4` | Broad coding, architecture, long-context reasoning, tool-heavy agent work | Too expensive for trivial extraction or routing | Start here when the task is genuinely hard |
| `gpt-5.4-pro` | Hard correctness, high precision, toughest reasoning tasks | Slower and more expensive than the default | Use only when the extra compute is worth it |
| `gpt-5.4-mini` | Subagents, cheap fan-out, coding helpers, computer-use helpers | Not the right final pass for the hardest synthesis | Use when you want speed, cost control, and enough intelligence |
| `gpt-5.4-nano` | Simple classification, extraction, ranking, and routing | Weak on broad reasoning or deep synthesis | Use only for high-volume lightweight work |
| Free / Go | Trial or light ChatGPT/Codex app use | Limited fit for heavy work | Do not treat this as the default serious work surface |
| Plus | Individual daily use | Still a personal plan, not a team control surface | Good fit for one developer using Codex often |
| Pro | Power-user ChatGPT/Codex work and developer mode | May still be too much if the task is simple | Good fit when the user wants the strongest personal surface |
| Business / Enterprise / Education | Team or org-managed usage | Overkill for solo testing | Good fit when admin control matters |

The plan guidance above is a practical fit rule derived from the current OpenAI docs. It is not a permanent entitlement contract.

## How to choose

1. Decide whether the task is about ChatGPT/Codex app usage or API usage.
2. Decide whether the task is broad reasoning, a small specialist worker, or a simple high-volume pass.
3. Pick the smallest model that still keeps the work safe.
4. If the task is a final correctness pass, only then consider `gpt-5.4-pro`.
5. If the task is a cheap helper or subagent, start with `gpt-5.4-mini`.
6. If the task is a simple router or extractor, use `gpt-5.4-nano`.
7. If the task is about plan tier or developer mode, record the surface and the tier explicitly.

## Sub-agent overrides

When a task fans out into specialists, the default model should still come from each agent profile in `.codex/agents/*.toml`.
If the user wants a different tradeoff for one lane, allow an explicit override with `--agent-model agent=model` on `scripts/route_task.py` or `scripts/codex_studio.py next`.

Good usage:

- keep the default model for most lanes
- override only the lanes that need extra precision or cheaper fan-out
- keep the override visible in route output, checklist output, and the review trail

Example:

```bash
python3 scripts/codex_studio.py next "Define a role matrix for a multi-agent UI and QA pass" --agent-model technical_director=gpt-5.4-pro --agent-model qa_lead=gpt-5.4-mini
```

Repo rule:

- do not hide model choice inside the route decision
- do not change the controller default just because one sub-agent needs a different model
- prefer the smallest model that can safely complete the lane

## When not to use a model

- Do not use `gpt-5.4-pro` for routine prompt tuning or short documentation edits.
- Do not use `gpt-5.4-mini` as the final authority when the task still needs deep synthesis.
- Do not use `gpt-5.4-nano` for architecture, release risk, or hard review work.
- Do not use older Codex-branded model names as the new default unless a legacy workflow requires them.

## Durable rule

When a model or plan decision matters, the agent should cite:

- `docs/research/openai-codex-models.md`
- `docs/research/openai-codex-infra-findings.md`
- `docs/reference/codex-compatibility.md`

and should leave the choice visible in the prompt journal, transcript, or eval note when the decision affects future work.
