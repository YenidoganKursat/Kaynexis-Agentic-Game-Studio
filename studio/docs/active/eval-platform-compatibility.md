# Eval Plan — Platform Compatibility

## Change under test
- Platform compatibility research, guide, example, and checklist routing for desktop, Steam, web, mobile, and TV families.
- Cross-platform support-tier guidance, support-sequence docs, and release-order matrices for the same families.

## Goal
- Confirm that platform tasks surface family-by-family deltas, support tiers, official sources, and a simple dashboard or matrix schema.

## Risks
- Routes may collapse into generic porting or release work.
- The guide may overfit to one family and hide the others.
- Support tiers may collapse back into a single compatibility label.
- Validation may stay generic instead of proving the family split.

## Validation
- Run `python3 scripts/route_task.py` on a platform-compatibility prompt and confirm the route and docs.
- Run `python3 scripts/codex_studio.py checklist --task "..." --json` and confirm the `platform_compatibility` discipline appears.
- Run `python3 scripts/validate_docs.py --strict`.
- Run `python3 scripts/validate_repo_layout.py`.

## Success criteria
- The platform guide, cross-platform guide, example, and research notes all exist and are linked from the entry docs.
- The route outputs `Kaynexis` plus the specialist lane set.
- The checklist includes the platform compatibility items, support-tier items, and the support layers that keep release risk visible.
