# Benchmarks

## Date

- 2026-03-29

## Summary

Benchmarking in this repo means comparing agent behavior or system behavior against a named family, a baseline, and a threshold.

Use ready-made benchmark families when the question is broad. Use the repo-local benchmark suite when the question is routing, checklist quality, docs sync, or another behavior that belongs to this operating system.

## Primary sources

- [SWE-bench](https://www.swebench.com/)
- [SWE-bench GitHub](https://github.com/swe-bench/SWE-bench)
- [AgentBench](https://github.com/THUDM/AgentBench)
- [GAIA](https://huggingface.co/gaia-benchmark)
- [OSWorld](https://github.com/xlang-ai/OSWorld)
- [WebArena](https://github.com/web-arena-x/webarena)
- [OpenAI Evals](https://platform.openai.com/docs/guides/evals)

## Why this matters to this repo

- Route quality, checklist quality, docs sync, and eval behavior are all agent-facing surfaces that should stay measurable.
- External benchmark families give the team a shared language when deciding how broad the measurement problem really is.
- Repo-local benchmarks keep this operating system honest about its own routing and validation behavior.

## Decision impact

- Add benchmark docs when the agent needs a reproducible measurement loop.
- Keep the family, baseline, metric, threshold, and artifact path explicit.
- Treat benchmark docs, the runner, and the eval plan as one bundle.
- Keep benchmark families separated from the repo-local benchmark suite so the agent knows what is external and what is owned here.

## Practical framing

- SWE-bench is the default reference for code-edit regression on real repositories.
- AgentBench is useful when the question is broad agent behavior across tools and environments.
- GAIA is useful when the question is general reasoning and task completion.
- OSWorld is useful when the question is desktop or operating-system behavior.
- WebArena is useful when the question is browser and website behavior.
- OpenAI Evals is useful when the team needs a reusable custom harness.
- The repo-local benchmark suite is useful when the question is route accuracy, checklist quality, docs sync, or another behavior that belongs to this repository.

## What to watch out for

- Do not force a heavy external family onto a small repo-local routing question.
- Do not measure without a baseline.
- Do not report a score without a threshold.
- Do not call a benchmark stable without an artifact path and command.

## Repo impact

- `docs/reference/benchmark-guide.md` describes the family choice and the local benchmark path.
- `docs/examples/benchmark-example.md` shows the same decision order in a concrete bundle.
- `studio/checklists/discipline/benchmark.toml` keeps the family, baseline, threshold, and evidence path explicit.
- `studio/docs/active/eval-benchmark.md` records the benchmark behavior under test.
- `scripts/run_bench.py` produces the local benchmark report artifact.
- `evals/benchmark/cases.json` defines the repo-local benchmark cases.
