# CI/CD

## Goals
- Keep local validation and GitHub Actions aligned instead of maintaining two different truths
- Produce artifacts that explain what CI actually checked
- Separate contract-level engine validation from real editor-backed validation

## Workflow map
- `validate.yml`: main-branch core repo validation, targeted Godot tests, version guard, validate artifact report, and CI quality gate
- `studio/docs/active/eval-ci-cd.md`: active eval plan for validate workflow hardening and artifact coverage
- `repo-validate.yml`: Python matrix for repo validation, evals, tests, routing smoke, adapter smoke, and artifact reports
- `doc-sync.yml`: changed-path doc sync guard for code, scripts, presets, and doc surfaces
- `docker-smoke.yml`: helper container build and smoke import, plus uploaded report
- `starter-kit-contracts.yml`: engine-by-engine contract smoke for Godot, Unity, and Unreal starter kits
- `release-readiness.yml`: manual readiness bundle for a named release check that now requires release-ready quality and no remaining external dependencies
- `studio/docs/active/eval-release-hardening.md`: active eval plan for protected-build hardening, code protection, and multiplayer trust
- `nightly-audit.yml`: scheduled full-stack audit that runs the local CI equivalent and uploads a nightly bundle
- Dependabot action-bump PRs skip doc-sync enforcement, but the rest of repo validation still runs so workflow and dependency changes stay honest

## Local commands
- `make validate`: fast layout/docs/assets/workflow validation
- `make ci-local`: compile, workflow validation, doctor, evals, tests, docs validation, versioning, and CI artifact report
- `make ci-quality`: generate a CI report and enforce the local quality gate
- `make ci-doc-sync`: run the repo-to-doc sync guard against the current working tree
- `make ci-workflows`: validate the GitHub workflow surface itself
- `make ci-report`: generate `build/ci/latest/ci-report.json` and `build/ci/latest/ci-report.md`
- `make bench`: run the repo-local benchmark corpus
- `make version`: validate the canonical version file and changelog sync
- `make starter-kit-smoke`: run contract smoke across all supported engines
- `make feature FEATURE="..."`: scaffold a feature brief, handoff, traceability, test plan, and eval plan bundle
- `make bug BUG="..."`: scaffold a bug report, crash triage, test plan, and eval plan bundle
- `python3 scripts/run_bench.py --json`: print the benchmark report as JSON
- `python3 scripts/version_guard.py --json`: print the version guard report as JSON
- `python3 scripts/doc_sync_audit.py --json`: surface docs that likely need review after code or content changes
- `python3 scripts/doc_sync_guard.py --json`: fail when changed code is missing the corresponding doc refresh
- `python3 scripts/ci_quality_gate.py --report build/ci/latest/ci-report.json --min-score 80 --minimum-readiness validation-ready`: enforce the current quality threshold
- `python3 scripts/ci_quality_gate.py --report build/ci/latest/ci-report.json --min-score 90 --minimum-readiness release-ready --forbid-external-dependencies`: enforce the release-readiness threshold

## Artifact outputs
- `build/ci/validate`: validate workflow smoke, version guard, quality gate, and artifact report bundle
- `build/ci/repo-validate/<python-version>`: per-matrix validation artifacts
- `build/ci/consolidated`: post-matrix summary
- `build/ci/starter-kit/<engine>`: per-engine contract smoke outputs
- `build/ci/release`: manual release-readiness bundle with version metadata and strict quality gate results
- `build/ci/version`: version guard bundle with the current version and changelog sync state
- `build/ci/nightly`: scheduled audit bundle
- `build/ci/*/ci-report.*`: scored CI reports with readiness and external dependency summaries
- `build/ci/doc-sync`: doc sync guard report bundle
- `build/bench/*/bench-report.*`: benchmark reports with family, baseline, threshold, and artifact metadata

## Validation layers
- Repo structure: `scripts/validate_repo_layout.py`
- Active docs semantic quality: `scripts/validate_docs.py`
- Workflow surface: `scripts/validate_workflows.py`
- Starter-kit manifests and command references: `scripts/validate_engine_kits.py`
- Engine contract smoke: `scripts/starter_kit_contract_smoke.py`
- Workflow/eval regression: `scripts/run_local_evals.py`
- Repo-local benchmark corpus: `scripts/run_bench.py`
- CI artifact reporting: `scripts/ci_artifact_report.py`
- Versioning guard: `scripts/version_guard.py`
- Doc sync audit reminders: `scripts/doc_sync_audit.py`
- Doc sync guard: `scripts/doc_sync_guard.py`
- CI quality gate: `scripts/ci_quality_gate.py`
- Release hardening: `docs/reference/release-hardening-guide.md`, `docs/examples/release-hardening-example.md`, `docs/research/game-development/production/release-hardening.md`, `studio/checklists/discipline/release_hardening.toml`, and `studio/docs/active/eval-release-hardening.md`
- Engine research now includes visuals/animation, UI, and audio/presentation playbooks, so sprite, texture, HUD, menu, audio, animation, and VFX changes stay visible to both routing and doc-sync checks.
- The user-facing engine example page at `docs/reference/engine-examples.md` is also part of the doc-validation surface, so changes to engine examples should be reviewed alongside the matching engine-selection and workflow docs.
- The genre development playbook at `docs/research/game-development/genre/genre-guide.md` is also part of that surface, so new or revised genre build guidance should stay synchronized with the matching preset, example matrix, and starter docs.
- Genre research now includes additional presets and architecture notes for city-builder, life-sim, hero-shooter, and soulslike support, so updates to those presets should keep the matching catalog, example matrix, and active starter docs in sync.
- Genre research now also includes auto-battler, grand-strategy, and stealth support, so those preset families should follow the same sync rule before merge.
- The starter-template surface now also includes `docs/examples/README.md`, `reference/handoff-contracts.md`, and `reference/feature-traceability.md`, so changes to genre starter docs should keep those references aligned with the template and with the advanced maturity framework.
- The lorebook methodology at `docs/reference/lorebook-methodology.md` is now part of the same doc-sync surface, so lorebook briefs, canon notes, and example entries should stay aligned with narrative routing and quest guidance.
- The world graph methodology at `docs/reference/world-graph-methodology.md` is now part of the same doc-sync surface, so relationship graphs, history notes, and example entries should stay aligned with narrative routing and quest guidance.
- The engine class atlas and game systems atlas are part of the same agent lookup surface, so gameplay, save, UI, and narrative system changes should keep the atlas references in the matching briefs, handoffs, and examples aligned.
- The feature scaffold now emits atlas references in generated briefs, handoffs, traceability docs, and eval-plan stubs, so CI review should treat atlas drift the same way it treats template drift.
- The bugfix scaffold and eval-plan scaffold now emit the same atlas references, so bug triage and evaluation docs should be reviewed with the same atlas-aware discipline.
- The bugfix scaffold can now emit test plan and eval plan stubs, so the CI review loop should expect a bugfix package to include validation docs when requested.
- The feature scaffold should be treated the same way: if a slice is complex enough to need an eval or test plan, the generated docs are part of the authoritative review bundle.
- `studio/docs/active/eval-ci-cd.md` tracks validate workflow hardening and artifact coverage, so CI/CD changes should keep that active note synchronized with the workflow file and this guide.
- The advanced performance guide and example now sit in the same routing surface, so algorithm-heavy perf work should keep `docs/reference/advanced-perf-guide.md`, `docs/examples/advanced-perf-example.md`, and `docs/research/game-development/foundations/perf-algorithms.md` in sync with the relevant perf notes.
- The quality guide and example now sit in the same routing surface, so code quality and optimization-criteria work should keep `docs/reference/quality-guide.md`, `docs/examples/quality-example.md`, and `docs/reference/code-review.md` in sync with the relevant review notes.
- The quality control process now sits in the same routing surface, so quality-control work should keep `docs/reference/quality-process.md`, `docs/examples/quality-process-example.md`, `docs/reference/quality-guide.md`, and `docs/reference/code-review.md` in sync with the relevant review notes and evidence path.
- The benchmark guide, example, runner, and eval strategy now sit in the same routing surface, so measurement work should keep `docs/reference/benchmark-guide.md`, `docs/examples/benchmark-example.md`, `docs/research/game-development/foundations/benchmarks.md`, and `docs/reference/eval-strategy.md` in sync with the report path.
- The version guide, example, changelog, and release metadata now sit in the same routing surface, so versioning work should keep `docs/reference/version-guide.md`, `docs/examples/version-example.md`, `docs/research/game-development/production/versioning.md`, `CHANGELOG.md`, and `VERSION` in sync with the report path.
- The short-name rule now lives in `studio/checklists/base/naming.toml`, so rename or simplification work should keep that checklist, the repo tour, and the validation surface aligned together.
- The build-release checklist now also carries a CI short-name rule, so workflow names, job labels, artifact labels, and report filenames should stay short and canonical as part of release readiness.
- The canonical short references now include `genre-maturity.md`, `lorebook.md`, `world-graph.md`, `engine-quick-map.md`, `engine-atlas.md`, and `game-systems-atlas.md`, so the router and the docs should avoid the retired verbose filenames.
- Local toolchain detection now prefers the stable Unity editor install, the Homebrew Godot binary when present, and the repo-local Unreal UAT stub for contract coverage, so CI and doctor output should be read as "real toolchain when available, stub when intentionally accepted" rather than as a blind pass/fail on installer presence.
- Release-oriented checklist resolution also surfaces the build-release layer, so release bundles inherit the same naming discipline instead of drifting into a separate release-only vocabulary.
- Version-aware release bundles also surface the versioning layer, so the version file, changelog, commit notes, and release tags stay in the same review bundle.
- The validate workflow now also runs the version guard and CI quality gate, so main-branch checks expose the same version metadata and readiness threshold as the local CI path.
- The release-readiness workflow now requires release-ready status and no external dependencies, so release bundles should be interpreted as a stricter signal than validation-only runs.

## Engine policy
- Godot can run real runtime/export checks when `GODOT_BIN` exists
- Unity and Unreal use repo-local stubs in CI for adapter contract smoke
- Full editor-backed CI only counts once `UNITY_CLI`, `UNREAL_UAT`, or `UNREAL_EDITOR` is wired to real installations
- CI reports include a simple quality score and readiness label so the team can tell when the repo is validation-ready versus release-ready
- Versioning checks now publish a small artifact bundle so prerelease and release-tag state is visible in the same CI summary as the rest of the repo health data
- The validate workflow now publishes version metadata too, so version drift can be inspected from the same main-branch artifact bundle as the rest of CI health data.

## Failure handling
- If `validate_workflows.py` fails, treat it as CI infrastructure drift, not a content bug
- If `starter_kit_contract_smoke.py` fails, treat it as engine-surface regression before feature regression
- If `ci-report` shows external dependencies, do not present the pipeline as shipping-ready
- If `doc_sync_audit` suggests a doc after a code change, review the linked doc before merging
- If `doc_sync_guard` fails, update the linked docs before merging rather than bypassing the guard
- If a Dependabot PR only bumps workflow actions, the doc-sync guard is allowed to skip that PR rather than force a documentation refresh
- If `ci_quality_gate` fails, either improve the repo signal or reduce the scope before declaring the pipeline healthy
