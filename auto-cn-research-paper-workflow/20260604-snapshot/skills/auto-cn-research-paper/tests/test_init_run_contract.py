#!/usr/bin/env python3
"""Regression tests for run initialization artifacts."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


INIT_RUN = Path(__file__).resolve().parents[1] / "scripts" / "init_run.py"


def test_init_run_creates_external_review_contract() -> None:
    workspace = Path(tempfile.mkdtemp(prefix="auto-cn-paper-init-test-"))
    result = subprocess.run(
        [sys.executable, str(INIT_RUN), "--workspace", str(workspace), "--theme", "基层数字治理"],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    assert result.returncode == 0, result.stdout

    run_dir = Path(result.stdout.strip())
    external_review = run_dir / "15_外部评审与迭代计划.md"
    assert external_review.exists(), result.stdout
    text = external_review.read_text(encoding="utf-8")
    assert "- external_review_passed: no" in text
    assert "- claude_opus_review_status: pending" in text
    assert "- claude_opus_review_channel: unknown" in text
    assert "- claude_opus_real_submission: false" in text
    assert "- claude_opus_review_scope: unspecified" in text
    assert "- claude_opus_review_run_id: unknown" in text
    assert "- claude_opus_review_recorded_at: unknown" in text
    assert "- gpt_pro_review_status: pending" in text
    assert "- gpt_pro_review_channel: unknown" in text
    assert "- gpt_pro_real_submission: false" in text
    assert "- gpt_pro_review_scope: unspecified" in text
    assert "- gpt_pro_review_run_id: unknown" in text
    assert "- gpt_pro_review_recorded_at: unknown" in text
    assert "review_scope=full_draft" in text


def main() -> int:
    try:
        test_init_run_creates_external_review_contract()
    except AssertionError as exc:
        print(f"FAIL test_init_run_creates_external_review_contract: {exc}")
        return 1
    print("PASS test_init_run_creates_external_review_contract")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
