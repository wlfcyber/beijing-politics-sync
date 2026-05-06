#!/usr/bin/env python3
"""Build a non-promotional Phase10.5 inventory while the real GPT gate is blocked.

This does not authorize Phase11. It only compares the 74 locked evidence rows
against the 29 Phase10 body rows and records what would need repair before any
future expansion.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / "05_coverage" / "phase07_locked_opus_input_packet.csv"
CONTROL = ROOT / "09_student_draft" / "phase10_polish_control_matrix.csv"
OUT_DIR = ROOT / "09_student_draft"

OUT_CSV = OUT_DIR / "phase10_5_pre_gpt_expansion_gap_inventory.csv"
OUT_SUMMARY = OUT_DIR / "phase10_5_pre_gpt_expansion_gap_summary.md"
OUT_ADDENDUM = ROOT / "08_review" / "gpt_phase_advice" / "phase_10_retry_addendum_after_quota_block.md"
OUT_VERIFY = ROOT / "08_review" / "phase10_5_pre_gpt_inventory_verification.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def split_ids(value: str) -> list[str]:
    if not value:
        return []
    parts: list[str] = []
    for chunk in value.replace("，", "；").replace(",", "；").split("；"):
        qid = chunk.strip()
        if qid:
            parts.append(qid)
    return parts


def visible_title(qid: str) -> str:
    # Q-2026顺义一模-19-2 -> 2026 顺义一模第19题第(2)问
    raw = qid.removeprefix("Q-")
    bits = raw.split("-")
    if len(bits) < 2:
        return qid
    suite = bits[0]
    number = bits[1:]
    year = suite[:4]
    place = suite[4:]
    if len(number) == 1:
        return f"{year} {place}第{number[0]}题"
    return f"{year} {place}第{number[0]}题第({number[1]})问"


def action_for(row: dict[str, str], body_status: str) -> str:
    perm = row.get("input_permission", "")
    hold_reason = row.get("hold_reason", "")
    question_type = row.get("question_type", "")
    status = row.get("status", "")

    if body_status == "in_phase10_body":
        return "already_in_controlled_body_keep_locked"
    if "hold_answer_locator_risk" in perm or "no_formal_rubric" in hold_reason:
        return "source_repair_required_before_body_expansion"
    if "hold_reasoning_form_risk" in perm:
        return "reasoning_form_recheck_required_before_body_expansion"
    if status == "L0":
        return "excluded_do_not_expand_without_new_source"
    if question_type == "选择题" and body_status == "same_type_index_only":
        return "keep_as_index_until_answer_key_and_options_are_reverified"
    if body_status == "same_type_index_only":
        return "index_only_until_gpt_and_governor_authorize_expansion"
    return "unrepresented_hold_row_needs_local_source_repair"


def main() -> None:
    packet = read_csv(PACKET)
    control = read_csv(CONTROL)

    body_ids = {r["question_id"] for r in control}
    same_type_refs: dict[str, list[str]] = defaultdict(list)
    for r in control:
        source = r["question_id"]
        for qid in split_ids(r.get("same_type_ids", "")):
            same_type_refs[qid].append(source)

    rows: list[dict[str, str]] = []
    for row in packet:
        qid = row["question_id"]
        if qid in body_ids:
            body_status = "in_phase10_body"
        elif qid in same_type_refs:
            body_status = "same_type_index_only"
        else:
            body_status = "not_represented_in_body_or_same_type_index"

        rows.append(
            {
                "question_id": qid,
                "visible_title": visible_title(qid),
                "suite_id": row.get("suite_id", ""),
                "module": row.get("module", ""),
                "question_type": row.get("question_type", ""),
                "status": row.get("status", ""),
                "phase07_input_permission": row.get("input_permission", ""),
                "phase10_body_status": body_status,
                "referenced_by_phase10_body_ids": "；".join(sorted(same_type_refs.get(qid, []))),
                "hold_reason": row.get("hold_reason", ""),
                "recommended_next_action": action_for(row, body_status),
                "source_locator": row.get("source_locator", ""),
                "answer_locator": row.get("answer_locator", ""),
                "rubric_or_commentary_locator": row.get("rubric_or_commentary_locator", ""),
                "risk_note": row.get("risk_note", ""),
            }
        )

    fieldnames = list(rows[0].keys()) if rows else []
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

    body_counter = Counter(r["phase10_body_status"] for r in rows)
    action_counter = Counter(r["recommended_next_action"] for r in rows)
    module_counter = Counter((r["module"], r["phase10_body_status"]) for r in rows)
    permission_counter = Counter(r["phase07_input_permission"] for r in rows)

    hold_rows = [r for r in rows if r["phase10_body_status"] != "in_phase10_body"]

    summary_lines = [
        "# Phase10.5 Pre-GPT Expansion Gap Summary",
        "",
        "Status: `LOCAL_PREPARATION_ONLY_GPT_PHASE10_GATE_BLOCKED`",
        "",
        "This file does not authorize Phase11, student expansion, Word/PDF, final PASS, 终稿, 最终稿, or 宝典成品. It only prepares a local inventory because the real GPT-5.5 Pro web gate returned a quota message.",
        "",
        "## Counts",
        "",
        f"- locked evidence rows checked: {len(rows)}",
        f"- Phase10 body rows: {body_counter.get('in_phase10_body', 0)}",
        f"- same-type index only rows: {body_counter.get('same_type_index_only', 0)}",
        f"- not represented rows: {body_counter.get('not_represented_in_body_or_same_type_index', 0)}",
        "",
        "## Phase07 Permission Counts",
        "",
    ]
    for key, value in sorted(permission_counter.items()):
        summary_lines.append(f"- `{key}`: {value}")

    summary_lines.extend(["", "## Body Status By Module", ""])
    for (module, status), value in sorted(module_counter.items()):
        summary_lines.append(f"- `{module}` / `{status}`: {value}")

    summary_lines.extend(["", "## Recommended Next Actions", ""])
    for key, value in sorted(action_counter.items()):
        summary_lines.append(f"- `{key}`: {value}")

    summary_lines.extend(["", "## Non-Body Rows To Control Before Any Future Expansion", ""])
    for r in hold_rows:
        refs = r["referenced_by_phase10_body_ids"] or "none"
        summary_lines.append(
            f"- `{r['question_id']}` {r['visible_title']} | {r['module']} | {r['question_type']} | "
            f"{r['phase07_input_permission']} | `{r['phase10_body_status']}` | refs: {refs} | "
            f"next: `{r['recommended_next_action']}`"
        )

    OUT_SUMMARY.write_text("\n".join(summary_lines) + "\n", encoding="utf-8")

    addendum = f"""# Phase10 GPT Retry Addendum After Quota Block

Status: `REAL_GPT55_WEB_RETRY_REQUIRED`

The Phase10 packet was attempted in the visible ChatGPT Pro conversation on 2026-05-05 02:43 CST, but the web UI returned: `你已达到限额。请稍后重试。`

Local fallback performed without phase promotion:

- Compared the 74 Phase07 locked evidence rows against the 29 Phase10 polished body rows.
- Wrote `{OUT_CSV.relative_to(ROOT)}`.
- Wrote `{OUT_SUMMARY.relative_to(ROOT)}`.
- Result counts:
  - Phase10 body rows: {body_counter.get('in_phase10_body', 0)}
  - same-type index only rows: {body_counter.get('same_type_index_only', 0)}
  - not represented rows: {body_counter.get('not_represented_in_body_or_same_type_index', 0)}

Question for GPT retry:

Given the Phase10 polished outline and this local gap inventory, should the next authorized step be:

1. controlled expansion from the 45 held rows after source repair;
2. concrete content review of the current 29-row body before any expansion;
3. a mixed path: first repair specific high-value held rows, then expand by cluster;
4. stop and repair source evidence before further student-facing writing?

Reminder: GPT advice is not source evidence; Codex must locally verify any substantive recommendation before patching.
"""
    OUT_ADDENDUM.write_text(addendum, encoding="utf-8")

    verify = [
        "# Phase10.5 Pre-GPT Inventory Verification",
        "",
        "Verdict: `PASS_LOCAL_PREPARATION_ONLY_NO_PHASE_PROMOTION`",
        "",
        f"- phase07 rows read: {len(packet)}",
        f"- phase10 rows read: {len(control)}",
        f"- inventory rows written: {len(rows)}",
        f"- body ids all found in packet: {sorted(body_ids - {r['question_id'] for r in packet}) == []}",
        f"- non-body rows: {len(hold_rows)}",
        "- GPT Phase10 gate remains blocked until real web retry succeeds.",
        "- Word/PDF/final PASS remain blocked.",
    ]
    OUT_VERIFY.write_text("\n".join(verify) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
