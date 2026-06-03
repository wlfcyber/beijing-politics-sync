#!/usr/bin/env python3
"""Apply source-checked rubric atom patches required by expansion adjudication."""

from __future__ import annotations

import csv
import shutil
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
TARGET = ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv"
PLAN = ROOT / "04_merge_audit" / "claude_cowork_all_question_completion_20260519" / "codex_source_check_corrected_rubric_atom_plan.csv"
OUT_DIR = ROOT / "04_merge_audit" / "codebook_expansion_atom_patch_20260519"

PATCH_QIDS = {
    "CC0011_2024_丰台_二模_17",
    "CC0019_2024_朝阳_一模_19",
    "CC0061_2024_西城_一模_18",
    "CC0254_2026_丰台_二模_18",
    "RECOVER_2026_房山_一模_17_1",
}

EVIDENCE_TYPE_BY_QID = {
    "CC0011_2024_丰台_二模_17": "evaluation_standard",
    "CC0019_2024_朝阳_一模_19": "marking_rubric",
    "CC0061_2024_西城_一模_18": "marking_rubric",
    "CC0254_2026_丰台_二模_18": "marking_rubric",
    "RECOVER_2026_房山_一模_17_1": "evaluation_standard",
}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def reward_description(phrase: str, scoring: str) -> str:
    return f"奖励：{phrase}（{scoring}）" if scoring else f"奖励：{phrase}"


def expression_rewarded(phrase: str, scoring: str) -> str:
    if scoring:
        return f"{phrase}；给分逻辑：{scoring}"
    return phrase


def value_expression(phrase: str) -> str:
    hits = []
    for token in ["核心价值观", "公平正义", "生态环境", "司法温暖", "社会福祉", "市场秩序", "诚信", "孝老敬亲", "法治与德治"]:
        if token in phrase:
            hits.append(token)
    return "|".join(hits)


def can_write_without_material(kmv: str, status: str) -> str:
    if status == "alternative_not_cumulative":
        return "uncertain"
    if kmv == "value":
        return "uncertain"
    return "no"


def uncertainty_for(qid: str, atom_id: str, status: str) -> str:
    parts = ["codex_source_checked_patch_20260519", f"patch_status={status}"]
    if atom_id.startswith("PATCH_CC0061_18_1") or atom_id.startswith("PATCH_CC0061_18_2"):
        parts.append("procedure_micro_item_not_core_code_evidence")
    if status == "alternative_not_cumulative":
        parts.append("alternative_explanation_not_cumulative_score")
    if qid == "CC0254_2026_丰台_二模_18":
        parts.append("replaces_wrong_student_problem_atoms")
    return "; ".join(parts)


def build_patch_rows(fields: list[str]) -> dict[str, list[dict[str, str]]]:
    _, plan_rows = read_csv(PLAN)
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in plan_rows:
        qid = row["question_id"]
        atom_id = row["proposed_rubric_atom_id"]
        phrase = row["rubric_or_answer_phrase"]
        scoring = row.get("point_value_or_scoring_logic", "")
        out = {field: "" for field in fields}
        out.update(
            {
                "rubric_atom_id": atom_id,
                "question_id": qid,
                "rubric_or_answer_phrase": phrase,
                "evidence_type": EVIDENCE_TYPE_BY_QID.get(qid, "marking_rubric"),
                "evidence_level": "formal",
                "plain_reward_description": reward_description(phrase, scoring),
                "related_material_atom_ids": row.get("related_material_atom_ids", ""),
                "what_expression_is_rewarded": expression_rewarded(phrase, scoring),
                "what_judgment_student_must_make_before_writing": row.get("what_judgment_student_must_make_before_writing", ""),
                "legal_knowledge_or_rule_if_explicit": row.get("legal_knowledge_or_rule_if_explicit", ""),
                "value_expression_if_explicit": value_expression(phrase),
                "knowledge_material_value_type": row.get("knowledge_material_value_type", ""),
                "can_be_written_without_material": can_write_without_material(row.get("knowledge_material_value_type", ""), row.get("patch_status", "")),
                "source_locator": row.get("source_locator", ""),
                "uncertainty": uncertainty_for(qid, atom_id, row.get("patch_status", "")),
            }
        )
        grouped[qid].append(out)
    return grouped


def annotate_cc0143(rows: list[dict[str, str]]) -> int:
    changed = 0
    for row in rows:
        if row.get("question_id") != "CC0143_2025_朝阳_一模_19":
            continue
        atom_id = row.get("rubric_atom_id", "")
        try:
            idx = int(atom_id.rsplit("_", 1)[1])
        except ValueError:
            continue
        if idx >= 11:
            note = "teaching_reflection_not_scoring_atom_not_core_code_support"
            existing = row.get("uncertainty", "")
            if note not in existing:
                row["uncertainty"] = f"{existing}; {note}" if existing else note
                changed += 1
    return changed


def main() -> None:
    fields, rows = read_csv(TARGET)
    patch_by_qid = build_patch_rows(fields)
    original_counts = Counter(row["question_id"] for row in rows)

    backup_dir = ROOT / "tool_outputs" / f"pre_codebook_expansion_atom_patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(TARGET, backup_dir / TARGET.name)

    output: list[dict[str, str]] = []
    inserted = set()
    removed_counts = Counter()
    for row in rows:
        qid = row["question_id"]
        if qid in PATCH_QIDS:
            removed_counts[qid] += 1
            if qid not in inserted:
                output.extend(patch_by_qid[qid])
                inserted.add(qid)
            continue
        output.append(row)
    for qid, patch_rows in patch_by_qid.items():
        if qid not in inserted:
            output.extend(patch_rows)
            inserted.add(qid)

    cc0143_annotated = annotate_cc0143(output)
    write_csv(TARGET, fields, output)

    patch_report_fields = ["question_id", "original_atoms_removed", "patch_atoms_added", "original_count_before_patch"]
    patch_report_rows = []
    for qid in sorted(PATCH_QIDS):
        patch_report_rows.append(
            {
                "question_id": qid,
                "original_atoms_removed": str(removed_counts[qid]),
                "patch_atoms_added": str(len(patch_by_qid.get(qid, []))),
                "original_count_before_patch": str(original_counts[qid]),
            }
        )
    write_csv(OUT_DIR / "p0_atom_patch_application_report.csv", patch_report_fields, patch_report_rows)

    md = [
        "# P0 Atom Patch Application Report",
        "",
        f"- target: `{TARGET}`",
        f"- backup: `{backup_dir / TARGET.name}`",
        "- patch source: `codex_source_check_corrected_rubric_atom_plan.csv`",
        "",
        "## Applied Replacements",
        "",
        "| question_id | removed | added | note |",
        "|---|---:|---:|---|",
    ]
    notes = {
        "CC0011_2024_丰台_二模_17": "single collapsed atom replaced by 4 source-checked formal atoms",
        "CC0019_2024_朝阳_一模_19": "single collapsed atom replaced by 6 source-checked formal atoms",
        "CC0061_2024_西城_一模_18": "3 original mixed atoms replaced by 6 split atoms; 18(1)(2) marked procedure micro-items",
        "CC0254_2026_丰台_二模_18": "8 wrong student-problem/teaching-suggestion atoms replaced by 8 scoring atoms",
        "RECOVER_2026_房山_一模_17_1": "3 original atoms replaced by 4 atoms with 1+2 alternative logic",
    }
    for row in patch_report_rows:
        md.append(
            f"| {row['question_id']} | {row['original_atoms_removed']} | {row['patch_atoms_added']} | {notes[row['question_id']]} |"
        )
    md.extend(
        [
            "",
            "## Additional Annotation",
            "",
            f"- CC0143 teaching-reflection atoms annotated as non-scoring/non-core support: {cc0143_annotated}",
            "",
            "## Gate",
            "",
            "P0 atom layer is now patched for expansion adjudication. Codebook expansion and pressure-test rerun may proceed, but framework_v2/final baodian remain blocked.",
            "",
        ]
    )
    (OUT_DIR / "p0_atom_patch_application_report.md").write_text("\n".join(md), encoding="utf-8")

    print(f"Backed up target to {backup_dir / TARGET.name}")
    print(f"Patched row count: {len(rows)} -> {len(output)}")
    print(f"CC0143 teaching-reflection annotations: {cc0143_annotated}")


if __name__ == "__main__":
    main()
