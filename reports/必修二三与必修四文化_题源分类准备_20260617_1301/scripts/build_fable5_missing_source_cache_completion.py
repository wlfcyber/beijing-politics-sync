#!/usr/bin/env python3
from __future__ import annotations

import csv
import shutil
from collections import Counter, defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
SOURCE_INVENTORY = RUN_DIR / "01_source_inventory" / "source_inventory.csv"
CACHE_MANIFEST = RUN_DIR / "02_text_cache" / "cache_manifest.csv"
TEXT_DIR = RUN_DIR / "02_text_cache" / "texts"
REPORT = RUN_DIR / "05_reports" / "fable5_missing_source_cache_completion_report.md"
AUDIT = RUN_DIR / "05_reports" / "fable5_missing_source_cache_completion_audit.csv"

PREPROCESSED_ROOT = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus")
PREPROCESSED_MANIFEST = PREPROCESSED_ROOT / "manifest.csv"

SPECIAL_OCR = {
    "5581e0237e861511efb8400525d43aa042ca59a4fa0878e1e249617f4397ecc2": RUN_DIR / "02_text_cache" / "ocr_cache" / "2026_西城_一模_pdf_paper" / "2026北京西城高三一模政治.ocr.txt",
    "54715a1e650d940e1470d8348f9c4cfaaa4a92cb983965a022b2fae5049ca1a4": RUN_DIR / "02_text_cache" / "ocr_cache" / "2026_西城_期末_细则_pdf" / "细则.ocr.txt",
}

HARD_EXCLUDED_SUITES = {"2026_石景山_期末"}


def load_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), list(reader.fieldnames or [])


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def preprocessed_rows() -> dict[str, dict[str, str]]:
    if not PREPROCESSED_MANIFEST.exists():
        return {}
    rows, _ = load_csv(PREPROCESSED_MANIFEST)
    return {row.get("sha256", ""): row for row in rows if row.get("sha256")}


def mac_pre_text_path(pre_row: dict[str, str]) -> Path | None:
    text_path = pre_row.get("text_path", "")
    if not text_path:
        return None
    name = Path(text_path.replace("\\", "/")).name
    path = PREPROCESSED_ROOT / "texts" / name
    return path if path.exists() else None


def is_placeholder_text(path: Path) -> bool:
    if not path.exists() or path.stat().st_size == 0:
        return True
    text = path.read_text(encoding="utf-8", errors="replace")
    markers = [
        "No reliable text layer was extracted",
        "rendered-ocr-needed",
        "chars: `0`",
    ]
    return any(marker in text for marker in markers)


def choose_representative(rows: list[dict[str, str]]) -> dict[str, str]:
    def score(row: dict[str, str]) -> tuple[int, int, int]:
        status = row.get("status", "")
        source_type = row.get("source_type", "")
        return (
            0 if status == "inventory-only" else 1 if status == "module-boundary-excluded" else 2,
            0 if source_type in {"paper", "rubric", "marking-report"} else 1,
            len(row.get("file_path", "")),
        )

    return sorted(rows, key=score)[0]


def build_text(row: dict[str, str], pre_by_sha: dict[str, dict[str, str]]) -> tuple[str, str, str, str]:
    sha = row["sha256"]
    target = TEXT_DIR / f"{sha[:16]}.txt"

    if row.get("suite_id") in HARD_EXCLUDED_SUITES or row.get("status") == "module-boundary-excluded":
        return "skipped-excluded", "", "", "excluded_by_hard_rule_not_required_for_b2_b3_b4_culture_handoff"

    special = SPECIAL_OCR.get(sha)
    if special:
        if not special.exists():
            raise SystemExit(f"missing special OCR text: {special}")
        if target.exists() and not is_placeholder_text(target):
            backup = TEXT_DIR / f"{sha[:16]}.pre_fable5_completion_backup.txt"
            if not backup.exists():
                shutil.copy2(target, backup)
        shutil.copy2(special, target)
        return "raw-extracted", str(target), str(special), "added_missing_source_for_fable5_cache_completion; method=apple_vision_ocr"

    if target.exists() and not is_placeholder_text(target):
        return "raw-extracted", str(target), row.get("file_path", ""), "added_missing_source_for_fable5_cache_completion; method=existing_run_text"

    pre_text = mac_pre_text_path(pre_by_sha.get(sha, {}))
    if pre_text and not is_placeholder_text(pre_text):
        shutil.copy2(pre_text, target)
        return "cache-hit", str(target), str(pre_text), "added_missing_source_for_fable5_cache_completion; method=preprocessed_corpus_text"

    if target.exists() and target.stat().st_size > 0:
        return "raw-extracted", str(target), row.get("file_path", ""), "added_missing_source_for_fable5_cache_completion; method=existing_run_text_placeholder_boundary"

    return "empty-or-unsupported", "", "", "missing_readable_text_after_cache_completion"


def main() -> int:
    inv_rows, _ = load_csv(SOURCE_INVENTORY)
    cache_rows, cache_fields = load_csv(CACHE_MANIFEST)
    pre_by_sha = preprocessed_rows()
    existing_sha = {row.get("sha256", "") for row in cache_rows}

    by_sha: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inv_rows:
        if row.get("sha256") and row["sha256"] not in existing_sha:
            by_sha[row["sha256"]].append(row)

    audit_rows: list[dict[str, str]] = []
    for sha, rows in sorted(by_sha.items()):
        rep = choose_representative(rows)
        extraction_status, run_text_path, source_text_path, note = build_text(rep, pre_by_sha)
        char_count = "0"
        if run_text_path and Path(run_text_path).exists():
            char_count = str(len(Path(run_text_path).read_text(encoding="utf-8", errors="replace")))
        cache_rows.append(
            {
                "suite_id": rep.get("suite_id", ""),
                "year": rep.get("year", ""),
                "district": rep.get("district", ""),
                "stage": rep.get("stage", ""),
                "source_type": rep.get("source_type", ""),
                "file_path": rep.get("file_path", ""),
                "sha256": sha,
                "cache_hit": "yes" if extraction_status == "cache-hit" else "no",
                "extraction_status": extraction_status,
                "char_count": char_count,
                "run_text_path": run_text_path,
                "source_text_path": source_text_path,
                "error": note,
            }
        )
        audit_rows.append(
            {
                "suite_id": rep.get("suite_id", ""),
                "source_type": rep.get("source_type", ""),
                "status": rep.get("status", ""),
                "file_type": rep.get("file_type", ""),
                "file_path": rep.get("file_path", ""),
                "sha256": sha,
                "duplicate_source_rows": str(len(rows)),
                "extraction_status": extraction_status,
                "run_text_path": run_text_path,
                "source_text_path": source_text_path,
                "char_count": char_count,
                "note": note,
            }
        )

    write_csv(CACHE_MANIFEST, cache_rows, cache_fields)
    audit_fields = [
        "suite_id",
        "source_type",
        "status",
        "file_type",
        "file_path",
        "sha256",
        "duplicate_source_rows",
        "extraction_status",
        "run_text_path",
        "source_text_path",
        "char_count",
        "note",
    ]
    write_csv(AUDIT, audit_rows, audit_fields)

    status_counts = Counter(row["extraction_status"] for row in cache_rows)
    source_counts = Counter(row["source_type"] for row in cache_rows)
    added_counts = Counter(row["extraction_status"] for row in audit_rows)
    bad = [row for row in cache_rows if row["extraction_status"] == "empty-or-unsupported"]
    report = f"""# Fable5 Missing Source Cache Completion

## Scope

- missing unique sha before completion: {len(by_sha)}
- source rows represented in missing groups: {sum(len(rows) for rows in by_sha.values())}
- cache rows after completion: {len(cache_rows)}
- unique sha after completion: {len({row['sha256'] for row in cache_rows})}

## Added Rows By Status

{dict(added_counts)}

## Cache Status After Completion

{dict(status_counts)}

## Source Type Counts After Completion

{dict(source_counts)}

## OCR Repairs

- `5581e0237e861511...` 2026 西城一模 PDF paper: Apple Vision OCR.
- `54715a1e650d940e...` 2026 西城期末细则 PDF: Apple Vision OCR.

## Hard Exclusions

- 2026 石景山期末 remains `skipped-excluded`; it is visible in the cache ledger but is not an input source for the B2/B3/B4_CULTURE handoff.

## Bad Rows

- `empty-or-unsupported`: {len(bad)}
"""
    REPORT.write_text(report, encoding="utf-8")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
