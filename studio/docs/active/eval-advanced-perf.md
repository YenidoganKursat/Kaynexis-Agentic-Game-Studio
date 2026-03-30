# Eval Plan: Advanced Performance Routing

## Goal

Verify that algorithm-heavy performance tasks surface the advanced performance guide and example, while still keeping the existing performance and genre-performance paths available.

## Scope

- spatial partitioning, culling, batching, instancing, and job-system tasks
- optimization requests that need an algorithm family before implementation
- agent examples for advanced performance decisions

## Expected behavior

- The router should surface `docs/reference/advanced-perf-guide.md` and `docs/examples/advanced-perf-example.md` for algorithm-heavy optimization tasks.
- The checklist path should treat those tasks as both `advanced_performance` and `performance` work, not generic research-only work.
- Generic performance tasks should still be able to land on the existing `perf-guide` and `genre-perf-guide` paths when the prompt is not algorithm-heavy.

## Validation

- run one route query for an algorithm-heavy optimization prompt
- confirm the returned docs include the advanced guide and example
- confirm the checklist path still includes the performance discipline when the task is algorithm-heavy
- re-run the repo validation and local eval surface after routing changes

## Exit criteria

- advanced optimization tasks are discoverable
- the examples index points to the new advanced perf example
- the router and checklist surface remain stable after the new context is added
