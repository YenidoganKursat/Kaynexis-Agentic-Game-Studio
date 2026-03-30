# Agent System Guide

## Summary

Use this guide when the task is about the repo's overall multi-agent operating model, not just one orchestration mode.
The operating model keeps single specialist mode visible, uses `Kaynexis` as the controller title, and keeps specialist lanes narrow and reviewable.
If the work should stay single-agent, this guide still helps by making that decision explicit instead of implicit.
If the task needs a durable pre-flight contract, pair this guide with `docs/reference/agent-execution.md` so the owner, mode, proof path, and custom rules are explicit before work starts.
If the task only needs the fastest safe start, pair this guide with `docs/reference/agent-speedpack.md` so the bundle stays short and the first proof path stays obvious.

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

- The repo already has a controller, a role matrix, a command tree, a validation matrix catalog, an execution packet, and an append-only review trail.
- A single operating-model page keeps those pieces aligned instead of scattering them across chat.
- Users can see one simple answer while the controller decides whether to stay single, pair up, or fan out.
- Role-specific checklist packs in `studio/checklists/discipline/` keep durable lanes narrow enough for review.

## Decision impact

- Single specialist mode stays the default.
- The controller title is `Kaynexis`.
- Specialist lanes keep scientist public titles in summaries, route output, and async packets.
- Specialist lanes also keep their default model from `.codex/agents/*.toml` visible, and the user can override a lane explicitly with `--agent-model agent=model` when the task needs a different tradeoff.
- Role matrix, hierarchy, validation matrix, execution packet, prompt journal, and transcript should be treated as one operating contract when the task touches agent behavior.

## OpenAI / Codex alignment

- If the task is about OpenAI, Codex, or agent-platform wiring, start with `docs/research/openai-codex-infra-findings.md` and `docs/reference/codex-compatibility.md`.
- If the task is about model choice or plan-tier fit, also start with `docs/research/openai-codex-models.md` and `docs/reference/codex-model-guide.md`.
- If the model decision itself needs a durable control path, pair that with `docs/examples/codex-model-guide-example.md`, `studio/checklists/discipline/openai_models.toml`, and `studio/docs/active/eval-openai-models.md`.
- Keep controller policy stable and put task-specific details, examples, and constraints in the routed prompt or workflow note.
- Treat prompt versions, eval plans, and traceable review paths as part of the operating model, not as an afterthought.
- Keep tool approvals and internet-access assumptions explicit whenever a workflow leaves the repo boundary.
- Prefer the smallest workflow that still keeps ownership obvious: single specialist first, paired specialist second, small panel only when the task truly branches.
- Use `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md` when the workflow itself needs a durable control contract.

## Operating model

1. Start from the user outcome.
2. Decide if one specialist owns the work.
3. If not, choose the smallest panel that can answer safely.
4. Add a hierarchy only when the task needs explicit reporting lines or async packets.
5. Add an execution packet when the task needs a pre-flight contract.
6. Add the prompt journal and transcript whenever the result should be easy to reopen later.
7. Keep the user-facing summary simple and the validation path short.

## Core layers

- `docs/reference/mastermind-guide.md` for the controller loop and broad orchestration
- `docs/reference/capabilities.md` and `docs/examples/capabilities-example.md` for the repo-wide capability surface when the user wants the whole studio brochure before diving into a lane
- `docs/reference/agent-portfolio.md` for single specialist, paired specialist, and panel selection
- `docs/reference/agent-hierarchy.md` for command trees, reporting lines, and async packets
- `docs/reference/agent-validation-matrix.md` for validation matrices that prove an operating-model choice
- `docs/reference/agent-speedpack.md` for the fastest safe start and the smallest useful bundle
- `docs/reference/agent-execution.md` for work packets that name the owner, mode, goal, proof path, and custom rules before implementation
- `docs/reference/prompt-journal.md` for append-only prompt history and agent notes
- `docs/reference/agent-transcript.md` for append-only task assignments and agent conversation turns
- `docs/reference/workflow-recipes.md` for the most repeatable agent-system workflows
- `docs/reference/task-prompt-examples.md` for prompt shapes that route cleanly
- `docs/reference/codex-model-guide.md` for model and plan-tier selection
- `scripts/route_task.py` and `scripts/codex_studio.py next` for explicit sub-agent model overrides when the user wants a different lane tradeoff
- `docs/reference/feature-traceability.md` for durable review trail coupling
- `docs/examples/agent-transcript-example.md` for a concrete transcript review bundle
- `docs/research/openai-codex-infra-findings.md` for OpenAI/Codex-specific workflow guidance
- `docs/research/openai-codex-models.md` for the source-backed model and plan-tier matrix
- `docs/reference/codex-compatibility.md` for platform and repo-compatibility guardrails
- `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md` for the durable control contract behind OpenAI/Codex workflows

## Example prompts for the agent

- "Prepare the repo for a multi-agent system with single-specialist default, Kaynexis controller title, role matrix, hierarchy, prompt journal, transcript, and review trail."
- "Keep the single specialist path visible while you set up a controller, a role matrix, and a command tree."
- "Keep the speed pack visible while you route a task through the fastest safe path."
- "Build a validation matrix for the agent system and keep the single specialist path visible."
- "Build an execution packet for a multi-agent slice and keep the proof path and custom rules explicit."
- "Define the smallest operating model that still keeps the review trail durable later."

## Validation

A good agent-system pass should leave behind:

- one simple user summary
- one controller decision
- one role matrix or command tree
- one validation matrix when the task changes agent behavior
- one execution packet when the task needs a pre-flight contract
- one review trail if the work should be reopened later
- one narrow validation path
- one durable doc update if the agent behavior changed
- one speed pack instead of a full packet when the task only needs the fastest safe start

## Related docs

- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/agent-validation-matrix.md`
- `docs/reference/agent-execution.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/examples/agent-system-example.md`
- `docs/examples/agent-speedpack-example.md`
- `docs/examples/agent-transcript-example.md`
- `docs/examples/agent-validation-matrix-example.md`
- `docs/examples/agent-execution-example.md`
- `docs/reference/agent-speedpack.md`
- `docs/research/game-development/foundations/agent-system.md`
- `docs/research/game-development/foundations/agent-execution.md`
- `docs/reference/codex-model-guide.md`
- `docs/research/openai-codex-models.md`
