#!/usr/bin/env python3
"""Regression tests for PDF page-anchor audit pack helpers."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "pdf_page_anchor_audit_pack.py"
SPEC = importlib.util.spec_from_file_location("pdf_page_anchor_audit_pack", SCRIPT)
assert SPEC and SPEC.loader
audit_pack = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit_pack
SPEC.loader.exec_module(audit_pack)


def test_parse_anchor_pages_handles_ranges_and_lists() -> None:
    assert audit_pack.parse_anchor_pages("p.1, p.5, p.8-p.11") == [1, 5, 8, 9, 10, 11]
    assert audit_pack.parse_anchor_pages("p.14-p.15") == [14, 15]
    assert audit_pack.parse_anchor_pages("p.7-p.7") == [7]


def test_parse_rows_handles_ranges_and_singletons() -> None:
    assert audit_pack.parse_rows("45,47,48-50") == {45, 47, 48, 49, 50}


def main() -> int:
    tests = [
        test_parse_anchor_pages_handles_ranges_and_lists,
        test_parse_rows_handles_ranges_and_singletons,
    ]
    for test in tests:
        try:
            test()
        except AssertionError as exc:
            print(f"FAIL {test.__name__}: {exc}")
            return 1
        print(f"PASS {test.__name__}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
