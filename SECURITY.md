# Security Policy

This repository treats workflow changes, automation scripts, and repo-wide instruction files as security-relevant because they can change how Codex and CI behave.

## Reporting a vulnerability

Do not open a public issue for a suspected security problem.

Preferred path:

1. Use GitHub private vulnerability reporting if the repository host has enabled it.
2. If that is unavailable, contact the maintainer privately before public disclosure.

Include:

- affected files or workflow paths
- reproduction steps
- impact assessment
- whether secrets, tokens, or user data may be exposed

## Scope

If a change touches any of the paths below, review it with extra care and include the rollback story in the PR.

Pay particular attention to:

- `.github/workflows/`
- `.codex/`
- `.agents/`
- `scripts/`
- Docker and dependency updates

## Hardening expectations

- Pin GitHub Actions to full commit SHAs
- Avoid expanding permissions unless the workflow truly needs them
- Treat new shell or automation surfaces as security-relevant changes
