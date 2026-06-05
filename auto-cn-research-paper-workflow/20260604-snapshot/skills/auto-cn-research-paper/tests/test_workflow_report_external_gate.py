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


def test_workflow_report_rejects_spotcheck_scope_external_pass() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-report-scope-test-"))
    (run_dir / "03_文献矩阵.md").write_text("# matrix\n", encoding="utf-8")
    (run_dir / "12_浏览器准入验收.md").write_text("- hands_free_ready: yes\n", encoding="utf-8")
    (run_dir / "15_外部评审与迭代计划.md").write_text(
        "\n".join(
            [
                "- external_review_passed: yes",
                "- claude_opus_review_status: pass",
                "- claude_opus_review_channel: app_session",
                "- claude_opus_real_submission: true",
                f"- claude_opus_review_run_id: {run_dir.name}",
                "- claude_opus_review_recorded_at: 2026-06-04T12:00:00+00:00",
                "- claude_opus_raw_record: visible-claude-page-spotcheck.md",
                "- claude_opus_review_scope: citation_page_spotcheck",
                "- gpt_pro_review_status: pass",
                "- gpt_pro_review_channel: web_session",
                "- gpt_pro_real_submission: true",
                f"- gpt_pro_review_run_id: {run_dir.name}",
                "- gpt_pro_review_recorded_at: 2026-06-04T12:00:00+00:00",
                "- gpt_pro_raw_record: visible-gpt-full-review.md",
                "- gpt_pro_review_scope: full_draft",
                "",
            ]
        ),
        encoding="utf-8",
    )

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
    for test in [
        test_workflow_report_does_not_trust_summary_only_external_pass,
        test_workflow_report_rejects_spotcheck_scope_external_pass,
    ]:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
        print(f"PASS {test.__name__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
