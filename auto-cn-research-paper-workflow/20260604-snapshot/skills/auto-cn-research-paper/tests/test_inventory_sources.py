#!/usr/bin/env python3
"""Regression tests for source inventory generation."""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "inventory_sources.py"


def run_script(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )


def test_inventory_accepts_official_html_full_text() -> None:
    temp = Path(tempfile.mkdtemp(prefix="auto-cn-paper-inventory-html-"))
    sources = temp / "sources"
    texts = temp / "texts"
    sources.mkdir()
    texts.mkdir()
    (sources / "official_source.html").write_text("<html><body>全文</body></html>", encoding="utf-8")
    (texts / "official_source.txt").write_text("全文", encoding="utf-8")

    result = run_script(
        [
            "--download-dir",
            str(sources),
            "--text-dir",
            str(texts),
            "--pattern",
            "*.html",
            "--out",
            str(temp / "source_inventory.md"),
        ]
    )

    assert result.returncode == 0, result.stdout
    text = (temp / "source_inventory.md").read_text(encoding="utf-8")
    assert "- usable_fulltext: 1" in text
    assert "official_html_full_text; full_text_read" in text


def main() -> int:
    tests = [test_inventory_accepts_official_html_full_text]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
    print("PASS test_inventory_accepts_official_html_full_text")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
