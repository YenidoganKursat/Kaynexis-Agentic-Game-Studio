# Release Checklist — {RELEASE_NAME}

## Build readiness
- Correct version / branch / tag
- VERSION and CHANGELOG.md agree
- Reproducible build path
- Artifact stored

## Quality gate
- Critical bugs reviewed
- Smoke / regression complete
- Known issues documented

## Hardening review
- Code protection choice documented
- Multiplayer trust boundary named
- Symbol and crash artifact policy explicit
- Dedicated server split or explicit fallback path named
- See `studio/docs/templates/release-hardening.md` for the protected-build variant

## Platform/store/cert
- Submission metadata ready
- Store assets ready
- Compliance notes reviewed

## Comms & rollback
- Patch notes ready
- Rollback owner named
- Hotfix path rehearsed
