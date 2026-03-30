# Build Pipeline — Kaynexis Agentic Game Studio

## Build graph
- Source -> route/checklist/research alignment -> repo validation -> starter-kit validation -> local evals -> engine-native smoke -> package -> artifact -> distribution

## Environments
- Local: `make ci-local`
- Front door: `python3 scripts/codex_studio.py`
- Validate: `.github/workflows/validate.yml`
- CI: `.github/workflows/repo-validate.yml`
- Doc sync gate: `.github/workflows/doc-sync.yml`
- Starter-kit matrix: `.github/workflows/starter-kit-contracts.yml`
- Release gate bundle: `.github/workflows/release-readiness.yml`
- Nightly audit: `.github/workflows/nightly-audit.yml`
- Container check: `.github/workflows/docker-smoke.yml` and `make docker-verify`
- Adapter contract smoke: repo-local Unity/Unreal tool stubs keep dry-run checks honest in CI
- Release: real editor/export jobs only count as complete once engine binaries are present on the runner
- Repo validation now includes a doc-sync guard and a minimum CI quality gate, so code or workflow changes must be accompanied by the docs they affect
- The validate workflow now runs the core repo validation path plus a targeted Godot smoke, version guard, validate artifact report, and CI quality gate, so main-branch gates should keep that workflow pinned and synchronized with the validator surface
- The matching eval plan lives at `studio/docs/active/eval-ci-cd.md`, so workflow hardening should keep that active note synchronized with the workflow file and the CI/CD doc
- The example surface in `docs/reference/engine-examples.md` is part of that doc-sync scope, so engine example updates should be validated like other engine support docs
- The genre development playbook at `docs/research/game-development/genre/genre-guide.md` is part of the same sync scope, so build-facing genre changes should update the playbook, the preset catalog, and the active starter together
- When adding or revising genre presets, keep the matching architecture note, example matrix row, and starter doc updated together so the support surface stays truthful for teams choosing city-builder, life-sim, hero-shooter, or soulslike paths
- The same rule now applies to auto-battler, grand-strategy, and stealth support as well, because those families change route, checklist, and first-slice advice together.
- The starter-template surface also pulls in `docs/examples/README.md`, `reference/handoff-contracts.md`, and `reference/feature-traceability.md`, so build-facing template changes should keep those execution docs current too.
- The genre advanced development framework now defines the maturity path for every supported genre family, so build readiness discussions should use it when deciding whether a genre is still in first-slice or already in scale-up mode.
- The lorebook methodology now defines the narrative canon surface, so build readiness discussions should keep `docs/reference/lorebook-methodology.md`, the lorebook brief, and narrative research notes synchronized before implementation.
- The world graph methodology now defines the relationship and history surface, so build readiness discussions should keep `docs/reference/world-graph-methodology.md`, the world graph brief, and narrative research notes synchronized before implementation.
- The engine atlas and game systems atlas now define the cross-engine ownership surface, so build readiness discussions should keep `docs/reference/engine-atlas.md`, `docs/reference/system-atlas.md`, and the matching example snippets in sync before implementation.
- The feature scaffold now generates atlas-aware briefs, handoffs, traceability docs, and eval-plan stubs, so build readiness should treat those generated docs as part of the authoritative build contract.
- The bugfix scaffold and eval-plan scaffold now generate atlas-aware triage and validation docs as well, so build readiness should treat bug reports, crash triage, and eval plans as part of the same authoritative contract.
- The advanced performance guide now handles algorithmic scale decisions, so build readiness discussions about culling, partitioning, batching, instancing, jobs, or state compression should keep `docs/reference/advanced-perf-guide.md`, `docs/examples/advanced-perf-example.md`, and `docs/research/game-development/foundations/perf-algorithms.md` aligned with the engine-specific perf notes.
- When the bugfix scaffold is invoked with validation flags, the resulting test plan and eval plan should be treated as first-class build evidence rather than optional notes.
- When the feature scaffold is invoked with validation flags, the resulting test plan and eval plan should be treated the same way and kept attached to the slice until merge.
- The `make feature` and `make bug` helper targets now mirror the scaffold bundle shape, so build readiness discussions should treat those commands as the preferred way to create reviewable feature or bug packages.
- The short-name rule now lives in `studio/checklists/base/naming.toml`, so build readiness discussions about renames or simplification should keep that checklist, the repo tour, and the validation surface aligned together.
- The build-release checklist now adds a CI short-name rule, so workflow names, job labels, artifact labels, and report filenames should stay short and canonical when release readiness work changes them.
- The canonical short refs for this pipeline now include `engine-quick-map.md`, `engine-atlas.md`, `game-systems-atlas.md`, `genre-maturity.md`, `lorebook.md`, and `world-graph.md`, so the front door and the router should not drift back to the retired verbose filenames.
- The local toolchain lookup now prefers the stable Unity editor install, the Homebrew Godot binary when present, and the repo-local Unreal UAT stub for contract coverage, so build-readiness checks should treat those as the current local contract surface and reserve "external dependency" language for genuinely missing coverage.
- Release-readiness bundles also resolve the build-release checklist, so the release path and the packaging path stay aligned on artifact naming and build assumptions.
- Release readiness now enforces `release-ready` status and forbids external dependencies, so the release bundle should be treated as a stricter signal than validation-only CI.
- Release-hardening bundles also resolve the release_hardening checklist, so protected builds, symbol policy, and multiplayer trust boundaries stay aligned with the build and release path instead of drifting into a separate one-off policy.
- Dependabot action-bump PRs may skip doc-sync enforcement, but only for workflow dependency bumps; normal feature or content changes still have to refresh the matching docs before merge.
- The validator now treats the expanded engine atlas families as first-class coverage, so this build pipeline note and the maintainer GitHub setup doc should stay aligned with `docs/reference/engine-atlas.md` and the matching research docs whenever new engine structures are added.
- The validate workflow now also emits version metadata, so the build pipeline note should stay aligned with `VERSION`, `CHANGELOG.md`, and the versioning checks as well.

## Engine contracts
- Godot 4: `python3 scripts/godot_smoke.py --static-only`, optional runtime smoke, then `python3 scripts/godot_export.py --preset "..."`
- Unity 6: the adapter auto-detects standard macOS Unity Hub installs when available; otherwise use `tools/engine-stubs/unity/Unity` for contract smoke only, or set a real `UNITY_CLI` path for editor-backed tests/builds
- Unreal 5: use `tools/engine-stubs/unreal/RunUAT.sh` for command-contract smoke; switch to a real `UNREAL_UAT` or `UNREAL_EDITOR` path for packaging work
- When a feature changes sprites, textures, HUDs, menus, audio, animation, or particle/VFX ownership, make the matching visuals/animation, UI, and audio/presentation playbooks part of the build-readiness check so presentation changes are validated alongside runtime ownership

## Artifacts & versioning
- Keep artifact names deterministic
- Treat `VERSION` as the source of truth for the working-tree version
- Keep `CHANGELOG.md` and release tags aligned with the same version family
- Store release notes, validation commands, and build provenance alongside artifacts
- Emit `build/ci/*` report bundles so CI failures have portable evidence instead of only console logs
- Add symbols or crash artifacts once the engine-specific build pipeline exists

## Failure / rollback
- If validation or evals regress, stop before merge
- If Docker or workflow changes break, revert the smallest change first
- Record release or infra regressions in `studio/docs/active/risk-register.md` and an eval plan when shared behavior changed
- If the doc-sync guard fails, update the impacted docs before merging instead of bypassing the gate
- If the failing PR is a Dependabot workflow-action bump, prefer the documented doc-sync skip instead of widening the guard for normal feature work
