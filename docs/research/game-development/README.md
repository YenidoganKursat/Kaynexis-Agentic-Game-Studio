# Game Development Research

This knowledge base is the durable research layer for the Codex-first studio system.

Use it when:

- choosing or revising engine architecture
- shaping custom packs, custom feature registries, custom architecture contracts, request-rule packs, or house-rule overrides
- shaping custom extension packs or plugin-like add-ons
- shaping durable execution packets or pre-flight contracts for routed work
- comparing engine build, test, performance, and toolchain readiness
- diagnosing recurring engine bugs, common errors, and engine-specific troubleshooting paths
- shaping build and release flows
- protected builds, code protection, symbol policy, and multiplayer trust
- protecting release builds with code protection, symbol policy, and multiplayer trust
- deciding on content pipeline rules
- introducing system-heavy gameplay or production workflows
- building or refreshing a theory stack, design-lens pack, or player-outcome framing
- tracking current game-industry, platform, and market signals
- tracking Steam-specific store, wishlist, forum, and hardware signals
- planning marketing strategy, channel mix, and measurement loops
- tracking current marketing status, chart packs, and campaign health
- planning platform compatibility across Windows, macOS, Linux/Steam Deck, web, mobile, and TV families
- planning cross-platform support tiers and release sequencing across Windows, macOS, Linux/Steam Deck, web, mobile, and TV families
- planning console premium, PS5-like, or other submission-heavy platform work
- explaining the repo's full capability surface to a newcomer
- choosing the smallest official library, package, plugin, or SDK set for a concrete case
- shaping OpenAI/Codex agent-platform wiring or prompt-routing policy
- choosing a Codex model family, plan tier, or reasoning profile
- using `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md` when the controller workflow itself needs a checklist and eval trail
- using `studio/checklists/discipline/openai_models.toml` and `studio/docs/active/eval-openai-models.md` when model fit itself needs a checklist and eval trail

Structure map:

| Structure | When to reach for it | Start here |
| --- | --- | --- |
| fast path | the shortest safe bundle for urgent or narrow work | `docs/reference/agent-speedpack.md`, `docs/examples/agent-speedpack-example.md`, `foundations/agent-speedpack.md` |
| operating model | single-specialist default, controller, hierarchy, review trail, and multi-agent proof choices | `foundations/agent-system.md`, `foundations/mastermind.md`, `foundations/agent-portfolio.md`, `foundations/agent-hierarchy.md`, `foundations/agent-validation-matrix.md`, `foundations/prompt-journal.md`, `foundations/agent-transcript.md` |
| work packets | reusable pre-flight contracts and owner/mode/proof-path bundles | `foundations/agent-execution.md`, `docs/reference/agent-execution.md`, `docs/examples/agent-execution-example.md` |
| capability catalog | repo-wide capability families, intro shapes, and the shortest starting docs | `docs/reference/capabilities.md`, `docs/examples/capabilities-example.md`, `foundations/capabilities.md` |
| engine and gameplay ownership | engine choice, class ownership, mechanic mapping, engine eval, fit, and cross-engine system ownership | `engines/README.md`, `reference/engine-map.md`, `reference/engine-atlas.md`, `reference/system-atlas.md`, `foundations/engine-eval.md`, `foundations/engine-fit.md` |
| engine troubleshooting | recurring engine bug families, first checks, and debug surfaces | `reference/engine-bugs.md`, `examples/engine-bugs-example.md`, `foundations/engine-bugs.md` |
| production and market signals | release hardening, release, versioning, platform, market, Steam, marketing strategy, and marketing status decisions | `production/README.md`, `production/release-hardening.md`, `production/versioning.md`, `production/platform-compatibility.md`, `production/sector-intel.md`, `production/steam-intel.md`, `production/marketing.md`, `production/marketing-intel.md` |
| cross-platform support strategy | support tiers, family sequencing, and release-order decisions | `production/cross-platform.md`, `reference/cross-platform-guide.md`, `examples/cross-platform-example.md` |
| console readiness | PS5-like, Xbox-like, and Switch-like submission gates, controller-first UX, and cert evidence | `production/console.md`, `reference/console-guide.md`, `examples/console-example.md` |
| customability and scale | custom packs, custom architecture, extensions, libraries, assets, theory, benchmarks, quality, perf, and GPU | `foundations/custom-packs.md`, `foundations/custom-architecture.md`, `foundations/extensions.md`, `reference/library-guide.md`, `reference/asset-guide.md`, `foundations/theory.md`, `foundations/benchmarks.md`, `foundations/quality.md`, `foundations/perf-algorithms.md`, `foundations/gpu.md` |

Research rules:

- prefer official or primary sources first
- date every note
- finish each note with a repo-impact statement
- link the note from the task, checklist, or active doc that depends on it

Structure:

- `foundations/` for canonical theory, standards, and academic research that should shape design and architectural reasoning across engines and genres
- `foundations/perf-algorithms.md` for spatial partitioning, culling, batching, job systems, and state-compression decisions
- `foundations/gpu.md` for GPU ownership, CPU-GPU communication, buffer contracts, and render-scale choices
- `foundations/quality.md` for code quality, maintainability, and optimization criteria decisions
- `foundations/benchmarks.md` for ready-made benchmark families, repo-local benchmark rules, and artifact-based measurement loops
- `foundations/theory.md` for durable design-lens stacks such as MDA, GameFlow, SDT, affordance, and cognitive load
- `foundations/engine-eval.md` for engine-family build, test, performance, and toolchain scorecards
- `foundations/custom-packs.md` for reusable custom feature bundles, pack registries, fixed versus overrideable rules, and hook/fallback decisions
- `foundations/custom-architecture.md` for project-specific architecture contracts, fixed versus overrideable rules, and request-rule packs
- `docs/research/game-development/foundations/custom-packs.md` for the same custom-pack registry when you need the full canonical path in an index or checklist
- `docs/research/game-development/foundations/custom-architecture.md` for the same custom-architecture contract when you need the full canonical path in an index or checklist
- `foundations/extensions.md` for opt-in extension packs, hook points, and manifest-driven add-ons
- `foundations/agent-execution.md` for execution packets, owner/mode contracts, proof paths, and custom rules before implementation starts
- `foundations/agent-speedpack.md` for the shortest safe starting bundle when the task should stay fast
- `research/game-development/foundations/engine-fit.md` for developer-profile and team-fit recommendations across the supported engine families
- `docs/examples/engine-fit-example.md`, `studio/checklists/discipline/engine_fit.toml`, `studio/docs/active/engine-fit.md`, and `studio/docs/active/eval-engine-fit.md` for the routable fit package
- `foundations/mastermind.md` for broad orchestration, delegation, and simple user-summary control loops
- `foundations/agent-portfolio.md` for single-specialist, paired-specialist, and multi-agent panel role mapping
- `foundations/agent-hierarchy.md` for command trees, reporting lines, and async status packets
- `foundations/agent-validation-matrix.md` for proof rows that justify single-specialist, paired-specialist, or panel choices
- `foundations/prompt-journal.md` for append-only prompt history and step-by-step agent notes
- `foundations/agent-transcript.md` for append-only task assignments and agent conversation turns
- `foundations/agent-system.md` for the umbrella operating model that keeps single-specialist mode visible while it coordinates controller, role matrix, hierarchy, and review trail choices
- `research/openai-codex-infra-findings.md` for the official OpenAI/Codex findings that shaped the repo's prompt-routing and eval rules
- `research/openai-codex-models.md` for the current model ladder, plan fit, and API-vs-ChatGPT split
- `reference/codex-compatibility.md` for the compatibility contract between Codex-native surfaces and repo conventions
- `reference/codex-model-guide.md` for the repo-local model and plan-tier decision matrix
- `examples/codex-model-guide-example.md` for a concrete model-choice prompt bundle
- `architecture/` for authority, events, state, and projection boundaries when a feature becomes system-level; start with the diagrams in `reference/architecture-guide.md` and `examples/architecture-example.md`

If the task is about shaping the fastest safe start with the smallest useful bundle, keep `docs/reference/agent-speedpack.md`, `docs/examples/agent-speedpack-example.md`, `docs/research/game-development/foundations/agent-speedpack.md`, `studio/checklists/discipline/speedpack.toml`, and `studio/docs/active/eval-agent-speedpack.md` together so the fast-path contract stays explicit.
- `engines/` for engine architecture and workflow notes
- `engines/*-class-editor-object-map.md` for the runtime/editor ownership model of each supported engine
- `engines/*-2d-3d-class-and-mechanic-guide.md` for the most-used 2D/3D classes, object usage patterns, mechanic recipes, writing style, and pitfalls in each supported engine
- `engines/*-2d-3d-navigation-damage-performance.md` for per-engine gameplay system, pathfinding, damage, and scale guidance
- `engines/*-gpu.md` for per-engine GPU ownership, buffer, instancing, and CPU-GPU communication guidance
- `engines/*-systems-playbook.md` for input, UI, inventory, abilities, save, encounter, and performance ownership decisions in each supported engine
- `engine-bugs.md` for recurring engine bug families, first checks, and debug surfaces in each supported engine
For the bug lane, keep `docs/reference/engine-bugs.md`, `docs/examples/engine-bugs-example.md`, and `docs/research/game-development/foundations/engine-bugs.md` in view before implementation.
If the task is about recurring engine bugs, common errors, or troubleshooting surfaces, start with `docs/reference/engine-bugs.md`, `docs/examples/engine-bugs-example.md`, and `docs/research/game-development/foundations/engine-bugs.md` before implementation.
- `engines/*-ui.md` for the most-used UI stacks, template sources, and screen-flow ownership decisions in each supported engine
- `engines/*-presentation.md` for audio playback, animation playback, presentation timing, and sync ownership decisions in each supported engine
- `engines/*-visuals-animation-playbook.md` for sprites, textures, images, animation, particle/VFX, and UI presentation ownership decisions in each supported engine
- `systems/` for gameplay/system design notes such as loop/state ownership, combat architecture, AI/navigation, save/progression boundaries, inventory/equipment, crafting/resource flow, character controller boundaries, enemy/encounter architecture, dialogue and quest state, party/companion structure, input/remap structure, UI flow, ability/upgrade systems, and world interactions
- `narrative/` for lorebook, canon, world graph, and world-state notes that support story-heavy games, codices, archives, faction networks, and structured world knowledge
- `production/` for release, CI, and content pipeline notes
- `production/README.md` for release hardening, release, versioning, platform, content, and incident entry points
- `reference/release-hardening-guide.md` for the release-hardening decision contract
- `production/platform-compatibility.md` for source-backed family-by-family compatibility planning
- `production/cross-platform.md` for support tiers, family sequencing, and release order
- `production/console.md` for PS5-like, Xbox-like, and Switch-like submission evidence and cert assumptions
- `production/release-hardening.md` for code protection, symbol policy, trust boundaries, and rollback evidence
- `production/sector-intel.md` for current game-industry, platform, and market signals
- `production/steam-intel.md` for Steam-specific store, wishlist, forum, hardware, and market signals
- `production/marketing.md` for strategy, channel mix, and measurement loops
- `production/versioning.md` for the canonical version file, changelog sync, and tag policy
- `production/release-hardening.md` for build integrity, symbol policy, and multiplayer trust
- `production/release-hardening.md` for protected builds, code protection, symbol policy, and multiplayer trust
- `assets/` for asset ownership, import rules, and asset alternatives
- `genre/` for genre-specific architectural guidance, contrast sets, and example game matrices
- `genre/genre-plan.md` for the planning schema that turns a genre preset into a buildable plan
- `genre/genre-guide.md` for how to build and validate each supported genre family
- `genre/genre-patterns.md` for the software pattern catalog behind each supported genre family
- `genre/genre-maturity.md` for how to mature each genre family into a production-ready support model
- `genre/*-md` for deeper dives into specific genre families such as deckbuilder roguelikes, survivorlikes, colony sims, factory automation games, metroidvanias, co-op survival, cozy sim, extraction-lite, narrative adventure, platformer, puzzle, and tactical RPG
- `narrative/README.md` for starting points when story canon, world graph, or lorebook architecture matter
- `reference/world-graph-methodology.md` for durable relationship and history modeling
- `reference/lorebook-methodology.md` for canon, codex, and unlockable lore
- `reference/asset-guide.md` for asset ownership, import, and alternative selection
- `reference/perf-guide.md` for FPS, frame time, memory, and scale decision order
- `reference/gpu-guide.md` for GPU ownership, render communication, buffers, and repeated-visual scale
- `reference/quality-guide.md` for code quality, maintainability, and optimization criteria
- `reference/quality-process.md` for the operating loop behind quality passes
- `reference/theory-guide.md` for durable theory stacks, design lenses, and evidence-first feature framing
- `research/game-development/foundations/theory.md` for the source-backed theory note that keeps the lens stack grounded
- `reference/architecture-guide.md` for authority, state, event, and projection architecture, with quick diagrams first
- `examples/theory-example.md`, `studio/checklists/discipline/theory.toml`, and `studio/docs/active/eval-theory.md` for the routable theory bundle
- `reference/custom-packs.md` for reusable custom feature bundles and pack registries
- `reference/custom-architecture.md` for project-specific architecture contracts and request-rule packs
- shaping custom architecture contracts, request-rule packs, or house-rule overrides when a project needs a fixed rule layer
- shaping reusable custom packs or project-specific feature registries when the project needs durable override bundles
- `examples/custom-packs-example.md`, `studio/checklists/discipline/custom_packs.toml`, `studio/docs/active/custom-packs-adr.md`, and `studio/docs/active/eval-custom-packs.md` for the full custom-pack bundle
- `reference/extensions-guide.md` for opt-in extension packs, hook points, and manifest-driven add-ons
- `reference/audio-animation-guide.md` for the simple-to-advanced audio and animation presentation ladder
- `reference/mastermind-guide.md` for broad orchestration, delegation, and user-summary control loops
- `reference/agent-system.md` for the umbrella operating model that keeps single-specialist mode visible while it coordinates controller, role matrix, hierarchy, and review trail choices
- `reference/codex-compatibility.md` for the compatibility contract between Codex-native surfaces and repo conventions
- `reference/agent-portfolio.md` for role matrices, specialist lanes, and multi-agent panel choices
- `reference/agent-hierarchy.md` for command trees, reporting lines, and async packets
- `reference/agent-validation-matrix.md` for validation matrices that prove single-specialist, pair, or panel choices
- `reference/prompt-journal.md` for prompt history, agent notes, and later review trails
- `reference/agent-transcript.md` for append-only task assignments and agent conversation turns
- `reference/agent-execution.md` for reusable work packets and pre-flight contracts that should stay separate from prompt history and transcripts
- `reference/ui-guide.md` for UI stacks, template sources, and screen-flow ownership
- `reference/genre-perf-guide.md` for genre-shaped optimization order and the first genre lever
- `reference/advanced-perf-guide.md` for advanced optimization algorithms, culling, batching, and data-oriented scale choices
- `reference/benchmark-guide.md` for benchmark families, baselines, thresholds, and artifact-backed measurement loops
- `reference/version-guide.md` for the canonical version file, changelog sync, and release tag policy
- `reference/sector-intel.md` for current game-industry, platform, and market signals
- `reference/steam-intel.md` for Steam-specific store, wishlist, forum, hardware, and chart-pack work
- `reference/platform-guide.md` for compatibility matrices across desktop, Steam, web, mobile, and TV families
- `reference/console-guide.md` for PS5-like, Xbox-like, and Switch-like readiness and submission assumptions
- `reference/cross-platform-guide.md` for support tiers and release sequencing across those same families
- `reference/marketing-guide.md` for campaign strategy, channel fit, and measurement criteria
- `reference/library-guide.md` for choosing the smallest official library or package set for a case
- `reference/engine-map.md` for the fastest engine ownership summary
- `reference/engine-fit.md` for the fastest developer-profile and team-fit summary
- `reference/engine-atlas.md` for the deeper class family breakdown
- `reference/godot-atlas.md`, `reference/unity-atlas.md`, and `reference/unreal-atlas.md` for engine-specific class deep dives
- `reference/system-atlas.md` for fast cross-system ownership and snippet jumping
- `reference/ui-guide.md` and `examples/ui-example.md` when UI stack, template source, or screen ownership is the real task
- `reference/library-guide.md` and `examples/library-example.md` when package, plugin, or SDK choice is the real task
- `reference/prompt-journal.md` and `examples/prompt-journal-example.md` when prompt history or agent step notes should be reopened later
- `reference/agent-transcript.md` and `examples/agent-transcript-example.md` when task assignments or agent conversation turns should be reopened later
- `reference/agent-execution.md` and `examples/agent-execution-example.md` when an execution packet should be reopened later
- `reference/agent-validation-matrix.md` and `examples/agent-validation-matrix-example.md` when the task needs proof rows for single-specialist, pair, or panel choice
- `templates/` for reusable note scaffolds
