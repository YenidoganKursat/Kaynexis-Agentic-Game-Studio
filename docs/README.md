# Repo Documentation

This folder contains durable documentation about operating the Codex-first studio operating system itself.

Use `docs/` for:

- installation guidance
- onboarding and first-run instructions
- command references
- repo structure explanations
- code review and eval operating policy
- research notes that justify durable repo and engine conventions
- maintainer-facing GitHub and contribution setup
- troubleshooting for the template and helper scripts
- operator-facing workflow recipes and task examples

Do not use `docs/` for live game project state.
That belongs in `studio/docs/active/`.

## Structure map

These are the durable doc families the repo now uses most often:

| Family | What it covers | Best starting docs |
| --- | --- | --- |
| compact front door | one short overview page that points to the right lane | `reference/studio-map.md` |
| fast path | the shortest safe bundle for urgent or narrow work | `reference/agent-speedpack.md`, `examples/agent-speedpack-example.md`, `research/game-development/foundations/agent-speedpack.md` |
| operator flow | setup, quick access, first-hour bootstrap, maintainer setup | `setup/quick-access.md`, `setup/getting-started.md`, `setup/first-hour-walkthrough.md`, `setup/engine-installation.md`, `setup/agent-setup.md` |
| capability catalog | the master tour of what this studio can do, which lane to use, and where to start | `reference/capabilities.md`, `examples/capabilities-example.md`, `research/game-development/foundations/capabilities.md` |
| engine and gameplay | engine choice, engine atlas, systems atlas, examples, perf, GPU, audio, UI | `reference/engine-selection-guide.md`, `reference/engine-map.md`, `reference/engine-atlas.md`, `reference/system-atlas.md`, `reference/engine-examples.md` |
| engine troubleshooting | recurring engine bug families, first checks, and debug surfaces | `reference/engine-bugs.md`, `examples/engine-bugs-example.md`, `research/game-development/foundations/engine-bugs.md` |
| agent operating model | controller, portfolio, hierarchy, execution packets, prompt journal, transcript, validation matrices | `reference/agent-system.md`, `reference/mastermind-guide.md`, `reference/agent-portfolio.md`, `reference/agent-hierarchy.md`, `reference/agent-execution.md`, `reference/prompt-journal.md`, `reference/agent-transcript.md`, `reference/agent-validation-matrix.md` |
| production and market | CI/CD, release hardening, versioning, platform, console, cross-platform support tiers, sector intel, Steam intel, marketing strategy, marketing status, and release validation | `reference/ci-cd.md`, `reference/release-hardening-guide.md`, `reference/version-guide.md`, `reference/platform-guide.md`, `reference/console-guide.md`, `reference/cross-platform-guide.md`, `examples/console-example.md`, `examples/cross-platform-example.md`, `research/game-development/production/console.md`, `research/game-development/production/cross-platform.md`, `reference/sector-intel.md`, `reference/steam-intel.md`, `reference/marketing-guide.md`, `reference/marketing-intel.md` |
| customability and scale | custom packs, custom architecture, extension packs, libraries, assets, theory, benchmarks, quality, perf, GPU | `reference/custom-packs.md`, `reference/custom-architecture.md`, `reference/extensions-guide.md`, `reference/library-guide.md`, `reference/asset-guide.md`, `reference/theory-guide.md`, `reference/benchmark-guide.md`, `reference/quality-guide.md`, `reference/perf-guide.md`, `reference/gpu-guide.md` |

If you want the fastest safe start, keep the full speed-pack bundle nearby:

- `reference/agent-speedpack.md`
- `examples/agent-speedpack-example.md`
- `research/game-development/foundations/agent-speedpack.md`
- `studio/checklists/discipline/speedpack.toml`
- `studio/docs/active/eval-agent-speedpack.md`

## Read this in order

If you are new to the repo, the shortest sensible path is:

1. `setup/quick-access.md`
2. `reference/studio-map.md`
3. `reference/repo-tour.md`
4. `reference/capabilities.md`
5. `reference/engine-selection-guide.md`
6. `reference/agent-system.md`
7. `reference/agent-speedpack.md`
8. `reference/engine-eval.md`
9. `reference/marketing-guide.md`

That sequence gives you the operator flow first, then the engine/genre decision model, then the concrete examples.

## Start Here

- `setup/quick-access.md`
- `reference/studio-map.md`
- `setup/getting-started.md`
- `setup/first-hour-walkthrough.md`
- `setup/engine-installation.md`
- `setup/agent-setup.md`
- `setup/installer-checklist.md`
- `setup/troubleshooting.md`
- `setup/github-setup.md`
- `setup/optional-codex-hooks.md`
- `setup/secrets-and-env.md`
- `reference/repo-tour.md`
- `reference/capabilities.md`
- `reference/command-cheatsheet.md`
- `reference/engine-selection-guide.md`
- `reference/engine-fit.md`
- `reference/engine-bugs.md`
- `reference/engine-eval.md`
- `reference/engine-examples.md`
- `reference/engine-map.md`
- `reference/engine-atlas.md`
- `reference/perf-guide.md`
- `reference/benchmark-guide.md`
- `reference/engine-eval.md`
- `reference/genre-perf-guide.md`
- `reference/advanced-perf-guide.md`
- `reference/version-guide.md`
- `reference/sector-intel.md`
- `reference/steam-intel.md`
- `reference/platform-guide.md`
- `reference/console-guide.md`
- `reference/cross-platform-guide.md`
- `examples/console-example.md`
- `reference/marketing-guide.md`
- `reference/gpu-guide.md`
- `reference/audio-animation-guide.md`
- `reference/quality-guide.md`
- `reference/quality-process.md`
- `reference/theory-guide.md`
- `reference/architecture-guide.md`
- `reference/custom-packs.md`
- `examples/custom-packs-example.md`
- `research/game-development/foundations/custom-packs.md`
- `reference/custom-architecture.md`
- `reference/extensions-guide.md`
- `reference/library-guide.md`
- `reference/asset-guide.md`
- `reference/agent-system.md`
- `reference/agent-speedpack.md`
- `reference/agent-validation-matrix.md`
- `reference/agent-execution.md`
- `reference/codex-compatibility.md`
- `examples/codex-model-guide-example.md`
- `examples/agent-validation-matrix-example.md`
- `examples/agent-execution-example.md`
- `reference/godot-atlas.md`
- `reference/unity-atlas.md`
- `reference/unreal-atlas.md`
- `reference/system-atlas.md`
- `examples/agent-system-example.md`
- `reference/workflow-recipes.md`
- `reference/task-prompt-examples.md`
- `reference/lorebook-methodology.md`
- `reference/world-graph-methodology.md`
- `reference/code-review.md`
- `reference/eval-strategy.md`
- `reference/genre-presets.md`
- `reference/genre-plan.md`
- `reference/codex-compatibility.md`
- `reference/agent-guide.md`
- `reference/sector-intel.md`
- `reference/steam-intel.md`
- `reference/platform-guide.md`
- `reference/cross-platform-guide.md`
- `reference/mastermind-guide.md`
- `reference/agent-portfolio.md`
- `reference/agent-hierarchy.md`
- `reference/agent-execution.md`
- `reference/prompt-journal.md`
- `reference/agent-transcript.md`
- `examples/agent-execution-example.md`
- `reference/handoff-contracts.md`
- `reference/feature-traceability.md`
- `reference/doc-sync-audit.md`
- `reference/balance-simulator.md`
- `examples/README.md`
- `research/openai-codex-infra-findings.md`
- `research/game-development/README.md`
- `research/game-development/production/README.md`
- `research/game-development/production/sector-intel.md`
- `research/game-development/production/steam-intel.md`
- `research/game-development/foundations/README.md`
- `research/game-development/engines/README.md`
- `research/game-development/genre/README.md`
- `research/game-development/genre/genre-plan.md`
- `research/game-development/genre/genre-guide.md`
- `research/game-development/genre/genre-maturity.md`
- `research/game-development/assets/README.md`

## Fast paths by task type

Use these when you already know the work category and want the fastest path to the right reference.

- gameplay slice: `research/game-development/systems/` plus `reference/engine-examples.md`
- UI or HUD flow: `research/game-development/systems/ui.md`
- inventory or item systems: `research/game-development/systems/inventory.md`
- save or progression systems: `research/game-development/systems/save.md`
- audio, animation, or presentation timing: `reference/audio-animation-guide.md` and `examples/audio-animation-example.md`
- code quality or optimization criteria: `reference/quality-guide.md`, `reference/quality-process.md`, `reference/code-review.md`, `examples/quality-example.md`, `examples/quality-process-example.md`, and the matching engine or perf notes
- theory stack or design lenses: `reference/theory-guide.md`, `examples/theory-example.md`, and `research/game-development/foundations/theory.md`
- full theory bundle nearby: `studio/checklists/discipline/theory.toml` and `studio/docs/active/eval-theory.md`
- state, authority, event, or projection architecture: `reference/architecture-guide.md` (diagrams), `examples/architecture-example.md`, and the matching architecture research notes
- custom packs or project-specific feature registries: `reference/custom-packs.md`, `examples/custom-packs-example.md`, and the matching custom-pack research notes
- custom architecture or request-rule packs: `reference/custom-architecture.md`, `examples/custom-architecture-example.md`, and the matching architecture research notes
- custom extension packs or plugin-like add-ons: `reference/extensions-guide.md`, `examples/extensions-example.md`, and the matching extension research notes
- library or package selection: `reference/library-guide.md` and `examples/library-example.md`
- engine comparison or scorecard: `reference/engine-eval.md`, `examples/engine-eval-example.md`, and `research/game-development/foundations/engine-eval.md`
- developer profile fit or team-style fit: `reference/engine-fit.md`, `examples/engine-fit-example.md`, and `research/game-development/foundations/engine-fit.md`
- asset or content pipeline: `reference/asset-guide.md`, `examples/asset-example.md`, and `research/game-development/assets/`
- current sector or market signals: `reference/sector-intel.md` and `examples/sector-intel-example.md`
- Steam store, wishlist, forum, or hardware signals: `reference/steam-intel.md`, `examples/steam-intel-example.md`, and `research/game-development/production/steam-intel.md`
- platform compatibility across Windows, macOS, Linux, Steam Deck, web, mobile, and TV families: `reference/platform-guide.md`, `examples/platform-example.md`, and `research/game-development/production/platform-compatibility.md`
- console premium and PS5-like readiness: `reference/console-guide.md`, `examples/console-example.md`, and `research/game-development/production/console.md`
- cross-platform support tiers and release sequencing: `reference/cross-platform-guide.md`, `examples/cross-platform-example.md`, and `research/game-development/production/cross-platform.md`
- marketing strategy or channel selection: `reference/marketing-guide.md`, `examples/marketing-example.md`, and `research/game-development/production/marketing.md`
- marketing status, chart packs, or current campaign snapshots: `reference/marketing-intel.md`, `examples/marketing-intel-example.md`, and `research/game-development/production/marketing-intel.md`
- broad orchestration or delegation: `reference/mastermind-guide.md`, `reference/agent-portfolio.md`, and `examples/mastermind-example.md`
- fastest safe start or urgent narrow work: `reference/agent-speedpack.md`, `examples/agent-speedpack-example.md`, and `research/game-development/foundations/agent-speedpack.md`
- agent system or operating model: `reference/agent-system.md`, `examples/agent-system-example.md`, `reference/mastermind-guide.md`, `reference/agent-portfolio.md`, and `reference/agent-hierarchy.md`
- agent validation matrix or operating-model proof: `reference/agent-validation-matrix.md`, `examples/agent-validation-matrix-example.md`, and `research/game-development/foundations/agent-validation-matrix.md`
- agent execution packet or reusable work packet: `reference/agent-execution.md`, `examples/agent-execution-example.md`, and `research/game-development/foundations/agent-execution.md`
- model choice or plan tier: `reference/codex-model-guide.md`, `examples/codex-model-guide-example.md`, and `research/openai-codex-models.md`
- OpenAI / Codex / agent platform: `research/openai-codex-infra-findings.md`, `research/openai-codex-models.md`, `reference/codex-compatibility.md`, `reference/codex-model-guide.md`, `reference/agent-system.md`, `examples/agent-system-example.md`, `studio/checklists/discipline/openai_codex.toml`, `studio/checklists/discipline/openai_models.toml`, `studio/docs/active/eval-openai-codex.md`, and `studio/docs/active/eval-openai-models.md`
- agent role matrix or multi-agent panel choice: `reference/agent-portfolio.md` and `examples/agent-portfolio-example.md`
- agent hierarchy, titles, async panels, or role-specific checklist packs: `reference/agent-hierarchy.md`, `examples/agent-hierarchy-example.md`, and `studio/checklists/discipline/`
- prompt history, agent step review trail, or agent conversation transcript: `reference/prompt-journal.md`, `reference/agent-transcript.md`, `examples/prompt-journal-example.md`, and `examples/agent-transcript-example.md`
- fast cross-system ownership: `reference/system-atlas.md`
- performance pass: `reference/perf-guide.md`, `reference/genre-perf-guide.md`, `examples/perf-example.md`, `examples/genre-perf-example.md`, and the matching engine performance note
- benchmark or measurement pass: `reference/benchmark-guide.md`, `examples/benchmark-example.md`, and `research/game-development/foundations/benchmarks.md`
- GPU / render communication: `reference/gpu-guide.md`, `examples/gpu-example.md`, and the matching engine GPU note
- advanced optimization algorithms: `reference/advanced-perf-guide.md` and `examples/advanced-perf-example.md`
- narrative canon or world graph: `reference/lorebook-methodology.md` and `reference/world-graph-methodology.md`
- genre selection or genre maturity: `reference/genre-presets.md`, `reference/genre-plan.md`, `genre-guide.md`, `genre-patterns.md`, and `genre-maturity.md`
- build or release pipeline: `reference/ci-cd.md` and `research/game-development/production/release-validation.md`
- protected builds or multiplayer trust: `reference/release-hardening-guide.md`, `examples/release-hardening-example.md`, and `research/game-development/production/release-hardening.md`
- versioning or release metadata: `reference/version-guide.md`, `examples/version-example.md`, and `research/game-development/production/versioning.md`, with commit notes kept in the same contract

## Responsibility Split

- `docs/` — static repo/operator documentation
- `docs/research/` — source-backed notes behind repo policy and engine/production decisions
- `studio/docs/templates/` — reusable project document templates
- `studio/docs/active/` — live project truth for the current game

## Engine Research Highlights

If you are doing engine-specific work, start here:

- `docs/research/game-development/engines/README.md`
- `docs/reference/engine-examples.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/audio-animation-guide.md`
- `docs/reference/godot-atlas.md`
- `docs/reference/unity-atlas.md`
- `docs/reference/unreal-atlas.md`
- `docs/reference/system-atlas.md`
- `docs/reference/quality-guide.md`
- `docs/reference/architecture-guide.md`
- `docs/reference/genre-perf-guide.md`
- `docs/reference/advanced-perf-guide.md`
- `docs/reference/library-guide.md`
- `docs/research/game-development/genre/README.md`
- `docs/research/game-development/genre/genre-guide.md`
- `docs/research/game-development/genre/genre-patterns.md`
- `docs/research/game-development/genre/genre-maturity.md`
- `docs/research/game-development/engines/godot-classes.md`
- `docs/research/game-development/engines/unity-classes.md`
- `docs/research/game-development/engines/unreal-classes.md`

Those guides exist so the repo does not silently collapse back into a Godot-only mental model. They explain the most-used classes, objects, mechanic ownership patterns, writing style expectations, and common mistakes for each engine family.

## Example-first reading

If you prefer concrete examples before theory, start with `reference/engine-examples.md` and `examples/README.md`, then jump back into the matching research note.

## Academic Foundations Highlights

If a design discussion is getting fuzzy or purely opinion-based, start here:

- `research/game-development/foundations/frameworks.md`
- `research/game-development/foundations/ux.md`
- `research/game-development/foundations/ai.md`
- `research/game-development/foundations/balance.md`
- `research/game-development/architecture/README.md`
- `research/game-development/architecture/authority.md`
- `research/game-development/architecture/events.md`
- `research/game-development/architecture/state.md`
- `research/game-development/architecture/projection.md`

Those notes exist so the repo can reason from canonical theory and standards, not just implementation habits.

## Systems Research Highlights

If the task is about inventory, character state, enemy architecture, or save/combat boundaries, start here:

- `research/game-development/systems/inventory.md`
- `research/game-development/systems/character.md`
- `research/game-development/systems/enemy.md`
- `research/game-development/systems/crafting.md`
- `research/game-development/systems/dialogue.md`
- `research/game-development/systems/party.md`
- `research/game-development/systems/input.md`
- `research/game-development/systems/ui.md`
- `research/game-development/systems/skills.md`
- `research/game-development/systems/interactions.md`
- `research/game-development/systems/combat.md`
- `research/game-development/systems/save.md`

Those notes exist so the repo does not reduce system-heavy work to "just add another script." They define ownership, persistence, authored-data boundaries, encounter roles, and the main scaling risks.

## Narrative Research Highlights

If the task is about story canon, lorebook structure, world graphs, or narrative state, start here:

- `reference/lorebook-methodology.md`
- `reference/world-graph-methodology.md`
- `research/game-development/narrative/README.md`
- `research/game-development/narrative/lorebook.md`
- `research/game-development/narrative/world-graph.md`
- `research/game-development/systems/dialogue.md`

Those notes exist so story facts, unlocks, and dialogue references stay separate instead of drifting into one large script layer.

## What good looks like

Every durable doc should answer at least three of these questions:

- what is the owner
- what is the first validation path
- what changes when scale increases
- what does not belong in this system
- what another contributor should read next

## Genre Research Highlights

If the team is still deciding what kind of game it is making, or if a feature depends on genre-specific constraints, start here:

- `research/game-development/genre/genre-guide.md`
- `research/game-development/genre/genre-maturity.md`
- `research/game-development/genre/genre-patterns.md`
- `research/game-development/genre/genre-examples.md`
- `examples/genre-gallery-example.md` when the team needs more than one contrast set
- `research/game-development/genre/auto-battler.md`
- `research/game-development/genre/deckbuilder.md`
- `research/game-development/genre/survivorlike.md`
- `research/game-development/genre/co-op-survival.md`
- `research/game-development/genre/cozy-sim.md`
- `research/game-development/genre/extraction-lite.md`
- `research/game-development/genre/narrative-adventure.md`
- `research/game-development/genre/platformer.md`
- `research/game-development/genre/puzzle.md`
- `research/game-development/genre/tactical-rpg.md`
- `research/game-development/genre/colony-sim.md`
- `research/game-development/genre/grand-strategy.md`
- `research/game-development/genre/stealth.md`
- `research/game-development/genre/factory.md`
- `research/game-development/genre/metroidvania.md`
- `research/game-development/genre/city-builder.md`
- `research/game-development/genre/life-sim.md`
- `research/game-development/genre/hero-shooter.md`
- `research/game-development/genre/soulslike.md`

Those notes exist so the repo does not flatten every project into the same first-slice advice. They explain dominant loops, first systems that usually break, and what to study from official game pages before scoping work.

### Genre families now covered

- `action-roguelite` for readable combat runs and build variety
- `deckbuilder-roguelike` for sequencing, reward health, and route tension
- `co-op-survival` for shared scarcity and session authority
- `auto-battler` for drafting economy, board placement, and round resolution
- `cozy-sim` for routines, attachment, and low-friction progression
- `extraction-lite` for risk economy and extraction clarity
- `grand-strategy` for long-horizon diplomacy and campaign state
- `survivorlike` for density readability and short-run escalation
- `narrative-adventure` for authored state and choice visibility
- `platformer` for movement feel and camera support
- `puzzle` for teach/test/twist sequencing
- `stealth` for patrol readability and detection fairness
- `colony-sim` for agent priorities and crisis recovery
- `city-builder` for zoning, transport, and simulation legibility
- `factory-automation` for throughput, logistics, and scale tooling
- `life-sim` for routine, identity, and relationship state
- `hero-shooter` for role kits and objective readability
- `metroidvania` for traversal gates and return loops
- `soulslike` for telegraph reading and recovery mastery
- `tactical-rpg` for forecastable combat and build depth

## Execution Glue Highlights

If the repo is drifting between planning, implementation, QA, and release, start here:

- `reference/handoff-contracts.md`
- `reference/feature-traceability.md`
- `reference/doc-sync-audit.md`
- `reference/balance-simulator.md`
- `examples/README.md`

Those docs and tools exist to keep repo truth connected from feature brief to release impact instead of letting important context dissolve into chat.
