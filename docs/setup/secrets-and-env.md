# Secrets And Environment

This repository does not require a `.env` file for basic setup, validation, or local evals.

Use `.env.example` only when you want optional integrations or helper scripts that need credentials.

## Included placeholders

- `OPENAI_API_KEY`
  Needed only for OpenAI API-powered helper scripts or external tooling.
- `GH_TOKEN`
  Useful if you use the GitHub CLI against private repos or APIs.
- `SENTRY_AUTH_TOKEN`
  Needed only for Sentry-related helper flows.
- `GODOT_BIN`
  Optional local path to a Godot 4.x binary for runtime smoke and export commands. This is not a secret.

## Rules

- Never commit a real `.env`
- Treat CI secrets and local secrets separately
- Keep example files non-secret and minimal

## Recommended flow

1. Copy `.env.example` to `.env`
2. Fill only the values you actually need
3. Re-run `python3 scripts/doctor.py`

The repository `.gitignore` already excludes `.env` files.
