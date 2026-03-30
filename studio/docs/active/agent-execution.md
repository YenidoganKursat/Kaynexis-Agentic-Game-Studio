# Agent Execution Packet - Kaynexis Agentic Game Studio

## Purpose
- Keep the execution contract for a task in one append-only review trail.
- Make the owner, mode, goal, inputs, outputs, proof path, custom rules, and stop conditions easy to reopen later.
- Use this file alongside `prompt-journal.md` and `agent-transcript.md`, not instead of them.

## How to use it
- Use `python3 scripts/codex_studio.py packet --task "..." --owner "Kaynexis" --mode "single-specialist" --goal "..."` to generate the front-door packet.
- Use the interactive `codex_studio.py` menu when you want the same packet shape without typing the whole command.
- Add `--route`, `--input`, `--output`, `--proof-path`, `--rule`, `--stop-condition`, `--doc`, and `--validation` when the task needs more structure.
- Use `python3 scripts/journal.py packet ...` when you want to append the packet directly to the active work log without going through the front door.

## Packet log
<!-- agent-execution-append -->

## Review path
- Open this file when you want to review the exact execution contract for a task.
- Keep entries short and append-only.
- Link to any supporting docs, validation output, or artifacts inside the entry itself.
- Use `prompt-journal.md` for the user prompt history and `agent-transcript.md` for assignment or conversation turns.
