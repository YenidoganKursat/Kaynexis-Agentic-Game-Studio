# Unreal Presentation

## Date
- 2026-03-29

## Summary
- Unreal presentation work is simplest when audio, animation, UI, and gameplay truth stay in separate layers.
- The practical default is to start with `Audio Components` plus `Animation Blueprints`, then move to `MetaSounds`, `Quartz`, or Sequencer only when the synchronization problem is real.
- `Animation Blueprints` own the visible motion state; audio systems own the cue; gameplay classes own the truth.

## Primary sources
- [Audio Components](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-components-in-unreal-engine)
- [MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-the-next-generation-sound-sources-in-unreal-engine)
- [Quartz overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-quartz-in-unreal-engine)
- [Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine)
- [Sequencer control of Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-animation-blueprint-parameters-from-sequencer-in-unreal-engine?application_version=5.6)

## Why this matters to this repo
- Unreal features in this repo often involve telegraphs, phase changes, designer-facing timing, and packaging-sensitive presentation work.
- That becomes harder to maintain when animation graphs or audio graphs silently become the gameplay owner.
- The repo needs a durable answer for which layer owns sound, which layer owns motion, and which layer owns the actual rule.

## Decision impact
- Use this note when the task involves combat telegraphs, cue timing, character reactions, boss phases, UI feedback, or any timed presentation slice.
- Prefer the smallest valid path first:
  - one audio component or cue path
  - one animation blueprint path
  - one gameplay owner
- Move to MetaSounds, Quartz, or Sequencer only when the simple path cannot prove the timing contract.

## Simple-to-advanced ladder

### Tier 0: simple playback
- Use `Audio Components` for a one-shot cue.
- Use `Animation Blueprints` for a readable motion state.
- Keep the gameplay timing outside the animation graph.

### Tier 1: state-driven presentation
- Use animation notifies, blend states, or simple blueprint ownership when the presentation must respond to gameplay state.
- Use audio components or simple source routing when the cue needs to stay local and easy to reason about.
- Keep designer-facing tuning in the right editor surface instead of burying it in one graph.

### Tier 2: coordinated timing
- Use `MetaSounds` or `Quartz` when a cue must land on a specific rhythmic or game-synced beat.
- Use Sequencer control when animation parameters or cinematic beats must be driven from authored timing.
- Keep the timing contract explicit so the presentation remains reviewable.

### Tier 3: advanced presentation
- Use richer animation graphs, advanced audio routing, or sequence-driven control only when the baseline proves the simpler path is not enough.
- Keep gameplay authority outside the presentation graph even when the presentation becomes elaborate.
- Record the proof path and the fallback lever before tuning further.

## Common mistakes
- Letting animation blueprints own hit confirmation, invulnerability, or persistence state.
- Using audio graphs as the only place where gameplay truth is represented.
- Collapsing UI, animation, and gameplay logic into one blueprint when the feature can be split cleanly.
- Adding Sequencer or MetaSounds complexity before the basic cue-and-motion path has been measured.

## Repo impact
- This note is the default reference for Unreal boss telegraphs, character reactions, combat feedback, UI confirms, and any feature where sound and motion must stay aligned without becoming the mechanic owner.
