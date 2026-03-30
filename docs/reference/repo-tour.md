# Repo Tour

This repository has two major layers:

- the operating layer that tells Codex how to work
- the live project layer that captures what the current game actually is

## Structure packs

The repo now prefers a small set of durable structure packs instead of one generic prompt shape.

For the compact front door, start with `docs/reference/studio-map.md`.

| Pack | What it covers | Key docs |
| --- | --- | --- |
| speed pack | fastest safe start, smallest useful bundle, and short validation | `docs/setup/quick-access.md`, `docs/reference/agent-speedpack.md`, `docs/examples/agent-speedpack-example.md`, `studio/checklists/discipline/speedpack.toml` |
| operating model | controller, role matrix, hierarchy, validation, and review trails | `docs/reference/agent-system.md`, `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, `docs/reference/agent-hierarchy.md`, `docs/reference/agent-validation-matrix.md` |
| work packets | execution packets, prompt history, and transcript history | `docs/reference/agent-execution.md`, `docs/reference/prompt-journal.md`, `docs/reference/agent-transcript.md` |
| capability catalog | repo-wide capability families, starter docs, and short intro shapes | `docs/reference/capabilities.md`, `docs/examples/capabilities-example.md`, `docs/research/game-development/foundations/capabilities.md` |
| engine / gameplay | engine selection, object ownership, engine atlas, system atlas, and recurring engine bug families | `docs/reference/engine-map.md`, `docs/reference/engine-atlas.md`, `docs/reference/system-atlas.md`, `docs/reference/engine-bugs.md`, `docs/reference/engine-eval.md`, `docs/reference/engine-fit.md` |
| production / release | versioning, CI/CD, release hardening, release validation, platform, console, cross-platform support tiers, Steam, sector, marketing strategy, and marketing status | `docs/reference/ci-cd.md`, `docs/reference/release-hardening-guide.md`, `docs/reference/version-guide.md`, `docs/reference/platform-guide.md`, `docs/reference/console-guide.md`, `docs/reference/cross-platform-guide.md`, `docs/reference/steam-intel.md`, `docs/reference/sector-intel.md`, `docs/reference/marketing-guide.md`, `docs/reference/marketing-intel.md` |
| customability / scale | custom packs, custom architecture, extensions, libraries, assets, theory, benchmarks, quality, perf, and GPU | `docs/reference/custom-packs.md`, `docs/reference/custom-architecture.md`, `docs/reference/extensions-guide.md`, `docs/reference/library-guide.md`, `docs/reference/asset-guide.md`, `docs/reference/theory-guide.md`, `docs/reference/benchmark-guide.md`, `docs/reference/quality-guide.md`, `docs/reference/perf-guide.md`, `docs/reference/gpu-guide.md` |

## Root Files

- `README.md` — first-run and operator-facing repo overview
- `VERSION` — canonical working-tree version source
- `AGENTS.md` — root behavior and decision rules for Codex
- `Makefile` — convenience commands for setup, validation, routing, and Docker
- `CHANGELOG.md` — template-level change history
- `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md` — community and maintainer policy

## Codex Configuration

- `.codex/config.toml` — stable project defaults for model, sandbox, and multi-agent behavior
- `.codex/agents/` — project-scoped agent profiles with stable role ids and scientist public titles
- `.agents/skills/` — reusable skills that define structured workflows

These directories define durable behavior. They are not where live project state should go.

## Static Repo Docs

- `docs/setup/` — onboarding, installation, and troubleshooting
- `docs/setup/quick-access.md` — shortest path from clone to the first usable command surface
- `docs/setup/engine-installation.md` — engine install and local toolchain bootstrap path
- `docs/setup/agent-setup.md` — Codex CLI and agent operating-model bootstrap path
- `docs/reference/` — repo map and command reference
- `docs/research/` — source-backed notes that explain why key repo guardrails exist
- `docs/reference/quality-guide.md` — code quality and optimization criteria for refactors and review
- `docs/reference/theory-guide.md` — design-lens stacks, evidence-first framing, and theory validation paths
- `docs/reference/benchmark-guide.md` — benchmark families, baselines, thresholds, and repo-local measurement loops
- `docs/reference/engine-fit.md` — developer-profile and team-fit recommendations across the supported engines
- `docs/reference/engine-bugs.md` — recurring engine bug families, first checks, and debug surfaces
- `docs/reference/engine-eval.md` — engine-family build, test, performance, and toolchain scorecards
- `docs/reference/asset-guide.md` — asset ownership, import rules, and alternative stacks
- `docs/reference/sector-intel.md` — current industry, platform, and market signals
- `docs/reference/steam-intel.md` — Steam store, wishlist, forum, and hardware signals
- `docs/reference/platform-guide.md` — family-by-family platform compatibility matrices and readiness assumptions
- `docs/reference/console-guide.md` — PS5-like, Xbox-like, and Switch-like readiness, cert evidence, and submission assumptions
- `docs/reference/cross-platform-guide.md` — support tiers, release sequencing, and family order for cross-platform planning
- `docs/reference/release-hardening-guide.md` — code protection, symbol policy, trust boundary, and rollback planning for protected builds
- `docs/reference/marketing-guide.md` — campaign strategy, channel fit, and measurement criteria
- `docs/reference/marketing-intel.md` — current campaign status, chart packs, and metric movement snapshots
- `docs/examples/marketing-intel-example.md` — the concrete chart-pack example for current marketing status requests
- `docs/examples/release-hardening-example.md` — the concrete protected-build and multiplayer-trust example for release hardening requests
- `docs/research/game-development/production/release-hardening.md` — the source-backed release-hardening note behind protected build decisions
- `docs/reference/capabilities.md` — the master catalog for what this studio can do and where to start
- `docs/examples/capabilities-example.md` — the concrete intro example for the full capability surface
- `docs/reference/architecture-guide.md` — state ownership, events, projection boundaries, architecture diagrams, and other advanced patterns
- `docs/reference/custom-packs.md` — registry-oriented custom feature bundles, pack families, and fallback rules
- `docs/examples/custom-packs-example.md` — a concrete registry example for fixed rules, override rules, and fallback behavior
- `docs/research/game-development/foundations/custom-packs.md` — the source-backed note behind the custom pack registry lane
- `studio/docs/templates/custom-packs.md` — reusable template for pack identity, hook model, and validation
- `docs/reference/custom-architecture.md` — project-specific architecture contracts, fixed versus overrideable rules, and house-rule packs
- `docs/research/game-development/foundations/custom-architecture.md` — the source-backed research note behind custom request contracts and rule packs
- `docs/reference/extensions-guide.md` — opt-in extension packs, hook points, and manifest-driven add-ons
- `docs/reference/agent-system.md` — the umbrella operating model for single-specialist default, role matrix, hierarchy, and prompt journal choices
- `docs/reference/agent-transcript.md` — append-only task assignment and agent conversation transcript history
- `docs/reference/codex-compatibility.md` — Codex-native surfaces and the OpenAI/Codex compatibility contract
- `docs/reference/codex-model-guide.md` — repo-local model ladder and plan-tier decision matrix
- `docs/reference/mastermind-guide.md` — broad orchestration, delegation, validation, and simple user summaries
- `docs/reference/agent-portfolio.md` — role matrix for single-specialist, paired-specialist, and multi-agent panel work
- `docs/reference/agent-hierarchy.md` — command tree, scientist titles, async packets, and reporting lines
- `docs/research/game-development/production/platform-compatibility.md` — source-backed family-by-family platform compatibility planning
- `docs/research/game-development/production/console.md` — source-backed console premium and submission notes
- `docs/research/game-development/production/cross-platform.md` — source-backed support tiers and release sequencing
- `docs/reference/prompt-journal.md` — append-only prompt history and agent step notes for later review
- `docs/reference/agent-execution.md` — reusable execution packets that keep owner, mode, goal, proof path, and custom rules explicit before work starts
- `docs/examples/benchmark-example.md` — a concrete benchmark bundle for family choice, baseline, threshold, and artifact path work
- `docs/examples/asset-example.md` — a concrete asset review bundle for source, runtime, and import boundary work
- `docs/examples/sector-intel-example.md` — a concrete current-signals bundle for source hierarchy and implication work
- `docs/examples/steam-intel-example.md` — a concrete Steam-intel bundle for traffic, wishlist, forum, hardware, and chart-pack work
- `docs/examples/platform-example.md` — a concrete platform-compatibility bundle for family split, input, performance, policy, and matrix work
- `docs/examples/console-example.md` — a concrete console readiness bundle for family split, controller-first UX, and submission evidence
- `docs/examples/cross-platform-example.md` — a concrete support-tier bundle for family split, release order, and chart-pack work
- `docs/examples/marketing-example.md` — a concrete marketing-strategy bundle for objective, audience, channel fit, and measurement work
- `docs/examples/architecture-example.md` — a concrete architecture review bundle for state and projection work
- `docs/examples/custom-packs-example.md` — a concrete custom-packs bundle for registry rows, fixed rules, and fallback behavior
- `docs/examples/custom-architecture-example.md` — a concrete custom-architecture bundle for request contracts and rule packs
- `docs/examples/extensions-example.md` — a concrete extension-pack bundle for manifests, hook points, and fallback paths
- `docs/examples/engine-fit-example.md` — a concrete developer-fit matrix for beginner, C# team, and Blueprint/C++ team decisions
- `docs/examples/engine-eval-example.md` — a concrete engine-comparison scorecard bundle for build, tests, performance, and toolchain readiness
- `docs/examples/agent-system-example.md` — a concrete operating-model bundle for single-specialist default, role matrix, hierarchy, and review trail choices
- `docs/examples/mastermind-example.md` — a concrete orchestration bundle for broad user requests and specialist handoffs
- `docs/examples/agent-portfolio-example.md` — a concrete role-matrix bundle for choosing single versus multi-agent execution
- `docs/examples/agent-hierarchy-example.md` — a concrete hierarchy bundle for titles, reporting lines, and async packets
- `docs/examples/agent-execution-example.md` — a concrete execution-packet bundle for owner, mode, goal, proof path, and custom-rule choices
- `docs/examples/agent-validation-matrix-example.md` — a concrete proof bundle for operating-mode decisions, proof rows, and model overrides
- `docs/research/game-development/foundations/agent-validation-matrix.md` — the source-backed research note behind the proof rows, lane splits, and model-override choices
- `docs/examples/prompt-journal-example.md` — a concrete review bundle for prompt history and step-by-step agent notes
- `docs/examples/agent-transcript-example.md` — a concrete review bundle for task assignments and agent conversation transcripts
- `docs/examples/codex-model-guide-example.md` — a concrete model-selection bundle for model, plan, reasoning, and fallback choice
- `docs/examples/theory-example.md` — a concrete theory-stack bundle for player outcome, lens order, evidence, and validation path
- `docs/examples/engine-bugs-example.md` — a concrete bug atlas bundle for recurring engine bug families and first checks
- `docs/research/game-development/foundations/engine-bugs.md` — the source-backed note behind the bug atlas
- `studio/checklists/discipline/engine_bugs.toml` — the checklist lane for recurring engine bug triage
- `docs/research/openai-codex-infra-findings.md` — official OpenAI/Codex findings that shape the repo's agent and routing rules
- `docs/research/openai-codex-models.md` — official model and plan-fit findings that shape the repo's model-selection rules
- `docs/research/game-development/foundations/theory.md` — the source-backed theory note behind durable design-lens stacks
- `docs/research/game-development/foundations/engine-eval.md` — engine-family build, test, performance, and toolchain scorecards
- `docs/research/game-development/foundations/engine-fit.md` — developer-profile and team-fit recommendations across the supported engines
- `docs/research/game-development/production/steam-intel.md` — current Steam store, forum, hardware, and market signals
- `studio/checklists/discipline/openai_codex.toml` — controller-policy, prompt-version, tool-access, and eval-path checklist rules for OpenAI/Codex work
- `studio/checklists/discipline/openai_models.toml` — model-choice, plan-fit, and compatibility checklist rules for OpenAI/Codex work
- `studio/checklists/discipline/theory.toml` — theory-stack and design-lens checklist rules
- `studio/checklists/discipline/custom.toml` — shared custom architecture and request-rule contract checklist rules
- `studio/checklists/discipline/custom_packs.toml` — shared custom pack registry checklist rules
- `studio/checklists/custom/README.md` — project-specific custom override notes and late-merge house rules
- `studio/checklists/discipline/extensions.toml` — shared custom extension-pack checklist rules
- `studio/checklists/discipline/agent_execution.toml` — execution-packet checklist rules for owner, mode, proof path, custom rules, and stop conditions
- `studio/extensions/README.md` — opt-in extension pack layout and manifest guidance
- `studio/extensions/custom/README.md` — project-specific extension-pack notes and override manifests
- `studio/extensions/custom/eval-plan.md` — attach/detach smoke plan for a concrete extension pack
- `studio/docs/active/custom-packs-adr.md` — the accepted decision to keep custom packs as a dedicated registry layer
- `studio/docs/active/eval-custom-packs.md` — active eval plan for custom pack routing and registry validation
- `studio/checklists/discipline/engine_eval.toml` — engine-comparison, build/test/performance, and toolchain scorecard checklist rules
- `studio/checklists/discipline/steam_intel.toml` — Steam store, forum, wishlist, and hardware intelligence checklist rules
- `studio/checklists/discipline/platform_compatibility.toml` — family-by-family platform readiness checklist rules
- `studio/checklists/discipline/producer.toml`, `technical_director.toml`, `qa_lead.toml`, `release_manager.toml`, `build_release_engineer.toml`, `docs_researcher.toml`, `performance_analyst.toml`, `game_designer.toml`, `engine_programmer.toml`, `gameplay_programmer.toml`, `ui_programmer.toml`, `narrative_director.toml`, `art_director.toml`, and `audio_director.toml` — role-specific checklist packs for task-based hierarchy and narrow ownership
- `studio/docs/active/eval-openai-codex.md` — active eval plan for the OpenAI/Codex agent workflow contract
- `studio/docs/active/eval-openai-models.md` — active eval plan for model-choice and plan-fit guidance
- `studio/docs/active/eval-theory.md` — active eval plan for theory-stack routing and checklist generation
- `studio/docs/active/eval-custom-architecture.md` — active eval plan for custom architecture and request-rule routing
- `studio/docs/active/eval-extensions.md` — active eval plan for opt-in extension packs and plugin-like add-ons
- `studio/docs/active/agent-execution.md` — active append-only execution packet log
- `studio/docs/active/eval-agent-execution.md` — active eval plan for execution-packet routing and packet generation
- `studio/docs/templates/agent-execution.md` — reusable execution-packet template
- `studio/docs/active/eval-engine-bugs.md` — active eval plan for engine-bugs routing and troubleshooting guidance
- `studio/docs/active/engine-eval.md` — active engine comparison scorecard for current families and readiness assumptions
- `studio/docs/active/eval-engine-eval.md` — active eval plan for engine-evaluation routing and scorecard generation
- `studio/docs/active/engine-fit.md` — active engine-fit matrix for developer profile and team shape
- `studio/docs/active/eval-engine-fit.md` — active eval plan for engine-fit routing and matrix generation
- `studio/checklists/discipline/engine_fit.toml` — discipline checklist for engine-profile, workflow-fit, and tradeoff reporting
- `studio/docs/active/eval-steam-intel.md` — active eval plan for Steam-intel guidance
- `studio/docs/active/eval-platform-compatibility.md` — active eval plan for platform-family compatibility and readiness guidance

Use these when you want to explain how to operate the template itself.

## Multi-Engine Layer

- `studio/starter-kits/godot-4/` — Godot 4 starter kit, smoke flow, and reference runtime surface
- `studio/starter-kits/unity-6/` — Unity 6 starter kit, adapter, asmdef/package layout, and runtime sample surface
- `studio/starter-kits/unreal-5/` — Unreal 5 starter kit, adapter, module layout, and packaging sample surface
- `studio/checklists/engine/` — engine-specific checklist rules for Godot, Unity, and Unreal
- `studio/checklists/base/naming.toml` — short canonical naming rules for docs, examples, presets, and rename sync
- `docs/research/game-development/engines/` — engine-specific architecture, class/editor/object, 2D/3D class-mechanic, and performance notes

If you want proof that the repo is not Godot-only, inspect these first:

- `studio/starter-kits/unity-6/README.md`
- `studio/starter-kits/unreal-5/README.md`
- `docs/research/game-development/engines/unity-classes.md`
- `docs/research/game-development/engines/unreal-classes.md`

This repo is not Godot-only. The current `src/` runtime sample is Godot-based, but the operating system, adapters, starter kits, checklists, research, and CI contracts are shared across all supported engine families.

## GitHub Surfaces

- `.github/CODEOWNERS` — review ownership
- `.github/ISSUE_TEMPLATE/` — structured issue intake
- `.github/pull_request_template.md` — PR review and validation contract
- `.github/workflows/` — CI and Docker smoke checks
- `.github/dependabot.yml` — update automation for actions, Docker, and Python dependencies

## Eval And Hooks

- `evals/` — local regression fixtures for routing and genre guidance
- `evals/benchmark/` — repo-local benchmark cases for route, checklist, and docs regression
- `scripts/run_local_evals.py` — local eval runner
- `scripts/run_bench.py` — benchmark runner for local measurement bundles
- `.codex/hooks.json` — optional repo-local Codex hooks
- `scripts/hooks/` — hook handlers for session context and Bash guardrails
- `.env.example` — optional local environment variable template for integrations and helper tooling

## Live Project State

- `studio/docs/templates/` — reusable markdown templates
- `studio/docs/active/` — live state for the current project
- `studio/presets/` — engine/platform/genre guidance packs
- `studio/playbooks/` — multi-phase ways of operating common project types
- `studio/docs/active/platform-targets.md` — live platform-family targets and readiness assumptions

If a decision, risk, milestone, or feature is important to the current game, it should usually end up in `studio/docs/active/`.

## Runtime and Implementation Surfaces

- `src/` — runtime code or engine-facing source
- `tests/` — automated tests or durable manual test artifacts
- `assets/` — project assets
- `prototypes/` — throwaway or focused experiments
- `tools/` — internal helper tools

These folders begin intentionally light. The template expects the real engine/project layout to shape them over time. In the current repo, `src/` is the Godot reference implementation; Unity and Unreal runtime examples live under their starter-kit scaffolds until a concrete project chooses them as the primary engine.

## Helper Scripts

The `scripts/` folder is the operational command layer.

High-value scripts:

- `codex_studio.py`
- `setup_repo.py`
- `doctor.py`
- `run_local_evals.py`
- `seed_project_baseline.py`
- `bootstrap_studio.py`
- `project_radar.py`
- `route_task.py`
- `scaffold_feature.py`
- `scaffold_bugfix.py`
- `version_guard.py`
- `generate_qa_matrix.py`
- `scaffold_eval_plan.py`
- `journal.py`

`scaffold_feature.py` now generates the feature brief plus handoff, traceability, and optional validation docs in one atlas-aware bundle. `scaffold_bugfix.py` does the same for bug triage and optional validation docs, so treat both as the fastest path from idea to reviewable package. `journal.py` appends prompt history and agent step notes to the active review log, appends task assignments plus agent conversation transcripts to the active transcript log, and appends execution packets to the active work log, so use it when a task, handoff, or pre-flight contract should be reopened later without reading the whole chat. If the task is proving an agent operating-model choice, use the agent validation matrix guide and example alongside those bundles instead of trying to overload the transcript.

Prefer short canonical names for new docs and scripts. Current examples are `engine-map`, `engine-fit`, `engine-eval`, `system-atlas`, `genre-plan`, `genre-maturity`, `quality-guide`, `sector-intel`, `steam-intel`, `marketing-guide`, `lorebook`, and `world-graph` instead of longer legacy labels.

If you are changing a naming convention, update `studio/checklists/base/naming.toml` in the same change so the short-name rule and rename-sync rule stay live.

## Optional Helper Environment

- `Dockerfile`
- `docker-compose.yml`

These are optional. They give you an isolated Ubuntu + Python shell for working with the repo.
