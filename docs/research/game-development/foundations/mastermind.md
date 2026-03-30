# Master Mind

## Date

- 2026-03-29

## Summary

- Broad agent work in this repo is easier to maintain when one orchestration layer keeps the user-facing answer simple and the internal worker plan explicit.
- The master mind should behave like a controller: intake, classify, delegate, verify, and summarize.
- It should not absorb every specialist role; it should route to the right roles and preserve a narrow proof path.

## Primary sources

- ReAct — https://arxiv.org/abs/2210.03629
- Reflexion — https://arxiv.org/abs/2303.11366
- Tree of Thoughts — https://arxiv.org/abs/2305.10601
- AutoGen — https://arxiv.org/abs/2308.08155
- CAMEL — https://arxiv.org/abs/2303.17760
- HuggingGPT — https://arxiv.org/abs/2303.17580

## Why this matters to this repo

- The repo already has many specialist guides, checklists, and routing rules.
- A master mind layer keeps the broad user request from turning into a vague all-purpose assistant prompt.
- The controller model matches the repo's existing pattern: one durable summary, one control plan, one validation path, and specialist handoffs as needed.

## Decision impact

- Broad tasks should start with a simple user summary and a control plan.
- Specialist workers should own the narrow subproblems, not the orchestration layer.
- Durable docs should capture the control decision when routing behavior changes.
- Validation should stay close to the change so the orchestration can be checked quickly.

## Repo impact

- Add a dedicated master mind guide and example to the user-facing reference docs.
- Add a master mind checklist layer for control-loop, delegation, and validation discipline.
- Route broad orchestration tasks through the master mind keywords so the user gets a simple summary and the repo gets a clear handoff structure.
