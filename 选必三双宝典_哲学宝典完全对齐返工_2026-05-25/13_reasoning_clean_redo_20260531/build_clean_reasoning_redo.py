#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


RUN = Path(__file__).resolve().parent
PREV = RUN.parent / "12_reasoning_exercise_compilation_20260531"
LEDGER = PREV / "REASONING_EXERCISE_COMPILATION_LEDGER.csv"

CLEAN_MD = RUN / "选必三_逻辑与思维_推理习题汇编_干净重做版_20260531.md"
AUDIT_CSV = RUN / "audit" / "REASONING_CLEAN_REDO_AUDIT.csv"
QA_REPORT = RUN / "qa" / "REASONING_CLEAN_REDO_QA_20260531.md"


FORBIDDEN_BODY_TOKENS = [
    "/Users/",
    "source_extracted",
    "ocr_vision",
    "direct_question_number",
    "rubric_file_name_matched",
    "paper_path",
    "rubric_path",
    "placement_id",
    "source_text_cache",
    "REASONING_EXERCISE",
    "debug",
    "OCR",
]


MANUAL_PAPER_OVERRIDES = {
    "P0026": """7．下列三段论的逻辑分析错误的是（ ）
A．凡共青团员都是青年，并非所有的青年工人都是共青团员，所以并非所有的青年工人都是青年。
不正确，一个形式结构正确的三段论前提中不周延的项在结论中不得周延，该三段论犯了“小项不当扩大”的逻辑错误。
B．调查报告不是文学作品，这篇文稿不是调查报告，所以这篇文稿不是文学作品。
不正确，一个形式结构正确的三段论，两个否定的前提不能必然推出结论，结论为否定当且仅当前提中有一否定。
C．物质是不灭的，这支钢笔是物质，所以这支钢笔是不灭的。
不正确，一个形式结构正确的三段论只能有三个不同的项，该三段论犯了“四概念”的逻辑错误。
    D．有些农民是劳动模范，有些农民是党员，所以有些党员是劳动模范。
不正确，一个形式结构正确的三段论中项在前提中至少周延一次，该三段论犯了“中项不周延”的逻辑错误。
A．A
B．B
C．C
D．D""",
}


MANUAL_RUBRIC_OVERRIDES = {
    # 2026海淀二模选择题答案在教师版 DOCX 的“参考答案/第一部分”中；
    # 讲评 PDF 会把第5、7题误导到后面的主观题讲评页。
    "P0016": "参考答案\n第一部分\n本部分共 15 题，每题 3 分，共 45 分。\n1.D 2.C 3.C 4.A 5.D\n6.A 7.A 8.B 9.C 10.A\n11.D 12.D 13.B 14.B 15.A",
    "P0019": "参考答案\n第一部分\n本部分共 15 题，每题 3 分，共 45 分。\n1.D 2.C 3.C 4.A 5.D\n6.A 7.A 8.B 9.C 10.A\n11.D 12.D 13.B 14.B 15.A",
    "P0044": "参考答案\n第一部分\n本部分共 15 题，每题 3 分，共 45 分。\n1.D 2.C 3.C 4.A 5.D\n6.A 7.A 8.B 9.C 10.A\n11.D 12.D 13.B 14.B 15.A",
    # 2024东城一模答案 PDF 为扫描件，OCR 表格顺序不稳定；此处按原 PDF 首页答案表回填。
    "P0031": "北京市东城区 2023-2024 学年度第二学期高三综合练习（一）思想政治参考答案及评分标准\n第一部分 选择题\n本部分共15题，每题3分，共45分。\n1.C 2.B 3.A 4.A 5.D 6.D 7.A 8.D\n9.B 10.C 11.A 12.B 13.D 14.C 15.C",
    "P0068": "北京市东城区 2023-2024 学年度第二学期高三综合练习（一）思想政治参考答案及评分标准\n第一部分 选择题\n本部分共15题，每题3分，共45分。\n1.C 2.B 3.A 4.A 5.D 6.D 7.A 8.D\n9.B 10.C 11.A 12.B 13.D 14.C 15.C",
    # 石景山一模以“细则/细则.doc”官方答案为准，试卷 PDF 内部答案区会被误读。
    "P0035": "石景山区2026年高三统一练习思想政治试卷答案及评分参考\n第一部分共15题，每题3分，共45分。\n1.B 2.D 3.A 4.C 5.D\n6.D 7.C 8.D 9.A 10.D\n11.B 12.C 13.C 14.C 15.B",
}

MANUAL_RUBRIC_SOURCE_PATHS = {
    "P0016": "/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026海淀二模/试卷/2026北京海淀高三二模政治（教师版）.docx",
    "P0019": "/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026海淀二模/试卷/2026北京海淀高三二模政治（教师版）.docx",
    "P0044": "/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026海淀二模/试卷/2026北京海淀高三二模政治（教师版）.docx",
    "P0035": "/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026石景山一模/细则/细则.doc",
}


def read_rows() -> list[dict[str, str]]:
    with LEDGER.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def clean_text(text: str) -> str:
    text = text or ""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = re.sub(r"```+", "", text)
    cleaned: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            if cleaned and cleaned[-1] != "":
                cleaned.append("")
            continue
        if re.match(r"^-{3,}\s*(page|ppt/slides)", line, re.I):
            continue
        if re.match(r"^={3,}.*page\s+\d+.*={3,}$", line, re.I):
            continue
        if re.match(r"^高三思想政治.*第\s*\d+\s*页", line):
            continue
        if re.match(r"^高三思想政治.*第\s*\d+\s*$", line):
            continue
        if re.match(r"^第\s*\d+\s*页\s*/?\s*共\s*\d+\s*页$", line):
            continue
        if re.match(r"^页\s*[\(（]\s*共\s*\d+\s*页\s*[\)）]$", line):
            continue
        line = re.sub(r"\s+", " ", line)
        line = line.replace("􀆰", ".")
        line = line.replace("ꎬ", "，").replace("ꎮ", "。").replace("ꎻ", "；")
        line = re.sub(
            r"([A-D])\s*[\.．、]\s*([①②③④0-9]+)\s*([A-D])\s*([①②③④0-9]+)$",
            r"\1. \2\n\3. \4",
            line,
        )
        cleaned.append(line)
    while cleaned and cleaned[-1] == "":
        cleaned.pop()
    return "\n".join(cleaned).strip()


def option_count(text: str) -> int:
    pats = [
        r"(?m)^\s*[A-DＡ-Ｄ]\s*[\.．、]",
        r"(?m)^\s*[A-DＡ-Ｄ]\s*$",
    ]
    seen = set()
    for pat in pats:
        for m in re.finditer(pat, text):
            ch = re.search(r"[A-DＡ-Ｄ]", m.group(0))
            if ch:
                seen.add(ch.group(0).translate(str.maketrans("ＡＢＣＤ", "ABCD")))
    inline = re.findall(r"(?<![A-Za-z])[A-D]\s*[\.．、]", text)
    for item in inline:
        seen.add(item[0])
    return len(seen)


def answer_visible(row: dict[str, str], rubric: str) -> bool:
    ans = correct_answer(row, rubric)
    if row.get("question_type") != "选择题":
        return bool(rubric)
    return bool(ans and ans in rubric)


def correct_answer(row: dict[str, str], rubric: str) -> str:
    ans = row.get("old_correct_answer", "").strip()
    if ans:
        return ans
    qbase = re.match(r"\d+", row.get("question_no", "") or "")
    if not qbase:
        return ""
    q = qbase.group(0)
    lines = [line.strip() for line in rubric.splitlines() if line.strip()]
    for i, line in enumerate(lines):
        if "题号" not in line or "|" not in line:
            continue
        heads = [c.strip() for c in line.split("|")]
        if heads and heads[0] == "题号":
            heads = heads[1:]
        for j in range(i + 1, min(i + 4, len(lines))):
            if "答案" not in lines[j] or "|" not in lines[j]:
                continue
            vals = [c.strip() for c in lines[j].split("|")]
            if vals and vals[0] == "答案":
                vals = vals[1:]
            if q in heads:
                idx = heads.index(q)
                if idx < len(vals) and re.fullmatch(r"[A-D]", vals[idx]):
                    return vals[idx]
    m = re.search(rf"(?<!\d){re.escape(q)}\s*[\.．、]?\s*([A-D])(?![A-Za-z])", rubric)
    if m:
        return m.group(1)
    return ""


def focus_choice_rubric(row: dict[str, str], rubric: str) -> str:
    ans = correct_answer(row, rubric)
    qbase = re.match(r"\d+", row.get("question_no", "") or "")
    q = qbase.group(0) if qbase else ""
    lines = [line.strip() for line in rubric.splitlines() if line.strip()]
    if "题号 |" in rubric and "答案 |" in rubric:
        for i, line in enumerate(lines):
            if "题号" not in line or "|" not in line:
                continue
            heads = [c.strip() for c in line.split("|")]
            for j in range(i + 1, min(i + 4, len(lines))):
                if "答案" in lines[j] and "|" in lines[j] and (not q or q in heads):
                    return "\n".join(lines[i : min(j + 1, len(lines))])
    if q and ans:
        # Teacher-version PDFs sometimes OCR the answer table as vertical pairs.
        m = re.search(r"(参考答案|第一部分\s*选择题|题号)(?P<body>.*?)(第二部分|16[\.．、（(]|$)", rubric, re.S)
        if m:
            body = clean_text((m.group(1) or "") + (m.group("body") or ""))
            if ans in body:
                return body[:1200]
        return f"题号 | {q}\n答案 | {ans}"
    return rubric[:1200]


def focus_main_rubric(row: dict[str, str], rubric: str) -> str:
    qno = row.get("question_no", "")
    qbase_m = re.match(r"(\d+)", qno)
    part_m = re.search(r"\((\d+)\)", qno)
    s = rubric
    if qbase_m and part_m:
        qbase = qbase_m.group(1)
        part = part_m.group(1)
        start_pat = rf"{re.escape(qbase)}\s*[\n ]*[\(（]\s*{re.escape(part)}\s*[\)）]"
        m = re.search(start_pat, s)
        if m:
            s = s[m.start() :]
            next_part = str(int(part) + 1)
            next_pat = rf"\n\s*{re.escape(qbase)}\s*[\n ]*[\(（]\s*{re.escape(next_part)}\s*[\)）]"
            nm = re.search(next_pat, s)
            if nm:
                s = s[: nm.start()]
    for marker in ["\n1.\n立意", "\n立意:", "\n精准把握问题设计"]:
        idx = s.find(marker)
        if idx != -1 and idx > 300:
            s = s[:idx]
    return s.strip()


def focus_rubric(row: dict[str, str], rubric: str) -> str:
    if row.get("question_type") == "选择题":
        return focus_choice_rubric(row, rubric)
    return focus_main_rubric(row, rubric)


def clean_title(title: str) -> str:
    return re.sub(r"^\d+\.\s*", "", title).strip()


def build_markdown(rows: list[dict[str, str]]) -> str:
    out: list[str] = []
    out.append("# 选必三《逻辑与思维》推理习题汇编（干净重做版）")
    out.append("")
    out.append("本版只保留题本正文：按推理框架收录原题、完整选项、答案或细则要点。来源核验信息另入审计表，不进入正文。")
    out.append("")
    current_family = None
    current_node = None
    counters: defaultdict[tuple[str, str], int] = defaultdict(int)
    for row in rows:
        family = row["family"].strip()
        node = row["node"].strip()
        if family != current_family:
            out.append(f"# {family}")
            out.append("")
            current_family = family
            current_node = None
        if node != current_node:
            out.append(f"## {node}")
            out.append("")
            current_node = node
        counters[(family, node)] += 1
        title = clean_title(row["title"])
        out.append(f"### {counters[(family, node)]}. {title}")
        out.append("")
        out.append(f"【题型位置】{family} / {node}")
        out.append("")
        paper = clean_text(MANUAL_PAPER_OVERRIDES.get(row["placement_id"], row["paper_excerpt"]))
        rubric = focus_rubric(row, clean_text(MANUAL_RUBRIC_OVERRIDES.get(row["placement_id"], row["rubric_excerpt"])))
        out.append("【原题】")
        out.append("")
        out.append("```text")
        out.append(paper)
        out.append("```")
        out.append("")
        out.append("【答案/细则】")
        out.append("")
        ans = correct_answer(row, rubric)
        if row["question_type"] == "选择题" and ans:
            out.append(f"答案：{ans}")
            out.append("")
        out.append("```text")
        out.append(rubric)
        out.append("```")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def write_audit(rows: list[dict[str, str]], body: str) -> None:
    AUDIT_CSV.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "placement_id",
        "family",
        "node",
        "title",
        "suite",
        "question_no",
        "question_type",
        "paper_path",
        "paper_status",
        "rubric_path",
        "rubric_status",
        "review_status",
        "choice_option_count",
        "choice_answer_visible",
        "correct_answer",
        "manual_body_override",
        "manual_rubric_override",
        "paper_text_present",
        "rubric_text_present",
    ]
    with AUDIT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for row in rows:
            paper = clean_text(MANUAL_PAPER_OVERRIDES.get(row["placement_id"], row["paper_excerpt"]))
            rubric = focus_rubric(row, clean_text(MANUAL_RUBRIC_OVERRIDES.get(row["placement_id"], row["rubric_excerpt"])))
            w.writerow(
                {
                    "placement_id": row["placement_id"],
                    "family": row["family"],
                    "node": row["node"],
                    "title": row["title"],
                    "suite": row["suite"],
                    "question_no": row["question_no"],
                    "question_type": row["question_type"],
                    "paper_path": row["paper_path"],
                    "paper_status": row["paper_status"],
                    "rubric_path": MANUAL_RUBRIC_SOURCE_PATHS.get(row["placement_id"], row["rubric_path"]),
                    "rubric_status": "manual_verified_original_answer_table"
                    if row["placement_id"] in MANUAL_RUBRIC_SOURCE_PATHS
                    else row["rubric_status"],
                    "review_status": row["review_status"],
                    "choice_option_count": option_count(paper) if row["question_type"] == "选择题" else "",
                    "choice_answer_visible": answer_visible(row, rubric) if row["question_type"] == "选择题" else "",
                    "correct_answer": correct_answer(row, rubric) if row["question_type"] == "选择题" else "",
                    "manual_body_override": row["placement_id"] in MANUAL_PAPER_OVERRIDES,
                    "manual_rubric_override": row["placement_id"] in MANUAL_RUBRIC_OVERRIDES,
                    "paper_text_present": bool(paper),
                    "rubric_text_present": bool(rubric),
                }
            )


def qa(rows: list[dict[str, str]], body: str) -> str:
    choice_rows = [r for r in rows if r["question_type"] == "选择题"]
    main_rows = [r for r in rows if r["question_type"] == "主观题"]
    option_issues = []
    answer_issues = []
    for r in choice_rows:
        paper = clean_text(MANUAL_PAPER_OVERRIDES.get(r["placement_id"], r["paper_excerpt"]))
        rubric = focus_rubric(r, clean_text(MANUAL_RUBRIC_OVERRIDES.get(r["placement_id"], r["rubric_excerpt"])))
        if option_count(paper) < 4:
            option_issues.append(r["placement_id"])
        if not answer_visible(r, rubric):
            answer_issues.append(r["placement_id"])
    body_hits = {tok: body.count(tok) for tok in FORBIDDEN_BODY_TOKENS if tok in body}
    lines = [
        "# 推理习题汇编干净重做版 QA",
        "",
        f"- placements: {len(rows)}",
        f"- unique_questions: {len({(r['suite'], r['question_no']) for r in rows})}",
        f"- main_placements: {len(main_rows)}",
        f"- choice_placements: {len(choice_rows)}",
        f"- families: {len(set(r['family'] for r in rows))}",
        f"- review_status_source_extracted: {sum(1 for r in rows if r['review_status'] == 'source_extracted')}",
        f"- choice_option_visible_issues: {len(option_issues)}",
        f"- choice_answer_visible_issues: {len(answer_issues)}",
        f"- forbidden_body_token_hits: {sum(body_hits.values())}",
        "",
        "## 推理族分布",
        "",
    ]
    for family, count in Counter(r["family"] for r in rows).items():
        lines.append(f"- {family}: {count}")
    lines.extend(["", "## 问题清单", ""])
    if option_issues:
        lines.append("- 选项不足 4 个的放置点：" + ", ".join(option_issues))
    if answer_issues:
        lines.append("- 答案未显性出现的选择题：" + ", ".join(answer_issues))
    if body_hits:
        lines.append("- 正文污染词命中：" + "; ".join(f"{k}={v}" for k, v in body_hits.items()))
    if not option_issues and not answer_issues and not body_hits:
        lines.append("- 无硬问题。")
    return "\n".join(lines) + "\n"


def main() -> None:
    rows = read_rows()
    body = build_markdown(rows)
    CLEAN_MD.write_text(body, encoding="utf-8")
    write_audit(rows, body)
    QA_REPORT.parent.mkdir(parents=True, exist_ok=True)
    QA_REPORT.write_text(qa(rows, body), encoding="utf-8")


if __name__ == "__main__":
    main()
