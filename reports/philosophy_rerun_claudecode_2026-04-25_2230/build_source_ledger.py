"""Build SOURCE_LEDGER.csv from preprocessed_corpus manifest.csv.

Walks the manifest, classifies each source by suite/year/district/stage and
source_type (paper / rubric / answer-key / report / lecture / archive /
classification-archive / reference-answer), then emits the artifact-contract
columns.
"""
from __future__ import annotations

import csv
import os
import re
import sys

CACHE_DIR = (
    r"C:\Users\Administrator\Desktop\beijing_politics_research"
    r"\data\preprocessed_corpus"
)
MANIFEST = os.path.join(CACHE_DIR, "manifest.csv")
OUT = (
    r"C:\Users\Administrator\Desktop\飞哥的政治庄园\reports"
    r"\philosophy_rerun_claudecode_2026-04-25_2230\SOURCE_LEDGER.csv"
)


def detect_year(suite_key: str, rel: str) -> str:
    for y in ("2024", "2025", "2026"):
        if y in suite_key or y in rel:
            return y
    return ""


def detect_district(name: str) -> str:
    districts = [
        "海淀", "西城", "东城", "朝阳", "丰台", "石景山", "房山", "通州",
        "顺义", "门头沟", "延庆", "昌平", "大兴", "怀柔", "平谷", "密云",
    ]
    for d in districts:
        if d in name:
            return d
    return ""


def detect_stage(name: str) -> str:
    if "二模" in name:
        return "二模"
    if "一模" in name:
        return "一模"
    if "期末" in name:
        return "期末"
    if "期中" in name:
        return "期中"
    if "三模" in name:
        return "三模"
    return ""


def detect_source_type(rel: str, name: str) -> str:
    n = name.lower()
    rl = rel.lower()
    if "试题分类" in name or "分类汇编" in name:
        return "classification-archive"
    if any(k in name for k in ("评分细则", "细则", "评标")):
        return "rubric"
    if any(k in name for k in ("阅卷报告", "阅卷总结", "讲评", "评卷报告")):
        return "marking-report"
    if (
        any(k in name for k in ("阅卷", "评卷"))
        and "报告" not in name
        and "总结" not in name
    ):
        return "marking-report"
    if "讲评" in name or "讲评.pdf" in n or "讲评.pptx" in n:
        return "lecture-scoring"
    if any(k in name for k in ("答案", "参考")):
        return "objective-answer-key" if "选" in name or "答案" in name else "reference-answer"
    if any(k in name for k in ("试题", "试卷", "教师版")):
        return "paper"
    if "pptx" in rl and "细则" in rl:
        return "rubric"
    return "paper"


def detect_status(method: str, status: str, source_type: str) -> str:
    if status == "rendered-ocr-needed":
        return "ocr-needed"
    if status == "text-extracted":
        return "inventory-only"
    return status or "inventory-only"


def short_question_range(name: str, source_type: str) -> str:
    m = re.findall(r"(\d{1,2})\s*题", name)
    if m:
        return ",".join(sorted(set(m), key=int))
    return ""


def main() -> int:
    with open(MANIFEST, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    out_rows = []
    for r in rows:
        rel = r["relative_path"]
        name = os.path.basename(rel)
        suite_key = r.get("suite_key", "")
        year = detect_year(suite_key, rel)
        district = detect_district(suite_key) or detect_district(rel)
        stage = detect_stage(suite_key) or detect_stage(rel)
        source_type = detect_source_type(rel, name)
        status = detect_status(r.get("method", ""), r.get("status", ""), source_type)
        qrange = short_question_range(name, source_type)
        suite_id = suite_key.split("__")[-1] if suite_key else ""

        out_rows.append({
            "suite_id": suite_id,
            "year": year,
            "district": district,
            "stage": stage,
            "file_path": r["source_path"],
            "file_type": r["suffix"].lstrip("."),
            "source_type": source_type,
            "question_range": qrange,
            "status": status,
            "notes": (
                f"cache_text={os.path.basename(r['text_path']) if r['text_path'] else ''};"
                f"cache_render={os.path.basename(r['render_dir']) if r['render_dir'] else ''};"
                f"gpt_md={os.path.basename(r['gpt_markdown_path']) if r['gpt_markdown_path'] else ''}"
            ),
        })

    with open(OUT, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "suite_id", "year", "district", "stage", "file_path",
                "file_type", "source_type", "question_range", "status",
                "notes",
            ],
        )
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"wrote {len(out_rows)} rows to {OUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
