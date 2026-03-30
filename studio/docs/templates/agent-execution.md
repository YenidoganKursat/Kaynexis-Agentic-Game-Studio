# Agent Execution Packet - {PROJECT_NAME}

## Purpose
- Keep the execution contract for a task in one append-only review trail.
- Make the owner, mode, goal, inputs, outputs, proof path, custom rules, and stop conditions easy to reopen later.
- Use this file alongside `prompt-journal.md` and `agent-transcript.md`, not instead of them.

## Packet shape
- Timestamp: short local date and time
- Task: the task title or request
- Owner: the controller or specialist who owns the packet
- Mode: single-specialist, paired-specialist, or multi-agent-panel
- Goal: the short outcome this packet is trying to preserve
- Inputs: the docs, code, or data that matter up front
- Outputs: the expected artifacts or repo changes
- Proof path: the command, artifact, or measurement that proves the packet was followed
- Custom rules: project-specific rules or overrides that must stay visible
- Stop conditions: what should stop the lane or force a handoff
- Review trail: the docs or artifacts the user should open later

## Packet log
<!-- agent-execution-append -->

## Review path
- Open this file when you want to review the exact execution contract for a task.
- Keep entries short and append-only.
- Link to any supporting docs, validation output, or artifacts inside the entry itself.
- Use `prompt-journal.md` for the user prompt history and `agent-transcript.md` for assignment or conversation turns.
