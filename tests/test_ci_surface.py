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
    assert "repo-validate.yml" in summaries
    assert "starter-kit-contracts.yml" in summaries
    assert "release-readiness.yml" in summaries
    assert "nightly-audit.yml" in summaries


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
    assert "docs/reference/ci-cd-architecture.md" in recommended
    assert "docs/reference/genre-presets.md" in recommended
