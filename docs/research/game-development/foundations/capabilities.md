# Capability Surface Notes

Date: 2026-03-30

## Summary

This note keeps the repo's capability catalog evidence-backed so the studio can explain what it can do today, not what it might do later.

## Primary sources

- `docs/reference/capabilities.md`
- `docs/examples/capabilities-example.md`
- Source link: <https://github.com/YenidoganKursat/Kaynexis-Agentic-Game-Studio/blob/main/docs/reference/capabilities.md>

## Why this matters to this repo

The catalog reduces repeated explanation in chat and gives routing a clear broad-intro target.
It also keeps the README indexes synchronized with the durable capability families.

## Decision impact

- Use the capability catalog when the user asks what the studio can do.
- Keep every capability family tied to a guide, an example, and a validation path.
- Update the catalog, example, README indexes, and routing surface together when a new family lands.

## What this note is for

This note keeps the repo's capability catalog evidence-backed.
The master catalog should describe what the studio can do today, not what it might do later.

## Core rule

- Group capabilities by durable decision surface, not by folder tree alone.
- Keep the top-level explanation short enough for a newcomer to read in one pass.
- Tie every capability family to a starting guide, an example, and a validation path.
- Do not advertise a capability unless the matching durable docs already exist.

## Recommended workflow

1. Start from the user question.
2. Decide whether the ask is about the whole studio or a narrower lane.
3. If it is broad, open the capability catalog first.
4. If it is narrow, jump to the specific lane and keep the answer short.
5. When a new capability family lands, update the catalog, the example, the README indexes, and the routing surface together.

## Good capability family shape

- family name
- what it covers
- best starting docs
- example prompt shape
- validation path

## Validation questions

- Can a newcomer understand the studio's main capabilities from one page?
- Can the router send a broad "what can you do?" request to the right lane?
- Does every listed family have at least one guide, one example, and one durable note?
- Did the README and repo-tour indexes stay synchronized with the catalog?

## Repo impact

The catalog becomes a stable brochure for the studio.
It reduces repeated explanation in chat and gives routing a clear broad-intro target.
