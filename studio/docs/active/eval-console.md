# Eval Plan — Console Readiness Lane

## Change under test
- The repo now has a dedicated console lane for PS5-like, Xbox-like, and Switch-like targets.

## Goal
- Prove that console readiness is surfaced as a distinct porting and certification path instead of being absorbed into generic platform notes.

## Risks
- PS5-like work may still be treated like desktop porting if the family split is not explicit.
- Submission evidence can be under-specified if the guide, example, and checklist drift apart.
- Controller-first UX, suspend/resume, and save/entitlement assumptions can be forgotten if they are not in the active docs.

## Validation
- Route a PS5-like task and verify the console guide, example, and research note appear in the surfaced docs.
- Resolve the console checklist and verify the platform family split, cert risk, and submission assumptions are present.
- Confirm the platform target matrix includes a console row and the cert checklist template is referenced.

## Success criteria
- Console work is visible as its own lane.
- The console guide, example, research note, checklist, and platform target matrix stay synchronized.
- The repo can explain console readiness without collapsing PS5-like work into a generic port note.
