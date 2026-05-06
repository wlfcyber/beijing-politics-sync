#!/usr/bin/env python3
from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "05_coverage" / "phase04_control_base_status_after_batch02.csv"
SUBJECTIVE_B_CANDIDATES = [
    ROOT / "claudecode_lane" / "opus47_batch03_subjective" / "phase04_batch03_A_subjective_results.csv",
    ROOT / "claudecode_lane" / "phase04_batch03_A_subjective_results.csv",
]
CHOICE_B_CANDIDATES = [
    ROOT / "claudecode_lane" / "opus47_batch03_choice" / "phase04_batch03_B_choice_results_normalized.csv",
    ROOT / "claudecode_lane" / "opus47_batch03_choice" / "phase04_batch03_B_choice_results.csv",
    ROOT / "claudecode_lane" / "phase04_batch03_B_choice_results.csv",
]
SUBJECTIVE_A = ROOT / "codex_lane" / "phase04_batch03_A_subjective_codexA_precheck.csv"
CHOICE_A = ROOT / "codex_lane" / "phase04_batch03_B_choice_codexA_precheck.csv"
OUT = ROOT / "05_coverage" / "phase04_control_base_status_after_batch03.csv"
OUT_RECON_CSV = ROOT / "06_conflicts" / "phase04_batch03_codexA_laneB_reconciliation.csv"
OUT_RECON_MD = ROOT / "06_conflicts" / "phase04_batch03_codexA_laneB_reconciliation.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    bad = [i for i, row in enumerate(rows, 2) if None in row]
    if bad:
        raise SystemExit(f"malformed CSV field count in {path}: lines {bad[:10]}")
    return rows


def read_first_existing(paths: list[Path]) -> tuple[Path | None, list[dict[str, str]]]:
    for path in paths:
        rows = read_csv(path)
        if rows:
            return path, rows
    return None, []


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows([{k: r.get(k, "") for k in fieldnames} for r in rows])


def apply_b_result(base_row: dict[str, str], b: dict[str, str]) -> dict[str, str]:
    row = dict(base_row)
    result = b.get("laneB_result", "")
    evidence = b.get("evidence_level", "")
    can_fusion = b.get("can_enter_fusion", "").lower() == "yes"
    row["B_status"] = result or row.get("B_status", "")
    row["verification_level"] = evidence or row.get("verification_level", "")
    row["answer_pairing_status"] = b.get("answer_status", row.get("answer_pairing_status", ""))
    row["rubric_pairing_status"] = b.get("rubric_status", row.get("rubric_pairing_status", ""))
    row["visual_status"] = b.get("visual_status", row.get("visual_status", ""))
    row["student稿_permission"] = "NO_STUDENT_DRAFT"

    note = b.get("notes", "") or b.get("blocker_reason", "")
    if result == "B_TARGET_CONFIRMED" and can_fusion:
        row["fusion_status"] = "confirmed_for_evidence_fusion_pending_formal_lock_batch03"
        row["phase04_level"] = "L3_A_PLUS_B_TARGET_CONFIRMED"
        row["blocker_reason"] = "Batch03 Lane B confirmed for evidence fusion only; no student draft"
        row["gap_priority"] = "P0_DONE_INTERNAL_ONLY"
        row["gap_action"] = "can enter evidence fusion pool; not student稿"
    elif result == "B_TARGET_SCOPE_OUT":
        row["fusion_status"] = "blocked_scope_out_after_batch03"
        row["phase04_level"] = "L0_BLOCKED"
        row["blocker_reason"] = b.get("blocker_reason", "scope_out_after_batch03")
        row["gap_priority"] = "P0_BOUNDARY_CLOSED"
        row["gap_action"] = "scope-out boundary recorded; exclude from fusion"
    elif result in {"B_TARGET_BLOCKED", "B_TARGET_NEEDS_VISUAL", "B_TARGET_CONFLICT"}:
        row["fusion_status"] = "blocked_after_batch03_laneB"
        row["phase04_level"] = "L0_BLOCKED"
        row["blocker_reason"] = b.get("blocker_reason", result)
        row["gap_priority"] = "P0_BLOCKED_BY_B"
        row["gap_action"] = "repair source/visual/conflict before fusion"
    else:
        row["fusion_status"] = "pending_batch03_merge_unrecognized"
        row["phase04_level"] = row.get("phase04_level", "")
        row["blocker_reason"] = f"unrecognized_batch03_result={result}; {note}"
    if note:
        row["excerpt"] = (row.get("excerpt", "")[:700] + " || Batch03 LaneB note: " + note)[:1200]
    return row


def main() -> None:
    base_rows = read_csv(BASE)
    if not base_rows:
        raise SystemExit(f"missing base control table: {BASE}")

    subjective_path, subjective_rows = read_first_existing(SUBJECTIVE_B_CANDIDATES)
    choice_path, choice_rows = read_first_existing(CHOICE_B_CANDIDATES)
    b_rows = subjective_rows + choice_rows
    if not b_rows:
        raise SystemExit("No Batch03 Lane B result CSVs found yet.")

    b_by_id = {r["target_id"]: r for r in b_rows if r.get("target_id")}
    a_precheck = {r.get("target_id"): r for r in (read_csv(SUBJECTIVE_A) + read_csv(CHOICE_A)) if r.get("target_id")}

    merged = []
    recon = []
    for row in base_rows:
        qid = row["canonical_question_id"]
        if qid in b_by_id:
            before = dict(row)
            row = apply_b_result(row, b_by_id[qid])
            a = a_precheck.get(qid, {})
            recon.append(
                {
                    "target_id": qid,
                    "suite_id": row.get("suite_id", ""),
                    "qno": row.get("original_qno", ""),
                    "question_type": row.get("question_type", ""),
                    "codexA_precheck": a.get("codexA_precheck_result") or a.get("codexA_choice_precheck_result", ""),
                    "laneB_result": b_by_id[qid].get("laneB_result", ""),
                    "before_phase04_level": before.get("phase04_level", ""),
                    "after_phase04_level": row.get("phase04_level", ""),
                    "can_enter_student_draft": row.get("student稿_permission", ""),
                    "notes": b_by_id[qid].get("notes", "") or b_by_id[qid].get("blocker_reason", ""),
                }
            )
        merged.append(row)

    fields = list(base_rows[0].keys())
    write_csv(OUT, merged, fields)
    recon_fields = [
        "target_id",
        "suite_id",
        "qno",
        "question_type",
        "codexA_precheck",
        "laneB_result",
        "before_phase04_level",
        "after_phase04_level",
        "can_enter_student_draft",
        "notes",
    ]
    write_csv(OUT_RECON_CSV, recon, recon_fields)

    level_counts = Counter(r["phase04_level"] for r in merged)
    b_counts = Counter(r["laneB_result"] for r in b_rows)
    lines = [
        "# Phase04 Batch03 Codex A / Lane B Reconciliation",
        "",
        "Status: `BATCH03_MERGED_NO_STUDENT_DRAFT`.",
        "",
        f"- subjective_source: `{subjective_path.relative_to(ROOT) if subjective_path else 'missing'}`",
        f"- choice_source: `{choice_path.relative_to(ROOT) if choice_path else 'missing'}`",
        "",
        "## Batch03 Lane B Counts",
        "",
    ]
    lines.extend(f"- {k}: {v}" for k, v in b_counts.items())
    lines.extend(["", "## Control Counts After Batch03", ""])
    lines.extend(f"- {k}: {v}" for k, v in level_counts.items())
    lines.extend(["", "## Merged Rows", ""])
    for r in recon:
        lines.append(
            f"- `{r['target_id']}` | {r['question_type']} | {r['codexA_precheck']} -> {r['laneB_result']} | {r['before_phase04_level']} -> {r['after_phase04_level']} | {r['notes'][:220]}"
        )
    lines.extend(
        [
            "",
            "## Gate Note",
            "",
            "- This merge is evidence-control only.",
            "- `student稿_permission` remains `NO_STUDENT_DRAFT` for all rows.",
            "- GPT-5.5 Pro must review the Batch03 packet before any further promotion.",
        ]
    )
    OUT_RECON_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
