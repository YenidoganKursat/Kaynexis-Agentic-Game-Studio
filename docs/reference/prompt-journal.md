# Prompt Journal

## Summary

Use this guide when a task should leave behind a reviewable trail of what the user asked and what the agent did.
The repo keeps the trail in one active file with two append-only sections:

- `Prompt history` for the user request, the route, and the short outcome
- `Agent journal` for step-by-step notes about expectation, finding, improvement, and evaluation

If the work also includes agent-to-agent assignments or conversation turns, use `docs/reference/agent-transcript.md` alongside this guide.
If the work also needs a durable execution contract, pair this guide with `docs/reference/agent-execution.md` so the plan and the history stay separate.

This is intentionally simple. The goal is later review, not verbose narration.

## Primary sources

- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/quality-process.md`

## Why this matters to this repo

- Prompt history disappears quickly in chat, but the repo needs a durable place to reopen it later.
- Step notes help the next person understand what was expected, what was found, and what actually improved.
- An append-only journal avoids turning review history into a loose collection of comments.
- This pairs well with traceability, handoff contracts, the execution packet, and the controller/portfolio/hierarchy layers already in the repo.

## Decision impact

- Keep one active journal file instead of scattering history across many notes.
- Keep prompt history and agent journal sections distinct inside the same file.
- Keep the execution packet in its own file so the contract does not get mixed into history.
- Keep task assignments and conversation turns in the transcript file instead of mixing them into prompt history.
- Keep each entry short, timestamped, and reviewable.
- Update the journal in the same change when a task changes routing, scope, or validation behavior.

## Record model

### Prompt history entry

- Timestamp
- Prompt text
- Route or owning discipline
- Short outcome or summary
- Optional review link or docs link

### Agent journal entry

- Timestamp
- Step name
- Expected outcome
- What was found
- What improved
- Short evaluation
- Optional next step
- Optional validation link or artifact

## Where the record lives

- `studio/docs/active/prompt-journal.md`
- `studio/docs/active/agent-transcript.md`
- `studio/docs/active/agent-execution.md`

The file is append-only. New entries go above the marker for the matching section.

## How to use it

- After a non-trivial prompt or routed task, add one prompt-history entry.
- After each meaningful agent step, add one journal entry.
- After an assignment or reply between agents, add one transcript entry.
- Keep the fields short enough that another operator can skim them later.
- If the work touches routing, checklists, or shared instruction behavior, update the matching eval plan in the same change.
- You can use either the direct journal helper or the front-door CLI wrapper:
  - `python3 scripts/journal.py prompt --prompt "..." --route "..." --summary "..."`
  - `python3 scripts/codex_studio.py journal prompt --prompt "..." --route "..." --summary "..."`

## Example prompts for the agent

- "Append this task to prompt history and add one agent journal entry after validation."
- "Record the user prompt, route, and outcome in the prompt journal."
- "Write a short agent journal entry with expectation, finding, improvement, and evaluation."

## Validation

- `python3 scripts/journal.py prompt --prompt "..." --route "..." --summary "..."`
- `python3 scripts/journal.py agent --step "..." --expected "..." --found "..." --improved "..." --evaluation "..."`
- `python3 scripts/journal.py transcript --kind assignment --task "..." --speaker "..." --target "..." --message "..."`
- `python3 scripts/journal.py transcript --kind conversation --speaker "..." --target "..." --message "..."`
- `python3 scripts/codex_studio.py packet --task "..." --goal "..."`
- `python3 scripts/codex_studio.py journal prompt --prompt "..." --route "..." --summary "..."`
- `python3 scripts/codex_studio.py journal agent --step "..." --expected "..." --found "..." --improved "..." --evaluation "..."`
- `python3 scripts/codex_studio.py journal transcript --kind assignment --task "..." --speaker "..." --target "..." --message "..."`
- `python3 scripts/validate_docs.py`
- `python3 scripts/validate_repo_layout.py`
- `make validate`

## Related docs

- `docs/examples/prompt-journal-example.md`
- `docs/reference/agent-transcript.md`
- `docs/reference/agent-execution.md`
- `docs/examples/agent-transcript-example.md`
- `docs/examples/agent-execution-example.md`
- `docs/reference/task-prompt-examples.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
- `studio/docs/active/prompt-journal.md`
- `studio/docs/active/agent-transcript.md`
- `studio/docs/active/agent-execution.md`
- `studio/docs/active/eval-agent-execution.md`
- `studio/docs/active/eval-prompt-journal.md`
- `studio/docs/active/eval-agent-transcript.md`
