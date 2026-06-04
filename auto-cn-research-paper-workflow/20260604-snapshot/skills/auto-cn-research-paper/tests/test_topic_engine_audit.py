#!/usr/bin/env python3
"""Regression tests for topic-engine readiness auditing."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


TOPIC_AUDIT = Path(__file__).resolve().parents[1] / "scripts" / "topic_engine_audit.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def write_topic_matrix(run_dir: Path, headers: list[str], rows: list[list[str]]) -> None:
    lines = [
        "# 选题评分表",
        "",
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(row) + " |")
    (run_dir / "01_选题评分表.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def test_topic_engine_audit_accepts_complete_topic_matrix() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-topic-pass-"))
    headers = [
        "编号",
        "候选题目",
        "研究对象",
        "方法",
        "文献可得",
        "材料可得",
        "对象清晰",
        "方法可行",
        "原创风险",
        "贡献限度",
        "完成风险",
        "总分",
        "结论",
    ]
    rows = []
    for index in range(1, 21):
        conclusion = "观察"
        if index == 1:
            conclusion = "主选"
        if index in (2, 3, 4):
            conclusion = "备选"
        rows.append(
            [
                f"T{index:02d}",
                f"候选题目{index}",
                "基层治理案例",
                "二次文献分析",
                "5",
                "4",
                "5",
                "4",
                "2",
                "4",
                "2",
                str(30 - index),
                conclusion,
            ]
        )
    write_topic_matrix(run_dir, headers, rows)

    result = run_script([str(TOPIC_AUDIT), str(run_dir)])

    assert result.returncode == 0, result.stdout
    assert "status=PASS" in result.stdout
    assert "candidate_count=20" in result.stdout
    assert "main_selection_count=1" in result.stdout
    assert "backup_count=3" in result.stdout


def test_topic_engine_audit_rejects_missing_dimensions_and_backup_count() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-topic-fail-"))
    headers = [
        "编号",
        "候选题目",
        "研究对象",
        "方法",
        "文献可得",
        "对象清晰",
        "方法可行",
        "原创风险",
        "完成风险",
        "总分",
        "结论",
    ]
    rows = []
    for index in range(1, 20):
        conclusion = "主选" if index == 1 else ("备选" if index in (2, 3, 4, 5) else "观察")
        rows.append(
            [
                f"T{index:02d}",
                f"候选题目{index}",
                "基层治理案例",
                "二次文献分析",
                "5",
                "5",
                "4",
                "2",
                "2",
                str(30 - index),
                conclusion,
            ]
        )
    write_topic_matrix(run_dir, headers, rows)

    result = run_script([str(TOPIC_AUDIT), str(run_dir)])

    assert result.returncode == 1, result.stdout
    assert "status=INCOMPLETE" in result.stdout
    assert "candidate_count=19" in result.stdout
    assert "missing required column: 材料可得" in result.stdout
    assert "missing required column: 贡献限度" in result.stdout
    assert "backup_count must be exactly 3" in result.stdout


def main() -> int:
    tests = [
        test_topic_engine_audit_accepts_complete_topic_matrix,
        test_topic_engine_audit_rejects_missing_dimensions_and_backup_count,
    ]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_topic_engine_audit_accepts_complete_topic_matrix")
    print("PASS test_topic_engine_audit_rejects_missing_dimensions_and_backup_count")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
