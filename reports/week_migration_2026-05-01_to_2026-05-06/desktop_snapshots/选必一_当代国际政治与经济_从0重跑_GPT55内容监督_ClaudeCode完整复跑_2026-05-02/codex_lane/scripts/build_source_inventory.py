#!/usr/bin/env python3
import argparse
import csv
import hashlib
import os
import re
from pathlib import Path


SKIP_DIR_NAMES = {
    ".DS_Store",
    "__MACOSX",
    ".git",
    "node_modules",
    ".venv",
}

TEXT_LIKE = {".txt", ".md", ".csv", ".json", ".jsonl", ".xml", ".html", ".htm"}
DOC_LIKE = {".doc", ".docx", ".ppt", ".pptx", ".pdf", ".wps", ".pages", ".key"}
IMAGE_LIKE = {".png", ".jpg", ".jpeg", ".webp", ".tif", ".tiff", ".bmp", ".heic"}
ARCHIVE_LIKE = {".zip", ".rar", ".7z"}


def stable_id(path: Path) -> str:
    return "SRC_" + hashlib.sha1(str(path).encode("utf-8")).hexdigest()[:12]


def guess_year(path_text: str) -> str:
    m = re.search(r"20(24|25|26)", path_text)
    return m.group(0) if m else ""


def guess_district(path_text: str) -> str:
    districts = [
        "海淀",
        "西城",
        "东城",
        "朝阳",
        "丰台",
        "石景山",
        "通州",
        "顺义",
        "延庆",
        "门头沟",
        "房山",
        "昌平",
        "大兴",
        "怀柔",
        "密云",
        "平谷",
        "燕山",
        "北京",
    ]
    for district in districts:
        if district in path_text:
            return district
    return ""


def guess_stage(path_text: str) -> str:
    # Avoid broad parent folders such as "2026各区期末和期中" overriding the
    # actual suite folder "2026通州期末" or "2026朝阳期中".
    for part in reversed(re.split(r"[\\/]+", path_text)):
        if re.search(r"\.(pdf|docx?|pptx?|xlsx?|rtf|txt|wps)$", part, re.IGNORECASE):
            continue
        if "期末" in part and "期中" in part:
            continue
        if "期中" in part:
            return "期中"
        if "期末" in part:
            return "期末"
        if "一模" in part or "综合练习（一）" in part or "综合练习(一)" in part:
            return "一模"
        if "二模" in part or "综合练习（二）" in part or "综合练习(二)" in part:
            return "二模"
        if "三模" in part:
            return "三模"
        if "适应" in part:
            return "适应性"
    stage_terms = [
        ("期中", "期中"),
        ("期末", "期末"),
        ("一模", "一模"),
        ("二模", "二模"),
        ("三模", "三模"),
        ("适应", "适应性"),
        ("综合练习（一）", "一模"),
        ("综合练习(一)", "一模"),
        ("综合练习（二）", "二模"),
        ("综合练习(二)", "二模"),
    ]
    for needle, label in stage_terms:
        if needle in path_text:
            return label
    return ""


def guess_evidence(path_text: str) -> str:
    lowered = path_text.lower()
    if re.search(r"细则|评标|阅卷|评分细则|阅卷总结|评分标准|给分|标分", path_text):
        return "P0_candidate_scoring"
    if re.search(r"答案及评分参考|答案与评分|答案和评分|答案|参考答案", path_text):
        return "P1_candidate_reference_answer"
    if re.search(r"讲评|讲义|课件|ppt|分析|评析", path_text) or lowered.endswith((".ppt", ".pptx")):
        return "P2_candidate_teaching_or_lecture"
    if re.search(r"试卷|原卷|政治|综合练习|高三", path_text):
        return "P3_candidate_paper"
    return "unknown"


def guess_file_flags(suffix: str, path_text: str) -> str:
    flags = []
    if suffix in IMAGE_LIKE:
        flags.append("image")
    if suffix in {".pdf"}:
        flags.append("pdf")
    if suffix in {".doc", ".docx", ".wps"}:
        flags.append("word")
    if suffix in {".ppt", ".pptx", ".key"}:
        flags.append("ppt")
    if suffix in ARCHIVE_LIKE:
        flags.append("archive")
    if re.search(r"图|表|漫画|图片|扫描|照片", path_text):
        flags.append("possible_visual_or_table")
    if suffix in TEXT_LIKE:
        flags.append("text_like")
    if not flags:
        flags.append("other")
    return ";".join(flags)


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES]
        for name in filenames:
            if name == ".DS_Store":
                continue
            yield Path(dirpath) / name


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    parser.add_argument("--root", action="append", required=True)
    args = parser.parse_args()

    rows = []
    for root_arg in args.root:
        root = Path(root_arg).expanduser().resolve()
        root_label = root.name
        if not root.exists():
            rows.append(
                {
                    "source_id": stable_id(root),
                    "root_label": root_label,
                    "root_path": str(root),
                    "relative_path": "",
                    "filename": root.name,
                    "suffix": "",
                    "size_bytes": "",
                    "mtime": "",
                    "year_hint": "",
                    "district_hint": "",
                    "stage_hint": "",
                    "evidence_guess": "missing_root",
                    "file_flags": "missing_root",
                    "status": "blocked_source",
                    "notes": "root does not exist",
                }
            )
            continue
        for path in iter_files(root):
            try:
                stat = path.stat()
            except OSError as exc:
                rows.append(
                    {
                        "source_id": stable_id(path),
                        "root_label": root_label,
                        "root_path": str(root),
                        "relative_path": str(path.relative_to(root)),
                        "filename": path.name,
                        "suffix": path.suffix.lower(),
                        "size_bytes": "",
                        "mtime": "",
                        "year_hint": "",
                        "district_hint": "",
                        "stage_hint": "",
                        "evidence_guess": "unknown",
                        "file_flags": "stat_failed",
                        "status": "blocked_source",
                        "notes": str(exc),
                    }
                )
                continue
            text = str(path)
            suffix = path.suffix.lower()
            rows.append(
                {
                    "source_id": stable_id(path),
                    "root_label": root_label,
                    "root_path": str(root),
                    "relative_path": str(path.relative_to(root)),
                    "filename": path.name,
                    "suffix": suffix,
                    "size_bytes": stat.st_size,
                    "mtime": int(stat.st_mtime),
                    "year_hint": guess_year(text),
                    "district_hint": guess_district(text),
                    "stage_hint": guess_stage(text),
                    "evidence_guess": guess_evidence(text),
                    "file_flags": guess_file_flags(suffix, text),
                    "status": "not_started",
                    "notes": "",
                }
            )

    fieldnames = [
        "source_id",
        "root_label",
        "root_path",
        "relative_path",
        "filename",
        "suffix",
        "size_bytes",
        "mtime",
        "year_hint",
        "district_hint",
        "stage_hint",
        "evidence_guess",
        "file_flags",
        "status",
        "notes",
    ]
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    summary_path = out.with_suffix(".summary.md")
    counts = {}
    for row in rows:
        key = row["evidence_guess"]
        counts[key] = counts.get(key, 0) + 1
    with summary_path.open("w", encoding="utf-8") as f:
        f.write("# Source Inventory Summary\n\n")
        f.write(f"- total_files: {len(rows)}\n")
        for key in sorted(counts):
            f.write(f"- {key}: {counts[key]}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
