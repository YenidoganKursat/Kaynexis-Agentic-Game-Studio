# Eval Plan - Agent Role Checklist Packs

## Date

2026-03-30

## Summary

Validate that the new role-specific checklist packs surface cleanly for task-based and agent-based requests while single-specialist mode remains the default.

## Primary sources

- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `studio/checklists/README.md`
- `scripts/studio_core.py`
- `scripts/route_task.py`

## Why this matters to this repo

The repo now has more explicit role packs for producer, technical director, QA, release, docs research, performance, engine, gameplay, UI, narrative, art, and audio work.
If those packs do not resolve cleanly, the hierarchy becomes harder to trust and the controller loses a fast way to hand work off.

## Decision impact

- Single specialist mode stays the default.
- Role-specific checklist packs should surface only when the task or agent clearly names that lane.
- The controller should still keep the user-facing summary simple even when the internal lane map gets larger.
- Role checklist packs should stay narrow enough that each lane is readable in one pass.

## Test cases

- A producer planning task should surface `producer.toml` and the supporting hierarchy / quality layers.
- A technical-director architecture task should surface `technical_director.toml` plus architecture and validation layers.
- A QA-lead validation task should surface `qa_lead.toml` plus quality and benchmark layers.
- A release-readiness task should surface `release_manager.toml` plus release and versioning layers.
- A performance tuning task should surface `performance_analyst.toml` plus performance, benchmark, and GPU layers.

## Validation

- `python3 scripts/codex_studio.py checklist --task \"Prepare a producer scope and handoff packet for the next milestone\" --json`
- `python3 scripts/codex_studio.py checklist --task \"Write a technical director architecture boundary and first blocker note\" --json`
- `python3 scripts/codex_studio.py checklist --task \"Draft a QA lead validation plan for the release gate\" --json`
- `python3 scripts/codex_studio.py checklist --task \"Prepare a release manager freeze and rollback note\" --json`
- `python3 scripts/codex_studio.py checklist --task \"Prepare a performance analyst baseline for an FPS pass\" --json`
- `python3 scripts/run_local_evals.py --json`

## Related docs

- `docs/reference/agent-system.md`
- `docs/reference/agent-portfolio.md`
- `docs/reference/agent-hierarchy.md`
- `docs/reference/mastermind-guide.md`
- `docs/reference/quality-guide.md`
- `docs/reference/perf-guide.md`
- `docs/reference/ci-cd.md`
- `docs/reference/version-guide.md`
