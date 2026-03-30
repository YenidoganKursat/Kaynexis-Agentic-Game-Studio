# Roadmap

This document turns the earlier theoretical review into an actionable product roadmap for the `studio template` template.

## Goal

Move the package from a strong "studio workflow kit" into a more execution-ready "game production operating layer" without turning it into bloated pseudo-autonomy.

## Top 10 Must-Have Additions

1. Engine starter kits
   - Add real starter skeletons for Godot, Unity, and Unreal.
   - Include canonical folder layout, sample scene/module, test entry point, and minimal CI assumptions.

2. CI and release templates
   - Add ready-made build pipelines for validation, smoke tests, exports, and release artifacts.
   - Cover at least local validation plus one hosted CI example.

3. Prompt regression suite
   - Add a small test corpus for skills and agents.
   - Verify routing quality, output structure, and handoff consistency over time.

4. Handoff contracts
   - Standardize what every role must output: scope, evidence, risk, validation, owner, blockers, next step.
   - Make cross-role work reviewable instead of conversationally fuzzy.

5. Feature traceability
   - Link feature brief -> ADR -> code path -> tests -> release note.
   - This is the missing glue between docs and implementation.

6. Save system and migration patterns
   - Add save schema examples, migration templates, and corruption recovery guidance.
   - This is a recurring high-risk area in games and deserves a first-class path.

7. Telemetry and balancing examples
   - Include event catalog examples, naming rules, KPI mapping, and a tiny balancing simulator.
   - Make economy and retention discussions less abstract.

8. Platform readiness packs
   - Expand platform guidance into concrete checklists for mobile, web, console, and PC release readiness.
   - Include input, perf, packaging, compliance, and storefront deltas.

9. Example outputs
   - Add one truly good example for a feature brief, ADR, QA matrix, bug report, perf pass, and postmortem.
   - This will improve output quality more than adding more roles.

10. Repo-to-doc sync helpers
   - Add small automations that detect when docs likely need refresh after code or content changes.
   - The template already values durable repo state; this makes that promise real.

## Delivery Status

The original top-10 roadmap items are now represented in the repo. This table is the current source of truth for whether each item is still missing or already delivered.

| Roadmap item | Status | Evidence |
|---|---|---|
| Engine starter kits | Delivered | `studio/starter-kits/godot-4/`, `studio/starter-kits/unity-6/`, `studio/starter-kits/unreal-5/`, plus engine setup docs and adapters |
| CI and release templates | Delivered | `.github/workflows/`, `docs/reference/ci-cd.md`, `studio/docs/active/build-pipeline.md`, `studio/docs/templates/release-checklist.md` |
| Prompt regression suite | Delivered | `evals/`, `scripts/run_local_evals.py`, `scripts/validate_repo_layout.py`, `tests/test_studio_system.py` |
| Handoff contracts | Delivered | `studio/docs/templates/handoff-contract.md`, `docs/examples/handoff-example.md`, `docs/reference/handoff-contracts.md` |
| Feature traceability | Delivered | `studio/docs/templates/feature-traceability.md`, `docs/examples/traceability-example.md`, `docs/reference/feature-traceability.md` |
| Save system and migration patterns | Delivered | `docs/research/game-development/systems/save.md`, `studio/docs/templates/save-migration-plan.md`, `docs/examples/test-example.md`, `docs/examples/traceability-example.md` |
| Telemetry and balancing examples | Delivered | `studio/docs/active/telemetry-schema.md`, `docs/reference/balance-simulator.md`, `scripts/balance_simulator.py` |
| Platform readiness packs | Delivered | `studio/docs/active/platform-targets.md`, `studio/playbooks/porting-program.md`, `studio/presets/platform/`, `docs/research/game-development/production/platform.md` |
| Example outputs | Delivered | `docs/examples/feature-example.md`, `docs/examples/adr-example.md`, `docs/examples/qa-example.md`, `docs/examples/bug-example.md`, `docs/examples/perf-example.md`, `docs/examples/postmortem-example.md` |
| Repo-to-doc sync helpers | Delivered | `scripts/doc_sync_guard.py`, `scripts/validate_docs.py`, `scripts/validate_workflows.py`, `tests/test_ci_surface.py` |

## Remaining External Gap

The roadmap items above are complete in-repo, but one external gap still matters for release-grade confidence:

- runner-backed engine-native smoke for Godot, Unity, and Unreal on a real CI runner
- real editor/export packaging coverage for the engine binaries instead of contract stubs alone

That gap is operational, not a missing template. It is the thing left to finish when the roadmap asks for "real release parity" instead of "local contract parity."

## Phased Roadmap

## Phase 1: Hardening

Primary objective: make the current package safer and cleaner.

- Remove packaged `__pycache__` artifacts from releases.
- Add validation for agent/skill metadata consistency.
- Add a release checklist for the template itself.
- Add smoke tests for all helper scripts.
- Add versioned changelog expectations for presets, skills, and scripts.

Success condition:
- The package can be validated locally in one command.
- A release zip contains only intended source assets.

## Phase 2: Execution Layer

Primary objective: reduce the gap between planning and real implementation.

- Add engine starter kits.
- Add feature traceability scaffolding.
- Add handoff contract templates.
- Add code-path aware feature scaffolding.
- Add example implementation slices for one engine.

Success condition:
- A new repo can go from bootstrap -> feature brief -> starter implementation with minimal manual setup.

## Phase 3: Production Readiness

Primary objective: make the template useful after prototype stage.

- Add save-system playbooks and migration patterns.
- Add telemetry schema examples plus balancing helpers.
- Add platform-specific release packs.
- Add incident / hotfix / rollback workflow support.
- Add liveops and community feedback ingestion patterns.

Success condition:
- The package can support a vertical slice, a playtest, and a first release candidate without major process gaps.

## Phase 4: Quality Intelligence

Primary objective: make the system measurable and self-checking.

- Add prompt regression suite.
- Add quality scoring for docs and handoffs.
- Add risk scoring to sprint and milestone docs.
- Add coverage checks for feature brief -> test plan -> release gate alignment.
- Add recommended dashboards or structured status summaries.

Success condition:
- The team can tell whether the operating system is improving output quality or just generating more text.

## Phase 5: Versioning

Primary objective: make release identity explicit and durable.

- Add a canonical `VERSION` file at the repo root.
- Keep `CHANGELOG.md`, release tags, and artifact provenance aligned with the same version family.
- Add a version guard so prerelease and release states are visible before packaging.
- Surface versioning as a first-class checklist and routing concern instead of hiding it inside generic release work.

Success condition:
- Another operator can answer "what version is this?" from one file, one changelog, and one CI artifact bundle without guessing.

## What Should Not Be Added Yet

These ideas sound impressive but are likely to create noise before they create value:

- More agents just to cover narrower sub-specialties
- Fully autonomous backlog management
- Heavy database infrastructure for docs before file-based workflows hit their limit
- Complex orchestration graphs with no real execution proof
- Marketplace-style preset explosion without strong examples
- Over-automated producer behavior that hides tradeoffs instead of surfacing them

## Highest-Leverage V3 Deliverables

If only a few things get built, these should land first:

1. Engine starter kits
2. Handoff contracts
3. Example outputs
4. CI/release templates
5. Prompt regression suite

Those five would shift the package from "well-structured idea" to "seriously reusable operating layer."

## Product Positioning

Today:
- Strong workflow template
- Strong role framing
- Strong document scaffolding
- Weak direct execution bridge

Target V3:
- Strong workflow template
- Strong role framing
- Strong document scaffolding
- Strong execution bridge
- Measurable output quality

## Final Take

The next version should not try to be more autonomous.
It should try to be more reliable, more reproducible, and closer to real game production work.

That means fewer "new clever concepts" and more:
- starter implementations
- validated examples
- traceable workflows
- role handoff discipline
- release-grade operational support
