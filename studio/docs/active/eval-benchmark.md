# Benchmark Eval

## Change under test

- `docs/reference/benchmark-guide.md` and `docs/examples/benchmark-example.md` define the benchmark ladder.
- `docs/research/game-development/foundations/benchmarks.md` records the source-backed benchmark families and the local benchmark rule.
- `scripts/run_bench.py` is the local benchmark runner.
- `scripts/studio_core.py` and `scripts/route_task.py` should surface benchmark routing and checklist guidance.
- `studio/checklists/discipline/benchmark.toml` should require the family, baseline, threshold, coverage, artifact, and doc-sync rule.

## Goal

- Route benchmark and measurement tasks to a dedicated benchmark bundle instead of generic quality or performance advice.
- Keep ready-made benchmark families visible alongside the repo-local benchmark suite.
- Make the benchmark runner produce a reusable artifact.
- Keep route, checklist, docs, and eval surfaces synchronized.

## Benchmark families

- SWE-bench
- AgentBench
- GAIA
- OSWorld
- WebArena
- OpenAI Evals
- Repo-local benchmark suite

## Benchmark cases

| Prompt / scenario | Why it matters | Baseline | Expected after change |
| --- | --- | --- | --- |
| "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio" | Tests the dedicated benchmark route | Benchmark tasks may stay on generic research or quality advice | `benchmark / measurement` plus the benchmark docs and runner are surfaced |
| "Compare SWE-bench and OpenAI Evals for code-edit regression coverage before choosing a harness" | Tests ready-made family selection | The agent may name the families but skip the measurement loop | The benchmark guide, example, and foundation note are surfaced with a clear family choice |
| "Compare AgentBench, GAIA, OSWorld, and WebArena for broad agent coverage before picking a benchmark family" | Tests broad benchmark family selection | The agent may collapse everything into one vague benchmark answer | The agent names the tradeoff between tool-use, desktop, browser, and reasoning families |
| "Design a benchmark pass for a Unity 6 inventory HUD and name the metric, baseline, and threshold" | Tests engine-aware benchmark measurement | The agent may drift into generic quality advice | The benchmark route still surfaces Unity perf guidance and the benchmark report path |

## Rubric

- correctness
- evidence quality
- instruction compliance
- validation honesty
- operator usability

## Run notes

- Date / operator / model / config
- Commands used
- Report artifact path
