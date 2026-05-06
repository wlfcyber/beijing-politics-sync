#!/usr/bin/env python3
import csv
import hashlib
import os
from pathlib import Path

RUN_DIR = Path(__file__).resolve().parents[2]
ROOTS = [
    Path("/Users/wanglifei/Desktop/2024模拟题"),
    Path("/Users/wanglifei/Desktop/2025模拟题"),
    Path("/Users/wanglifei/Desktop/2026模拟题"),
]
NOTEBOOK = Path("/Users/wanglifei/Desktop/北京高考政治/选必一复查_2026-04-29/选必一_交付要求记事本.md")
EXTS = {".docx", ".doc", ".pdf", ".pptx", ".ppt", ".png", ".jpg", ".jpeg"}


def stable_id(path: Path) -> str:
    digest = hashlib.sha1(str(path).encode("utf-8")).hexdigest()[:12]
    return f"SRC_{digest}"


def year_from_path(path: Path) -> str:
    text = str(path)
    for year in ("2024", "2025", "2026"):
        if year in text:
            return year
    return ""


def suite_from_path(path: Path, root: Path) -> str:
    rel = path.relative_to(root)
    parts = rel.parts
    if not parts:
        return root.name
    if root.name == "2025模拟题" and parts[0].startswith("2025各区") and len(parts) > 1:
        return parts[1]
    if root.name == "2026模拟题" and parts[0] in {"2026各区一模", "2026各区期末和期中", "已放弃"} and len(parts) > 1:
        return parts[1]
    return parts[0]


def evidence_type(path: Path) -> str:
    text = str(path)
    name = path.name
    if "/细则/" in text or "细则" in name or "评标" in name or "阅卷" in name or "答案" in name:
        return "rubric_or_marking"
    if "/试卷/" in text or "试题" in name or "试卷" in name or "原卷" in name:
        return "paper"
    if "讲评" in name or "总结" in name:
        return "lecture_or_review"
    if "分类汇编" in name:
        return "classified_compilation"
    return "other"


def extraction_method(path: Path) -> str:
    ext = path.suffix.lower()
    if ext in {".docx", ".doc"}:
        return "pending_word_or_textutil"
    if ext == ".pdf":
        return "pending_pdf_text_or_render"
    if ext in {".pptx", ".ppt"}:
        return "pending_ppt_render_or_zip"
    if ext in {".png", ".jpg", ".jpeg"}:
        return "pending_image_ocr_or_visual"
    return "pending"


def confidence_for(path: Path) -> str:
    if evidence_type(path) == "rubric_or_marking":
        return "high"
    if evidence_type(path) == "paper":
        return "high"
    if evidence_type(path) == "classified_compilation":
        return "medium"
    return "medium"


def main() -> None:
    rows = []
    rows.extend(
        [
            {
                "source_id": "SRC_ROOT_2024",
                "path": str(ROOTS[0]),
                "year": "2024",
                "suite": "root",
                "file_type": "directory",
                "evidence_type": "source_root",
                "status": "source_checked",
                "extraction_method": "filesystem",
                "confidence": "high",
                "notes": "Raw source root for 2024 mock papers.",
            },
            {
                "source_id": "SRC_ROOT_2025",
                "path": str(ROOTS[1]),
                "year": "2025",
                "suite": "root",
                "file_type": "directory",
                "evidence_type": "source_root",
                "status": "source_checked",
                "extraction_method": "filesystem",
                "confidence": "high",
                "notes": "Raw source root for 2025 mock papers.",
            },
            {
                "source_id": "SRC_ROOT_2026",
                "path": str(ROOTS[2]),
                "year": "2026",
                "suite": "root",
                "file_type": "directory",
                "evidence_type": "source_root",
                "status": "source_checked",
                "extraction_method": "filesystem",
                "confidence": "high",
                "notes": "Raw source root for 2026 mock papers.",
            },
            {
                "source_id": "NOTEBOOK_XBY1",
                "path": str(NOTEBOOK),
                "year": "2026",
                "suite": "run_notebook",
                "file_type": "markdown",
                "evidence_type": "user_hard_rules",
                "status": "source_checked",
                "extraction_method": "text_read",
                "confidence": "high",
                "notes": "Hard user rules and corrections; not a scoring evidence source.",
            },
        ]
    )

    for root in ROOTS:
        for dirpath, _, filenames in os.walk(root):
            for filename in filenames:
                path = Path(dirpath) / filename
                if path.name.startswith("~$"):
                    continue
                if path.suffix.lower() not in EXTS:
                    continue
                rows.append(
                    {
                        "source_id": stable_id(path),
                        "path": str(path),
                        "year": year_from_path(path),
                        "suite": suite_from_path(path, root),
                        "file_type": path.suffix.lower().lstrip("."),
                        "evidence_type": evidence_type(path),
                        "status": "not_started",
                        "extraction_method": extraction_method(path),
                        "confidence": confidence_for(path),
                        "notes": "",
                    }
                )

    fieldnames = [
        "source_id",
        "path",
        "year",
        "suite",
        "file_type",
        "evidence_type",
        "status",
        "extraction_method",
        "confidence",
        "notes",
    ]
    ledger_path = RUN_DIR / "SOURCE_LEDGER.csv"
    with ledger_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    inventory_path = RUN_DIR / "codex_lane" / "source_inventory.csv"
    with inventory_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    suites = {}
    for row in rows:
        if row["suite"] in {"root", "run_notebook"}:
            continue
        suites.setdefault(row["suite"], {"rubric": 0, "paper": 0, "other": 0})
        if row["evidence_type"] == "rubric_or_marking":
            suites[row["suite"]]["rubric"] += 1
        elif row["evidence_type"] == "paper":
            suites[row["suite"]]["paper"] += 1
        else:
            suites[row["suite"]]["other"] += 1

    summary_path = RUN_DIR / "codex_lane" / "source_inventory_summary.md"
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# Source Inventory Summary\n\n")
        f.write(f"- source files: {len(rows) - 4}\n")
        f.write(f"- suites/directories: {len(suites)}\n\n")
        f.write("| suite | rubric_or_marking | paper | other |\n")
        f.write("|---|---:|---:|---:|\n")
        for suite in sorted(suites):
            counts = suites[suite]
            f.write(f"| {suite} | {counts['rubric']} | {counts['paper']} | {counts['other']} |\n")

    print(f"wrote {ledger_path}")
    print(f"wrote {inventory_path}")
    print(f"wrote {summary_path}")
    print(f"source files: {len(rows) - 4}")
    print(f"suites/directories: {len(suites)}")


if __name__ == "__main__":
    main()
