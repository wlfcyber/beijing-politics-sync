#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTROL = ROOT / "05_coverage/phase04_control_base_status.csv"
LANEB = ROOT / "claudecode_lane/phase04_laneB_targeted_verification_results.csv"
OUT = ROOT / "05_coverage/phase04_control_base_status_after_laneB_batch01.csv"
RECON = ROOT / "06_conflicts/phase04_batch01_codexA_laneB_reconciliation.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def canonical_target(row: dict[str, str]) -> str:
    suite = row["suite"].strip()
    qno = row["qno"].strip()
    qno = qno.replace("Q", "").replace("（", "(").replace("）", ")")
    if qno == "PENDING":
        return f"SUITE-{suite}-PENDING"
    if qno == "18(2)" and suite == "2026丰台一模":
        return "Q-2026丰台一模-18-2"
    if qno == "16(2)":
        return f"Q-{suite}-16-2"
    if qno == "16(3)":
        return f"Q-{suite}-16-3"
    return f"Q-{suite}-{qno}"


def main() -> None:
    control = read_csv(CONTROL)
    lane_b_rows = read_csv(LANEB)
    b_by_id = {canonical_target(r): r for r in lane_b_rows}

    merged: list[dict[str, str]] = []
    recon: list[dict[str, str]] = []

    for r in control:
        out = dict(r)
        b = b_by_id.get(r["canonical_question_id"])
        if b:
            out["B_status"] = b["laneB_result"]
            out["visual_status"] = b["visual_status"]
            out["answer_pairing_status"] = b["answer_status"]
            out["rubric_pairing_status"] = b["rubric_status"]
            out["blocker_reason"] = b["blocker_reason"]
            out["verification_level"] = b["evidence_level"]
            if b["laneB_result"] == "B_TARGET_CONFIRMED" and b["can_enter_fusion"] == "yes":
                if b["evidence_level"] == "A-formal":
                    out["phase04_level"] = "L4_LOCKED_FOR_FUSION"
                    out["fusion_status"] = "locked_for_fusion_after_laneB_batch01"
                else:
                    out["phase04_level"] = "L3_A_PLUS_B_TARGET_CONFIRMED"
                    out["fusion_status"] = "confirmed_for_evidence_fusion_pending_formal_lock"
                out["student稿_permission"] = "NO_STUDENT_DRAFT_YET_GPT_BLOCKED"
            elif b["can_enter_fusion"].startswith("conditional"):
                out["phase04_level"] = "L2_PENDING_SCOPE_DECISION"
                out["fusion_status"] = "conditional_fusion_pending_scope_decision"
                out["student稿_permission"] = "NO_STUDENT_DRAFT"
            elif b["laneB_result"] in {"B_TARGET_BLOCKED", "B_TARGET_NEEDS_VISUAL"}:
                out["phase04_level"] = "L0_BLOCKED"
                out["fusion_status"] = "blocked_after_laneB_batch01"
                out["student稿_permission"] = "NO_STUDENT_DRAFT"
            recon.append({
                "canonical_question_id": r["canonical_question_id"],
                "suite_id": r["suite_id"],
                "qno": r["original_qno"],
                "codexA_before_level": r["phase04_level"],
                "laneB_result": b["laneB_result"],
                "laneB_evidence_level": b["evidence_level"],
                "merged_level": out["phase04_level"],
                "merged_fusion_status": out["fusion_status"],
                "conflict_or_note": b["notes"],
            })
        merged.append(out)

    # Report-only discovery from ClaudeCode Batch01: this row existed in control as 待判 and was patched by Codex A after B reported it.
    q12 = next((r for r in merged if r["canonical_question_id"] == "Q-2026朝阳期中-12"), None)
    if q12:
        q12["B_status"] = "B_TARGET_CONFIRMED_IN_REPORT_NOT_RESULTS_CSV"
        q12["verification_level"] = "B-choice-signal"
        q12["phase04_level"] = "L3_A_PLUS_B_TARGET_CONFIRMED"
        q12["fusion_status"] = "confirmed_for_evidence_fusion_pending_formal_lock"
        q12["student稿_permission"] = "NO_STUDENT_DRAFT_YET_GPT_BLOCKED"
        q12["blocker_reason"] = "ClaudeCode Batch01 report found answer B and logical-rule classification; needs Batch02 formal CSV row reconciliation before lock."
        recon.append({
            "canonical_question_id": "Q-2026朝阳期中-12",
            "suite_id": "S-2026朝阳期中",
            "qno": "12",
            "codexA_before_level": "L0_BLOCKED_as_待判_before_patch",
            "laneB_result": "B_TARGET_CONFIRMED_IN_REPORT_NOT_RESULTS_CSV",
            "laneB_evidence_level": "B-choice-signal",
            "merged_level": q12["phase04_level"],
            "merged_fusion_status": q12["fusion_status"],
            "conflict_or_note": "ClaudeCode report found Q12 as missing from in-scope index; Codex patched it to 推理 with answer B from 003 answer table; needs formal reconciliation in Batch02.",
        })

    # Codex visual recovery after the Lane B prompt; B did not see these newer notes.
    for qid, note in [
        ("Q-2024西城一模-11", "Codex A recovered all four options from Word XML text boxes after Lane B had marked options as image-blocked; keep pending B recheck, not locked."),
        ("Q-2025海淀二模-12", "Codex A visually read page_04 after Lane B run and recovered full options; answer source still missing, so remains blocked."),
        ("Q-2025海淀二模-13", "Codex A visually read page_04 after Lane B run and recovered full options; answer source still missing, so remains blocked."),
    ]:
        recon.append({
            "canonical_question_id": qid,
            "suite_id": "",
            "qno": "",
            "codexA_before_level": "post_laneB_codexA_new_evidence",
            "laneB_result": b_by_id.get(qid, {}).get("laneB_result", "not_in_laneB_csv"),
            "laneB_evidence_level": b_by_id.get(qid, {}).get("evidence_level", ""),
            "merged_level": next((r["phase04_level"] for r in merged if r["canonical_question_id"] == qid), "not_in_control"),
            "merged_fusion_status": next((r["fusion_status"] for r in merged if r["canonical_question_id"] == qid), "not_in_control"),
            "conflict_or_note": note,
        })

    write_csv(OUT, list(merged[0]), merged)
    write_csv(RECON, list(recon[0]), recon)
    print("merged rows", len(merged))
    print("reconciliation rows", len(recon))


if __name__ == "__main__":
    main()
