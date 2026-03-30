# Eval Plan — Agent Hierarchy

## Change under test

- The repo now has a command-tree layer for multi-agent work.
- Single specialist mode must remain available and visible.
- Async status packets should be explicit and narrow.

## Goal

- Verify that hierarchy tasks route to the right docs, checklists, and review signals.

## Checkpoints

1. `route_task.py` should route hierarchy requests to the new hierarchy surface.
2. `codex_studio.py checklist` should surface hierarchy checklist items.
3. `validate_docs.py` should keep the guide, example, and research note in sync.
4. `tests/test_studio_system.py` should lock the route and checklist behavior.

## Acceptance criteria

- The command tree is explicit.
- Single specialist mode is still the default.
- The user summary stays short.
- The validation path stays small.

## Risks

- Hierarchy can become a fancy name for generic panel mode if the titles and reporting lines are not explicit.
- The controller can become too broad if every lane is allowed to own too much.

