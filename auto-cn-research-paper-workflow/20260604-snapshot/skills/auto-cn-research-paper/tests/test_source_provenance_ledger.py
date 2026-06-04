#!/usr/bin/env python3
"""Regression tests for source provenance ledger enforcement."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
LEDGER_SCRIPT = SKILL_DIR / "scripts" / "source_provenance_ledger.py"
RUN_AUDIT = SKILL_DIR / "scripts" / "run_audit.py"


def run_script(args: list[str], cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        cwd=str(cwd) if cwd else None,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def write_minimal_run(run_dir: Path) -> Path:
    for name in [
        "00_运行状态.md",
        "01_选题评分表.md",
        "04_优秀论文范式提取.md",
        "05_论证骨架.md",
        "08_终稿修改清单.md",
        "09_完成度审计.md",
    ]:
        (run_dir / name).write_text("ok\n", encoding="utf-8")
    (run_dir / "02_检索日志.md").write_text("人大图书馆 libproxy.ruc.edu.cn 实际检索记录\n详情页: 已打开\n", encoding="utf-8")
    (run_dir / "03_文献矩阵.md").write_text(
        "| 编号 | 核验状态 | 作者 | 年份 | 题名 | 来源 | DOI/URL/数据库记录 |\n"
        "| --- | --- | --- | --- | --- | --- | --- |\n"
        "| S-001 | PDF_or_user_exported | 张三 | 2024 | 示例论文 | 示例期刊 | https://libproxy.ruc.edu.cn/cnki/S001 |\n",
        encoding="utf-8",
    )
    (run_dir / "06_论文初稿.md").write_text("正文引用示例[1]\n\n## 参考文献\n[1] 张三. 示例论文[J]. 示例期刊, 2024: 1-12.\n", encoding="utf-8")
    (run_dir / "07_引用与证据审查.md").write_text("must_fix: 未发现\n", encoding="utf-8")
    (run_dir / "evidence_index.md").write_text("source_count: 1\n", encoding="utf-8")
    (run_dir / "citation_plan.md").write_text("missing_citation_sources: 0\n", encoding="utf-8")
    (run_dir / "citation_page_suggestions.md").write_text("missing_page_suggestions: 0\n", encoding="utf-8")
    pdf = run_dir / "示例论文.pdf"
    pdf.write_bytes(b"%PDF-1.4\nsource provenance fixture\n")
    return pdf


def test_source_provenance_ledger_records_file_hash_and_validates() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-source-ledger-"))
    pdf = write_minimal_run(run_dir)

    result = run_script(
        [
            str(LEDGER_SCRIPT),
            str(run_dir),
            "--add",
            "--source-id",
            "S-001",
            "--title",
            "示例论文",
            "--database",
            "CNKI via RUC Library",
            "--route-url",
            "https://libproxy.ruc.edu.cn/cnki/S001",
            "--method",
            "PDF_or_user_exported",
            "--local-file",
            str(pdf),
        ]
    )

    assert result.returncode == 0, result.stdout
    text = (run_dir / "source_provenance_ledger.md").read_text(encoding="utf-8")
    assert "- provenance_ready: yes" in text
    assert "S-001" in text
    assert "| source_id | run_id | title |" in text
    assert f"| S-001 | {run_dir.name} |" in text
    assert "sha256:" in text
    assert "retrieved_at:" in text

    validate = run_script([str(LEDGER_SCRIPT), str(run_dir), "--validate"])
    assert validate.returncode == 0, validate.stdout
    assert "provenance_ready=yes" in validate.stdout


def test_run_audit_requires_source_provenance_when_requested() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-source-ledger-audit-"))
    pdf = write_minimal_run(run_dir)

    missing = run_script([str(RUN_AUDIT), str(run_dir), "--min-fulltext", "1", "--require-source-provenance"])
    assert missing.returncode == 1, missing.stdout
    assert "source provenance ledger" in missing.stdout

    add = run_script(
        [
            str(LEDGER_SCRIPT),
            str(run_dir),
            "--add",
            "--source-id",
            "S-001",
            "--title",
            "示例论文",
            "--database",
            "CNKI via RUC Library",
            "--route-url",
            "https://libproxy.ruc.edu.cn/cnki/S001",
            "--method",
            "PDF_or_user_exported",
            "--local-file",
            str(pdf),
        ]
    )
    assert add.returncode == 0, add.stdout

    passed = run_script([str(RUN_AUDIT), str(run_dir), "--min-fulltext", "1", "--require-source-provenance"])
    assert passed.returncode == 0, passed.stdout
    assert "source_provenance_ready=yes" in passed.stdout


def test_source_provenance_rejects_cross_run_records() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-source-ledger-cross-run-"))
    pdf = write_minimal_run(run_dir)
    add = run_script(
        [
            str(LEDGER_SCRIPT),
            str(run_dir),
            "--add",
            "--source-id",
            "S-001",
            "--title",
            "示例论文",
            "--database",
            "CNKI via RUC Library",
            "--route-url",
            "https://libproxy.ruc.edu.cn/cnki/S001",
            "--method",
            "PDF_or_user_exported",
            "--local-file",
            str(pdf),
        ]
    )
    assert add.returncode == 0, add.stdout

    ledger = run_dir / "source_provenance_ledger.md"
    text = ledger.read_text(encoding="utf-8")
    ledger.write_text(text.replace(f"| S-001 | {run_dir.name} |", "| S-001 | other-run |"), encoding="utf-8")

    validate = run_script([str(LEDGER_SCRIPT), str(run_dir), "--validate"])
    assert validate.returncode == 1, validate.stdout
    assert "run_id mismatch" in ledger.read_text(encoding="utf-8")


def main() -> int:
    tests = [
        test_source_provenance_ledger_records_file_hash_and_validates,
        test_run_audit_requires_source_provenance_when_requested,
        test_source_provenance_rejects_cross_run_records,
    ]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_source_provenance_ledger_records_file_hash_and_validates")
    print("PASS test_run_audit_requires_source_provenance_when_requested")
    print("PASS test_source_provenance_rejects_cross_run_records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
