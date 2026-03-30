# Current Sprint — Kaynexis Agentic Game Studio

## Sprint goal
- Prove the first playable slice around `First Combat Room`

## In scope
- Confirm engine and repo layout decisions
- Confirm `studio.toml`, starter-kit, and checklist assumptions
- Harden the Godot reference slice so it stays trustworthy
- Keep Unity and Unreal support honest at adapter/contract level until full editor-backed validation exists for every engine
- Establish one repeatable validation path
- Keep docs, evals, and routing in sync with the chosen workflow

## Out of scope
- Broad content expansion
- Secondary platforms
- Full progression or release polish

## Top blockers
- Runner-backed engine-native smoke is still missing for Godot, Unity, and Unreal, so CI parity still depends on runner-side engine binaries even though local toolchain health is green | Owner: technical_director | Mitigation: keep local adapter/contracts green, then add real engine binaries to the runner before claiming release-grade parity
- Hosted GitHub ruleset is active on `main`, but it currently enforces only the always-on `repo-validate` matrix | Owner: producer | Mitigation: keep the ruleset audited and add more required checks only when their workflows are not path-filtered

## Definition of done
- The first slice remains fair, bounded, and validated
- Validation is documented locally and mirrored in CI without fake tool-path confidence
- Docs, checklist output, and research links updated to reflect the real project state instead of template assumptions
