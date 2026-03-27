#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from _studio_common import ACTIVE_DIR, REPO_ROOT, detect_engine, has_substantive_files, repo_summary

CRITICAL_DOCS = [
    "game-brief.md",
    "genre-starter.md",
    "engine-profile.md",
    "current-sprint.md",
    "milestones.md",
    "risk-register.md",
    "decision-log.md",
]

def main() -> int:
    parser = argparse.ArgumentParser(description="Scan the repo for high-impact missing pieces and top risks.")
    parser.add_argument("--warn-only", action="store_true", help="Never fail, only print warnings.")
    parser.add_argument("--json", action="store_true", help="Emit JSON.")
    args = parser.parse_args()

    missing_docs = [name for name in CRITICAL_DOCS if not (ACTIVE_DIR / name).exists()]
    findings: list[dict[str, str]] = []
    if detect_engine() == "unknown":
        findings.append({"severity": "high", "finding": "Engine could not be detected from common repo clues.", "next": "Confirm engine in studio/docs/active/engine-profile.md"})
    if detect_engine() == "godot" and not (REPO_ROOT / "export_presets.cfg").exists():
        findings.append({"severity": "high", "finding": "Godot export presets are missing.", "next": "Add export_presets.cfg before treating the repo as release-ready."})
    if detect_engine() == "godot" and not (REPO_ROOT / "scripts" / "godot_smoke.py").exists():
        findings.append({"severity": "medium", "finding": "Godot smoke automation is missing.", "next": "Restore scripts/godot_smoke.py and wire it into local validation."})
    if missing_docs:
        findings.append({"severity": "high", "finding": f"Missing critical active docs: {', '.join(missing_docs)}", "next": "Run bootstrap_studio.py or create the docs manually."})
    if not has_substantive_files(REPO_ROOT / "tests"):
        findings.append({"severity": "medium", "finding": "Tests directory exists but has no substantive tests/files.", "next": "Add smoke/regression coverage or explicit manual validation docs."})
    if not has_substantive_files(REPO_ROOT / "src"):
        findings.append({"severity": "medium", "finding": "Runtime source directory is empty or only placeholders exist.", "next": "Confirm engine-native source layout or update engine-profile.md."})
    if not has_substantive_files(REPO_ROOT / "assets"):
        findings.append({"severity": "low", "finding": "Assets directory is empty or only placeholders exist.", "next": "Fine for a fresh repo; document the actual content pipeline once assets land."})

    summary = repo_summary()
    payload = {
        "summary": summary,
        "critical_missing_docs": missing_docs,
        "findings": findings,
    }

    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print("Project Radar")
        print("=============")
        for key, value in summary.items():
            print(f"{key}: {value}")
        print()
        if findings:
            for item in findings:
                print(f"[{item['severity'].upper()}] {item['finding']}")
                print(f"  Next: {item['next']}")
        else:
            print("No major structural gaps found.")
    return 0 if args.warn_only or not findings else 1

if __name__ == "__main__":
    raise SystemExit(main())
