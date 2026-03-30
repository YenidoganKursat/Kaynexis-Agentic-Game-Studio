# Engines

This folder holds the engine-specific knowledge base for the studio system.

Use these notes when:

- choosing the primary engine for a project
- deciding whether a feature should live in runtime code, authored data, or editor tooling
- selecting the right 2D or 3D stack before implementation
- mapping a mechanic onto engine-native classes and objects instead of forcing a generic pattern
- comparing Godot 4, Unity 6, and Unreal 5 on build, test, performance, or toolchain readiness
- troubleshooting recurring engine bugs, common errors, and editor/runtime/build mismatches
- deciding how input, UI, inventory, abilities, encounters, save flow, and scale should be owned in that engine

If the task is an engine comparison or scorecard task, read `docs/reference/engine-eval.md` and `docs/examples/engine-eval-example.md` before this page so the decision is measured instead of guessed.

## Atlas-first orientation

The engine layer now uses a deeper atlas vocabulary so the docs can answer ownership questions earlier:

- `docs/reference/engine-map.md` for the short cross-engine owner summary
- `docs/reference/engine-atlas.md` for the deeper class-family breakdown, including the additional structural families layer
- `docs/reference/system-atlas.md` for the gameplay/system ownership overview
- `docs/reference/godot-atlas.md`, `docs/reference/unity-atlas.md`, and `docs/reference/unreal-atlas.md` for engine-specific deep dives

Recommended read order for an engine-specific task:

1. `*-architecture.md`
2. `*-class-editor-object-map.md`
3. `*-2d-3d-class-and-mechanic-guide.md`
4. `docs/reference/engine-bugs.md` and `docs/examples/engine-bugs-example.md` when the task is bug or troubleshooting shaped
5. `*-2d-3d-navigation-damage-performance.md`
6. `*-gpu.md`
7. `*-systems-playbook.md`
8. `*-ui.md`
9. `*-presentation.md`
10. `*-visuals-animation-playbook.md`

What each note does:

- `*-architecture.md` explains the repo-level layout and toolchain assumptions for that engine.
- `*-class-editor-object-map.md` explains the core runtime, data, and editor ownership model.
- `*-2d-3d-class-and-mechanic-guide.md` explains the most-used classes, object types, mechanic patterns, writing style expectations, and common mistakes for 2D and 3D work.
- `*-2d-3d-navigation-damage-performance.md` explains navigation, damage/contact, and scale/performance decisions.
- `docs/reference/engine-bugs.md` explains recurring engine bug families, first checks, and debug surfaces before the agent proposes a fix.
- `*-gpu.md` explains GPU ownership, CPU-GPU communication, buffer shape, and repeated-visual scale decisions.
- `*-systems-playbook.md` explains controls, UI, inventory, abilities, encounters, save flow, and performance-sensitive ownership decisions.
- `*-ui.md` explains the most-used UI stack, template source choices, focus behavior, and screen-flow ownership decisions.
- `*-presentation.md` explains audio playback, animation playback, timing ownership, and presentation sync decisions.
- `*-visuals-animation-playbook.md` explains sprites, textures, images, animation playback, VFX, and UI presentation ownership decisions.

If you want concrete side-by-side examples before you choose a mechanic or slice, also read `docs/reference/engine-examples.md`.
If you are comparing engines for build, test, performance, or toolchain readiness, also read `docs/reference/engine-eval.md` and `docs/examples/engine-eval-example.md` before implementation.

If the task is UI, HUD, menu, settings, onboarding, or template-shaped, also read `docs/reference/ui-guide.md` and `docs/examples/ui-example.md` before implementation.

If the task is audio, animation, timing, or presentation shaped, also read `docs/reference/audio-animation-guide.md` and `docs/examples/audio-animation-example.md` before implementation.

If the task is GPU, buffer, instancing, render scale, or CPU-GPU communication shaped, also read `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` before implementation.

If the task is about source art, imported assets, shared tuning, or loading boundaries, also read `docs/reference/asset-guide.md` and `docs/examples/asset-example.md` before implementation.

If the task is specifically about FPS, frame time, memory, or scale, read `docs/reference/perf-guide.md` and `docs/examples/perf-example.md` before chasing a micro-optimization. If the bottleneck is genre-shaped, add `docs/reference/genre-perf-guide.md` and `docs/examples/genre-perf-example.md` too. If the real question is culling, batching, instancing, job systems, or state compression, add `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` as well.

If the task is specifically about choosing a library, package, plugin, or SDK for a case, read `docs/reference/library-guide.md` and `docs/examples/library-example.md` before implementation.

If the task is specifically about asset ownership, import rules, compression, or streaming boundaries, read `docs/reference/asset-guide.md` and `docs/examples/asset-example.md` before implementation.

If you want the shortest cross-engine ownership summary, start with `docs/reference/engine-map.md` and then open `docs/reference/engine-atlas.md` for the deeper class-family breakdown before the matching mini atlas and deep dive note.
If the task is a bug, crash, or troubleshooting pass, read `docs/reference/engine-bugs.md` and `docs/examples/engine-bugs-example.md` before implementation so the symptom family and first debug surface are explicit.
