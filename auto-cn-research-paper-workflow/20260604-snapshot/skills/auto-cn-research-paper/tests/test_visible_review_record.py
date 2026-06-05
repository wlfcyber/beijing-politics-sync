#!/usr/bin/env python3
"""Regression tests for visible web/app external review records."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
VISIBLE_REVIEW = SKILL_DIR / "scripts" / "visible_review_record.py"
RUN_AUDIT = SKILL_DIR / "scripts" / "run_audit.py"


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
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-visible-review-"))
    for name in REQUIRED_FILES:
        (run_dir / name).write_text("# test\n", encoding="utf-8")
    (run_dir / "02_检索日志.md").write_text("人大图书馆 libproxy.ruc.edu.cn\n", encoding="utf-8")
    (run_dir / "07_引用与证据审查.md").write_text("未发现\n", encoding="utf-8")
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
                "- gpt_pro_review_status: pending",
                "- gpt_pro_review_channel: unknown",
                "- gpt_pro_real_submission: false",
                "- gpt_pro_raw_record: unknown",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return run_dir


def test_visible_review_record_updates_one_lane_but_not_final_pass() -> None:
    run_dir = make_run_dir()
    raw = run_dir / "gpt_visible_review.md"
    raw.write_text("verdict: PASS\n", encoding="utf-8")

    result = run_script(
        [
            str(VISIBLE_REVIEW),
            str(run_dir),
            "--lane",
            "gpt_pro",
            "--status",
            "pass",
            "--channel",
            "web_session",
            "--raw-record",
            str(raw),
            "--review-url",
            "https://chatgpt.com/c/example",
        ]
    )

    assert result.returncode == 1, result.stdout
    text = (run_dir / "15_外部评审与迭代计划.md").read_text(encoding="utf-8")
    assert "- external_review_passed: no" in text
    assert "- gpt_pro_review_status: pass" in text
    assert "- gpt_pro_review_channel: web_session" in text
    assert "- gpt_pro_real_submission: true" in text
    assert "- gpt_pro_review_scope: unspecified" in text
    assert f"- gpt_pro_review_run_id: {run_dir.name}" in text
    assert "- gpt_pro_review_recorded_at:" in text
    assert f"- gpt_pro_raw_record: {raw.resolve()}" in text
    assert "https://chatgpt.com/c/example" in text


def test_visible_review_record_allows_final_gate_only_after_both_visible_passes() -> None:
    run_dir = make_run_dir()
    gpt_raw = run_dir / "gpt_visible_review.md"
    claude_raw = run_dir / "claude_visible_review.md"
    gpt_raw.write_text("verdict: PASS\n", encoding="utf-8")
    claude_raw.write_text("verdict: PASS\n", encoding="utf-8")

    first = run_script(
        [
            str(VISIBLE_REVIEW),
            str(run_dir),
            "--lane",
            "gpt_pro",
            "--status",
            "pass",
            "--channel",
            "web_session",
            "--raw-record",
            str(gpt_raw),
            "--review-scope",
            "full_draft",
        ]
    )
    assert first.returncode == 1, first.stdout

    second = run_script(
        [
            str(VISIBLE_REVIEW),
            str(run_dir),
            "--lane",
            "claude_opus",
            "--status",
            "pass",
            "--channel",
            "app_session",
            "--raw-record",
            str(claude_raw),
            "--review-scope",
            "full_draft",
        ]
    )
    assert second.returncode == 0, second.stdout

    audit = run_script([str(RUN_AUDIT), str(run_dir), "--min-fulltext", "0", "--require-external-review"])
    assert audit.returncode == 0, audit.stdout
    assert "external_review_passed=yes" in audit.stdout


def test_external_review_rejects_cross_run_visible_records() -> None:
    run_dir = make_run_dir()
    gpt_raw = run_dir / "gpt_visible_review.md"
    claude_raw = run_dir / "claude_visible_review.md"
    gpt_raw.write_text("verdict: PASS\n", encoding="utf-8")
    claude_raw.write_text("verdict: PASS\n", encoding="utf-8")

    for lane, channel, raw in [
        ("gpt_pro", "web_session", gpt_raw),
        ("claude_opus", "app_session", claude_raw),
    ]:
        result = run_script(
            [
                str(VISIBLE_REVIEW),
                str(run_dir),
                "--lane",
                lane,
                "--status",
                "pass",
                "--channel",
                channel,
                "--raw-record",
                str(raw),
                "--review-scope",
                "full_draft",
            ]
        )
        if lane == "gpt_pro":
            assert result.returncode == 1, result.stdout
        else:
            assert result.returncode == 0, result.stdout

    status_path = run_dir / "15_外部评审与迭代计划.md"
    text = status_path.read_text(encoding="utf-8")
    status_path.write_text(text.replace(f"- gpt_pro_review_run_id: {run_dir.name}", "- gpt_pro_review_run_id: other-run"), encoding="utf-8")

    audit = run_script([str(RUN_AUDIT), str(run_dir), "--min-fulltext", "0", "--require-external-review"])
    assert audit.returncode == 1, audit.stdout
    assert "review run_id mismatch" in audit.stdout


def test_visible_review_record_supplemental_pass_does_not_close_gate() -> None:
    run_dir = make_run_dir()
    gpt_raw = run_dir / "gpt_visible_review.md"
    claude_raw = run_dir / "claude_page_spotcheck.md"
    gpt_raw.write_text("verdict: PASS\nreview_scope: full_draft\n", encoding="utf-8")
    claude_raw.write_text("verdict: PASS\nreview_scope: citation_page_spotcheck\n", encoding="utf-8")

    first = run_script(
        [
            str(VISIBLE_REVIEW),
            str(run_dir),
            "--lane",
            "gpt_pro",
            "--status",
            "pass",
            "--channel",
            "web_session",
            "--raw-record",
            str(gpt_raw),
            "--review-scope",
            "full_draft",
        ]
    )
    assert first.returncode == 1, first.stdout

    second = run_script(
        [
            str(VISIBLE_REVIEW),
            str(run_dir),
            "--lane",
            "claude_opus",
            "--status",
            "pass",
            "--channel",
            "app_session",
            "--raw-record",
            str(claude_raw),
            "--review-scope",
            "citation_page_spotcheck",
        ]
    )
    assert second.returncode == 1, second.stdout

    text = (run_dir / "15_外部评审与迭代计划.md").read_text(encoding="utf-8")
    assert "- external_review_passed: no" in text
    assert "- claude_opus_review_scope: citation_page_spotcheck" in text

    audit = run_script([str(RUN_AUDIT), str(run_dir), "--min-fulltext", "0", "--require-external-review"])
    assert audit.returncode == 1, audit.stdout
    assert "review scope is not full_draft" in audit.stdout


def main() -> int:
    tests = [
        test_visible_review_record_updates_one_lane_but_not_final_pass,
        test_visible_review_record_allows_final_gate_only_after_both_visible_passes,
        test_external_review_rejects_cross_run_visible_records,
        test_visible_review_record_supplemental_pass_does_not_close_gate,
    ]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_visible_review_record_updates_one_lane_but_not_final_pass")
    print("PASS test_visible_review_record_allows_final_gate_only_after_both_visible_passes")
    print("PASS test_external_review_rejects_cross_run_visible_records")
    print("PASS test_visible_review_record_supplemental_pass_does_not_close_gate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
