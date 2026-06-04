#!/usr/bin/env python3
"""Regression tests for current-machine source file auditing."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SOURCE_FILE_AUDIT = Path(__file__).resolve().parents[1] / "scripts" / "source_file_audit.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def write_inventory(run_dir: Path, pdf_path: str, text_path: str) -> None:
    (run_dir / "source_inventory.md").write_text(
        "# Source Inventory\n\n"
        "| File | Type | Size | Header | Text | Evidence status |\n"
        "| --- | --- | --- | --- | --- | --- |\n"
        f"| `{pdf_path}` | pdf | 123 | `25 50 44 46` | `{text_path}` | PDF_or_user_exported; full_text_read |\n"
        "\n- usable_fulltext: 1\n",
        encoding="utf-8",
    )


def test_source_file_audit_accepts_current_local_files() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-source-file-pass-"))
    pdf = run_dir / "source.pdf"
    text = run_dir / "source.txt"
    pdf.write_bytes(b"%PDF-1.4\nfixture\n")
    text.write_text("===== PAGE 1 =====\n数字形式主义\n", encoding="utf-8")
    write_inventory(run_dir, str(pdf), str(text))

    result = run_script([str(SOURCE_FILE_AUDIT), str(run_dir), "--min-current-fulltext", "1"])

    assert result.returncode == 0, result.stdout
    assert "status=PASS" in result.stdout
    assert "current_text_count=1" in result.stdout
    assert "windows_path_count=0" in result.stdout
    report = (run_dir / "23_材料文件迁移审计.md").read_text(encoding="utf-8")
    assert "- current_source_files_ready: yes" in report


def test_source_file_audit_rejects_windows_paths_without_local_files() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-source-file-fail-"))
    write_inventory(
        run_dir,
        r"C:\Users\Administrator\Documents\论文写作\sources\source.pdf",
        r"C:\Users\Administrator\Documents\论文写作\fulltext_extract\source.txt",
    )

    result = run_script([str(SOURCE_FILE_AUDIT), str(run_dir), "--min-current-fulltext", "1"])

    assert result.returncode == 1, result.stdout
    assert "status=INCOMPLETE" in result.stdout
    assert "current_text_count=0" in result.stdout
    assert "windows_path_count=2" in result.stdout
    assert "missing current source file" in result.stdout
    assert "missing current extracted text" in result.stdout
    report = (run_dir / "23_材料文件迁移审计.md").read_text(encoding="utf-8")
    assert "- current_source_files_ready: no" in report
    assert "Windows-era paths are recorded" in report


def test_source_file_audit_counts_matrix_sources_missing_from_inventory() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-source-file-matrix-"))
    html = run_dir / "official.html"
    text = run_dir / "official.txt"
    html.write_text("<html><body>官方全文</body></html>", encoding="utf-8")
    text.write_text("===== PAGE 1 =====\n官方全文\n", encoding="utf-8")
    (run_dir / "source_inventory.md").write_text(
        "# Source Inventory\n\n"
        "| File | Type | Size | Header | Text | Evidence status |\n"
        "| --- | --- | --- | --- | --- | --- |\n",
        encoding="utf-8",
    )
    (run_dir / "03_文献矩阵.md").write_text(
        "# 文献矩阵\n\n"
        "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | 研究对象 | 方法 | 核心观点 | 局限 | 与本文关系 | DOI/URL/数据库记录 |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        f"| S-001 | official_html_full_text；full_text_read | 王五 | 2024 | 官方HTML论文 | 杂志 | 对象 | 方法 | 观点 | 局限 | 关系 | 官方全文页: `https://example.com/article.html`；本地 HTML: `{html}`；提取文本: `{text}` |\n",
        encoding="utf-8",
    )

    result = run_script([str(SOURCE_FILE_AUDIT), str(run_dir), "--min-current-fulltext", "1"])

    assert result.returncode == 0, result.stdout
    assert "status=PASS" in result.stdout
    assert "inventory_row_count=1" in result.stdout
    assert "current_text_count=1" in result.stdout


def main() -> int:
    tests = [
        test_source_file_audit_accepts_current_local_files,
        test_source_file_audit_rejects_windows_paths_without_local_files,
        test_source_file_audit_counts_matrix_sources_missing_from_inventory,
    ]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_source_file_audit_accepts_current_local_files")
    print("PASS test_source_file_audit_rejects_windows_paths_without_local_files")
    print("PASS test_source_file_audit_counts_matrix_sources_missing_from_inventory")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
