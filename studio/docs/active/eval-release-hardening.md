# Eval — Release Hardening

## Change under test
- New release-hardening lane, including code protection, build integrity, and multiplayer trust guidance.

## Goal
- Prove that release-hardening tasks route to the right docs, checklist, and validation path without losing the build/release lane.

## Risks
- Code protection could be mistaken for a real security boundary.
- Multiplayer trust could drift if the guide does not state authority and dedicated-server assumptions clearly.
- Release docs could diverge if the hardening lane is not kept in sync with the build pipeline note.

## Validation
- `python3 scripts/route_task.py "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split" --json`
- `python3 scripts/codex_studio.py checklist --task "Harden a Unity 6 co-op build with managed stripping, symbol policy, and a dedicated server split" --json`
- `python3 scripts/validate_docs.py --strict`
- `python3 scripts/validate_repo_layout.py`

## Success criteria
- The route returns a dedicated release-hardening lane.
- The checklist includes build integrity, code protection, trust boundary, symbol policy, and smoke items.
- The guide, example, research note, checklist, and template all stay aligned.
