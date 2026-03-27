# GitHub Maintainer Setup

Use this after creating the remote repository.

## What is already prepared

- `.github/CODEOWNERS`
- issue forms under `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `.github/workflows/repo-validate.yml`
- `.github/workflows/docker-smoke.yml`
- `.github/workflows/starter-kit-contracts.yml`
- `.github/workflows/release-readiness.yml`
- `.github/workflows/nightly-audit.yml`
- `.github/dependabot.yml`
- root community files: `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md`

## Suggested public metadata

Suggested repository name:

> Codex Game Studio Pro Max

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
2. Create the remote repository on GitHub
3. Add the remote and push the local `main` branch
4. Apply the description and topics
5. Enable GitHub Issues and Pull Requests
6. Enable private vulnerability reporting if available
7. Review Dependabot settings
8. Create repo labels that match your issue workflow if you want labels on forms later
9. Turn on rulesets for `main`

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
- if you later wire OpenAI, Sentry, release uploads, or engine-backed build jobs, add those secrets only then

## Recommended ruleset

Based on GitHub rulesets and CODEOWNERS guidance, set up a branch ruleset for `main` or your default branch that:

- blocks force pushes
- requires pull requests
- requires code owner review
- requires the `repo-validate` check
- requires the `starter-kit-contracts` check
- requires the `docker-smoke` check when Docker surfaces matter
- optionally requires a future engine export check once a Godot-capable or editor-backed runner exists

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

## References

- CODEOWNERS: [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- Community health files: [GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- Rulesets: [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- Secure use of Actions: [GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use)
