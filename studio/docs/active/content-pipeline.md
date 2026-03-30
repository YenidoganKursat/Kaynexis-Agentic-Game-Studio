# Content Pipeline — Kaynexis Agentic Game Studio

## Content types
- Engine-native scenes/prefabs/maps
- Gameplay data such as enemy archetypes, encounters, and upgrade definitions
- UI, VFX, audio, and documentation needed to validate the slice

## Authoring flow
- Designers define feature intent in active docs before content scale grows
- Runtime content lands in the engine-specific project layer and keeps naming deterministic
- Tooling or import helpers belong in `tools/` or `scripts/`, not inside ad-hoc content folders

## Validation & naming
- Names should reflect gameplay purpose, not temporary author shorthand
- New content should link to at least one validation path: test, smoke, or manual QA artifact
- Treat engine-specific import settings as part of the review surface for Godot 4

## Ownership & change management
- Technical direction owns structure and import assumptions
- Design/content owners update the linked active docs when behavior or data contracts change
- Large content waves should ship with checklist coverage and at least one review note about risk

## Asset choices
- Read `docs/reference/asset-guide.md` before choosing between a reusable scene/object, a shared data asset, a sprite atlas, Addressables, or a streamable package.
- Name the source asset, the runtime owner, and the import or load boundary in the first draft.
