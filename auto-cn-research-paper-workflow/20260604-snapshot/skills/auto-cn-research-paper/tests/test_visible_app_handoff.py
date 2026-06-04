#!/usr/bin/env python3
"""Regression tests for manual visible app handoff records."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
HANDOFF = SKILL_DIR / "scripts" / "visible_app_handoff.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def make_run_dir() -> Path:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-app-handoff-"))
    (run_dir / "27_网页外审精简包.md").write_text("# review pack\nfinal_anchor_ready: no\n", encoding="utf-8")
    (run_dir / "15_外部评审与迭代计划.md").write_text(
        "\n".join(
            [
                "# 外部评审与迭代计划",
                "",
                "- external_review_passed: no",
                "- claude_opus_review_status: pending",
                "- claude_opus_review_channel: unknown",
                "- claude_opus_real_submission: false",
                "- claude_opus_raw_record: unknown",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return run_dir


def test_app_handoff_creates_pending_prompt_without_review_submission() -> None:
    run_dir = make_run_dir()

    result = run_script(
        [
            str(HANDOFF),
            str(run_dir),
            "--lane",
            "claude_opus",
            "--target-app",
            "Claude",
            "--no-copy",
        ]
    )

    assert result.returncode == 0, result.stdout
    assert "status=manual_submission_pending" in result.stdout
    assert "real_submission=false" in result.stdout

    pending_dir = run_dir / "visible_reviews" / "pending"
    prompt_files = list(pending_dir.glob("*_claude_opus_app_handoff_prompt.md"))
    record_files = list((run_dir / "visible_reviews").glob("*_claude_opus_app_handoff_pending.md"))
    assert len(prompt_files) == 1
    assert len(record_files) == 1

    prompt_text = prompt_files[0].read_text(encoding="utf-8")
    assert "final_anchor_ready: no" in prompt_text
    assert "Claude Opus / Opus 4.8 Max" in prompt_text

    record_text = record_files[0].read_text(encoding="utf-8")
    assert "- status: manual_submission_pending" in record_text
    assert "- visible_review_not_submitted: true" in record_text
    assert f"- prompt_file: {prompt_files[0].resolve()}" in record_text

    status_text = (run_dir / "15_外部评审与迭代计划.md").read_text(encoding="utf-8")
    assert "- claude_opus_real_submission: false" in status_text
    assert "manual_submission_pending" not in status_text


def main() -> int:
    tests = [test_app_handoff_creates_pending_prompt_without_review_submission]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_app_handoff_creates_pending_prompt_without_review_submission")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
