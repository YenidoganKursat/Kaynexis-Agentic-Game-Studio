# Codex Compatibility

This repository is intentionally shaped around official Codex repo conventions.

It is also intentionally multi-engine. The repo-level contract covers `godot-4`, `unity-6`, and `unreal-5`; the current Godot slice is only the reference implementation that proves the studio OS can drive a real runtime surface.

## Codex-native surfaces in this repo

- `AGENTS.md` at the repo root, plus nested `AGENTS.md` files
- `.codex/config.toml` for shared project defaults
- `.codex/agents/` for focused custom agents
- `.agents/skills/` for reusable workflows
- `.codex/hooks.json` for optional experimental hooks
- local evals under `evals/`
- GitHub validation workflows that mirror the local checks
- starter-kit adapters and command contracts for Godot, Unity, and Unreal

## Supported operating model

- root instructions stay concise
- review policy lives in dedicated docs
- evals guard shared behavior changes
- hooks are opt-in
- Docker is optional, not mandatory
- engine parity is defined at starter-kit and adapter level, not by pretending all three engines share the same runtime files

## OpenAI / Codex alignment

- When the work touches OpenAI, Codex, or agent-platform design, start with `docs/research/openai-codex-infra-findings.md` and `docs/reference/agent-system.md`.
- When model choice or plan-tier fit is part of the question, also start with `docs/research/openai-codex-models.md` and `docs/reference/codex-model-guide.md`.
- If you need the repo-local model control contract, pair that with `docs/examples/codex-model-guide-example.md`, `studio/checklists/discipline/openai_models.toml`, and `studio/docs/active/eval-openai-models.md`.
- Keep the controller summary short and the specialist lanes narrow, even if the internal workflow uses traces, handoffs, or a multi-agent panel.
- Treat prompt-shape changes, routing changes, and tool-access changes as eval-worthy and document the proof path in `studio/docs/active/`.
- Keep internet access, tool approvals, and safety assumptions explicit for any workflow that reaches outside the repo.
- Prefer the official OpenAI docs first when the question is about OpenAI products, Codex, or agent workflow surfaces.
- Prefer the current model catalog and the codex model guide when the question is about model choice, reasoning level, or plan fit.
- Use `studio/checklists/discipline/openai_codex.toml` and `studio/docs/active/eval-openai-codex.md` when you need the repo-local control contract for this workflow.

## What to customize first

1. `.github/CODEOWNERS`
2. `studio/docs/active/engine-profile.md`
3. `studio/docs/active/game-brief.md`
4. `studio/docs/active/current-sprint.md`
5. `.env` if you actually need integrations

## Helpful local commands

```bash
make ci-local
python3 scripts/codex_studio.py engine --list --json
python3 scripts/run_local_evals.py
python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine godot-4 --platform pc-premium --genre action-roguelite
python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine unity-6 --platform pc-premium --genre tactical-rpg
python3 scripts/seed_project_baseline.py --project-name "Your Game" --engine unreal-5 --platform console-premium --genre co-op-survival
python3 scripts/starter_kit_contract_smoke.py --engine godot-4 --json
python3 scripts/unity_adapter.py test --project-path studio/starter-kits/unity-6/scaffold --dry-run --json
python3 scripts/unreal_adapter.py package --project-path studio/starter-kits/unreal-5/scaffold --uat-path tools/engine-stubs/unreal/RunUAT.sh --dry-run --json
python3 scripts/toggle_codex_hooks.py --status
```

## Related docs

- `docs/reference/code-review.md`
- `docs/reference/eval-strategy.md`
- `docs/setup/optional-codex-hooks.md`
- `docs/setup/github-setup.md`
