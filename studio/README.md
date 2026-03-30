# Studio Folder

This directory holds mutable project state, templates, presets, and playbooks.

Static repo and onboarding docs live under `docs/`. Anything that represents the live state of the game project belongs here instead.

## Layout

- `docs/templates/` — reusable document templates
- `docs/active/` — live project docs that should be updated during work
- `presets/engine/` — engine-specific guidance packs
- `presets/platform/` — platform-specific constraints and checklist seeds
- `presets/genre/` — genre guardrails and workflow hints
- `playbooks/` — multi-sprint operating guides for common project shapes

## Typical flow

1. Run `python3 scripts/codex_studio.py init --project-name "Your Game" --engine godot-4 --platform pc-premium --genre action-roguelite --yes`
2. Review `docs/active/game-brief.md`, `docs/active/genre-starter.md`, and `docs/active/engine-profile.md`
3. If the machine still needs an engine install or an agent bootstrap, open `docs/setup/engine-installation.md` and `docs/setup/agent-setup.md`
4. Use skills to create feature, QA, release, and postmortem documents as the project evolves

## High-value files

- `docs/active/game-brief.md` — product direction and player promise
- `docs/active/genre-starter.md` — genre-specific first slice, risks, and next commands
- `docs/active/engine-profile.md` — engine assumptions and technical boundaries
- `docs/active/current-sprint.md` — immediate work
- `docs/active/risk-register.md` — explicit project risk
- `docs/active/decision-log.md` — durable decisions and reversals
- `docs/active/eval-plan-*.md` — behavior-change baselines and regression notes
- `docs/active/preset-pack.md` — imported engine/platform/genre guidance
