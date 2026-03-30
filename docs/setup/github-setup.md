# GitHub Setup

Use this when creating or auditing the remote repository.

## What is already prepared

- `.github/CODEOWNERS`
- issue forms under `.github/ISSUE_TEMPLATE/`
- `.github/pull_request_template.md`
- `.github/workflows/repo-validate.yml`
- `.github/workflows/validate.yml`
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
- if you simplify or rename doc or checklist surfaces, keep `studio/checklists/base/naming.toml`, `docs/reference/repo-tour.md`, and the validation docs updated together so the short canonical names rule stays visible
- if you change the validate workflow, keep `docs/reference/ci-cd.md`, `studio/docs/active/build-pipeline.md`, and `studio/docs/active/eval-ci-cd.md` updated together so the main-branch gate stays truthful
- if you prefer a lighter main-branch gate, keep `docs/reference/ci-cd.md` and `studio/docs/active/build-pipeline.md` aligned with the actual `validate.yml` command set so the docs do not overstate the runner contract
- if you change the doc-sync or repo-validate push diff logic, keep `scripts/resolve_changed_paths.py`, `docs/reference/ci-cd.md`, `studio/docs/active/build-pipeline.md`, and `studio/docs/active/eval-ci-cd.md` updated together so rewritten base SHAs do not create false failures
- keep the canonical short refs in sync too: `docs/reference/ci-cd.md`, `studio/docs/active/build-pipeline.md`, and `studio/docs/active/genre-starter.md` should use the short names that `scripts/studio_core.py` now surfaces.
- if you extend the doc validation surface, keep `docs/reference/engine-atlas.md`, the engine class research notes, and the maintainer-facing CI docs synchronized so the validator and the docs say the same thing about the covered engine families.

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
- Dependabot PRs that only bump workflow actions are allowed to skip doc-sync enforcement so dependency maintenance does not create fake doc drift
- a quality gate that enforces the minimum CI health score before release-readiness or nightly reports are accepted
- the engine research index now includes visuals/animation, UI, and audio/presentation playbooks, so sprite, texture, HUD, menu, audio, animation, and VFX changes should keep the relevant docs in sync before merge
- the user-facing engine examples page at `docs/reference/engine-examples.md` now sits inside the doc-validation surface, so engine example changes should be reviewed with the same care as engine-selection or workflow updates
- the genre development playbook at `docs/research/game-development/genre/genre-guide.md` now sits in the same research surface, so when a genre family changes, update the playbook, the preset catalog, the example matrix, and the active starter together
- the genre support surface now includes city-builder, life-sim, hero-shooter, and soulslike preset families, so new presets should update the docs, examples, and starter content together rather than drifting separately
- the genre support surface now also includes auto-battler, grand-strategy, and stealth preset families, so new presets should update the docs, examples, and starter content together rather than drifting separately
- the genre advanced development framework at `docs/research/game-development/genre/genre-maturity.md` now defines the maturity target, so if a genre family changes, update the preset, playbook, example matrix, starter docs, and maturity guide together
- the handoff and traceability docs now sit in the same sync loop as genre starter changes, so `docs/examples/README.md`, `docs/reference/handoff-contracts.md`, and `docs/reference/feature-traceability.md` should stay aligned with starter-template updates
- the lorebook methodology at `docs/reference/lorebook-methodology.md` now sits in the same sync loop as narrative starter changes, so lorebook briefs, narrative canon notes, and example entries should stay aligned with routing and quest guidance
- the world graph methodology at `docs/reference/world-graph-methodology.md` now sits in the same sync loop as narrative starter changes, so relationship graph docs, history notes, and example entries should stay aligned with routing and quest guidance
- the engine class atlas and game systems atlas now sit in the same lookup loop as feature briefs and handoffs, so gameplay and systems changes should keep those atlas references visible in docs/examples before merge
- the validate workflow now also runs a version guard and CI quality gate, so maintainer docs should treat version metadata and readiness score as part of the main-branch gate
- the feature scaffold now writes atlas references into generated docs, so maintainers should expect new briefs and handoffs to include the system atlas, engine class atlas, and quick map by default
- the bugfix and eval-plan scaffold now do the same, so triage docs and evaluation docs should also include the system atlas, engine class atlas, and quick map by default
- the advanced performance guide and example now sit in the same routing loop too, so performance-heavy updates should keep `docs/reference/advanced-perf-guide.md`, `docs/examples/advanced-perf-example.md`, and `docs/research/game-development/foundations/perf-algorithms.md` aligned before merge
- the bugfix scaffold can also create test plan and eval plan stubs, so maintainers should expect a fuller bugfix package when those flags are used
- the feature scaffold should also be expected to emit a brief plus validation docs when the slice needs them, so feature review should look for the whole package rather than a single markdown file
- the `make feature` and `make bug` helper targets now mirror that bundle shape, so maintainers should use the Makefile helpers when they want the review package instead of a single scaffolded file
- release-oriented checklist resolution now also surfaces `build-release`, so release bundles should follow the same short-name and artifact rules instead of inventing a release-only naming style
- release readiness now requires `release-ready` quality and no external dependencies, so a release bundle should be treated as a stricter signal than a validation-only run
- local toolchain detection now prefers the stable Unity editor install, the Homebrew Godot binary when present, and the repo-local Unreal UAT stub for contract coverage, so GitHub CI and local doctor output should be read as "real engine when available, contract stub when intentionally accepted" instead of assuming a missing installer means the entire engine surface is broken

## References

- CODEOWNERS: [GitHub Docs](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)
- Community health files: [GitHub Docs](https://docs.github.com/en/communities/setting-up-your-project-for-healthy-contributions/creating-a-default-community-health-file)
- Rulesets: [GitHub Docs](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- Secure use of Actions: [GitHub Docs](https://docs.github.com/en/actions/reference/security/secure-use)
