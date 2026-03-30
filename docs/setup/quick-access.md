# Quick Access

Use this page when you want the shortest path from clone to a usable repo and do not want to read the full setup stack first.

## One-command setup

The front-door wrapper is:

```bash
python3 scripts/start_game_studio.py
```

That defaults to the guided setup flow. If you want to be explicit, use:

```bash
python3 scripts/codex_studio.py init \
  --project-name "Your Game" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite \
  --yes
```

## Fast access commands

- `make start` - front-door setup alias for the same guided setup flow
- `python3 scripts/codex_studio.py next "your task"` - route the next task
- `python3 scripts/codex_studio.py checklist --task "your task"` - resolve the checklist bundle
- `python3 scripts/codex_studio.py doctor` - run the repo health pass
- `python3 scripts/codex_studio.py engine --list --json` - inspect supported starter kits

## Speed pack

Use this when the task needs the fastest safe start and you do not want a long operating-model detour.

- `docs/reference/agent-speedpack.md` for the short operating contract
- `docs/examples/agent-speedpack-example.md` for one concrete fast-path bundle
- `docs/research/game-development/foundations/agent-speedpack.md` for the source-backed rationale
- `studio/checklists/discipline/speedpack.toml` for the fast-path checklist
- `studio/docs/active/eval-agent-speedpack.md` for the routing and checklist eval trail

Keep the speed pack small:

- one route
- one checklist
- one proof path
- one short summary
- history artifacts only when later review matters

## Structure packs

If you are about to work in the repo, these are the main durable packs to keep visible:

- fast path: `docs/reference/agent-speedpack.md`, `docs/examples/agent-speedpack-example.md`, `docs/research/game-development/foundations/agent-speedpack.md`
- operating model: `docs/reference/agent-system.md`, `docs/reference/mastermind-guide.md`, `docs/reference/agent-portfolio.md`, `docs/reference/agent-hierarchy.md`
- work packets: `docs/reference/agent-execution.md`, `docs/reference/prompt-journal.md`, `docs/reference/agent-transcript.md`, `docs/reference/agent-validation-matrix.md`
- engine and gameplay: `docs/reference/engine-map.md`, `docs/reference/engine-atlas.md`, `docs/reference/system-atlas.md`, `docs/reference/engine-eval.md`, `docs/reference/engine-fit.md`
- production and market: `docs/reference/ci-cd.md`, `docs/reference/version-guide.md`, `docs/reference/platform-guide.md`, `docs/reference/sector-intel.md`, `docs/reference/steam-intel.md`, `docs/reference/marketing-guide.md`
- console premium and PS5-like readiness: `docs/reference/console-guide.md`, `docs/examples/console-example.md`, `docs/research/game-development/production/console.md`
- customability and scale: `docs/reference/custom-packs.md`, `docs/examples/custom-packs-example.md`, `docs/research/game-development/foundations/custom-packs.md`, `docs/reference/custom-architecture.md`, `docs/reference/extensions-guide.md`, `docs/reference/library-guide.md`, `docs/reference/asset-guide.md`, `docs/reference/theory-guide.md`, `docs/reference/benchmark-guide.md`, `docs/reference/perf-guide.md`, `docs/reference/gpu-guide.md`

## OpenAI / Codex lane

If the task is about OpenAI, Codex, or agent-platform wiring, use these first:

- `docs/research/openai-codex-infra-findings.md`
- `docs/reference/codex-compatibility.md`
- `docs/reference/agent-system.md`
- `studio/checklists/discipline/openai_codex.toml`
- `studio/docs/active/eval-openai-codex.md`

That lane keeps controller policy, prompt versions, tool access, and eval paths explicit.

## Engine quick checks

Godot:

```bash
python3 scripts/godot_smoke.py --static-only
```

Unity:

```bash
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --unity-path tools/engine-stubs/unity/Unity \
  --dry-run --json
```

Unreal:

```bash
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path tools/engine-stubs/unreal/RunUAT.sh \
  --dry-run --json
```

## Setup packs

Use these when you want the install/bootstrap instructions in one place:

- `docs/setup/engine-installation.md` - install Godot, Unity, or Unreal with the right local smoke versus editor-backed boundary
- `docs/setup/agent-setup.md` - install the Codex CLI and bootstrap the agent operating model, journals, and review trail
- `docs/reference/custom-packs.md` - define reusable custom feature registries before you turn every override into a one-off note
- `docs/reference/console-guide.md` - map PS5-like or other console-premium readiness before scope hardens

## Where to go next

- `docs/setup/getting-started.md` for the full bootstrap flow
- `docs/setup/first-hour-walkthrough.md` for the first working hour
- `docs/setup/engine-installation.md` for engine install and path setup
- `docs/setup/agent-setup.md` for Codex CLI and agent stack bootstrap
- `docs/reference/command-cheatsheet.md` for the full command surface
- `docs/setup/troubleshooting.md` if something fails
