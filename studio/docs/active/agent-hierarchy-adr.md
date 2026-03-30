# Agent Hierarchy ADR

## Status
- Accepted

## Context
- The repo already had a master mind controller and an agent portfolio, but broad requests still needed a clearer command tree.
- The user asked for explicit titles, grouped authority, async work, and a structure that still keeps the single specialist option alive.
- Broad, cross-functional work is easier to manage when titles, reporting lines, and validation packets are visible.

## Decision
- Add a dedicated agent hierarchy layer above the portfolio layer.
- Keep single specialist mode as the default.
- Use the hierarchy only when the task genuinely needs a controller, directors, leads, specialists, and validators.
- Require every async lane to report upward with a compact packet.

## Consequences
- Benefits: clear titles, clear reporting lines, clearer handoffs, simpler review of async work.
- Costs: one more doc layer and one more checklist layer to maintain.
- Follow-up work: keep route keywords, examples, checklists, and active docs synchronized so the hierarchy does not drift into generic panel mode.

## Rejected options
- Collapse hierarchy into the existing agent portfolio page without a separate command-tree contract.
- Make the multi-agent panel the default instead of preserving single specialist mode.
- Use one generic "worker" title for every lane and lose accountability.

