# Agent Transcript Guide

## Summary

Use this guide when a task needs a durable record of task assignments, agent-to-agent conversation turns, or handoff decisions.
Keep this separate from `docs/reference/prompt-journal.md`: the prompt journal is for the user prompt and the agent step note, while this guide is for conversation turns and assignment history between agents.
If the work also needs a durable execution contract, pair this guide with `docs/reference/agent-execution.md` so the contract stays separate from the messages.

## Primary sources

- OpenAI Agents SDK: https://platform.openai.com/docs/guides/agents-sdk
- Messages object: https://platform.openai.com/docs/api-reference/messages/object
- Agent Builder safety: https://platform.openai.com/docs/guides/agent-builder-safety
- Evaluation best practices: https://platform.openai.com/docs/guides/evaluation-best-practices

## Why this matters to this repo

- Multi-agent work is much easier to reopen when assignments and replies are preserved as a transcript.
- The repo already keeps a prompt history journal, but transcript history is a different record: who talked to whom, what they were told, and what the next step became.
- The execution packet is another separate record: it captures the owner, mode, proof path, custom rules, and stop conditions before the messages start.
- Append-only transcripts make later review simpler than reading raw chat logs.

## Decision impact

- Keep prompt history, agent journal notes, and agent transcripts as separate durable records.
- Keep the execution packet separate as well so the contract does not get mixed into the message trail.
- Keep each transcript entry short, timestamped, and easy to skim.
- Keep assignment history and conversation turns in distinct append-only sections.
- Keep the transcript linked to the prompt journal, traceability, and handoff docs when the task should be reopened later.

## Record model

### Task assignment entry

- Timestamp
- Task or thread title
- Speaker or assigner
- Target agent or panel
- Message or assignment text
- Expected result or next step

### Conversation turn entry

- Timestamp
- Speaker
- Target or audience
- Message
- Result or decision
- Next step

## Where the record lives

- `studio/docs/active/agent-transcript.md`
- `studio/docs/active/agent-execution.md`

The file is append-only. New entries go above the marker for the matching section.

## How to use it

- After a task is split across agents, append one assignment entry.
- After a meaningful agent-to-agent reply, append one conversation entry.
- Keep the message short enough that another operator can skim the transcript later.
- If the work also needs user prompt history or agent step notes, pair this guide with `docs/reference/prompt-journal.md`.
- If the work also needs a durable execution contract, pair this guide with `docs/reference/agent-execution.md`.

## Example prompts for the agent

- "Record the task assignment history and keep the conversation transcript append-only."
- "Append a short agent-to-agent transcript entry for this handoff."
- "Store the assignment and reply history so the user can reopen the thread later."

## Validation

- `python3 scripts/journal.py transcript --kind assignment --task "..." --speaker "..." --target "..." --message "..."`
- `python3 scripts/journal.py transcript --kind conversation --speaker "..." --target "..." --message "..."`
- `python3 scripts/codex_studio.py packet --task "..." --goal "..."`
- `python3 scripts/codex_studio.py journal transcript --kind assignment --task "..." --speaker "..." --target "..." --message "..."`
- `python3 scripts/codex_studio.py journal transcript --kind conversation --speaker "..." --target "..." --message "..."`
- `python3 scripts/validate_docs.py`
- `python3 scripts/validate_repo_layout.py`
- `make validate`

## Related docs

- `docs/examples/agent-transcript-example.md`
- `docs/examples/agent-execution-example.md`
- `docs/reference/prompt-journal.md`
- `docs/examples/prompt-journal-example.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/agent-execution.md`
- `docs/research/game-development/foundations/agent-execution.md`
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
- `studio/docs/active/agent-transcript.md`
- `studio/docs/active/agent-execution.md`
- `studio/docs/active/eval-agent-transcript.md`
