# QA Example

## Scope
- First combat room with one dash and one upgrade choice

## Critical cases
| Case | Steps | Expected |
|---|---|---|
| Fresh room clear | Start room, dodge pulse, defeat enemy | Upgrade choice appears |
| Room fail | Take damage until reset | Room resets without stale upgrade state |
| Upgrade branch A | Clear room and choose offensive option | Next attempt damage cadence changes |
| Upgrade branch B | Clear room and choose defensive option | Next attempt survivability changes |

## Edge risks
- pause during pulse telegraph
- retry after fail without ghost state
- input spam during upgrade confirmation

## Exit criteria
- No stale room state after retry
- At least one tester describes the pulse window as readable
