# Command Cheatsheet

## One-Time Setup

Quick access:

```bash
make start
python3 scripts/start_game_studio.py
```

Guided setup:

```bash
python3 scripts/codex_studio.py init
```

Direct setup examples:

```bash
# Godot 4
python3 scripts/codex_studio.py init \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite \
  --yes

# Unity 6
python3 scripts/codex_studio.py init \
  --project-name "Your Game" \
  --engine unity-6 \
  --platform pc-premium \
  --genre tactical-rpg \
  --yes

# Unreal 5
python3 scripts/codex_studio.py init \
  --project-name "Your Game" \
  --engine unreal-5 \
  --platform console-premium \
  --genre co-op-survival \
  --yes
```

Seed a concrete active-doc baseline:

```bash
python3 scripts/seed_project_baseline.py \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite
```

List the supported engine families:

```bash
python3 scripts/codex_studio.py engine --list --json
```

Install git hooks manually:

```bash
./scripts/install_git_hooks.sh
```

## Health and Validation

Run the health check:

```bash
python3 scripts/codex_studio.py doctor
```

Run the local eval corpus:

```bash
python3 scripts/run_local_evals.py
```

Run the repo-local benchmark corpus:

```bash
python3 scripts/run_bench.py
python3 scripts/run_bench.py --json
make bench
```

Validate version metadata:

```bash
python3 scripts/version_guard.py --json
make version
cat VERSION
```

Validate engine starter kits:

```bash
python3 scripts/validate_engine_kits.py
```

Validate the repo:

```bash
python3 scripts/validate_repo_layout.py
python3 scripts/validate_docs.py
python3 scripts/validate_assets.py
```

Or:

```bash
make validate
make ci-local
```

Godot reference-slice validation:

```bash
python3 scripts/godot_smoke.py --static-only
python3 scripts/godot_smoke.py
python3 -m pytest -q tests/test_godot_surface.py
```

Godot export:

```bash
python3 scripts/godot_export.py --preset "Linux/X11"
python3 scripts/godot_export.py --preset "Windows Desktop"
```

Unity command generation:

```bash
python3 scripts/unity_adapter.py test --project-path studio/starter-kits/unity-6/scaffold --dry-run --json
python3 scripts/unity_adapter.py build --project-path studio/starter-kits/unity-6/scaffold --dry-run --json
```

If a local Unity editor is not auto-detected, append `--unity-path tools/engine-stubs/unity/Unity` for stub-backed contract smoke.

Unreal command generation:

```bash
python3 scripts/unreal_adapter.py package --project-path studio/starter-kits/unreal-5/scaffold --uat-path tools/engine-stubs/unreal/RunUAT.sh --dry-run --json
```

CI/CD helpers:

```bash
make ci-workflows
make ci-doc-sync
make ci-quality
make ci-report
make starter-kit-smoke
python3 scripts/starter_kit_contract_smoke.py --engine unity-6 --json
python3 scripts/ci_artifact_report.py --output-dir build/ci/manual --label manual-check
```

Engine contract smoke by family:

```bash
python3 scripts/starter_kit_contract_smoke.py --engine godot-4 --json
python3 scripts/starter_kit_contract_smoke.py --engine unity-6 --json
python3 scripts/starter_kit_contract_smoke.py --engine unreal-5 --json
```

Print studio status:

```bash
python3 scripts/studio_status.py
```

## Docs and Presets

Bootstrap active docs:

```bash
# Godot 4 baseline
python3 scripts/bootstrap_studio.py \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite

# Unity 6 baseline
python3 scripts/bootstrap_studio.py \
  --project-name "Your Game" \
  --engine unity-6 \
  --platform pc-premium \
  --genre tactical-rpg

# Unreal 5 baseline
python3 scripts/bootstrap_studio.py \
  --project-name "Your Game" \
  --engine unreal-5 \
  --platform console-premium \
  --genre co-op-survival
```

Replace the preset pack:

```bash
python3 scripts/apply_preset.py --engine godot-4 --platform pc-premium --genre action-roguelite --replace
python3 scripts/apply_preset.py --engine unity-6 --platform pc-premium --genre tactical-rpg --replace
python3 scripts/apply_preset.py --engine unreal-5 --platform console-premium --genre co-op-survival --replace
```

## Routing and Planning

Find the likely workflow for a task:

```bash
python3 scripts/codex_studio.py next "Add aim assist tuning for controller combat"
```

Build an agent validation matrix:

```bash
python3 scripts/codex_studio.py next "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible"
python3 scripts/codex_studio.py checklist --task "Build validation matrices for a multi-agent UI and QA pass while keeping single specialist mode visible"
```

Resolve the merged checklist bundle:

```bash
python3 scripts/codex_studio.py checklist --task "Add aim assist tuning for controller combat"
```

Scaffold a research note:

```bash
python3 scripts/codex_studio.py research --category systems --title "Aim assist architecture"
```

Inspect the engine research pack:

```bash
ls docs/research/game-development/engines
sed -n '1,80p' docs/research/game-development/engines/README.md
sed -n '1,120p' docs/research/game-development/engines/unity-classes.md
```

Scan for top gaps:

```bash
python3 scripts/project_radar.py --warn-only
```

## Scaffolding

Feature brief + ADR + test plan:

```bash
python3 scripts/scaffold_feature.py "Core Combat" --with-adr --with-test-plan --with-eval-plan
```

This now creates the feature brief plus default `handoff-*.md`, `traceability-*.md`, and optional validation docs unless you explicitly pass `--no-handoff` or `--no-traceability`.

Bug triage docs:

```bash
python3 scripts/scaffold_bugfix.py "Save Corruption After Alt-F4" --with-test-plan --with-eval-plan
```

This creates the bug report and crash triage docs, plus validation docs when you want the bug package to move as a single review bundle.

Prompt history and agent journal

Use this when you need prompt history and agent journal records in one append-only file.

```bash
python3 scripts/codex_studio.py journal prompt \
  --prompt "Add a prompt history log and an agent journal so the user can review later." \
  --route "prompt history / agent journal" \
  --summary "Created append-only journal sections and a journal command." \
  --doc docs/reference/prompt-journal.md \
  --json

python3 scripts/codex_studio.py journal agent \
  --step "Draft the journal template and journal command" \
  --expected "One active file with two append-only sections" \
  --found "The repo had no durable history trail yet" \
  --improved "Added a shared prompt journal file and append helper" \
  --evaluation "The record is now easy to reopen later without reading the whole chat" \
  --doc docs/reference/prompt-journal.md \
  --validation "python3 scripts/journal.py prompt --dry-run --json" \
  --json
```

Agent transcript

Use this when agent assignments or back-and-forth conversation turns should stay reviewable later.

```bash
python3 scripts/codex_studio.py journal transcript \
  --kind assignment \
  --task "Profile the inventory HUD and report the first bottleneck" \
  --speaker "Kaynexis" \
  --target "technical_director, qa_lead" \
  --message "Capture one baseline, one likely bottleneck, and one first lever before any refactor." \
  --json

python3 scripts/codex_studio.py journal transcript \
  --kind conversation \
  --speaker "technical_director" \
  --target "qa_lead" \
  --message "Use a shared baseline before changing pooling or layout code." \
  --json
```

Use this when you want a later-review trail that records both the user prompt and the agent's step notes in one append-only file.

QA matrix:

```bash
python3 scripts/generate_qa_matrix.py "Vertical Slice"
```

Eval plan:

```bash
python3 scripts/scaffold_eval_plan.py "Reviewer Prompt Refresh"
```

## Make Targets

Show the target list:

```bash
make help
```

Common targets:

- `make studio`
- `make setup`
- `make start`
- `make baseline`
- `make doctor`
- `make evals`
- `make engine-kits`
- `make validate`
- `make ci-local`
- `make test`
- `make godot-smoke`
- `make godot-smoke-strict`
- `make export-linux`
- `make export-windows`
- `make unity-test-command`
- `make unity-build-command`
- `make unreal-package-command`
- `make status`
- `make radar`
- `make route TASK="..."`
- `make checklist TASK="..."`
- `make research EVAL_TITLE="..."`
- `make feature FEATURE="..."` now emits the feature brief, handoff, traceability, test plan, and eval plan bundle
- `make bug BUG="..."` now emits the bug report, crash triage, test plan, and eval plan bundle
- `make qa QA_TITLE="..."`
- `make eval EVAL_TITLE="..."`
- `make hooks-enable`
- `make hooks-disable`
- `make docker-verify`

## Optional Docker Commands

Build the helper container:

```bash
docker compose build
```

Open a shell in the helper container:

```bash
docker compose run --rm app
```
