# OpenAI/Codex Agent Workflow Eval Plan

## Change under test

The repo now routes OpenAI/Codex agent-platform tasks through a dedicated controller workflow and research bundle that keeps prompt policy, prompt versions, tool-access assumptions, and eval paths explicit.

## Goal

Make OpenAI/Codex tasks land on the right docs and checklist layers without collapsing single-specialist mode or hiding the controller decision.

## Risks

- OpenAI/Codex keywords steal unrelated mastermind tasks.
- The new route surfaces too much or too little context.
- Prompt policy and task prompt details drift apart again.
- Tool access or internet assumptions remain implicit in some docs.

## Validation

- `python3 scripts/route_task.py "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals" --json`
- `python3 scripts/codex_studio.py checklist --task "Prepare an OpenAI/Codex agent workflow with explicit prompt versions, evals, and tool approvals" --json`
- `python3 scripts/validate_docs.py --strict`
- `python3 scripts/validate_repo_layout.py`
- `python3 scripts/run_local_evals.py --json`
- `python3 -m pytest -q tests/test_studio_system.py`

## Success criteria

- The dedicated OpenAI/Codex route is selected for agent-platform tasks.
- The checklist bundle includes the OpenAI/Codex discipline and the controller/hierarchy/journal support layers.
- The docs surface the OpenAI/Codex research note before implementation notes.
- Single-specialist mode stays visible in controller summaries.
