#!/usr/bin/env python3
"""Apply Lane B Phase08 review-only cleanliness fixes.

The patch only edits teaching-body wording in the Phase08 prototype and keeps
question IDs, answers, statuses, pairings, and freeze inputs unchanged.
"""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
PROTO_MD = ROOT / "07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.md"
PROTO_CSV = ROOT / "07_student_prototype/phase08_opus_teaching_prototype_REVIEW_ONLY.csv"
CHANGE_CSV = ROOT / "07_student_prototype/phase08_opus_change_log.csv"
COMPLIANCE_MD = ROOT / "opus_writer/phase08_teaching_prototype/phase08_opus_boundary_compliance.md"


def replace_once_or_more(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        if new in text:
            return text
        raise SystemExit(f"missing replacement target [{label}]: {old}")
    return text.replace(old, new)


def patch_md() -> None:
    text = PROTO_MD.read_text(encoding="utf-8")
    replacements = [
        (
            '每条保留 question_id 不脱离原始定位。',
            '每条保留 question_id 不脱离题目定位。',
            "md-reading-note",
        ),
        (
            '答案落点:在"创新思维与逻辑思维区别题"这一类型上得分,重点写清创新思维不排斥逻辑分析、合作创新建立在对前人成果继承之上。',
            '答案落点:正确选项 C(②③),重点写清创新思维不排斥逻辑分析、合作创新建立在对前人成果继承之上。',
            "md-q2024cyym-7-answer-letter",
        ),
        (
            "答案落点:点出活动是多主体协同完成、整体性贯穿调查与提案全过程,并指向制度优势的运用。",
            "答案落点:正确选项 D(③④),点出活动是多主体协同完成、整体性贯穿调查与提案全过程,并指向制度优势的运用。",
            "md-q2024cyym-9-answer-letter",
        ),
        (
            '答案落点:在"哲学题、选必三超前思维作干扰"这一类型上确认 C 项。',
            '答案落点:正确选项 C,落在哲学唯物论“从实际出发、从当下做起”;选必三“超前思维”只是干扰项。',
            "md-q2025ftqm-7-soften",
        ),
        (
            "答案落点:正确选项 B(原始 phase07 数据已锁定 B),理由是①与③均犯中项不周延的谬误。",
            "答案落点:正确选项 B,理由是①与③均犯中项不周延的谬误。",
            "md-q2025dcqm-13-phase07",
        ),
        (
            '答案落点:正确选项 A(原始 phase07 数据锁定);理由是 A 选项对"小项不当扩大"的描述本身存在错误。',
            '答案落点:正确选项 A;理由是 A 选项对"小项不当扩大"的描述本身存在错误。',
            "md-q2025syym-7-phase07",
        ),
        (
            "题型:类比推理 + 联言判断作辅助;评分细则要求填动态性 + 类比推理。",
            "题型:类比推理 + 联言判断作辅助;本题要求填动态性 + 类比推理。",
            "md-q2024cyem-19-1-rubric",
        ),
        (
            '有效式或错误式:细则明确①动态性(替代写法限定为变化发展/矛盾运动/创新);②类比推理"无变通"——必须严格写"类比推理",不可改写。',
            '有效式或错误式:本题明确①动态性(替代写法限定为变化发展/矛盾运动/创新);②类比推理"无变通"——必须严格写"类比推理",不可改写。',
            "md-q2024cyem-19-1-xize",
        ),
        (
            "有效式或错误式:细则明确联言判断本身得分(2 分) + 保真条件(3 分):全真才真/一假即假。",
            "有效式或错误式:本题要求写出联言判断本身(2 分) + 保真条件(3 分):全真才真/一假即假。",
            "md-q2024cyem-19-2-xize",
        ),
        (
            "细则要求按两条件分析判定。",
            "本题要求按两条件分析判定。",
            "md-q2026syym-19-1-xize",
        ),
    ]
    for old, new, label in replacements:
        text = replace_once_or_more(text, old, new, label)
    PROTO_MD.write_text(text, encoding="utf-8")


CSV_GENERATED_TEXT_REPLACEMENTS: dict[str, list[tuple[str, str, str]]] = {
    "Q-2024朝阳一模-7": [
        (
            "答案落点:在创新思维与逻辑思维区别题型上得分",
            "答案落点:正确选项 C(②③),在创新思维与逻辑思维区别题型上得分",
            "csv-q2024cyym-7-answer-letter",
        ),
    ],
    "Q-2024朝阳一模-9": [
        (
            "答案落点:在跨模块cross政治+辩证思维系统观念题型上得分",
            "答案落点:正确选项 D(③④),在政治模块与辩证思维系统观念结合题型上得分",
            "csv-q2024cyym-9-answer-letter",
        ),
    ],
    "Q-2024海淀二模-17-1": [
        (
            "表格化采分细则",
            "表格化采分要求",
            "csv-q2024hdem-17-1-xize",
        ),
    ],
    "Q-2025丰台期末-7": [
        (
            '答案落点:在"哲学题_选必三超前思维作干扰_答案非选必三"类型上确认 C',
            "答案落点:正确选项 C,落在哲学唯物论从实际出发、从当下做起;选必三超前思维只是干扰项",
            "csv-q2025ftqm-7-soften",
        ),
    ],
    "Q-2024朝阳一模-20-1": [
        (
            '细则31先指出推理类型(充分条件假言推理1分),理由"前真后必真,后假则前假"(2分)',
            '先指出推理类型(充分条件假言推理1分),再说明理由"前真后必真,后假则前假"(2分)',
            "csv-q2024cyym-20-1-xize31",
        ),
    ],
    "Q-2024朝阳二模-19-1": [
        (
            "类比推理+联言判断辅助(细则022填空1=动态性,填空2=类比推理)",
            "类比推理+联言判断辅助(第一空=动态性,第二空=类比推理)",
            "csv-q2024cyem-19-1-xize022-a",
        ),
        (
            "答案落点:依据细则022填空答案2分+保真表述3分",
            "答案落点:按本题要求写出填空答案2分+保真表述3分",
            "csv-q2024cyem-19-1-xize022-b",
        ),
        (
            ";cross_reference_policy:thinking 与 reasoning 同源,reduce repetitive wording 但禁止单挂",
            ";双挂载提示:思维与推理同源,但不可单挂",
            "csv-q2024cyem-19-1-cross-policy",
        ),
    ],
    "Q-2024朝阳二模-19-2": [
        (
            "有效式或错误式:细则022联言判断本身2分+保真条件3分:全真才真/一假即假",
            "有效式或错误式:联言判断本身2分+保真条件3分:全真才真/一假即假",
            "csv-q2024cyem-19-2-xize022-a",
        ),
        (
            "答案落点:依细则022 2+3 分写出联言判断成立条件",
            "答案落点:按 2+3 分要求写出联言判断成立条件",
            "csv-q2024cyem-19-2-xize022-b",
        ),
        (
            ";cross_reference_policy:与 19(1)动态性挂载共享,但禁止单挂",
            ";双挂载提示:与 19(1)动态性挂载共享,但不可单挂",
            "csv-q2024cyem-19-2-cross-policy",
        ),
    ],
    "Q-2024朝阳期中-9": [
        (
            ";cross_reference_policy:同类题中 Q-2024西城一模-11 仅作 ID 引用",
            "",
            "csv-q2024cyqz-9-cross-policy",
        ),
    ],
    "Q-2026顺义一模-19-1": [
        (
            ";cross_reference_policy:与 19(2)互为同题参照,禁止单挂",
            ";双挂载提示:与 19(2)互为同题参照,不可单挂",
            "csv-q2026syym-19-1-cross-policy",
        ),
    ],
    "Q-2026顺义一模-19-2": [
        (
            '主挂载推理:推理结构与科学思维三特征联结(原始 phase07 数据将 19(2) primary_reasoning_type 置为"三段论;判断;推理",rule_slogan 为"科学思维三特征")',
            "主挂载推理:推理结构与科学思维三特征联结",
            "csv-q2026syym-19-2-pipeline",
        ),
        (
            ";cross_reference_policy:与 19(1)互为同题参照,禁止单挂",
            ";双挂载提示:与 19(1)互为同题参照,不可单挂",
            "csv-q2026syym-19-2-cross-policy",
        ),
    ],
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit(f"missing csv header: {path}")
        return list(reader.fieldnames), list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def patch_proto_csv() -> None:
    fieldnames, rows = read_csv(PROTO_CSV)
    seen = set()
    for row in rows:
        qid = row["question_id"]
        replacements = CSV_GENERATED_TEXT_REPLACEMENTS.get(qid)
        if not replacements:
            continue
        text = row["generated_text"]
        for old, new, label in replacements:
            text = replace_once_or_more(text, old, new, label)
        if any(term in text for term in ["phase07", "primary_reasoning_type", "rule_slogan", "细则", "cross_reference_policy", "reduce repetitive wording"]):
            raise SystemExit(f"dirty generated_text remains for {qid}: {text}")
        row["generated_text"] = text
        seen.add(qid)
    missing = set(CSV_GENERATED_TEXT_REPLACEMENTS) - seen
    if missing:
        raise SystemExit(f"missing csv rows for patch: {sorted(missing)}")
    write_csv(PROTO_CSV, fieldnames, rows)


CHANGE_LOG_AFTER_UPDATES = {
    "Q-2024朝阳一模-7": '教学小标题化;显式补入答案 C(②③);不暴露 framework_node 标记;答案、易错陷阱、同类题完整保留。',
    "Q-2024朝阳一模-9": '小标题化;显式补入答案 D(③④);同类题以分号串保留(含 Q-2026顺义一模-3 仅作 ID 引用);framework_node 标记不暴露。',
    "Q-2025丰台期末-7": '转写为"正确选项 C,落在哲学唯物论从实际出发、从当下做起;选必三超前思维只是干扰项";不暴露 Lane B 字眼;答案 C 不变。',
    "Q-2024朝阳一模-20-1": '转化为"先指出推理类型(充分条件假言推理),再用前真后必真后假则前假作为推理理由"教学语言;1+2 分赋分保留;不暴露文件编号。',
    "Q-2024朝阳二模-19-1": '统一"主挂载推理(类比推理 + 联言判断辅助) + 次挂载思维(辩证思维·动态性)"双段;两个填空答案锁定不变;移除文件编号式表述;不删任一挂载。',
    "Q-2024朝阳二模-19-2": '转化为"联言判断本身 + 保真条件全真才真/一假即假"教学动作;2+3 分结构保留;移除文件编号式表述;思维次挂载延续 19(1)动态性。',
    "Q-2026顺义一模-19-2": '不重新归类;展示为"主挂载:推理结构与科学思维三特征联结;次挂载:科学思维"双挂载;移除 phase07 字段名式表述;同题 19(1)互为参照,禁止单挂。',
}


def patch_change_log_csv() -> None:
    fieldnames, rows = read_csv(CHANGE_CSV)
    seen = set()
    for row in rows:
        qid = row["question_id"]
        if qid in CHANGE_LOG_AFTER_UPDATES:
            row["after_prototype_text"] = CHANGE_LOG_AFTER_UPDATES[qid]
            seen.add(qid)
    missing = set(CHANGE_LOG_AFTER_UPDATES) - seen
    if missing:
        raise SystemExit(f"missing change-log rows for patch: {sorted(missing)}")
    write_csv(CHANGE_CSV, fieldnames, rows)


def patch_compliance_md() -> None:
    text = COMPLIANCE_MD.read_text(encoding="utf-8")
    text = replace_once_or_more(
        text,
        "- 进入 Codex A 验证 + Lane B 原型审计 + Governor / Confucius review-only gate + 新一轮 GPT commander packet。",
        "- Lane B Phase08 原型审计已完成并报 WARN;本补丁已清理正文中的文件编号式表述、阶段字段名式表述,并补入两个选择题答案字母。下一步进入 Codex A 复验 + Governor / Confucius review-only gate + 新一轮 GPT commander packet。",
        "compliance-next-step",
    )
    COMPLIANCE_MD.write_text(text, encoding="utf-8")


def main() -> None:
    patch_md()
    patch_proto_csv()
    patch_change_log_csv()
    patch_compliance_md()
    print("PHASE08_LANEB_CLEANLINESS_PATCH_APPLIED")


if __name__ == "__main__":
    main()
