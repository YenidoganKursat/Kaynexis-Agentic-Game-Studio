# Agent Execution Packet Guide

## Summary

Use this guide when a task needs a durable execution contract before work starts.
The packet sits between intake and implementation: it names the owner, mode, goal, inputs, outputs, proof path, custom rules, and stop conditions in one compact shape.
Single specialist mode stays visible. If the task fans out, the packet names the lanes without hiding the fallback.
If the task only needs the fastest safe start, use `docs/reference/agent-speedpack.md` first and reach for the packet only when the work needs a durable pre-flight contract.
If the work should be reopened later, pair this guide with the prompt journal and agent transcript so the history stays reviewable as a single bundle.

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

## Why this matters to this repo

- The repo already has a controller, role matrix, hierarchy, validation matrix, prompt journal, transcript, and custom architecture layers.
- A packet keeps the first frame of work compact so agents do not re-derive scope every time.
- Custom rules and project-specific overrides stay visible in one place instead of getting buried in chat.
- A narrow packet makes the proof path easier to choose before the slice grows.

## Decision impact

- One packet per meaningful task.
- The packet names owner, mode, goal, inputs, outputs, custom rules, proof path, stop conditions, and review trail.
- The packet stays separate from the prompt journal, transcript, and validation matrix.
- Single specialist mode remains visible even when a packet fans out into a pair or a panel.
- Project-specific rules belong in the packet if they affect the work, not only in the chat thread.

## Packet schema

- Task
- Owner
- Mode
- Goal
- Inputs
- Outputs
- Custom rules
- Proof path
- Stop conditions
- Review trail
- Validation

## Packet families

| Family | When to use | Shape |
| --- | --- | --- |
| Single specialist packet | One owner can finish the work | owner + mode + goal + proof path |
| Paired packet | One doer and one checker are enough | owner + validator + proof path |
| Panel packet | The task crosses design, implementation, QA, or release | controller + lane owners + stop conditions |
| Handoff packet | The task moves between workers | owner + reports_to + next step |
| Custom rule packet | Project-specific overrides are needed | global rule + local override + conflict note |

## How to use it

- Use `python3 scripts/codex_studio.py packet --task "..." --owner "Kaynexis" --mode "single-specialist" --goal "..."` to generate the front-door packet.
- Use the interactive `codex_studio.py` menu when you want the same packet shape without typing the whole command.
- Add `--route`, `--input`, `--output`, `--proof-path`, `--rule`, `--stop-condition`, `--doc`, and `--validation` when the task needs more structure.
- Keep the packet paired with `docs/examples/agent-execution-example.md` and `studio/docs/templates/agent-execution.md` so the contract and template stay aligned.
- Use `python3 scripts/journal.py packet ...` when you want to append the packet directly to the active work log without going through the front door.

## Example prompts for the agent

- "Build an execution packet for a UI refactor with one owner and one proof path."
- "Write the work packet that keeps custom rules, stop conditions, and validation visible."
- "Define the smallest packet that still lets this task be reopened later."

## Validation

A good agent-execution pass should leave behind:

- one packet with a named owner and mode
- one proof path
- one custom-rule section if the task has overrides
- one narrow validation path
- one durable doc update if the work changes repo behavior
- one prompt-history entry, one agent journal note, and one transcript entry if the work should be reopened later

## Related docs

- `docs/examples/agent-execution-example.md`
- `docs/research/game-development/foundations/agent-execution.md`
- `studio/docs/templates/agent-execution.md`
- `docs/reference/agent-system.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/agent-validation-matrix.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/reference/agent-speedpack.md`
- `docs/examples/agent-speedpack-example.md`
- `docs/reference/custom-architecture.md`
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
- `studio/checklists/discipline/agent_execution.toml`
- `studio/docs/active/agent-execution.md`
- `studio/docs/active/eval-agent-execution.md`
