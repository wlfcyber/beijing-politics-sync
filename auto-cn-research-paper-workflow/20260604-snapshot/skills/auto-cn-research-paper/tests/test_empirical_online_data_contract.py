#!/usr/bin/env python3
"""Regression tests for online empirical-data workflow rules."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
SKILL_MD = SKILL_DIR / "SKILL.md"
INIT_RUN = SKILL_DIR / "scripts" / "init_run.py"
FINAL_REVIEW_PACKET = SKILL_DIR / "scripts" / "final_review_packet.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def test_skill_accepts_crawlable_online_empirical_data() -> None:
    text = SKILL_MD.read_text(encoding="utf-8")
    assert "`online_public_dataset`" in text
    assert "公开或授权在线数据" in text
    assert "爬虫" in text
    assert "empirical_data_ledger.md" in text


def test_init_run_creates_empirical_data_ledger() -> None:
    workspace = Path(tempfile.mkdtemp(prefix="auto-cn-paper-empirical-init-"))
    result = run_script([str(INIT_RUN), "--workspace", str(workspace), "--theme", "基层数字治理"])
    assert result.returncode == 0, result.stdout

    run_dir = Path(result.stdout.strip())
    status = (run_dir / "00_运行状态.md").read_text(encoding="utf-8")
    ledger = run_dir / "empirical_data_ledger.md"
    assert "| 实证路线 | 待选择" in status
    assert ledger.exists(), result.stdout
    ledger_text = ledger.read_text(encoding="utf-8")
    assert "- empirical_route: pending" in ledger_text
    assert "- data_collection_status: pending" in ledger_text
    assert "online_public_dataset" in ledger_text
    assert "公开或授权在线数据" in ledger_text


def test_final_review_packet_includes_empirical_ledger() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-empirical-packet-"))
    (run_dir / "06_论文初稿.md").write_text("# 论文初稿\n\n正文。\n", encoding="utf-8")
    (run_dir / "15_外部评审与迭代计划.md").write_text("- external_review_passed: no\n", encoding="utf-8")
    (run_dir / "citation_final.md").write_text("- final_anchor_ready: yes\n", encoding="utf-8")
    (run_dir / "empirical_data_ledger.md").write_text(
        "\n".join(
            [
                "# 实证数据采集台账",
                "",
                "- empirical_route: online_public_dataset",
                "- data_collection_status: verified",
                "- source_access_type: public_web",
                "- crawler_compliance: public_allowed",
                "- records_collected: 128",
                "- dataset_hash: sha256:test",
                "",
            ]
        ),
        encoding="utf-8",
    )

    result = run_script([str(FINAL_REVIEW_PACKET), str(run_dir)])
    assert result.returncode == 0, result.stdout

    review_packet = (run_dir / "26_最终外部评审包.md").read_text(encoding="utf-8")
    web_packet = (run_dir / "27_网页外审精简包.md").read_text(encoding="utf-8")
    assert "### File: empirical_data_ledger.md" in review_packet
    assert "## 实证数据采集摘要" in web_packet
    assert "- empirical_route: online_public_dataset" in web_packet
    assert "- records_collected: 128" in web_packet


def main() -> int:
    for test in [
        test_skill_accepts_crawlable_online_empirical_data,
        test_init_run_creates_empirical_data_ledger,
        test_final_review_packet_includes_empirical_ledger,
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
