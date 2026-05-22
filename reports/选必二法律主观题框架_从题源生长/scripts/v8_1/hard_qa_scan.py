#!/usr/bin/env python3
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "v8_1_student_delivery_fix"
PACKET = ROOT / "v8_student_usable_rebuild" / "09_packet_for_user_gpt_review_20260521"

FILES = [
    "01_student_exam_framework_v8.md",
    "02_full_baodian_v8.md",
    "06_gold_standard_question_runs.md",
    "07_full_score_sentence_bank_v8.md",
    "08_question_by_question_runs_v8.md",
    "08_question_by_question_runs_v8.csv",
    "09_teacher_evidence_framework_v8.md",
]

PATTERNS = [
    ("参考答案", r"参考答案"),
    ("评分细则", r"评分细则"),
    ("阅卷前制定", r"阅卷前制定"),
    ("原答案", r"原答案"),
    ("[page", r"\[page"),
    ("[slide", r"\[slide"),
    ("第.*页", r"第.{0,20}页"),
    ("得分关键词含分值", r"得分关键词：.*分"),
    ("满分句评分细则", r"满分句：评分细则"),
    ("R_", r"R_"),
    ("M_", r"M_"),
    ("设问原子缺失", r"设问原子缺失"),
    ("待回源", r"待回源"),
    ("法律语言背景或价值铺垫", r"法律语言: 背景或价值铺垫|法律语言：背景或价值铺垫"),
    ("见细则关键词", r"见细则关键词"),
    ("gold_sample_all_material_atoms", r"gold_sample_all_material_atoms"),
    ("gold_sample_all_rubric_atoms", r"gold_sample_all_rubric_atoms"),
    ("CC0229_bad_逃逸粒子", r"逃逸粒子"),
    ("CC0229_bad_创新资源集聚", r"创新资源集聚"),
    ("CC0229_bad_空间布局精准", r"空间布局精准"),
    ("CC0229_bad_全链条产业生态", r"全链条产业生态"),
]

TEACHER_ALLOWED = {"09_teacher_evidence_framework_v8.md"}
TEACHER_ALLOWED_PATTERNS = {"R_", "M_"}


def zone_for(file_name: str) -> str:
    if file_name in TEACHER_ALLOWED:
        return "teacher_evidence"
    if file_name.endswith(".csv"):
        return "student_or_backend_table"
    return "student_body"


def severity(file_name: str, label: str) -> str:
    if file_name in TEACHER_ALLOWED and label in TEACHER_ALLOWED_PATTERNS:
        return "allowed_teacher_evidence"
    if file_name in TEACHER_ALLOWED and label in {"gold_sample_all_material_atoms", "gold_sample_all_rubric_atoms"}:
        return "P0"
    if label.startswith("CC0229_bad"):
        return "P0"
    if zone_for(file_name) == "student_body":
        return "P0"
    return "P1"


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    rows = []
    for file_name in FILES:
        path = PACKET / file_name
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            for label, pattern in PATTERNS:
                if re.search(pattern, line):
                    sev = severity(file_name, label)
                    rows.append({
                        "file_name": file_name,
                        "line_no": line_no,
                        "zone": zone_for(file_name),
                        "pattern_label": label,
                        "severity": sev,
                        "action": "rewrite_or_move_to_teacher_evidence" if sev == "P0" else ("allowed_in_teacher_evidence" if sev == "allowed_teacher_evidence" else "review"),
                        "line_excerpt": line[:500],
                    })

    csv_path = OUT / "00_hard_QA_scan.csv"
    with csv_path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=[
            "file_name", "line_no", "zone", "pattern_label", "severity", "action", "line_excerpt"
        ])
        writer.writeheader()
        writer.writerows(rows)

    counts = {}
    for r in rows:
        counts[r["severity"]] = counts.get(r["severity"], 0) + 1

    md = []
    md.append("# v8.1 STEP 00 硬 QA 扫描")
    md.append("")
    md.append("结论：当前 v8 不能直接交付。扫描命中大量学生正文禁用词，必须进入 v8.1 修复。")
    md.append("")
    md.append("## 一、扫描范围")
    for f in FILES:
        md.append(f"- `{f}`")
    md.append("")
    md.append("## 二、命中统计")
    md.append("")
    md.append("| severity | count |")
    md.append("|---|---:|")
    for k in ["P0", "P1", "allowed_teacher_evidence"]:
        md.append(f"| {k} | {counts.get(k, 0)} |")
    md.append("")
    md.append("## 三、判定")
    md.append("")
    if counts.get("P0", 0):
        md.append("- QA 状态：FAIL。")
        md.append("- 原因：学生正文/逐题运行正文仍包含评分说明、证据编号、页码、设问缺失、细则摘抄或禁止词风险。")
        md.append("- 执行门槛：必须先修复金样板同步、设问缺失、优先 10 题、句库和教师证据框架，才能生成 v8.1 宝典。")
    else:
        md.append("- QA 状态：PASS。")
    md.append("")
    md.append("## 四、P0 前 80 条样例")
    md.append("")
    md.append("| file | line | pattern | action | excerpt |")
    md.append("|---|---:|---|---|---|")
    p0s = [r for r in rows if r["severity"] == "P0"][:80]
    for r in p0s:
        ex = r["line_excerpt"].replace("|", "｜")
        md.append(f"| `{r['file_name']}` | {r['line_no']} | {r['pattern_label']} | {r['action']} | {ex} |")
    (OUT / "00_hard_QA_scan.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    print(f"rows={len(rows)} p0={counts.get('P0',0)} p1={counts.get('P1',0)} allowed={counts.get('allowed_teacher_evidence',0)}")


if __name__ == "__main__":
    main()
