# Code Review Guide

Use this guide when reviewing code, docs, config, or workflow changes in this repository.

## Default stance

- Review like an owner.
- Lead with correctness, security, behavior regressions, and missing test coverage.
- Deprioritize style-only comments unless they hide a real bug, release risk, or maintenance trap.
- Cite files, commands, docs, or repro steps whenever possible.

## Always check

- Does the change alter runtime behavior, project docs, or Codex behavior?
- Is the touched system described somewhere durable, such as an active doc, template, or config file?
- Is the validation proportional to the risk?
- Are rollback or recovery paths clear for risky changes?

## Risk checklist

Use this checklist to keep review comments focused on real risk rather than style-only noise.

### Runtime and project risk

- crashes, hangs, data loss, or save corruption
- broken inputs, controller regressions, or platform-specific failures
- performance, load time, memory, or build/export regressions
- content pipeline drift, missing imports, or naming mismatches

### Codex and workflow risk

- conflicting instructions across `AGENTS.md`, `.codex/config.toml`, `.codex/agents/`, or `.agents/skills/`
- broadened agent mandates that blur ownership or reduce review discipline
- recursion-prone delegation or unbounded fan-out
- hidden behavior changes in setup, doctor, routing, or scaffolding scripts
- root instructions growing so large that detailed policy should move to dedicated docs

## Validation expectations

- For quality or optimization-criteria work, pair this guide with `docs/reference/quality-guide.md` and `docs/reference/quality-process.md` so the review bar, process loop, optimization bar, and first lever stay explicit.
- Small doc-only change: link checks, grep checks, script validation, and a clear before/after explanation
- Script or config change: command output from the touched script plus `python3 scripts/doctor.py` or `make validate`
- Agent or instruction change: at minimum an eval plan or an explicit rationale for why behavior is unchanged
- Behavior change: automated tests or an explicit manual validation story with commands and expected results

## Findings format

1. Findings first, ordered by severity
2. Open questions or assumptions
3. Brief change summary
4. Residual risk

## Block a change if

- evidence is missing for a risky claim
- regression risk is known but untested
- instruction precedence is unclear
- the change silently weakens review, security, or documentation discipline
- recursive or high-cost delegation becomes easier without a documented reason
