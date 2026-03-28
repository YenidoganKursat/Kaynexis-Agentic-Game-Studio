#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from datetime import datetime, UTC
from pathlib import Path

from _studio_common import (
    REPO_ROOT,
    detect_engine,
    find_godot_binary,
    find_unity_cli,
    find_unity_hub,
    find_unreal_editor,
    find_unreal_uat,
    repo_summary,
    unity_editor_channel,
    write_text,
)
from studio_core import available_starter_kits, load_studio_config
from validate_docs import collect_doc_findings
from validate_engine_kits import validate_kit
from validate_workflows import validate_workflows


def git_output(*args: str) -> str | None:
    result = subprocess.run(["git", *args], cwd=REPO_ROOT, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        return None
    value = result.stdout.strip()
    return value or None


def build_report(label: str | None = None) -> dict[str, object]:
    config = load_studio_config()
    project = config.get("project", {}) if isinstance(config.get("project"), dict) else {}
    doc_errors, doc_warnings = collect_doc_findings()
    workflow_failures, workflow_summaries = validate_workflows()
    starter_kit_failures = {engine: validate_kit(engine) for engine in available_starter_kits()}

    remotes = git_output("remote")
    report = {
        "generated_at_utc": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "label": label or "ci-report",
        "project": {
            "name": project.get("name", REPO_ROOT.name),
            "primary_engine": project.get("primary_engine", "unknown"),
            "supported_engines": project.get("supported_engines", []),
            "platform": project.get("platform", "unknown"),
            "genre": project.get("genre", "unknown"),
        },
        "git": {
            "branch": git_output("branch", "--show-current"),
            "sha": git_output("rev-parse", "--short", "HEAD"),
            "remote_names": [line for line in (remotes or "").splitlines() if line],
        },
        "repo_summary": repo_summary(),
        "runtime": {
            "detected_engine": detect_engine(),
            "godot_bin": find_godot_binary(),
            "unity_cli": find_unity_cli(),
            "unity_hub": find_unity_hub(),
            "unity_channel": unity_editor_channel(find_unity_cli()),
            "unreal_editor": find_unreal_editor(),
            "unreal_uat": find_unreal_uat(),
        },
        "quality": {
            "doc_errors": doc_errors,
            "doc_warnings": doc_warnings,
            "workflow_failures": workflow_failures,
            "starter_kit_failures": starter_kit_failures,
        },
        "workflow_summary": workflow_summaries,
        "external_dependencies": [
            item
            for item in [
                "Configure a git remote before treating GitHub policy as active." if not ((remotes or "").splitlines()) else None,
                "Set GODOT_BIN to enable runtime smoke and export checks." if not find_godot_binary() else None,
                "Unity Hub is present, but no Unity editor CLI is configured yet." if find_unity_hub() and not find_unity_cli() else None,
                "Install Unity and set UNITY_CLI for editor-backed validation." if not find_unity_hub() and not find_unity_cli() else None,
                "Detected Unity editor install is prerelease; use a stable editor before treating coverage as release-grade." if unity_editor_channel(find_unity_cli()) in {"alpha", "beta"} else None,
                "Install Unreal Engine and set UNREAL_UAT or UNREAL_EDITOR for engine-backed packaging validation." if not find_unreal_uat() and not find_unreal_editor() else None,
            ]
            if item
        ],
    }
    return report


def render_markdown(report: dict[str, object]) -> str:
    project = report["project"]
    quality = report["quality"]
    lines = [
        f"# CI Artifact Report — {project['name']}",
        "",
        f"- Generated: {report['generated_at_utc']}",
        f"- Label: {report['label']}",
        f"- Branch: {report['git']['branch'] or 'unknown'}",
        f"- SHA: {report['git']['sha'] or 'unknown'}",
        "",
        "## Project surface",
        f"- Primary engine: {project['primary_engine']}",
        f"- Supported engines: {', '.join(project['supported_engines'])}",
        f"- Platform: {project['platform']}",
        f"- Genre: {project['genre']}",
        "",
        "## Quality summary",
        f"- Doc errors: {len(quality['doc_errors'])}",
        f"- Doc warnings: {len(quality['doc_warnings'])}",
        f"- Workflow failures: {len(quality['workflow_failures'])}",
        f"- Starter-kit failures: {sum(len(items) for items in quality['starter_kit_failures'].values())}",
        "",
        "## External dependencies",
    ]
    dependencies = report["external_dependencies"] or ["- None"]
    for item in dependencies:
        lines.append(f"- {item}" if item != "- None" else item)
    lines += [
        "",
        "## Workflow coverage",
    ]
    for name, summary in report["workflow_summary"].items():
        lines.append(f"- {name}: jobs={', '.join(summary['jobs'])} | triggers={', '.join(summary['triggers'])} | artifact_steps={summary['upload_artifact_steps']}")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate CI artifact reports summarizing repo health and workflow coverage.")
    parser.add_argument("--output-dir", default=str(REPO_ROOT / "build" / "ci" / "latest"))
    parser.add_argument("--label", help="Optional label for the generated report.")
    parser.add_argument("--json", action="store_true", help="Print the report JSON to stdout.")
    args = parser.parse_args()

    output_dir = Path(args.output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    report = build_report(label=args.label)
    json_path = output_dir / "ci-report.json"
    md_path = output_dir / "ci-report.md"
    write_text(json_path, json.dumps(report, indent=2))
    write_text(md_path, render_markdown(report))

    payload = {
        "json": str(json_path),
        "markdown": str(md_path),
        "workflow_failures": len(report["quality"]["workflow_failures"]),
        "doc_errors": len(report["quality"]["doc_errors"]),
    }
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        print(f"Wrote {json_path}")
        print(f"Wrote {md_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
