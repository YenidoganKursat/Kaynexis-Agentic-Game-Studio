# Party

## Date
- 2026-03-28

## Summary
- Companion systems break first when the repo cannot distinguish between roster membership, active party composition, relationship state, combat behavior, and narrative availability. Those are related systems, but they should not share the same storage or control logic.
- The architecture question is: does the player command a small narrative party, a tactical squad, or lightweight AI followers? Each one changes how state, control, save boundaries, and UI should work.
- Companion-heavy games scale best when companion identity data, progression data, party-slot rules, and runtime behavior are separated. A companion being recruitable is not the same as being active, controllable, romanceable, or present in a cutscene.
- Readability matters in both narrative and combat space. Players need to know who is in the party, who is temporarily absent, what commands are available, and why a companion did or did not act.

## Primary sources
- [Baldur's Gate 3 community update on origins, hirelings, and companions](https://store.steampowered.com/news/app/1086940/view/3657534571513526777)
- [Baldur's Gate 3 community update on romance and companionship](https://baldursgate3.game/news/community-update-7-romance-companionship_6)
- [Dragon Age: The Veilguard companions hub](https://www.ea.com/en/games/dragon-age/dragon-age-the-veilguard/companions-hub)

## Why this matters to this repo
- Party or companion tasks should not be treated as only AI work or only narrative work. They cut across authored companion data, runtime following/command behavior, relationship systems, quest gating, and save/load.
- Codex needs a stable way to ask:
  - who can join the roster
  - who can occupy active party slots
  - who owns combat behavior and follow logic
  - how approval, loyalty, or progression data persist
  - how scene availability maps to party membership
- This note helps the repo route companion work into the right system boundaries instead of one giant "follower manager."

## Decision impact
- Companion or squad tasks should surface this note for keywords such as companion, follower, squad, formation, party member, recruitable ally, loyalty, approval, or escort AI.
- Feature briefs should explicitly distinguish:
  - roster state
  - active party state
  - progression or relationship state
  - runtime AI/control state
- QA should always test recruit, dismiss, downed, absent-for-story, and save/load transitions separately.

## Architecture guidance

### Split companion data into four ownership layers
- Identity data:
  - name
  - role
  - class
  - faction
  - visuals
- Persistent progression data:
  - unlock status
  - approval or loyalty
  - learned abilities
  - equipment
- Party composition data:
  - currently active
  - slot index
  - temporary availability
  - scene participation
- Runtime behavior data:
  - current command state
  - follow target
  - navigation intent
  - combat target
  - cooldown state

### Treat active party as a projection, not the whole system
- The active party should be derived from broader roster truth plus availability rules.
- That avoids bugs where removing a companion from the world accidentally erases progression or relationship state.

### Keep command grammar explicit
- Even in simple follower systems, decide what the player may request:
  - follow
  - hold
  - attack my target
  - revive
  - stay hidden
  - use ability
- Unclear command grammar leads to AI that feels random even when the implementation is technically correct.

### Separate narrative availability from combat controllability
- A companion may be:
  - recruited but not in the active combat party
  - in the active party but absent from a scene
  - scene-present but not combat-controllable
  - romanceable or loyalty-sensitive without being mechanically active
- These states should not be overloaded into one boolean.

### Handle absence and failure states explicitly
- Decide what happens when a companion is:
  - downed
  - dead or permanently lost
  - temporarily story-locked
  - not yet recruited
  - unavailable because the party is full
- The UI and save system need those distinctions to be stable.

## What to watch out for
- Relationship state stored only on runtime follower actors
- Party-slot UI driving roster truth instead of reflecting it
- Narrative scenes assuming all recruited companions are present
- Escort or follow logic coupled directly to quest stage logic
- Save files serializing spawned companion actors instead of the underlying party and progression state
