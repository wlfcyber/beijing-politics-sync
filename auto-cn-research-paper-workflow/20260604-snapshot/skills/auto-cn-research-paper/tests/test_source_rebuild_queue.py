#!/usr/bin/env python3
"""Regression tests for current-machine source rebuild queue generation."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


REBUILD_QUEUE = Path(__file__).resolve().parents[1] / "scripts" / "source_rebuild_queue.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def write_matrix(run_dir: Path) -> None:
    (run_dir / "03_文献矩阵.md").write_text(
        "# 文献矩阵\n\n"
        "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        "| S-001 | PDF_or_user_exported；full_text_read | 张三 | 2026 | CNKI论文 | 学报 | 对象 | 方法 | 观点 | 局限 | 关系 | DOI: `10.123/test`；PDF: `C:\\Users\\Administrator\\Downloads\\cnki.pdf` |\n"
        "| S-002 | PDF_or_user_exported；full_text_read；public_journal_pdf | 李四 | 2023 | 公开PDF论文 | 期刊 | 对象 | 方法 | 观点 | 局限 | 关系 | 官方 PDF: `https://example.com/paper.pdf`；本地 PDF: `C:\\Users\\Administrator\\Documents\\paper.pdf` |\n"
        "| S-003 | official_html_full_text；full_text_read | 王五 | 2024 | 官方HTML论文 | 杂志 | 对象 | 方法 | 观点 | 局限 | 关系 | 官方全文页: `https://example.com/article.html`；提取文本: `C:\\Users\\Administrator\\Documents\\article.txt` |\n",
        encoding="utf-8",
    )


def write_migration_audit(run_dir: Path) -> None:
    (run_dir / "23_材料文件迁移审计.md").write_text(
        "# 材料文件迁移审计\n\n"
        "## Inventory Rows\n\n"
        "| Recorded source | Current source | Recorded text | Current text | Evidence status |\n"
        "| --- | --- | --- | --- | --- |\n"
        "| C:\\Users\\Administrator\\Downloads\\cnki.pdf | missing | C:\\Users\\Administrator\\Documents\\cnki.txt | missing | PDF_or_user_exported; full_text_read |\n"
        "| C:\\Users\\Administrator\\Documents\\paper.pdf | missing | C:\\Users\\Administrator\\Documents\\paper.txt | missing | PDF_or_user_exported; full_text_read |\n"
        "| C:\\Users\\Administrator\\Documents\\article.html | missing | C:\\Users\\Administrator\\Documents\\article.txt | missing | official_html_full_text; full_text_read |\n",
        encoding="utf-8",
    )


def test_source_rebuild_queue_classifies_missing_sources() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-rebuild-queue-"))
    write_matrix(run_dir)
    write_migration_audit(run_dir)

    result = run_script([str(REBUILD_QUEUE), str(run_dir)])

    assert result.returncode == 0, result.stdout
    assert "status=INCOMPLETE" in result.stdout
    assert "rebuild_item_count=3" in result.stdout
    assert "public_download_count=2" in result.stdout
    assert "authorized_database_count=1" in result.stdout
    report = (run_dir / "24_Mac材料重建队列.md").read_text(encoding="utf-8")
    assert "S-001" in report
    assert "需人大/CNKI重拉或人工迁移" in report
    assert "S-002" in report
    assert "可公开官方下载" in report
    assert "https://example.com/paper.pdf" in report
    assert "S-003" in report
    assert "可公开官方HTML抓取" in report
    assert "下一步脚本" in report


def main() -> int:
    try:
        test_source_rebuild_queue_classifies_missing_sources()
    except AssertionError as exc:
        print(f"FAIL test_source_rebuild_queue_classifies_missing_sources: {exc}")
        return 1
    print("PASS test_source_rebuild_queue_classifies_missing_sources")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
