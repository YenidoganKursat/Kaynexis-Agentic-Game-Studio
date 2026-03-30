# Eval Plan: Master Mind Routing

## Change under test

- Add a repo-wide master mind orchestration layer that keeps user summaries simple and routes broad tasks to specialist workers.

## Goal

- Ensure broad, cross-functional tasks route to a dedicated master mind control loop instead of falling through to an unrelated specialist lane.
- Ensure the user-facing guidance stays simple while the internal handoff plan remains explicit.

## Cases

1. `Coordinate a multi-step engine and genre research task with simple user summaries and internal worker handoffs`
2. `Run the master mind loop on a routing change and keep the user-facing answer short`
3. `Break a broad request into specialist tasks, then report one simple summary plus the validation path`
4. `Manage a multi-step repo change with one clear summary and explicit worker handoffs`

## Expected behavior

- Route broad orchestration tasks to the master mind discipline.
- Surface the master mind guide and example in research refs.
- Include the master mind checklist items in the resolved checklist bundle.
- Keep the control plan readable by a non-specialist user.

## Validation

- `python3 scripts/codex_studio.py next "<case>" --json`
- `python3 scripts/codex_studio.py checklist --task "<case>" --json`
- `python3 scripts/route_task.py "<case>" --json`
- `python3 -m pytest -q tests/test_studio_system.py`

## Success criteria

- The route is explicit and stable.
- The user summary stays short.
- The worker handoffs are named.
- The docs and checklist surface the same control contract.

## Risks

- A broad keyword set could accidentally capture unrelated tasks.
- The orchestration layer could become a hidden implementation owner if the docs are not explicit.
