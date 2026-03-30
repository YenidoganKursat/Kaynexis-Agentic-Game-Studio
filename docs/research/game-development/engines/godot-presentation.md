# Godot Presentation

## Date
- 2026-03-29

## Summary
- Godot presentation work is cleanest when audio playback, animation playback, and gameplay truth stay in separate lanes.
- The simplest valid path is usually one `AudioStreamPlayer` plus one `AnimationPlayer`.
- `AnimationTree` becomes the right choice when the state set grows and the project needs structured blending or state-machine control.
- Audio buses and effects should shape the mix, not own the mechanic.

## Primary sources
- [AudioStreamPlayer](https://docs.godotengine.org/en/stable/classes/class_audiostreamplayer.html)
- [AudioEffectInstance](https://docs.godotengine.org/en/stable/classes/class_audioeffectinstance.html)
- [AnimationPlayer](https://docs.godotengine.org/en/stable/classes/class_animationplayer.html)
- [AnimationTree](https://docs.godotengine.org/en/stable/classes/class_animationtree.html)

## Why this matters to this repo
- Godot tasks here often need tight feedback loops: combat telegraphs, hit reactions, UI confirms, footstep cues, or boss phase beats.
- Those features get hard to review when timing and gameplay truth are mixed into the same node or callback.
- The repo benefits from a durable answer to what owns playback, what owns timing, and what only projects the result.

## Decision impact
- Use this note when the task involves sound cues, motion cues, footstep timing, reaction windows, boss telegraphs, or presentation polish.
- Prefer the smallest valid path first:
  - one `AudioStreamPlayer`
  - one `AnimationPlayer`
  - one clear gameplay owner
- Move to `AnimationTree`, audio buses, or effect chains only when the simple path is not enough.

## Simple-to-advanced ladder

### Tier 0: simple playback
- Use `AudioStreamPlayer` for a one-shot cue.
- Use `AnimationPlayer` for a short timed motion or reaction.
- Keep the gameplay window in the runtime script, not in the presentation node.

### Tier 1: state-driven presentation
- Use `AudioStreamPlayer2D` or `AudioStreamPlayer3D` when the cue must feel spatial.
- Use `AnimationTree` when the motion needs stateful transitions or blend control.
- Keep the state model explicit so presentation can reflect it instead of defining it.

### Tier 2: coordinated timing
- Use audio bus routing when mix priority or ducking matters.
- Use `AnimationPlayer` method tracks or `AnimationTree` transitions when one cue must land on one visible beat.
- Keep callbacks as synchronization helpers, not the only truth source.

### Tier 3: advanced presentation
- Use bus chains, effect instances, and structured animation trees when the project needs more control than a few one-shots and clips.
- Keep the validation path narrow: one cue, one motion, one baseline measurement.
- Escalate only when the baseline proves the simpler path is not enough.

## Common mistakes
- Letting animation callbacks own damage, invulnerability, or room progression.
- Using audio playback nodes as hidden state containers.
- Mixing UI feedback, world feedback, and gameplay authority in one script.
- Adding bus effects or animation trees before the simple path has been measured.

## Repo impact
- This note is the default reference for Godot boss telegraphs, combat reactions, footstep cues, menu confirms, and any feature where sound and motion must stay aligned without becoming the mechanic owner.
