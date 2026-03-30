# Agent System

## Date

- 2026-03-29

## Summary

- The repo should expose one operating model for multi-agent work instead of scattering the same decision across several pages.
- Single specialist mode must remain the default.
- When the work fans out, the controller, role matrix, hierarchy, and prompt journal should all stay visible together.

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

- The repo already has dedicated docs for the controller, role matrix, hierarchy, and review trail.
- A single operating-model note keeps those layers aligned when the work is broad.
- The user-facing summary stays simple while the control plan stays explicit.

## Decision impact

- Keep single specialist mode visible in every portfolio and hierarchy decision.
- Keep the `Kaynexis` controller title stable.
- Keep the scientist public titles for specialist lanes stable.
- Keep prompt history and agent journal entries append-only when the task should be reviewed later.

## Repo impact

- Add an umbrella agent-system guide and example that point to the controller, portfolio, hierarchy, and journal docs.
- Route explicit multi-agent-system requests to the operating model instead of only the portfolio or hierarchy lanes.
- Keep the checklists and active docs aligned with the new umbrella page.

