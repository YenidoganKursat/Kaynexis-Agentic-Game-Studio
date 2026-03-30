# Engine Eval — Kaynexis Agentic Game Studio

## Current frame
- Supported engines: Godot 4, Unity 6, Unreal 5
- Current reference runtime: Godot 4 in `src/`
- Comparison context: Unity and Unreal stay available through starter kits, adapters, and research notes
- Current validation gap: runner-backed engine-native smoke still needs a real CI runner with engine binaries

## Scorecard
| Engine | Build smoke | Test smoke | Performance proof | Toolchain friction | Current note |
|---|---|---|---|---|---|
| Godot 4 | static smoke and export helpers exist | static smoke plus runtime smoke when local binary exists | perf guide and engine perf notes exist | local binary optional for contract smoke | reference runtime stays in `src/` |
| Unity 6 | adapter build command exists | adapter test command exists | profiler and performance notes exist | editor binary must be available for full validation | starter-kit parity is maintained |
| Unreal 5 | UAT / BuildGraph contract exists | automation / package contract smoke exists | performance and Insights notes exist | editor or UAT binary required for full validation | starter-kit parity is maintained |

## Evaluation loop
- Name the comparison engines.
- Name the build, test, performance, and toolchain signals.
- Record the first blocker per engine family.
- Keep the recommendation short and evidence-backed.

## Recommendation state
- Favor the engine that gives the smallest proof path for the current slice, not the one with the broadest reputation.
- When the choice is unclear, keep the comparison matrix in this file current and rerun the eval plan before the next scope lock.

## Related docs
- `docs/reference/engine-eval.md`
- `docs/examples/engine-eval-example.md`
- `docs/reference/engine-selection-guide.md`
- `docs/reference/engine-map.md`
- `docs/reference/benchmark-guide.md`
- `docs/reference/perf-guide.md`
- `docs/research/game-development/foundations/engine-eval.md`
- `studio/checklists/discipline/engine_eval.toml`
- `studio/docs/active/eval-engine-eval.md`
