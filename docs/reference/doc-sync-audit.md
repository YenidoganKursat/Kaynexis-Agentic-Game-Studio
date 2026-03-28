# Doc Sync Audit

Use the doc sync audit when code, scripts, starter kits, workflows, or presets changed and you want a fast answer to:

- which docs should probably be reviewed
- why those docs are likely stale
- which changed files triggered the suggestion

## Command

```bash
python3 scripts/doc_sync_audit.py --json
```

Or pass explicit changed paths:

```bash
python3 scripts/doc_sync_audit.py src/main.gd scripts/route_task.py studio/presets/genre/metroidvania.md
```

## What it does

- reads changed paths from arguments or `git status --short`
- maps those paths to likely affected docs
- prints suggested docs plus the reason each one was flagged

## What it does not do

- it does not edit docs automatically
- it does not guarantee a doc is wrong
- it does not replace human review

Use it as a repo-to-doc sync reminder, not a final truth engine.
