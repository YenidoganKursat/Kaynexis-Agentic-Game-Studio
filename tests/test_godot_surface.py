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


def test_godot_slice_has_local_telemetry_wiring() -> None:
    telemetry_script = (REPO_ROOT / "src" / "telemetry.gd").read_text(encoding="utf-8")
    main_script = (REPO_ROOT / "src" / "main.gd").read_text(encoding="utf-8")

    assert "TELEMETRY_LOG_PATH" in telemetry_script
    assert "combat_room_start" in main_script
    assert "combat_room_fail" in main_script
    assert "combat_room_clear" in main_script
    assert "upgrade_selected" in main_script
    assert "dash_used" in main_script
