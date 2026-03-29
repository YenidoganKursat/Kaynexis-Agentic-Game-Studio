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

## Start Here

- `setup/getting-started.md`
- `setup/first-hour-walkthrough.md`
- `setup/installer-checklist.md`
- `setup/troubleshooting.md`
- `setup/github-maintainer-setup.md`
- `setup/optional-codex-hooks.md`
- `setup/secrets-and-env.md`
- `reference/repo-tour.md`
- `reference/command-cheatsheet.md`
- `reference/engine-selection-guide.md`
- `reference/engine-examples.md`
- `reference/workflow-recipes.md`
- `reference/task-prompt-examples.md`
- `reference/lorebook-methodology.md`
- `reference/world-graph-methodology.md`
- `reference/code-review.md`
- `reference/eval-strategy.md`
- `reference/genre-presets.md`
- `reference/codex-compatibility.md`
- `reference/engine-agent-guidelines.md`
- `reference/handoff-contracts.md`
- `reference/feature-traceability.md`
- `reference/doc-sync-audit.md`
- `reference/balance-simulator.md`
- `examples/README.md`
- `research/openai-codex-infra-findings.md`
- `research/game-development/README.md`
- `research/game-development/foundations/README.md`
- `research/game-development/engines/README.md`
- `research/game-development/genre/README.md`
- `research/game-development/genre/genre-development-playbook.md`
- `research/game-development/genre/genre-advanced-development-framework.md`

## Responsibility Split

- `docs/` — static repo/operator documentation
- `docs/research/` — source-backed notes behind repo policy and engine/production decisions
- `studio/docs/templates/` — reusable project document templates
- `studio/docs/active/` — live project truth for the current game

## Engine Research Highlights

If you are doing engine-specific work, start here:

- `docs/research/game-development/engines/README.md`
- `docs/reference/engine-examples.md`
- `docs/research/game-development/genre/README.md`
- `docs/research/game-development/genre/genre-development-playbook.md`
- `docs/research/game-development/genre/genre-advanced-development-framework.md`
- `docs/research/game-development/engines/godot-4-2d-3d-class-and-mechanic-guide.md`
- `docs/research/game-development/engines/unity-6-2d-3d-class-and-mechanic-guide.md`
- `docs/research/game-development/engines/unreal-5-2d-3d-class-and-mechanic-guide.md`

Those guides exist so the repo does not silently collapse back into a Godot-only mental model. They explain the most-used classes, objects, mechanic ownership patterns, writing style expectations, and common mistakes for each engine family.

## Academic Foundations Highlights

If a design discussion is getting fuzzy or purely opinion-based, start here:

- `research/game-development/foundations/design-frameworks-mda-gameflow-and-sdt.md`
- `research/game-development/foundations/game-feel-usability-and-accessibility-foundations.md`
- `research/game-development/foundations/ai-pathfinding-and-decision-foundations.md`
- `research/game-development/foundations/difficulty-balance-and-adaptation-foundations.md`

Those notes exist so the repo can reason from canonical theory and standards, not just implementation habits.

## Systems Research Highlights

If the task is about inventory, character state, enemy architecture, or save/combat boundaries, start here:

- `research/game-development/systems/inventory-equipment-and-item-architecture.md`
- `research/game-development/systems/character-controller-ability-and-state-architecture.md`
- `research/game-development/systems/enemy-roster-behavior-and-encounter-architecture.md`
- `research/game-development/systems/crafting-recipes-and-resource-flow-architecture.md`
- `research/game-development/systems/dialogue-conversation-and-quest-state-architecture.md`
- `research/game-development/systems/party-companion-and-squad-architecture.md`
- `research/game-development/systems/input-controls-camera-and-remapping-architecture.md`
- `research/game-development/systems/ui-hud-menu-and-screen-flow-architecture.md`
- `research/game-development/systems/abilities-skill-trees-upgrades-and-build-architecture.md`
- `research/game-development/systems/interactions-pickups-and-world-object-architecture.md`
- `research/game-development/systems/combat-damage-and-effects-architecture.md`
- `research/game-development/systems/save-progression-and-runtime-data-architecture.md`

Those notes exist so the repo does not reduce system-heavy work to "just add another script." They define ownership, persistence, authored-data boundaries, encounter roles, and the main scaling risks.

## Narrative Research Highlights

If the task is about story canon, lorebook structure, world graphs, or narrative state, start here:

- `reference/lorebook-methodology.md`
- `reference/world-graph-methodology.md`
- `research/game-development/narrative/README.md`
- `research/game-development/narrative/lorebook-world-state-and-canon-architecture.md`
- `research/game-development/narrative/world-graph-relationship-history-architecture.md`
- `research/game-development/systems/dialogue-conversation-and-quest-state-architecture.md`

Those notes exist so story facts, unlocks, and dialogue references stay separate instead of drifting into one large script layer.

## Genre Research Highlights

If the team is still deciding what kind of game it is making, or if a feature depends on genre-specific constraints, start here:

- `research/game-development/genre/genre-development-playbook.md`
- `research/game-development/genre/genre-advanced-development-framework.md`
- `research/game-development/genre/genre-design-pattern-catalog.md`
- `research/game-development/genre/genre-example-matrix.md`
- `research/game-development/genre/auto-battler-architecture.md`
- `research/game-development/genre/deckbuilder-roguelike-architecture.md`
- `research/game-development/genre/survivorlike-architecture.md`
- `research/game-development/genre/colony-sim-architecture.md`
- `research/game-development/genre/grand-strategy-architecture.md`
- `research/game-development/genre/stealth-architecture.md`
- `research/game-development/genre/factory-automation-architecture.md`
- `research/game-development/genre/metroidvania-architecture.md`
- `research/game-development/genre/city-builder-architecture.md`
- `research/game-development/genre/life-sim-architecture.md`
- `research/game-development/genre/hero-shooter-architecture.md`
- `research/game-development/genre/soulslike-architecture.md`

Those notes exist so the repo does not flatten every project into the same first-slice advice. They explain dominant loops, first systems that usually break, and what to study from official game pages before scoping work.

### Genre families now covered

- `action-roguelite` for readable combat runs and build variety
- `deckbuilder-roguelike` for sequencing, reward health, and route tension
- `co-op-survival` for shared scarcity and session authority
- `auto-battler` for draft economy, board placement, and round resolution
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
