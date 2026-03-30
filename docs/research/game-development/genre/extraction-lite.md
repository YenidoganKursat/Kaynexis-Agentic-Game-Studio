# Extraction Lite

## Date
- 2026-03-29

## Summary
- Extraction-lite games fail first on unfair loss, unclear risk/reward, and hidden economy abuse. The player has to understand what is worth taking, what can be lost, and what counts as a successful escape.
- The dominant loop is:
  - enter a raid or contract
  - take risk for loot or objectives
  - manage pressure from enemies or other players
  - escape through a readable extraction window
  - convert the raid result into stash or progression
- The first systems that usually break are:
  - death feeling opaque or arbitrary
  - loot authority becoming ambiguous
  - match pacing collapsing under too much downtime
  - exploit or cheat loops destroying economy trust
- This genre needs explicit architecture for:
  - raid authority
  - stash versus raid inventory
  - extraction timing and escape rules
  - loss-state readability
  - anti-cheat or exploit-resistant economy trust

## Primary sources
- [Hunt: Showdown 1896 on Steam](https://store.steampowered.com/app/594650/Hunt_Showdown/)
- [Hunt: Showdown official site](https://www.huntshowdown.com/)
- [Hunt: Showdown Early Access Release Notes](https://www.huntshowdown.com/news/hunt-showdown-early-access-release-notes)

## Why this matters to this repo
- Extraction-lite tasks in this repo should not be treated like ordinary shooter or loot tasks. They are risk-economy and extraction-clarity problems first.
- Agents should explicitly name:
  - what makes the raid valuable
  - what is lost on death
  - how the extraction window is read
  - what keeps the economy honest
- First slices should prove one raid, one extraction, and one meaningful loss state before the design broadens.

## Decision impact
- Future presets and feature briefs should require:
  - session truth for the raid
  - stash versus on-raid ownership
  - readable extraction rules
  - anti-exploit safeguards
  - a clear loss-and-return loop
- When a project selects this genre, route output should surface economy, persistence, and extraction pressure together.
