#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import os
import re
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
WORKSPACE = Path("/Users/wanglifei/Desktop/北京高考政治")

SOURCE_ROOTS = [
    Path("/Users/wanglifei/Desktop/2024模拟题"),
    Path("/Users/wanglifei/Desktop/2025模拟题"),
    Path("/Users/wanglifei/Desktop/2026模拟题"),
    Path("/Users/wanglifei/GaokaoPolitics/2024各区模拟题"),
    Path("/Users/wanglifei/GaokaoPolitics/2025各区模拟题"),
    Path("/Users/wanglifei/GaokaoPolitics/2026各区模拟题"),
]

INCLUDE_SUFFIXES = {
    ".pdf",
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".csv",
    ".txt",
    ".md",
    ".jpg",
    ".jpeg",
    ".png",
}

SKIP_NAMES = {
    ".DS_Store",
    "Thumbs.db",
}

DISTRICTS = [
    "海淀",
    "西城",
    "东城",
    "朝阳",
    "丰台",
    "石景山",
    "顺义",
    "房山",
    "延庆",
    "门头沟",
    "昌平",
    "通州",
    "大兴",
    "怀柔",
    "密云",
    "平谷",
    "燕山",
]

STAGES = [
    ("一模", "一模"),
    ("二模", "二模"),
    ("期末", "期末"),
    ("期中", "期中"),
    ("零模", "零模"),
    ("适应", "适应性测试"),
]


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def clean_text(path: Path) -> str:
    return str(path).replace(" ", "")


def first_match(pattern: str, text: str) -> str:
    m = re.search(pattern, text)
    return m.group(1) if m else ""


def infer_year(path: Path) -> str:
    text = clean_text(path)
    m = re.search(r"(202[456])", text)
    return m.group(1) if m else ""


def infer_district(path: Path) -> str:
    text = clean_text(path)
    for district in DISTRICTS:
        if district in text:
            return district
    return ""


def infer_stage(path: Path) -> str:
    text = clean_text(path)
    for needle, stage in STAGES:
        if needle in text:
            return stage
    return ""


def infer_source_type(path: Path) -> str:
    text = clean_text(path).lower()
    name = path.name.lower()
    cn = clean_text(path)

    if any(k in cn for k in ["评标", "评分细则", "评分标准", "细则"]):
        return "rubric"
    if any(k in cn for k in ["阅卷", "讲评", "试卷分析", "质量分析"]):
        return "marking-report"
    if any(k in cn for k in ["答案", "参考答案", "解析"]):
        return "reference-answer"
    if any(k in cn for k in ["分类", "模块"]):
        return "module-classification"
    if any(k in cn for k in ["试题", "试卷", "模拟题", "政治"]):
        return "paper"
    if name.endswith((".jpg", ".jpeg", ".png")):
        return "image-source"
    return "unknown-source"


def suite_id_for(path: Path) -> str:
    year = infer_year(path) or "unknown_year"
    district = infer_district(path) or "unknown_district"
    stage = infer_stage(path) or "unknown_stage"
    return f"{year}_{district}_{stage}"


def status_for(path: Path, duplicate_of: str) -> str:
    year = infer_year(path)
    district = infer_district(path)
    stage = infer_stage(path)
    if year == "2026" and district == "石景山" and stage == "期末":
        return "module-boundary-excluded"
    if duplicate_of:
        return "duplicate-or-drift"
    return "inventory-only"


def notes_for(path: Path, duplicate_of: str) -> str:
    notes = []
    year = infer_year(path)
    district = infer_district(path)
    stage = infer_stage(path)
    if year == "2026" and district == "石景山" and stage == "期末":
        notes.append("excluded_by_hard_rule_2026_shijingshan_final_no_usable_rubric")
    if duplicate_of:
        notes.append(f"exact_duplicate_of={duplicate_of}")
    if "已放弃" in str(path):
        notes.append("under_abandoned_folder")
    if not infer_district(path) or not infer_stage(path):
        notes.append("metadata_needs_review")
    return "; ".join(notes)


def relative_to_root(path: Path, roots: list[Path]) -> tuple[str, str]:
    for root in roots:
        try:
            return str(root), str(path.relative_to(root))
        except ValueError:
            continue
    return "", str(path)


def main() -> None:
    rows = []
    missing_roots = []
    seen_hash_to_path: dict[str, str] = {}

    for root in SOURCE_ROOTS:
        if not root.exists():
            missing_roots.append(str(root))
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith(".")]
            for filename in filenames:
                if filename in SKIP_NAMES or filename.startswith("~$"):
                    continue
                path = Path(dirpath) / filename
                if path.suffix.lower() not in INCLUDE_SUFFIXES:
                    continue
                try:
                    file_hash = sha256_file(path)
                    stat = path.stat()
                except OSError as exc:
                    file_hash = ""
                    stat = None
                    duplicate_of = ""
                    status = "blocked"
                    notes = f"read_error={exc}"
                else:
                    duplicate_of = seen_hash_to_path.get(file_hash, "")
                    if not duplicate_of:
                        seen_hash_to_path[file_hash] = str(path)
                    status = status_for(path, duplicate_of)
                    notes = notes_for(path, duplicate_of)

                root_path, rel_path = relative_to_root(path, SOURCE_ROOTS)
                row = {
                    "suite_id": suite_id_for(path),
                    "year": infer_year(path),
                    "district": infer_district(path),
                    "stage": infer_stage(path),
                    "file_path": str(path),
                    "root_path": root_path,
                    "relative_path": rel_path,
                    "file_type": path.suffix.lower().lstrip("."),
                    "source_type": infer_source_type(path),
                    "question_range": "",
                    "status": status,
                    "sha256": file_hash,
                    "duplicate_of": duplicate_of,
                    "size_bytes": stat.st_size if stat else "",
                    "modified_at": datetime.fromtimestamp(stat.st_mtime).isoformat(timespec="seconds") if stat else "",
                    "notes": notes,
                }
                rows.append(row)

    rows.sort(key=lambda r: (r["year"], r["district"], r["stage"], r["source_type"], r["file_path"]))

    inventory_path = RUN_DIR / "01_source_inventory" / "source_inventory.csv"
    inventory_fields = [
        "suite_id",
        "year",
        "district",
        "stage",
        "file_path",
        "root_path",
        "relative_path",
        "file_type",
        "source_type",
        "question_range",
        "status",
        "sha256",
        "duplicate_of",
        "size_bytes",
        "modified_at",
        "notes",
    ]
    with inventory_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=inventory_fields)
        writer.writeheader()
        writer.writerows(rows)

    ledger_path = RUN_DIR / "00_control" / "SOURCE_LEDGER.csv"
    ledger_fields = [
        "suite_id",
        "year",
        "district",
        "stage",
        "file_path",
        "file_type",
        "source_type",
        "question_range",
        "status",
        "notes",
    ]
    with ledger_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ledger_fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in ledger_fields})

    counts_by_status = Counter(row["status"] for row in rows)
    counts_by_year = Counter(row["year"] or "unknown" for row in rows)
    counts_by_type = Counter(row["source_type"] for row in rows)
    suites = defaultdict(int)
    for row in rows:
        suites[row["suite_id"]] += 1

    summary_path = RUN_DIR / "01_source_inventory" / "source_inventory_summary.md"
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# Source Inventory Summary\n\n")
        f.write(f"- generated_at: {datetime.now().isoformat(timespec='seconds')}\n")
        f.write(f"- source_roots_checked: {len(SOURCE_ROOTS)}\n")
        f.write(f"- missing_roots: {len(missing_roots)}\n")
        f.write(f"- files_indexed: {len(rows)}\n")
        f.write(f"- unique_sha256: {len({row['sha256'] for row in rows if row['sha256']})}\n")
        f.write(f"- suite_ids_detected: {len(suites)}\n\n")

        f.write("## Missing Roots\n\n")
        if missing_roots:
            for item in missing_roots:
                f.write(f"- {item}\n")
        else:
            f.write("- none\n")

        f.write("\n## Status Counts\n\n")
        for key, value in sorted(counts_by_status.items()):
            f.write(f"- {key}: {value}\n")

        f.write("\n## Year Counts\n\n")
        for key, value in sorted(counts_by_year.items()):
            f.write(f"- {key}: {value}\n")

        f.write("\n## Source Type Counts\n\n")
        for key, value in sorted(counts_by_type.items()):
            f.write(f"- {key}: {value}\n")

        f.write("\n## Suite Counts\n\n")
        for key, value in sorted(suites.items()):
            f.write(f"- {key}: {value}\n")

    print(f"wrote {inventory_path}")
    print(f"wrote {ledger_path}")
    print(f"wrote {summary_path}")
    print(f"files_indexed={len(rows)} suites={len(suites)}")


if __name__ == "__main__":
    main()
