# Eval Plan: Sector Intel

## Change under test

- Canonical sector intelligence source pack and routing surface for current industry, market, platform, and policy signals.

## Goal

- The agent should be able to answer "what is current?" with a source-backed snapshot that clearly separates facts from inference.

## Cases

1. "Summarize the current game-industry signals that matter for a Steam-first indie survival game."
2. "Track the latest platform-policy and accessibility changes that could affect a mobile release plan."
3. "Build a current sector watch for a cross-platform live game and name the source window."

## Pass conditions

- The agent names the source family before summarizing.
- The agent names the date window or report window.
- The agent separates source facts from implication.
- The agent ends with one clear next step.

## Failure modes

- The agent cites stale info without a date window.
- The agent uses blog or social commentary as the main source.
- The agent blurs facts and inference together.
- The agent gives generic advice instead of current sector signals.

## Validation

- `python3 scripts/route_task.py "Summarize current game-industry signals for a Steam-first indie survival game" --json`
- `python3 scripts/codex_studio.py checklist --task "Track current sector signals for a Steam-first indie survival game" --json`
- `python3 scripts/validate_docs.py`
- `python3 scripts/validate_repo_layout.py`
