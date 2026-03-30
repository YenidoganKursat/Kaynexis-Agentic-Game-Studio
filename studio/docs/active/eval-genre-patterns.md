# Eval Plan: Genre Patterns

## Goal
- Verify that genre-focused tasks surface the genre guide, software pattern catalog, example contrast set, and maturity guidance before implementation.

## Scope
- genre preset selection and genre support work
- software pattern selection for genre loops
- contrast set and example game selection
- traceability for genre changes

## Expected behavior
- The router should surface `docs/research/game-development/genre/genre-guide.md`, `docs/research/game-development/genre/genre-patterns.md`, `docs/research/game-development/genre/genre-examples.md`, and `docs/research/game-development/genre/genre-maturity.md` for genre-heavy tasks.
- The checklist path should include `genre` and `research` when the task is about genre architecture or software pattern selection.
- The traceability surface should show the software pattern family and the example contrast set.

## Validation
- run one route query for a genre-pattern prompt
- confirm the returned docs include the genre guide, pattern catalog, and example matrix
- confirm the checklist path includes the genre discipline
- confirm the research refs include the matching genre notes
- re-run repo validation after routing changes

## Exit criteria
- genre pattern tasks are discoverable by the router
- the examples index points to the genre examples and pattern catalog
- the genre notes cover software pattern selection, contrast sets, and maturity
- the routing and checklist surfaces remain stable after the new context is added
