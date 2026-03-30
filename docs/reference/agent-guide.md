# Agent Guide

This guide tells Codex-facing agents how to use the engine knowledge base in this repo before making engine-specific recommendations or patches.

For the fastest possible lookup, also use `docs/reference/engine-map.md` as the first pass when you need a compact cross-engine ownership summary.
For a broad "what can this repo do?" or capability-overview request, also start with `docs/reference/capabilities.md` and `docs/examples/capabilities-example.md` so the answer stays simple before it fans out.
For a deeper class-by-class ownership pass, use `docs/reference/engine-atlas.md`, then the matching engine mini atlas.
For system-heavy work, pair that with `docs/reference/system-atlas.md` so the agent can jump from system ownership to concrete snippets.
For recurring engine bugs, common errors, or troubleshooting tasks, add `docs/reference/engine-bugs.md` and `docs/examples/engine-bugs-example.md` before implementation so the symptom family, first debug surface, and runtime/editor boundary stay explicit.
For the whole multi-agent operating model, use `docs/reference/agent-system.md` and `docs/examples/agent-system-example.md` so the controller title, single-specialist default, role matrix, hierarchy, and review trail stay aligned.
For a fresh machine or new clone, use `docs/setup/agent-setup.md` so the Codex CLI, controller title, single-specialist default, and multi-agent rules stay grounded in one install path.
For OpenAI/Codex or agent-platform work, also add `docs/research/openai-codex-infra-findings.md`, `docs/research/openai-codex-models.md`, `docs/reference/codex-compatibility.md`, and `docs/reference/codex-model-guide.md` so prompt policy, evals, tool-access assumptions, and model-fit assumptions stay explicit.
If the work is specifically about model choice or plan-tier fit, also add `docs/examples/codex-model-guide-example.md`, `studio/checklists/discipline/openai_models.toml`, and `studio/docs/active/eval-openai-models.md` so the model ladder, plan fit, and proof path stay durable.
If the task fans out into specialists, let the user override lane models explicitly with `--agent-model agent=model` so the default profile and the per-lane tradeoff both stay visible.
For broad, cross-functional work, also use `docs/reference/mastermind-guide.md` and `docs/examples/mastermind-example.md` so the user-facing summary stays simple while specialist handoffs stay explicit.
For broad orchestration work, add `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, `docs/examples/mastermind-example.md`, and `docs/examples/agent-portfolio-example.md` before implementation so the control loop, role matrix, handoffs, and validation path stay explicit.
Keep single specialist mode available in every portfolio decision; panel mode is optional, not a replacement.
If the work needs proof that a single specialist, pair, or panel was the right operating choice, also add `docs/reference/agent-validation-matrix.md` and `docs/examples/agent-validation-matrix-example.md` so the proof rows stay separate from prompt history and transcripts.
If the work needs titles, reporting lines, or async packets, also add `docs/reference/agent-hierarchy.md` and `docs/examples/agent-hierarchy-example.md`.
The public title layer uses `Kaynexis` for the controller and scientist names for specialist lanes; keep the internal role ids stable and use the mapped aliases in summaries, command trees, and route output.
If the work should remain reviewable later, also add `docs/reference/prompt-journal.md` and `docs/examples/prompt-journal-example.md` so the prompt history and agent step notes stay append-only.
If the work includes agent-to-agent assignment history or conversation turns, also add `docs/reference/agent-transcript.md` and `docs/examples/agent-transcript-example.md` so the transcript stays separate from prompt history.
For performance work, add `docs/reference/perf-guide.md` and `docs/examples/perf-example.md` before implementation so the first lever, baseline, and fallback path are explicit.
For genre-shaped performance work, add `docs/reference/genre-perf-guide.md` and `docs/examples/genre-perf-example.md` before implementation so the genre family, first lever, and fallback path are explicit.
For advanced optimization work, add `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` before implementation so the algorithm family, first lever, and fallback path are explicit.
For benchmark or measurement work, add `docs/reference/benchmark-guide.md` and `docs/examples/benchmark-example.md` before implementation so the family, baseline, metric, threshold, and artifact are explicit.
For versioning work, add `docs/reference/version-guide.md`, `docs/examples/version-example.md`, and `docs/research/game-development/production/versioning.md` before implementation so the canonical version file, changelog sync, and tag policy are explicit.
For release hardening or protected multiplayer builds, add `docs/reference/release-hardening-guide.md`, `docs/examples/release-hardening-example.md`, and `docs/research/game-development/production/release-hardening.md` before implementation so code protection, symbol policy, trust boundaries, and rollback evidence stay explicit.
For sector intelligence or current-industry work, add `docs/reference/sector-intel.md`, `docs/examples/sector-intel-example.md`, and `docs/research/game-development/production/sector-intel.md` before implementation so the source hierarchy, current window, and signal-to-implication shape are explicit.
For Steam store, wishlist, forum, or hardware intelligence work, add `docs/reference/steam-intel.md`, `docs/examples/steam-intel-example.md`, and `docs/research/game-development/production/steam-intel.md` before implementation so the source hierarchy, current window, signal split, and chart pack are explicit.
For platform compatibility across Windows, macOS, Linux/Steam Deck, web, Android/iOS, or TV/webOS families, add `docs/reference/platform-guide.md`, `docs/examples/platform-example.md`, and `docs/research/game-development/production/platform-compatibility.md` before implementation so the family split, input model, performance envelope, and policy constraints are explicit.
For PS5-like or other console-premium work, add `docs/reference/console-guide.md`, `docs/examples/console-example.md`, and `docs/research/game-development/production/console.md` before implementation so controller-first UX, suspend/resume, save / entitlement, and submission gates stay explicit.
If the work is specifically about support tiers, release sequencing, or which families are core, supported, demo-only, research-only, or deferred, also add `docs/reference/cross-platform-guide.md`, `docs/examples/cross-platform-example.md`, and `docs/research/game-development/production/cross-platform.md` before implementation so the support-strategy layer stays explicit.
For marketing strategy or campaign evaluation, add `docs/reference/marketing-guide.md`, `docs/examples/marketing-example.md`, and `docs/research/game-development/production/marketing.md` before implementation so the audience, channel fit, measurement path, and policy constraints are explicit. If the task is only a short announce/demo/update beat, use the `storefront-launch` and `marketing-beat-brief` skills instead so the work stays at the beat level.
For genre pattern work, add `docs/research/game-development/genre/genre-guide.md`, `docs/research/game-development/genre/genre-patterns.md`, and `docs/research/game-development/genre/genre-examples.md` before implementation so the dominant tension, software pattern family, and contrast set are explicit. If you need a broader contrast set, also add `docs/examples/genre-gallery-example.md`.
For genre planning work, add `docs/reference/genre-plan.md` and `docs/examples/genre-plan-example.md` before implementation so the player outcome, dominant tension, contrast set, loop ladder, state owner, accessibility envelope, and validation ladder are explicit.
For GPU / rendering / communication work, add `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` before implementation so the CPU owner, GPU owner, upload path, readback policy, and first lever are explicit.
For UI work, add `docs/reference/ui-guide.md` and `docs/examples/ui-example.md` before implementation so the screen owner, projection boundary, focus model, and template source are explicit.
For audio and animation work, add `docs/reference/audio-animation-guide.md` and `docs/examples/audio-animation-example.md` before implementation so the playback owner, timing owner, gameplay owner, and sync path are explicit.
For quality and optimization-criteria work, add `docs/reference/quality-guide.md`, `docs/reference/quality-process.md`, `docs/examples/quality-example.md`, and `docs/examples/quality-process-example.md` before implementation so the ownership model, control loop, validation path, and first lever are explicit.
For theory stacks or design-lens work, add `docs/reference/theory-guide.md`, `docs/examples/theory-example.md`, and `docs/research/game-development/foundations/theory.md` before implementation so the player outcome, lens stack, evidence path, and first failure mode are explicit.
For architecture-heavy work, add `docs/reference/architecture-guide.md` and `docs/examples/architecture-example.md` before implementation so the canonical owner, boundary, proof path, and diagram shape are explicit.
For reusable custom packs or project-specific feature registries, also add `docs/reference/custom-packs.md` and `docs/examples/custom-packs-example.md` before implementation so the registry entry, fixed rules, hook points, fallback, and validation path stay explicit.
For custom architecture or request-rule pack work, also add `docs/reference/custom-architecture.md` and `docs/examples/custom-architecture-example.md` so fixed versus overrideable rules, precedence, and fallback stay explicit.
For optional extension packs or plugin-like add-ons, also add `docs/reference/extensions-guide.md` and `docs/examples/extensions-example.md` so the manifest, hook points, override points, and fallback stay explicit.
For library or package selection, add `docs/reference/library-guide.md` and `docs/examples/library-example.md` before implementation so the built-in option, official package, and fallback path are explicit.
For asset-heavy work, add `docs/reference/asset-guide.md` and `docs/examples/asset-example.md` before implementation so the source asset, runtime owner, import boundary, and validation path are explicit.

## Required read order

When a task is engine-specific, the agent should read in this order:

1. `studio/docs/active/engine-profile.md`
2. The engine architecture baseline in `docs/research/game-development/engines/`
3. The matching engine class/editor/object map in `docs/research/game-development/engines/`
4. `docs/reference/engine-atlas.md` for the core class and object family breakdown
5. `docs/reference/engine-bugs.md` and `docs/examples/engine-bugs-example.md` for recurring engine bug families and first checks
6. `docs/reference/godot-atlas.md`, `docs/reference/unity-atlas.md`, or `docs/reference/unreal-atlas.md`
7. `docs/reference/system-atlas.md` for cross-system ownership
8. The matching 2D/3D class and mechanic guide in `docs/research/game-development/engines/`
9. `docs/reference/ui-guide.md` and `docs/examples/ui-example.md` when the task is about HUDs, menus, settings, or template selection
10. The matching 2D/3D, navigation, damage, and performance note in `docs/research/game-development/engines/`
11. `docs/reference/benchmark-guide.md` and `docs/examples/benchmark-example.md` when the task is benchmark-shaped or needs a measurement harness
12. The matching advanced performance guide or example when the task is about culling, partitioning, batching, instancing, or job systems
13. The matching GPU guide and example when the task is about GPU, render, buffer, or CPU-GPU communication shape
14. The matching library guide or example when the task is about packages, plugins, or SDK choice
15. The matching systems playbook in `docs/research/game-development/engines/`
16. The matching audio and animation presentation playbook in `docs/research/game-development/engines/`
17. The matching visuals, images, and animation playbook in `docs/research/game-development/engines/`
18. The matching engine checklist in `studio/checklists/engine/`
19. The relevant active docs such as `build-pipeline.md`, `current-sprint.md`, or `content-pipeline.md`

For performance tasks, insert `docs/reference/perf-guide.md` and `docs/examples/perf-example.md` before implementation, then inspect the matching engine performance note. If the agent cannot name the baseline, the target hardware, and the first lever, it should not start optimizing yet.
If the task is genre-shaped, insert `docs/reference/genre-plan.md`, `docs/examples/genre-plan-example.md`, `docs/examples/genre-gallery-example.md`, `docs/reference/genre-perf-guide.md`, and `docs/examples/genre-perf-example.md` as well, then inspect the matching engine performance note. If the agent cannot name the genre family, the player outcome, the baseline, the target hardware, and the first lever, it should not start optimizing yet.
If the task is advanced-algorithm shaped, insert `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` as well, then inspect the matching engine performance note. If the agent cannot name the algorithm family, the baseline, the target hardware, and the first lever, it should not start optimizing yet.
If the task is benchmark-shaped, insert `docs/reference/benchmark-guide.md` and `docs/examples/benchmark-example.md` as well, then inspect `docs/research/game-development/foundations/benchmarks.md` and `docs/reference/eval-strategy.md`. If the agent cannot name the family, baseline, metric, threshold, and artifact, it should not start benchmarking yet.
If the task is GPU-shaped, insert `docs/reference/gpu-guide.md` and `docs/examples/gpu-example.md` as well, then inspect the matching engine GPU note. If the agent cannot name the CPU owner, the GPU owner, the upload path, the readback policy, and the first lever, it should not start implementing yet.
If the task is about a library, package, plugin, or SDK choice, insert `docs/reference/library-guide.md` and `docs/examples/library-example.md` as well, then inspect the matching engine or package docs. If the agent cannot name the case, the built-in option, and the chosen library boundary, it should not start implementing yet.
If the task is architecture-heavy, insert `docs/reference/architecture-guide.md` and `docs/examples/architecture-example.md` as well, then inspect the matching architecture research notes and diagrams. The matching architecture checklist now expects the diagram-aware owner/boundary proof path, so if the agent cannot name the canonical owner, the boundary, the state or event path, and the proof loop, it should not start implementing yet. If the task is custom architecture or request-rule-pack heavy, add `docs/reference/custom-architecture.md` and `docs/examples/custom-architecture-example.md` in the same pass so fixed versus overrideable rules stay reviewable. If the task is about optional add-ons, hook packs, or plugin-like capabilities, add `docs/reference/extensions-guide.md` and `docs/examples/extensions-example.md` in the same pass so the manifest and fallback stay reviewable.

If the task is broad or cross-functional, insert `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, `docs/examples/mastermind-example.md`, `docs/examples/agent-portfolio-example.md`, `docs/reference/agent-hierarchy.md`, and `docs/examples/agent-hierarchy-example.md` as well, then keep the user-facing summary simple while you map the specialist handoffs. Single specialist mode should still remain a valid output of that review. If the agent cannot name the control loop, the specialist roles, and the narrow validation path, it should not start implementation yet.

When a task is system-specific, add the matching systems note before implementation:

- inventory, loot, equipment, quick bar, or loadout -> `docs/research/game-development/systems/inventory.md`
- avatar, player controller, locomotion, dash, jump, or ability boundary -> `docs/research/game-development/systems/character.md`
- enemy, boss, patrol, aggro, perception, or encounter behavior -> `docs/research/game-development/systems/enemy.md`
- input, controller support, remapping, pause, or camera -> `docs/research/game-development/systems/input.md`
- HUD, menu, settings, pause flow, inventory screen, or onboarding UI -> `docs/research/game-development/systems/ui.md`
- HUD, menu, settings, pause flow, inventory screen, onboarding UI, or template selection -> `docs/reference/ui-guide.md` and `docs/examples/ui-example.md`
- abilities, upgrades, perks, skill trees, cooldowns, or build variety -> `docs/research/game-development/systems/skills.md`
- interactables, pickups, prompts, levers, chests, or world objects -> `docs/research/game-development/systems/interactions.md`
- persistence or progression interaction -> `docs/research/game-development/systems/save.md`
- lorebook, codex, canon, archive, or unlockable world knowledge -> `docs/reference/lorebook-methodology.md` and `docs/research/game-development/narrative/lorebook.md`
- world graph, faction network, history network, lineage, or organization graph -> `docs/reference/world-graph-methodology.md` and `docs/research/game-development/narrative/world-graph.md`
- asset, asset pipeline, source art, import, compression, or runtime-vs-authoring asset ownership -> `docs/reference/asset-guide.md` and `docs/examples/asset-example.md`
- state, authority, events, projection, or runtime-to-save mapping -> `docs/reference/architecture-guide.md` (diagrams) and `docs/examples/architecture-example.md`

## Engine-specific knowledge index

### Godot 4
- Architecture: `docs/research/game-development/engines/godot.md`
- Class/editor/object map: `docs/research/game-development/engines/godot-map.md`
- Common classes/mechanics: `docs/research/game-development/engines/godot-classes.md`
- Systems/performance: `docs/research/game-development/engines/godot-performance.md`
- UI: `docs/research/game-development/engines/godot-ui.md`
- Presentation: `docs/research/game-development/engines/godot-presentation.md`
- Visuals/animation: `docs/research/game-development/engines/godot-visuals.md`
- Checklist: `studio/checklists/engine/godot-4.toml`

### Unity 6
- Architecture: `docs/research/game-development/engines/unity.md`
- Class/editor/object map: `docs/research/game-development/engines/unity-map.md`
- Common classes/mechanics: `docs/research/game-development/engines/unity-classes.md`
- Systems/performance: `docs/research/game-development/engines/unity-performance.md`
- UI: `docs/research/game-development/engines/unity-ui.md`
- Presentation: `docs/research/game-development/engines/unity-presentation.md`
- Visuals/animation: `docs/research/game-development/engines/unity-visuals.md`
- Checklist: `studio/checklists/engine/unity-6.toml`

### Unreal 5
- Architecture: `docs/research/game-development/engines/unreal.md`
- Class/editor/object map: `docs/research/game-development/engines/unreal-map.md`
- Common classes/mechanics: `docs/research/game-development/engines/unreal-classes.md`
- Systems/performance: `docs/research/game-development/engines/unreal-performance.md`
- UI: `docs/research/game-development/engines/unreal-ui.md`
- Presentation: `docs/research/game-development/engines/unreal-presentation.md`
- Visuals/animation: `docs/research/game-development/engines/unreal-visuals.md`
- Checklist: `studio/checklists/engine/unreal-5.toml`

## Shared rules for all engine-specialized agents

- Do not start from generic engine memory when the repo has a matching research note. Read the repo note first.
- State the ownership model before implementation:
  - what is the runtime unit
  - what is the reusable data unit
  - what is the editor-facing unit
  - what is the validation loop
- For system-heavy gameplay work, also state:
  - what world stack is in charge: `2D`, `3D`, or limited hybrid
  - which engine-native classes or object families own movement, contact, camera, animation, and authored data
  - what navigation model is in charge: native navmesh/server stack versus explicit graph/grid
  - what damage/contact model is in charge: overlaps, collision callbacks, direct queries, or ability/effect framework
  - what scale lever is in charge: ordinary authored objects versus instancing, pooling, servers, DOTS, or Mass
- For architecture work, also state:
  - the canonical owner
  - the event source and listener set if events are involved
  - the state graph and legal transitions if phases matter
  - the projection targets if UI, save, telemetry, or network are involved
  - the narrow proof path that shows the boundary holds
- For genre work, also state:
  - the dominant tension
  - the chosen software pattern family
  - the contrast set or example games
  - the first slice that proves the genre
  - the first system that breaks if the genre is shallow
- For controls, UI, inventory, abilities, and save work, also state:
  - what input owner is in charge: engine action maps, input assets, or a bespoke remap layer
  - what UI owner is in charge: HUD widgets, menu screens, editor windows, or overlay canvases
  - what authored-data owner is in charge: `Resource`, `ScriptableObject`, `Data Asset`, or another shared asset type
  - what persistence owner is in charge: live object state versus save projection versus meta progression
- For GPU / render-scale work, also state:
  - what CPU owner is in charge
  - what GPU owner is in charge
  - what buffer shape and update cadence are in charge
  - what readback policy is in charge
  - what first lever is in charge
- For inventory tasks, explicitly separate:
  - item definition data
  - runtime slot or stack state
  - equipment or loadout state
  - UI projection
  - persistence projection
- For character tasks, explicitly separate:
  - input interpretation
  - locomotion authority
  - combat or ability authority
  - animation/presentation authority
  - camera/targeting authority
  - persistence/data authority
- For enemy tasks, explicitly separate:
  - archetype data
  - sensing/perception
  - navigation or locomotion
  - decision model
  - action execution
  - encounter role
- For control tasks, explicitly separate:
  - physical device input
  - action mapping
  - gameplay consumers
  - UI consumers
  - camera response
  - remap persistence
- For UI tasks, explicitly separate:
  - screen or HUD state
  - projected gameplay data
  - focus/navigation behavior
  - blocked gameplay state
  - copy/accessibility expectations
- For visuals, image, sprite, animation, texture, or VFX tasks, explicitly separate:
  - source art or texture asset
  - world versus UI presentation
  - animation playback owner
  - particle or VFX owner
  - material or shader owner
  - runtime projection versus authored data
- For audio and animation tasks, explicitly separate:
  - playback owner
  - timing or sync owner
  - gameplay owner
  - simple playback path versus advanced routing path
- For class-atlas work, explicitly separate:
  - runtime owner
  - shared data owner
  - editor owner
  - mechanic input
  - mechanic output
  - validation loop
- For docs, examples, presets, or rename work, keep the short canonical name visible and check `studio/checklists/base/naming.toml` before broadening the change.
- For build, release, workflow, or artifact naming work, keep workflow names, job labels, artifact labels, and report filenames short and canonical; the CI short-name rule lives in `studio/checklists/base/naming.toml` and the build-release checklist, and release bundles should surface that same rule instead of inventing a separate naming style.
- For versioning work, treat `VERSION`, `CHANGELOG.md`, release tags, commit notes, and artifact labels as one contract; prerelease suffixes should stay visible until the tag is actually cut, and versioning commits should say what changed in the subject or body.
- For ability and upgrade tasks, explicitly separate:
  - authored definition data
  - current-run granted state
  - durable progression state
  - cooldown or charge owner
  - UI projection
- For interaction tasks, explicitly separate:
  - candidate selection
  - validation rule
  - world mutation
  - reward or inventory projection
  - persistence expectation
- Keep runtime code and editor-only code conceptually separate.
- Prefer the engine's native composition model over forcing the same pattern across all three engines.
- When a feature affects designer iteration, explain which editor surface is used and what the operator will see there.

## Godot-specific operating rules

- Inspect the scene tree before touching node paths, signals, or groups.
- Distinguish scene reuse from data reuse:
  - reusable hierarchy -> scene / `PackedScene`
  - shared authored data -> `Resource`
- For 2D/3D system work, explicitly choose between NavigationServer-driven movement and custom `AStarGrid2D` / `AStar3D` graphs.
- For hit or damage systems, say whether authored areas, collision callbacks, or direct space-state queries own contact detection.
- For high-entity counts, say when the feature should stay node-based and when it should move toward `MultiMesh` or lower-level server APIs.
- Use `@tool` only when the editor itself must react live.
- If the task is editor tooling, say whether it should be a tool script, an inspector plugin, or a dock/plugin.

## Unity-specific operating rules

- Distinguish container, behavior, and data:
  - container -> `GameObject`
  - behavior -> Component / `MonoBehaviour`
  - shared authored data -> `ScriptableObject`
- Prefer prefabs for repeated hierarchies and spawnable authored objects.
- For 2D/3D system work, explicitly choose between built-in 2D, built-in 3D, and data-oriented runtime paths.
- For nav and sensing systems, say whether AI Navigation, a custom graph/grid, or a DOTS-oriented solution is responsible.
- For damage and combat queries, say how layers, triggers/collisions, non-alloc queries, and pooling are used to avoid hidden cost.
- Keep `UnityEditor` usage inside editor-only code.
- Choose the editor surface deliberately:
  - object-specific editing -> custom `Editor`
  - workflow/tool window -> `EditorWindow`

## Unreal-specific operating rules

- Distinguish object, world entity, and reusable behavior:
  - reflected/supporting object -> `UObject`
  - placeable/spawned world thing -> `AActor`
  - reusable sub-behavior -> Component
- State whether a value should be edited in C++, Blueprint defaults, or the Details panel.
- For 2D/3D system work, explicitly choose between Paper2D, standard 3D gameplay framework, or a constrained hybrid.
- For AI and traversal, say whether navmesh, EQS, StateTree, or a justified custom graph owns the problem.
- For combat systems, say whether simple damage or the Gameplay Ability System owns attributes, abilities, and effect flow.
- For high-scale representations, say whether the feature should remain Actor-based or move toward instancing or Mass.
- Prefer PIE/SIE and Blueprint compile loops as the first validation path for gameplay/editor changes.
- Avoid hard-coded asset ownership when the task is clearly designer-facing.

## What every engine-aware recommendation should include

1. Current engine evidence from the repo
2. The chosen ownership model
3. The chosen world stack and system model for gameplay-heavy work
4. The editor surface involved, if any
5. The narrowest validation loop
6. The main risk if the change grows
