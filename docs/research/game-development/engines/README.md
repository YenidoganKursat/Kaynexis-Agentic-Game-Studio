# Engine Research Notes

This folder holds the engine-specific knowledge base for the studio system.

Use these notes when:

- choosing the primary engine for a project
- deciding whether a feature should live in runtime code, authored data, or editor tooling
- selecting the right 2D or 3D stack before implementation
- mapping a mechanic onto engine-native classes and objects instead of forcing a generic pattern
- deciding how input, UI, inventory, abilities, encounters, save flow, and scale should be owned in that engine

Recommended read order for an engine-specific task:

1. `*-architecture.md`
2. `*-class-editor-object-map.md`
3. `*-2d-3d-class-and-mechanic-guide.md`
4. `*-2d-3d-navigation-damage-performance.md`
5. `*-systems-playbook.md`
6. `*-visuals-animation-playbook.md`

What each note does:

- `*-architecture.md` explains the repo-level layout and toolchain assumptions for that engine.
- `*-class-editor-object-map.md` explains the core runtime, data, and editor ownership model.
- `*-2d-3d-class-and-mechanic-guide.md` explains the most-used classes, object types, mechanic patterns, writing style expectations, and common mistakes for 2D and 3D work.
- `*-2d-3d-navigation-damage-performance.md` explains navigation, damage/contact, and scale/performance decisions.
- `*-systems-playbook.md` explains controls, UI, inventory, abilities, encounters, save flow, and performance-sensitive ownership decisions.
- `*-visuals-animation-playbook.md` explains sprites, textures, images, animation playback, VFX, and UI presentation ownership decisions.
