# Agent Portfolio

## Date

- 2026-03-29

## Summary

- Broad agent work is easier to maintain when each agent stays in a single lane and the controller chooses the smallest useful panel.
- The repo should support three clear modes: single specialist, paired specialist, and multi-agent panel.
- The master mind is the controller that keeps the user-facing summary simple and the internal handoff map explicit.

## Primary sources

- ReAct — https://arxiv.org/abs/2210.03629
- Reflexion — https://arxiv.org/abs/2303.11366
- Tree of Thoughts — https://arxiv.org/abs/2305.10601
- AutoGen — https://arxiv.org/abs/2308.08155
- CAMEL — https://arxiv.org/abs/2303.17760
- HuggingGPT — https://arxiv.org/abs/2303.17580

## Why this matters to this repo

- The repo already has many specialist agents for design, engineering, QA, release, content, and presentation.
- Without a portfolio note, broad requests can blur those lanes into a generic "agent" bucket.
- A role matrix lets the controller pick the smallest panel that can answer the task safely.

## Decision impact

- Single-specialist mode is the default when the task has one clear owner and one narrow validation path.
- Paired-specialist mode is the right middle ground when one role can frame or inspect while another implements or validates.
- Multi-agent panel mode should only be used when the task clearly spans incompatible specialties or when the validation path needs independent review.
- The choice of mode changes the prompt structure, the handoff shape, and the expected evidence in the final answer.

## Repo impact

- Broad requests should surface `docs/reference/mastermind-guide.md` and `docs/reference/agent-portfolio.md` before implementation.
- Specialist handoffs should stay narrow and name what each worker owns and does not own.
- When the task is likely to fan out, the user summary should stay simple and the validation path should stay short.

## Related docs

- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/examples/agent-portfolio-example.md`
