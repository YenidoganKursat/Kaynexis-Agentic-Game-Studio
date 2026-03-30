# Agent Transcript Example

## Scope

Show one task-assignment entry and one conversation-turn entry for a multi-agent task that needs later review.

## Baseline

- The repo had prompt history and agent step notes, but no dedicated transcript lane for agent-to-agent exchanges.
- Assignments and replies were too easy to lose inside chat or long handoff notes.

## Decision order

1. Keep the task assignment separate from the user prompt history.
2. Append one transcript entry when a worker receives a scoped task.
3. Append one transcript entry when another worker replies or hands work off.
4. Keep the timestamps, speaker, target, and next step short.
5. Link the transcript to the prompt journal and the relevant handoff docs instead of creating a new note per message.

## Example entries

```md
## Task assignment history
### 2026-03-29 18:10 — Task assignment
- Kind: assignment
- Task: Profile the inventory HUD and report the first bottleneck
- Speaker: Kaynexis
- Target: technical_director, qa_lead
- Message: Capture one baseline, one likely bottleneck, and one first lever before any refactor.
- Result: The profiling pass was assigned as a narrow review bundle.

## Agent conversation transcript
### 2026-03-29 18:16 — Agent conversation
- Kind: conversation
- Task: Profile the inventory HUD and report the first bottleneck
- Speaker: technical_director
- Target: qa_lead
- Message: Use a shared baseline before changing pooling or layout code.
- Result: QA lead will capture frame-time and allocation data first.
- Next step: Record the profiling result after the next pass.
```

## Good agent prompts

- "Append the task assignment history and keep the conversation transcript append-only."
- "Write a short transcript entry for this handoff and keep the target visible."
- "Record the assignment and reply history so the user can reopen it later."

## Validation

- Open `studio/docs/active/agent-transcript.md` and confirm both sections exist.
- Run `python3 scripts/journal.py transcript --kind assignment --task "..." --speaker "..." --target "..." --message "..." --dry-run --json` and confirm the entry shape.
- Run `python3 scripts/journal.py transcript --kind conversation --speaker "..." --target "..." --message "..." --dry-run --json` and confirm the entry shape.
- Run the doc and repo validators after the change.
