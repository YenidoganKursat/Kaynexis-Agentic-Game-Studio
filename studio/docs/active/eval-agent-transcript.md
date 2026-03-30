# Eval Plan — Agent Transcript

## Change under test
- Append-only tracking for task assignments and agent conversation turns in a durable transcript file.

## Goal
- Keep agent-to-agent conversation history reviewable without mixing it into the prompt history trail.

## Risks
- Task assignments could drift back into prompt-journal-only wording.
- Conversation turns could become too verbose to skim.
- Routing or checklist changes could stop surfacing the transcript lane.

## Validation
- Write one assignment entry and one conversation entry with the helper.
- Confirm the active transcript file keeps separate append-only sections.
- Confirm routing surfaces the transcript docs for multi-agent conversation tasks.
- Confirm the checklist bundle includes transcript validation items.

## Success criteria
- Assignment history is append-only.
- Conversation history is append-only.
- The prompt journal still covers user prompts and agent step notes.
- The transcript appears in docs, examples, routing, and validation.
