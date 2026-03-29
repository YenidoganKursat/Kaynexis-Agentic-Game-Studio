# GitHub Maintainer Setup

Use this when creating or auditing the remote repository.

## What is already prepared

- `.github/CODEOWNERS`
- issue forms under `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `.github/workflows/repo-validate.yml`
- `.github/workflows/doc-sync.yml`
- `.github/workflows/docker-smoke.yml`
- `.github/workflows/starter-kit-contracts.yml`
- `.github/workflows/release-readiness.yml`
- `.github/workflows/nightly-audit.yml`
- `.github/dependabot.yml`
- root community files: `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md`

## Suggested public metadata

Suggested repository slug:

> Kaynexis-Agentic-Game-Studio

Suggested public display title:

> Kaynexis Agentic Game Studio

Suggested short description:

> A Codex-first multi-engine studio operating system for planning, routing, research, starter kits, and CI/CD.

Suggested homepage or pinned-repo pitch:

> Durable repo-state tooling for building games across Godot, Unity, and Unreal with checklist-driven execution and research-backed workflows.

Suggested topics:

- `codex`
- `multi-engine`
- `game-development`
- `game-studio`
- `developer-tooling`
- `starter-kits`
- `checklists`
- `ci-cd`
- `godot`
- `godot-engine`
- `unity`
- `unity3d`
- `ue5`
- `unreal-engine`
- `game-architecture`
- `research-driven-development`

## First maintainer tasks

1. Confirm `.github/CODEOWNERS`
   Update `@YenidoganKursat` if your real GitHub handle or team differs.
2. Create the remote repository on GitHub if it does not exist yet
3. Add the remote and push the local `main` branch if the local repo is not connected yet
4. Apply the description and topics
5. Enable GitHub Issues and Pull Requests
6. Enable private vulnerability reporting if available
7. Review Dependabot settings
8. Create repo labels that match your issue workflow if you want labels on forms later
9. Turn on rulesets for `main`

If the repository already has a working `origin`, skip the create/add/push steps and treat this as a GitHub policy and metadata audit.

## Minimal shell commands

```bash
git remote add origin <your-github-url>
git add .
git commit -m "Bootstrap Codex game studio baseline"
git push -u origin main
```

## Suggested GitHub CLI metadata command

Replace `OWNER/REPO` with your actual repository and adjust topics as needed:

```bash
gh repo edit OWNER/REPO \
  --description "A Codex-first multi-engine studio operating system for planning, routing, research, starter kits, and CI/CD." \
  --add-topic codex \
  --add-topic multi-engine \
  --add-topic game-development \
  --add-topic game-studio \
  --add-topic developer-tooling \
  --add-topic starter-kits \
  --add-topic checklists \
  --add-topic ci-cd \
  --add-topic godot \
  --add-topic godot-engine \
  --add-topic unity \
  --add-topic unity3d \
  --add-topic ue5 \
  --add-topic unreal-engine \
  --add-topic game-architecture \
  --add-topic research-driven-development \
  --enable-issues \
  --enable-projects=false
```

## What GitHub needs from you

- a real GitHub repository URL
- the correct owner in `.github/CODEOWNERS`
- rulesets enabled for `main`
- Actions enabled for the repository
- no secrets are required for the current default workflows
- if you expand genre support, keep `docs/reference/genre-presets.md`, the genre research index, and `studio/docs/active/genre-starter.md` synchronized with the new preset files
- if you later wire OpenAI, Sentry, release uploads, or engine-backed build jobs, add those secrets only then

## Recommended ruleset

Based on GitHub rulesets and CODEOWNERS guidance, set up a branch ruleset for `main` or your default branch that:

- blocks force pushes
- requires pull requests
- requires code owner review
- requires the always-on `repo-validate` matrix jobs
- only requires `starter-kit-contracts` or `docker-smoke` if those workflows are always-on for the branches you protect
- optionally requires a future engine export check once a Godot-capable or editor-backed runner exists

Current hosted-repo note:

- The public `main` branch now has an active ruleset enforcing pull requests, code-owner review, linear history, force-push protection, delete protection, and required `repo-validate (3.11)` / `repo-validate (3.13)` checks.

## Suggested labels

If you want a clean triage surface from day one, these are a good baseline:

- `area:gameplay`
- `area:engine`
- `area:build`
- `area:docs`
- `area:research`
- `kind:bug`
- `kind:feature`
- `kind:infra`
- `priority:p0`
- `priority:p1`
- `priority:p2`
- `status:blocked`

## Actions security defaults

GitHub recommends pinning actions to full commit SHAs. The workflows in this repo pin the first-party actions they use (`actions/checkout`, `actions/setup-python`, and `actions/upload-artifact`) and `scripts/validate_workflows.py` enforces that policy.

Repo CI now also includes:

- a doc-sync guard workflow that fails when code or workflow changes are not mirrored by the relevant docs
- a quality gate that enforces the minimum CI health score before release-readiness or nightly reports are accepted
- the engine research index now includes visuals/animation playbooks, so sprite, texture, animation, and VFX changes should keep the relevant docs in sync before merge
- the user-facing engine examples page at `docs/reference/engine-examples.md` now sits inside the doc-validation surface, so engine example changes should be reviewed with the same care as engine-selection or workflow updates
- the genre development playbook at `docs/research/game-development/genre/genre-development-playbook.md` now sits in the same research surface, so when a genre family changes, update the playbook, the preset catalog, the example matrix, and the active starter together
- the genre support surface now includes city-builder, life-sim, hero-shooter, and soulslike preset families, so new presets should update the docs, examples, and starter content together rather than drifting separately
- the genre support surface now also includes auto-battler, grand-strategy, and stealth preset families, so new presets should update the docs, examples, and starter content together rather than drifting separately
- the genre advanced development framework at `docs/research/game-development/genre/genre-advanced-development-framework.md` now defines the maturity target, so if a genre family changes, update the preset, playbook, example matrix, starter docs, and maturity guide together
- the handoff and traceability docs now sit in the same sync loop as genre starter changes, so `docs/examples/README.md`, `docs/reference/handoff-contracts.md`, and `docs/reference/feature-traceability.md` should stay aligned with starter-template updates

## References

- CODEOWNERS: [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- Community health files: [GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- Rulesets: [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- Secure use of Actions: [GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use)
