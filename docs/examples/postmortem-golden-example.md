# Golden Example — Postmortem

## Outcome
- First combat room reached playable state with readable reset loop and upgrade choice

## What worked
- Small scope prevented feature drift
- One enemy archetype exposed fairness problems early
- Manual smoke path stayed current with code changes

## What failed
- Upgrade choice arrived before combat readability was fully stable
- Too much timing logic lived in one script early on

## What changes next
- Add a traceability doc for the next slice
- Require one readability validation note before adding a second enemy
- Keep upgrade tuning behind a separate test pass
