#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

from _studio_common import (
    ACTIVE_DIR,
    REPO_ROOT,
    engine_detection_report,
    find_godot_binary,
    find_unity_cli,
    find_unity_hub,
    find_unreal_editor,
    find_unreal_uat,
    has_substantive_files,
    load_root_studio_config,
    repo_summary,
    unity_editor_channel,
)
from validate_docs import collect_doc_findings

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
    engine_report = engine_detection_report()
    resolved_engine = str(engine_report["resolved_engine"])
    config = load_root_studio_config()
    project = config.get("project", {}) if isinstance(config.get("project"), dict) else {}
    supported_engines = [str(item) for item in project.get("supported_engines", [])] if isinstance(project.get("supported_engines"), list) else []
    unity_cli = find_unity_cli()
    unity_channel = unity_editor_channel(unity_cli)
    unity_hub = find_unity_hub()
    unreal_uat = find_unreal_uat()
    unreal_editor = find_unreal_editor()
    if resolved_engine == "unknown":
        findings.append({"severity": "high", "finding": "Engine could not be detected from common repo clues.", "next": "Confirm engine in studio/docs/active/engine-profile.md"})
    if engine_report["mismatch"]:
        findings.append(
            {
                "severity": "high",
                "finding": f"Configured primary engine '{engine_report['configured_slug']}' disagrees with repo clues that still look like '{engine_report['clue_engine']}'.",
                "next": "Treat studio.toml as the source of truth and remove or relocate stale engine-native root files that imply a different primary engine.",
            }
        )
    if resolved_engine == "godot" and not (REPO_ROOT / "export_presets.cfg").exists():
        findings.append({"severity": "high", "finding": "Godot export presets are missing.", "next": "Add export_presets.cfg before treating the repo as release-ready."})
    if resolved_engine == "godot" and not (REPO_ROOT / "scripts" / "godot_smoke.py").exists():
        findings.append({"severity": "medium", "finding": "Godot smoke automation is missing.", "next": "Restore scripts/godot_smoke.py and wire it into local validation."})
    if "godot-4" in supported_engines and not find_godot_binary():
        findings.append({"severity": "medium", "finding": "Godot support exists, but no local Godot binary is configured for runtime/export checks.", "next": "Install Godot 4.x or set GODOT_BIN before claiming engine-backed validation."})
    if "unity-6" in supported_engines and not unity_cli:
        next_step = "Install a Unity editor and set UNITY_CLI before claiming engine-backed Unity validation."
        if unity_hub:
            next_step = "Unity Hub is installed; add a Unity editor version and set UNITY_CLI before claiming engine-backed Unity validation."
        findings.append({"severity": "medium", "finding": "Unity support exists, but no Unity editor CLI is configured.", "next": next_step})
    elif "unity-6" in supported_engines and unity_channel in {"alpha", "beta"}:
        findings.append(
            {
                "severity": "medium",
                "finding": f"Unity support is editor-backed locally, but the detected editor install is {unity_channel}.",
                "next": "Use a stable Unity editor install before treating local Unity coverage as release-grade evidence.",
            }
        )
    if "unreal-5" in supported_engines and not (unreal_uat or unreal_editor):
        findings.append({"severity": "medium", "finding": "Unreal support exists, but no Unreal editor/UAT install is configured.", "next": "Install Unreal Engine and set UNREAL_UAT or UNREAL_EDITOR before claiming engine-backed Unreal validation."})
    if missing_docs:
        findings.append({"severity": "high", "finding": f"Missing critical active docs: {', '.join(missing_docs)}", "next": "Run bootstrap_studio.py or create the docs manually."})
    doc_errors, doc_warnings = collect_doc_findings()
    if doc_errors:
        findings.append({"severity": "high", "finding": f"Active docs are semantically stale or inconsistent: {doc_errors[0]}", "next": "Run validate_docs.py, then fix the active docs until they reflect the configured project truth."})
    elif doc_warnings:
        findings.append({"severity": "medium", "finding": f"Active docs still have unresolved placeholders or warnings: {doc_warnings[0]}", "next": "Resolve the warning and rerun validate_docs.py."})
    if not has_substantive_files(REPO_ROOT / "tests"):
        findings.append({"severity": "medium", "finding": "Tests directory exists but has no substantive tests/files.", "next": "Add smoke/regression coverage or explicit manual validation docs."})
    if not has_substantive_files(REPO_ROOT / "src"):
        findings.append({"severity": "medium", "finding": "Runtime source directory is empty or only placeholders exist.", "next": "Confirm engine-native source layout or update engine-profile.md."})
    if not has_substantive_files(REPO_ROOT / "assets"):
        findings.append({"severity": "low", "finding": "Assets directory is empty or only placeholders exist.", "next": "Fine for a fresh repo; document the actual content pipeline once assets land."})
    if (REPO_ROOT / ".git").exists():
        remote_result = subprocess.run(["git", "remote"], cwd=REPO_ROOT, check=False, capture_output=True, text=True)
        if not [line.strip() for line in remote_result.stdout.splitlines() if line.strip()]:
            findings.append({"severity": "medium", "finding": "No git remote is configured, so GitHub workflows and governance are only theoretical.", "next": "Create a remote and push the repository before treating CI or ruleset guidance as active."})
    engine_native_ready = bool(find_godot_binary()) and bool(unity_cli) and unity_channel == "stable" and bool(unreal_uat or unreal_editor)
    if not engine_native_ready:
        missing_toolchains: list[str] = []
        if not find_godot_binary():
            missing_toolchains.append("Godot")
        if not unity_cli:
            missing_toolchains.append("Unity")
        elif unity_channel in {"alpha", "beta"}:
            missing_toolchains.append("Unity(stable)")
        if not (unreal_uat or unreal_editor):
            missing_toolchains.append("Unreal")
        findings.append(
            {
                "severity": "medium",
                "finding": "Real engine-native release validation is still deferred behind external tool installation.",
                "next": f"Wire the remaining toolchains into local or CI runners before claiming shipping-grade build coverage: {', '.join(missing_toolchains) if missing_toolchains else 'review engine setup state'}.",
            }
        )

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
            print("No major structural gaps detected by the current radar checks.")
    return 0 if args.warn_only or not findings else 1

if __name__ == "__main__":
    raise SystemExit(main())
