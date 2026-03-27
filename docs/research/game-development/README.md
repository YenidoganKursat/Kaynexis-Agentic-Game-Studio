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

- `engines/` for engine architecture and workflow notes
- `engines/*-class-editor-object-map.md` for the runtime/editor ownership model of each supported engine
- `engines/*-2d-3d-navigation-damage-performance.md` for per-engine gameplay system, pathfinding, damage, and scale guidance
- `systems/` for gameplay/system design notes such as loop/state ownership, combat architecture, AI/navigation, and save/progression boundaries
- `production/` for release, CI, and content pipeline notes
- `genre/` for genre-specific architectural guidance, contrast sets, and example game matrices
- `templates/` for reusable note scaffolds
