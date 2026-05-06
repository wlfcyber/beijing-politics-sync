#!/usr/bin/env python3
"""Build Phase09 controlled student draft from the 29 Phase08 prototype rows only."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PHASE08_CSV = ROOT / "07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv"
FREEZE_CSV = ROOT / "05_coverage/phase08_opus_prototype_input_freeze.csv"
OUT_DIR = ROOT / "09_student_draft"
REVIEW_DIR = ROOT / "08_review"

STUDENT_MD = OUT_DIR / "phase09_student_draft_CONTROLLED_FROM_29.md"
CONTROL_CSV = OUT_DIR / "phase09_student_draft_control_matrix.csv"
BACKCHECK_CSV = OUT_DIR / "phase09_question_id_backcheck.csv"
CHANGELOG_CSV = OUT_DIR / "phase09_opus_or_codex_change_log.csv"
TERMS_SCAN_MD = OUT_DIR / "phase09_internal_terms_scan.md"
RISK_REGISTER_MD = OUT_DIR / "phase09_QID_risk_register.md"
VERIFICATION_MD = REVIEW_DIR / "phase09_codexA_student_draft_verification.md"


FIELD_LABELS = {
    "题目来源简记",
    "材料信号",
    "可写思维/方法",
    "为什么能想到",
    "答题动作",
    "解题动作",
    "答案落点",
    "易错陷阱",
    "同类题",
    "题型",
    "逻辑形式",
    "规则口诀",
    "有效式或错误式",
}

FORBIDDEN_STUDENT_TERMS = [
    "Phase07",
    "Phase08",
    "phase07",
    "phase08",
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
    "primary_reasoning_type",
    "rule_slogan",
    "source_entry_status",
    "question_id",
    "细则31",
    "细则022",
    "文件路径",
]

HARD_EXCLUDED_REFERENCES = {
    "Q-2024西城一模-11",
    "Q-2025海淀二模-12",
    "Q-2025海淀二模-13",
    "Q-2026顺义一模-3",
}

REASONING_ORDER = [
    "题型",
    "逻辑形式",
    "规则口诀",
    "有效式或错误式",
    "解题动作",
    "答案落点",
    "易错陷阱",
    "同类题",
]

THINKING_ORDER = [
    "材料信号",
    "可写思维/方法",
    "为什么能想到",
    "答题动作",
    "答案落点",
    "易错陷阱",
    "同类题",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def clean_text(text: str) -> str:
    text = text.strip()
    if text.endswith("。"):
        text = text[:-1]
    # Pair remaining ASCII double quotes into Chinese quotation marks.
    out: list[str] = []
    open_quote = False
    for ch in text:
        if ch == '"':
            out.append("“" if not open_quote else "”")
            open_quote = not open_quote
        else:
            out.append(ch)
    text = "".join(out)
    text = text.replace(" ,", "，").replace(",", "，")
    text = text.replace(";", "；")
    text = re.sub(r"([A-D])\(([^)]+)\)", r"\1（\2）", text)
    text = text.replace("Phase07", "").replace("Phase08", "")
    text = text.replace("phase07", "").replace("phase08", "")
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_fields(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    current: str | None = None
    for raw in text.split(";"):
        part = raw.strip()
        if not part:
            continue
        if ":" in part:
            label, value = part.split(":", 1)
            label = label.strip()
            if label in FIELD_LABELS:
                current = label
                fields[current] = value.strip()
                continue
        if current:
            fields[current] = (fields[current] + ";" + part).strip()
    return fields


def parse_cross(text: str) -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    if ";推理挂载(主挂载);" not in text or ";思维挂载(次挂载);" not in text:
        return parse_fields(text), {}, {}
    before, rest = text.split(";推理挂载(主挂载);", 1)
    reasoning, thinking = rest.split(";思维挂载(次挂载);", 1)
    source = parse_fields(before)
    reason_fields = parse_fields(reasoning)
    think_fields = parse_fields(thinking)
    return source, reason_fields, think_fields


def extract_title(source_text: str) -> str:
    source_text = clean_text(source_text)
    source_text = source_text.replace("题目来源简记:", "")
    source_text = source_text.replace(" 第 ", "第")
    source_text = source_text.replace(" 题", "题")
    source_text = source_text.replace("，选择题", "（选择题）")
    source_text = source_text.replace("，主观题", "（主观题）")
    source_text = source_text.replace("选择题。", "选择题")
    source_text = source_text.replace("主观题。", "主观题")
    return source_text


def set_override(fields: dict[str, str], **kwargs: str) -> dict[str, str]:
    updated = dict(fields)
    updated.update(kwargs)
    return updated


def apply_normal_overrides(qid: str, module: str, fields: dict[str, str]) -> tuple[dict[str, str], str, str, str]:
    draft_section = module
    primary_mount = module
    secondary_mount = ""
    risk_status = "standardized_from_phase08"

    if qid == "Q-2025丰台期末-7":
        draft_section = "边界陷阱"
        primary_mount = "边界陷阱"
        risk_status = "resolved_boundary_trap_not_thinking_mainline"
        fields = set_override(
            fields,
            **{
                "材料信号": "漫画把人困在“为昨天懊恼、替明天担心”的状态里，真正提醒的是回到当下现实，不是让学生去写超前思维",
                "可写思维/方法": "这道题是边界陷阱：答案落在哲学唯物论的“从实际出发、从当下做起”，选必三“超前思维”只是干扰项",
                "为什么能想到": "如果把“明天”二字直接等同于超前思维，就会掉入选项陷阱；漫画的重心是不要脱离现实、不要被过去和未来牵着走",
                "答题动作": "先排除“超前思维创造幸福”的夸大表述，再抓住“从实际出发、把握当下”这个哲学落点",
                "答案落点": "选 C，理由是从实际出发、从当下做起，生活才能少些迷茫",
                "易错陷阱": "A 把关注当下说成“就能”成功，绝对化；B 借“明天”诱导写超前思维，方向反了；D 把成功关键泛化，材料支撑不足",
            },
        )

    if qid == "Q-2025顺义一模-7":
        risk_status = "resolved_answer_expression_rechecked_against_source"
        fields = set_override(
            fields,
            **{
                "题型": "三段论谬误判断纠错题",
                "逻辑形式": "三段论 + 项的周延 + 逆向选择",
                "规则口诀": "前提中不周延的项，结论中不得周延；一个三段论只能有三个不同的项；中项至少周延一次",
                "有效式或错误式": "A 项的推理实际问题是“大项不当扩大”：大项“青年”在肯定前提中不周延，却在否定结论中周延；A 把它说成“小项不当扩大”，所以 A 的逻辑分析错误",
                "解题动作": "先看题干问“逻辑分析错误的是”，这是逆向选择；再逐项划大项、小项、中项，最后判断“题目给出的谬误名称”是否与真实谬误一致",
                "答案落点": "选 A，原因是 A 对谬误名称判断错了；真实错误应是大项不当扩大，不是小项不当扩大",
                "易错陷阱": "B 的“两否定前提不能必然推出结论”、C 的“四概念”、D 的“中项不周延”都是可成立的分析，不是本题要选的错误分析",
            },
        )

    if qid == "Q-2024朝阳一模-20-1":
        risk_status = "resolved_sufficient_conditional_valid_form"
        fields = set_override(
            fields,
            **{
                "规则口诀": "充分条件假言推理：前真后必真；否定后件，可以否定前件",
                "有效式或错误式": "结构是“如果没有广泛生长竹子，就不可能有大量炭化竹节；现在有大量炭化竹节，所以并非没有广泛生长竹子”。这是充分条件假言推理的否定后件式，有效",
                "答案落点": "写“这是充分条件假言推理；依据前真后必真、后假则前假，否定后件可以否定前件，所以推理成立”",
            },
        )

    if qid == "Q-2024朝阳一模-20-2":
        risk_status = "resolved_necessary_conditional_valid_form"
        fields = set_override(
            fields,
            **{
                "规则口诀": "必要条件假言推理：“只有 P 才 Q”；肯定后件，可以肯定前件；仅肯定前件，不能肯定后件",
                "有效式或错误式": "可补为“只有 A 区域古代气候温暖，A 区域古代才有可能生长竹子；A 区域古代广泛生长着竹子，所以 A 区域古代气候较为温暖”。这是必要条件假言推理的肯定后件式，有效",
                "解题动作": "先把竹子生长的必要条件写成“只有……才……”；再由“A 区域古代广泛生长着竹子”推出“A 区域古代气候温暖”；时间限定词“古代/当时”必须保留",
                "答案落点": "补全句式时写清“只有 A 区域古代气候温暖，A 区域古代才有可能生长竹子”，再推出古代气候较为温暖",
            },
        )

    if qid == "Q-2026通州期末-19-2":
        risk_status = "resolved_sufficient_vs_necessary_split"
        fields = set_override(
            fields,
            **{
                "规则口诀": "充分条件：肯定前件可以肯定后件；必要条件：肯定后件可以肯定前件，仅肯定前件不能肯定后件",
                "有效式或错误式": "推理①若为充分条件假言推理的肯定前件式，则结构有效；推理②若为必要条件假言推理的肯定前件式，则结构无效，因为“有必要条件”不等于“结果一定发生”",
                "答案落点": "推理①有效，推理②无效；答题时必须分别写出充分条件和必要条件的规则，不能用一个“肯定前件”口诀混答",
            },
        )

    if qid == "Q-2026丰台一模-18-2":
        risk_status = "resolved_L4_reasoning_chain_preserved"
        fields = set_override(
            fields,
            **{
                "题型": "甲：必要条件假言推理的肯定后件式；乙：三段论大项不当扩大",
                "规则口诀": "必要条件假言推理：肯定后件可以肯定前件；三段论：前提中不周延的项，结论中不得周延",
                "有效式或错误式": "甲为必要条件假言推理的肯定后件式，且前提真实，推理成立；乙的大项在前提中不周延，却在结论中周延，犯大项不当扩大，推理不成立",
                "解题动作": "先识别甲为必要条件假言推理的肯定后件式，并结合前提真实判定甲推理正确；再识别乙为三段论大项在前提中不周延却在结论中周延，属于大项不当扩大，判定乙推理错误",
                "答案落点": "甲正确，乙错误；甲不能泛写成演绎推理，乙必须点出“大项不当扩大”",
            },
        )

    if qid == "Q-2025海淀二模-20":
        risk_status = "resolved_angle_pool_preserved"
        fields = set_override(
            fields,
            **{
                "答题动作": "从“整体性、动态性、分析与综合、质量互变、辩证否定”里选最贴材料的两个角度写深；每个角度都要带上共享发展的具体层次和推进共同富裕的作用",
                "答案落点": "角度池写法：可优先选“整体性 + 动态性”或“分析与综合 + 质量互变”等组合，核心是两角度写透；不要把所有角度堆成必答清单",
                "易错陷阱": "不能写成三点全必答；不能把辩证否定写成否定一切；整体性必须写出联结、综合、系统优化，不能只写“整体”两个字",
            },
        )

    if qid in {"Q-2024朝阳二模-19-1", "Q-2024朝阳二模-19-2"}:
        risk_status = "resolved_no_audit_expression_reflux"

    return fields, draft_section, primary_mount, secondary_mount or "", risk_status


def apply_cross_overrides(qid: str, source: dict[str, str], reason: dict[str, str], think: dict[str, str]) -> tuple[dict[str, str], dict[str, str], str, str, str]:
    primary = "推理"
    secondary = "思维"
    risk_status = "cross_double_mount_preserved"

    if qid == "Q-2024朝阳二模-19-1":
        risk_status = "resolved_no_audit_expression_reflux"
        reason = set_override(
            reason,
            **{
                "逻辑形式": "第一空考辩证思维动态性，第二空考类比推理",
                "有效式或错误式": "第一空写“动态性”；第二空必须写“类比推理”，不要改写成相近词",
                "解题动作": "看到“生生不息、日新、革新、不断充实”，第一空锁定动态性；看到由一个对象经验迁移到另一个对象，第二空锁定类比推理",
                "答案落点": "第一空写“动态性”，第二空写“类比推理”",
                "易错陷阱": "第一空填“整体性/质量互变”丢分；第二空把“类比”改写为其他词不给分",
            },
        )
    if qid == "Q-2024朝阳二模-19-2":
        risk_status = "resolved_no_audit_expression_reflux"
        reason = set_override(
            reason,
            **{
                "规则口诀": "“当且仅当各联言支都真，联言判断才真；一假即假”",
                "有效式或错误式": "联言判断只有在各个联言支都真实时才为真；只要有一个联言支为假，整个联言判断就为假",
                "解题动作": "先把材料中的并列表述拆成若干联言支，再写清“全真才真、一假即假”的保真条件",
                "答案落点": "写出联言判断本身，并写清“全真才真、一假即假”的保真条件",
            },
        )
        think = set_override(
            think,
            **{
                "题型": "辩证思维 · 动态性（与第(1)问辅助线一致）",
            },
        )
    if qid == "Q-2026顺义一模-19-2":
        primary = "思维"
        secondary = "推理"
        risk_status = "resolved_scientific_thinking_primary_reasoning_auxiliary"
        think = set_override(
            think,
            **{
                "题型": "科学思维三特征",
                "答题动作": "把客观性、预见性、可检验性逐条对应材料：从老人真实需求出发，体现客观性；研判老龄化趋势和市场潜力，体现预见性；反复测试、多轮迭代，体现可检验性",
                "易错陷阱": "主讲线是科学思维，不是典型三段论；只列三个特征不分析材料会丢分",
            },
        )
        reason = set_override(
            reason,
            **{
                "题型": "三段论 / 判断 / 推理（作为科学思维三特征落地的推理骨架）",
                "逻辑形式": "此问可放在交叉题中辅助理解，但卷面主骨架是科学思维三特征，不要把它写成典型三段论题",
                "解题动作": "推理侧只提醒学生：结论必须由材料事实支撑；真正展开时仍回到客观性、预见性、可检验性",
            },
        )
    if qid == "Q-2024朝阳期中-9":
        reason = set_override(reason, **{"答案落点": "选 B，判断为归纳推理中的共变法"})
    if qid == "Q-2026顺义一模-19-1":
        reason = set_override(reason, **{"答案落点": "从前提真实性和结构正确性两方面判断：材料不能必然推出该结论，理由必须写完整"})
    return reason, think, primary, secondary, risk_status


def format_bullets(fields: dict[str, str], order: list[str]) -> list[str]:
    lines: list[str] = []
    label_map = {
        "同类题": "同类题索引",
    }
    for label in order:
        value = fields.get(label, "").strip()
        if not value:
            continue
        shown_label = label_map.get(label, label)
        lines.append(f"- {shown_label}：{clean_text(value)}。")
    return lines


def qids_from_text(text: str) -> list[str]:
    return re.findall(r"Q-\d{4}[\u4e00-\u9fff]+(?:一模|二模|期末|期中)-\d+(?:-\d+)?", text)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    REVIEW_DIR.mkdir(parents=True, exist_ok=True)

    phase08_rows = read_csv(PHASE08_CSV)
    freeze_rows = read_csv(FREEZE_CSV)
    freeze_by_qid = {r["question_id"]: r for r in freeze_rows}
    freeze_ids = [r["question_id"] for r in freeze_rows]
    proto_ids = [r["question_id"] for r in phase08_rows]
    if set(proto_ids) != set(freeze_ids):
        raise SystemExit("Phase08 prototype id set differs from freeze")

    section_order = {"思维": 0, "推理": 1, "交叉": 2}
    ordered_rows = sorted(
        phase08_rows,
        key=lambda r: (section_order.get(r["module"], 9), proto_ids.index(r["question_id"])),
    )

    md: list[str] = [
        "# 选必三《逻辑与思维》学生稿草案",
        "",
        "本稿用于下一轮校对和成文化，不是可直接交付的排版稿。",
        "",
        "## 使用方式",
        "",
        "- 看到材料，先判断它是在考“思维方法”还是“推理规则”。",
        "- 思维题按“材料信号 → 可写方法 → 为什么能想到 → 答题动作 → 答案落点 → 易错陷阱”走。",
        "- 推理题按“题型 → 逻辑形式 → 规则口诀 → 有效式或错误式 → 解题动作 → 答案落点 → 易错陷阱”走。",
        "- 同类题只作为索引，不在本稿里展开答案。",
        "",
        "---",
        "",
        "## 一、思维方法",
        "",
    ]

    control_rows: list[dict[str, str]] = []
    changelog_rows: list[dict[str, str]] = []
    risk_rows: list[dict[str, str]] = []
    entry_no = 0

    def add_control(
        row: dict[str, str],
        title: str,
        draft_section: str,
        primary_mount: str,
        secondary_mount: str,
        risk_status: str,
        same_type_ids: str,
    ) -> None:
        freeze = freeze_by_qid[row["question_id"]]
        control_rows.append(
            {
                "entry_no": str(len(control_rows) + 1),
                "question_id": row["question_id"],
                "visible_title": title,
                "module": row["module"],
                "draft_section": draft_section,
                "question_type": freeze["question_type"],
                "source_entry_status": row["source_entry_status"],
                "input_permission": freeze["input_permission"],
                "primary_mount": primary_mount,
                "secondary_mount": secondary_mount,
                "same_type_ids": same_type_ids,
                "gpt_named_risk_status": risk_status,
                "student_body_origin": "phase08_prototype_29_only",
                "no_expansion_policy": "no_74_pool_no_45_hold_no_288_L0_no_hard_excluded_expansion",
            }
        )
        changelog_rows.append(
            {
                "question_id": row["question_id"],
                "change_type": "student_facing_rewrite",
                "changed_by": "Codex_A",
                "from_file": str(PHASE08_CSV.relative_to(ROOT)),
                "to_file": str(STUDENT_MD.relative_to(ROOT)),
                "notes": risk_status,
            }
        )

    # Thinking mainline and boundary trap.
    thinking_rows = [r for r in ordered_rows if r["module"] == "思维"]
    boundary_rows: list[dict[str, str]] = []
    for row in thinking_rows:
        qid = row["question_id"]
        fields = parse_fields(row["generated_text"])
        fields, draft_section, primary_mount, secondary_mount, risk_status = apply_normal_overrides(qid, "思维", fields)
        title = extract_title(fields.get("题目来源简记", qid))
        same_type_ids = clean_text(fields.get("同类题", ""))
        if draft_section == "边界陷阱":
            boundary_rows.append(row)
            continue
        entry_no += 1
        md.append(f"### {title}")
        md.append("")
        md.extend(format_bullets(fields, THINKING_ORDER))
        md.append("")
        add_control(row, title, draft_section, primary_mount, secondary_mount, risk_status, same_type_ids)

    md.append("## 二、边界陷阱")
    md.append("")
    for row in boundary_rows:
        qid = row["question_id"]
        fields = parse_fields(row["generated_text"])
        fields, draft_section, primary_mount, secondary_mount, risk_status = apply_normal_overrides(qid, "思维", fields)
        title = extract_title(fields.get("题目来源简记", qid))
        same_type_ids = clean_text(fields.get("同类题", ""))
        md.append(f"### {title}")
        md.append("")
        md.extend(format_bullets(fields, THINKING_ORDER))
        md.append("")
        add_control(row, title, draft_section, primary_mount, secondary_mount, risk_status, same_type_ids)

    md.append("## 三、推理题型")
    md.append("")
    for row in [r for r in ordered_rows if r["module"] == "推理"]:
        qid = row["question_id"]
        fields = parse_fields(row["generated_text"])
        fields, draft_section, primary_mount, secondary_mount, risk_status = apply_normal_overrides(qid, "推理", fields)
        title = extract_title(fields.get("题目来源简记", qid))
        same_type_ids = clean_text(fields.get("同类题", ""))
        md.append(f"### {title}")
        md.append("")
        md.extend(format_bullets(fields, REASONING_ORDER))
        md.append("")
        add_control(row, title, draft_section, primary_mount, secondary_mount, risk_status, same_type_ids)

    md.append("## 四、交叉题")
    md.append("")
    md.append("交叉题要保留两条线：一条是卷面主讲线，一条是辅助理解线。主讲线决定正文展开重点，辅助线只帮助防误判。")
    md.append("")
    for row in [r for r in ordered_rows if r["module"] == "交叉"]:
        qid = row["question_id"]
        source, reason, think = parse_cross(row["generated_text"])
        reason, think, primary, secondary, risk_status = apply_cross_overrides(qid, source, reason, think)
        title = extract_title(source.get("题目来源简记", qid))
        same_type_ids = clean_text(reason.get("同类题") or think.get("同类题") or "")
        md.append(f"### {title}")
        md.append("")
        if primary == "思维":
            md.append("#### 主讲线：思维方法")
            md.extend(format_bullets(think, ["题型", "材料信号", "答题动作", "易错陷阱"]))
            md.append("")
            md.append("#### 辅助线：推理结构")
            md.extend(format_bullets(reason, ["题型", "逻辑形式", "解题动作", "易错陷阱", "同类题"]))
        else:
            md.append("#### 主讲线：推理结构")
            md.extend(format_bullets(reason, ["题型", "逻辑形式", "规则口诀", "有效式或错误式", "解题动作", "答案落点", "易错陷阱"]))
            md.append("")
            md.append("#### 辅助线：思维方法")
            md.extend(format_bullets(think, ["题型", "材料信号", "答题动作", "易错陷阱", "同类题"]))
        if same_type_ids and "同类题索引" not in "\n".join(md[-12:]):
            md.append(f"- 同类题索引：{same_type_ids}。")
        md.append("")
        add_control(row, title, "交叉", primary, secondary, risk_status, same_type_ids)

    STUDENT_MD.write_text("\n".join(md).strip() + "\n", encoding="utf-8")

    control_fields = [
        "entry_no",
        "question_id",
        "visible_title",
        "module",
        "draft_section",
        "question_type",
        "source_entry_status",
        "input_permission",
        "primary_mount",
        "secondary_mount",
        "same_type_ids",
        "gpt_named_risk_status",
        "student_body_origin",
        "no_expansion_policy",
    ]
    write_csv(CONTROL_CSV, control_rows, control_fields)
    write_csv(
        CHANGELOG_CSV,
        changelog_rows,
        ["question_id", "change_type", "changed_by", "from_file", "to_file", "notes"],
    )

    student_text = STUDENT_MD.read_text(encoding="utf-8")
    qid_lines = {}
    for line_no, line in enumerate(student_text.splitlines(), 1):
        for qid in qids_from_text(line):
            qid_lines.setdefault(qid, []).append(line_no)

    visible_titles = {r["question_id"]: r["visible_title"] for r in control_rows}
    backcheck_rows: list[dict[str, str]] = []
    for qid in sorted(set(freeze_ids) | set(qid_lines)):
        role = "entry_control_row" if qid in freeze_ids else "reference_only_same_type"
        if qid in HARD_EXCLUDED_REFERENCES:
            role = "hard_excluded_reference_only"
        line_hits = qid_lines.get(qid, [])
        visible_title = visible_titles.get(qid, "")
        visible_line_hits: list[int] = []
        if visible_title:
            for line_no, line in enumerate(student_text.splitlines(), 1):
                if line.strip().lstrip("# ").strip() == visible_title:
                    visible_line_hits.append(line_no)
        hard_ok = "PASS"
        if qid in HARD_EXCLUDED_REFERENCES and line_hits:
            lines = student_text.splitlines()
            for ln in line_hits:
                if "同类题索引" not in lines[ln - 1]:
                    hard_ok = "FAIL_EXPANDED_HARD_EXCLUDED_REFERENCE"
        backcheck_rows.append(
            {
                "question_id": qid,
                "role": role,
                "in_phase08_freeze": "yes" if qid in freeze_ids else "no",
                "appears_in_student_md": "yes" if line_hits else "no",
                "line_numbers": ";".join(map(str, line_hits)),
                "visible_title_match": "yes" if visible_line_hits else "no",
                "visible_title_line_numbers": ";".join(map(str, visible_line_hits)),
                "hard_excluded_reference_check": hard_ok,
            }
        )
    write_csv(
        BACKCHECK_CSV,
        backcheck_rows,
        [
            "question_id",
            "role",
            "in_phase08_freeze",
            "appears_in_student_md",
            "line_numbers",
            "visible_title_match",
            "visible_title_line_numbers",
            "hard_excluded_reference_check",
        ],
    )

    for qid, issue, resolution in [
        ("Q-2025丰台期末-7", "不能放入思维主链正文", "已移入边界陷阱小节，明确答案落在哲学唯物论，不作为选必三正例"),
        ("Q-2025顺义一模-7", "答案落点表达自相矛盾", "已据原答案改为大项不当扩大；A 项错在把它说成小项不当扩大；源迹：05_coverage/phase03_question_coverage_matrix.csv 的 036 顺义参考答案摘录写明“大项‘青年’在前提中不周延、在结论中周延，犯大项不当扩大，不是小项不当扩大”"),
        ("Q-2026顺义一模-19-2", "不能写成典型三段论题", "已改为科学思维主讲，推理结构辅助"),
        ("Q-2024朝阳二模-19-1", "不得回流审稿味编号", "已统一为学生可理解的“第一空/第二空”表达，不保留文件编号或审稿编号"),
        ("Q-2024朝阳二模-19-2", "不得回流审稿味编号", "已用联言判断保真条件表述，不含文件或编号痕迹"),
        ("Q-2024朝阳一模-20-1", "充分条件有效式需清晰", "已写明否定后件式有效"),
        ("Q-2024朝阳一模-20-2", "必要条件有效式需清晰", "已写明肯定后件式有效并保留古代/当时"),
        ("Q-2026通州期末-19-2", "充分/必要条件不得混用", "已分列充分条件肯前有效、必要条件肯前无效"),
        ("Q-2026丰台一模-18-2", "L4 动作链不得简写", "已保留甲必要条件肯后式真实成立、乙三段论大项不当扩大"),
        ("Q-2025海淀二模-20", "角度池不得变三点全必答", "已写成角度池选二写深，不写三点全必答"),
    ]:
        risk_rows.append({"question_id": qid, "gpt_issue": issue, "resolution": resolution, "status": "RESOLVED_FOR_PHASE09_DRAFT"})
    risk_lines = [
        "# Phase09 QID Risk Register",
        "",
        "| question_id | GPT issue | Phase09 resolution | status |",
        "|---|---|---|---|",
    ]
    for r in risk_rows:
        risk_lines.append(f"| `{r['question_id']}` | {r['gpt_issue']} | {r['resolution']} | `{r['status']}` |")
    RISK_REGISTER_MD.write_text("\n".join(risk_lines) + "\n", encoding="utf-8")

    term_hits = []
    for term in FORBIDDEN_STUDENT_TERMS:
        if term in student_text:
            term_hits.append(term)
    q11_wrong = "B=①④" in student_text or "B（①④）" in student_text
    hard_expanded_fails = [r for r in backcheck_rows if r["hard_excluded_reference_check"].startswith("FAIL")]

    scan_lines = [
        "# Phase09 Internal Terms Scan",
        "",
        f"- target: `{STUDENT_MD.relative_to(ROOT)}`",
        f"- forbidden_term_hits: {len(term_hits)}",
        f"- hits: {', '.join(term_hits) if term_hits else 'NONE'}",
        f"- q11_wrong_pairing_hit: {'YES' if q11_wrong else 'NO'}",
        f"- hard_excluded_reference_expansion_failures: {len(hard_expanded_fails)}",
    ]
    TERMS_SCAN_MD.write_text("\n".join(scan_lines) + "\n", encoding="utf-8")

    status_counts = Counter(r["source_entry_status"] for r in control_rows)
    module_counts = Counter(r["module"] for r in control_rows)
    draft_section_counts = Counter(r["draft_section"] for r in control_rows)
    checks = {
        "row_count_29": len(control_rows) == 29,
        "id_set_equals_phase08_freeze": set(r["question_id"] for r in control_rows) == set(freeze_ids),
        "no_forbidden_student_terms": not term_hits,
        "no_q11_wrong_pairing": not q11_wrong,
        "hard_excluded_reference_only": not hard_expanded_fails,
        "q2025_shunyi_7_corrected_to_da_xiang": "真实错误应是大项不当扩大" in student_text and "确为小项不当扩大" not in student_text,
        "q2025_fengtai_7_boundary_trap": any(r["question_id"] == "Q-2025丰台期末-7" and r["draft_section"] == "边界陷阱" for r in control_rows),
        "q2026_shunyi_19_2_scientific_primary": any(r["question_id"] == "Q-2026顺义一模-19-2" and r["primary_mount"] == "思维" for r in control_rows),
    }
    verdict = "PASS_CODEXA_PHASE09_CONTROLLED_DRAFT" if all(checks.values()) else "FAIL_CODEXA_PHASE09_CONTROLLED_DRAFT"
    verification_lines = [
        "# Phase09 Codex A Student Draft Verification",
        "",
        f"- verdict: `{verdict}`",
        f"- student_draft: `{STUDENT_MD.relative_to(ROOT)}`",
        f"- control_matrix: `{CONTROL_CSV.relative_to(ROOT)}`",
        f"- input_rows: {len(freeze_rows)}",
        f"- draft_rows: {len(control_rows)}",
        f"- module_counts: {dict(module_counts)}",
        f"- status_counts: {dict(status_counts)}",
        f"- draft_section_counts: {dict(draft_section_counts)}",
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
            "- This Phase09 draft is still a controlled student-draft candidate only.",
            "- It does not authorize Word/PDF, final PASS, final wording, or expansion beyond the 29 Phase08 prototype rows.",
            "- Same-type IDs are index references only and are not expanded into answers.",
        ]
    )
    VERIFICATION_MD.write_text("\n".join(verification_lines) + "\n", encoding="utf-8")

    print(verdict)
    print("student_draft", STUDENT_MD)
    print("control_rows", len(control_rows))
    print("term_hits", term_hits)


if __name__ == "__main__":
    main()
