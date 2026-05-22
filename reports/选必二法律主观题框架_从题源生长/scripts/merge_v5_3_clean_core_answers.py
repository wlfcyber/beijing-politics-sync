#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TODAY = datetime.now().strftime("%Y%m%d")
STAMP = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

BATCH_DIR = ROOT / "10_framework_validation/v5_2_answer_rewrite_batches_20260521"
RUNS_IN = ROOT / f"12_final_baodian/question_by_question_framework_runs_v5_2_27strict_core_{TODAY}.csv"
QUESTIONS = ROOT / "04_merge_audit/merged_subjective_law_questions.csv"

FORBIDDEN = [
    "后台",
    "OCR",
    "页眉",
    "可替换",
    "只给",
    "不给分",
    "评分细则",
    "法理依据：",
    "现实意义：",
    "为必踩点",
    "为必出点",
    "原答案",
    "【设问要素】",
    "【阅卷细则】",
    "（，",
    "（）",
    "，。",
    "北京市",
    "学年度",
    "PASS_CANDIDATE",
    "reference_only",
    "formal",
    "slide",
    "page",
]

FIELDS = [
    "question_id",
    "clean_exam_answer",
    "full_score_sentence_bank",
    "must_have_keywords",
    "source_rubric_atom_ids",
    "cautions",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def clean_lines(text: str) -> str:
    lines = []
    for line in text.strip().splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("- "):
            line = line[2:].strip()
        lines.append(line)
    return " | ".join(lines)


def normalize_student_text(text: str) -> str:
    replacements = {
        "不要把答案写成": "不要写成",
        "不要把答案只写成": "不要只写成",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def extract_field(section: str, field: str) -> str:
    labels = "|".join(re.escape(f) for f in FIELDS if f != "question_id")
    pattern = rf"(?ms)^{re.escape(field)}:\s*\n?(.*?)(?=^(?:{labels}):\s*$|^## |\Z)"
    match = re.search(pattern, section)
    if not match:
        return ""
    return normalize_student_text(clean_lines(match.group(1)))


def parse_batch(path: Path) -> list[dict[str, str]]:
    text = path.read_text(encoding="utf-8")
    # Keep the delimiter in each section. Workers used slightly different
    # markdown styles, so the safest delimiter is the field itself.
    starts = [m.start() for m in re.finditer(r"(?m)^(?:##\s*)?question_id:\s*\S+\s*$", text)]
    sections = []
    for i, start in enumerate(starts):
        end = starts[i + 1] if i + 1 < len(starts) else len(text)
        sections.append(text[start:end])
    rows = []
    for section in sections:
        q_match = re.search(r"(?m)^##\s*question_id:\s*(\S+)\s*$", section) or re.search(
            r"(?m)^question_id:\s*(\S+)\s*$", section
        )
        if not q_match:
            continue
        row = {"question_id": q_match.group(1).strip()}
        for field in FIELDS[1:]:
            row[field] = extract_field(section, field)
        rows.append(row)
    return rows


def split_list_field(text: str) -> list[str]:
    return [p.strip() for p in text.split("|") if p.strip()]


def markdown_paragraphs(text: str) -> str:
    parts = split_list_field(text)
    return "\n\n".join(parts) if parts else text.strip()


def markdown_bullets(text: str) -> list[str]:
    return [f"- {p}" for p in split_list_field(text)]


def audit_rows(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    findings = []
    for r in rows:
        for field in ["clean_exam_answer", "full_score_sentence_bank", "must_have_keywords", "cautions"]:
            value = r.get(field, "")
            hits = [p for p in FORBIDDEN if p in value]
            if hits:
                findings.append(
                    {
                        "question_id": r["question_id"],
                        "field": field,
                        "hits": "|".join(hits),
                        "snippet": value[:260],
                    }
                )
    return findings


def main() -> None:
    original_runs = read_csv(RUNS_IN)
    run_by_q = {r["question_id"]: r for r in original_runs}
    question_by_q = {r["question_id"]: r for r in read_csv(QUESTIONS)}

    parsed = []
    for path in sorted(BATCH_DIR.glob("batch_*_rewritten_answers.md")):
        parsed.extend(parse_batch(path))
    rewrite_by_q = {r["question_id"]: r for r in parsed}

    expected = set(run_by_q)
    found = set(rewrite_by_q)
    missing = sorted(expected - found)
    extra = sorted(found - expected)
    if missing or extra:
        raise SystemExit(f"batch qid mismatch missing={missing} extra={extra}")

    rows = []
    sentence_rows = []
    for idx, old in enumerate(original_runs, 1):
        qid = old["question_id"]
        rw = rewrite_by_q[qid]
        q = question_by_q.get(qid, {})
        sentences = split_list_field(rw["full_score_sentence_bank"])
        keywords = split_list_field(rw["must_have_keywords"])
        source_ids = split_list_field(rw["source_rubric_atom_ids"])
        row = {
            **old,
            "clean_exam_answer": rw["clean_exam_answer"],
            "complete_answer_generated": rw["clean_exam_answer"],
            "full_score_sentence_bank": " | ".join(sentences),
            "must_have_keywords": "、".join(keywords) if keywords else old.get("must_have_keywords", ""),
            "clean_rubric_atom_ids": "|".join(source_ids) if source_ids else old.get("clean_rubric_atom_ids", ""),
            "rewrite_cautions": rw["cautions"],
            "status": "v5_3_clean_core_rewritten",
        }
        rows.append(row)
        for s_idx, sent in enumerate(sentences, 1):
            sentence_rows.append(
                {
                    "question_id": qid,
                    "node_names": old.get("framework_entry_nodes", ""),
                    "sentence_id": f"{qid}_CLEAN_S{s_idx:02d}",
                    "sentence": sent,
                    "source_rubric_atom_ids": "|".join(source_ids),
                    "use_condition": q.get("ask_text", old.get("ask_text", "")),
                }
            )

    out_dir = ROOT / "12_final_baodian"
    val_dir = ROOT / "10_framework_validation"
    runs_path = out_dir / f"question_by_question_framework_runs_v5_3_27core_clean_{TODAY}.csv"
    sentence_path = out_dir / f"full_score_sentence_bank_v5_3_27core_clean_{TODAY}.csv"
    md_path = out_dir / f"选必二法律主观题满分宝典_v5_3_27核心清洗稿_{TODAY}.md"
    student_md_path = out_dir / f"选必二法律主观题满分宝典_v5_3_27核心清洗学生版_{TODAY}.md"
    audit_csv = val_dir / f"v5_3_clean_core_answer_audit_{TODAY}.csv"
    audit_md = val_dir / f"v5_3_clean_core_answer_audit_{TODAY}.md"

    fields = list(rows[0].keys())
    write_csv(runs_path, rows, fields)
    write_csv(sentence_path, sentence_rows, ["question_id", "node_names", "sentence_id", "sentence", "source_rubric_atom_ids", "use_condition"])

    parts = [
        "# 选必二法律主观题满分宝典 V5.3 27核心清洗稿",
        "",
        f"生成时间：{STAMP}",
        "",
        "## 当前裁定",
        "",
        "- 这是 V5.2 经 Claude Opus 外审后的清洗稿，不是最终全 65 题宝典。",
        "- strict_core 当前为 27 道；其余题保持 source_check / low_frequency / reference_only / boundary_open 标签。",
        "- 本稿重点修复 Claude 指出的“细则原子直接拼答案”问题，把核心题改写为学生可直接学习的考场答案。",
        "",
        "## 27 道核心题逐题示范",
        "",
    ]
    for idx, row in enumerate(rows, 1):
        qid = row["question_id"]
        q = question_by_q.get(qid, {})
        sentences = split_list_field(row["full_score_sentence_bank"])
        parts.extend(
            [
                f"## 核心题 {idx}：{qid}",
                "",
                f"题源：{q.get('year', row.get('year', ''))} {q.get('district', row.get('district', ''))} {q.get('exam_stage', row.get('exam_stage', ''))} 第{q.get('question_no', row.get('question_no', ''))}题",
                "",
                f"证据等级：{row.get('evidence_level', '')}",
                "",
                f"设问：{q.get('ask_text', row.get('ask_text', ''))}",
                "",
                f"框架入口：{row.get('framework_entry_nodes', '')}",
                "",
                "### 完整考场版答案",
                "",
                markdown_paragraphs(row["clean_exam_answer"]),
                "",
                "### 满分句",
                "",
            ]
        )
        for sent in sentences:
            parts.append(f"- {sent}")
        parts.extend(
            [
                "",
                "### 必踩关键词",
                "",
                row.get("must_have_keywords", ""),
                "",
                "### 证据原子",
                "",
                row.get("clean_rubric_atom_ids", ""),
                "",
                "### 易错刹车",
                "",
            ]
        )
        parts.extend(markdown_bullets(row.get("rewrite_cautions", "")))
        parts.append("")
    md_path.write_text("\n".join(parts), encoding="utf-8")

    student_parts = [
        "# 选必二法律主观题满分宝典 V5.3 学生核心清洗版",
        "",
        f"生成时间：{STAMP}",
        "",
        "## 先会用这四步",
        "",
        "1. 先看设问要你判什么：定责任、判效力、找程序、划边界、推价值。",
        "2. 再把材料里的主体、行为、损害、程序和价值场景圈出来。",
        "3. 每个材料事实都改写成法律语言，不要只抄故事。",
        "4. 答案按“法律规则 + 材料事实 + 责任/效力/程序结论 + 价值收束”写成完整句。",
        "",
        "## 27 道核心题逐题示范",
        "",
    ]
    for idx, row in enumerate(rows, 1):
        q = question_by_q.get(row["question_id"], {})
        sentences = split_list_field(row["full_score_sentence_bank"])
        student_parts.extend(
            [
                f"## 核心题 {idx}",
                "",
                f"题源：{q.get('year', row.get('year', ''))} {q.get('district', row.get('district', ''))} {q.get('exam_stage', row.get('exam_stage', ''))} 第{q.get('question_no', row.get('question_no', ''))}题",
                "",
                f"设问：{q.get('ask_text', row.get('ask_text', ''))}",
                "",
                f"入口：{row.get('framework_entry_nodes', '')}",
                "",
                "### 这题先判断什么",
                "",
                row.get("minimum_judgment_required", "") or f"先判断本题属于“{row.get('framework_entry_nodes', '')}”。",
                "",
                "### 考场满分答案",
                "",
                markdown_paragraphs(row["clean_exam_answer"]),
                "",
                "### 可以拆成这些满分句",
                "",
            ]
        )
        for sent in sentences:
            student_parts.append(f"- {sent}")
        student_parts.extend(
            [
                "",
                "### 必踩关键词",
                "",
                row.get("must_have_keywords", ""),
                "",
                "### 易错刹车",
                "",
            ]
        )
        student_parts.extend(markdown_bullets(row.get("rewrite_cautions", "")))
        student_parts.append("")
    student_md_path.write_text("\n".join(student_parts), encoding="utf-8")

    findings = audit_rows(rows)
    write_csv(audit_csv, findings, ["question_id", "field", "hits", "snippet"])
    report = [
        "# V5.3 27核心清洗稿答案审计",
        "",
        f"生成时间：{STAMP}",
        "",
        f"- 核心题数：{len(rows)}",
        f"- 满分句数：{len(sentence_rows)}",
        f"- 禁用痕迹命中：{len(findings)}",
        "",
    ]
    if findings:
        report.append("## Findings")
        for f in findings:
            report.append(f"- `{f['question_id']}` / `{f['field']}`：{f['hits']} -> {f['snippet']}")
    else:
        report.append("机械扫描未发现后台标签、页眉、OCR 提示、分值/给分说明等禁用痕迹。")
    audit_md.write_text("\n".join(report), encoding="utf-8")

    print(md_path)
    print(student_md_path)
    print(runs_path)
    print(sentence_path)
    print(audit_md)
    print(f"rows={len(rows)} sentences={len(sentence_rows)} findings={len(findings)}")


if __name__ == "__main__":
    main()
