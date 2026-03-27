# Repo Tour

This repository has two major layers:

- the operating layer that tells Codex how to work
- the live project layer that captures what the current game actually is

## Root Files

- `README.md` — first-run and operator-facing repo overview
- `AGENTS.md` — root behavior and decision rules for Codex
- `Makefile` — convenience commands for setup, validation, routing, and Docker
- `CHANGELOG.md` — template-level change history
- `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md` — community and maintainer policy

## Codex Configuration

- `.codex/config.toml` — stable project defaults for model, sandbox, and multi-agent behavior
- `.codex/agents/` — project-scoped agent profiles
- `.agents/skills/` — reusable skills that define structured workflows

These directories define durable behavior. They are not where live project state should go.

## Static Repo Docs

- `docs/setup/` — onboarding, installation, and troubleshooting
- `docs/reference/` — repo map and command reference
- `docs/research/` — source-backed notes that explain why key repo guardrails exist

Use these when you want to explain how to operate the template itself.

## Multi-Engine Layer

- `studio/starter-kits/godot-4/` — Godot 4 starter kit, smoke flow, and reference runtime surface
- `studio/starter-kits/unity-6/` — Unity 6 starter kit, adapter, asmdef/package layout, and runtime sample surface
- `studio/starter-kits/unreal-5/` — Unreal 5 starter kit, adapter, module layout, and packaging sample surface
- `studio/checklists/engine/` — engine-specific checklist rules for Godot, Unity, and Unreal
- `docs/research/game-development/engines/` — engine-specific architecture, class/editor/object, 2D/3D class-mechanic, and performance notes

If you want proof that the repo is not Godot-only, inspect these first:

- `studio/starter-kits/unity-6/README.md`
- `studio/starter-kits/unreal-5/README.md`
- `docs/research/game-development/engines/unity-6-2d-3d-class-and-mechanic-guide.md`
- `docs/research/game-development/engines/unreal-5-2d-3d-class-and-mechanic-guide.md`

This repo is not Godot-only. The current `src/` runtime sample is Godot-based, but the operating system, adapters, starter kits, checklists, research, and CI contracts are shared across all supported engine families.

## GitHub Surfaces

- `.github/CODEOWNERS` — review ownership
- `.github/ISSUE_TEMPLATE/` — structured issue intake
- `.github/pull_request_template.md` — PR review and validation contract
- `.github/workflows/` — CI and Docker smoke checks
- `.github/dependabot.yml` — update automation for actions, Docker, and Python dependencies

## Eval And Hooks

- `evals/` — local regression fixtures for routing and genre guidance
- `scripts/run_local_evals.py` — local eval runner
- `.codex/hooks.json` — optional repo-local Codex hooks
- `scripts/hooks/` — hook handlers for session context and Bash guardrails
- `.env.example` — optional local environment variable template for integrations and helper tooling

## Live Project State

- `studio/docs/templates/` — reusable markdown templates
- `studio/docs/active/` — live state for the current project
- `studio/presets/` — engine/platform/genre guidance packs
- `studio/playbooks/` — multi-phase ways of operating common project types

If a decision, risk, milestone, or feature is important to the current game, it should usually end up in `studio/docs/active/`.

## Runtime and Implementation Surfaces

- `src/` — runtime code or engine-facing source
- `tests/` — automated tests or durable manual test artifacts
- `assets/` — project assets
- `prototypes/` — throwaway or focused experiments
- `tools/` — internal helper tools

These folders begin intentionally light. The template expects the real engine/project layout to shape them over time. In the current repo, `src/` is the Godot reference implementation; Unity and Unreal runtime examples live under their starter-kit scaffolds until a concrete project chooses them as the primary engine.

## Helper Scripts

The `scripts/` folder is the operational command layer.

High-value scripts:

- `codex_studio.py`
- `setup_repo.py`
- `doctor.py`
- `run_local_evals.py`
- `seed_project_baseline.py`
- `bootstrap_studio.py`
- `project_radar.py`
- `route_task.py`
- `scaffold_feature.py`
- `scaffold_bugfix.py`
- `generate_qa_matrix.py`
- `scaffold_eval_plan.py`

## Optional Helper Environment

- `Dockerfile`
- `docker-compose.yml`

These are optional. They give you an isolated Ubuntu + Python shell for working with the repo.
