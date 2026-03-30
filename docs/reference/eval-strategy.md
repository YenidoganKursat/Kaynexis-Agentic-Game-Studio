# Eval Strategy

Use eval plans whenever a change may alter how Codex routes, reviews, researches, scaffolds, or validates work in this repository.

## Require an eval plan for

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.agents/skills/**`
- shared scripts such as `codex_studio.py`, `route_task.py`, `setup_repo.py`, `doctor.py`, or other repo-wide workflow tools
- changes that tighten or relax review, safety, or delegation behavior
- changes that alter the system atlas, engine atlas, or feature/handoff surfacing used by agents during routing
- changes that alter the agent-validation matrix or the proof path for single-specialist, paired-specialist, or panel decisions
- changes that add or retune benchmark families, benchmark routes, benchmark runners, or benchmark report surfaces
- changes that introduce or retune versioning, changelog, or release-tag behavior

## Minimal eval loop

1. State the behavior under test.
2. Pick `3` to `10` representative prompts, scenarios, or operator tasks.
3. Record the baseline expectation or the current failure.
4. Define a rubric for success.
5. Run before/after checks and note regressions honestly.
6. Store the plan and outcome in `studio/docs/active/eval-plan-*.md`.

## Suggested rubric dimensions

- correctness
- evidence quality
- instruction compliance
- delegation restraint
- validation honesty
- operator usability

## Good enough for this repo

This template does not require a heavy benchmark harness for every change.
A lightweight eval plan is enough when another operator could reproduce the prompts, commands, and pass/fail reasoning.
For benchmark-shaped work, store the plan and outcome in `studio/docs/active/eval-benchmark.md` so the family, baseline, metric, threshold, and artifact stay together.

## Exit criteria

- no high-severity regressions remain unexplained
- tradeoffs are documented
- the commands, prompts, and outputs are reproducible by another operator

## Commands

Scaffold an eval plan:

```bash
python3 scripts/scaffold_eval_plan.py "Reviewer Prompt Refresh"
```

Run the standard repo checks:

```bash
python3 scripts/doctor.py
make validate
```

Run the benchmark corpus:

```bash
python3 scripts/run_bench.py --json
make bench
```

Run the versioning guard:

```bash
python3 scripts/version_guard.py --json
make version
```
