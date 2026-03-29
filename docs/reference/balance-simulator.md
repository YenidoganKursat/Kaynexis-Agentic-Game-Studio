# Balance Simulator

Use the balance simulator for quick early economy or progression checks when you need a rough answer before building a full telemetry pipeline.

## Command

```bash
python3 scripts/balance_simulator.py \
  --runs 5000 \
  --success-rate 0.58 \
  --reward-win 18 \
  --reward-loss 7 \
  --upgrade-cost 90 \
  --seed 42 \
  --json
```

## What it estimates

- expected currency per run
- average runs to afford the upgrade
- median runs to afford the upgrade
- p90 runs to afford the upgrade

## When to use it

- tuning first-run reward cadence
- sanity-checking unlock cost pacing
- comparing win/loss reward deltas
- checking whether a progression curve is too generous or too punishing

This tool is intentionally small. It is a planning helper, not a replacement for live telemetry.
