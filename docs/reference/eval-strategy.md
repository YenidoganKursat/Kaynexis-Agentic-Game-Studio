# Eval Strategy

Use eval plans whenever a change may alter how Codex routes, reviews, researches, scaffolds, or validates work in this repository.

## Require an eval plan for

- `AGENTS.md`
- `.codex/config.toml`
- `.codex/agents/*.toml`
- `.agents/skills/**`
- shared scripts such as `route_task.py`, `setup_repo.py`, `doctor.py`, or other repo-wide workflow tools
- changes that tighten or relax review, safety, or delegation behavior

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
