# Examples

Use this folder when you want a high-signal example before writing your own doc.

The examples here are meant to be complete enough to copy the structure from, but specific enough that you should still replace the project names, dates, and validation steps with the real ones for your slice.

## Example families at a glance

| Family | Example files | What they prove |
| --- | --- | --- |
| engine and gameplay | `engine-fit-example.md`, `engine-eval-example.md`, `engine-bugs-example.md`, `perf-example.md`, `genre-perf-example.md`, `advanced-perf-example.md`, `benchmark-example.md`, `gpu-example.md`, `ui-example.md`, `audio-animation-example.md`, `asset-example.md`, `library-example.md`, `genre-gallery-example.md` | how to choose an engine, prove readiness, classify recurring engine bugs, and keep the core gameplay or presentation stack narrow |
| agent operating model | `agent-system-example.md`, `agent-speedpack-example.md`, `mastermind-example.md`, `agent-portfolio-example.md`, `agent-hierarchy-example.md`, `agent-validation-matrix-example.md`, `agent-execution-example.md`, `prompt-journal-example.md`, `agent-transcript-example.md` | how to keep single-specialist mode visible while still using controller, hierarchy, packets, speed packs, and review trails |
| repo capabilities | `capabilities-example.md` | how to present the studio's full capability surface without drowning the reader |
| production and market | `version-example.md`, `release-hardening-example.md`, `sector-intel-example.md`, `steam-intel-example.md`, `platform-example.md`, `console-example.md`, `cross-platform-example.md`, `marketing-example.md`, `marketing-intel-example.md` | how to keep release history, protected builds, market signals, platform fit, console readiness, cross-platform support tiers, launch strategy, and current-status charts reviewable |
| customability and theory | `custom-packs-example.md`, `custom-architecture-example.md`, `extensions-example.md`, `theory-example.md`, `architecture-example.md` | how to keep pack registries, house rules, optional capability surfaces, theory stacks, and state ownership explicit |

If you need the fastest safe bundle, compare `docs/reference/agent-speedpack.md`, `docs/examples/agent-speedpack-example.md`, `docs/research/game-development/foundations/agent-speedpack.md`, `studio/checklists/discipline/speedpack.toml`, and `studio/docs/active/eval-agent-speedpack.md` before building a broader orchestration packet.

Included now:

- `feature-example.md`
- `adr-example.md`
- `qa-example.md`
- `traceability-example.md`
- `test-example.md`
- `eval-example.md`
- `bug-example.md`
- `perf-example.md`
- `benchmark-example.md`
- `engine-fit-example.md`
- `engine-eval-example.md`
- `engine-bugs-example.md`
- `version-example.md`
- `release-hardening-example.md`
- `docs/examples/release-hardening-example.md`
- `gpu-example.md`
- `genre-perf-example.md`
- `advanced-perf-example.md`
- `quality-example.md`
- `quality-process-example.md`
- `audio-animation-example.md`
- `ui-example.md`
- `sector-intel-example.md`
- `steam-intel-example.md`
- `platform-example.md`
- `console-example.md`
- `cross-platform-example.md`
- `marketing-example.md`
- `marketing-intel-example.md`
- `library-example.md`
- `asset-example.md`
- `architecture-example.md`
- `custom-architecture-example.md`
- `extensions-example.md`
- `postmortem-example.md`
- `handoff-example.md`
- `mastermind-example.md`
- `agent-portfolio-example.md`
- `agent-hierarchy-example.md`
- `prompt-journal-example.md`
- `agent-transcript-example.md`
- `agent-execution-example.md`
- `codex-model-guide-example.md`
- `custom-packs-example.md`
- `theory-example.md`
- `capabilities-example.md`
- `agent-system-example.md`
- `agent-speedpack-example.md`
- `docs/reference/agent-speedpack.md`
- `docs/examples/agent-speedpack-example.md`
- `docs/research/game-development/foundations/agent-speedpack.md`
- `studio/checklists/discipline/speedpack.toml`
- `studio/docs/active/eval-agent-speedpack.md`
- `agent-validation-matrix-example.md`
- `genre-plan-example.md`
- `genre-example.md`
- `genre-gallery-example.md`
- `lorebook-example.md`
- `world-graph-example.md`

These are not meant to be copied blindly. They show the level of specificity the repo expects.

The legacy `golden-example` filenames have been retired; use the short canonical example names only.

If you are building a genre-driven feature, compare the example to:

- `docs/reference/genre-presets.md`
- `docs/research/game-development/genre/genre-guide.md`
- `docs/research/game-development/genre/genre-patterns.md`
- `docs/research/game-development/genre/genre-maturity.md`
- `genre-gallery-example.md` when you need more than one contrast set.

If you are building a lorebook or world bible, compare the example to:

- `docs/reference/lorebook-methodology.md`
- `docs/research/game-development/narrative/lorebook.md`

If you are building a world graph or history network, compare the example to:

- `docs/reference/world-graph-methodology.md`
- `docs/research/game-development/narrative/world-graph.md`

If you are building gameplay or system-heavy work, compare the example to:

- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/system-atlas.md`

If you are building audio or animation presentation work, compare `audio-animation-example.md` with `docs/reference/audio-animation-guide.md` and the matching engine presentation note before implementation. The example shows how to separate playback ownership, timing ownership, and gameplay truth before tuning the presentation layer.

If you are building a UI, HUD, menu, settings, or template-selection task, compare `ui-example.md` with `docs/reference/ui-guide.md` and the matching engine UI note before implementation. The example shows how to name the screen owner, projection boundary, input model, and template source before tuning the flow.

If you are designing state ownership, authority, event flow, or projection boundaries, compare `architecture-example.md` with `docs/reference/architecture-guide.md` (including its diagrams) and the matching architecture research notes before implementation.
If you are designing reusable custom feature bundles or a registry of project-specific packs, compare `custom-packs-example.md` with `docs/reference/custom-packs.md` and the matching custom-pack research note before implementation. The example shows how to keep the registry entry, fixed rules, overrideable rules, hook points, fallback, and validation path explicit.
If you are designing project-specific architecture, house rules, or request-rule packs, compare `custom-architecture-example.md` with `docs/reference/custom-architecture.md` and the matching architecture research notes before implementation. The example shows how to keep fixed rules separate from overrideable rules.
If you are designing opt-in custom capability surfaces, plugin-like add-ons, or hook packs, compare `extensions-example.md` with `docs/reference/extensions-guide.md`, `docs/reference/custom-architecture.md`, and the matching extension research notes before implementation. The example shows how to keep the manifest, hook points, and fallback path explicit.
Keep the full custom bundle nearby when you work on this lane:

- `docs/reference/custom-packs.md`
- `docs/examples/custom-packs-example.md`
- `docs/research/game-development/foundations/custom-packs.md`
- `studio/checklists/discipline/custom_packs.toml`
- `studio/docs/active/custom-packs-adr.md`
- `studio/docs/active/eval-custom-packs.md`
- `studio/docs/templates/custom-packs.md`
- `docs/reference/custom-architecture.md`
- `docs/examples/custom-architecture-example.md`
- `docs/research/game-development/foundations/custom-architecture.md`
- `studio/checklists/discipline/custom.toml`
- `studio/checklists/custom/README.md`
- `studio/docs/active/eval-custom-architecture.md`
If you are working on an extension pack, keep the full extension bundle nearby too:

- `docs/reference/extensions-guide.md`
- `docs/examples/extensions-example.md`
- `docs/research/game-development/foundations/extensions.md`
- `studio/checklists/discipline/extensions.toml`
- `studio/extensions/README.md`
- `studio/extensions/custom/README.md`
- `studio/extensions/custom/eval-plan.md`
- `studio/docs/active/eval-extensions.md`

If you are preparing a performance pass, compare `perf-example.md` with `docs/reference/perf-guide.md` and the matching engine performance note before making changes. The example shows the baseline, the likely bottleneck, the first lever, and the validation loop the agent should preserve.
If you are preparing a benchmark pass, compare `benchmark-example.md` with `docs/reference/benchmark-guide.md`, `docs/research/game-development/foundations/benchmarks.md`, and `docs/reference/eval-strategy.md` before making changes. The example shows how to name the family, baseline, metric, threshold, and report artifact before measuring.
If you are comparing engines for build, test, performance, or toolchain readiness, compare `engine-eval-example.md` with `docs/reference/engine-eval.md`, `docs/reference/engine-selection-guide.md`, and `docs/research/game-development/foundations/engine-eval.md` before making the call. The example shows how to keep build, tests, performance, and toolchain friction separate in one scorecard.
If you are comparing engines for developer profile or team-fit reasons, compare `docs/examples/engine-fit-example.md` with `docs/reference/engine-fit.md`, `docs/reference/engine-selection-guide.md`, and `docs/research/game-development/foundations/engine-fit.md` before making the call. The example shows how to keep beginner fit, C# fit, Blueprint fit, and C++ fit separate in one matrix.
If you are classifying recurring engine bug families or first checks, compare `docs/examples/engine-bugs-example.md` with `docs/reference/engine-bugs.md` and `docs/research/game-development/foundations/engine-bugs.md` before implementation. The example shows how to keep bug families, first checks, and debug surfaces separate before any patching starts.
The canonical path is `docs/examples/engine-bugs-example.md`, and it should stay synchronized with `docs/reference/engine-bugs.md` and `docs/research/game-development/foundations/engine-bugs.md`.
If you are turning that comparison into a routable agent task, keep `studio/checklists/discipline/engine_eval.toml` and `studio/docs/active/eval-engine-eval.md` next to the example so the checklist and eval plan stay aligned with the scorecard.
If you are turning that fit comparison into a routable agent task, keep `studio/checklists/discipline/engine_fit.toml`, `studio/docs/active/engine-fit.md`, and `studio/docs/active/eval-engine-fit.md` next to the example so the checklist and eval plan stay aligned with the matrix.
If you are preparing a versioning pass, compare `version-example.md` with `docs/reference/version-guide.md`, `docs/research/game-development/production/versioning.md`, and `CHANGELOG.md` before making changes. The example shows how to keep the working-tree version, changelog, commit notes, and release tag policy in the same contract.
If you are hardening a protected build or co-op release, compare `release-hardening-example.md` with `docs/reference/release-hardening-guide.md`, `docs/research/game-development/production/release-hardening.md`, and `studio/docs/templates/release-hardening.md` before making changes. The example shows how to keep build integrity, symbol policy, trust boundaries, and rollback evidence in the same contract.
If you are tracking current game-industry, platform, or policy signals, compare `sector-intel-example.md` with `docs/reference/sector-intel.md` and `docs/research/game-development/production/sector-intel.md` before making changes. The example shows how to separate official facts, signal windows, implications, and next actions.
If you are tracking Steam store, wishlist, forum, or hardware signals, compare `steam-intel-example.md` with `docs/reference/steam-intel.md` and `docs/research/game-development/production/steam-intel.md` before making changes. The example shows how to separate traffic, forum themes, hardware mix, market context, and a simple chart pack.
If you are planning platform compatibility across Windows, macOS, Linux, Steam Deck, PS5-like console premium, web, mobile, or TV families, compare `platform-example.md` with `docs/reference/platform-guide.md` and `docs/research/game-development/production/platform-compatibility.md` before making changes. The example shows how to separate families, inputs, performance envelopes, policy constraints, and a readiness matrix.
If you are planning console premium or PS5-like readiness, compare `docs/examples/console-example.md` with `docs/reference/console-guide.md` and `docs/research/game-development/production/console.md` before making changes. The example shows how to separate controller-first UX, suspend/resume, save / entitlement, and submission gates.
If you are deciding support tiers or release sequencing across those same families, compare `cross-platform-example.md` with `docs/reference/cross-platform-guide.md` and `docs/research/game-development/production/cross-platform.md` before making changes. The example shows how to separate core, supported, demo, research, and deferred families before the release order hardens.

The canonical path for this example is `docs/examples/cross-platform-example.md`, and it should stay synchronized with `docs/reference/cross-platform-guide.md` and `docs/research/game-development/production/cross-platform.md`.
If you are building a marketing strategy or campaign evaluation, compare `marketing-example.md` with `docs/reference/marketing-guide.md` and `docs/research/game-development/production/marketing.md` before making changes. The example shows how to separate objective, audience, channel fit, asset readiness, and measurement.
If you are building a current marketing status or chart-pack report, compare `marketing-intel-example.md` with `docs/reference/marketing-intel.md` and `docs/research/game-development/production/marketing-intel.md` before making changes. The example shows how to separate source window, baseline, metric movement, chart family, and one recommendation.
If you are preparing a GPU pass, compare `gpu-example.md` with `docs/reference/gpu-guide.md` and the matching engine GPU note before making changes. The example shows the CPU owner, GPU owner, upload path, readback policy, and first lever the agent should preserve.

If the performance pass is genre-shaped, compare `genre-perf-example.md` with `docs/reference/genre-perf-guide.md` before changing code. That example shows how to name the genre family, choose the first genre lever, and avoid the wrong early optimization.

If the performance pass is algorithm-heavy, compare `advanced-perf-example.md` with `docs/reference/advanced-perf-guide.md` before changing code. That example shows how to name the algorithm family, keep the algorithmic lever small, and avoid jumping to ECS, Mass, or another large-scale system too early.

If you are reviewing code quality or optimization criteria, compare `quality-example.md` and `quality-process-example.md` with `docs/reference/quality-guide.md`, `docs/reference/quality-process.md`, and `docs/reference/code-review.md` before changing code. Those examples show how to name the ownership model, baseline, validation path, first lever, control loop, and go/no-go gate before refactoring.

If you are building a theory stack or design-lens pack, compare `theory-example.md` with `docs/reference/theory-guide.md` and `docs/research/game-development/foundations/theory.md` before changing code or design. The example shows how to name the player outcome, choose the minimum lens stack, and keep the evidence and validation path explicit.

If you are choosing libraries, packages, plugins, or SDKs, compare `library-example.md` with `docs/reference/library-guide.md` before implementation. The example shows how to name the case, keep the stack small, and separate built-in APIs from official packages and plugins.

If you are choosing assets, import paths, or streaming boundaries, compare `asset-example.md` with `docs/reference/asset-guide.md` before implementation. The example shows how to name the source asset, runtime owner, shared data owner, and validation path.

If you are building a feature scaffold package, compare the example set to:

- `docs/examples/feature-example.md`
- `docs/examples/traceability-example.md`
- `docs/examples/handoff-example.md`
- `docs/examples/test-example.md`
- `docs/examples/eval-example.md`

Keep the execution packet bundle nearby when you work on this lane:

- `docs/reference/agent-execution.md`
- `docs/examples/agent-execution-example.md`
- `docs/research/game-development/foundations/agent-execution.md`
- `studio/checklists/discipline/agent_execution.toml`
- `studio/docs/active/agent-execution.md`
- `studio/docs/active/eval-agent-execution.md`
- `studio/docs/templates/agent-execution.md`

If you are coordinating a broad request, compare `mastermind-example.md` with `docs/reference/mastermind-guide.md` before splitting the work. The example shows the simple user summary, the control loop, the specialist handoffs, and the narrow validation path the controller should preserve.

If you are deciding whether to keep a request single-agent or fan out into a small panel, compare `agent-portfolio-example.md` with `docs/reference/agent-portfolio.md` before splitting the work. The example shows the role matrix, the operating mode decision, and the narrow validation path the controller should preserve.

If you are deciding titles, reporting lines, or async status packets for a panel, compare `agent-hierarchy-example.md` with `docs/reference/agent-hierarchy.md` before splitting the work. The example shows the command tree, the mode decision, and the narrow validation path the controller should preserve.

If you are recording prompt history or step-by-step agent notes for later review, compare `prompt-journal-example.md` with `docs/reference/prompt-journal.md` before writing a new trail. The example shows the append-only review file, the timestamped prompt entry, and the short agent evaluation note the repo expects.

If you are recording task assignments or inter-agent conversation turns for later review, compare `agent-transcript-example.md` with `docs/reference/agent-transcript.md` before writing a new transcript. The example shows the append-only assignment section, the conversation section, and the short reply note the repo expects.
If you need to explain the whole studio capability surface to a new contributor, compare `capabilities-example.md` with `docs/reference/capabilities.md` and `docs/research/game-development/foundations/capabilities.md` before writing the summary.

If you need the shortest safe bundle for an urgent or narrow task, compare `agent-speedpack-example.md` with `docs/reference/agent-speedpack.md` and `docs/setup/quick-access.md` before building a broader orchestration packet.

If you are building a work packet or execution contract, compare `agent-execution-example.md` with `docs/reference/agent-execution.md` and `docs/research/game-development/foundations/agent-execution.md` before implementation. The example shows owner, mode, goal, inputs, outputs, proof path, custom rules, and stop conditions.

If you are planning the repo's overall multi-agent operating model, compare `agent-system-example.md` with `docs/reference/agent-system.md`, `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, and `docs/reference/agent-hierarchy.md` before splitting the work. The example shows how to keep the single specialist default visible while still making the controller title, role matrix, hierarchy, and review trail explicit.
If you need to prove that single specialist, pair, or panel was the right operating choice, compare `agent-validation-matrix-example.md` with `docs/reference/agent-validation-matrix.md`, `docs/reference/agent-system.md`, and the matching research note before splitting the work. The example shows how to keep the proof rows separate from prompt history and transcript history.

Keep the full theory bundle nearby when you work on this lane:

- `docs/reference/theory-guide.md`
- `docs/examples/theory-example.md`
- `docs/research/game-development/foundations/theory.md`
- `studio/checklists/discipline/theory.toml`
- `studio/docs/active/eval-theory.md`

If you are shaping OpenAI/Codex agent-platform wiring, compare `agent-system-example.md` with `docs/research/openai-codex-infra-findings.md`, `docs/research/openai-codex-models.md`, `docs/reference/codex-compatibility.md`, and `docs/reference/codex-model-guide.md` before splitting the work. The example shows how to keep the single specialist default visible while still making the controller policy, prompt shape, eval path, model choice, and safety assumptions explicit.
If you are choosing a model or plan tier, compare `codex-model-guide-example.md` with `docs/reference/codex-model-guide.md` and `docs/research/openai-codex-models.md` before work. The example shows how to separate surface, selected model, plan tier, reasoning level, and fallback.
If you want the full control bundle, pair that with `studio/checklists/discipline/openai_codex.toml`, `studio/checklists/discipline/openai_models.toml`, `studio/docs/active/eval-openai-codex.md`, and `studio/docs/active/eval-openai-models.md` so the workflow stays versioned, testable, and easy to hand off.

If you are turning a genre preset into a buildable plan, compare `genre-plan-example.md` with `docs/reference/genre-plan.md` before writing a new plan. The example shows the player outcome, contrast set, loop ladder, state owner, accessibility envelope, and validation ladder the repo expects.

If you are adding new planning templates, keep this folder in sync so every new template has at least one concrete, high-signal example beside it.

The feature scaffold now threads the system atlas, engine class atlas, and engine quick map into generated feature, handoff, traceability, and eval-plan docs, so examples here should stay aligned with that atlas-first output.

The bugfix scaffold and eval-plan scaffold now use the same atlas references, so bug reports, crash triage, test plans, and eval plans should stay aligned with the system atlas too.
If you are preparing a bugfix slice, the scaffold can now optionally create test plan and eval plan stubs alongside the bug and crash docs, so keep the examples in this folder aligned with that broader bugfix package.

The feature scaffold now has the same validation-doc rhythm, so feature examples should show the brief, handoff, traceability, and optional test/eval docs as one package instead of isolated files. When you update a feature example, make sure the example shows the review bundle a real agent would receive: brief, handoff, traceability, test plan, and eval plan together.
