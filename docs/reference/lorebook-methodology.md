# Lorebook Methodology

Use this when a game needs a durable world-knowledge layer for canon, story facts, factions, places, characters, timeline events, glossary terms, and unlockable lore entries.

## What a lorebook is in this repo
- A lorebook is not a story dump.
- It is a canonical index of world facts that gameplay, dialogue, quests, UI, and localization can query.
- It should stay narrower than the full narrative script and broader than a one-off quest brief.

## Core rule
- The lorebook should define what is true, not replace the systems that apply those truths in gameplay.
- World state still belongs to runtime systems.
- Dialogue and quest systems may read lorebook entries and request updates, but they should not become the authority for canon.

## Recommended workflow
1. Define the canon scope.
2. Choose the entry types you need.
3. Decide what the player can read immediately and what should unlock later.
4. Link entries to quest, dialogue, item, faction, or location state.
5. Validate one lookup path, one unlock path, and one save/load resume path.

## Good lorebook entry shape
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
- owner

## What to avoid
- lore entries that secretly mutate world truth
- uncatalogued story facts living only in dialogue files
- text strings as the only identity for canon
- lorebook entries that cannot survive rewrite or localization

## Good use cases
- faction encyclopedia
- bestiary
- codex / archive / journal
- world timeline
- location notes
- item and artifact histories
- quest clue references

## Validation questions
- Is the canon scope explicit?
- Can the system answer where a fact came from?
- Can a quest or dialogue node reference the lorebook without owning canon?
- Can the game load a save and still resolve lore unlocks correctly?

## Related docs
- `docs/research/game-development/narrative/lorebook-world-state-and-canon-architecture.md`
- `docs/reference/world-graph-methodology.md`
- `docs/reference/feature-traceability.md`
- `docs/reference/handoff-contracts.md`
- `studio/docs/templates/lorebook-brief.md`
