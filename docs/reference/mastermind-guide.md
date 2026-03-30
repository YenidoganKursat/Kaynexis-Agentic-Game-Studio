# Master Mind Guide

Use this guide when a task is broad, cross-functional, or likely to split into specialist workers.

The master mind is the orchestration layer for this repo:

- it keeps the user-facing answer simple
- it turns a broad request into a narrow control plan
- it delegates work to specialist agents or roles
- it verifies the result with a small proof path
- it records durable decisions when the change should survive the chat

The master mind is not a "do everything" agent. It is a controller that keeps ownership clear and user output readable.
It should always keep the single specialist option alive; panel mode is a choice, not the default.
If the controller decision itself needs a proof trail, also read `docs/reference/agent-validation-matrix.md` and `docs/examples/agent-validation-matrix-example.md` so the control plan stays testable.
When titles are needed, keep the `Kaynexis` controller title and the scientist specialist titles consistent with `.codex/agents/*.toml` and the agent hierarchy docs.
For the full operating model above this controller, start with `docs/reference/agent-system.md` and `docs/examples/agent-system-example.md`.
If the task is about OpenAI, Codex, or agent-platform wiring, also read `docs/research/openai-codex-infra-findings.md` and `docs/reference/codex-compatibility.md` before splitting the work.
If the task needs a durable pre-flight contract, also read `docs/reference/agent-execution.md` and `docs/examples/agent-execution-example.md` so the owner, mode, proof path, and custom rules are explicit before the control loop fans out.
If the workflow itself needs a durable control contract, also read `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md`.

## Operating modes

- Single specialist mode: use one specialist when one lane clearly owns the answer.
- Paired specialist mode: use a doer plus a validator when the task is narrow but should be checked.
- Multi-agent panel mode: use the master mind plus 2-4 specialists when the request crosses design, implementation, docs, QA, or release boundaries.
- Controller-only mode: use the master mind to decide the route when the task is still too broad or ambiguous for implementation.

## Primary sources

- ReAct: https://arxiv.org/abs/2210.03629
- Reflexion: https://arxiv.org/abs/2303.11366
- Tree of Thoughts: https://arxiv.org/abs/2305.10601
- AutoGen: https://arxiv.org/abs/2308.08155
- CAMEL: https://arxiv.org/abs/2303.17760
- HuggingGPT: https://arxiv.org/abs/2303.17580

These sources all point in the same direction:

- interleave reasoning with action instead of pretending the first guess is final
- keep explicit reflection or memory when the work is multi-step
- explore alternatives when the problem branches
- use a controller to choose and sequence specialist tools or workers
- summarize the result after execution instead of exposing raw internal chatter to the user

## Why this matters to this repo

- The repo already has many specialist roles, atlases, and checklists.
- Broad tasks can drift unless one controller keeps the user summary, evidence, and handoffs aligned.
- A master mind gives the repo one predictable control loop for intake, delegation, verification, and durable doc updates.
- This improves operator usability without flattening the specialist roles that keep the repo maintainable.
- If the broad task includes state, authority, event, or projection architecture, the controller should pull in the architecture guide diagrams so the summary stays simple while the owner/boundary map stays explicit.
- If the work should be reopened later, the controller should also add a prompt-history entry and one agent journal note. If the task split across agents, also capture the assignment or conversation transcript so the review trail stays durable.

## Decision impact

When the master mind is used, it should always name:

- the user outcome
- the control loop
- the specialist roles or workers
- the evidence or source base
- the execution packet when the task needs a pre-flight contract
- the narrow validation path

If the task is still too vague to name a first validation path, the master mind should not start implementation yet.

## Master Mind control loop

1. Intake the request and restate the user outcome in one simple sentence.
2. Classify the work into the smallest useful disciplines or specialist roles.
3. Decide which docs, examples, atlases, or research notes need to be read first.
4. Delegate narrow subproblems to specialist workers or roles.
5. Verify the output against the repo, tests, docs, or measurements.
6. Summarize the result back to the user in simple language.
7. Record any durable decision in active docs when the change should persist.

## What to avoid

- Do not hide the plan inside a long stream of internal reasoning.
- Do not let the master mind become the implementation owner for every subtask.
- Do not start broad work without an evidence base.
- Do not skip the validation path just because the request sounds managerial.

## Example prompts for the agent

- "Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs."
- "Run the master mind loop on a routing change and keep the user-facing answer short."
- "Break a broad request into specialist tasks, then report one simple summary plus the validation path."

## Validation

A good master mind pass should leave behind:

- one plain-language user summary
- one control plan
- one handoff map
- one execution packet if the work needed a durable pre-flight contract
- one validation path
- one durable doc update if the work changes repo behavior
- one prompt-history entry, one agent journal note, and one transcript entry if the work should be reopened later

## Related docs

- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/reference/agent-validation-matrix.md`
- `docs/reference/agent-execution.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/agent-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
- `docs/examples/mastermind-example.md`
- `docs/examples/agent-system-example.md`
- `docs/examples/agent-portfolio-example.md`
- `docs/examples/agent-hierarchy-example.md`
- `docs/examples/prompt-journal-example.md`
- `docs/examples/agent-transcript-example.md`
- `docs/examples/agent-validation-matrix-example.md`
- `docs/examples/agent-execution-example.md`
- `docs/research/game-development/foundations/mastermind.md`
- `docs/research/game-development/foundations/agent-validation-matrix.md`
- `docs/research/game-development/foundations/agent-execution.md`
