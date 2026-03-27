# Installer Checklist

Use this checklist when you are the person standing up the repo for a team or new project.

## Before Sharing the Repo

- Confirm Python `3.11+` is available.
- Confirm the intended engine, platform, and genre presets.
- Run `python3 scripts/codex_studio.py init --project-name "Your Game" --engine ... --platform ... --genre ... --yes`
- Review `studio/docs/active/game-brief.md`
- Review `studio/docs/active/genre-starter.md`
- Review `studio/docs/active/engine-profile.md`
- Review `studio/docs/active/platform-targets.md`
- Read `docs/reference/code-review.md`
- Read `docs/reference/eval-strategy.md`
- Install git hooks if the repo is already initialized.
- Run `make validate`
- Run `python3 scripts/run_local_evals.py`
- Run `python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine ... --platform ... --genre ...`
- Run `python3 scripts/doctor.py`

## If This Repo Wraps an Existing Game

- Update `studio/docs/active/engine-profile.md` to describe the actual engine version and repo layout.
- Update `studio/docs/active/build-pipeline.md` with the real build/export path.
- Update `studio/docs/active/content-pipeline.md` with the real import/content workflow.
- Run `python3 scripts/project_radar.py --warn-only` and capture the findings.
- Trim or adapt unused skills, agents, and presets only after the real project shape is clear.

## Before Inviting Collaborators

- Make sure `README.md` matches the real way the team should start.
- Make sure `docs/setup/getting-started.md` reflects the real bootstrap command.
- Make sure `docs/reference/command-cheatsheet.md` matches the commands you expect people to use.
- Make sure `docs/reference/genre-presets.md` matches the genre choices you want new users to see.
- Make sure review and eval expectations are still accurate for your team.
- Make sure `.github/CODEOWNERS` and community health files reflect the real maintainer identity.
- Confirm there are no unresolved placeholders in `studio/docs/active/`.
- Confirm there are no committed `__pycache__` or `.pyc` files.
- Confirm the first meaningful feature or milestone is visible in `current-sprint.md`.

## Before Starting Real Implementation

- Route the first real task with `python3 scripts/codex_studio.py next "Describe the first real task"`.
- Create a feature brief or bug report instead of jumping straight into code.
- Create an eval plan before changing shared instructions, agents, or routing behavior.
- Decide whether `src/`, engine-native folders, or another layout is the true runtime source path.
- Add at least one real test or one explicit manual validation story.

## Minimum Healthy Baseline

You have done enough installer work when:

- the team can clone the repo and run one setup command
- the active docs explain what the game is and what is being built next
- the routing/scaffolding commands work
- validation passes
- nobody needs tribal knowledge just to get started
