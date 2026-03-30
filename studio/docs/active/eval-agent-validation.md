# Eval Plan — Agent Validation Matrix

## Change under test

- Add a validation-matrix guide and example for agent-system decisions, lane ownership, transcript history, and model overrides.

## Goal

- Keep single-specialist mode visible while making it easy to prove when a pair or a panel is justified.
- Keep the controller, role matrix, hierarchy, prompt journal, and transcript aligned with one compact validation path.

## Checkpoints

1. `route_task.py` should route validation-matrix requests to the new agent-validation surface.
2. `codex_studio.py checklist` should surface the validation checklist items.
3. `validate_docs.py` should keep the guide, example, research note, and active eval in sync.
4. `tests/test_studio_system.py` should lock the route and checklist behavior.
5. `AGENTS.md` should name the validation-matrix lane in the routing heuristic so the operating model stays visible.

## Success criteria

- The matrix guide stays simple enough to skim in one pass.
- Single specialist mode remains visible and available.
- Any explicit lane model override stays visible in route output when the task fans out.
- The shared routing policy and docs all point at the same validation-matrix lane.

## Watch items

- Do not let the matrix catalog replace the agent system or portfolio docs.
- Do not let the matrix become a generic QA table with no operating-model decision.
- Do not hide the transcript or prompt journal when the task should be reopened later.
