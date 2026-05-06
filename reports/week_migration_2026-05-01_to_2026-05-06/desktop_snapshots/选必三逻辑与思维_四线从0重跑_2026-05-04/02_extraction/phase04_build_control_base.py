#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LANEA = ROOT / "05_coverage/phase03_laneA_dedup_question_matrix.csv"
SUPPORT = ROOT / "05_coverage/phase03_laneA_support_evidence_matrix.csv"
DUPES = ROOT / "05_coverage/phase03_laneA_duplicate_or_reference_rows.csv"
GAPS = ROOT / "06_conflicts/phase03_post_patch_gap_queue.csv"
CODEX_PATCH = ROOT / "05_coverage/phase03_codex_local_patch_addendum.csv"
LANEB_PATCH = ROOT / "claudecode_lane/phase03_laneB_patch_addendum.csv"

OUT_DIR = ROOT / "05_coverage"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def norm_qno(qno: str) -> str:
    cleaned = (qno or "").replace("（", "(").replace("）", ")").strip()
    if cleaned.upper().startswith("Q"):
        cleaned = cleaned[1:].strip()
    return cleaned


def key(suite: str, qno: str) -> tuple[str, str]:
    return (suite.replace("S-", "").strip(), norm_qno(qno))


def main() -> None:
    lanea = read_csv(LANEA)
    gaps = read_csv(GAPS)
    codex_patch = read_csv(CODEX_PATCH)
    laneb_patch = read_csv(LANEB_PATCH)

    gap_by_key = {(r["suite"].strip(), norm_qno(r["qno"])): r for r in gaps}
    codex_patch_by_key = {
        (r["suite"].strip(), norm_qno(r["原始题号"])): r for r in codex_patch
    }

    laneb_patch_by_key: dict[tuple[str, str], dict[str, str]] = {}
    for r in laneb_patch:
        suite = r.get("suite_id", "")
        if "丰台" in suite:
            laneb_patch_by_key[("2026丰台一模", norm_qno(r.get("原始题号", "")))] = r
        if "海淀" in suite:
            laneb_patch_by_key[("2025海淀二模", norm_qno(r.get("原始题号", "")))] = r

    control_rows: list[dict[str, str]] = []
    answer_rows: list[dict[str, str]] = []
    rubric_rows: list[dict[str, str]] = []
    visual_rows: list[dict[str, str]] = []
    blocked_rows: list[dict[str, str]] = []

    for r in lanea:
        suite_name = r["suite_id"].replace("S-", "")
        qno = norm_qno(r["原始题号"])
        k = key(r["suite_id"], qno)
        patch = codex_patch_by_key.get(k)
        bpatch = laneb_patch_by_key.get(k)
        gap = gap_by_key.get(k)

        section = patch.get("部分归属", r["部分归属"]) if patch else r["部分归属"]
        qtype = patch.get("题型", r["题型"]) if patch else r["题型"]

        if section in {"思维", "推理", "交叉"}:
            scope_status = "in_scope" if section != "交叉" else "cross"
        elif section in {"边界", "待判", "missing"}:
            scope_status = "pending"
        else:
            scope_status = "out_of_scope"

        answer_status = "paired_candidate" if r["是否有答案"].startswith("yes") else "missing_or_unpaired"
        rubric_status = "paired_candidate" if (
            r["是否有评分细则"].startswith("yes") or r["是否有讲评"].startswith("yes")
        ) else "missing_or_unpaired"
        visual_status = "visual_confirmed" if r["是否已视觉核读"] == "yes" else "not_visual_confirmed"
        if bpatch:
            visual_status = "visual_confirmed_laneB"
            answer_status = "paired_formal"
            rubric_status = "paired_formal"
        if patch and patch.get("证据等级") == "B-choice-signal":
            answer_status = "paired_answer_table_B_choice_signal"
        if patch and patch.get("证据等级") == "A-formal":
            answer_status = "paired_formal"
            rubric_status = "paired_formal"

        blocker_reason = r.get("blocked_reason", "")
        phase04_level = "L0_BLOCKED"
        fusion_status = "blocked"
        verification_level = "A_inventory_only"
        b_status = "not_verified_by_B"

        if bpatch:
            phase04_level = "L4_LOCKED_FOR_FUSION"
            fusion_status = "locked_for_fusion"
            verification_level = "A_plus_B_target_confirmed"
            b_status = "B_target_confirmed"
            blocker_reason = "student draft still blocked by GPT Phase03 gate"
        elif patch:
            phase04_level = "L1_A_ONLY_PENDING_B_TARGET"
            fusion_status = "pending_B_target_verification"
            verification_level = patch.get("证据等级", "A_patch")
            blocker_reason = "Codex local patch ready; requires Lane B targeted verification before locked fusion"
        elif gap:
            phase04_level = "L0_BLOCKED" if gap["priority"] == "P0" else "L1_A_ONLY_PENDING_B_TARGET"
            fusion_status = "blocked_or_pending_gap_queue"
            blocker_reason = gap.get("recommended_action", "") or gap.get("reason", "")
        elif section in {"思维", "推理", "交叉"}:
            if r["题型"] == "主观题" or section == "推理":
                phase04_level = "L1_A_ONLY_PENDING_B_TARGET"
                fusion_status = "pending_B_target_verification"
                blocker_reason = "in-scope/cross row requires targeted verification before fusion"
            else:
                phase04_level = "L1_A_ONLY_PENDING_B_TARGET"
                fusion_status = "pending_answer_option_verification"
                blocker_reason = "choice row requires full options and reliable answer pairing"
        elif scope_status == "pending":
            phase04_level = "L0_BLOCKED"
            fusion_status = "blocked_pending_scope"
            blocker_reason = blocker_reason or "scope pending or boundary row"
        else:
            phase04_level = "L0_BLOCKED"
            fusion_status = "out_of_scope_or_blocked"
            blocker_reason = blocker_reason or "not in current fusion scope"

        if "blocked_until_options_visual_check" in r["blocked_status"] and not bpatch and not patch:
            phase04_level = "L0_BLOCKED"
            fusion_status = "blocked_visual_or_options"
            blocker_reason = blocker_reason or "options/visual check not complete"

        student_permission = "NO_STUDENT_DRAFT"
        if phase04_level == "L4_LOCKED_FOR_FUSION":
            student_permission = "NO_STUDENT_DRAFT_YET_GPT_BLOCKED"

        row = {
            "canonical_question_id": r["question_id"],
            "suite_id": r["suite_id"],
            "source_id": r["source_id"],
            "stable_locator": r["stable_locator"],
            "original_qno": qno,
            "question_type": qtype,
            "scope_status": scope_status,
            "section_scope": section,
            "knowledge_node": patch.get("rule_or_thinking_node", r.get("知识节点", "")) if patch else r.get("知识节点", ""),
            "reasoning_node": bpatch.get("primary_type", r.get("题型节点", "")) if bpatch else r.get("题型节点", ""),
            "A_status": "canonical_control_base_row",
            "B_status": b_status,
            "fusion_status": fusion_status,
            "phase04_level": phase04_level,
            "verification_level": verification_level,
            "answer_pairing_status": answer_status,
            "rubric_pairing_status": rubric_status,
            "visual_status": visual_status,
            "student稿_permission": student_permission,
            "blocker_reason": blocker_reason,
            "gap_priority": gap.get("priority", "") if gap else "",
            "gap_action": gap.get("recommended_action", "") if gap else "",
            "excerpt": r.get("excerpt", ""),
        }
        control_rows.append(row)

        answer_rows.append({
            "canonical_question_id": row["canonical_question_id"],
            "suite_id": row["suite_id"],
            "original_qno": qno,
            "question_type": qtype,
            "answer_pairing_status": answer_status,
            "can_enter_fusion": "yes" if phase04_level == "L4_LOCKED_FOR_FUSION" else "no",
            "can_enter_student_draft": "no",
            "notes": patch.get("answer_or_scoring", "") if patch else "",
        })
        rubric_rows.append({
            "canonical_question_id": row["canonical_question_id"],
            "suite_id": row["suite_id"],
            "original_qno": qno,
            "question_type": qtype,
            "rubric_pairing_status": rubric_status,
            "can_enter_fusion": "yes" if phase04_level == "L4_LOCKED_FOR_FUSION" else "no",
            "can_enter_student_draft": "no",
            "notes": bpatch.get("logical_form_or_thinking_chain", "") if bpatch else "",
        })
        visual_rows.append({
            "canonical_question_id": row["canonical_question_id"],
            "suite_id": row["suite_id"],
            "original_qno": qno,
            "requires_visual_processing": r["是否需要视觉核读"],
            "visual_confirmation_status": visual_status,
            "can_enter_locked_fusion": "yes" if phase04_level == "L4_LOCKED_FOR_FUSION" else "no",
            "notes": bpatch.get("source_locator", "") if bpatch else "",
        })
        if phase04_level == "L0_BLOCKED":
            blocked_rows.append({
                "canonical_question_id": row["canonical_question_id"],
                "suite_id": row["suite_id"],
                "original_qno": qno,
                "section_scope": section,
                "question_type": qtype,
                "blocker_reason": blocker_reason,
                "recommended_action": gap.get("recommended_action", "") if gap else "",
            })

    fields = [
        "canonical_question_id", "suite_id", "source_id", "stable_locator", "original_qno",
        "question_type", "scope_status", "section_scope", "knowledge_node", "reasoning_node",
        "A_status", "B_status", "fusion_status", "phase04_level", "verification_level",
        "answer_pairing_status", "rubric_pairing_status", "visual_status",
        "student稿_permission", "blocker_reason", "gap_priority", "gap_action", "excerpt",
    ]
    write_csv(OUT_DIR / "phase04_control_base_status.csv", fields, control_rows)
    write_csv(OUT_DIR / "phase04_answer_key_pairing_matrix.csv", list(answer_rows[0]), answer_rows)
    write_csv(OUT_DIR / "phase04_rubric_pairing_matrix.csv", list(rubric_rows[0]), rubric_rows)
    write_csv(OUT_DIR / "phase04_visual_confirmation_matrix.csv", list(visual_rows[0]), visual_rows)
    write_csv(OUT_DIR / "phase04_blocked_questions_final_for_phase04.csv", list(blocked_rows[0]) if blocked_rows else ["canonical_question_id"], blocked_rows)

    in_scope_rows = [r for r in control_rows if r["section_scope"] in {"思维", "推理", "交叉"}]
    support_rows = read_csv(SUPPORT)
    dupe_rows = read_csv(DUPES)
    counts = Counter(r["phase04_level"] for r in control_rows)
    scope_counts = Counter(r["section_scope"] for r in control_rows)

    (OUT_DIR / "phase04_canonical_358_index.md").write_text(
        "# Phase04 Canonical 358 Index\n\n"
        f"- total canonical rows: {len(control_rows)}\n"
        f"- phase04 levels: {dict(counts)}\n"
        f"- section scopes: {dict(scope_counts)}\n"
        f"- control file: `phase04_control_base_status.csv`\n"
        "\nThis index freezes the Codex A canonical paper/question rows as the every-question control base. It is not a final truth base and does not authorize student稿.\n",
        encoding="utf-8",
    )

    with (OUT_DIR / "phase04_in_scope_cross_119_index.md").open("w", encoding="utf-8") as f:
        f.write("# Phase04 In-Scope/Cross 119 Index\n\n")
        f.write(f"- total in-scope/cross rows: {len(in_scope_rows)}\n")
        f.write("- allowed use: evidence fusion control only\n")
        f.write("- forbidden use: student稿 / Opus成文化 / Word-PDF / PASS\n\n")
        for r in in_scope_rows:
            f.write(
                f"- {r['canonical_question_id']} | {r['section_scope']} | {r['question_type']} | "
                f"{r['phase04_level']} | {r['fusion_status']} | {r['blocker_reason']}\n"
            )

    (OUT_DIR / "phase04_support_reference_index.md").write_text(
        "# Phase04 Support/Reference Evidence Index\n\n"
        f"- support/reference rows split from Lane A: {len(support_rows)}\n"
        "- use: answer/rubric/commentary pairing only\n"
        "- forbidden use: replacing original paper/question rows\n",
        encoding="utf-8",
    )

    (OUT_DIR / "phase04_removed_duplicates_log.md").write_text(
        "# Phase04 Removed Duplicate/Reference Log\n\n"
        f"- duplicate/reference rows preserved: {len(dupe_rows)}\n"
        "- note: these rows remain audit evidence and cannot disappear from final governance.\n",
        encoding="utf-8",
    )

    print("phase04_control_base_status.csv rows", len(control_rows))
    print("phase04_in_scope_cross_119_index.md rows", len(in_scope_rows))
    print("phase04 levels", dict(counts))
    print("section scopes", dict(scope_counts))


if __name__ == "__main__":
    main()
