# Agent Transcript — Kaynexis Agentic Game Studio

## Summary

- This file is the append-only log for agent task assignments and agent-to-agent conversation turns.
- Keep it short, timestamped, and easy to reopen later.
- Keep it separate from prompt history and agent step notes.

## Primary sources

- OpenAI Agents SDK: https://platform.openai.com/docs/guides/agents-sdk
- Messages object: https://platform.openai.com/docs/api-reference/messages/object
- Agent Builder safety: https://platform.openai.com/docs/guides/agent-builder-safety
- Evaluation best practices: https://platform.openai.com/docs/guides/evaluation-best-practices

## Why this matters to this repo

- Multi-agent work is easier to reopen when assignments and replies are preserved in one trail.
- The repo already keeps prompt history and step notes, but conversation turns need their own record.
- Append-only entries make later review more reliable than reading raw chat logs.

## Decision impact

- Keep task assignment history and agent conversation history in this file.
- Keep prompt history in `studio/docs/active/prompt-journal.md`.
- Keep transcript entries linked to handoff, traceability, and controller docs when the work should be reopened later.

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

The file is append-only. New entries go above the marker for the matching section.

## How to use it

- After a task is split across agents, append one assignment entry.
- After a meaningful agent-to-agent reply, append one conversation entry.
- Keep each message short enough that another operator can skim the transcript later.
- If the work also needs user prompt history or agent step notes, pair this file with `studio/docs/active/prompt-journal.md`.

## Example prompts for the agent

- "Record the task assignment history and keep the conversation transcript append-only."
- "Append a short agent-to-agent transcript entry for this handoff."
- "Store the assignment and reply history so the user can reopen the thread later."

## Validation

- `python3 scripts/journal.py transcript --kind assignment --task "..." --speaker "..." --target "..." --message "..."`
- `python3 scripts/journal.py transcript --kind conversation --speaker "..." --target "..." --message "..."`
- `python3 scripts/codex_studio.py journal transcript --kind assignment --task "..." --speaker "..." --target "..." --message "..."`
- `python3 scripts/codex_studio.py journal transcript --kind conversation --speaker "..." --target "..." --message "..."`
- `python3 scripts/validate_docs.py`
- `python3 scripts/validate_repo_layout.py`
- `make validate`

## Related docs

- `docs/reference/agent-transcript.md`
- `docs/examples/agent-transcript-example.md`
- `docs/reference/prompt-journal.md`
- `docs/examples/prompt-journal-example.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
