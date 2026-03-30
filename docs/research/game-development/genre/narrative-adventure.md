# Narrative Adventure

## Date
- 2026-03-29

## Summary
- Narrative adventures fail first on branch explosion, hidden state bugs, and weak choice visibility. The player must be able to tell what changed, why it changed, and when it matters again.
- The dominant loop is:
  - enter a scene
  - read dialogue or narration
  - make a meaningful choice
  - project consequence into later scenes
  - continue with authored state intact
- The first systems that usually break are:
  - branch trees becoming too wide to produce safely
  - consequence state becoming opaque
  - content throughput slowing because every scene needs too many variants
  - localization and tone drifting across branches
- This genre needs explicit architecture for:
  - dialogue ownership
  - branch projection
  - consequence state and scene memory
  - localization-aware content production
  - simple recovery from authoring mistakes

## Primary sources
- [Life is Strange official site](https://lifeisstrange.square-enix-games.com/en-us)
- [Life is Strange FAQ: Double Exposure](https://lifeisstrange.square-enix-games.com/de/games/life-is-strange-double-exposure/faq)
- [Pentiment official site](https://pentiment.obsidian.net/)
- [Pentiment on Steam](https://store.steampowered.com/app/1205520/)

## Why this matters to this repo
- Narrative adventure tasks in this repo should not be routed like generic quest or dialogue tasks. They are branch-management and consequence-presentation problems first.
- Agents should explicitly name:
  - which scene owns the truth
  - what state persists across scenes
  - where choices become visible later
  - how the content pipeline avoids branch explosion
- First slices should prove one scene, one meaningful choice, and one follow-up consequence before the story fans out.

## Decision impact
- Future presets and feature briefs should require:
  - dialogue or branch projection
  - state projection for consequences
  - localization sensitivity
  - a small content pipeline that can survive branch growth
- When a project selects this genre, route output should surface dialogue, state, and content-production notes together.
