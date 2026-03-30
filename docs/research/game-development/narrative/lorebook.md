# Lorebook

## Date
- 2026-03-29

## Summary
- Lorebooks work best when they act as a canonical index of world knowledge, not as a hidden narrative engine.
- The stable split is: authored lore entries define facts and references, runtime state owns unlocks and consequences, and dialogue or quest systems query the canon instead of redefining it.
- A production-safe lorebook can explain what the player already knows, what remains locked, what changed after a quest, and which facts should survive save/load and localization.

## Primary sources
- [Yarn Spinner Variable Storage](https://docs.yarnspinner.dev/components/variable-storage/variable-storage)
- [Yarn Spinner Dialogue Runner overview](https://docs.yarnspinner.dev/2.5/using-yarnspinner-with-rust/components/dialogue-runner)
- [Yarn Spinner Variables](https://docs.yarnspinner.dev/next/writing-dialogue-in-yarn/writing-in-yarn/logic-and-variables)
- [Yarn Spinner Dialogue Presenter Base](https://docs.yarnspinner.dev/api/csharp/yarn.unity/yarn.unity.dialoguepresenterbase)
- [Twine Cookbook Macros](https://twinery.org/cookbook/terms/terms_macros.html)
- [Twine Cookbook Style Guide](https://twinery.org/cookbook/style_guide.html)

## Why this matters to this repo
- The repo already has dialogue, quest, localization, and content-pipeline notes. Lorebook support fills the missing middle layer: a durable world-knowledge surface that feeds those systems without collapsing into a giant narrative script.
- That matters for games with codices, archives, bestiaries, faction glossaries, clue systems, or story collections.
- Without this layer, teams tend to store canon in scattered dialogue nodes, item descriptions, quest scripts, and wiki pages that drift apart.

## Decision impact
- Use this note when the game needs a lorebook, codex, world bible, journal, bestiary, or archive system.
- Tasks mentioning lorebook, canon, world bible, story bible, codex, archive, bestiary, or world knowledge should surface this note.
- Feature briefs should state which systems own canon, which systems only read it, and how unlocks or revisions are validated.

## Architecture guidance

### Separate canon from presentation
- Canon entries should live in structured data, not only in localized prose.
- Presentation text can be rewritten for tone, but stable ids and metadata must stay consistent.
- A lorebook entry may surface as a codex page, glossary panel, bestiary card, quest clue, or codex unlock.

### Use stable entry identity
- Every entry should have a stable id that survives rewrites, localization, and ordering changes.
- Do not use display text as the only lookup key.
- Prefer explicit tags for faction, location, timeline, item, event, and character relationships.

### Let runtime state own unlocks
- The lorebook may be read by quests, dialogue, item systems, or UI.
- The unlock of an entry should be owned by a runtime system that can be saved, loaded, and tested.
- If a lore entry changes world state, that transition must be explicit and reviewable.

### Keep the entry schema small but expressive
- Good lorebook entries usually need:
  - stable id
  - title
  - short summary
  - canon status
  - tags
  - related entries
  - unlock conditions
  - gameplay hooks
  - localization keys
  - source or owner
  - revision

### Design for retrieval, not just writing
- A lorebook is successful when the game can answer:
  - what does the player already know?
  - what just became unlockable?
  - which facts are still hidden?
  - which quest or scene should reference this entry?
- Retrieval should be deterministic and easy to debug.

### Keep narrative ownership explicit
- Dialogue systems may reference lorebook entries.
- Quest systems may unlock them.
- UI systems may present them.
- None of those systems should become the canon authority by accident.

## What to watch out for
- Story facts stored only in dialogue scripts
- Lore entries that change gameplay state without an owned system
- Canon that cannot survive localization or rewrite
- Too many entry types before the basic lookup/unlock loop works
- A lorebook that is only a wiki page instead of a usable game system

## Validation expectations
- A mature lorebook support surface should be able to answer:
  - What is canon?
  - What is visible now?
  - What unlocks the next fact?
  - Which system owns that unlock?
  - Can the lorebook survive save/load and localization?
- If those questions cannot be answered clearly, the lorebook is still in concept territory.

## Related references
- `docs/reference/world-graph-methodology.md`
- `docs/reference/lorebook-methodology.md`
- `docs/research/game-development/systems/dialogue.md`
- `docs/research/game-development/systems/save.md`
- `docs/research/game-development/foundations/frameworks.md`
