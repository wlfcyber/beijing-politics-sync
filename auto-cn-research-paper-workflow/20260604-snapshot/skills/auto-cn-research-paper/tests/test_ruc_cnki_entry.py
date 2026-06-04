#!/usr/bin/env python3
"""Regression tests for RUC/CNKI entry discovery and opening."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "ruc_cnki_entry.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def test_ruc_cnki_entry_lists_official_candidates() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-ruc-entry-"))
    result = run_script([str(run_dir), "--list"])

    assert result.returncode == 0, result.stdout
    out = run_dir / "ruc_cnki_entry_candidates.md"
    assert out.exists(), result.stdout
    text = out.read_text(encoding="utf-8")
    assert "中国知网-中国期刊全文数据库（网络版）" in text
    assert "rid=114" in text
    assert "libproxy.ruc.edu.cn/ermsClient/eresourceInfo.do?rid=114" in text
    assert "libproxy.ruc.edu.cn/entry.do?rid=114&uid=249" in text


def test_ruc_cnki_entry_dry_run_records_selected_target() -> None:
    run_dir = Path(tempfile.mkdtemp(prefix="auto-cn-paper-ruc-entry-open-"))
    result = run_script([str(run_dir), "--open", "--mode", "offcampus", "--dry-run"])

    assert result.returncode == 0, result.stdout
    text = (run_dir / "ruc_cnki_entry_open.md").read_text(encoding="utf-8")
    assert "- open_status: dry_run" in text
    assert "- selected_mode: offcampus" in text
    assert "- selected_url: https://libproxy.ruc.edu.cn/entry.do?rid=114&uid=249" in text
    assert "用户必须自行完成登录" in text


def main() -> int:
    tests = [
        test_ruc_cnki_entry_lists_official_candidates,
        test_ruc_cnki_entry_dry_run_records_selected_target,
    ]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_ruc_cnki_entry_lists_official_candidates")
    print("PASS test_ruc_cnki_entry_dry_run_records_selected_target")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
