# Eval Plan: Library Selection Routing

## Goal

Verify that library-selection tasks surface the new library guide and example, while still keeping build-release tasks separate.

## Scope

- library and dependency selection questions
- engine-specific package or plugin decisions
- agent examples for built-in versus official package choices

## Expected behavior

- The router should surface `docs/reference/library-guide.md` and `docs/examples/library-example.md` for library-selection tasks.
- The checklist path should include the `library` and `research` layers so the smallest-stack decision stays tied to primary sources.
- The agent should still prefer the smallest built-in or official stack before any third-party dependency.
- Build-release tasks should remain focused on build and packaging, not library choice, unless the task explicitly asks for both.

## Validation

- run one route query for a library-selection prompt
- confirm the returned docs include the new library guide and example
- confirm the task text can name the case, the built-in option, and the chosen package or plugin
- re-run the repo validation and local eval surface after routing changes

## Exit criteria

- library-selection tasks are discoverable
- the examples index points to the new library example
- the router and checklist surface remain stable after the new context is added
