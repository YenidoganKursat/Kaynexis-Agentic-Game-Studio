# Agent Execution Packet Example

## Scope

This example shows how to turn a broad task into one reusable execution packet before implementation starts.

## Baseline

- The repo already has prompt history, agent transcript, validation matrices, and role matrices.
- The packet is not a replacement for those records.
- It is the execution contract that tells the next worker what to do, what to avoid, and what proves success.

## Decision order

1. Name the owner.
2. Name the operating mode.
3. State the goal in one sentence.
4. List the inputs.
5. List the outputs.
6. Write the custom rules or overrides.
7. Name the proof path.
8. Set the stop conditions.
9. Link the packet to prompt history, transcript, and validation artifacts.

## Example execution packet

> Task: Build a packet for a multi-agent UI refactor.
> Owner: Kaynexis
> Mode: paired-specialist
> Goal: Keep the UI flow narrow enough that the first proof path is obvious.
> Inputs: current UI guide, current route output, current checklist bundle
> Outputs: one packet, one proof path, one validation note
> Custom rules: Keep single-specialist fallback visible; do not hide the transcript trail.
> Proof path: `python3 scripts/codex_studio.py packet --dry-run --json`
> Stop conditions: owner is ambiguous, route is still broad, or proof path is missing

## Good agent prompts

- "Build an execution packet for a UI refactor with one owner and one proof path."
- "Write the packet that keeps custom rules, stop conditions, and validation visible."
- "Create the smallest work packet that still makes later review easy."

## Validation

- `python3 scripts/codex_studio.py packet --task "Build an execution packet for a UI refactor" --goal "Keep the refactor narrow" --dry-run --json`
- `python3 scripts/codex_studio.py checklist --task "Build an execution packet for a UI refactor"`

## Related docs

- `docs/reference/agent-execution.md`
- `docs/reference/agent-system.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/agent-validation-matrix.md`
- `docs/reference/prompt-journal.md`
- `docs/reference/agent-transcript.md`
- `docs/reference/custom-architecture.md`
- `studio/docs/templates/agent-execution.md`
- `studio/docs/active/agent-execution.md`
- `studio/docs/active/eval-agent-execution.md`
