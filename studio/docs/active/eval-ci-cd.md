# Eval - CI/CD Surface

## Change under test

- Harden the GitHub Actions validate workflow so it stays pinned, emits a validate artifact bundle, and stays aligned with the local validation surface.
- Harden the GitHub Actions validate and release-readiness workflows so they stay pinned, emit reusable bundles, and reflect the same version and readiness thresholds as the local validation surface.
- Harden the doc-sync and repo-validate changed-path resolution so push events keep working even when the recorded base SHA is no longer available in the checkout.

## Goal

- Keep the main-branch validation path reliable, reproducible, and easy to inspect later.
- Make sure workflow drift is caught by both the validator and the docs.

## Risks

- A workflow rename or new artifact path could drift out of sync with the docs.
- Unpinned actions or missing artifacts would weaken the release signal.
- A validate workflow that is too narrow would miss repo-health regressions.
- A release-readiness workflow that only asks for validation-ready status would understate release risk.
- A push-event diff that fails to resolve the base SHA would create a false CI failure even when the PR branch itself is healthy.

## Validation

- `python3 scripts/validate_workflows.py`
- `python3 scripts/validate_repo_layout.py`
- `python3 scripts/validate_docs.py --strict`
- `python3 scripts/doctor.py --json`
- `python3 scripts/ci_artifact_report.py --label validate --output-dir build/ci/validate --json`
- `python3 scripts/version_guard.py --output-dir build/ci/version --json`
- `python3 scripts/ci_quality_gate.py --report build/ci/validate/ci-report.json --min-score 80 --minimum-readiness validation-ready --json`
- `python3 scripts/resolve_changed_paths.py --base-sha deadbeefdeadbeefdeadbeefdeadbeefdeadbeef --paths-file build/ci/pytest-quality/changed-paths.txt --json`

## Success criteria

- `validate.yml` is pinned, documented, and checked by the workflow validator.
- The validate workflow emits a reusable artifact bundle.
- The validate workflow also emits version metadata and passes the CI quality gate.
- The docs and setup guide mention the validate workflow explicitly.
- The doctor surface and workflow surface both flag missing validate coverage.
- `release-readiness.yml` requires `release-ready` quality and no external dependencies before it uploads a bundle.
- Push-triggered doc-sync and repo-validate jobs resolve changed paths safely even when a previous base SHA was rewritten or is temporarily unavailable.
