#!/usr/bin/env python3
"""Write local adjudication for the four v1.1 FAIL rows."""

from __future__ import annotations

import csv
import shutil
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
OUT_DIR = ROOT / "10_framework_validation" / "fail4_source_adjudication_20260519"
QUESTIONS = ROOT / "04_merge_audit" / "merged_subjective_law_questions.csv"
MATERIALS = ROOT / "04_merge_audit" / "merged_material_atoms_subjective.csv"
RUBRICS = ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv"
PRESSURE = ROOT / "10_framework_validation" / "framework_v1_1_question_by_question_sentence_pressure_test_20260519.csv"

FAIL_IDS = [
    "CC0143_2025_朝阳_一模_19",
    "CC0276_2026_房山_二模_17",
    "RECOVER_2026_西城_二模_18_2",
    "RECOVER_2026_西城_二模_18_3",
]

LOCAL_DECISIONS = {
    "CC0143_2025_朝阳_一模_19": {
        "local_decision": "candidate_core_pending_dual_model",
        "proposed_bucket": "consumer_contract_fraud_and_punitive_compensation",
        "reason": "formal marking_report gives detailed scoring: contract formation, hidden bundled fee facts, fraud/true intention, revocable or invalid contract, Consumers' Rights and Interests Protection Law, threefold compensation, consumer/platform-order value. This is not IP/unfair-competition, but it is a strong selected-compulsory-2 consumer/contract case. It should not remain FAIL; it should be sent to GPT/Claude for a targeted codebook supplement or merged into CODE_COWORK_004/007.",
        "next_action": "send targeted adjudication to GPT-5.5 Pro and Claude Opus/Cowork; do not promote locally before dual-model agreement because current expansion round did not place it.",
        "core_use_now": "no",
    },
    "CC0276_2026_房山_二模_17": {
        "local_decision": "boundary_non_core_keep_audit",
        "proposed_bucket": "foreign_related_rule_of_law_governance_boundary",
        "reason": "formal scoring rewards涉外法律法规体系、涉外司法实践、公正司法、多元纠纷解决平台、涉外海事纠纷化解、大国责任. The answer mechanism is law-governance/涉外法治建设, not private-law rights-duty-rule conversion. It risks必修三化 if used as selected-compulsory-2 core.",
        "next_action": "keep in boundary/open audit, not in core framework; if user wants broad法治题 appendix, list separately.",
        "core_use_now": "no",
    },
    "RECOVER_2026_西城_二模_18_2": {
        "local_decision": "open_container_pending_dual_model",
        "proposed_bucket": "ai_responsibility_boundary_industry_development",
        "reason": "formal rubric has legal signals: responsibility boundary, legal expectation, rights-obligations balance, user rights and innovation balance. But scoring is mainly industry-development impact and法治营商环境. It can be an AI responsibility-boundary open container, not yet a core node.",
        "next_action": "send with CC0143 in targeted adjudication; ask models whether it should revise CODE_COWORK_002 or remain open container.",
        "core_use_now": "no",
    },
    "RECOVER_2026_西城_二模_18_3": {
        "local_decision": "exclude_from_xuanbier_core",
        "proposed_bucket": "digital_governance_rule_of_law_boundary",
        "reason": "formal rubric rewards数字治理规则、法律实施机制、治理法治化、示范指引、依法行政、国家治理能力现代化. This is overwhelmingly法治治理/必修三综合, not a selected-compulsory-2 legal-life scoring mechanism.",
        "next_action": "quarantine as boundary/non-core; do not send as core framework evidence unless user widens scope to综合法治.",
        "core_use_now": "no",
    },
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def join_rows(rows: list[dict[str, str]], key: str, limit: int = 6) -> str:
    parts = []
    for row in rows[:limit]:
        value = row.get(key, "")
        if value:
            parts.append(value.replace("\n", " ")[:320])
    return " || ".join(parts)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    questions = {row["question_id"]: row for row in read_csv(QUESTIONS)}
    pressure = {row["question_id"]: row for row in read_csv(PRESSURE)}
    mats: dict[str, list[dict[str, str]]] = {qid: [] for qid in FAIL_IDS}
    rubs: dict[str, list[dict[str, str]]] = {qid: [] for qid in FAIL_IDS}
    for row in read_csv(MATERIALS):
        if row["question_id"] in mats:
            mats[row["question_id"]].append(row)
    for row in read_csv(RUBRICS):
        if row["question_id"] in rubs:
            rubs[row["question_id"]].append(row)

    fields = [
        "question_id",
        "year",
        "district",
        "exam_stage",
        "question_no",
        "sub_question_no",
        "evidence_level",
        "module_boundary_risk",
        "ask_text",
        "pressure_status",
        "expansion_status",
        "local_decision",
        "proposed_bucket",
        "core_use_now",
        "reason",
        "next_action",
        "material_atoms_summary",
        "rubric_atoms_summary",
    ]
    rows = []
    for qid in FAIL_IDS:
        q = questions[qid]
        p = pressure[qid]
        d = LOCAL_DECISIONS[qid]
        rows.append(
            {
                "question_id": qid,
                "year": q.get("year", ""),
                "district": q.get("district", ""),
                "exam_stage": q.get("exam_stage", ""),
                "question_no": q.get("question_no", ""),
                "sub_question_no": q.get("sub_question_no", ""),
                "evidence_level": q.get("evidence_level", ""),
                "module_boundary_risk": q.get("module_boundary_risk", ""),
                "ask_text": q.get("ask_text", ""),
                "pressure_status": p.get("pass_status", ""),
                "expansion_status": p.get("expansion_status", ""),
                "local_decision": d["local_decision"],
                "proposed_bucket": d["proposed_bucket"],
                "core_use_now": d["core_use_now"],
                "reason": d["reason"],
                "next_action": d["next_action"],
                "material_atoms_summary": join_rows(mats[qid], "material_phrase", 8),
                "rubric_atoms_summary": join_rows(rubs[qid], "rubric_or_answer_phrase", 8),
            }
        )

    write_csv(OUT_DIR / "fail4_source_adjudication_20260519.csv", fields, rows)

    # Build a compact model packet folder.
    packet_dir = ROOT / "05_reasoner_packets" / "fail4_targeted_adjudication_20260519"
    packet_dir.mkdir(parents=True, exist_ok=True)
    write_csv(packet_dir / "fail4_source_adjudication_20260519.csv", fields, rows)
    for src in [QUESTIONS, MATERIALS, RUBRICS, PRESSURE, ROOT / "08_codebook" / "provisional_codebook_v1_1_after_cc0364_split_20260519.csv"]:
        shutil.copy2(src, packet_dir / src.name)

    md = [
        "# FAIL4 Source Adjudication",
        "",
        "These are local source decisions after the v1.1 sentence-level pressure test. They are not final framework promotions.",
        "",
        "## Summary",
        "",
        "| question_id | local_decision | proposed_bucket | core_use_now |",
        "|---|---|---|---|",
    ]
    for row in rows:
        md.append(
            f"| `{row['question_id']}` | {row['local_decision']} | {row['proposed_bucket']} | {row['core_use_now']} |"
        )
    md.extend(["", "## Per-Question Decisions", ""])
    for row in rows:
        md.extend(
            [
                f"### {row['question_id']}",
                "",
                f"- evidence_level: {row['evidence_level']}",
                f"- module_boundary_risk: {row['module_boundary_risk']}",
                f"- ask: {row['ask_text']}",
                f"- local_decision: {row['local_decision']}",
                f"- proposed_bucket: {row['proposed_bucket']}",
                f"- reason: {row['reason']}",
                f"- next_action: {row['next_action']}",
                "",
            ]
        )
    md.extend(
        [
            "## Gate",
            "",
            "`CC0143` and `RECOVER_2026_西城_二模_18_2` need targeted dual-model adjudication before any codebook/core change. `CC0276` and `RECOVER_2026_西城_二模_18_3` should remain boundary/non-core unless the user widens the project scope.",
            "",
        ]
    )
    (OUT_DIR / "fail4_source_adjudication_20260519.md").write_text("\n".join(md), encoding="utf-8")
    (packet_dir / "FAIL4_TARGETED_ADJUDICATION_README.md").write_text("\n".join(md), encoding="utf-8")

    print(f"Wrote {OUT_DIR / 'fail4_source_adjudication_20260519.csv'}")
    print(f"Wrote packet dir {packet_dir}")


if __name__ == "__main__":
    main()
