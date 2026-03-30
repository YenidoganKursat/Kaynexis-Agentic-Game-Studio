# Prompt Journal Example

## Scope

Show one prompt-history entry and one agent-journal entry for a task that needs later review.
If the task also has agent assignments or inter-agent conversation, compare the transcript example beside this file.

## Baseline

- No durable review trail existed for the task.
- The user could only inspect chat history to see what happened.

## Decision order

1. Capture the user prompt once in the history section.
2. Append one agent journal entry after a meaningful step.
3. Keep the timestamp, expectation, found, improvement, and evaluation short.
4. Link the journal to the guide and active doc instead of writing a new note for every step.

## Example entries

```md
## Prompt history
### 2026-03-29 18:10 — User prompt
- Prompt: "Add a prompt history log and an agent journal so the user can review later."
- Route: prompt history / agent journal
- Summary: Created append-only journal sections and a journal command.
- Review: `docs/reference/prompt-journal.md`

## Agent journal
### 2026-03-29 18:16 — Agent step
- Step: Draft the journal template and journal command
- Expected: One active file with two append-only sections
- Found: The repo had no durable history trail yet
- Improved: Added a shared prompt journal file and append helper
- Evaluation: The record is now easy to reopen later without reading the whole chat
```

## Good agent prompts

- "Append a user prompt to prompt history and keep the route visible."
- "Write an agent journal entry with expectation, found, improvement, and evaluation."
- "When a task fans out into workers, keep the transcript in a separate append-only file."
- "Record this task in the prompt journal so the user can review it later."

## Validation

- Open `studio/docs/active/prompt-journal.md` and confirm both sections exist.
- Run `python3 scripts/codex_studio.py journal prompt --prompt "..." --route "..." --summary "..." --dry-run --json` and confirm the entry shape.
- Run `python3 scripts/codex_studio.py journal agent --step "..." --expected "..." --found "..." --improved "..." --evaluation "..." --dry-run --json` and confirm the entry shape.
- Run the doc and repo validators after the change.
