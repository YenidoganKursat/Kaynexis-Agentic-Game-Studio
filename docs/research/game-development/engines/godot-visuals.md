# Godot Visuals

## Date
- 2026-03-28

## Summary
- Godot's visual layer works best when sprite presentation, UI image presentation, animation playback, and VFX ownership are separated instead of being fused into one scene script.
- For this repo, the practical default is: use `Sprite2D` and `AnimatedSprite2D` for 2D world art, `TextureRect` and `Control` for UI imagery, `AnimationPlayer` and `AnimationTree` for authored motion/state, and `GPUParticles2D` or `GPUParticles3D` for effects.
- If a feature needs 3D presentation, the repo should explicitly decide whether the visual is billboard-style sprite art, a mesh-based presentation, or a particle-driven effect before implementation starts.

## Primary sources
- [Sprite2D](https://docs.godotengine.org/en/stable/classes/class_sprite2d.html)
- [AnimatedSprite2D](https://docs.godotengine.org/en/stable/classes/class_animatedsprite2d.html)
- [TextureRect](https://docs.godotengine.org/en/stable/classes/class_texturerect.html)
- [AnimationPlayer](https://docs.godotengine.org/en/stable/classes/class_animationplayer.html)
- [AnimationTree](https://docs.godotengine.org/en/stable/classes/class_animationtree.html)
- [AnimatedSprite3D](https://docs.godotengine.org/en/stable/classes/class_animatedsprite3d.html)
- [MeshInstance3D](https://docs.godotengine.org/en/stable/classes/class_meshinstance3d.html)
- [GPUParticles2D](https://docs.godotengine.org/en/4.0/classes/class_gpuparticles2d.html)
- [GPUParticles3D](https://docs.godotengine.org/en/stable/classes/class_gpuparticles3d.html)

## Why this matters to this repo
- Godot tasks in this repo should not guess at art ownership. The repo needs a durable answer for which node, resource, or animation class owns a sprite sheet, UI image, animation state, or particle effect.
- Agents need to distinguish visual presentation from gameplay authority so readability fixes, damage timing, and UI clarity do not get hidden inside animation callbacks.
- The repo should make it obvious when a feature is "just presentation" versus when it also changes collision, state, or persistence.

## Decision impact
- Use this playbook when a task involves sprites, animated sprites, texture-based UI, animation playback, particle effects, or 3D presentation around a gameplay slice.
- Prefer explicit boundaries:
  - 2D world art -> `Sprite2D` / `AnimatedSprite2D`
  - 2D UI imagery -> `TextureRect` / `Control`
  - 3D billboard or light-weight presentation -> `AnimatedSprite3D` or sprite-style 3D nodes
  - 3D mesh presentation -> `MeshInstance3D`
  - animation timing and authored motion -> `AnimationPlayer` / `AnimationTree`
  - particle/VFX systems -> `GPUParticles2D` / `GPUParticles3D`

## 2D visuals
- `Sprite2D` is the default owner for a static 2D world visual.
- `AnimatedSprite2D` is the default owner when the visual is a small flipbook-style animation with discrete frames.
- Keep texture loading and frame ownership in the sprite node or its assigned resource, not scattered across unrelated gameplay scripts.
- Watch out for: treating a sprite node as the place where combat or progression state should live.

## 3D visuals
- `AnimatedSprite3D` is useful when the game wants billboarded 2D art in a 3D scene.
- `MeshInstance3D` is the cleaner choice when the presentation should be a real 3D object rather than a sprite impostor.
- Separate visual representation from interaction and damage authority so the repo can swap presentation without rewriting the mechanic.
- Watch out for: forcing mesh-level presentation decisions into a 2D sprite pipeline or vice versa.

## Animation and presentation
- `AnimationPlayer` is the simplest authored timing surface for one-off motion, cutscene beats, or presentation events.
- `AnimationTree` is better when the repo needs stateful blending or multiple animation states that respond to gameplay state.
- Keep animation as a presentation partner; do not let animation callbacks become the only place where gameplay truth exists.
- Watch out for: storing invulnerability, room progression, or damage authority only inside animation events.

## UI image ownership
- `TextureRect` is the default owner for texture-backed UI imagery.
- The same UI rule should apply across screens: HUD icons, upgrade cards, menus, and overlays should be projected from gameplay state, not own the state themselves.
- If a screen needs interaction and layout, `Control` should own that composition while `TextureRect` owns the image itself.
- Watch out for: treating UI images as gameplay containers instead of presentation surfaces.

## VFX and particles
- `GPUParticles2D` and `GPUParticles3D` are the visual-effect owners when the effect is particle-driven.
- Keep the effect's trigger, lifetime, and gameplay meaning separate from the particle node so effects can be swapped or tuned without changing the mechanic.
- Watch out for: using particles as the only proof that an event happened without a gameplay-side confirmation path.

## Common mistakes
- Mixing sprite, animation, and gameplay authority in one scene script.
- Using a `TextureRect` or sprite node as the source of truth for progression state.
- Letting `AnimationPlayer` or `AnimationTree` become the only contract for combat timing.
- Creating 3D visuals without deciding whether they are sprite-based or mesh-based.
- Treating particle effects as gameplay logic instead of presentation.
