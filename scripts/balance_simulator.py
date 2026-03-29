#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import random
from statistics import mean, median


def percentile(sorted_values: list[int], ratio: float) -> int:
    if not sorted_values:
        return 0
    index = min(len(sorted_values) - 1, max(0, int(round((len(sorted_values) - 1) * ratio))))
    return sorted_values[index]


def simulate_runs(
    *,
    runs: int,
    success_rate: float,
    reward_win: int,
    reward_loss: int,
    upgrade_cost: int,
    seed: int,
) -> dict[str, float | int]:
    rng = random.Random(seed)
    currencies: list[int] = []
    runs_to_afford: list[int] = []

    for _ in range(runs):
        currency = 0
        attempts = 0
        while currency < upgrade_cost:
            attempts += 1
            if rng.random() <= success_rate:
                currency += reward_win
            else:
                currency += reward_loss
        currencies.append(currency)
        runs_to_afford.append(attempts)

    ordered = sorted(runs_to_afford)
    return {
        "runs": runs,
        "expected_currency_when_afforded": round(mean(currencies), 2),
        "average_runs_to_afford": round(mean(runs_to_afford), 2),
        "median_runs_to_afford": int(median(runs_to_afford)),
        "p90_runs_to_afford": percentile(ordered, 0.9),
        "upgrade_cost": upgrade_cost,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Run a tiny progression pacing simulation for early balance checks.")
    parser.add_argument("--runs", type=int, default=5000)
    parser.add_argument("--success-rate", type=float, default=0.6)
    parser.add_argument("--reward-win", type=int, default=18)
    parser.add_argument("--reward-loss", type=int, default=7)
    parser.add_argument("--upgrade-cost", type=int, default=90)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    payload = simulate_runs(
        runs=args.runs,
        success_rate=args.success_rate,
        reward_win=args.reward_win,
        reward_loss=args.reward_loss,
        upgrade_cost=args.upgrade_cost,
        seed=args.seed,
    )

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        for key, value in payload.items():
            print(f"{key}: {value}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
