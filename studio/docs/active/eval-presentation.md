# Eval Plan: Presentation Routing

## Goal
- Verify that audio and animation work routes through the new presentation guidance, checklist, and examples without losing the current visuals or content-pipeline behavior.

## Scope
- `scripts/route_task.py`
- `scripts/studio_core.py`
- `studio/checklists/discipline/presentation.toml`
- `docs/reference/audio-animation-guide.md`
- `docs/examples/audio-animation-example.md`
- `docs/research/game-development/engines/godot-presentation.md`
- `docs/research/game-development/engines/unity-presentation.md`
- `docs/research/game-development/engines/unreal-presentation.md`

## Cases
- A task about a Godot boss windup should surface the presentation guide and the Godot presentation note.
- A task about a Unity UI confirm sound plus animation should surface the presentation checklist and Unity presentation note.
- A task about an Unreal telegraph should surface the presentation guide, the presentation checklist, and the Unreal presentation note.

## Pass criteria
- The route name is stable and explicit.
- The checklist includes presentation ownership, presentation tier, sync, evidence, and doc-sync items.
- The docs and example are linked from the task, the route output, and the repo docs indexes.

## Validation
- `python3 scripts/route_task.py "<presentation task>" --json`
- `python3 scripts/codex_studio.py checklist --task "<presentation task>" --json`
- `python3 scripts/validate_docs.py`
- `python3 scripts/run_local_evals.py --json`
