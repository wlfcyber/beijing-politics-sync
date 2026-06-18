#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
TEXT_DIR = RUN_DIR / "02_text_cache" / "texts"
FABLE_DIR = RUN_DIR / "06_fable5_source_cache"

SOURCE_INVENTORY = RUN_DIR / "01_source_inventory" / "source_inventory.csv"
CACHE_MANIFEST = RUN_DIR / "02_text_cache" / "cache_manifest.csv"
QUESTION_CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
FINAL_MATRIX = RUN_DIR / "00_control" / "COVERAGE_MATRIX.csv"


REPAIRS = {
    "f414cf7940ad820265da0a6b31d1a822b0fbe5f21a89bfea71b42be598f32cdc": {
        "text_path": RUN_DIR / "02_text_cache" / "ocr_cache" / "2026_西城_二模_评标" / "西城二模评标.ocr.txt",
        "method": "apple_vision_ocr",
        "note": "CamScanner PDF; OCR produced page-marked rubric text.",
    },
    "dced3f3054457ebcf15b8217e10703e359761f0c131ea57678cfea5dbada1c34": {
        "text_path": RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_通州_一模.txt",
        "method": "apple_vision_ocr_absorbed",
        "note": "Paper PDF already OCR-absorbed during question-gap repair.",
    },
    "fb15943f37f694ac19837e8c5e75fb0272b38eae27ec5529bb037fa163c2a403": {
        "text_path": RUN_DIR / "02_text_cache" / "ocr_absorbed" / "2026_顺义_二模.txt",
        "method": "apple_vision_ocr_absorbed",
        "note": "Paper PDF already OCR-absorbed during question-gap repair.",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({name: row.get(name, "") for name in fieldnames})


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def source_text_path(row: dict[str, str]) -> Path | None:
    for key in ("run_text_path", "source_text_path"):
        value = (row.get(key) or "").strip()
        if not value or value == ".":
            continue
        path = Path(value)
        if path.exists() and path.is_file():
            return path
    return None


def make_repaired_text(row: dict[str, str], repair: dict[str, object]) -> tuple[Path, int, str]:
    src = Path(repair["text_path"])
    raw = src.read_text(encoding="utf-8", errors="replace").strip()
    target = TEXT_DIR / f"{row['sha256'][:16]}.txt"
    text = "\n".join(
        [
            f"source_file: {row['file_path']}",
            f"suite_id: {row['suite_id']}",
            f"source_type: {row['source_type']}",
            f"sha256: {row['sha256']}",
            f"extraction_method: {repair['method']}",
            f"repair_note: {repair['note']}",
            "",
            "===== BEGIN SOURCE-DERIVED TEXT =====",
            raw,
            "===== END SOURCE-DERIVED TEXT =====",
            "",
        ]
    )
    target.write_text(text, encoding="utf-8")
    return target, len(text), str(repair["method"])


def patch_cache_manifest() -> tuple[list[dict[str, str]], list[dict[str, object]]]:
    rows = read_csv(CACHE_MANIFEST)
    repair_audit: list[dict[str, object]] = []
    for row in rows:
        repair = REPAIRS.get(row["sha256"])
        if not repair:
            continue
        out_path, char_count, method = make_repaired_text(row, repair)
        old_status = row.get("extraction_status", "")
        row["cache_hit"] = "no"
        row["extraction_status"] = "raw-extracted"
        row["char_count"] = str(char_count)
        row["run_text_path"] = str(out_path)
        row["source_text_path"] = row["file_path"]
        row["error"] = f"repaired_for_fable5_cache_handoff; method={method}"
        repair_audit.append(
            {
                "suite_id": row["suite_id"],
                "source_type": row["source_type"],
                "file_path": row["file_path"],
                "sha256": row["sha256"],
                "old_status": old_status,
                "new_status": row["extraction_status"],
                "char_count": char_count,
                "run_text_path": str(out_path),
                "method": method,
                "note": repair["note"],
            }
        )
    with CACHE_MANIFEST.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    return rows, repair_audit


def usable_as_rubric(row: dict[str, str]) -> str:
    if row["source_type"] in {"rubric", "marking-report", "lecture-scoring"}:
        return "yes"
    return "no"


def handoff_status(row: dict[str, str]) -> str:
    if row.get("extraction_status") == "skipped-excluded":
        return "excluded_by_hard_rule"
    path = source_text_path(row)
    if row.get("extraction_status") in {"cache-hit", "raw-extracted"} and path:
        return "ai_readable_text_ready"
    return "needs_repair"


def build_handoff_files(cache_rows: list[dict[str, str]], repair_audit: list[dict[str, object]]) -> None:
    FABLE_DIR.mkdir(parents=True, exist_ok=True)
    inventory_rows = read_csv(SOURCE_INVENTORY)
    matrix_rows = read_csv(FINAL_MATRIX)
    question_rows = read_csv(QUESTION_CANDIDATES)

    inv_by_sha: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in inventory_rows:
        inv_by_sha[row["sha256"]].append(row)

    source_packets = []
    manifest_rows: list[dict[str, object]] = []
    for row in cache_rows:
        status = handoff_status(row)
        text_path = source_text_path(row)
        text = ""
        text_hash = ""
        if text_path and status == "ai_readable_text_ready":
            text = text_path.read_text(encoding="utf-8", errors="replace")
            text_hash = sha256_text(text)
        inv_matches = inv_by_sha.get(row["sha256"], [])
        duplicate_paths = [item["file_path"] for item in inv_matches if item["file_path"] != row["file_path"]]
        packet = {
            "suite_id": row["suite_id"],
            "year": row["year"],
            "district": row["district"],
            "stage": row["stage"],
            "source_type": row["source_type"],
            "file_path": row["file_path"],
            "sha256": row["sha256"],
            "handoff_status": status,
            "extraction_status": row["extraction_status"],
            "text_path": str(text_path) if text_path else "",
            "text_char_count": len(text),
            "text_sha256": text_hash,
            "usable_as_rubric": usable_as_rubric(row),
            "reference_answer_warning": "do_not_use_as_rubric" if row["source_type"] == "reference-answer" else "",
            "duplicate_source_paths": duplicate_paths,
            "text": text,
        }
        source_packets.append(packet)
        manifest_rows.append({k: v for k, v in packet.items() if k not in {"text", "duplicate_source_paths"}} | {
            "duplicate_source_count": len(duplicate_paths),
        })

    with (FABLE_DIR / "fable5_ai_readable_source_cache.jsonl").open("w", encoding="utf-8") as f:
        for packet in source_packets:
            f.write(json.dumps(packet, ensure_ascii=False) + "\n")

    write_csv(
        FABLE_DIR / "fable5_source_cache_manifest.csv",
        manifest_rows,
        [
            "suite_id",
            "year",
            "district",
            "stage",
            "source_type",
            "file_path",
            "sha256",
            "handoff_status",
            "extraction_status",
            "text_path",
            "text_char_count",
            "text_sha256",
            "usable_as_rubric",
            "reference_answer_warning",
            "duplicate_source_count",
        ],
    )

    write_csv(
        FABLE_DIR / "cache_repair_audit.csv",
        repair_audit,
        [
            "suite_id",
            "source_type",
            "file_path",
            "sha256",
            "old_status",
            "new_status",
            "char_count",
            "run_text_path",
            "method",
            "note",
        ],
    )

    source_status = Counter(row["handoff_status"] for row in manifest_rows)
    source_types = Counter(row["source_type"] for row in cache_rows)
    matrix_status = Counter(row["status"] for row in matrix_rows)
    target_counts = Counter(row["book_module"] for row in matrix_rows if row["status"] == "included")
    question_types = Counter(row["question_type"] for row in matrix_rows)
    bad_sources = [row for row in manifest_rows if row["handoff_status"] == "needs_repair"]
    subjective_ref = [
        row
        for row in matrix_rows
        if row["status"] == "included"
        and row.get("question_type") == "subjective"
        and "reference-answer" in row.get("source_types", "")
    ]

    evidence_missing = []
    for idx, row in enumerate(matrix_rows, start=2):
        for part in (row.get("evidence_source") or "").split("|"):
            value = part.strip()
            if not value or value.startswith("{"):
                continue
            path = Path(value)
            if not path.is_absolute():
                path = RUN_DIR / value
            if not path.exists():
                evidence_missing.append(
                    {
                        "matrix_line": idx,
                        "suite_id": row["suite_id"],
                        "question": row["question"],
                        "missing_evidence_source": value,
                    }
                )
    write_csv(
        FABLE_DIR / "matrix_evidence_path_audit.csv",
        evidence_missing,
        ["matrix_line", "suite_id", "question", "missing_evidence_source"],
    )

    suite_rows: list[dict[str, object]] = []
    by_suite: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in cache_rows:
        by_suite[row["suite_id"]].append(row)
    matrix_by_suite = Counter(row["suite_id"] for row in matrix_rows)
    for suite_id, rows in sorted(by_suite.items()):
        suite_rows.append(
            {
                "suite_id": suite_id,
                "source_count": len(rows),
                "paper_sources": sum(1 for r in rows if r["source_type"] == "paper"),
                "rubric_sources": sum(1 for r in rows if r["source_type"] == "rubric"),
                "marking_report_sources": sum(1 for r in rows if r["source_type"] == "marking-report"),
                "reference_answer_sources": sum(1 for r in rows if r["source_type"] == "reference-answer"),
                "ready_sources": sum(1 for r in rows if handoff_status(r) == "ai_readable_text_ready"),
                "excluded_sources": sum(1 for r in rows if handoff_status(r) == "excluded_by_hard_rule"),
                "matrix_rows": matrix_by_suite.get(suite_id, 0),
            }
        )
    write_csv(
        FABLE_DIR / "fable5_suite_source_index.csv",
        suite_rows,
        [
            "suite_id",
            "source_count",
            "paper_sources",
            "rubric_sources",
            "marking_report_sources",
            "reference_answer_sources",
            "ready_sources",
            "excluded_sources",
            "matrix_rows",
        ],
    )

    report = [
        "# Fable5 Source Cache Handoff",
        "",
        f"- generated_at: {datetime.now().astimezone().isoformat(timespec='seconds')}",
        f"- run_dir: `{RUN_DIR}`",
        f"- primary_file_for_fable5: `{FABLE_DIR / 'fable5_ai_readable_source_cache.jsonl'}`",
        f"- manifest: `{FABLE_DIR / 'fable5_source_cache_manifest.csv'}`",
        f"- suite_index: `{FABLE_DIR / 'fable5_suite_source_index.csv'}`",
        "",
        "## What This Solves",
        "",
        "- Fable5 can start from one JSONL source cache instead of opening PDFs, DOCX, DOC, or PPTX one by one.",
        "- Each packet keeps the original source path, sha256, suite id, source type, extraction status, and source-derived text.",
        "- Reference answers are explicitly marked `do_not_use_as_rubric`; they may support objective answer-key checks only.",
        "- Rubrics/marking reports are marked separately as usable scoring sources.",
        "",
        "## Source Cache Status",
        "",
        f"- source_inventory_rows: {len(inventory_rows)}",
        f"- source_inventory_unique_sha256: {len(set(row['sha256'] for row in inventory_rows))}",
        f"- canonical_cache_rows: {len(cache_rows)}",
        f"- canonical_cache_unique_sha256: {len(set(row['sha256'] for row in cache_rows))}",
        f"- cache_handoff_status: {dict(source_status)}",
        f"- source_type_counts: {dict(source_types)}",
        f"- repaired_empty_or_unsupported_sources: {len(repair_audit)}",
        f"- needs_repair_after_handoff: {len(bad_sources)}",
        "",
        "## Coverage Matrix Status",
        "",
        f"- final_matrix_rows: {len(matrix_rows)}",
        f"- final_matrix_status_counts: {dict(matrix_status)}",
        f"- target_included_counts: B2_ECONOMICS {target_counts.get('B2_ECONOMICS', 0)}; B3_POLITICS_RULE_OF_LAW {target_counts.get('B3_POLITICS_RULE_OF_LAW', 0)}; B4_CULTURE {target_counts.get('B4_CULTURE', 0)}",
        f"- final_matrix_question_type_counts: {dict(question_types)}",
        f"- question_candidate_rows: {len(question_rows)}",
        f"- subjective_included_rows_using_reference_answer_as_source: {len(subjective_ref)}",
        f"- missing_matrix_evidence_paths: {len(evidence_missing)}",
        "",
        "## Remaining Boundaries",
        "",
        "- `excluded_by_hard_rule` sources are kept visible but are not required input for the B2/B3/B4_CULTURE main handoff.",
        "- Source-derived OCR is an AI-readable transcription layer; exact visual formatting remains in the original files and rendered evidence where needed.",
        "- Do not treat this cache as a student-facing artifact. It is a model handoff/cache artifact.",
        "",
    ]
    if repair_audit:
        report.extend(["## Repair Audit", ""])
        for row in repair_audit:
            report.append(
                f"- `{row['suite_id']}` {row['source_type']}: {row['old_status']} -> {row['new_status']}, chars {row['char_count']}, `{row['run_text_path']}`"
            )
        report.append("")

    (FABLE_DIR / "FABLE5_READ_ME_FIRST.md").write_text("\n".join(report), encoding="utf-8")


def main() -> int:
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    cache_rows, repair_audit = patch_cache_manifest()
    build_handoff_files(cache_rows, repair_audit)
    print(f"repaired={len(repair_audit)}")
    print(f"handoff_dir={FABLE_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
