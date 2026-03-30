# Unity Presentation

## Date
- 2026-03-29

## Summary
- Unity presentation work is simplest when `AudioSource`, `Animator`, and `AnimationClip` stay in separate lanes.
- The practical default is to start with a clip and one source, then move to `AudioMixer`, state machines, and timing graphs only when the feature really needs them.
- `Animator` owns the animation state machine and transition logic; `AudioMixer` owns mix routing; gameplay code owns the truth.

## Primary sources
- [AudioSource](https://docs.unity3d.com/6000.1/Documentation/Manual/class-AudioSource.html)
- [AudioMixer](https://docs.unity3d.com/6000.1/Documentation/Manual/class-AudioMixer.html)
- [Animator component](https://docs.unity3d.com/6000.1/Documentation/Manual/class-Animator.html)
- [Animation clips](https://docs.unity3d.com/6000.1/Documentation/Manual/AnimationClips.html)

## Why this matters to this repo
- Unity features in this repo often combine feedback, controller navigation, and repeated state changes.
- That combination gets messy when the same `MonoBehaviour` owns sound playback, animation transitions, UI state, and gameplay truth.
- The repo needs a stable answer for which surface owns playback, which owns timing, and which owns the actual rule.

## Decision impact
- Use this note when the task involves combat feedback, menu confirms, HUD motion, inventory open/close, or any state-driven presentation.
- Prefer the smallest valid path first:
  - one `AudioSource`
  - one `Animator`
  - one gameplay owner
- Move to mixer routing, blend trees, or timing graphs only when the baseline proves they are needed.

## Simple-to-advanced ladder

### Tier 0: simple playback
- Use `AudioSource` for a one-shot cue.
- Use `Animator` plus a single `AnimationClip` for a visible motion beat.
- Keep the gameplay decision in code, not in the clip.

### Tier 1: state-driven presentation
- Use `Animator` controllers and animation parameters when state needs to blend or branch.
- Use `AudioMixer` groups when sounds need to be separated or balanced.
- Keep state and projection separate so the UI or animation can reflect the game rather than own it.

### Tier 2: coordinated timing
- Use animation events or a timing surface only when the cue must land on a visible frame or beat.
- Use mixer snapshots or routing when the mix needs to duck or emphasize a state change.
- Keep the proof path narrow enough that timing remains reviewable.

### Tier 3: advanced presentation
- Use timeline or playables when one motion, one cue, and one camera beat must stay aligned.
- Use advanced animation layers or mixer graphs when the project has proven that the simpler path is too small.
- Capture the baseline first so the advanced path is justified rather than habitual.

## Common mistakes
- Letting `Animator` become the only place where combat truth exists.
- Using `AudioSource` as a gameplay state container.
- Mixing menu logic, gameplay logic, and presentation logic in one component.
- Adding `AudioMixer` or timeline complexity before the basic cue-plus-clip path has been measured.

## Repo impact
- This note is the default reference for Unity boss telegraphs, UI confirms, combat reactions, menu motion, and any feature where sound and animation must stay aligned without becoming the mechanic owner.
