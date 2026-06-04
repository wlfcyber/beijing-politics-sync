#!/usr/bin/env python3
"""Regression tests for Mac readiness reporting."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "mac_readiness_report.py"


def test_mac_readiness_report_writes_required_fields() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-mac-readiness-"))
    result = subprocess.run(
        [sys.executable, str(SCRIPT), str(run_dir)],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    assert result.returncode in {0, 1}, result.stdout
    out = run_dir / "mac_readiness_report.md"
    assert out.exists(), result.stdout
    text = out.read_text(encoding="utf-8")
    assert "- platform_system:" in text
    assert "- python3_status:" in text
    assert "- bun_status:" in text
    assert "- claude_status:" in text
    assert "- pro_cli_status:" in text
    assert "- pro_cli_doctor_ready:" in text
    assert "- pro_cli_auth_status:" in text
    assert "- pro_cli_browser_session_status:" in text
    assert "- chrome_app_status:" in text
    assert "- final_user_goal_blocked_by:" in text
    assert "Windows evidence cannot satisfy this Mac gate" in text


def main() -> int:
    try:
        test_mac_readiness_report_writes_required_fields()
    except AssertionError as exc:
        print(f"FAIL test_mac_readiness_report_writes_required_fields: {exc}")
        return 1
    print("PASS test_mac_readiness_report_writes_required_fields")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
