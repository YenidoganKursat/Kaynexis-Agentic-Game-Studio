# Engine Selection Guide

This repo supports three engine families at the studio-OS level:

- `godot-4`
- `unity-6`
- `unreal-5`

That does not mean the runtime files are identical. It means the repo gives all three engines:

- starter-kit manifests
- adapter commands
- checklist coverage
- research notes
- CI contract smoke
- user-facing setup and routing support

If your real concern is FPS, frame time, memory, or scale, pair the engine choice with `docs/reference/perf-guide.md` and `docs/reference/genre-perf-guide.md` before you commit to a representation path.
If the real concern is algorithmic scale - spatial partitioning, culling, batching, instancing, job systems, or state compression - also add `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` before you commit to a representation path.
If the real concern is GPU ownership, render communication, buffer shape, or repeated-visual scale, also add `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` before you commit to a render path.
If the real concern is how the engines compare on build, tests, performance, and toolchain readiness, also add `docs/reference/engine-eval.md` and `docs/examples/engine-eval-example.md` before you commit to an engine choice.
If the real concern is which engine fits a specific developer profile or team shape, also add `docs/reference/engine-fit.md` and `docs/examples/engine-fit-example.md` before you commit to an engine choice.
If the real concern is how to install the engine cleanly on a new machine, also add `docs/setup/engine-installation.md` before you commit to an install path.

If your real concern is which library, package, plugin, or SDK should own the case, pair the engine choice with `docs/reference/library-guide.md` and `docs/examples/library-example.md` before you commit to a dependency path.
If your real concern is code quality, maintainability, refactor safety, or optimization criteria, pair the engine choice with `docs/reference/quality-guide.md` and `docs/examples/quality-example.md` before you commit to a refactor path.

## Pick Godot 4 when

- you want the fastest path from idea to playable reference slice
- you prefer a scene-and-script workflow
- you want a lighter-weight baseline for small teams or solo development
- you want the current runtime reference in `src/` to stay close to your real game

Good fits:

- action prototypes
- puzzle games
- 2D-heavy projects
- short iteration loops

What this repo gives you for Godot:

- a real reference slice in `src/`
- static smoke and export helper scripts
- Godot-specific research and checklist coverage
- a class/mechanic guide that maps common 2D and 3D work onto `CharacterBody`, `Area`, `RigidBody`, `Camera`, `AnimationTree`, `PackedScene`, and `Resource`
- a GPU guide that maps CPU-GPU ownership, buffers, instancing, compute, and readback decisions onto the supported engines
- concrete example slices and cross-engine comparisons in `docs/reference/engine-examples.md`

Commands:

```bash
python3 scripts/codex_studio.py init --engine godot-4 --yes
python3 scripts/godot_smoke.py --static-only
python3 scripts/godot_export.py --preset "Linux/X11"
```

## Pick Unity 6 when

- you want package and assembly-definition boundaries from the start
- you expect more editor tooling, mobile/web build considerations, or plugin ecosystem usage
- you want a strong separation between runtime, editor, and test surfaces
- your team already thinks in `GameObject`, `Component`, `Prefab`, and `ScriptableObject`

Good fits:

- tactical projects
- systems-heavy mid-scale projects
- multi-platform indies
- content pipelines that benefit from editor tools

What this repo gives you for Unity:

- a starter kit with package and asmdef structure
- runtime, editor, prefab, and ScriptableObject sample surface under the Unity scaffold
- adapter commands for test/build contract smoke
- Unity-specific performance, navigation, and object-model research
- a class/mechanic guide that maps common 2D and 3D work onto `CharacterController`, `Rigidbody`, colliders/triggers, `Animator`, Prefabs, pooling, and `ScriptableObject`
- concrete example slices and cross-engine comparisons in `docs/reference/engine-examples.md`

Commands:

```bash
python3 scripts/codex_studio.py init --engine unity-6 --yes
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --dry-run --json
```

If a local Unity editor is not auto-detected, add `--unity-path tools/engine-stubs/unity/Unity` and treat the result as contract smoke rather than release-grade validation.

## Pick Unreal 5 when

- you want to think in modules, gameplay framework, packaging, and larger-scale 3D systems early
- you expect deeper use of Unreal-native architecture like Actors, Components, Blueprints, StateTree, EQS, GAS, or Mass
- you want a pipeline that grows toward more formal packaging and platform delivery

Good fits:

- co-op survival
- extraction-lite
- heavier 3D combat
- more production-heavy projects with strong engine conventions

What this repo gives you for Unreal:

- a starter kit with project/module/package contract
- gameplay framework, component, config, and content sample surface under the Unreal scaffold
- adapter commands for package contract smoke
- Unreal-specific research on architecture, object model, navigation, damage, and scale
- a class/mechanic guide that maps common 2D and 3D work onto `Character`, `Pawn`, `Actor`, `Component`, Data Asset, Blueprint, collision primitives, and GAS boundaries
- concrete example slices and cross-engine comparisons in `docs/reference/engine-examples.md`

Commands:

```bash
python3 scripts/codex_studio.py init --engine unreal-5 --yes
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path tools/engine-stubs/unreal/RunUAT.sh \
  --dry-run --json
```

## Quick decision table

| If you care most about... | Best default |
| --- | --- |
| fastest path to a playable reference slice | `godot-4` |
| editor tooling and package boundaries | `unity-6` |
| deeper 3D framework and packaging shape | `unreal-5` |
| smallest contributor setup burden | `godot-4` |
| stronger built-in content and editor workflow culture | `unity-6` |
| Unreal-native gameplay framework and large-system planning | `unreal-5` |

## What “support” means in this repo

Support is layered:

1. `studio.toml` supports engine selection
2. `codex_studio.py` understands the selected engine
3. starter-kit manifests define the contract
4. adapters expose test/build/package command surfaces
5. checklists enforce engine-specific rules
6. research notes explain how to design correctly for that engine
7. CI runs contract smoke for all supported engines

For each engine, the research stack explicitly includes:

- architecture baseline
- class/editor/object ownership
- 2D/3D class and mechanic guidance
- navigation, damage, and performance guidance

## What support does not mean

Support does not mean:

- all three engines share one runtime codebase
- all three engines have equal gameplay sample depth
- dry-run adapter output is the same thing as a real editor-backed build

Right now:

- the shared system supports all three engines
- the current reference runtime in `src/` is Godot-based
- Unity and Unreal runtime examples live under their starter-kit scaffolds

## Local machine setup

You only need the engine you actually plan to use locally.

If you are still choosing the install path, start with `docs/setup/engine-installation.md` and then set the local path variables below.

Optional local paths:

- `GODOT_BIN`
- `UNITY_CLI`
- `UNREAL_EDITOR`
- `UNREAL_UAT`

Put them in `.env` for local overrides or `studio.toml` for durable team defaults.

## If you need to switch engines later

Do this deliberately:

1. update `studio.toml`
2. re-run `python3 scripts/codex_studio.py init --engine <new-engine> --overwrite`
3. re-check `studio/docs/active/engine-profile.md`
4. re-route the next task
5. run the new engine’s contract smoke path

Do not silently switch engines only in docs or only in runtime files.

If you need concrete examples before you decide, read `docs/reference/engine-examples.md` and compare the same mechanic in each engine family.
If you need a build / test / performance scorecard before you decide, read `docs/reference/engine-eval.md` and `docs/examples/engine-eval-example.md` alongside the engine selection guide.
If you need a developer-fit matrix before you decide, read `docs/reference/engine-fit.md` and `docs/examples/engine-fit-example.md` alongside the engine selection guide.
If you need concrete optimization examples before you decide, read `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` alongside the engine performance notes.
