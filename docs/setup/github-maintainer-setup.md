# GitHub Maintainer Setup

Use this after creating the remote repository.

## What is already prepared

- `.github/CODEOWNERS`
- issue forms under `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `.github/workflows/repo-validate.yml`
- `.github/workflows/docker-smoke.yml`
- `.github/dependabot.yml`
- root community files: `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`, `CODE_OF_CONDUCT.md`

## First maintainer tasks

1. Confirm `.github/CODEOWNERS`
   Update `@YenidoganKursat` if your real GitHub handle or team differs.
2. Create the remote repository on GitHub
3. Add the remote and push the local `main` branch
4. Enable GitHub Issues and Pull Requests
5. Enable private vulnerability reporting if available
6. Review Dependabot settings
7. Create repo labels that match your issue workflow if you want labels on forms later

## Minimal shell commands

```bash
git remote add origin <your-github-url>
git add .
git commit -m "Bootstrap Codex game studio baseline"
git push -u origin main
```

## What GitHub needs from you

- A real GitHub repository URL
- The correct owner in `.github/CODEOWNERS`
- Rulesets enabled for `main`
- Actions enabled for the repository
- No secrets are required for the current default workflows
- If you later wire OpenAI, Sentry, or release upload jobs, add those secrets only then

## Recommended ruleset

Based on GitHub rulesets and CODEOWNERS guidance, set up a branch ruleset for `main` or your default branch that:

- blocks force pushes
- requires pull requests
- requires code owner review
- requires the `repo-validate` check
- requires the `docker-smoke` check when Docker surfaces matter
- optionally requires a future engine export check once a Godot-capable runner exists

## Actions security defaults

GitHub recommends pinning actions to full commit SHAs. The workflows in this repo already do that for the actions they use.

## References

- CODEOWNERS: [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- Community health files: [GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- Rulesets: [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- Secure use of Actions: [GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use)
