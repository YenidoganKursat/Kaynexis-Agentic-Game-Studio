# Current Sprint — Codex Game Studio Pro Max

## Sprint goal
- Prove the first playable slice around `First Combat Room`

## In scope
- Confirm engine and repo layout decisions
- Confirm `studio.toml`, starter-kit, and checklist assumptions
- Harden the Godot reference slice so it stays trustworthy
- Keep Unity and Unreal support honest at adapter/contract level until real editor automation is configured
- Establish one repeatable validation path
- Keep docs, evals, and routing in sync with the chosen workflow

## Out of scope
- Broad content expansion
- Secondary platforms
- Full progression or release polish

## Top blockers
- Real Unity and Unreal tool paths are still external | Owner: technical_director | Mitigation: keep adapter contracts green with stubs, then wire real CLI/UAT paths before claiming full editor integration
- Runtime export confidence still depends on a local Godot binary or a runner with Godot installed | Owner: lead_programmer | Mitigation: keep static smoke green and add runtime smoke where `GODOT_BIN` is available
- GitHub remote exists, but branch rulesets and stricter review policy still need to be confirmed on the hosted repo | Owner: producer | Mitigation: audit the live repository against `docs/setup/github-maintainer-setup.md`

## Definition of done
- The first slice remains fair, bounded, and validated
- Validation is documented locally and mirrored in CI without fake tool-path confidence
- Docs, checklist output, and research links updated to reflect the real project state instead of template assumptions
