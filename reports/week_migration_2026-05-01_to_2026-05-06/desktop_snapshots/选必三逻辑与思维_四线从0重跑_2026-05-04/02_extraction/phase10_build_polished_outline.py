#!/usr/bin/env python3
"""Build Phase10 polish/outline from the locked 29-row Phase09 draft only."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
IN_MD = ROOT / "09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md"
IN_MATRIX = ROOT / "09_student_draft/phase09_student_draft_control_matrix.csv"
OUT_DIR = ROOT / "09_student_draft"
REVIEW_DIR = ROOT / "08_review"

OUT_MD = OUT_DIR / "phase10_polished_outline_FROM_29.md"
OUT_MATRIX = OUT_DIR / "phase10_polish_control_matrix.csv"
BACKCHECK_CSV = OUT_DIR / "phase10_question_id_traceability_backcheck.csv"
STYLE_DECISION_MD = OUT_DIR / "phase10_same_type_index_style_decision.md"
CROSS_ANCHOR_MD = OUT_DIR / "phase10_cross_answer_anchor_patch.md"
TERMS_SCAN_MD = OUT_DIR / "phase10_internal_terms_scan.md"
RISK_REGISTER_MD = OUT_DIR / "phase10_QID_risk_register.md"
VERIFICATION_MD = REVIEW_DIR / "phase10_codexA_polish_verification.md"

QID_RE = re.compile(r"Q-(\d{4})([\u4e00-\u9fff]+)(一模|二模|期末|期中)-(\d+)(?:-(\d+))?")

FORBIDDEN_STUDENT_TERMS = [
    "Phase09",
    "Phase10",
    "packet",
    "source locator",
    "lane",
    "Lane",
    "Governor",
    "Confucius",
    "L3",
    "L4",
    "B-choice-signal",
    "LOCKED_FOR_FUSION",
    "文件路径",
    "细则编号",
    "/Users/",
    "source_entry_status",
    "question_id",
]

HARD_EXCLUDED = {
    "Q-2024西城一模-11",
    "Q-2025海淀二模-12",
    "Q-2025海淀二模-13",
    "Q-2026顺义一模-3",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def qid_to_visible(qid: str) -> str:
    m = QID_RE.fullmatch(qid)
    if not m:
        return qid
    year, district, stage, qno, sub = m.groups()
    title = f"{year} {district}{stage}第{qno}题"
    if sub:
        title += f"第({sub})问"
    return title


def readable_same_type(text: str) -> str:
    return QID_RE.sub(lambda m: qid_to_visible(m.group(0)), text)


def normalize_choice_answer(qid: str, line: str) -> str:
    replacements = {
        "Q-2024朝阳一模-7": {
            "- 答案落点：正确选项 C（②③），重点写清创新思维不排斥逻辑分析、合作创新建立在对前人成果继承之上。":
            "- 答案落点：选 C，②③。重点写清创新思维不排斥逻辑分析，合作创新建立在对前人成果继承之上。",
        },
        "Q-2024朝阳一模-9": {
            "- 答案落点：正确选项 D（③④），点出活动是多主体协同完成、整体性贯穿调查与提案全过程，并指向制度优势的运用。":
            "- 答案落点：选 D，③④。点出活动是多主体协同完成，整体性贯穿调查与提案全过程，并指向制度优势的运用。",
        },
        "Q-2025丰台期末-8": {
            "- 答题动作：选 D。②运用发散思维表达人们对和平的向往与追求；④以形象思维触及和平的本质特征。":
            "- 答题动作：选 D，②④。②运用发散思维表达人们对和平的向往与追求；④以形象思维触及和平的本质特征。",
            "- 答案落点：在“形象思维、发散思维”这一类型上得分；指出诗歌从多个意象发散表达，并以具体形象触及和平本质。":
            "- 答案落点：选 D，②④。诗歌从多个意象发散表达，并以具体形象触及和平本质。",
        },
        "Q-2025丰台期末-7": {
            "- 答案落点：选 C，理由是从实际出发、从当下做起，生活才能少些迷茫。":
            "- 答案落点：选 C。理由是从实际出发、从当下做起，生活才能少些迷茫。",
        },
        "Q-2024朝阳期中-7": {
            "- 答案落点：选 B，排序为②①③；结论由两个前提关于“北京中轴线”的中项贯通推出。":
            "- 答案落点：选 B，②①③。结论由两个前提关于“北京中轴线”的中项贯通推出。",
            "- 有效式或错误式：正确排序为②大前提“北京中轴线是不可替代的文化遗产”+①小前提“北京中轴线是世界遗产委员会确认的世界遗产”+③结论“有些由世界遗产委员会确认的是不可替代的文化遗产”；中项“北京中轴线”周延，推理有效，正确选项 B。":
            "- 有效式或错误式：排序为②大前提“北京中轴线是不可替代的文化遗产”+①小前提“北京中轴线是世界遗产委员会确认的世界遗产”+③结论“有些由世界遗产委员会确认的是不可替代的文化遗产”；中项“北京中轴线”周延，推理有效。",
        },
        "Q-2025东城期末-13": {
            "- 答案落点：正确选项 B，理由是①与③均犯中项不周延的谬误。":
            "- 答案落点：选 B，①③。理由是①与③均犯中项不周延的谬误。",
        },
        "Q-2025顺义一模-7": {
            "- 答案落点：选 A，原因是 A 对谬误名称判断错了；真实错误应是大项不当扩大，不是小项不当扩大。":
            "- 答案落点：选 A。原因是 A 对谬误名称判断错了；真实错误应是大项不当扩大，不是小项不当扩大。",
        },
        "Q-2024朝阳期中-9": {
            "- 有效式或错误式：小李实验中铃声随空气量同向变化，符合共变法，正确选项 B。":
            "- 有效式或错误式：小李实验中铃声随空气量同向变化，符合共变法。",
            "- 答案落点：选 B，判断为归纳推理中的共变法。":
            "- 答案落点：选 B。判断为归纳推理中的共变法。",
        },
    }
    return replacements.get(qid, {}).get(line, line)


def normalize_student_tone(line: str) -> str:
    replacements = {
        "- 为什么能想到：本题要求从三个角度分别采分，科学思维对应客观性与预见性、创新思维对应“三新”与发散聚合、超前，辩证思维对应整体性与分析综合；每一角度都要落到时间利用调查的具体动作上才不丢分。":
        "- 为什么能想到：本题要求从三个角度分别展开，科学思维对应客观性与预见性，创新思维对应“三新”与发散聚合、超前，辩证思维对应整体性与分析综合；每一角度都要落到时间利用调查的具体动作上。",
        "- 答题动作：三角度多挂载、按表格化采分；科学思维 2 分(客观性、预见性)，创新思维 3 分(三新、发散聚合、超前)，辩证思维 2 分(整体性、分析综合)；每个分点必须结合材料分析。":
        "- 答题动作：按三个角度拆开：科学思维看客观性、预见性；创新思维看“三新”、发散聚合、超前；辩证思维看整体性、分析综合；每个角度都必须结合材料分析。",
        "- 易错陷阱：只列知识点而不结合材料，只能拿基础 1 分；混淆角度归属(把“整体性”写到科学思维下、把“客观性”写到创新思维下)直接丢分。":
        "- 易错陷阱：只列知识点而不结合材料，只能停留在浅层作答；混淆角度归属(把“整体性”写到科学思维下、把“客观性”写到创新思维下)会丢分。",
        "- 答题动作：调查了解 = 感性具体(1 分)；分析研究 = 思维抽象 + 思维具体(1 分)；两阶段相互依赖、不可割裂(2 分)。":
        "- 答题动作：调查了解对应感性具体；分析研究对应思维抽象和思维具体；两阶段相互依赖、不可割裂。",
        "- 易错陷阱：把感性具体和思维具体的方向颠倒不给分；用“实践决定认识”替代具体环节只能得 1 分。":
        "- 易错陷阱：把感性具体和思维具体的方向颠倒不给分；用“实践决定认识”替代具体环节只能作补充，不能代替三环节本身。",
        "- 有效式或错误式：六点框架按“调研→因果→矛盾→推理想象→超前”顺序展开；附加补点“强调实践 + 1 分，超前思维，内外矛盾”。":
        "- 有效式或错误式：整体框架按“调研→因果→矛盾→推理想象→超前”顺序展开；可补充强调实践基础、超前思维和内外矛盾。",
        "- 为什么能想到：题干明确“运用系统观念与创新思维”，材料从原始突破写到链式扩展，正好对应系统观念的整体性与创新思维的从单点到链式；两类思维并行采分。":
        "- 为什么能想到：题干明确“运用系统观念与创新思维”，材料从原始突破写到链式扩展，正好对应系统观念的整体性与创新思维的从单点到链式；两类思维需要并行展开。",
        "- 易错陷阱：补完整推理时漏写“古代/当时”等时间表述会扣 1 分。":
        "- 易错陷阱：补完整推理时漏写“古代/当时”等时间表述会影响结论限定。",
    }
    return replacements.get(line, line)


def current_qid_from_heading(line: str, title_to_qid: dict[str, str], current: str) -> str:
    if not line.startswith("### "):
        return current
    title = line[4:].strip()
    return title_to_qid.get(title, current)


def add_q2026_shunyi_anchor(qid: str, line: str, section_lines: list[str]) -> list[str]:
    section_lines.append(line)
    if qid == "Q-2026顺义一模-19-2" and line.startswith("- 答题动作："):
        anchor = "- 答案落点：科学思维具有客观性、预见性和可检验性；本题产品研发立足老人真实需求、研判老龄化趋势，并通过反复测试迭代接受检验。"
        if anchor not in section_lines:
            section_lines.append(anchor)
    return section_lines


def polish_markdown(text: str, title_to_qid: dict[str, str]) -> str:
    lines = text.splitlines()
    output: list[str] = [
        "# 选必三《逻辑与思维》题型触发与答题框架",
        "",
        "## 使用方式",
        "",
        "- 先看材料动作，再判断它是在考“思维方法”还是“推理规则”。",
        "- 思维题按“材料信号 → 可写思维/方法 → 为什么能想到 → 答题动作 → 答案落点 → 易错陷阱 → 同类题”走。",
        "- 推理题按“题型 → 逻辑形式 → 规则口诀 → 有效式或错误式 → 解题动作 → 答案落点 → 易错陷阱 → 同类题”走。",
        "- 同类题只作为索引，用来提醒你回看相近题型，不在这里展开答案。",
        "",
        "---",
        "",
    ]
    current_qid = ""
    skip_intro = True
    for raw in lines:
        line = raw.rstrip()
        if skip_intro:
            if line == "## 一、思维方法":
                skip_intro = False
            else:
                continue
        if line == "## 一、思维方法":
            output.extend(["## 一、思维方法：从材料动作锁定方法", ""])
            continue
        if line == "## 二、边界陷阱":
            output.extend(["## 二、边界陷阱：别把别的模块硬塞进来", ""])
            continue
        if line == "## 三、推理题型":
            output.extend(["## 三、推理题型：先定形式再判有效", ""])
            continue
        if line == "## 四、交叉题":
            output.extend(["## 四、交叉题：主讲线优先，辅助线防误判", ""])
            continue
        if line.startswith("交叉题要保留两条线"):
            output.append("交叉题要先看卷面主讲线；辅助线只帮助防误判，不能抢走主问题。")
            continue
        current_qid = current_qid_from_heading(line, title_to_qid, current_qid)
        line = normalize_choice_answer(current_qid, line)
        line = normalize_student_tone(line)
        if line.startswith("- 同类题索引："):
            line = readable_same_type(line)
        output = add_q2026_shunyi_anchor(current_qid, line, output)
    while len(output) > 1 and output[-1] == "" and output[-2] == "":
        output.pop()
    return "\n".join(output).strip() + "\n"


def line_numbers_for(text_lines: list[str], needle: str) -> list[int]:
    return [i for i, line in enumerate(text_lines, start=1) if needle in line]


def main() -> None:
    matrix = read_csv(IN_MATRIX)
    title_to_qid = {r["visible_title"]: r["question_id"] for r in matrix}
    phase09_text = IN_MD.read_text(encoding="utf-8")
    student_text = polish_markdown(phase09_text, title_to_qid)
    OUT_MD.write_text(student_text, encoding="utf-8")

    control_rows: list[dict[str, str]] = []
    for r in matrix:
        same_type_ids = r["same_type_ids"]
        control_rows.append(
            {
                **r,
                "phase10_title_strategy": "student_readable_heading_body_control_matrix_qid_trace",
                "phase10_same_type_style": "readable_titles_in_body_raw_qids_in_matrix",
                "same_type_visible": readable_same_type(same_type_ids),
                "phase10_scope_lock": "same_29_rows_no_expansion",
            }
        )
    control_fields = list(control_rows[0].keys())
    write_csv(OUT_MATRIX, control_rows, control_fields)

    student_lines = student_text.splitlines()
    backcheck_rows: list[dict[str, str]] = []
    for r in control_rows:
        visible_lines = line_numbers_for(student_lines, f"### {r['visible_title']}")
        raw_qid_lines = line_numbers_for(student_lines, r["question_id"])
        backcheck_rows.append(
            {
                "question_id": r["question_id"],
                "visible_title": r["visible_title"],
                "visible_heading_match": "yes" if visible_lines else "no",
                "visible_heading_line_numbers": ";".join(map(str, visible_lines)),
                "raw_qid_in_student_body": "yes" if raw_qid_lines else "no",
                "raw_qid_line_numbers": ";".join(map(str, raw_qid_lines)),
                "traceability_status": "PASS" if visible_lines and not raw_qid_lines else "FAIL",
            }
        )
    for qid in sorted(HARD_EXCLUDED):
        visible = qid_to_visible(qid)
        backcheck_rows.append(
            {
                "question_id": qid,
                "visible_title": visible,
                "visible_heading_match": "no",
                "visible_heading_line_numbers": "",
                "raw_qid_in_student_body": "yes" if qid in student_text else "no",
                "raw_qid_line_numbers": ";".join(map(str, line_numbers_for(student_lines, qid))),
                "traceability_status": "PASS" if qid not in student_text and "B=①④" not in student_text else "FAIL",
            }
        )
    write_csv(
        BACKCHECK_CSV,
        backcheck_rows,
        [
            "question_id",
            "visible_title",
            "visible_heading_match",
            "visible_heading_line_numbers",
            "raw_qid_in_student_body",
            "raw_qid_line_numbers",
            "traceability_status",
        ],
    )

    STYLE_DECISION_MD.write_text(
        "\n".join(
            [
                "# Phase10 Same-Type Index Style Decision",
                "",
                "- decision: `student_readable_titles_in_body_raw_qids_in_control_matrix`",
                "- reason: 学生正文不再显示 raw QID；同类题索引改成“年份 + 区 + 阶段 + 题号/小问”的可读标题。",
                "- traceability: `phase10_polish_control_matrix.csv` 保留 `question_id`、`same_type_ids` 与 `same_type_visible`。",
                "- scope_lock: 同类题只作为索引，未进入 29 行的题不得展开答案或解析。",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    CROSS_ANCHOR_MD.write_text(
        "\n".join(
            [
                "# Phase10 Cross Answer Anchor Patch",
                "",
                "| question_id | patch | status |",
                "|---|---|---|",
                "| `Q-2026顺义一模-19-2` | 在主讲线“思维方法”下补入可直接写到答题纸上的答案落点，保持科学思维主讲、推理辅助。 | `PATCHED` |",
                "| `Q-2024朝阳二模-19-1` | 保留第一空/第二空答案落点。 | `PRESERVED` |",
                "| `Q-2024朝阳二模-19-2` | 保留联言判断保真条件答案落点。 | `PRESERVED` |",
                "| `Q-2024朝阳期中-9` | 保留共变法答案落点。 | `PRESERVED` |",
                "| `Q-2026顺义一模-19-1` | 保留前提真实性和结构正确性答案落点。 | `PRESERVED` |",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    risk_lines = [
        "# Phase10 QID Risk Register",
        "",
        "| question_id | Phase10 lock | status |",
        "|---|---|---|",
        "| `Q-2025顺义一模-7` | 保留“大项不当扩大；A 错在说成小项不当扩大”；来源线索继续留在审计文件。 | `LOCKED` |",
        "| `Q-2025丰台期末-7` | 保持边界陷阱，不进入超前思维正例组。 | `LOCKED` |",
        "| `Q-2026顺义一模-19-2` | 科学思维三特征主讲，推理骨架辅助。 | `LOCKED` |",
        "| `Q-2024朝阳二模-19-1/19-2` | 无细则编号、文件编号、来源页码、审稿术语；第一空/第二空表达保留。 | `LOCKED` |",
        "| `Q-2024朝阳一模-20-1/20-2`、`Q-2026通州期末-19-2` | 充分条件与必要条件分开写。 | `LOCKED` |",
        "| `Q-2026丰台一模-18-2` | 甲必要条件肯定后件式正确、乙三段论大项不当扩大错误，链条不简化。 | `LOCKED` |",
        "| `Q-2025海淀二模-20` | 保持辩证思维角度池，两角度写深，不写三点全必答。 | `LOCKED` |",
        "| hard-excluded rows | 只可作为可读索引或缺席，不展开答案、选项、题型结论。 | `LOCKED` |",
        "",
        "## Audit Source Trace Pointers",
        "",
        "- `Q-2025顺义一模-7`：来源线索见 `09_student_draft/phase09_QID_risk_register.md` 的 `Q-2025顺义一模-7` 行；该行记录 `05_coverage/phase03_question_coverage_matrix.csv` 中 036 顺义参考答案摘录：大项“青年”在前提中不周延、在结论中周延，犯大项不当扩大，不是小项不当扩大。",
    ]
    RISK_REGISTER_MD.write_text("\n".join(risk_lines) + "\n", encoding="utf-8")

    term_hits = [term for term in FORBIDDEN_STUDENT_TERMS if term in student_text]
    choice_leftovers = []
    for pat in ["正确选项", "选 D。②", "选 A，原因", "选 C，理由", "B=①④", "B（①④）"]:
        if pat in student_text:
            choice_leftovers.append(pat)
    hard_expansion_failures = [
        qid for qid in HARD_EXCLUDED if qid in student_text or (qid == "Q-2024西城一模-11" and "B=①④" in student_text)
    ]
    terms_scan_lines = [
        "# Phase10 Internal Terms Scan",
        "",
        f"- target: `{OUT_MD.relative_to(ROOT)}`",
        f"- forbidden_term_hits: {len(term_hits)}",
        f"- hits: {', '.join(term_hits) if term_hits else 'NONE'}",
        f"- choice_format_leftovers: {len(choice_leftovers)}",
        f"- choice_hits: {', '.join(choice_leftovers) if choice_leftovers else 'NONE'}",
        f"- hard_excluded_raw_qid_or_wrong_pairing_failures: {len(hard_expansion_failures)}",
        f"- hard_excluded_failures: {', '.join(hard_expansion_failures) if hard_expansion_failures else 'NONE'}",
    ]
    TERMS_SCAN_MD.write_text("\n".join(terms_scan_lines) + "\n", encoding="utf-8")

    section_counts = Counter(r["draft_section"] for r in control_rows)
    module_counts = Counter(r["module"] for r in control_rows)
    trace_failures = [r for r in backcheck_rows if r["traceability_status"] != "PASS" and r["question_id"] not in HARD_EXCLUDED]
    checks = {
        "row_count_29": len(control_rows) == 29,
        "same_29_qids_as_phase09": {r["question_id"] for r in control_rows} == {r["question_id"] for r in matrix},
        "no_forbidden_student_terms": not term_hits,
        "no_choice_format_leftovers": not choice_leftovers,
        "no_hard_excluded_expansion": not hard_expansion_failures,
        "all_entry_visible_headings_match": not trace_failures,
        "q2025_shunyi_7_da_xiang_preserved": "真实错误应是大项不当扩大" in student_text and "小项不当扩大旧表达" not in student_text,
        "q2025_fengtai_7_boundary_trap": any(r["question_id"] == "Q-2025丰台期末-7" and r["draft_section"] == "边界陷阱" for r in control_rows),
        "q2026_shunyi_19_2_scientific_primary": any(r["question_id"] == "Q-2026顺义一模-19-2" and r["primary_mount"] == "思维" for r in control_rows),
        "q2026_shunyi_19_2_answer_anchor_added": "本题产品研发立足老人真实需求、研判老龄化趋势" in student_text,
    }
    verdict = "PASS_CODEXA_PHASE10_POLISH" if all(checks.values()) else "FAIL_CODEXA_PHASE10_POLISH"
    verification_lines = [
        "# Phase10 Codex A Polish Verification",
        "",
        f"- verdict: `{verdict}`",
        f"- student_polish: `{OUT_MD.relative_to(ROOT)}`",
        f"- control_matrix: `{OUT_MATRIX.relative_to(ROOT)}`",
        f"- input_rows: {len(matrix)}",
        f"- output_rows: {len(control_rows)}",
        f"- module_counts: {dict(module_counts)}",
        f"- section_counts: {dict(section_counts)}",
        "",
        "## Checks",
        "",
    ]
    for name, ok in checks.items():
        verification_lines.append(f"- {name}: {'PASS' if ok else 'FAIL'}")
    verification_lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- Phase10 is still polish/outline only.",
            "- It does not authorize Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品.",
            "- Same-type titles are readable indexes only; raw QIDs and source trace remain in the control matrix and audit files.",
        ]
    )
    VERIFICATION_MD.write_text("\n".join(verification_lines) + "\n", encoding="utf-8")

    print(verdict)
    print("student_polish", OUT_MD)
    print("control_rows", len(control_rows))
    print("term_hits", term_hits)
    print("choice_leftovers", choice_leftovers)


if __name__ == "__main__":
    main()
