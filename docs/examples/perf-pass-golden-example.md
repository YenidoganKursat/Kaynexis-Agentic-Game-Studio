# Golden Example — Perf Pass

## Scope
- Survivorlike prototype spike from 200 to 900 active enemies

## Baseline
- Avg frame time: 28 ms
- Worst spike: 43 ms
- Repro: 6-minute survival arena with projectile-heavy build

## Likely bottlenecks
- per-enemy update overhead
- projectile allocation churn
- expensive overlap checks at peak density

## Smallest high-impact fixes
- pool projectiles before touching AI behavior
- reduce per-frame expensive queries for off-screen enemies
- separate visual swarm density from full simulation count

## Validation
- Re-run same 6-minute scenario
- Capture frame time before and after
- Reject changes that improve perf but break dodge readability
