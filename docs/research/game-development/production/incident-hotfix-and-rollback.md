# Incident, Hotfix, and Rollback Workflow

## Date
- 2026-03-28

## Summary
- Game incidents rarely fail because no one wrote code fast enough. They fail because ownership, evidence, blast radius, rollback options, and player-facing communication were unclear.
- Hotfix readiness is not only a build problem. It depends on knowing:
  - what changed
  - who can approve a rollback
  - which artifact is known-good
  - which save/data risks make rollback unsafe
  - how players will be informed
- The repo should treat incident response as a documented workflow with named roles and artifacts, not a panic-time improvisation.

## Primary sources
- [Steamworks documentation](https://partner.steamgames.com/doc/home)
- [Release a version update in phases](https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases)
- [Stage a rollout for your app release](https://support.google.com/googleplay/android-developer/answer/6346149)

## Why this matters to this repo
- This system already values release validation and durable docs. Incident response is the production version of that same principle.
- Build-pipeline, release-checklist, bug-report, and crash-triage templates should all point toward the same hotfix and rollback language.
- For live or public builds, the repo should always be able to answer:
  - what version is live
  - what version is safe to revert to
  - what data or save risks block rollback
  - who owns the player-facing message

## Decision impact
- Release and bugfix tasks should surface this note for hotfix, rollback, incident, and live-issue work.
- Release checklists should name a rollback owner and a known-good artifact.
- Postmortems should record whether the rollback decision path was clear enough.

## Workflow guidance

### Before an incident
- Keep deterministic build identifiers and artifact locations.
- Keep one known-good build path and one rollback owner.
- Document save/data compatibility assumptions before launch.

### During an incident
- Triage:
  - what is broken
  - who is affected
  - what changed
  - can it be disabled, fixed forward, or rolled back
- Decide whether the safest move is:
  - hotfix forward
  - disable the feature or route
  - staged rollout pause
  - full rollback

### After containment
- Capture:
  - blast radius
  - evidence used
  - time to detect
  - time to contain
  - what made rollback easier or harder

## What to watch out for
- Hotfixing without a clear save/schema compatibility check
- Rolling back binaries while leaving incompatible live data assumptions in place
- Treating communication as optional until after the technical fix
- Losing the exact artifact path or version identifier needed to revert quickly
