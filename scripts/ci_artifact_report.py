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


def load_json_file(path: Path) -> dict[str, object] | None:
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None


def load_benchmark_report() -> dict[str, object] | None:
    for path in (
        REPO_ROOT / "build" / "bench" / "eval" / "bench-report.json",
        REPO_ROOT / "build" / "bench" / "latest" / "bench-report.json",
    ):
        report = load_json_file(path)
        if report is not None:
            return report
    return None


def load_version_report() -> dict[str, object] | None:
    for path in (
        REPO_ROOT / "build" / "ci" / "version" / "version-report.json",
        REPO_ROOT / "build" / "ci" / "latest" / "version-report.json",
    ):
        report = load_json_file(path)
        if report is not None:
            return report
    return None


def build_report(label: str | None = None) -> dict[str, object]:
    config = load_studio_config()
    project = config.get("project", {}) if isinstance(config.get("project"), dict) else {}
    doc_errors, doc_warnings = collect_doc_findings()
    workflow_failures, workflow_summaries = validate_workflows()
    starter_kit_failures = {engine: validate_kit(engine) for engine in available_starter_kits()}
    benchmark_report = load_benchmark_report()
    version_report = load_version_report()

    remotes = git_output("remote")
    external_dependencies = [
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
    ]
    doc_penalty = len(doc_errors) * 12 + len(doc_warnings) * 4
    workflow_penalty = len(workflow_failures) * 12
    kit_penalty = sum(len(items) for items in starter_kit_failures.values()) * 8
    dependency_penalty = len(external_dependencies) * 4
    # External dependencies are reported separately and gate release readiness,
    # but they should not collapse the repo-quality score for validation use.
    quality_score = max(0, min(100, 100 - doc_penalty - workflow_penalty - kit_penalty))
    readiness = "release-ready" if quality_score >= 90 and not external_dependencies else "validation-ready" if quality_score >= 75 else "needs-attention"
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
            "score": quality_score,
            "readiness": readiness,
            "penalties": {
                "doc_errors": doc_penalty,
                "workflow_failures": workflow_penalty,
                "starter_kit_failures": kit_penalty,
                "external_dependencies": dependency_penalty,
            },
        },
        "workflow_summary": workflow_summaries,
        "benchmark": {
            "report": benchmark_report,
            "summary": {
                "case_count": benchmark_report.get("summary", {}).get("case_count", 0) if benchmark_report else 0,
                "failure_count": benchmark_report.get("summary", {}).get("failure_count", 0) if benchmark_report else 0,
                "score": benchmark_report.get("summary", {}).get("score", 0) if benchmark_report else 0,
                "readiness": benchmark_report.get("summary", {}).get("readiness", "unknown") if benchmark_report else "unknown",
            },
            "artifacts": benchmark_report.get("artifacts", {}) if benchmark_report else {},
        },
        "versioning": {
            "report": version_report,
            "summary": {
                "version": version_report.get("version", "") if version_report else "",
                "tag": version_report.get("tag", "") if version_report else "",
                "status": version_report.get("status", "unknown") if version_report else "unknown",
                "is_prerelease": version_report.get("is_prerelease", False) if version_report else False,
                "failure_count": len(version_report.get("failures", [])) if version_report else 0,
            },
            "artifacts": version_report.get("artifacts", {}) if version_report else {},
        },
        "external_dependencies": external_dependencies,
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
        f"- Quality score: {report['quality']['score']} / 100",
        f"- Readiness: {report['quality']['readiness']}",
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
        f"- Penalties: {quality['penalties']}",
        "",
        "## Benchmark summary",
    ]
    benchmark = report.get("benchmark", {})
    benchmark_summary = benchmark.get("summary", {}) if isinstance(benchmark, dict) else {}
    benchmark_artifacts = benchmark.get("artifacts", {}) if isinstance(benchmark, dict) else {}
    if benchmark_summary and benchmark_summary.get("case_count"):
        lines += [
            f"- Case count: {benchmark_summary.get('case_count')}",
            f"- Failure count: {benchmark_summary.get('failure_count')}",
            f"- Score: {benchmark_summary.get('score')} / 100",
            f"- Readiness: {benchmark_summary.get('readiness')}",
        ]
        if benchmark_artifacts:
            lines += [
                f"- JSON: {benchmark_artifacts.get('json')}",
                f"- Markdown: {benchmark_artifacts.get('markdown')}",
            ]
    else:
        lines.append("- None")
    lines += [
        "",
        "## Version summary",
    ]
    version = report.get("versioning", {})
    version_summary = version.get("summary", {}) if isinstance(version, dict) else {}
    version_artifacts = version.get("artifacts", {}) if isinstance(version, dict) else {}
    if version_summary and version_summary.get("version"):
        lines += [
            f"- Version: {version_summary.get('version')}",
            f"- Tag: {version_summary.get('tag')}",
            f"- Status: {version_summary.get('status')}",
            f"- Prerelease: {version_summary.get('is_prerelease')}",
            f"- Failure count: {version_summary.get('failure_count')}",
        ]
        if version_artifacts:
            lines += [
                f"- JSON: {version_artifacts.get('json')}",
                f"- Markdown: {version_artifacts.get('markdown')}",
            ]
    else:
        lines.append("- None")
    lines += [
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
