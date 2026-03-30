# Eval Plan — Prompt Journal

## Change under test

- Add an append-only prompt history and agent journal for later review.
- Add a journal command that writes timestamped entries into the active journal file.
- Surface the new journal guide, example, checklist, and active doc in routing and docs.

## Atlas references

- Primary system atlas: `docs/reference/system-atlas.md`
- Core class atlas: `docs/reference/engine-atlas.md`
- Fast owner map: `docs/reference/engine-map.md`

## Goal

- A later reviewer should be able to open one file and see what the user asked, what the agent expected, what it found, what improved, and what was validated.

## Eval set

| Prompt / scenario | Why it matters | Baseline | Expected after change |
|---|---|---|---|
| "Record a prompt history entry for this task" | Captures the user-facing audit trail | No durable journal trail | A timestamped prompt-history entry is appended |
| "Write an agent journal entry after validation" | Captures step-level progress | No step journal | A timestamped agent-journal entry is appended |
| "Route a task that asks for prompt history" | Verifies routing and checklist surfacing | No journal route | The route surfaces the prompt-journal guide, example, and checklist |

Add at least one scenario that matches the exact feature, instruction, or routing change you are making.

## Rubric

- Correctness
- Evidence quality
- Instruction compliance
- Delegation restraint
- Validation honesty

## Run notes

- Date / operator / model / config
- Commands used
- Links to transcripts, screenshots, or artifacts

## Regression watchlist

- The journal should stay append-only.
- The prompt history and agent journal should remain easy to open later.
- Routing and checklist output should keep surfacing the journal guide and example.

## Exit criteria

- The journal command works in dry-run and write modes.
- The active journal shows timestamped prompt and agent entries.
- The docs, checklist, and routing surfaces all point at the same journal model.
