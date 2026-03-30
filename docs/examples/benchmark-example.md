# Benchmark Example

## Scope

- Build a benchmark bundle for route accuracy, checklist quality, and docs sync.
- Keep the benchmark family, baseline, metric, threshold, and report artifact explicit.

## Baseline

| Surface | Baseline | Goal |
| --- | --- | --- |
| Route behavior | Benchmark tasks fall back to generic research or quality advice | Benchmark tasks route to `benchmark / measurement` |
| Checklist behavior | Benchmark tasks only surface generic quality or performance items | Benchmark tasks surface benchmark items plus the support layers they need |
| Docs behavior | Benchmark tasks do not surface the benchmark guide or example | Benchmark tasks surface the benchmark guide, example, and research note |
| Report behavior | No benchmark artifact exists | `scripts/run_bench.py` writes a benchmark report and markdown summary |

## Decision order

1. Name the benchmark family.
2. Name the baseline.
3. Name the metric.
4. Name the threshold.
5. Name the report artifact.
6. Keep the benchmark guide, example, and eval plan synchronized.

## Ready-made benchmark families

- SWE-bench for code-edit regression on real repositories
- AgentBench for broad agent behavior across tools and environments
- GAIA for general reasoning and task completion
- OSWorld for desktop and operating-system tasks
- WebArena for browser and website tasks
- OpenAI Evals for custom harnesses and reusable evals
- Repo-local benchmark suite for route, checklist, and docs regression in this repo

## Repo-local benchmark case

- Route check: `Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio`
- Checklist check: the benchmark discipline must surface the benchmark family, the baseline, the threshold, the evidence artifact, and the doc-sync rule
- Report check: `scripts/run_bench.py` should write a readable artifact into `build/bench/latest/`

## Good agent prompts

- "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio."
- "Compare SWE-bench and OpenAI Evals for code-edit regression coverage before choosing a harness."
- "Choose between AgentBench, GAIA, OSWorld, and WebArena for a broad agent benchmark and name the threshold."
- "Design a benchmark pass for a Unity 6 inventory HUD and keep the metric, baseline, and artifact explicit."

## Validation

- `python3 scripts/codex_studio.py next "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio"`
- `python3 scripts/codex_studio.py checklist --task "Build a benchmark suite that measures route accuracy, checklist quality, and docs sync for this studio"`
- `python3 scripts/run_bench.py --json`
- `python3 scripts/run_local_evals.py --json`
- `studio/docs/active/eval-benchmark.md` stays synchronized with the benchmark guide and runner
