# Game Architecture Research

## Recommended starting notes
- `docs/reference/architecture-guide.md` for the quick owner/boundary diagrams
- `docs/examples/architecture-example.md`
- `authority.md`
- `events.md`
- `state.md`
- `projection.md`

## What belongs here
- Repo-level architecture patterns that decide who owns truth, how systems talk, how state changes, and how runtime data reaches UI or saves.
- Use these notes when a task is no longer about one mechanic, but about the shape of the whole gameplay system.
- Use the guide diagrams first when you need the smallest possible owner/boundary map before choosing a deeper note.

## Reading order
1. Start with `authority.md` if the task needs a single source of truth.
2. Read `state.md` if the task has phase flow, state graphs, or mode switching.
3. Read `events.md` if the task needs decoupled gameplay or UI notifications.
4. Read `projection.md` if the task needs runtime-to-UI, runtime-to-save, or runtime-to-network mapping.

## Validation rule
- Every architecture task should name the owner, the boundary, the failure mode, and the smallest validation loop before implementation starts.
