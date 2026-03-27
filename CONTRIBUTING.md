# Contributing

Use this repository like a studio operating system, not a loose prompt dump.

## Quick start

1. Run `python3 scripts/codex_studio.py init`
2. Read `docs/setup/getting-started.md`
3. Review `docs/reference/code-review.md`
4. Run `make ci-local`

## Branch and change shape

- Prefer small, reviewable changes over broad refactors.
- Keep durable behavior in `AGENTS.md`, `.codex/`, `.agents/`, `scripts/`, and `docs/reference/`.
- Keep live project truth in `studio/docs/active/`.
- If you change shared instructions, routing, agents, or setup behavior, create or update an `eval-plan-*.md` file.

## Before opening a PR

- Run `make validate`
- Run `python3 scripts/run_local_evals.py`
- Run `python3 scripts/doctor.py`
- Update docs when behavior, process, or expectations changed
- Use the PR template and fill in the validation section honestly

## Review expectations

- Lead with correctness, regressions, security, and missing validation
- Use `docs/reference/code-review.md` as the review checklist
- If a change touches `.codex/`, `.agents/`, `AGENTS.md`, or shared scripts, note the eval impact explicitly

## Commit and ownership notes

- This template assumes `codex/` branch prefixes by default when feature branches are created
- Update `.github/CODEOWNERS` if your GitHub handle or team structure differs from the current default
