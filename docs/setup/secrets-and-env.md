# Secrets And Environment

This repository does not require a `.env` file for basic setup, validation, or local evals.

Use `.env.example` only when you want optional integrations or helper scripts that need credentials.

The same file also holds optional local engine tool paths. That means the repo can stay multi-engine even when different contributors only have one engine installed locally.

## Included placeholders

- `OPENAI_API_KEY`
  Needed only for OpenAI API-powered helper scripts or external tooling.
- `GH_TOKEN`
  Useful if you use the GitHub CLI against private repos or APIs.
- `SENTRY_AUTH_TOKEN`
  Needed only for Sentry-related helper flows.
- `GODOT_BIN`
  Optional local path to a Godot 4.x binary for runtime smoke and export commands. This is not a secret.
- `UNITY_CLI`
  Optional local Unity editor or batchmode CLI path for documented Unity validation/build commands. This is not a secret.
- `UNREAL_EDITOR`
  Optional local Unreal editor path for documented package/build commands. This is not a secret.
- `UNREAL_UAT`
  Optional local Unreal Automation Tool path when you want package commands to target `RunUAT` directly instead of deriving it from `UNREAL_EDITOR`. This is not a secret.

## Rules

- Never commit a real `.env`
- Treat CI secrets and local secrets separately
- Keep example files non-secret and minimal
- Keep long-lived tool paths in `studio.toml` when they are repo defaults and use `.env` only for local overrides
- Do not assume every machine has every engine installed; only the paths you need for the current contributor or runner should be set

## Recommended flow

1. Copy `.env.example` to `.env`
2. Fill only the values you actually need
3. Re-run `python3 scripts/doctor.py`
4. If the path should be a durable team default, mirror it into `studio.toml`

The repository `.gitignore` already excludes `.env` files.
