# Dialogue

## Date
- 2026-03-28

## Summary
- Dialogue systems become fragile when authored lines, branching rules, quest progress, relationship state, and gameplay triggers all execute in the same conversation callback. The durable split is: authored content defines lines and conditions, conversation runtime evaluates availability, and quest/state systems own persistent consequences.
- The most important early question is not "which dialogue tool?" but "what may a conversation legally change?" Without a narrow contract, dialogue becomes an unreviewable scripting layer that mutates any part of the game.
- Branching scales better when conversations emit a small set of explicit state updates such as flags, counters, quest stage changes, approvals, or unlock events. Free-form custom script hooks should be rare and documented.
- Recovery paths matter as much as happy paths. A production-safe dialogue architecture can explain what happens if a scene is interrupted, replayed, skipped, failed, localized, or resumed after loading a save.

## Primary sources
- [Life is Strange official site](https://lifeisstrange.square-enix-games.com/en-us)
- [Pentiment official site](https://pentiment.obsidian.net/)
- [Baldur's Gate 3 community update on companions and relationships](https://baldursgate3.game/news/community-update-7-romance-companionship_6)

## Why this matters to this repo
- Narrative tasks in this repo should stop at a stable boundary: authored dialogue content can request state changes, but quest truth and persistent world consequences must live in explicit systems.
- Agents need a shared mental model for:
  - what counts as authored dialogue data
  - what counts as runtime conversation state
  - what quest progression or relationship changes are allowed
  - how save/load and localization interact with conversation state
- This note gives Codex a durable way to reason about dialogue work across Godot, Unity, and Unreal without collapsing everything into one bespoke scripting graph.

## Decision impact
- Feature and quest briefs should define:
  - authored line ownership
  - branch-condition ownership
  - persistent consequence ownership
  - interruption and replay behavior
- Tasks mentioning dialogue, conversation, branching, quest stage, relationship state, or cutscene triggers should surface this note.
- Test plans should always include one interrupted path, one repeated conversation path, and one save/load resume path.

## Architecture guidance

### Separate four layers
- Authored content:
  - lines
  - speaker metadata
  - choices
  - local presentation markers
- Conversation runtime:
  - current node
  - available choices
  - temporary local variables
  - scene playback state
- Quest and world state:
  - quest stages
  - flags
  - counters
  - unlocks
  - relationship or reputation changes
- Presentation layer:
  - subtitles
  - portraits
  - voice timing
  - camera or animation cues

### Use explicit consequence messages
- A dialogue choice should emit explicit consequence requests such as:
  - set flag
  - advance quest stage
  - grant item
  - change companion approval
  - schedule follow-up scene
- Avoid arbitrary script execution as the default path.

### Guard against replay and interruption bugs
- Decide whether a scene is:
  - one-shot
  - replayable but non-repeatable in consequence
  - fully repeatable
- That choice belongs in authored state metadata, not only in code assumptions.

### Keep quest stage ownership outside the conversation graph
- Conversations may read quest state and request a stage change.
- The quest system should remain the authority that validates whether a stage can advance and what else must happen with that transition.

### Design for localization and revision
- Dialogue assets should survive:
  - line rewrites
  - branch reordering
  - added conditions
  - voice-over delays
- Stable IDs beat line-text-based logic every time.

## What to watch out for
- Choice nodes directly mutating unrelated gameplay systems
- Quest stage logic duplicated inside multiple scenes
- Relationship state stored only in dialogue graphs
- Save files preserving the current line but not the underlying consequence state
- Localization forcing branch rewrites because conditions are attached to display text instead of stable node IDs
