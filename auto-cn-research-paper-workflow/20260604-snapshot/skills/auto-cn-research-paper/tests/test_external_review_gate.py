#!/usr/bin/env python3
"""Regression tests for the external advisor gate."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parents[1] / "scripts"
RUN_AUDIT = SCRIPT_DIR / "run_audit.py"


REQUIRED_FILES = [
    "00_运行状态.md",
    "01_选题评分表.md",
    "02_检索日志.md",
    "03_文献矩阵.md",
    "04_优秀论文范式提取.md",
    "05_论证骨架.md",
    "06_论文初稿.md",
    "07_引用与证据审查.md",
    "08_终稿修改清单.md",
    "09_完成度审计.md",
]


def make_run_dir(external_review_text: str) -> Path:
    root = Path(tempfile.mkdtemp(prefix="auto-cn-paper-test-"))
    for name in REQUIRED_FILES:
        (root / name).write_text("# test\n", encoding="utf-8")
    (root / "02_检索日志.md").write_text("libproxy.ruc.edu.cn\n", encoding="utf-8")
    (root / "07_引用与证据审查.md").write_text("未发现\n", encoding="utf-8")
    (root / "15_外部评审与迭代计划.md").write_text(
        external_review_text.replace("{run_id}", root.name),
        encoding="utf-8",
    )
    return root


def run_external_gate(run_dir: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(RUN_AUDIT),
            str(run_dir),
            "--min-fulltext",
            "0",
            "--require-external-review",
        ],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def test_external_review_summary_alone_is_not_enough() -> None:
    run_dir = make_run_dir("- external_review_passed: yes\n")
    result = run_external_gate(run_dir)

    assert result.returncode != 0, result.stdout
    assert "claude" in result.stdout.lower(), result.stdout
    assert "gpt" in result.stdout.lower(), result.stdout


def test_external_review_requires_both_real_passes() -> None:
    run_dir = make_run_dir(
        "\n".join(
            [
                "- external_review_passed: yes",
                "- claude_opus_review_status: pass",
                "- claude_opus_review_channel: web_session",
                "- claude_opus_real_submission: true",
                "- claude_opus_review_run_id: {run_id}",
                "- claude_opus_review_recorded_at: 2026-06-04T12:00:00+00:00",
                "- claude_opus_raw_record: .codex/advisor-runs/claude.json",
                "- claude_opus_review_scope: full_draft",
                "- gpt_pro_review_status: pass",
                "- gpt_pro_review_channel: web_session",
                "- gpt_pro_real_submission: true",
                "- gpt_pro_review_run_id: {run_id}",
                "- gpt_pro_review_recorded_at: 2026-06-04T12:00:00+00:00",
                "- gpt_pro_raw_record: .codex/advisor-runs/gpt.json",
                "- gpt_pro_review_scope: full_draft",
                "",
            ]
        )
    )
    result = run_external_gate(run_dir)

    assert result.returncode == 0, result.stdout


def test_external_review_rejects_cli_or_api_as_final_channel() -> None:
    run_dir = make_run_dir(
        "\n".join(
            [
                "- external_review_passed: yes",
                "- claude_opus_review_status: pass",
                "- claude_opus_review_channel: app_session",
                "- claude_opus_real_submission: true",
                "- claude_opus_review_run_id: {run_id}",
                "- claude_opus_review_recorded_at: 2026-06-04T12:00:00+00:00",
                "- claude_opus_raw_record: visible-claude-app-review.md",
                "- claude_opus_review_scope: full_draft",
                "- gpt_pro_review_status: pass",
                "- gpt_pro_review_channel: cli_or_api_real_call",
                "- gpt_pro_real_submission: true",
                "- gpt_pro_review_run_id: {run_id}",
                "- gpt_pro_review_recorded_at: 2026-06-04T12:00:00+00:00",
                "- gpt_pro_raw_record: .codex/advisor-runs/gpt.json",
                "- gpt_pro_review_scope: full_draft",
                "",
            ]
        )
    )
    result = run_external_gate(run_dir)

    assert result.returncode != 0, result.stdout
    assert "web/app visible session" in result.stdout, result.stdout


def test_external_review_rejects_supplemental_scope_as_final_pass() -> None:
    run_dir = make_run_dir(
        "\n".join(
            [
                "- external_review_passed: yes",
                "- claude_opus_review_status: pass",
                "- claude_opus_review_channel: app_session",
                "- claude_opus_real_submission: true",
                "- claude_opus_review_run_id: {run_id}",
                "- claude_opus_review_recorded_at: 2026-06-04T12:00:00+00:00",
                "- claude_opus_raw_record: visible-claude-page-spotcheck.md",
                "- claude_opus_review_scope: citation_page_spotcheck",
                "- gpt_pro_review_status: pass",
                "- gpt_pro_review_channel: web_session",
                "- gpt_pro_real_submission: true",
                "- gpt_pro_review_run_id: {run_id}",
                "- gpt_pro_review_recorded_at: 2026-06-04T12:00:00+00:00",
                "- gpt_pro_raw_record: visible-gpt-full-review.md",
                "- gpt_pro_review_scope: full_draft",
                "",
            ]
        )
    )
    result = run_external_gate(run_dir)

    assert result.returncode != 0, result.stdout
    assert "review scope is not full_draft" in result.stdout, result.stdout


def main() -> int:
    tests = [
        test_external_review_summary_alone_is_not_enough,
        test_external_review_requires_both_real_passes,
        test_external_review_rejects_cli_or_api_as_final_channel,
        test_external_review_rejects_supplemental_scope_as_final_pass,
    ]
    failures = 0
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            failures += 1
            print(f"FAIL {test.__name__}: {exc}")
        else:
            print(f"PASS {test.__name__}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
