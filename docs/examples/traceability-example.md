# Traceability Example

## Feature brief
- Path: `studio/docs/active/feature-core-movement.md`
- Status: Approved for implementation

## Atlas references
- `docs/reference/system-atlas.md`
- `docs/reference/engine-atlas.md`
- `docs/reference/engine-map.md`

## Architecture decision
- Path: `studio/docs/active/adr-core-movement-state-split.md`
- Status: Approved

## Touched implementation paths
- Code: `src/player.gd`, `src/telemetry.gd`
- Content: `studio/docs/active/feature-core-movement.md`
- Data: `studio/docs/active/telemetry-schema.md`

## Validation surface
- Test plan / QA matrix: `studio/docs/active/test-plan-core-movement.md`
- Smoke path: launch room, move, dash, observe telemetry event
- Known gaps: no save migration, no network sync

## Release impact
- Release note / checklist path: `studio/docs/active/release-checklist.md`
- Telemetry or analytics impact: movement event emitted on dash
- Rollback or hotfix note: safe to disable telemetry hook without changing movement logic
