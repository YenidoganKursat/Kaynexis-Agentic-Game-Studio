# Golden Example — Handoff Contract

## Scope
- Hand off the first Unreal starter-kit packaging slice after the command contract and docs were updated

## Evidence
- `scripts/unreal_adapter.py --dry-run --json` returns a valid `BuildCookRun` command
- `studio/starter-kits/unreal-5/kit.toml` lists the same packaging expectation
- `studio/docs/active/build-pipeline.md` was updated with the command shape

## Risks
- Real local `UNREAL_UAT` path is still external to the repo
- Win64 packaging has command coverage, not full editor-backed CI yet

## Validation
- Completed:
  - contract smoke
  - starter-kit validation
- Next:
  - run with a real local UAT path
  - capture artifact output path

## Owner
- Current owner: build/release engineer
- Receiving owner: maintainer with local Unreal install

## Blockers
- No real Unreal installation path configured in `studio.toml`

## Next step
- Configure `UNREAL_UAT`, run one real Win64 package attempt, and record the artifact path in `studio/docs/active/build-pipeline.md`
