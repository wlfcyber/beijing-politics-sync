#!/usr/bin/env python3
"""Build Phase12 expansion control files from existing ledgers.

This is a mechanical ledger transformer. It does not promote any entry into
final student body; it only applies the GPT Phase12 gate labels.
"""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

GAP = ROOT / "09_student_draft/phase10_5_pre_gpt_expansion_gap_inventory.csv"
REPAIR = ROOT / "09_student_draft/phase10_5_source_repair_priority_queue.csv"
INDEX29 = ROOT / "09_student_draft/phase11D_combined_source_verified_29_index.csv"
CONTROL362 = ROOT / "05_coverage/phase04_control_base_status_after_batch03_cleaned.csv"

MUST_FIX_QID = "Q-2024海淀二模-17-1"

STAGE_ORDER = ["一模", "二模", "期中", "期末", "三模"]
DISTRICT_ORDER = ["海淀", "西城", "东城", "朝阳", "丰台"]
YEAR_ORDER = {"2026": 1, "2025": 2, "2024": 3}
XUANBISAN_HINTS = [
    "逻辑",
    "推理",
    "判断",
    "概念",
    "三段论",
    "联言",
    "选言",
    "假言",
    "归纳",
    "类比",
    "科学思维",
    "辩证思维",
    "创新思维",
    "思维抽象",
    "思维具体",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], headers: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=headers, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def md_escape(s: str) -> str:
    return (s or "").replace("\n", " ").strip()


def parse_suite(suite_id: str, visible_title: str = "") -> tuple[str, str, str]:
    text = suite_id.replace("S-", "") or visible_title
    m = re.search(r"(20\d{2})(.+)", text)
    year = m.group(1) if m else ""
    rest = m.group(2) if m else text
    stage = "其他"
    district = rest
    for st in STAGE_ORDER:
        if rest.endswith(st):
            stage = st
            district = rest[: -len(st)]
            break
    district = district.strip() or "其他区"
    if district not in DISTRICT_ORDER:
        district = district or "其他区"
    return year, district, stage


def parse_qno(title: str, qid: str = "") -> tuple[str, str]:
    text = title or qid
    q = ""
    sub = ""
    m = re.search(r"第(\d+)题", text)
    if not m:
        m = re.search(r"-(\d+)(?:-\d+)?$", qid)
    if m:
        q = m.group(1)
    m2 = re.search(r"第[（(]?(\d+)[）)]?问", text)
    if not m2:
        m2 = re.search(r"-(\d+)-(\d+)$", qid)
        if m2:
            q = q or m2.group(1)
            sub = m2.group(2)
    else:
        sub = m2.group(1)
    return q, sub


def current_body_status(phase10_status: str) -> str:
    if phase10_status == "in_phase10_body":
        return "body"
    if phase10_status == "same_type_index_only":
        return "index_only"
    if phase10_status == "not_represented_in_body_or_same_type_index":
        return "not_represented"
    return phase10_status or "unknown"


def source_status(value: str) -> str:
    v = (value or "").lower()
    if not v or v == "none":
        return "missing"
    return "present"


def answer_status(row: dict[str, str]) -> str:
    v = (row.get("answer_locator") or "").lower()
    perm = row.get("phase07_input_permission", "")
    if "hold_answer_locator_risk" in perm:
        return "needs_source_upgrade"
    if "answer_confirmed" in v or "locked" in v:
        return "confirmed"
    if not v:
        return "missing"
    return "present_unverified"


def rubric_status(row: dict[str, str]) -> str:
    v = (row.get("rubric_or_commentary_locator") or "").lower()
    if "formal" in v or "rubric_confirmed" in v or "locked" in v:
        return "confirmed_formal_or_rubric"
    if "paired_candidate" in v or "no_formal" in v:
        return "support_or_paired_candidate_needs_upgrade"
    if "missing_reasoning" in v:
        return "missing_reasoning_form"
    if not v:
        return "missing"
    return "present"


def reasoning_status(row: dict[str, str]) -> str:
    if row["question_id"] == MUST_FIX_QID:
        return "MUST_FIX_SOURCE_OR_SCOPE"
    perm = row.get("phase07_input_permission", "")
    if "hold_reasoning_form_risk" in perm:
        return "needs_reasoning_form_recheck"
    if row.get("module") in {"推理", "交叉"} and row.get("phase10_body_status") != "in_phase10_body":
        return "needs_typology_assignment"
    return "present_or_not_required"


def thinking_status(row: dict[str, str]) -> str:
    if row["question_id"] == MUST_FIX_QID:
        return "must_fix_seed_scope_before_body"
    st = row.get("phase10_body_status", "")
    if st == "in_phase10_body":
        return "existing_body_review_only"
    if st == "same_type_index_only":
        return "index_only_needs_body_decision"
    return "not_represented_needs_decision"


def decision(row: dict[str, str], priority_by_qid: dict[str, str]) -> tuple[str, str]:
    qid = row["question_id"]
    st = row.get("phase10_body_status", "")
    perm = row.get("phase07_input_permission", "")
    priority = priority_by_qid.get(qid, "")
    if qid == MUST_FIX_QID:
        return "body_after_repair", "GPT Phase12 seed gate: MUST_FIX_SOURCE_OR_SCOPE; original asks science-only, source/rubric calibration required before正文"
    if st == "in_phase10_body":
        return "body_now", "Already in 29-row controlled body, still REVIEW_ONLY and not final"
    if "hold_answer_locator_risk" in perm:
        return "body_after_repair", f"Answer/source locator upgrade required before body expansion; priority={priority or 'unranked'}"
    if "hold_reasoning_form_risk" in perm:
        return "body_after_repair", f"Reasoning form recheck required before body expansion; priority={priority or 'unranked'}"
    if st == "same_type_index_only":
        return "index_only", "Index-only currently; Phase12 must decide whether new material signal justifies正文"
    return "blocked", "No Phase12 promotion rule matched; keep out until manual source decision"


def build() -> None:
    gap_rows = read_csv(GAP)
    repair_rows = read_csv(REPAIR)
    priority_by_qid = {r["question_id"]: r["priority"] for r in repair_rows}

    matrix: list[dict[str, str]] = []
    for r in gap_rows:
        year, district, stage = parse_suite(r.get("suite_id", ""), r.get("visible_title", ""))
        qno, subq = parse_qno(r.get("visible_title", ""), r.get("question_id", ""))
        dec, reason = decision(r, priority_by_qid)
        matrix.append(
            {
                "question_id": r["question_id"],
                "visible_title": r["visible_title"],
                "district": district,
                "year": year,
                "exam_stage": stage,
                "question_no": qno,
                "subquestion_no": subq,
                "module": r["module"],
                "question_type": r["question_type"],
                "current_body_status": current_body_status(r["phase10_body_status"]),
                "permission_status": r["phase07_input_permission"],
                "source_locator_status": source_status(r["source_locator"]),
                "answer_locator_status": answer_status(r),
                "rubric_locator_status": rubric_status(r),
                "reasoning_form_status": reasoning_status(r),
                "thinking_chain_status": thinking_status(r),
                "decision": dec,
                "decision_reason": reason,
            }
        )

    matrix_headers = [
        "question_id",
        "visible_title",
        "district",
        "year",
        "exam_stage",
        "question_no",
        "subquestion_no",
        "module",
        "question_type",
        "current_body_status",
        "permission_status",
        "source_locator_status",
        "answer_locator_status",
        "rubric_locator_status",
        "reasoning_form_status",
        "thinking_chain_status",
        "decision",
        "decision_reason",
    ]
    write_csv(ROOT / "05_coverage/phase12_74row_expansion_decision_matrix.csv", matrix, matrix_headers)

    counts = {
        "total": len(matrix),
        "decision": Counter(r["decision"] for r in matrix),
        "current_body_status": Counter(r["current_body_status"] for r in matrix),
        "question_type": Counter(r["question_type"] for r in matrix),
        "module": Counter(r["module"] for r in matrix),
        "answer_locator_status": Counter(r["answer_locator_status"] for r in matrix),
        "reasoning_form_status": Counter(r["reasoning_form_status"] for r in matrix),
    }
    summary = [
        "# Phase12 74-Row Expansion Decision Summary",
        "",
        "Status: `REVIEW_ONLY_NO_WORD_NO_FINAL`",
        "",
        "GPT Phase12 verdict adopted: `EXPAND_TO_74_FIRST_THEN_RESCAN`.",
        "",
        f"- total rows: {counts['total']}",
        "",
        "## Current Body Status",
    ]
    for k, v in counts["current_body_status"].most_common():
        summary.append(f"- `{k}`: {v}")
    summary.append("\n## Decision Counts")
    for k, v in counts["decision"].most_common():
        summary.append(f"- `{k}`: {v}")
    summary.append("\n## Question Type Counts")
    for k, v in counts["question_type"].most_common():
        summary.append(f"- `{k}`: {v}")
    summary.append("\n## Module Counts")
    for k, v in counts["module"].most_common():
        summary.append(f"- `{k}`: {v}")
    summary.append("\n## Gate Notes")
    summary.extend(
        [
            "- 29-row candidate remains `CANDIDATE_PACKET_ONLY`.",
            "- `Q-2024海淀二模-17-1` is forced into `MUST_FIX_SOURCE_OR_SCOPE` before正文.",
            "- Non-body rows are not promoted by this file; they require source repair or reasoning-form recheck.",
            "- No Word, PDF, final PASS, 终稿, or 宝典成品 is allowed at this phase.",
        ]
    )
    (ROOT / "05_coverage/phase12_74row_expansion_decision_summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")

    # Freeze current 29-row candidate.
    idx_rows = read_csv(INDEX29)
    freeze_rows = [
        {
            "order": r.get("order", ""),
            "title": r.get("title", ""),
            "source_file": r.get("source_file", ""),
            "not_final": "yes",
            "word_pdf_permission": "no",
            "final_pass_permission": "no",
            "reason": "evidence_pool_74_and_control_base_362_not_fully_processed",
        }
        for r in idx_rows
    ]
    freeze_headers = ["order", "title", "source_file", "not_final", "word_pdf_permission", "final_pass_permission", "reason"]
    write_csv(ROOT / "09_student_draft/phase12_29row_candidate_not_final_freeze.csv", freeze_rows, freeze_headers)
    (ROOT / "09_student_draft/phase12_29row_candidate_not_final_freeze.md").write_text(
        "\n".join(
            [
                "# Phase12 29-Row Candidate Not-Final Freeze",
                "",
                "Status: `CANDIDATE_PACKET_ONLY_NO_WORD_NO_FINAL`",
                "",
                f"- body_rows: {len(idx_rows)}",
                "- not_final: yes",
                "- word_pdf_permission: no",
                "- final_pass_permission: no",
                "- reason: evidence_pool_74_and_control_base_362_not_fully_processed",
                "",
                "The 29-row candidate can only serve as a review-only content packet. It cannot be renamed or described as final/终稿/宝典成品.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    # 45-row queues and split logs.
    repair_headers = [
        "priority",
        "question_id",
        "visible_title",
        "module",
        "question_type",
        "phase10_body_status",
        "phase07_input_permission",
        "ref_count",
        "repair_reason",
        "source_locator",
        "answer_locator",
        "hold_reason",
        "risk_note",
        "phase12_next_action",
    ]
    repair_out = []
    decision_by_qid = {r["question_id"]: r["decision"] for r in matrix}
    for r in repair_rows:
        rr = dict(r)
        rr["phase12_next_action"] = decision_by_qid.get(r["question_id"], "blocked")
        repair_out.append(rr)
    write_csv(ROOT / "05_coverage/phase12_45_nonbody_repair_queue.csv", repair_out, repair_headers)

    answer_rows = [r for r in gap_rows if "hold_answer_locator_risk" in r.get("phase07_input_permission", "")]
    ans_headers = [
        "question_id",
        "visible_title",
        "question_type",
        "module",
        "phase10_body_status",
        "source_locator",
        "answer_locator",
        "rubric_or_commentary_locator",
        "repair_required",
        "repair_rule",
    ]
    ans_out = [
        {
            **{h: r.get(h, "") for h in ans_headers if h in r},
            "repair_required": "yes",
            "repair_rule": "return_to_source_answer_key_or_rubric; no logical guessing; blocked if answer source cannot be confirmed",
        }
        for r in answer_rows
    ]
    write_csv(ROOT / "05_coverage/phase12_answer_locator_repair_matrix.csv", ans_out, ans_headers)

    reasoning_rows = [r for r in gap_rows if "hold_reasoning_form_risk" in r.get("phase07_input_permission", "")]
    reason_headers = [
        "question_id",
        "visible_title",
        "question_type",
        "module",
        "phase10_body_status",
        "source_locator",
        "answer_locator",
        "rubric_or_commentary_locator",
        "logical_form_status",
        "repair_rule",
    ]
    reason_out = [
        {
            **{h: r.get(h, "") for h in reason_headers if h in r},
            "logical_form_status": "missing_pending_recheck",
            "repair_rule": "extract proposition form; classify reasoning type; mark valid/invalid form; add rule口诀 and trap before body",
        }
        for r in reasoning_rows
    ]
    write_csv(ROOT / "05_coverage/phase12_reasoning_form_repair_matrix.csv", reason_out, reason_headers)

    def split_log(status_value: str, path: Path) -> None:
        rows = [r for r in gap_rows if r.get("phase10_body_status") == status_value]
        out = []
        for r in rows:
            out.append(
                {
                    "question_id": r["question_id"],
                    "visible_title": r["visible_title"],
                    "module": r["module"],
                    "question_type": r["question_type"],
                    "why_not_body_before": r.get("hold_reason", "") or r.get("recommended_next_action", ""),
                    "phase12_decision": decision_by_qid.get(r["question_id"], ""),
                    "specific_blocker_or_repair": r.get("recommended_next_action", ""),
                    "needs_source_repair": "yes" if "answer_locator" in r.get("recommended_next_action", "") or "source_repair" in r.get("recommended_next_action", "") or "hold_answer_locator" in r.get("phase07_input_permission", "") else "no",
                    "needs_reasoning_form_repair": "yes" if "reasoning_form" in r.get("recommended_next_action", "") or "hold_reasoning_form" in r.get("phase07_input_permission", "") else "no",
                    "enter_index": "yes" if status_value == "same_type_index_only" else "to_decide",
                }
            )
        headers = [
            "question_id",
            "visible_title",
            "module",
            "question_type",
            "why_not_body_before",
            "phase12_decision",
            "specific_blocker_or_repair",
            "needs_source_repair",
            "needs_reasoning_form_repair",
            "enter_index",
        ]
        write_csv(path, out, headers)

    split_log("not_represented_in_body_or_same_type_index", ROOT / "05_coverage/phase12_not_represented_29_decision_log.csv")
    split_log("same_type_index_only", ROOT / "05_coverage/phase12_index_only_16_decision_log.csv")

    # Initial 362-row rescan scaffold.
    gap_qids = {r["question_id"] for r in gap_rows}
    control = read_csv(CONTROL362)
    control_out = []
    for r in control:
        qid = r.get("canonical_question_id", "")
        node_text = " ".join(
            [
                r.get("knowledge_node", ""),
                r.get("reasoning_node", ""),
                r.get("excerpt", "")[:240],
            ]
        )
        has_xuanbisan_hint = any(h in node_text for h in XUANBISAN_HINTS)
        blocker_text = (r.get("blocker_reason", "") + " " + r.get("fusion_status", "")).lower()
        if qid in gap_qids:
            cat = "already_in_74"
        elif "duplicate" in blocker_text:
            cat = "duplicate"
        elif "support" in blocker_text or r.get("section_scope") == "支撑材料":
            cat = "support_reference"
        elif r.get("scope_status") in {"out_of_scope", "boundary"} or r.get("section_scope") == "边界":
            cat = "out_of_scope"
        elif has_xuanbisan_hint:
            cat = "new_candidate"
        elif r.get("visual_status") == "not_visual_confirmed" and r.get("phase04_level") != "L0_BLOCKED":
            cat = "visual_missing"
        elif "reasoning" in blocker_text or "推理" in r.get("reasoning_node", ""):
            cat = "reasoning_form_missing"
        elif "answer" in blocker_text or r.get("answer_pairing_status") not in {"answer_confirmed", "confirmed", "answer_LOCKED_FOR_FUSION"}:
            cat = "answer_missing"
        elif r.get("phase04_level") == "L0_BLOCKED":
            cat = "blocked"
        else:
            cat = "blocked"
        control_out.append(
            {
                "canonical_question_id": qid,
                "suite_id": r.get("suite_id", ""),
                "original_qno": r.get("original_qno", ""),
                "question_type": r.get("question_type", ""),
                "section_scope": r.get("section_scope", ""),
                "knowledge_node": r.get("knowledge_node", ""),
                "reasoning_node": r.get("reasoning_node", ""),
                "phase04_level": r.get("phase04_level", ""),
                "answer_pairing_status": r.get("answer_pairing_status", ""),
                "rubric_pairing_status": r.get("rubric_pairing_status", ""),
                "visual_status": r.get("visual_status", ""),
                "phase12_rescan_category": cat,
                "blocker_reason": r.get("blocker_reason", ""),
            }
        )
    control_headers = [
        "canonical_question_id",
        "suite_id",
        "original_qno",
        "question_type",
        "section_scope",
        "knowledge_node",
        "reasoning_node",
        "phase04_level",
        "answer_pairing_status",
        "rubric_pairing_status",
        "visual_status",
        "phase12_rescan_category",
        "blocker_reason",
    ]
    write_csv(ROOT / "05_coverage/phase12_362_control_base_rescan_matrix.csv", control_out, control_headers)
    c = Counter(r["phase12_rescan_category"] for r in control_out)
    lines = [
        "# Phase12 362 Control Base Rescan Summary",
        "",
        "Status: `INITIAL_RESCAN_SCAFFOLD_REVIEW_ONLY`",
        "",
        "This file is an initial categorization scaffold. It does not replace row-by-row source review.",
        "",
        f"- total control-base rows: {len(control_out)}",
    ]
    for k, v in c.most_common():
        lines.append(f"- `{k}`: {v}")
    lines.extend(
        [
            "",
            "Next: manually review `new_candidate`, `answer_missing`, `visual_missing`, and `blocked` rows with 选必三 terms before any Word gate.",
        ]
    )
    (ROOT / "05_coverage/phase12_362_control_base_rescan_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # Initial sort matrix for 74 rows.
    district_rank = {d: i + 1 for i, d in enumerate(DISTRICT_ORDER)}
    stage_rank = {s: i + 1 for i, s in enumerate(STAGE_ORDER)}
    sort_rows = []
    for r in matrix:
        qtype_rank = 1 if r["question_type"] == "主观题" else 2
        d_rank = district_rank.get(r["district"], 99)
        y_rank = YEAR_ORDER.get(r["year"], 99)
        st_rank = stage_rank.get(r["exam_stage"], 99)
        q_rank = int(r["question_no"]) if r["question_no"].isdigit() else 999
        sub_rank = int(r["subquestion_no"]) if r["subquestion_no"].isdigit() else 0
        sort_rows.append(
            {
                "question_id": r["question_id"],
                "visible_title": r["visible_title"],
                "question_type_group": r["question_type"],
                "district": r["district"],
                "year": r["year"],
                "exam_stage": r["exam_stage"],
                "question_no": r["question_no"],
                "subquestion_no": r["subquestion_no"],
                "sort_key": f"{qtype_rank:02d}-{d_rank:02d}-{y_rank:02d}-{st_rank:02d}-{q_rank:03d}-{sub_rank:02d}",
                "phase12_decision": r["decision"],
            }
        )
    sort_rows.sort(key=lambda x: x["sort_key"])
    sort_headers = [
        "question_id",
        "visible_title",
        "question_type_group",
        "district",
        "year",
        "exam_stage",
        "question_no",
        "subquestion_no",
        "sort_key",
        "phase12_decision",
    ]
    write_csv(ROOT / "09_student_draft/phase12_sort_key_matrix.csv", sort_rows, sort_headers)

    # Quantity gate in failing state until expansion is actually done.
    body_now = sum(1 for r in matrix if r["current_body_status"] == "body")
    nonbody = len(matrix) - body_now
    gate = [
        "# Phase12 Quantity And Coverage Gate",
        "",
        "Status: `FAIL_PENDING_EXPANSION`",
        "",
        f"- current body rows: {body_now}",
        f"- locked evidence rows: {len(matrix)}",
        f"- non-body rows to process: {nonbody}",
        f"- 45-row repair queue rows: {len(repair_rows)}",
        f"- 362 control-base rows in rescan scaffold: {len(control_out)}",
        "",
        "Hard gate:",
        "",
        "- 29 rows is not acceptable.",
        "- 74 evidence rows are not fully adjudicated into final body/index/blocked yet.",
        "- 45 non-body rows are not repaired yet.",
        "- 362 control base has only an initial scaffold; no Word is allowed.",
    ]
    (ROOT / "08_review/phase12_quantity_and_coverage_gate.md").write_text("\n".join(gate) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
