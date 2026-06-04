#!/usr/bin/env python3
"""Regression tests for workflow report external-review readiness."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


WORKFLOW_REPORT = Path(__file__).resolve().parents[1] / "scripts" / "workflow_report.py"


def test_workflow_report_does_not_trust_summary_only_external_pass() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-report-test-"))
    (run_dir / "03_文献矩阵.md").write_text("# matrix\n", encoding="utf-8")
    (run_dir / "12_浏览器准入验收.md").write_text("- hands_free_ready: yes\n", encoding="utf-8")
    (run_dir / "15_外部评审与迭代计划.md").write_text("- external_review_passed: yes\n", encoding="utf-8")

    result = subprocess.run(
        [sys.executable, str(WORKFLOW_REPORT), str(run_dir), "--target-fulltext", "0"],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )

    assert result.returncode != 0, result.stdout
    status_text = (run_dir / "workflow_status.md").read_text(encoding="utf-8")
    assert "- external_review_passed: no" in status_text
    assert "- hands_free_workflow_ready: no" in status_text


def main() -> int:
    try:
        test_workflow_report_does_not_trust_summary_only_external_pass()
    except AssertionError as exc:
        print(f"FAIL test_workflow_report_does_not_trust_summary_only_external_pass: {exc}")
        return 1
    print("PASS test_workflow_report_does_not_trust_summary_only_external_pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
