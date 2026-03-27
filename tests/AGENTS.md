# Test Instructions

These instructions apply under `tests/`.

## Goals
- Create tests that map to player-facing acceptance criteria.
- Prefer reliable smoke/regression cases over brittle overfitting.
- Cover the riskiest paths first: save, network, perf-sensitive, and release-blocking issues.

## Minimum test language
Each new test plan or suite should answer:
- what is under test
- setup/preconditions
- expected outcome
- failure signal
- cleanup/reset needs
