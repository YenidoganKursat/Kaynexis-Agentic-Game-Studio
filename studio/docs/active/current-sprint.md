# Current Sprint — kaynexisGame

## Sprint goal
- Prove the first playable slice around `First Combat Room`

## In scope
- Confirm engine and repo layout decisions
- Confirm `studio.toml`, starter-kit, and checklist assumptions
- Harden the Godot reference slice so it stays trustworthy
- Stand up Unity and Unreal starter-kit parity without faking full editor automation
- Establish one repeatable validation path
- Keep docs, evals, and routing in sync with the chosen workflow

## Out of scope
- Broad content expansion
- Secondary platforms
- Full progression or release polish

## Top blockers
- Unity and Unreal tool paths are still external | Owner: technical_director | Mitigation: keep `studio.toml` tool fields current and document intended commands in build-pipeline.md
- Runtime export confidence still depends on a local Godot binary or CI runner with Godot installed | Owner: lead_programmer | Mitigation: keep static smoke green and add runtime smoke wherever `GODOT_BIN` is available
- GitHub remote and rulesets are not configured yet | Owner: producer | Mitigation: create remote and apply maintainer setup doc

## Definition of done
- The Godot reference slice is fair, bounded, and validated
- Starter-kit parity is green for Godot, Unity, and Unreal manifests
- Validation is documented locally and mirrored in CI
- Docs, checklist output, and research links updated to reflect the real project state instead of template assumptions
