# Workflow Recipes

These are practical, repeatable ways to use the repo.

Use them when you want a reliable path instead of inventing your own flow every time.

## Recipe: Start a new game baseline

Use this when the repo is fresh or the project identity changed.

```bash
# Replace --engine with godot-4, unity-6, or unreal-5 depending on the real project.
python3 scripts/codex_studio.py init \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite \
  --yes
python3 scripts/codex_studio.py doctor
```

Then open:

- `studio/docs/active/game-brief.md`
- `studio/docs/active/engine-profile.md`
- `studio/docs/active/current-sprint.md`
- the matching `docs/research/game-development/engines/*-2d-3d-class-and-mechanic-guide.md`

## Recipe: Turn an idea into a real slice

Use this when you have a feature idea but not yet a buildable task.

```bash
python3 scripts/codex_studio.py next "Add a short-range parry that rewards precise timing"
python3 scripts/codex_studio.py checklist --task "Add a short-range parry that rewards precise timing"
python3 scripts/scaffold_feature.py "Parry Mechanic" --with-adr --with-test-plan
```

The scaffold now also writes a default handoff contract and traceability doc so the slice is easier to review and continue.

Good outcome:

- one routed task
- one merged checklist
- one durable feature brief
- one explicit validation path

## Recipe: Investigate a bug without thrashing

Use this when a bug is vague or emotionally noisy.

```bash
python3 scripts/scaffold_bugfix.py "Player gets stuck after dodge near a wall"
python3 scripts/codex_studio.py next "Investigate player gets stuck after dodge near a wall"
python3 scripts/codex_studio.py checklist --task "Investigate player gets stuck after dodge near a wall"
```

Then document:

- reproduction steps
- engine/runtime assumptions
- likely owner
- smallest validation loop

## Recipe: Research before architecture work

Use this when the task affects save, combat, AI, pathfinding, data ownership, or engine structure.

```bash
python3 scripts/codex_studio.py research --category systems --title "Boss encounter state ownership"
python3 scripts/codex_studio.py next "Design boss encounter state ownership"
```

Before implementation, make sure the final task references at least one relevant research note.

## Recipe: Prepare for a performance pass

Use this when FPS, memory, or scale is becoming risky.

```bash
python3 scripts/codex_studio.py next "Run a performance pass on enemy projectile scale"
python3 scripts/codex_studio.py checklist --task "Run a performance pass on enemy projectile scale"
python3 scripts/scaffold_feature.py "Projectile Scale Perf Pass" --with-test-plan
```

Then decide explicitly:

- representation choice
- contact model
- measurement path
- rollback plan if the optimization is not worth it

## Recipe: Validate the engine contract before real work

Godot:

```bash
python3 scripts/godot_smoke.py --static-only
```

Unity:

```bash
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --unity-path tools/engine-stubs/unity/Unity \
  --dry-run --json
```

Unreal:

```bash
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path tools/engine-stubs/unreal/RunUAT.sh \
  --dry-run --json
```

Use the stub-backed commands for contract shape only. Use real engine paths when you want editor-backed confidence.

## Recipe: Pre-merge confidence pass

Use this before calling a shared change "done".

```bash
python3 scripts/validate_docs.py
python3 scripts/validate_repo_layout.py
python3 scripts/run_local_evals.py --json
python3 -m pytest -q tests
make ci-local
```

## Recipe: Prepare a release-readiness bundle

Use this when you want a structured review package before an external demo or milestone branch.

```bash
make ci-report
python3 scripts/ci_artifact_report.py --output-dir build/ci/manual-release --label release-readiness --json
```

Then review:

- `build/ci/manual-release/ci-report.json`
- `build/ci/manual-release/ci-report.md`

## Recipe: Daily operator loop

This is a good default daily rhythm:

1. `python3 scripts/codex_studio.py doctor`
2. open `studio/docs/active/current-sprint.md`
3. route the next task
4. resolve the checklist for the same task
5. touch the minimum docs required for that task
6. keep one validation path green while you work
7. end with `python3 scripts/run_local_evals.py`

## Recipe: New contributor handoff

Use this when someone new joins the repo.

Ask them to read:

1. `README.md`
2. `docs/setup/getting-started.md`
3. `docs/setup/first-hour-walkthrough.md`
4. `docs/reference/engine-selection-guide.md`
5. `docs/reference/command-cheatsheet.md`
6. `studio/docs/active/game-brief.md`
7. `studio/docs/active/engine-profile.md`

Then ask them to run:

```bash
python3 scripts/codex_studio.py doctor
python3 scripts/codex_studio.py engine --list --json
python3 scripts/codex_studio.py next "Summarize the most credible next task for this repo"
```
