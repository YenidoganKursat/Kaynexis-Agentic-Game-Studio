# CI/CD Architecture

## Goals
- Keep local validation and GitHub Actions aligned instead of maintaining two different truths
- Produce artifacts that explain what CI actually checked
- Separate contract-level engine validation from real editor-backed validation

## Workflow map
- `repo-validate.yml`: Python matrix for repo validation, evals, tests, routing smoke, adapter smoke, and artifact reports
- `doc-sync.yml`: changed-path doc sync guard for code, scripts, presets, and doc surfaces
- `docker-smoke.yml`: helper container build and smoke import, plus uploaded report
- `starter-kit-contracts.yml`: engine-by-engine contract smoke for Godot, Unity, and Unreal starter kits
- `release-readiness.yml`: manual readiness bundle for a named release check
- `nightly-audit.yml`: scheduled full-stack audit that runs the local CI equivalent and uploads a nightly bundle

## Local commands
- `make validate`: fast layout/docs/assets/workflow validation
- `make ci-local`: compile, workflow validation, doctor, evals, tests, docs validation, and CI artifact report
- `make ci-quality`: generate a CI report and enforce the local quality gate
- `make ci-doc-sync`: run the repo-to-doc sync guard against the current working tree
- `make ci-workflows`: validate the GitHub workflow surface itself
- `make ci-report`: generate `build/ci/latest/ci-report.json` and `build/ci/latest/ci-report.md`
- `make starter-kit-smoke`: run contract smoke across all supported engines
- `python3 scripts/doc_sync_audit.py --json`: surface docs that likely need review after code or content changes
- `python3 scripts/doc_sync_guard.py --json`: fail when changed code is missing the corresponding doc refresh
- `python3 scripts/ci_quality_gate.py --report build/ci/latest/ci-report.json --min-score 80 --minimum-readiness validation-ready`: enforce the current quality threshold

## Artifact outputs
- `build/ci/repo-validate/<python-version>`: per-matrix validation artifacts
- `build/ci/consolidated`: post-matrix summary
- `build/ci/starter-kit/<engine>`: per-engine contract smoke outputs
- `build/ci/release`: manual release-readiness bundle
- `build/ci/nightly`: scheduled audit bundle
- `build/ci/*/ci-report.*`: scored CI reports with readiness and external dependency summaries
- `build/ci/doc-sync`: doc sync guard report bundle

## Validation layers
- Repo structure: `scripts/validate_repo_layout.py`
- Active docs semantic quality: `scripts/validate_docs.py`
- Workflow surface: `scripts/validate_workflows.py`
- Starter-kit manifests and command references: `scripts/validate_engine_kits.py`
- Engine contract smoke: `scripts/starter_kit_contract_smoke.py`
- Workflow/eval regression: `scripts/run_local_evals.py`
- CI artifact reporting: `scripts/ci_artifact_report.py`
- Doc sync audit reminders: `scripts/doc_sync_audit.py`
- Doc sync guard: `scripts/doc_sync_guard.py`
- CI quality gate: `scripts/ci_quality_gate.py`
- Engine research now includes visuals/animation playbooks, so sprite, texture, animation, and VFX changes stay visible to both routing and doc-sync checks.
- The user-facing engine example page at `docs/reference/engine-examples.md` is also part of the doc-validation surface, so changes to engine examples should be reviewed alongside the matching engine-selection and workflow docs.
- The genre development playbook at `docs/research/game-development/genre/genre-development-playbook.md` is also part of that surface, so new or revised genre build guidance should stay synchronized with the matching preset, example matrix, and starter docs.
- Genre research now includes additional presets and architecture notes for city-builder, life-sim, hero-shooter, and soulslike support, so updates to those presets should keep the matching catalog, example matrix, and active starter docs in sync.
- Genre research now also includes auto-battler, grand-strategy, and stealth support, so those preset families should follow the same sync rule before merge.
- The starter-template surface now also includes `docs/examples/README.md`, `reference/handoff-contracts.md`, and `reference/feature-traceability.md`, so changes to genre starter docs should keep those references aligned with the template and with the advanced maturity framework.
- The lorebook methodology at `docs/reference/lorebook-methodology.md` is now part of the same doc-sync surface, so lorebook briefs, canon notes, and example entries should stay aligned with narrative routing and quest guidance.
- The world graph methodology at `docs/reference/world-graph-methodology.md` is now part of the same doc-sync surface, so relationship graphs, history notes, and example entries should stay aligned with narrative routing and quest guidance.

## Engine policy
- Godot can run real runtime/export checks when `GODOT_BIN` exists
- Unity and Unreal use repo-local stubs in CI for adapter contract smoke
- Full editor-backed CI only counts once `UNITY_CLI`, `UNREAL_UAT`, or `UNREAL_EDITOR` is wired to real installations
- CI reports include a simple quality score and readiness label so the team can tell when the repo is validation-ready versus release-ready

## Failure handling
- If `validate_workflows.py` fails, treat it as CI infrastructure drift, not a content bug
- If `starter_kit_contract_smoke.py` fails, treat it as engine-surface regression before feature regression
- If `ci-report` shows external dependencies, do not present the pipeline as shipping-ready
- If `doc_sync_audit` suggests a doc after a code change, review the linked doc before merging
- If `doc_sync_guard` fails, update the linked docs before merging rather than bypassing the guard
- If `ci_quality_gate` fails, either improve the repo signal or reduce the scope before declaring the pipeline healthy
