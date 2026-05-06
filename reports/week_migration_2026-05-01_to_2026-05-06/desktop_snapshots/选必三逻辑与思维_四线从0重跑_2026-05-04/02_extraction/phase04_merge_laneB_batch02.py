#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "05_coverage/phase04_control_base_status_after_laneB_batch01.csv"
CODEX_ADDENDUM = ROOT / "05_coverage/phase04_batch02_codex_visual_scope_repair_addendum.csv"
LANEB_RAW = ROOT / "claudecode_lane/phase04_batch02_laneB_results.csv"
LANEB_NORMALIZED = ROOT / "claudecode_lane/phase04_batch02_laneB_results_normalized.csv"
LANEB = LANEB_NORMALIZED if LANEB_NORMALIZED.exists() else LANEB_RAW
OUT = ROOT / "05_coverage/phase04_control_base_status_after_batch02.csv"
RECON = ROOT / "06_conflicts/phase04_batch02_codexA_laneB_reconciliation.csv"
RECON_MD = ROOT / "06_conflicts/phase04_batch02_codexA_laneB_reconciliation.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def normalize_qno(qno: str) -> str:
    qno = qno.strip().replace("Q", "").replace("（", "(").replace("）", ")")
    qno = qno.replace("(2)", "-2").replace("(3)", "-3")
    return qno


def canonical_id(row: dict[str, str]) -> str:
    existing = row.get("canonical_question_id") or row.get("target_id")
    if existing:
        return existing.strip()
    suite = row.get("suite", "").strip()
    qno = normalize_qno(row.get("qno", ""))
    return f"Q-{suite}-{qno}"


def status_from_lane_b(b: dict[str, str]) -> tuple[str, str, str]:
    can = b.get("can_enter_fusion", "").strip().lower()
    result = b.get("laneB_result", "").strip()
    evidence = b.get("evidence_level", "").strip()
    if can == "yes":
        if evidence == "A-formal":
            return (
                "L4_LOCKED_FOR_FUSION",
                "locked_for_fusion_after_laneB_batch02",
                "NO_STUDENT_DRAFT_YET_GPT_BLOCKED",
            )
        return (
            "L3_A_PLUS_B_TARGET_CONFIRMED",
            "confirmed_for_evidence_fusion_pending_formal_lock_batch02",
            "NO_STUDENT_DRAFT_YET_GPT_BLOCKED",
        )
    if can.startswith("conditional") or result.endswith("SCOPE_DECISION"):
        return (
            "L2_PENDING_SCOPE_DECISION",
            "conditional_fusion_pending_scope_decision_batch02",
            "NO_STUDENT_DRAFT",
        )
    return ("L0_BLOCKED", "blocked_after_laneB_batch02", "NO_STUDENT_DRAFT")


def answer_letter(text: str) -> str:
    text = text or ""
    focused = re.search(r"answer_confirmed_([ABCD])", text)
    if focused:
        return focused.group(1)
    focused = re.search(r"答案[为是]?([ABCD])|answer[_ =:：-]*([ABCD])", text)
    if focused:
        return next(part for part in focused.groups() if part)
    return ""


def make_new_control_row(
    fieldnames: list[str],
    qid: str,
    b: dict[str, str],
    add: dict[str, str] | None,
) -> dict[str, str]:
    row = {name: "" for name in fieldnames}
    suite = (b.get("suite") or (add or {}).get("suite") or "").strip()
    qno = (b.get("qno") or (add or {}).get("qno") or "").strip()
    source_locator = (add or {}).get("source_locator", "")
    source_id = source_locator.split("::", 1)[0]
    level, fusion, student = status_from_lane_b(b)
    row.update(
        {
            "canonical_question_id": qid,
            "suite_id": f"S-{suite}" if suite and not suite.startswith("S-") else suite,
            "source_id": source_id,
            "stable_locator": source_locator or b.get("source_evidence", ""),
            "original_qno": qno,
            "question_type": (add or {}).get("question_type", "选择题"),
            "scope_status": "in_scope" if level != "L0_BLOCKED" else "pending",
            "section_scope": b.get("section_scope") or (add or {}).get("section_scope", ""),
            "knowledge_node": b.get("node") or (add or {}).get("reasoning_or_thinking_node", ""),
            "reasoning_node": b.get("logical_or_method_form") or (add or {}).get("logical_or_method_form", ""),
            "A_status": "codexA_batch02_addendum" if add else "not_in_codexA_batch02_addendum",
            "B_status": b.get("laneB_result", ""),
            "fusion_status": fusion,
            "phase04_level": level,
            "verification_level": b.get("evidence_level", ""),
            "answer_pairing_status": b.get("answer_status", ""),
            "rubric_pairing_status": b.get("rubric_status", ""),
            "visual_status": b.get("visual_status", ""),
            "student稿_permission": student,
            "blocker_reason": b.get("blocker_reason", ""),
            "gap_priority": "BATCH02",
            "gap_action": "new row added by visual/scope repair and Lane B verification",
            "excerpt": b.get("source_evidence", "") or (add or {}).get("notes", ""),
        }
    )
    return row


def main() -> None:
    missing = [path for path in [BASE, CODEX_ADDENDUM, LANEB] if not path.exists()]
    if missing:
        raise SystemExit("Missing required Batch02 input(s): " + ", ".join(str(p) for p in missing))

    base_rows = read_csv(BASE)
    addendum_rows = read_csv(CODEX_ADDENDUM)
    lane_b_rows = read_csv(LANEB)
    if not base_rows:
        raise SystemExit(f"Empty base control file: {BASE}")

    fieldnames = list(base_rows[0].keys())
    by_id = {row["canonical_question_id"]: row for row in base_rows}
    add_by_id = {canonical_id(row): row for row in addendum_rows}
    b_by_id = {canonical_id(row): row for row in lane_b_rows}

    recon_rows: list[dict[str, str]] = []

    for qid, b in b_by_id.items():
        add = add_by_id.get(qid)
        before = by_id.get(qid)
        if before is None:
            before = make_new_control_row(fieldnames, qid, b, add)
            by_id[qid] = before
            base_rows.append(before)
            before_level = "not_in_batch01_control_base"
        else:
            before_level = before.get("phase04_level", "")

        level, fusion, student = status_from_lane_b(b)
        before["B_status"] = b.get("laneB_result", "")
        before["verification_level"] = b.get("evidence_level", "")
        before["visual_status"] = b.get("visual_status", "")
        before["answer_pairing_status"] = b.get("answer_status", "")
        before["rubric_pairing_status"] = b.get("rubric_status", "")
        before["blocker_reason"] = b.get("blocker_reason", "")
        before["phase04_level"] = level
        before["fusion_status"] = fusion
        before["student稿_permission"] = student
        if b.get("section_scope"):
            before["section_scope"] = b["section_scope"]
        if b.get("node"):
            before["knowledge_node"] = b["node"]
        if b.get("logical_or_method_form"):
            before["reasoning_node"] = b["logical_or_method_form"]

        codex_answer = answer_letter(add.get("answer_status", "") if add else "")
        laneb_answer = answer_letter(b.get("answer_status", ""))
        conflicts: list[str] = []
        if add and add.get("section_scope") and b.get("section_scope") and add["section_scope"] != b["section_scope"]:
            conflicts.append(f"scope_diff CodexA={add['section_scope']} LaneB={b['section_scope']}")
        if codex_answer and laneb_answer and codex_answer != laneb_answer:
            conflicts.append(f"answer_diff CodexA={codex_answer} LaneB={laneb_answer}")
        if add and add.get("can_enter_fusion_before_laneB") == "no" and b.get("can_enter_fusion") == "yes":
            conflicts.append("promotion_requires_GPT_review")

        recon_rows.append(
            {
                "canonical_question_id": qid,
                "suite_id": before.get("suite_id", ""),
                "qno": before.get("original_qno", b.get("qno", "")),
                "codexA_before_level": before_level,
                "codexA_batch02_status": "in_addendum" if add else "not_in_addendum",
                "laneB_result": b.get("laneB_result", ""),
                "laneB_evidence_level": b.get("evidence_level", ""),
                "laneB_can_enter_fusion": b.get("can_enter_fusion", ""),
                "merged_level": level,
                "merged_fusion_status": fusion,
                "conflict_or_note": "; ".join(conflicts) or b.get("notes", ""),
                "source_evidence": b.get("source_evidence", ""),
            }
        )

    for qid, add in add_by_id.items():
        if qid in b_by_id:
            continue
        recon_rows.append(
            {
                "canonical_question_id": qid,
                "suite_id": f"S-{add.get('suite', '')}",
                "qno": add.get("qno", ""),
                "codexA_before_level": "codexA_batch02_addendum",
                "codexA_batch02_status": "in_addendum",
                "laneB_result": "missing_from_laneB_batch02",
                "laneB_evidence_level": "",
                "laneB_can_enter_fusion": "no",
                "merged_level": by_id.get(qid, {}).get("phase04_level", "not_in_control"),
                "merged_fusion_status": by_id.get(qid, {}).get("fusion_status", "not_in_control"),
                "conflict_or_note": "Codex A addendum row did not receive Lane B verification in Batch02.",
                "source_evidence": add.get("notes", ""),
            }
        )

    write_csv(OUT, fieldnames, base_rows)
    recon_fields = [
        "canonical_question_id",
        "suite_id",
        "qno",
        "codexA_before_level",
        "codexA_batch02_status",
        "laneB_result",
        "laneB_evidence_level",
        "laneB_can_enter_fusion",
        "merged_level",
        "merged_fusion_status",
        "conflict_or_note",
        "source_evidence",
    ]
    write_csv(RECON, recon_fields, recon_rows)

    level_counts = Counter(row["phase04_level"] for row in base_rows)
    recon_counts = Counter(row["merged_level"] for row in recon_rows)
    conflicts = [
        row
        for row in recon_rows
        if "diff" in row["conflict_or_note"]
        or "CONFLICT" in row["conflict_or_note"]
        or row["laneB_result"] == "missing_from_laneB_batch02"
    ]
    locked = [row for row in recon_rows if row["merged_level"] == "L4_LOCKED_FOR_FUSION"]
    confirmed = [row for row in recon_rows if row["merged_level"] == "L3_A_PLUS_B_TARGET_CONFIRMED"]

    lines = [
        "# Phase04 Batch02 Codex A / Lane B Reconciliation",
        "",
        "Status: `BATCH02_MERGED_NO_STUDENT_DRAFT`.",
        "",
        "## Control Counts After Batch02",
        "",
    ]
    for key, value in level_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Batch02 Merge Counts", ""])
    for key, value in recon_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Locked / Confirmed Rows", ""])
    for row in locked + confirmed:
        lines.append(f"- `{row['canonical_question_id']}` | {row['laneB_evidence_level']} | {row['merged_level']} | {row['conflict_or_note']}")
    lines.extend(["", "## Conflicts Or Missing Lane B Rows", ""])
    if conflicts:
        for row in conflicts:
            lines.append(f"- `{row['canonical_question_id']}` | {row['laneB_result']} | {row['conflict_or_note']}")
    else:
        lines.append("- none detected by mechanical comparison")
    lines.extend(
        [
            "",
            "## Gate Note",
            "",
            "- This merge is evidence-fusion only. `student稿_permission` remains blocked for all rows.",
            "- GPT-5.5 Pro must review this Batch02 packet before Phase04 promotion.",
        ]
    )
    RECON_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(f"wrote {OUT}")
    print(f"wrote {RECON}")
    print(f"wrote {RECON_MD}")
    print(f"control rows {len(base_rows)}")
    print(f"reconciliation rows {len(recon_rows)}")


if __name__ == "__main__":
    main()
