# Changelog

## Unreleased

### Added
- onboarding docs under `docs/setup/` and `docs/reference/`
- `scripts/setup_repo.py` for one-command repository bootstrap
- `scripts/doctor.py` for local tooling and repo health checks
- `Makefile` for common setup, validation, routing, and Docker tasks
- README guidance for first-run, validation, and optional container usage
- research-backed review and eval docs under `docs/reference/` and `docs/research/`
- `studio/docs/templates/eval-plan.md` plus `scripts/scaffold_eval_plan.py`
- `.codex/agents/reviewer.toml` for narrow, read-only review passes
- guided genre-first setup via `scripts/start_game_studio.py`
- `studio/docs/templates/genre-starter.md` and genre picker reference docs
- GitHub community health files, issue forms, PR template, CODEOWNERS, and CI workflows
- local eval corpus under `evals/` plus `scripts/run_local_evals.py`
- optional Codex hooks scaffolding under `.codex/hooks.json` and `scripts/hooks/`
- maintainer setup docs for GitHub and optional hooks
- baseline project seeding via `scripts/seed_project_baseline.py`
- `.env.example` plus secrets and Codex compatibility setup docs

### Changed
- `bootstrap_studio.py` now avoids duplicating preset packs on repeated bootstrap runs unless overwrite is explicit
- `project_radar.py` now treats placeholder-only `src/`, `tests/`, and `assets/` folders as empty
- repo layout validation now includes required installer-facing documentation surfaces
- `.codex/config.toml` now keeps subagent nesting at the conservative default depth
- setup/bootstrap flows now generate a genre starter doc and route tasks with active genre context
- repo validation and doctor now check GitHub, eval, and optional hooks surfaces

## v2.0.0 — Pro Max

Major expansion of the Codex-native game studio template.

### Added
- 50 custom agents with clearer role boundaries and sandbox/model defaults
- 46 reusable skills covering design, implementation, QA, release, growth, and compliance
- 34 templates for core docs, feature docs, QA, release, marketing, telemetry, economy, and postmortems
- 16 preset packs across engine, platform, and genre
- 6 multi-phase operating playbooks
- bootstrap, preset, routing, scaffolding, validation, and status scripts
- layered `AGENTS.md` files for root, source, tests, assets, docs, prototypes, and tools
- git hooks for layout, docs, asset validation, and commit message conventions

### Expanded coverage
- scope rescue
- combat loop design
- level blockouts
- puzzle design
- tutorial/onboarding
- narrative and quest production
- telemetry and analytics
- save system design
- backend and netcode foundations
- porting / mobile / web readiness
- localization and accessibility
- storefront, marketing, community ops, liveops
- compliance, age rating, certification
- hotfixes and postmortems

### Philosophy
- broader possibility space
- still small, reviewable slices
- durable repo state over ephemeral chat
- explicit validation and risk reporting
