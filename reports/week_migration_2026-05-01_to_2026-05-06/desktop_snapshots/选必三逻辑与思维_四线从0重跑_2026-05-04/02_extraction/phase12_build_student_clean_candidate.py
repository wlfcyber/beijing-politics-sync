#!/usr/bin/env python3
"""Build Phase12 student-clean Markdown/index candidates.

This is a mechanical cleanup pass after post-external Governor/Confucius gates.
It does not create Word/PDF/final. It strips review-only scaffolding from the
student-visible files and saves traceability separately.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")

SRC_BODY = ROOT / "09_student_draft/phase12_expanded_body_TEACHING_PATCHED_REVIEW_ONLY.md"
SRC_REASONING = ROOT / "09_student_draft/phase12_reasoning_typology_index_TEACHING_PATCHED_REVIEW_ONLY.md"
SRC_THINKING = ROOT / "09_student_draft/phase12_thinking_method_index_TEACHING_PATCHED_REVIEW_ONLY.md"

OUT_BODY = ROOT / "09_student_draft/phase12_student_clean_candidate.md"
OUT_REASONING = ROOT / "09_student_draft/phase12_reasoning_typology_index_STUDENT_CLEAN_CANDIDATE.md"
OUT_THINKING = ROOT / "09_student_draft/phase12_thinking_method_index_STUDENT_CLEAN_CANDIDATE.md"
OUT_COPY = ROOT / "outputs/2026北京高考政治选必三逻辑与思维宝典---思维与推理全触发全链条_学生版_CLEAN_CANDIDATE.md"

TRACE = ROOT / "08_review/phase12_student_clean_traceability_matrix.csv"
AUDIT_MD = ROOT / "08_review/phase12_student_clean_build_audit.md"
AUDIT_CSV = ROOT / "08_review/phase12_student_clean_build_audit.csv"
GPT_PROMPT = ROOT / "08_review/gpt_phase_advice/phase_12_student_clean_candidate_prompt_for_gpt55_USER_SUBMIT.md"

FORBIDDEN_PATTERNS = [
    "REVIEW_ONLY",
    "TEACHING_PATCHED",
    "NO_WORD",
    "NO_PDF",
    "NO_FINAL",
    "question_id",
    "phase12_decision",
    "source_pool",
    "phase11B",
    "body_after_362",
    "manual_lock",
    "phase06",
    "external_forced",
    "SCIENCE_ONLY",
    "no_manual",
    "no_phase06",
    "kept out",
    "fallback",
    "source_locked",
    "评分来源",
    "答案源",
    "评标",
    "参考答案",
    "OCR",
    "debug",
]


def extract_traceability(body: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    current_title = ""
    for lineno, line in enumerate(body.splitlines(), start=1):
        if line.startswith("### "):
            current_title = line[4:].strip()
        if "<!-- question_id:" in line:
            qid = re.search(r"question_id:\s*([^;]+)", line)
            decision = re.search(r"phase12_decision:\s*([^;]+)", line)
            source = re.search(r"source_pool:\s*([^ ]+)", line)
            rows.append(
                {
                    "clean_order": str(len(rows) + 1),
                    "visible_title": current_title,
                    "question_id": qid.group(1).strip() if qid else "",
                    "phase12_decision": decision.group(1).strip() if decision else "",
                    "source_pool": source.group(1).strip() if source else "",
                    "review_line": str(lineno),
                }
            )
    return rows


def clean_body(body: str) -> str:
    start = body.find("## 主观题")
    if start == -1:
        raise RuntimeError("Cannot find 主观题 section in body.")
    content = body[start:]
    content = re.sub(r"(?m)^<!-- question_id:.*?-->\n?", "", content)
    content = re.sub(r"\n{3,}", "\n\n", content)
    header = """# 2026北京高考政治选必三《逻辑与思维》宝典：思维与推理全触发全链条

使用顺序：先看主观题，掌握材料信号、可写方法、答题动作和易错陷阱；再看选择题，训练完整选项、正确项理由和错项陷阱。正文顺序为主观题在前、选择题在后；每类内部按海淀、西城、东城、朝阳、丰台、其他区，同一区按 2026、2025、2024 排列。

"""
    return header + content.strip() + "\n"


def clean_basis(raw: str, kind: str) -> str:
    text = raw.strip()
    replacements = [
        ("phase06_logical_form_locked:", "归类提示："),
        ("manual_lock:", "归类提示："),
        ("external_forced_check", ""),
        ("no_phase06_locked_reasoning_row", "仅作辅助检索，不作典型推理正例"),
        (
            "no_manual_positive_mount_after_MUST_FIX_CONTENT; kept out of positive nodes",
            "仅作辅助检索，不作正向方法例题",
        ),
        ("SCIENCE_ONLY_SOURCE_SUPPORTED", "原题只问科学思维，按科学思维专项处理"),
        ("scientific_thinking_primary", "科学思维为主线"),
        ("only_boundary_trap_not_超前思维_positive", "只作边界提醒，不作超前思维正例"),
        (
            "choice_trap_material_fact_not_subjective_method_positive",
            "只作易混选择题，不作主观题方法正例",
        ),
        ("not_middle_term", "不是中项不周延"),
        ("choice_signal", "选择题信号"),
        ("source_locked_D", ""),
        ("答案源支持", "本题材料支持"),
        ("（modus tollens）", ""),
    ]
    for old, new in replacements:
        text = text.replace(old, new)
    text = text.replace("_", "；").replace(";", "；")
    text = re.sub(r"\s+", " ", text).strip(" ；")
    if not text:
        text = "仅作辅助检索。" if kind == "reasoning" else "仅作辅助理解。"
    if not text.startswith(("归类提示：", "仅作", "原题")):
        text = "归类提示：" + text
    return text


def clean_index(src: Path, title: str, kind: str) -> str:
    lines = src.read_text(encoding="utf-8").splitlines()
    out = [
        f"# {title}",
        "",
        "索引用来帮助学生按方法或题型回找正文题目。带有“易混选择题”“边界提醒”“相关检索”的条目，不要当作主观题正例硬套。",
        "",
    ]
    for line in lines:
        if line.startswith("# ") or line.startswith("Status:"):
            continue
        if line.startswith("重建原因") or line.startswith("本索引不由"):
            continue
        if line.startswith("## "):
            out.append(line)
            out.append("")
            continue
        if line.startswith("- "):
            match = re.match(r"- (\[[^\]]+\]) `\d+` (.*?) \(`Q-[^)]+`\) - (.*)", line)
            if match:
                tag, visible, basis = match.groups()
                tag = (
                    tag.replace("正文正例", "可正用例")
                    .replace("辅助挂载", "相关检索")
                    .replace("选择题陷阱", "易混选择题")
                    .replace("边界陷阱", "边界提醒")
                )
                out.append(f"- {tag} {visible}：{clean_basis(basis, kind)}")
                continue
        if line.strip():
            out.append(line)
    return "\n".join(out).strip() + "\n"


def count_choice_entries(body: str) -> int:
    marker = "\n## 选择题"
    if marker not in body:
        return 0
    section = body.split(marker, 1)[1]
    return len(re.findall(r"(?m)^### ", section))


def count_subjective_entries(body: str) -> int:
    marker = "\n## 选择题"
    if marker not in body:
        return len(re.findall(r"(?m)^### ", body))
    section = body.split(marker, 1)[0]
    return len(re.findall(r"(?m)^### ", section))


def forbidden_hits(paths: list[Path]) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern in text:
                rows.append({"file": str(path.relative_to(ROOT)), "pattern": pattern})
    return rows


def write_gpt_prompt() -> None:
    GPT_PROMPT.write_text(
        """# 给 GPT-5.5 Pro 的选必三学生清洁候选稿复审请求

请只审内容质量、学生可学性、题型/思维归类准确性和是否仍有审计话术残留，不要要求生成 Word。

本轮候选稿路径：

- 学生清洁候选正文：`09_student_draft/phase12_student_clean_candidate.md`
- 推理题型索引：`09_student_draft/phase12_reasoning_typology_index_STUDENT_CLEAN_CANDIDATE.md`
- 思维方法索引：`09_student_draft/phase12_thinking_method_index_STUDENT_CLEAN_CANDIDATE.md`
- 追溯矩阵：`08_review/phase12_student_clean_traceability_matrix.csv`
- 清洁构建审计：`08_review/phase12_student_clean_build_audit.md`

请重点检查：

1. 77 条是否仍显得穷尽、具体、像哲学宝典那样逐题可学。
2. 50 道选择题是否都有完整选项、正确项理由、错项陷阱。
3. 27 道主观题是否都有材料信号、可写方法/规则、为什么触发、答案落点、易错陷阱和同类题。
4. 推理索引是否仍有充分条件/必要条件、三段论大小项、边界陷阱误挂。
5. 思维索引是否仍把边界陷阱当正例。
6. 学生正文中是否还残留 review-only、source、phase、manual_lock、qid 等内部审计语言。

请给 verdict：

- CLEAN_PASS_TO_WORD_PREP
- PATCH_REQUIRED_NO_WORD

如果需要返修，请按 question title 精确列出 must_fix / should_fix。
""",
        encoding="utf-8",
    )


def main() -> None:
    body_raw = SRC_BODY.read_text(encoding="utf-8")
    trace_rows = extract_traceability(body_raw)
    body_clean = clean_body(body_raw)
    reasoning_clean = clean_index(SRC_REASONING, "推理题型索引", "reasoning")
    thinking_clean = clean_index(SRC_THINKING, "思维方法索引", "thinking")

    OUT_BODY.write_text(body_clean, encoding="utf-8")
    OUT_REASONING.write_text(reasoning_clean, encoding="utf-8")
    OUT_THINKING.write_text(thinking_clean, encoding="utf-8")
    OUT_COPY.write_text(body_clean, encoding="utf-8")

    with TRACE.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["clean_order", "visible_title", "question_id", "phase12_decision", "source_pool", "review_line"],
        )
        writer.writeheader()
        writer.writerows(trace_rows)

    write_gpt_prompt()

    outputs = [OUT_BODY, OUT_REASONING, OUT_THINKING]
    hits = forbidden_hits(outputs)
    audit_rows = [
        {"check_id": "body_entries", "status": "PASS" if len(re.findall(r'(?m)^### ', body_clean)) == 77 else "FAIL", "detail": str(len(re.findall(r'(?m)^### ', body_clean)))},
        {"check_id": "subjective_entries", "status": "PASS" if count_subjective_entries(body_clean) == 27 else "FAIL", "detail": str(count_subjective_entries(body_clean))},
        {"check_id": "choice_entries", "status": "PASS" if count_choice_entries(body_clean) == 50 else "FAIL", "detail": str(count_choice_entries(body_clean))},
        {"check_id": "complete_option_blocks", "status": "PASS" if body_clean.count("【完整选项】") == 50 else "FAIL", "detail": str(body_clean.count("【完整选项】"))},
        {"check_id": "choice_correct_blocks", "status": "PASS" if body_clean.count("【正确项】") >= 50 else "FAIL", "detail": str(body_clean.count("【正确项】"))},
        {"check_id": "choice_trap_blocks", "status": "PASS" if body_clean.count("【错项陷阱】") >= 50 else "FAIL", "detail": str(body_clean.count("【错项陷阱】"))},
        {"check_id": "traceability_rows", "status": "PASS" if len(trace_rows) == 77 else "FAIL", "detail": str(len(trace_rows))},
        {"check_id": "internal_marker_hits", "status": "PASS" if not hits else "FAIL", "detail": str(len(hits))},
    ]

    with AUDIT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["check_id", "status", "detail"])
        writer.writeheader()
        writer.writerows(audit_rows)
        for hit in hits:
            writer.writerow({"check_id": "internal_marker_hit", "status": "FAIL", "detail": f"{hit['file']}::{hit['pattern']}"})

    status = "STUDENT_CLEAN_CANDIDATE_BUILT_PENDING_GPT_AND_FINAL_GATES" if not hits else "STUDENT_CLEAN_CANDIDATE_BUILT_WITH_BLOCKERS"
    AUDIT_MD.write_text(
        f"""# Phase12 Student Clean Candidate Build Audit

Status: `{status}`

This build strips review-only scaffolding into separate traceability while preserving the 77-entry teaching body. It does not create Word, PDF, final PASS, TASK_COMPLETE, 终稿, 最终稿, or 宝典成品.

## Outputs

- Student clean candidate: `09_student_draft/phase12_student_clean_candidate.md`
- Output copy: `outputs/2026北京高考政治选必三逻辑与思维宝典---思维与推理全触发全链条_学生版_CLEAN_CANDIDATE.md`
- Reasoning index candidate: `09_student_draft/phase12_reasoning_typology_index_STUDENT_CLEAN_CANDIDATE.md`
- Thinking index candidate: `09_student_draft/phase12_thinking_method_index_STUDENT_CLEAN_CANDIDATE.md`
- Traceability matrix: `08_review/phase12_student_clean_traceability_matrix.csv`
- GPT user-submit prompt: `08_review/gpt_phase_advice/phase_12_student_clean_candidate_prompt_for_gpt55_USER_SUBMIT.md`

## Counts

- body entries: {len(re.findall(r'(?m)^### ', body_clean))}
- subjective entries: {count_subjective_entries(body_clean)}
- choice entries: {count_choice_entries(body_clean)}
- complete option blocks: {body_clean.count('【完整选项】')}
- choice correct blocks: {body_clean.count('【正确项】')}
- choice trap blocks: {body_clean.count('【错项陷阱】')}
- traceability rows: {len(trace_rows)}
- internal marker hits: {len(hits)}

## Gate

Next step is GPT-5.5 Pro clean-candidate review or user-submitted GPT review, then final Governor/Confucius gates. Word/PDF/final remain blocked.
""",
        encoding="utf-8",
    )
    print(status)
    print(f"body_entries={len(re.findall(r'(?m)^### ', body_clean))}")
    print(f"internal_marker_hits={len(hits)}")


if __name__ == "__main__":
    main()
