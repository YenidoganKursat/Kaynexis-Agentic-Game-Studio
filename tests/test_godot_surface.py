from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_godot_static_surface() -> None:
    result = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts" / "godot_smoke.py"), "--json", "--static-only"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=False,
    )

    payload = json.loads(result.stdout)
    assert result.returncode == 0, payload
    assert payload["failures"] == []
    assert {"Player", "PulseWarden", "Hud", "ArenaBounds"}.issubset(set(payload["static"]["scene_nodes"]))
    assert {"Linux/X11", "Windows Desktop"}.issubset(set(payload["static"]["presets"]))
