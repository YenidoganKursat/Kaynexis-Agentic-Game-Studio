# Optional Codex Hooks

This repo ships with a repo-local `.codex/hooks.json`, but the feature is disabled by default because Codex hooks are still experimental.

## Included hooks

- `SessionStart` context hook
  Adds lightweight reminders about review and eval docs.
- `PreToolUse` Bash guard
  Blocks a short list of obviously destructive shell commands.

## Enable

```bash
python3 scripts/toggle_codex_hooks.py --enable
```

Or:

```bash
make hooks-enable
```

## Disable

```bash
python3 scripts/toggle_codex_hooks.py --disable
```

Or:

```bash
make hooks-disable
```

## Notes

- The official Codex docs mark hooks as experimental.
- The feature flag lives in `.codex/config.toml` as `codex_hooks = true|false`.
- Repo-local hooks are discovered from `.codex/hooks.json`.

## Reference

- Hooks: [OpenAI Codex Docs](https://developers.openai.com/codex/hooks)
