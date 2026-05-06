#!/usr/bin/env python3
"""Build GPT-required Phase04 Batch02 control files."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COVERAGE = ROOT / "05_coverage"
CONFLICTS = ROOT / "06_conflicts"

CONTROL = COVERAGE / "phase04_control_base_status_after_laneB_batch01.csv"
ADDENDUM = COVERAGE / "phase04_batch02_codex_visual_scope_repair_addendum.csv"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def blocked_type(row: dict[str, str]) -> str:
    level = row.get("phase04_level", "")
    if level.startswith("L4"):
        return "LOCKED_FOR_FUSION"
    if level.startswith("L3"):
        return "CONFIRMED_NOT_LOCKED"
    if level.startswith("L2"):
        return "PENDING_SCOPE"
    if level.startswith("L1"):
        return "A_ONLY_PENDING_B"

    reason = (row.get("blocker_reason", "") + " " + row.get("gap_action", "")).lower()
    section = row.get("section_scope", "")
    scope = row.get("scope_status", "")
    qtype = row.get("question_type", "")

    if "duplicate" in reason:
        return "DUPLICATE_REMOVED"
    if "support" in reason or "reference" in reason:
        return "REFERENCE_SUPPORT_ROW"
    if "visual" in reason or "image" in reason or "scan" in reason or "pdf text layer is blank" in reason:
        return "VISUAL_BLOCKED"
    if "answer" in reason or row.get("answer_pairing_status") == "missing_or_unpaired":
        return "ANSWER_SOURCE_MISSING"
    if "rubric" in reason or row.get("rubric_pairing_status") == "missing_or_unpaired":
        return "RUBRIC_SOURCE_MISSING"
    if "options" in reason or "choice options" in reason:
        return "OPTIONS_MISSING"
    if section == "边界":
        return "OUT_OF_SCOPE_OR_BOUNDARY"
    if section == "待判" or scope == "pending":
        return "PENDING_SCOPE"
    if qtype == "suite_visual_blocker":
        return "VISUAL_BLOCKED"
    return "TRUE_BLOCKER"


def build_blocked_split(rows: list[dict[str, str]]) -> None:
    out = []
    fields = [
        "canonical_question_id",
        "suite_id",
        "original_qno",
        "phase04_level",
        "scope_status",
        "section_scope",
        "question_type",
        "blocked_type",
        "answer_pairing_status",
        "rubric_pairing_status",
        "visual_status",
        "blocker_reason",
        "excerpt",
    ]
    for row in rows:
        out.append({field: row.get(field, "") for field in fields if field != "blocked_type"} | {"blocked_type": blocked_type(row)})
    write_csv(COVERAGE / "phase04_blocked_type_split.csv", out, fields)

    counts = Counter(r["blocked_type"] for r in out)
    lines = ["# Phase04 Blocked Type Split", "", "Status: `BATCH02_CONTROL_SPLIT_READY`.", "", "## Counts", ""]
    for key, value in counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Notes", "", "- This split is heuristic and conservative; Lane B must recheck P0 visual/answer/scope rows.", "- It exists to prevent `L0_BLOCKED=236` from hiding out-of-scope, duplicate, support, and true blocker rows in one bucket."])
    (COVERAGE / "phase04_blocked_type_split.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_chaoyang_q12(rows: list[dict[str, str]]) -> None:
    target = next(r for r in rows if r["canonical_question_id"] == "Q-2026朝阳期中-12")
    fields = [
        "target_id",
        "suite",
        "qno",
        "source_locator",
        "section_scope",
        "answer_status",
        "verification_level",
        "current_phase04_level",
        "required_laneB_action",
        "notes",
    ]
    out = [
        {
            "target_id": target["canonical_question_id"],
            "suite": target["suite_id"],
            "qno": target["original_qno"],
            "source_locator": target["stable_locator"],
            "section_scope": target["section_scope"],
            "answer_status": target["answer_pairing_status"],
            "verification_level": target["verification_level"],
            "current_phase04_level": target["phase04_level"],
            "required_laneB_action": "write formal Batch02 results CSV row and confirm can_enter_fusion decision",
            "notes": "GPT P0-1: Q12 was corrected from Codex 待判 by Lane B; control count must remain 120 and the B result row must become machine-readable.",
        }
    ]
    write_csv(COVERAGE / "phase04_2026_chaoyang_q12_formal_patch.csv", out, fields)


def build_fengtai_scan() -> None:
    selected_rows = read_csv(ADDENDUM)
    selected_by_id = {r["target_id"]: r for r in selected_rows if r["suite"] == "2026丰台一模"}
    answer_key = {
        "1": "B",
        "2": "A",
        "3": "D",
        "4": "A",
        "5": "A",
        "6": "D",
        "7": "B",
        "8": "C",
        "9": "D",
        "10": "C",
        "11": "D",
        "12": "B",
        "13": "A",
        "14": "A",
        "15": "C",
    }
    classifications = {
        "1": ("no", "边界", "中国特色社会主义/时政", "not_selected3"),
        "2": ("no", "边界", "政治与法治", "not_selected3"),
        "3": ("no", "边界", "政治与法治", "not_selected3"),
        "4": ("yes", "思维", "综合思维", "new_candidate_batch02"),
        "5": ("boundary", "边界", "联系/认识哲学边界", "not_selected3_mainline"),
        "6": ("boundary", "边界", "系统/联系与文化边界", "not_selected3_mainline"),
        "7": ("yes", "思维", "发散聚合;超前思维", "new_candidate_batch02"),
        "8": ("yes", "推理", "充分条件假言推理", "new_candidate_batch02"),
        "9": ("yes", "推理", "概念外延关系;联言判断", "new_candidate_batch02"),
        "10": ("no", "边界", "法律与生活", "not_selected3"),
        "11": ("no", "边界", "法律与生活", "not_selected3"),
        "12": ("no", "边界", "经济与社会路径", "not_selected3"),
        "13": ("no", "边界", "经济监管", "not_selected3"),
        "14": ("no", "边界", "当代国际政治与经济", "not_selected3"),
        "15": ("no", "边界", "当代国际政治与经济", "not_selected3"),
        "16": ("no", "边界", "哲学与文化", "not_selected3"),
        "17": ("no", "边界", "政治与法治", "not_selected3"),
        "18(1)": ("no", "边界", "经济与社会", "not_selected3"),
        "18(2)": ("yes", "推理", "必要条件假言推理;三段论大项不当扩大", "already_L4"),
        "19": ("no", "边界", "当代国际政治与经济", "not_selected3"),
        "20": ("no", "边界", "法律与生活", "not_selected3"),
        "21": ("boundary", "边界", "党领导/哲学边界", "not_selected3_mainline"),
    }
    fields = ["suite", "qno", "render_locator", "answer", "selected3_candidate", "section_scope", "node", "status", "notes"]
    rows = []
    for qno, (candidate, section, node, status) in classifications.items():
        target_id = f"Q-2026丰台一模-{qno.replace('(', '-').replace(')', '')}"
        notes = ""
        if qno in {"4", "7", "8", "9"}:
            patch = selected_by_id.get(f"Q-2026丰台一模-{qno}", {})
            notes = patch.get("notes", "")
        rows.append(
            {
                "suite": "2026丰台一模",
                "qno": qno,
                "render_locator": "042 renders/contact sheet + supplemental text",
                "answer": answer_key.get(qno, "subjective_or_no_choice_key"),
                "selected3_candidate": candidate,
                "section_scope": section,
                "node": node,
                "status": status,
                "notes": notes,
            }
        )
    write_csv(COVERAGE / "phase04_2026_fengtai_yimo_visual_suite_scan.csv", rows, fields)

    lines = [
        "# 2026丰台一模 Selected-Compulsory-Three Candidates",
        "",
        "Status: `CODEX_A_VISUAL_SCAN_READY_FOR_LANEB`.",
        "",
        "New candidates that were missing from Batch01 control base:",
        "",
    ]
    for qno in ["4", "7", "8", "9"]:
        patch = selected_by_id[f"Q-2026丰台一模-{qno}"]
        lines.append(f"- `Q{qno}` | {patch['section_scope']} | {patch['answer_status']} | {patch['reasoning_or_thinking_node']}")
    lines.extend(["", "Already locked:", "", "- `Q18(2)` | 推理 | 必要条件假言推理 + 三段论大项不当扩大 | L4 before student稿 gate"])
    (COVERAGE / "phase04_2026_fengtai_yimo_selected3_candidates.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_haidian_q12_q13() -> None:
    add = {r["target_id"]: r for r in read_csv(ADDENDUM)}
    fields = ["target_id", "suite", "qno", "options_status", "answer_status", "section_scope", "node", "can_enter_fusion_before_laneB", "required_action"]
    rows = []
    for qid in ["Q-2025海淀二模-12", "Q-2025海淀二模-13"]:
        row = add[qid]
        rows.append(
            {
                "target_id": qid,
                "suite": row["suite"],
                "qno": row["qno"],
                "options_status": "visual_options_recovered_from_008_page04",
                "answer_status": row["answer_status"],
                "section_scope": row["section_scope"],
                "node": row["reasoning_or_thinking_node"],
                "can_enter_fusion_before_laneB": "no",
                "required_action": "Lane B independently verifies supplemental answer source and visual options; no logic-derived answer",
            }
        )
    write_csv(COVERAGE / "phase04_2025_haidian_ermo_Q12_Q13_status.csv", rows, fields)

    lines = [
        "# 2025海淀二模 Q12/Q13 Answer Search",
        "",
        "Status: `ANSWER_SOURCE_FOUND_BUT_PENDING_LANEB`.",
        "",
        "- Original current-run sources `009/010/011` did not expose Q12/Q13 answer pairing.",
        "- Codex A used rendered `008 page_04.png` for full options.",
        "- Batch02 registered supplemental raw answer source `SUPP-2025海淀二模-北京高考在线-试题及答案`.",
        "- Supplemental answer table gives `Q12=D`, `Q13=C`.",
        "- No row enters fusion before Lane B independently confirms both source and options.",
        "- No answer may be inferred from question logic.",
    ]
    (COVERAGE / "phase04_2025_haidian_ermo_Q12_Q13_answer_search.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_q11_and_q2(rows: list[dict[str, str]]) -> None:
    fields = ["target_id", "suite", "qno", "codexA_status", "answer_status", "required_laneB_action", "can_enter_fusion_before_laneB"]
    write_csv(
        COVERAGE / "phase04_2024_xicheng_yimo_Q11_B_recheck.csv",
        [
            {
                "target_id": "Q-2024西城一模-11",
                "suite": "2024西城一模",
                "qno": "11",
                "codexA_status": "Word XML textbox options recovered; answer B from 025/026",
                "answer_status": "answer_confirmed_B_from_key",
                "required_laneB_action": "independently extract DOCX XML textbox or render DOCX and confirm all four options plus answer pairing",
                "can_enter_fusion_before_laneB": "no",
            }
        ],
        fields,
    )

    q2 = next(r for r in rows if r["canonical_question_id"] == "Q-2025海淀期末-2")
    lines = [
        "# 2025海淀期末 Q2 Scope Decision",
        "",
        "Status: `SCOPE_DECISION_READY_FOR_LANEB`.",
        "",
        "GPT裁决方向：可入思维部分证据池，但必须标注边界交叉/诱惑项。",
        "",
        "Evidence:",
        "",
        "- Answer: `C` = ②③.",
        "- ② 场景迁移/联想思维，是选必三思维。",
        "- ③ 辩证思维整体性，是选必三思维。",
        "- ① 扬弃具有哲学诱惑项性质，但不是答案。",
        "- ④ 经验推广不构成明确思维方法。",
        "",
        "Recommended machine status:",
        "",
        "```text",
        "section_scope = 思维",
        "scope_status = cross or in_scope_with_boundary_note",
        "verification_level = B-choice-signal",
        "fusion_level = L3 only after Lane B row can_enter_fusion=yes",
        "student稿_permission = no",
        "```",
        "",
        "Current Batch01 row:",
        "",
        f"- phase04_level: `{q2['phase04_level']}`",
        f"- answer_pairing_status: `{q2['answer_pairing_status']}`",
        f"- blocker_reason: `{q2['blocker_reason']}`",
    ]
    (COVERAGE / "phase04_2025_haidian_qimo_Q2_scope_decision.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_aonly_queue(rows: list[dict[str, str]]) -> None:
    add_rows = read_csv(ADDENDUM)
    fields = ["target_id", "suite", "qno", "section_scope", "tranche", "reason", "source_locator"]
    queue = []
    for row in rows:
        if row["phase04_level"] == "L1_A_ONLY_PENDING_B_TARGET":
            section = row["section_scope"]
            reason = row["blocker_reason"]
            if section in {"推理", "交叉"}:
                tranche = "Batch02_Tranche_A_reasoning_cross_formal"
            elif "visual" in reason.lower() or "image" in reason.lower() or "scan" in reason.lower():
                tranche = "Batch02_Tranche_B_visual_risk"
            elif "answer" in reason.lower() or row["answer_pairing_status"] in {"missing_or_unpaired", "paired_candidate"}:
                tranche = "Batch02_Tranche_C_answer_pairing"
            else:
                tranche = "Batch02_Tranche_D_thinking_pending_B"
            queue.append(
                {
                    "target_id": row["canonical_question_id"],
                    "suite": row["suite_id"],
                    "qno": row["original_qno"],
                    "section_scope": section,
                    "tranche": tranche,
                    "reason": reason,
                    "source_locator": row["stable_locator"],
                }
            )
    for row in add_rows:
        queue.append(
            {
                "target_id": row["target_id"],
                "suite": row["suite"],
                "qno": row["qno"],
                "section_scope": row["section_scope"],
                "tranche": "Batch02_Tranche_B_visual_or_answer_patch",
                "reason": row["blocker_reason"],
                "source_locator": row["source_locator"],
            }
        )
    write_csv(COVERAGE / "phase04_Aonly_batch02_queue.csv", queue, fields)


def main() -> None:
    rows = read_csv(CONTROL)
    build_blocked_split(rows)
    build_chaoyang_q12(rows)
    build_fengtai_scan()
    build_haidian_q12_q13()
    build_q11_and_q2(rows)
    build_aonly_queue(rows)
    print("Batch02 GPT-required files written.")


if __name__ == "__main__":
    main()
