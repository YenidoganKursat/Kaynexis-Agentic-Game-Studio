# Unity 6 Visuals, Images, and Animation Playbook

## Date
- 2026-03-28

## Summary
- Unity's visual layer works best when sprite presentation, animation, UI imagery, and particle effects are separated into the right engine surface instead of being crammed into one MonoBehaviour.
- For this repo, the practical default is: use the sprite pipeline for 2D art, `Animator` for authored animation state, UI Toolkit or uGUI for UI imagery, and `ParticleSystem` for particle-driven effects.
- The repo should make a deliberate choice about whether a visual is a sprite, an animated sprite sheet, a UI element, or a world-space effect before implementation starts.

## Primary sources
- [Sprite Editor](https://docs.unity3d.com/ru/2021.1/Manual/SpriteEditor.html)
- [Animator component](https://docs.unity3d.com/6000.1/Documentation/Manual/class-Animator.html)
- [Particle System component reference](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ParticleSystem.html)
- [UI Toolkit](https://docs.unity3d.com/6000.1/Documentation/Manual/UIElements.html)
- [ScriptableObject](https://docs.unity3d.com/6000.1/Documentation/Manual/class-ScriptableObject.html)

## Why this matters to this repo
- Unity tasks in this repo should not collapse sprite import, animation playback, UI imagery, and VFX into one behavior script by habit.
- Agents need a stable answer to "is this a sprite asset, an animation asset, a UI surface, or a particle effect?" because that choice affects authoring speed, validation, and reuse.
- Visual decisions should stay compatible with the repo's broader rule that shared authored data and runtime state should live on different layers.

## Decision impact
- Use this playbook when a task involves sprites, sprite sheets, animation clips, animator state, UI images, or particle effects.
- Prefer explicit boundaries:
  - 2D world art -> sprite pipeline and sprite-based scene objects
  - authored animation -> `Animator` and animation clips
  - UI imagery -> UI Toolkit or uGUI as the owning surface
  - repeated effect bursts -> `ParticleSystem`
  - shared tuning or frame metadata -> `ScriptableObject`

## 2D visuals
- Use the sprite pipeline for world art that should stay lightweight and easy to author.
- Use sprite slicing or atlas-oriented workflows when the same source art needs multiple frames or variants.
- Keep sprite ownership on the scene object or prefab that represents the visual, not on a global manager.
- Watch out for: putting sprite import assumptions in gameplay code instead of letting the asset pipeline own them.

## 3D visuals
- Use the same object/component split for 3D visuals: the world object owns the presence, while components and assets own the visual behavior and tuning.
- Keep mesh presentation separate from the logic that decides when something spawns, dies, flashes, or changes state.
- Watch out for: building a 3D visual system that cannot be swapped or pooled because the presentation and gameplay are fused together.

## Animation and presentation
- `Animator` owns the animation state machine and the blend/transition contract.
- Animation should reflect gameplay state, not silently define gameplay state.
- Keep clip timing, transition timing, and gameplay authority separate so the feature remains readable and testable.
- Watch out for: using animation events as the only place where combat truth exists.

## UI image ownership
- UI Toolkit should own the visual composition when the project needs data-driven UI and authoring simplicity.
- uGUI remains viable when the project already depends on it or when runtime UI behavior is built around the older stack.
- Keep UI imagery and menu state separate from gameplay state, then project from the runtime layer into the UI layer.
- Watch out for: a UI script that becomes the source of truth for inventory, progression, or combat decisions.

## VFX and particles
- `ParticleSystem` is the default owner for common particle-driven effects such as sparks, smoke, hits, and ambient motion.
- Use the particle system as presentation, not as the only place where the event is represented.
- Watch out for: hidden allocations or excessive per-frame particle churn in hot paths.

## Common mistakes
- Treating the sprite pipeline as a dumping ground for all 2D visuals without deciding who owns the state.
- Mixing animator state, UI state, and combat state in one script.
- Putting shared tuning into scene objects when the data should be a `ScriptableObject`.
- Using particle effects as if they were gameplay authority.
