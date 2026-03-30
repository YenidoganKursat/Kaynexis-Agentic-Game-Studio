# Eval Plan: Capability Catalog

## Change under test

- Add a master catalog that introduces the repo's major capability families in one readable place.

## Goal

- Make broad "what can this repo do?" requests land on a compact, source-backed catalog instead of forcing the user to piece together dozens of lane docs.

## Risks

- The catalog could become too long to scan quickly.
- The broad lane could blur into the mastermind or agent-system docs if the summary is not kept distinct.
- The README and repo-tour indexes could drift if the new family is not surfaced everywhere.

## Validation

- Route a broad capability-intro request and confirm the capability catalog appears first.
- Confirm the catalog points to the right families instead of trying to duplicate every lane doc.
- Confirm the example shows a simple answer shape and a short follow-up path.
- Confirm the research note and checklist stay aligned with the catalog and the indexes.

## Success criteria

- A user can ask what the studio can do and get a simple, scannable capability overview.
- The repo keeps the capability catalog, the lane docs, and the index pages synchronized.
- The validation path stays small enough to reopen later without reading the whole chat.
