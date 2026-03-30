# Benchmark Guide

## Summary

Use this page when you need a systematic way to measure agent routing, checklist quality, docs sync, or any other reproducible decision surface in this repo.

The rule is simple: name the benchmark family, name the baseline, name the metric, name the threshold, and store the artifact.

## Primary sources

- [SWE-bench](https://www.swebench.com/)
- [SWE-bench GitHub](https://github.com/swe-bench/SWE-bench)
- [AgentBench](https://github.com/THUDM/AgentBench)
- [GAIA](https://huggingface.co/gaia-benchmark)
- [OSWorld](https://github.com/xlang-ai/OSWorld)
- [WebArena](https://github.com/web-arena-x/webarena)
- [OpenAI Evals](https://platform.openai.com/docs/guides/evals)

## Why this matters to this repo

- The repo already has routing, checklist, research, and eval surfaces that can drift if they are not measured together.
- Benchmarking keeps the agent honest about route quality, checklist quality, and docs sync instead of relying on confidence.
- Ready-made benchmark families are useful when the question is broad; the repo-local benchmark suite is useful when the question is specific to this operating system.

## Decision impact

- Choose the benchmark family before comparing behavior.
- Keep the baseline, metric, and threshold explicit.
- Keep the evidence artifact and the runner command explicit.
- Update the benchmark guide, example, checklist, and eval plan together when the benchmark surface changes.

## Ready-made benchmark families

| Family | Best for | Fit here |
| --- | --- | --- |
| SWE-bench | Code-edit regression on real repositories | Good reference for repo-editing and patch-quality comparisons |
| AgentBench | Broad agent behavior across tools and environments | Good reference for multi-step tool use and environment breadth |
| GAIA | General reasoning and task completion | Good reference for complex assistant behavior |
| OSWorld | Desktop and operating-system tasks | Good reference for OS-level agent workflows |
| WebArena | Browser and website tasks | Good reference for web navigation and browser automation |
| OpenAI Evals | Custom, reusable eval harnesses | Good reference for repo-local benchmark harness design |
| Repo-local benchmark suite | Route, checklist, docs, and validation surfaces in this repo | The benchmark runner used by this operating system |

## Repo-local benchmark suite

- `scripts/run_bench.py` runs the local benchmark corpus.
- `evals/benchmark/cases.json` defines the route, checklist, and docs regression cases.
- The suite should cover:
  - route accuracy
  - checklist coverage
  - docs and research surfacing
  - benchmark family selection
  - baseline and threshold clarity

## Example prompts for the agent

- "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio."
- "Compare SWE-bench and OpenAI Evals for code-edit regression coverage before choosing a harness."
- "Choose between AgentBench, GAIA, OSWorld, and WebArena for a broad agent benchmark and name the threshold."
- "Design a benchmark pass for a Unity 6 inventory HUD and keep the metric, baseline, and artifact explicit."

## Validation

- `python3 scripts/run_bench.py --json`
- `make bench`
- `python3 scripts/run_local_evals.py --json`
- `make validate`

## Related docs

- `docs/examples/benchmark-example.md`
- `docs/research/game-development/foundations/benchmarks.md`
- `studio/docs/active/eval-benchmark.md`
- `docs/reference/eval-strategy.md`
- `docs/reference/quality-guide.md`
- `docs/reference/perf-guide.md`
