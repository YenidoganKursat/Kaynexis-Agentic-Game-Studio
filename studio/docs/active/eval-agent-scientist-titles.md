# Eval: Agent Scientist Titles

## Change under test

Add scientist public titles to every agent profile while keeping the stable role ids, routing, and checklist behavior unchanged.

## Goal

The repo should expose human-friendly scientist names in agent summaries and route output without breaking single-specialist mode, command trees, or checklist resolution.

## Validation path

- `python3 scripts/validate_agent_metadata.py --json`
- `python3 scripts/route_task.py "Define a role matrix for the agent system and choose single specialist versus multi-agent panel mode" --json`
- `python3 scripts/route_task.py "Build a command tree for a UI-heavy feature so the software architect, creator lead, and quality controller each have a narrow lane, but keep the single specialist option available if the scope shrinks" --json`
- `python3 scripts/validate_docs.py`
- `python3 scripts/validate_repo_layout.py`
- `python3 -m pytest -q tests/test_studio_system.py`

## Risks

- A title mismatch between `.codex/agents/*.toml` and the docs could confuse operators.
- Route output must keep the machine role ids stable even when public titles change.
- The scientist layer should stay descriptive, not become a second routing key.

## What to watch

- Public titles should remain short and recognizable.
- The single specialist mode must remain visible in `docs/reference/agent-portfolio.md` and `docs/reference/mastermind-guide.md`.
- Any future role addition should receive both a stable role id and a scientist public title in the same change.
