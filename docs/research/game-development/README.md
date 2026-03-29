# Game Development Research

This knowledge base is the durable research layer for the Codex-first studio system.

Use it when:

- choosing or revising engine architecture
- shaping build and release flows
- deciding on content pipeline rules
- introducing system-heavy gameplay or production workflows

Research rules:

- prefer official or primary sources first
- date every note
- finish each note with a repo-impact statement
- link the note from the task, checklist, or active doc that depends on it

Structure:

- `foundations/` for canonical theory, standards, and academic research that should shape design and architectural reasoning across engines and genres
- `engines/` for engine architecture and workflow notes
- `engines/*-class-editor-object-map.md` for the runtime/editor ownership model of each supported engine
- `engines/*-2d-3d-class-and-mechanic-guide.md` for the most-used 2D/3D classes, object usage patterns, mechanic recipes, writing style, and pitfalls in each supported engine
- `engines/*-2d-3d-navigation-damage-performance.md` for per-engine gameplay system, pathfinding, damage, and scale guidance
- `engines/*-systems-playbook.md` for input, UI, inventory, abilities, save, encounter, and performance ownership decisions in each supported engine
- `engines/*-visuals-animation-playbook.md` for sprites, textures, images, animation, particle/VFX, and UI presentation ownership decisions in each supported engine
- `systems/` for gameplay/system design notes such as loop/state ownership, combat architecture, AI/navigation, save/progression boundaries, inventory/equipment, crafting/resource flow, character controller boundaries, enemy/encounter architecture, dialogue and quest state, party/companion structure, input/remap structure, UI flow, ability/upgrade systems, and world interactions
- `narrative/` for lorebook, canon, world graph, and world-state notes that support story-heavy games, codices, archives, faction networks, and structured world knowledge
- `production/` for release, CI, and content pipeline notes
- `genre/` for genre-specific architectural guidance, contrast sets, and example game matrices
- `genre/genre-development-playbook.md` for how to build and validate each supported genre family
- `genre/genre-advanced-development-framework.md` for how to mature each genre family into a production-ready support model
- `genre/*-architecture.md` for deeper dives into specific genre families such as deckbuilder roguelikes, survivorlikes, colony sims, factory automation games, and metroidvanias
- `narrative/README.md` for starting points when story canon, world graph, or lorebook architecture matter
- `reference/world-graph-methodology.md` for durable relationship and history modeling
- `reference/lorebook-methodology.md` for canon, codex, and unlockable lore
- `templates/` for reusable note scaffolds
