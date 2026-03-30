# Support

This file is the quick pointer for repo and studio-system support. It is intentionally short so people can find the right path without hunting through chat history.

## Where to start

- Usage questions: read `README.md` and `docs/setup/getting-started.md`
- Repo commands: read `docs/reference/command-cheatsheet.md`
- Genre selection: read `docs/reference/genre-presets.md`
- Review and eval policy: read `docs/reference/code-review.md` and `docs/reference/eval-strategy.md`

## Filing work

Use the GitHub issue forms when the work needs to survive beyond the current session and should be triaged with a durable label, owner, or milestone.

Use the GitHub issue forms for:

- bug reports
- feature proposals
- infra or routing changes
- genre preset improvements

## Before asking for help

- Run `python3 scripts/doctor.py`
- Run `make validate`
- Run `python3 scripts/run_local_evals.py`
- Include the failing command, output, and the files you expected to change
