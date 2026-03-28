#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

READINESS_ORDER = {
    "needs-attention": 0,
    "validation-ready": 1,
    "release-ready": 2,
}


def load_report(path: Path) -> dict[str, object]:
    if not path.exists():
        raise FileNotFoundError(f"Missing CI report: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"CI report is not an object: {path}")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser(description="Enforce a minimum CI quality score and readiness level.")
    parser.add_argument("--report", type=Path, default=Path("build/ci/latest/ci-report.json"), help="Path to the CI report JSON.")
    parser.add_argument("--min-score", type=int, default=80, help="Minimum acceptable quality score.")
    parser.add_argument(
        "--minimum-readiness",
        choices=sorted(READINESS_ORDER),
        default="validation-ready",
        help="Minimum acceptable readiness label.",
    )
    parser.add_argument("--forbid-external-dependencies", action="store_true", help="Fail if the report still lists external dependencies.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    report = load_report(args.report)
    quality = report.get("quality", {}) if isinstance(report.get("quality"), dict) else {}
    score = int(quality.get("score", -1))
    readiness = str(quality.get("readiness", "needs-attention"))
    external_dependencies = report.get("external_dependencies", [])
    if not isinstance(external_dependencies, list):
        external_dependencies = []

    failures: list[str] = []
    if score < args.min_score:
        failures.append(f"quality score {score} is below minimum {args.min_score}")
    if READINESS_ORDER.get(readiness, -1) < READINESS_ORDER[args.minimum_readiness]:
        failures.append(f"readiness '{readiness}' is below minimum '{args.minimum_readiness}'")
    if args.forbid_external_dependencies and external_dependencies:
        failures.append("external dependencies are still present")

    payload = {
        "report": str(args.report),
        "score": score,
        "readiness": readiness,
        "external_dependencies": external_dependencies,
        "passed": not failures,
        "failures": failures,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        if failures:
            print("CI quality gate failed:")
            for item in failures:
                print(f"- {item}")
        else:
            print(f"CI quality gate passed: score={score}, readiness={readiness}")
    return 0 if not failures else 1


if __name__ == "__main__":
    raise SystemExit(main())
