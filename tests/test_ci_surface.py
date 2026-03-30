from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = REPO_ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from validate_workflows import validate_workflows


def test_validate_workflows_surface() -> None:
    failures, summaries = validate_workflows()
    assert failures == []
    assert "validate.yml" in summaries
    assert "repo-validate.yml" in summaries
    assert "doc-sync.yml" in summaries
    assert "starter-kit-contracts.yml" in summaries
    assert "release-readiness.yml" in summaries
    assert "nightly-audit.yml" in summaries
    validate_runs = "\n".join(summaries["validate.yml"]["runs"])
    assert "scripts/version_guard.py" in validate_runs
    assert "scripts/ci_quality_gate.py" in validate_runs
    doc_sync_runs = "\n".join(summaries["doc-sync.yml"]["runs"])
    assert "scripts/resolve_changed_paths.py" in doc_sync_runs
    repo_validate_runs = "\n".join(summaries["repo-validate.yml"]["runs"])
    assert "scripts/resolve_changed_paths.py" in repo_validate_runs
    release_runs = "\n".join(summaries["release-readiness.yml"]["runs"])
    assert "release-ready" in release_runs
    assert "forbid-external-dependencies" in release_runs


def test_doctor_includes_validate_workflow_surface() -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "doctor.py"), "--json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    payload = json.loads(result.stdout)
    github_automation = next(check for check in payload["checks"] if check["name"] == "github-automation")
    assert github_automation["status"] == "pass"
    assert "validate.yml" in github_automation["detail"]


def test_ci_artifact_report_generates_files() -> None:
    output_dir = REPO_ROOT / "build" / "ci" / "pytest-surface"
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "ci_artifact_report.py"), "--output-dir", str(output_dir), "--json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    payload = json.loads(result.stdout)
    assert Path(payload["json"]).exists()
    assert Path(payload["markdown"]).exists()
    report = json.loads(Path(payload["json"]).read_text())
    assert report["project"]["name"] == "Kaynexis Agentic Game Studio"
    assert 0 <= report["quality"]["score"] <= 100
    assert report["quality"]["readiness"] in {"needs-attention", "validation-ready", "release-ready"}
    assert "unity_cli" in report["runtime"]
    assert "unity_hub" in report["runtime"]
    assert "unity_channel" in report["runtime"]
    assert "unreal_uat" in report["runtime"]
    assert "unreal_editor" in report["runtime"]


def test_starter_kit_contract_smoke_unity_surface() -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "starter_kit_contract_smoke.py"), "--engine", "unity-6", "--json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    payload = json.loads(result.stdout)
    assert payload["failures"] == []


def test_doc_sync_audit_is_surface_checked() -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "doc_sync_audit.py"), "src/main.gd", "scripts/route_task.py", "studio/presets/genre/metroidvania.md", "--json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    payload = json.loads(result.stdout)
    recommended = {item["doc"] for item in payload["recommendations"]}
    assert "docs/reference/ci-cd.md" in recommended
    assert "docs/reference/genre-presets.md" in recommended


def test_doc_sync_guard_and_quality_gate_surface() -> None:
    guard = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "doc_sync_guard.py"), "scripts/route_task.py", "src/main.gd", "--json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert guard.returncode == 1, guard.stdout or guard.stderr
    guard_payload = json.loads(guard.stdout)
    assert guard_payload["passed"] is False
    assert guard_payload["missing_docs"]

    report_dir = REPO_ROOT / "build" / "ci" / "pytest-quality"
    report = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "ci_artifact_report.py"), "--output-dir", str(report_dir), "--json"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert report.returncode == 0, report.stderr or report.stdout

    quality = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "ci_quality_gate.py"),
            "--report",
            str(report_dir / "ci-report.json"),
            "--min-score",
            "80",
            "--minimum-readiness",
            "validation-ready",
            "--json",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert quality.returncode == 0, quality.stderr or quality.stdout
    quality_payload = json.loads(quality.stdout)
    assert quality_payload["passed"] is True


def test_doc_sync_guard_skips_dependabot_pr_when_explicitly_allowed(tmp_path: Path) -> None:
    paths_file = tmp_path / "changed-paths.txt"
    paths_file.write_text(".github/workflows/repo-validate.yml\n", encoding="utf-8")

    guard = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "doc_sync_guard.py"),
            "--paths-file",
            str(paths_file),
            "--allow-dependabot-pr",
            "--pr-author",
            "dependabot[bot]",
            "--json",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert guard.returncode == 0, guard.stdout or guard.stderr
    guard_payload = json.loads(guard.stdout)
    assert guard_payload["passed"] is True
    assert guard_payload["skipped"] is True
    assert guard_payload["skip_reason"] == "dependabot pull request"
    assert guard_payload["missing_docs"] == []


def test_resolve_changed_paths_falls_back_when_base_sha_is_missing(tmp_path: Path) -> None:
    changed_paths = tmp_path / "changed-paths.txt"
    bogus_sha = "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef"

    result = subprocess.run(
        [
            sys.executable,
            str(REPO_ROOT / "scripts" / "resolve_changed_paths.py"),
            "--base-sha",
            bogus_sha,
            "--paths-file",
            str(changed_paths),
            "--json",
        ],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr or result.stdout
    payload = json.loads(result.stdout)
    assert payload["requested_base_sha"] == bogus_sha
    assert payload["resolved_base_sha"] != bogus_sha
    assert payload["paths"] == changed_paths.read_text(encoding="utf-8").splitlines()
