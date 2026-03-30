# Eval Plan - Agent Speed Pack

## Change under test

- Add a fast-path guide, example, research note, and checklist for agent tasks that need the smallest safe bundle.

## Goal

- Keep the first bundle short while preserving single-specialist fallback, a narrow proof path, and the option to add history only when needed.

## Checkpoints

1. `route_task.py` should route fast-path requests to the speed-pack lane.
2. `codex_studio.py checklist` should surface the speed-pack checklist items.
3. `docs/setup/quick-access.md`, `docs/reference/studio-map.md`, `docs/reference/agent-system.md`, and `docs/reference/agent-execution.md` should mention the speed pack.
4. `validate_docs.py` and `validate_repo_layout.py` should include the new files and required markers.
5. `tests/test_studio_system.py` should lock the route and checklist behavior.

## Success criteria

- The speed pack stays the shortest safe start.
- Single specialist mode stays visible.
- Extra history artifacts only appear when later review is needed.

## Watch items

- Do not let the speed pack become another long orchestration doc.
- Do not require prompt history or transcript unless the task actually needs reopening.
- Do not hide the proof path or the validation loop behind the speed-pack language.
