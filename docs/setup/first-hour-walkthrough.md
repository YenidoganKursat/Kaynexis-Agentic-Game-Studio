# First Hour Walkthrough

This guide is for the first real hour in the repo.

The goal is simple:

- choose an engine
- initialize the project state
- confirm the active docs
- route one real task
- resolve the checklist for that same task
- run one validation path before you start building

## Before you start

Minimum tools:

- Python `3.11+`

Helpful extras:

- Git
- Docker
- Codex CLI
- one local engine install if you want engine-backed validation instead of contract smoke

## Step 1: Choose the engine family

Use this quick rule:

- choose `godot-4` when you want the lightest path to a real reference slice, fast iteration, or a small team setup
- choose `unity-6` when you want a package-driven workflow, strong tooling conventions, or broader mobile/web/plugin familiarity
- choose `unreal-5` when you want a heavier 3D, systems, or packaging-oriented pipeline and plan around Unreal-native concepts early

If you are unsure, read `docs/reference/engine-selection-guide.md` first.
If you want concrete examples before you choose, open `docs/reference/engine-examples.md` too.

## Step 2: Initialize the repo

Interactive:

```bash
python3 scripts/codex_studio.py init
```

Non-interactive examples:

```bash
# Godot 4
python3 scripts/codex_studio.py init \
  --project-name "Signal Forge" \
  --engine godot-4 \
  --platform pc-premium \
  --genre action-roguelite \
  --yes

# Unity 6
python3 scripts/codex_studio.py init \
  --project-name "Grid Breakers" \
  --engine unity-6 \
  --platform pc-premium \
  --genre tactical-rpg \
  --yes

# Unreal 5
python3 scripts/codex_studio.py init \
  --project-name "Drift Colony" \
  --engine unreal-5 \
  --platform console-premium \
  --genre co-op-survival \
  --yes
```

## Step 3: Open the active docs

Read these before you do any real feature work:

1. `studio/docs/active/game-brief.md`
2. `studio/docs/active/genre-starter.md`
3. `studio/docs/active/engine-profile.md`
4. `studio/docs/active/current-sprint.md`
5. `studio/docs/active/risk-register.md`

What you are checking for:

- the project name is correct
- the chosen engine is correct
- the platform and genre match the real plan
- the sprint is not too broad
- the risks do not contradict the task you want to start

## Step 4: Route one real task

Use a concrete request, not a vague theme.

Better:

```bash
python3 scripts/codex_studio.py next \
  "Implement a readable first enemy attack for the tutorial room"
```

Worse:

```bash
python3 scripts/codex_studio.py next "work on combat"
```

You want the route to tell you:

- which skill cluster fits the task
- which agents are relevant
- which docs should ground the task
- which research notes you should read first

## Step 5: Resolve the checklist for the same task

Run the same task through checklist resolution:

```bash
python3 scripts/codex_studio.py checklist \
  --task "Implement a readable first enemy attack for the tutorial room"
```

Now you have:

- base repo health checks
- engine-specific rules
- discipline-specific rules
- milestone-specific rules when applicable
- any custom studio overrides

## Step 6: Pick one validation path before coding

Godot:

```bash
python3 scripts/godot_smoke.py --static-only
```

Unity:

```bash
python3 scripts/unity_adapter.py test \
  --project-path studio/starter-kits/unity-6/scaffold \
  --dry-run --json
```

If Unity is not installed on the machine yet, add `--unity-path tools/engine-stubs/unity/Unity` to keep this as contract smoke instead of editor-backed validation.

Unreal:

```bash
python3 scripts/unreal_adapter.py package \
  --project-path studio/starter-kits/unreal-5/scaffold \
  --uat-path tools/engine-stubs/unreal/RunUAT.sh \
  --dry-run --json
```

This keeps the task grounded in one proof path before the work grows.

## Step 7: If the route feels too broad, create a brief first

Use a short brief before a non-trivial slice:

```bash
python3 scripts/scaffold_feature.py "Tutorial Enemy Attack" --with-adr --with-test-plan
```

That scaffold also creates default handoff and traceability docs, which is useful even for solo work because it keeps the next step explicit.

Do this especially when:

- the task changes gameplay rules
- the task touches save, progression, damage, AI, or UI flow
- the task crosses multiple disciplines
- the task sounds bigger than one focused slice

## Step 8: End the hour with health checks

Run:

```bash
python3 scripts/codex_studio.py doctor
python3 scripts/run_local_evals.py
python3 scripts/validate_engine_kits.py
```

If you want the broader local CI equivalent:

```bash
make ci-local
```

## Good first-hour outcomes

At the end of the first hour, you are in good shape if all of this is true:

- the chosen engine is written into `studio.toml`
- active docs match the real project identity
- you have one concrete next task
- you have a checklist bundle for that task
- you know which research note you should read next
- you know one validation command you will keep green during the slice

## Common mistakes

- starting implementation before opening `current-sprint.md`
- using a vague task description that routes poorly
- treating Unity or Unreal dry-run smoke as a real build
- skipping the checklist because the task "feels small"
- editing many active docs at once before the project identity is stable
