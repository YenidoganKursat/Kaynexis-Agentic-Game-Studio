# Eval Plan — World Graph Routing and Methodology

## Scope
- Verify that world-graph, relationship, faction network, chronology, lineage, biography, organization, and history tasks route to the narrative/world graph lane.
- Verify that the world-graph methodology, brief template, and golden example stay linked.
- Verify that world-graph work surfaces the right research notes, checklist items, and handoff expectations.

## Success criteria
- `scripts/route_task.py` routes world-graph tasks to `narrative / world graph`.
- `scripts/studio_core.py` returns the world graph methodology and architecture note in `research_refs`.
- `scripts/validate_docs.py` and `scripts/validate_repo_layout.py` include the new world graph docs.
- `tests/test_studio_system.py` covers the routing and docs surface.
- `make ci-local` stays green after the new narrative layer is added.

## Regression checks
- A lorebook task should still route to `narrative / lorebook`.
- A quest task should still route to `narrative / quest`.
- A generic story task should not accidentally lose narrative routing because of the new world graph lane.
- The world graph lane should preserve the fast-read / append-only / ownership guidance in docs.

## Evidence to record
- Routing output for a world graph task
- Validation output from `validate_docs.py`
- Validation output from `validate_repo_layout.py`
- Test output from `pytest`

## Next review
- Revisit this eval plan after the next narrative or world-state routing change.
