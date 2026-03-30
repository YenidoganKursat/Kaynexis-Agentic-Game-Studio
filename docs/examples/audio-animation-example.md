# Audio and Animation Example

## Scope

- Godot 4 combat room: a boss windup cue, a readable hit flash, and a short reaction animation
- Unity 6 inventory HUD: an open/close sound, a menu transition, and a controller-safe confirm cue
- Unreal 5 enemy telegraph: a MetaSounds cue, an animation notify, and a clear damage window

## Baseline

| Case | Current pain | Quality target |
| --- | --- | --- |
| Godot boss windup | the attack timing is hidden across scene logic and animation callbacks | keep the gameplay authority in runtime code and let audio/animation project it |
| Unity HUD | the UI sound, animation, and state change are tangled together | separate the playback owner, the state owner, and the UI projection |
| Unreal telegraph | the damage timing only feels readable inside the animation graph | keep the gameplay window explicit and use presentation only as feedback |

## Decision order

1. Name the gameplay owner first.
2. Name the playback owner second.
3. Name the sync owner third.
4. Choose the simplest valid playback path.
5. Add mixer, graph, timeline, or notify complexity only if the baseline proves it is needed.

## Engine-shaped examples

### Godot 4

- `AudioStreamPlayer` plays the cue.
- `AnimationPlayer` handles the windup and reaction motion.
- `AnimationTree` only enters the picture if the state set becomes large enough to need blending.
- The game logic still owns the hit window, recovery window, and reward state.

### Unity 6

- `AudioSource` plays the cue.
- `Animator` owns the state machine and transitions.
- `AudioMixer` handles mix separation only when the project needs ducking, grouping, or volume routing.
- The gameplay code still owns the timing decision and the damage or reward consequence.

### Unreal 5

- `Audio Components` or `MetaSounds` play the cue.
- `Animation Blueprints` own the visible motion state.
- `Quartz` or Sequencer is only chosen when the sync problem is real and reproducible.
- The gameplay layer still owns the authoritative hit window and phase change.

## Good agent prompts

- "Run an audio and animation pass on a Godot combat room and keep the go/no-go gate explicit."
- "Compare Unity AudioSource, AudioMixer, and Animator ownership for an inventory HUD open/close flow."
- "Design an Unreal enemy telegraph that uses MetaSounds and Animation Blueprints without hiding gameplay truth."
- "Keep the playback owner, timing owner, and gameplay owner separate before adding more presentation polish."

## Validation

- show the ownership model
- name the validation loop
- show one command, one manual loop, or one timing check that proves the change
- if the feature grows beyond the baseline, document the first lever and the fallback lever
