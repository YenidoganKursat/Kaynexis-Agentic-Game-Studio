# Repo Documentation

This folder contains durable documentation about operating the repository itself.

Use `docs/` for:

- installation guidance
- onboarding and first-run instructions
- command references
- repo structure explanations
- code review and eval operating policy
- research notes that justify durable repo conventions
- maintainer-facing GitHub and contribution setup
- troubleshooting for the template and helper scripts

Do not use `docs/` for live game project state.
That belongs in `studio/docs/active/`.

## Start Here

- `setup/getting-started.md`
- `setup/installer-checklist.md`
- `setup/troubleshooting.md`
- `setup/github-maintainer-setup.md`
- `setup/optional-codex-hooks.md`
- `setup/secrets-and-env.md`
- `reference/repo-tour.md`
- `reference/command-cheatsheet.md`
- `reference/code-review.md`
- `reference/eval-strategy.md`
- `reference/genre-presets.md`
- `reference/codex-compatibility.md`
- `research/openai-codex-infra-findings.md`

## Responsibility Split

- `docs/` — static repo/operator documentation
- `docs/research/` — source-backed notes behind repo policy
- `studio/docs/templates/` — reusable project document templates
- `studio/docs/active/` — live project truth for the current game
