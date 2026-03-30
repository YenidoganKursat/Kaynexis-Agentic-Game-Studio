# Agent Hierarchy

## Date

- 2026-03-29

## Summary

- Broad orchestration works best when the controller is separate from the specialists and each lane has a named title.
- The repo should support a command tree with single specialist, paired specialist, and multi-agent panel modes.
- The single specialist option must always remain available and should stay the default unless a broader tree is clearly justified.

## Primary sources

- ReAct — https://arxiv.org/abs/2210.03629
- Reflexion — https://arxiv.org/abs/2303.11366
- Tree of Thoughts — https://arxiv.org/abs/2305.10601
- AutoGen — https://arxiv.org/abs/2308.08155
- CAMEL — https://arxiv.org/abs/2303.17760
- HuggingGPT — https://arxiv.org/abs/2303.17580
- MetaGPT — https://arxiv.org/abs/2308.00352
- ChatDev — https://arxiv.org/abs/2307.07924

## Why this matters to this repo

- The repo already has many specialist agents for design, engineering, QA, release, content, and presentation.
- Without a hierarchy note, broad requests can blur those lanes into a generic "agent" bucket.
- A command tree keeps each agent narrow enough to be testable, delegable, and easy to hand off.

## Decision impact

- Single specialist mode is the default path.
- A hierarchical panel should only be used when the request truly needs nested ownership or parallel lanes.
- Public titles should make it obvious who is the software architect, quality controller, creator lead, or release owner.
- The command tree should fit in one short control plan so the user summary stays simple.

## Repo impact

- Broad requests should surface `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, and `docs/reference/agent-hierarchy.md` before implementation.
- Specialist handoffs should stay narrow and name what each worker owns and does not own.
- When the task is likely to fan out, the user summary should stay short and the validation path should stay short.
- Async status packets should be treated as durable evidence, not as chat noise.

## Async contract

- Each lane returns a short packet with title, owner, reports_to, scope, blockers, evidence, next_action, and status.
- Blocked lanes escalate to their parent; they do not fan out sideways.
- The controller merges the packets and publishes one simple summary.

## Related docs

- `docs/reference/agent-hierarchy.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/examples/agent-hierarchy-example.md`
