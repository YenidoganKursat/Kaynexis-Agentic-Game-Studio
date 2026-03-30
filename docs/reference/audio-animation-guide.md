# Audio and Animation Guide

Use this page when a task is about sound cues, animation timing, presentation state, or how audio and animation should coordinate without becoming the gameplay owner.

`audio-direction-lite.md` is the short project-level starting point. This page is the full operating guide for simple-to-advanced presentation work.

## Summary

- Audio and animation should reinforce gameplay truth, not secretly own it.
- The simplest valid solution is usually a single playback owner plus a clear validation loop.
- The advanced solution is only worth it when the basic clip, state machine, or mixer path no longer holds up under scale or timing pressure.
- The same ownership vocabulary should appear in the guide, the engine playbook, the checklist, the route output, and the example.

## Primary sources

- Godot: [AudioStreamPlayer](https://docs.godotengine.org/en/stable/classes/class_audiostreamplayer.html), [AudioEffectInstance](https://docs.godotengine.org/en/stable/classes/class_audioeffectinstance.html), [AnimationPlayer](https://docs.godotengine.org/en/stable/classes/class_animationplayer.html), [AnimationTree](https://docs.godotengine.org/en/stable/classes/class_animationtree.html)
- Unity: [AudioSource](https://docs.unity3d.com/6000.1/Documentation/Manual/class-AudioSource.html), [AudioMixer](https://docs.unity3d.com/6000.1/Documentation/Manual/class-AudioMixer.html), [Animator component](https://docs.unity3d.com/6000.1/Documentation/Manual/class-Animator.html), [Animation clips](https://docs.unity3d.com/6000.1/Documentation/Manual/AnimationClips.html)
- Unreal: [Audio Components](https://dev.epicgames.com/documentation/en-us/unreal-engine/audio-components-in-unreal-engine), [MetaSounds](https://dev.epicgames.com/documentation/en-us/unreal-engine/metasounds-the-next-generation-sound-sources-in-unreal-engine), [Quartz overview](https://dev.epicgames.com/documentation/en-us/unreal-engine/overview-of-quartz-in-unreal-engine), [Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/animation-blueprints-in-unreal-engine), [Sequencer control of Animation Blueprints](https://dev.epicgames.com/documentation/en-us/unreal-engine/control-animation-blueprint-parameters-from-sequencer-in-unreal-engine?application_version=5.6)

## Why this matters to this repo

- This repo keeps running into timing-heavy work: combat telegraphs, footsteps, hit reactions, UI confirms, menu flows, and boss phases.
- Those tasks become hard to review when audio owns gameplay truth or animation owns collision, damage, or persistence.
- A clear presentation model keeps the player feedback readable while preserving a clean gameplay owner.

## Decision impact

- Use this guide when a task involves sound effects, music, voice, animation clips, animation graphs, presentation timing, or synchronized feedback.
- Prefer the simplest valid path first:
  - one cue -> one playback owner
  - one state -> one animator or animation tree
  - one timing path -> one validation loop
- Move to advanced routing, snapshots, graphs, notifies, or sequencers only when the basic path is proven too small.

## Simple-to-advanced ladder

### Tier 0: simple playback

- Audio: one-shot clip playback, basic event cues, and a small number of sources.
- Animation: one clip, one flipbook, or one authored motion event.
- Use this when the goal is to prove readability and feedback, not to build a full presentation system.

### Tier 1: state-driven presentation

- Audio: positional playback, grouped sources, and a basic mix split.
- Animation: a state machine or authored transition surface tied to gameplay state.
- Use this when the feature needs stateful feedback but still fits in a small, readable ownership model.

### Tier 2: timed coordination

- Audio: routing through mixer groups or bus-style layers, plus event-driven ducking or emphasis.
- Animation: animation events, notifies, call-method tracks, or state-specific transition windows.
- Use this when one cue must land against one animation event or one gameplay window.

### Tier 3: advanced presentation

- Audio: graph-based synthesis, explicit timing systems, advanced routing, concurrency control, or source pooling.
- Animation: blend graphs, layered states, timeline/sequence control, or a dedicated presentation graph.
- Use this only when the simple path is not enough and the repo can name the baseline, the first lever, and the fallback lever.

## Engine-specific notes

### Godot 4

- Simple: `AudioStreamPlayer` or `AudioStreamPlayer2D`/`AudioStreamPlayer3D` plus `AnimationPlayer` for a short windup, hit flash, or UI confirm.
- Mid: `AnimationTree` for stateful animation transitions and audio bus routing for clear mix separation.
- Advanced: audio buses and effect chains for mix control, `AudioEffectInstance` for custom effect work, and `AnimationTree`-driven state blending when the presentation needs more than a few clips.
- Watch out for: hiding damage, invulnerability, or room progression inside animation callbacks or sound triggers.

### Unity 6

- Simple: `AudioSource` plus `Animator` and `AnimationClip` for a readable cue-and-motion pair.
- Mid: `AudioMixer` routing, animation controllers, blend trees, and animation events for state-aware presentation.
- Advanced: timeline or playable-driven sequencing when one cue, one motion, and one camera beat must stay aligned.
- Watch out for: making `Animator` or `AudioSource` the only place where the game truth exists.

### Unreal 5

- Simple: `Audio Components` plus `Animation Blueprints` for a clean playback pair.
- Mid: `MetaSounds`, `Quartz`, animation notifies, and Sequencer links when the presentation needs tighter timing.
- Advanced: layered animation graphs, audio routing, and sequence-driven control when the presentation needs designer-facing timing or more than one feedback lane.
- Watch out for: letting animation graphs or sound graphs become the only owner of gameplay state.

## Common mistakes

- Putting gameplay authority inside animation callbacks.
- Treating audio cues as proof of state instead of projection of state.
- Using a timeline or sequence as a shortcut for unclear architecture.
- Mixing simple playback, mix design, and gameplay ownership into one script or blueprint.
- Reaching for advanced graphs before the baseline is measured.

## Example prompts for the agent

```bash
python3 scripts/codex_studio.py next "Design a Godot boss windup where animation timing and audio cue timing stay separate from gameplay authority"
python3 scripts/codex_studio.py next "Compare Unity AudioMixer routing and Animator state ownership for an inventory open and close flow"
python3 scripts/codex_studio.py next "Plan an Unreal MetaSounds and Animation Blueprint timing path for a readable enemy telegraph"
python3 scripts/codex_studio.py checklist --task "Run an audio and animation pass on a Unity 6 combat HUD without hiding gameplay truth in the presentation layer"
```

## Validation

- State the playback owner, the timing owner, and the gameplay owner.
- Name the narrowest proof path: one cue, one animation event, one manual loop, or one timing test.
- If the task becomes scale-sensitive, name the baseline, the first lever, and the fallback lever.
- Keep the guide, engine playbook, checklist, and example synchronized in the same change.

## Related docs

- `docs/examples/audio-animation-example.md`
- `docs/research/game-development/engines/godot-presentation.md`
- `docs/research/game-development/engines/unity-presentation.md`
- `docs/research/game-development/engines/unreal-presentation.md`
- `docs/reference/engine-map.md`
- `docs/reference/engine-examples.md`
- `docs/reference/system-atlas.md`
- `docs/reference/workflow-recipes.md`
- `docs/reference/task-prompt-examples.md`
- `docs/reference/agent-guide.md`
- `studio/docs/templates/audio-direction-lite.md`
