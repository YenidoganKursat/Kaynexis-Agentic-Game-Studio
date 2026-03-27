# Repo Documentation

This folder contains durable documentation about operating the Codex-first studio operating system itself.

Use `docs/` for:

- installation guidance
- onboarding and first-run instructions
- command references
- repo structure explanations
- code review and eval operating policy
- research notes that justify durable repo and engine conventions
- maintainer-facing GitHub and contribution setup
- troubleshooting for the template and helper scripts
- operator-facing workflow recipes and task examples

Do not use `docs/` for live game project state.
That belongs in `studio/docs/active/`.

## Start Here

- `setup/getting-started.md`
- `setup/first-hour-walkthrough.md`
- `setup/installer-checklist.md`
- `setup/troubleshooting.md`
- `setup/github-maintainer-setup.md`
- `setup/optional-codex-hooks.md`
- `setup/secrets-and-env.md`
- `reference/repo-tour.md`
- `reference/command-cheatsheet.md`
- `reference/engine-selection-guide.md`
- `reference/workflow-recipes.md`
- `reference/task-prompt-examples.md`
- `reference/code-review.md`
- `reference/eval-strategy.md`
- `reference/genre-presets.md`
- `reference/codex-compatibility.md`
- `reference/engine-agent-guidelines.md`
- `research/openai-codex-infra-findings.md`
- `research/game-development/README.md`
- `research/game-development/engines/README.md`

## Responsibility Split

- `docs/` — static repo/operator documentation
- `docs/research/` — source-backed notes behind repo policy and engine/production decisions
- `studio/docs/templates/` — reusable project document templates
- `studio/docs/active/` — live project truth for the current game

## Engine Research Highlights

If you are doing engine-specific work, start here:

- `docs/research/game-development/engines/README.md`
- `docs/research/game-development/engines/godot-4-2d-3d-class-and-mechanic-guide.md`
- `docs/research/game-development/engines/unity-6-2d-3d-class-and-mechanic-guide.md`
- `docs/research/game-development/engines/unreal-5-2d-3d-class-and-mechanic-guide.md`
