# Agent Transcript

## Date

- 2026-03-29

## Summary

- Multi-agent work needs a durable transcript layer that is separate from prompt history and agent step notes.
- Task assignments and agent conversation turns should be append-only so a later review can reconstruct who was asked what, who replied, and what changed.
- A transcript should stay short, timestamped, and linked to the docs that explain the controller, role matrix, and handoff rules.

## Primary sources

- OpenAI Agents SDK: https://platform.openai.com/docs/guides/agents-sdk
- Messages object: https://platform.openai.com/docs/api-reference/messages/object
- Agent Builder safety: https://platform.openai.com/docs/guides/agent-builder-safety
- Evaluation best practices: https://platform.openai.com/docs/guides/evaluation-best-practices

## Why this matters to this repo

- The repo already treats prompt history, agent journal notes, and controller handoffs as durable artifacts.
- Conversation transcripts fill the gap between a prompt journal and a handoff contract.
- That makes it easier to reopen multi-agent work without searching through chat history or a long decision log.

## Decision impact

- Keep task assignment history and agent conversation history in a separate append-only file.
- Keep the prompt journal focused on user prompts and single-step agent notes.
- Keep the transcript linked to master mind, portfolio, hierarchy, and traceability docs when the work is multi-agent.

## Repo impact

- Add a transcript helper, guide, example, checklist, and eval plan so transcript behavior stays versioned.
- Route transcript-shaped tasks to a dedicated transcript lane instead of reusing the prompt journal.
- Keep later-review paths simple: prompt journal for the prompt, transcript for agent turns, and traceability for the surrounding bundle.
