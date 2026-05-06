#!/usr/bin/env python3
"""Finalize Phase12 362-row rescan and add source-confirmed new rows.

This script is intentionally conservative. It does not infer answers. It only
promotes rows with a recovered paper source plus a reliable answer/visible
evidence note, and leaves the rest as review-only blocked/excluded rows.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")

MATRIX_362 = BASE / "05_coverage/phase12_362_control_base_rescan_matrix.csv"
SUMMARY_362 = BASE / "05_coverage/phase12_362_control_base_rescan_summary.md"
QUEUE_362 = BASE / "05_coverage/phase12_362_new_candidate_repair_queue.csv"
NEW_ENTRIES = BASE / "09_student_draft/phase12_362_new_entries_REVIEW_ONLY.md"

BODY_74 = BASE / "09_student_draft/phase12_expanded_body_FROM_74_REVIEW_ONLY.md"
CONTROL_74 = BASE / "09_student_draft/phase12_expanded_body_control_matrix.csv"
BODY_362 = BASE / "09_student_draft/phase12_expanded_body_FROM_362_REVIEW_ONLY.md"
CONTROL_362 = BASE / "09_student_draft/phase12_expanded_body_FROM_362_control_matrix.csv"
GAP_362 = BASE / "09_student_draft/phase12_expanded_body_FROM_362_gap_backcheck.csv"


DISTRICT_ORDER = {"海淀": 1, "西城": 2, "东城": 3, "朝阳": 4, "丰台": 5}
YEAR_ORDER = {"2026": 1, "2025": 2, "2024": 3}
STAGE_ORDER = {"一模": 1, "二模": 2, "期中": 3, "期末": 4}


PROMOTE_NEW = {
    "Q-2024朝阳一模-6": {
        "visible_title": "2024 朝阳一模第6题",
        "module": "推理",
        "district": "朝阳",
        "year": "2024",
        "exam_stage": "一模",
        "question_no": "6",
        "subquestion_no": "0",
        "answer": "B",
        "source_note": "paper:030 lines 71-75; commentary:032 lines 106-111 gives B and option diagnoses",
        "reason": "逻辑规则选择题，讲评材料给出答案和 A/B/C/D 逻辑诊断，可转 review-only 正文。",
    },
    "Q-2025西城二模-6": {
        "visible_title": "2025 西城二模第6题",
        "module": "推理",
        "district": "西城",
        "year": "2025",
        "exam_stage": "二模",
        "question_no": "6",
        "subquestion_no": "0",
        "answer": "C",
        "source_note": "paper:037 lines 61-64; answer key:037 line 306 / 038 line 5 gives 6.C",
        "reason": "概念外延关系选择题，题干选项与答案表均已回源确认。",
    },
    "Q-2026通州期末-10": {
        "visible_title": "2026 通州期末第10题",
        "module": "推理",
        "district": "其他区",
        "year": "2026",
        "exam_stage": "期末",
        "question_no": "10",
        "subquestion_no": "0",
        "answer": "B",
        "source_note": "paper text:006 lines 138-143; render page_04 shows four statements; answer table:006 lines 307-329 gives Q10=B",
        "reason": "法学逻辑思维选择题，完整四项经页面渲染确认，答案表确认 B。",
    },
}

ANSWER_MISSING_NEW = {
    "Q-2024朝阳期中-10": "题干显然涉及概念外延/关系判断，但本轮只找到试卷题面，未找到可靠选择题答案表；不得逻辑猜答案。",
}

MANUAL_OUT = {
    "Q-2024西城一模-19-1": "同题第(1)问只要求分析未来产业发展状况；第(5)问才是可入选必三逻辑与思维的设问，已在 74 行内。",
    "Q-2026东城期末-17-1": "同题第(1)问明确运用《经济与社会》提出政策建议；第(2)问逻辑论证已在 74 行内。",
    "Q-2026顺义一模-19-3": "同题第(3)问为产业经济/治理建议；第(1)(2)问的推理与科学思维已在 74 行内。",
}

NEW_ENTRY_TEXT = {
    "Q-2024朝阳一模-6": """### 2024 朝阳一模第6题

【题干信号】题目直接说“思维必须合乎逻辑”，四个选项分别考概念划分、排中律、矛盾律和四概念。

【正确项】B。“不赞成所有人都有崇高的理想”与“不赞成所有人都没有崇高的理想”可以同时成立，它等于承认有的人有、有的人没有，没有违反排中律。

【错项陷阱】A把物权、债权、知识产权和著作权、商标权并列，属于越级划分。C一边说所有科技人员都懂计算机，一边说有些不懂计算机的是科技人员，违反矛盾律。D把“老舍的作品”整体和《茶馆》这一个作品混用，容易犯四概念错误。

【同类题】逻辑三律、概念划分、排中律、矛盾律、四概念。
""",
    "Q-2025西城二模-6": """### 2025 西城二模第6题

【题干信号】“洛阳红”是“牡丹”的一个具体品种，核心是判断两个概念的外延包含关系。

【正确项】C。“谷雨”是“节气”的一个具体种类，和“洛阳红”是“牡丹”的一个品种一样，都是种概念与属概念的关系。

【错项陷阱】A红墙黄瓦只是故宫的建筑特征，不是故宫的一个种类。B景山公园是北京市内的一个地点，偏向空间隶属，不是概念种属。D《红楼梦》是“四大名著”之一，更接近个体与集合成员关系，不如 C 的种属关系稳定。

【同类题】概念外延关系、种属关系、属种关系。
""",
    "Q-2026通州期末-10": """### 2026 通州期末第10题

【题干信号】题目明确把“逻辑思维”放到法学研究和实践中，四个小判断分别考反对关系、逻辑错误、关系判断和选言判断。

【正确项】B。①“抵押权”和“质权”都是担保物权下的不同类型，外延上属于反对关系。③“两公司存在长期货物买卖合作关系”断定的是两个主体之间的关系，属于关系判断。

【错项陷阱】②把知识产权权利列举理解成“定义过宽”，问题不在定义，而在权利范围与列举方式。④“要么放弃继承，要么接受继承”并不构成相容选言判断，表达更接近不相容选择，不能写成相容选言。

【同类题】概念外延关系、反对关系、关系判断、选言判断。
""",
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def classify(row: dict[str, str]) -> tuple[str, str, str]:
    qid = row["canonical_question_id"]
    initial = row.get("phase12_rescan_category", "")
    blocker = row.get("blocker_reason", "")
    answer = row.get("answer_pairing_status", "")
    rubric = row.get("rubric_pairing_status", "")
    visual = row.get("visual_status", "")
    section = row.get("section_scope", "")
    qtype = row.get("question_type", "")

    if qid in PROMOTE_NEW:
        return "new_body_candidate", "body_after_362_repair", PROMOTE_NEW[qid]["reason"]
    if qid in ANSWER_MISSING_NEW:
        return "answer_missing", "blocked_keep_out", ANSWER_MISSING_NEW[qid]
    if qid in MANUAL_OUT:
        return "out_of_scope", "excluded_keep_out", MANUAL_OUT[qid]
    if initial == "already_in_74":
        return "already_in_74", "covered_by_74_review_body", "已进入 74-row review-only expanded body。"
    if "scope_out" in blocker or "其他模块" in rubric or section == "边界":
        return "out_of_scope", "excluded_keep_out", blocker or "边界模块，不进入选必三正文。"
    if "queue_split_error_cleaned" in blocker:
        return "duplicate", "excluded_keep_out", "队列拆分错误或重复行，保留审计不进正文。"
    if qtype == "suite_visual_blocker" or "paper PDF text layer is blank" in blocker:
        return "visual_missing", "blocked_keep_out", "整套或局部视觉恢复不足，不能转正文。"
    if "choice options not fully detected" in blocker:
        return "visual_missing", "blocked_keep_out", "选择题选项未完整恢复，不能转正文。"
    if answer == "missing_or_unpaired":
        return "answer_missing", "blocked_keep_out", "答案源缺失或未配对。"
    if initial == "answer_missing":
        return "answer_missing", "blocked_keep_out", "初筛为答案/来源缺口，本轮未找到足够证据。"
    if visual == "not_visual_confirmed" and initial != "out_of_scope":
        return "blocked", "blocked_keep_out", "范围或题面仍需人工回源，不从材料关键词推断入正文。"
    if initial == "out_of_scope":
        return "out_of_scope", "excluded_keep_out", blocker or "初筛已判边界外。"
    return "blocked", "blocked_keep_out", "未满足 362 回扫正文准入证据。"


def sort_key(row: dict[str, str]) -> str:
    group = 1 if row.get("question_type_group") == "主观题" else 2
    district = DISTRICT_ORDER.get(row.get("district", ""), 6)
    year = YEAR_ORDER.get(row.get("year", ""), 9)
    stage = STAGE_ORDER.get(row.get("exam_stage", ""), 9)
    qno = int(row.get("question_no") or 0)
    subq = int(row.get("subquestion_no") or 0)
    return f"{group:02d}-{district:02d}-{year:02d}-{stage:02d}-{qno:03d}-{subq:02d}"


def parse_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^###\s+(.+?)\s*$", text, re.M))
    sections: dict[str, str] = {}
    for idx, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        sections[title] = body
    return sections


def write_new_entries() -> None:
    parts = [
        "# Phase12 362-Rescan New Entries",
        "",
        "Status: `REVIEW_ONLY_NO_WORD_NO_FINAL`",
        "",
        "本文件只收纳 362-row 回扫中新发现且已回源确认的新增正文候选。它不是终稿，不得直接进 Word。",
        "",
        "## 选择题",
        "",
    ]
    for qid in ["Q-2024朝阳一模-6", "Q-2025西城二模-6", "Q-2026通州期末-10"]:
        parts.append(NEW_ENTRY_TEXT[qid].rstrip())
        parts.append("")
    NEW_ENTRIES.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")


def build_extended_body() -> None:
    old_rows = read_csv(CONTROL_74)
    old_sections = parse_sections(BODY_74.read_text(encoding="utf-8"))
    new_sections = parse_sections(NEW_ENTRIES.read_text(encoding="utf-8"))

    rows: list[dict[str, str]] = []
    for row in old_rows:
        qno = re.search(r"第(\d+)题", row["visible_title"])
        subq = re.search(r"第\((\d+)\)问|第（(\d+)）问", row["visible_title"])
        row = dict(row)
        row.setdefault("question_no", qno.group(1) if qno else "")
        row.setdefault("subquestion_no", next((g for g in (subq.groups() if subq else []) if g), "0"))
        row["phase12_362_status"] = "carried_from_74"
        row["sort_key"] = row.get("sort_key") or sort_key(row)
        rows.append(row)

    for qid, meta in PROMOTE_NEW.items():
        rows.append(
            {
                "order": "",
                "question_id": qid,
                "visible_title": meta["visible_title"],
                "question_type_group": "选择题",
                "module": meta["module"],
                "district": meta["district"],
                "year": meta["year"],
                "exam_stage": meta["exam_stage"],
                "question_no": meta["question_no"],
                "subquestion_no": meta["subquestion_no"],
                "sort_key": sort_key(
                    {
                        "question_type_group": "选择题",
                        "district": meta["district"],
                        "year": meta["year"],
                        "exam_stage": meta["exam_stage"],
                        "question_no": meta["question_no"],
                        "subquestion_no": meta["subquestion_no"],
                    }
                ),
                "phase12_decision": "body_after_362_repair",
                "current_body_status": "new_from_362_rescan",
                "body_found": "yes",
                "source_pool": "phase12_362_rescan_repair",
                "source_file": NEW_ENTRIES.name,
                "note": "new_body_candidate_after_362_rescan; review_only",
                "phase12_362_status": "new_body_candidate",
            }
        )

    rows = sorted(rows, key=lambda r: r["sort_key"])
    parts = [
        "# Phase12 Expanded Body From 362 Rescan",
        "",
        "Status: `REVIEW_ONLY_NO_WORD_NO_FINAL`",
        "",
        "本稿在 74-row review-only 扩展正文基础上，加入 362-row 回扫中已回源确认的新增候选。它只用于继续双索引、外部模型复核和 Governor/Confucius 验收，不得命名为终稿、最终稿或宝典成品。",
        "",
        f"- 条目总数：{len(rows)}",
        "- 主观题在前，选择题在后",
        "- 每类内部按海淀、西城、东城、朝阳、丰台、其他区；同一区内部按 2026、2025、2024 排序",
        "",
    ]
    current_group = ""
    out_rows = []
    gap_rows = []
    for idx, row in enumerate(rows, start=1):
        group = row["question_type_group"]
        if group != current_group:
            parts.append(f"## {group}")
            parts.append("")
            current_group = group
        title = row["visible_title"]
        body = new_sections.get(title) or old_sections.get(title)
        found = "yes" if body else "no"
        parts.append(f"### {title}")
        parts.append("")
        parts.append(f"<!-- question_id: {row['question_id']}; phase12_decision: {row.get('phase12_decision','')}; source_pool: {row.get('source_pool','')} -->")
        parts.append("")
        parts.append(body or "【待修复】本条缺正文块，不得合并进 Word。")
        parts.append("")

        out_row = dict(row)
        out_row["order"] = str(idx)
        out_row["body_found"] = found
        out_rows.append(out_row)
        gap_rows.append(
            {
                "question_id": row["question_id"],
                "visible_title": title,
                "body_found": found,
                "coverage_bucket": "body" if found == "yes" else "missing",
                "repair_or_blocker": row.get("note", ""),
            }
        )

    BODY_362.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    control_fields = [
        "order",
        "question_id",
        "visible_title",
        "question_type_group",
        "module",
        "district",
        "year",
        "exam_stage",
        "question_no",
        "subquestion_no",
        "sort_key",
        "phase12_decision",
        "current_body_status",
        "body_found",
        "source_pool",
        "source_file",
        "note",
        "phase12_362_status",
    ]
    write_csv(CONTROL_362, out_rows, control_fields)
    write_csv(GAP_362, gap_rows, ["question_id", "visible_title", "body_found", "coverage_bucket", "repair_or_blocker"])


def main() -> None:
    rows = read_csv(MATRIX_362)
    fieldnames = list(rows[0].keys())
    if "phase12_initial_rescan_category" not in fieldnames:
        fieldnames.append("phase12_initial_rescan_category")
    for extra in ["phase12_final_action", "phase12_rescan_note"]:
        if extra not in fieldnames:
            fieldnames.append(extra)

    queue_rows: list[dict[str, str]] = []
    for row in rows:
        initial = row.get("phase12_initial_rescan_category") or row.get("phase12_rescan_category", "")
        row["phase12_initial_rescan_category"] = initial
        final, action, note = classify(row)
        row["phase12_rescan_category"] = final
        row["phase12_final_action"] = action
        row["phase12_rescan_note"] = note
        qid = row["canonical_question_id"]
        if qid in PROMOTE_NEW or qid in ANSWER_MISSING_NEW:
            meta = PROMOTE_NEW.get(qid, {})
            queue_rows.append(
                {
                    "question_id": qid,
                    "visible_title": meta.get("visible_title", row.get("canonical_question_id", "")),
                    "module": meta.get("module", row.get("section_scope", "")),
                    "question_type": row.get("question_type", ""),
                    "rescan_decision": final,
                    "final_action": action,
                    "answer_status": "confirmed" if qid in PROMOTE_NEW else "missing",
                    "source_note": meta.get("source_note", ""),
                    "reason": note,
                }
            )

    write_csv(MATRIX_362, rows, fieldnames)
    write_csv(
        QUEUE_362,
        queue_rows,
        ["question_id", "visible_title", "module", "question_type", "rescan_decision", "final_action", "answer_status", "source_note", "reason"],
    )
    write_new_entries()
    build_extended_body()

    counts = Counter(row["phase12_rescan_category"] for row in rows)
    actions = Counter(row["phase12_final_action"] for row in rows)
    body_rows = read_csv(CONTROL_362)
    body_counts = Counter(row["question_type_group"] for row in body_rows)

    summary = [
        "# Phase12 362 Control Base Rescan Summary",
        "",
        "Status: `REVIEW_ONLY_362_RESCAN_DONE_NO_WORD_NO_FINAL`",
        "",
        "本文件记录 362-row control base 回扫的最终分类。它不授权 Word/PDF/final，也不把当前扩展稿命名为终稿。",
        "",
        "## Counts",
        "",
        f"- total control-base rows: {len(rows)}",
        f"- already_in_74: {counts.get('already_in_74', 0)}",
        f"- new_body_candidate: {counts.get('new_body_candidate', 0)}",
        f"- answer_missing: {counts.get('answer_missing', 0)}",
        f"- visual_missing: {counts.get('visual_missing', 0)}",
        f"- out_of_scope: {counts.get('out_of_scope', 0)}",
        f"- duplicate: {counts.get('duplicate', 0)}",
        f"- blocked: {counts.get('blocked', 0)}",
        "",
        "## Body Impact",
        "",
        "- 74-row review-only body remains fully represented.",
        f"- new source-confirmed rows added from 362 rescan: {counts.get('new_body_candidate', 0)}",
        f"- expanded review-only body rows after 362 rescan: {len(body_rows)}",
        f"- 主观题: {body_counts.get('主观题', 0)}",
        f"- 选择题: {body_counts.get('选择题', 0)}",
        "- 当前目标 90-120 未强行凑数：本轮只把证据闭合的新增题进 review-only；答案缺口或视觉缺口继续 blocked。",
        "",
        "## New Body Candidates",
        "",
    ]
    for qid, meta in PROMOTE_NEW.items():
        summary.append(f"- `{qid}` | {meta['visible_title']} | answer={meta['answer']} | {meta['source_note']}")
    summary.extend(
        [
            "",
            "## New But Blocked",
            "",
        ]
    )
    for qid, note in ANSWER_MISSING_NEW.items():
        summary.append(f"- `{qid}` | answer_missing | {note}")
    summary.extend(
        [
            "",
            "## Action Counts",
            "",
        ]
    )
    for key, value in actions.most_common():
        summary.append(f"- {key}: {value}")
    summary.extend(
        [
            "",
            "## Output Files",
            "",
            f"- `{MATRIX_362.relative_to(BASE)}`",
            f"- `{QUEUE_362.relative_to(BASE)}`",
            f"- `{NEW_ENTRIES.relative_to(BASE)}`",
            f"- `{BODY_362.relative_to(BASE)}`",
            f"- `{CONTROL_362.relative_to(BASE)}`",
            f"- `{GAP_362.relative_to(BASE)}`",
            "",
            "## Remaining Gate",
            "",
            "- 双索引尚未生成。",
            "- Codex/ClaudeCode/GPT/Governor/Confucius 验收尚未完成。",
            "- Word/PDF/final 仍禁止。",
        ]
    )
    SUMMARY_362.write_text("\n".join(summary).rstrip() + "\n", encoding="utf-8")

    print(f"updated: {MATRIX_362}")
    print(f"written: {SUMMARY_362}")
    print(f"written: {BODY_362}")
    print(f"control_base_rows: {len(rows)}")
    print(f"expanded_body_rows: {len(body_rows)}")
    print("categories:", dict(counts))


if __name__ == "__main__":
    main()
