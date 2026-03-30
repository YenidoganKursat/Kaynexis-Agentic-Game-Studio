# Build Pipeline — {PROJECT_NAME}

## Build graph
- Source -> validation -> package -> artifact -> distribution

## Environments
- Local / CI / staging / release

## Artifacts & versioning
- VERSION is the source of truth for the working-tree version
- Keep CHANGELOG.md and release tags aligned with the same version family
- Build numbers, symbols, release notes, storage

## Failure / rollback
- Who acts, how rollback works, what evidence is captured
