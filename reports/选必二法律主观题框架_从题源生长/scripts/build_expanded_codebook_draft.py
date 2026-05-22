#!/usr/bin/env python3
"""Build an expansion draft codebook from dual-model adjudication."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
BASE_CODEBOOK = ROOT / "08_codebook" / "provisional_codebook_v0.csv"
GPT_CSV = ROOT / "06_open_observations" / "codebook_expansion_after_cowork_sourcecheck_20260519" / "gpt55pro_codebook_expansion_after_cowork_sourcecheck_20260519.csv"
OUT_CODEBOOK = ROOT / "08_codebook" / "provisional_codebook_v1_expansion_draft_20260519.csv"
OUT_MD = ROOT / "08_codebook" / "provisional_codebook_v1_expansion_draft_20260519.md"
OUT_MAP = ROOT / "08_codebook" / "codebook_v1_expansion_source_evidence_map_20260519.csv"
OUT_OPEN = ROOT / "08_codebook" / "transfer_open_container_after_expansion_20260519.csv"
OUT_RISKS = ROOT / "08_codebook" / "codebook_v1_expansion_risks_20260519.md"


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


def append_unique(existing: str, extra: str) -> str:
    values = []
    seen = set()
    for part in (existing or "").split("|") + (extra or "").split("|"):
        value = part.strip()
        if value and value not in seen:
            values.append(value)
            seen.add(value)
    return "|".join(values)


def gpt_decisions() -> dict[str, dict[str, str]]:
    _, rows = read_csv(GPT_CSV)
    return {r["expansion_decision_id"]: r for r in rows}


def merge_decision(row: dict[str, str], dec: dict[str, str], source_id: str, note: str) -> None:
    row["source_observation_ids"] = append_unique(row.get("source_observation_ids", ""), source_id)
    row["supporting_question_ids"] = append_unique(row.get("supporting_question_ids", ""), dec.get("supporting_question_ids", ""))
    row["supporting_rubric_atom_ids"] = append_unique(row.get("supporting_rubric_atom_ids", ""), dec.get("supporting_rubric_atom_ids_or_patch_atom_ids", ""))
    row["supporting_material_atom_ids"] = append_unique(row.get("supporting_material_atom_ids", ""), dec.get("supporting_material_atom_ids", ""))
    row["reason"] = f"{row.get('reason','')} | expansion_20260519: {note}".strip(" |")
    row["status"] = "provisional_expanded"


def main() -> None:
    fields, base_rows = read_csv(BASE_CODEBOOK)
    dec = gpt_decisions()
    rows = [dict(r) for r in base_rows]
    by_code = {r["code_id"]: r for r in rows}

    merge_decision(
        by_code["CODE_COWORK_001"],
        dec["DEC_002"],
        "EXP_CMP_002",
        "add table/completion law-fact-value cell subtype; still governed by independent-cell scoring",
    )
    merge_decision(
        by_code["CODE_COWORK_002"],
        dec["DEC_003"],
        "EXP_CMP_003",
        "add principle/institution/typical-case significance branch; RECOVER_2026_西城_二模_18_3 remains open container",
    )
    merge_decision(
        by_code["CODE_COWORK_007"],
        dec["DEC_004"],
        "EXP_CMP_004",
        "split into issue-spotting/compliance and procedure-remedy/entity-request subpatterns before pressure test",
    )

    for code in ["CODE_COWORK_004", "CODE_COWORK_006"]:
        trimmed = dict(dec["DEC_005"])
        # CC0364 is still source_check_needed; keep it out of core support until split.
        for key in ["supporting_question_ids", "supporting_rubric_atom_ids_or_patch_atom_ids", "supporting_material_atom_ids"]:
            parts = [p for p in trimmed.get(key, "").split("|") if p and "CC0364_2026_通州_期末_19_1" not in p and "R_CC0364_2026_通州_期末_19_1" not in p and "M_CC0364_2026_通州_期末_19_1" not in p]
            trimmed[key] = "|".join(parts)
        merge_decision(
            by_code[code],
            trimmed,
            "EXP_CMP_005",
            "add limited multi-actor/multi-request separate chain; CC0364 kept pending until atom split",
        )

    new_code = {field: "" for field in fields}
    d = dec["DEC_001"]
    new_code.update(
        {
            "code_id": "CODE_COWORK_008",
            "temporary_label": "知识产权/不正当竞争司法保护四步链",
            "plain_description": "面对知识产权、不正当竞争、恶意诉讼、惩罚性赔偿、调解或驳回等创新保护案例，学生先判断行为性质，再援引规则，再落到司法手段与创新/竞争秩序意义。该 code 只使用裁剪后的六题核心支撑。",
            "source_observation_ids": "EXP_CMP_001|GPT_DEC_001|CLAUDE_EXP_DEC_001_TRIMMED_BY_LOCAL_ADJUDICATION",
            "supporting_question_ids": d["supporting_question_ids"],
            "supporting_rubric_atom_ids": d["supporting_rubric_atom_ids_or_patch_atom_ids"],
            "supporting_material_atom_ids": d["supporting_material_atom_ids"],
            "evidence_level_summary": "formal; dual-model accepted; support set trimmed by GPT+Codex source check; CC0103 and CC0131 share base case and should be downweighted in frequency claims",
            "ask_types_supported": "说明|论证|意义|评析",
            "what_student_must_judge": d["what_student_must_judge"],
            "material_trigger_pattern": d["material_trigger_pattern"],
            "legal_knowledge_or_rule_pattern": d["legal_knowledge_or_rule_pattern"],
            "rubric_reward_pattern": d["rubric_reward_pattern"],
            "full_score_sentence_pattern": d["full_score_sentence_pattern"],
            "must_have_keywords": "知识产权|不正当竞争|惩罚性赔偿|调解|停止侵害|公平竞争秩序|创新主体权益|司法示范",
            "module_boundary_risk": d["module_boundary_risk"],
            "risk_of_empty_value_talk": d["risk_of_empty_value_talk"],
            "risk_of_legal_exam_overanalysis": d["risk_of_legal_exam_overanalysis"],
            "transfer_potential": "high for IP/unfair-competition judicial-protection cases; not for consumer fraud or broad AI governance",
            "counterexamples": "CC0143_2025_朝阳_一模_19 is consumer fraud/contract/consumer-rights; RECOVER_2026_西城_二模_18_2 is AI rights-boundary open container",
            "status": "provisional_expanded",
            "reason": "Dual real-model agreement after Cowork and Codex source check; GPT/local adjudication trims support set.",
        }
    )
    rows.append(new_code)

    # Open containers and rejects from GPT decisions, kept out of core codebook.
    open_decision_ids = ["DEC_006", "DEC_007", "DEC_008", "DEC_009", "DEC_010", "DEC_011", "DEC_013", "DEC_014", "DEC_015", "DEC_016"]
    open_fields = [
        "container_id",
        "source_decision_id",
        "status",
        "question_ids",
        "rubric_atom_ids",
        "material_atom_ids",
        "reason",
        "core_codebook_use",
    ]
    open_rows = []
    for decision_id in open_decision_ids:
        drow = dec[decision_id]
        status = "reject_core" if drow["decision"] == "reject" else "open_container_only"
        open_rows.append(
            {
                "container_id": drow["new_or_revised_code_label"],
                "source_decision_id": decision_id,
                "status": status,
                "question_ids": drow["supporting_question_ids"],
                "rubric_atom_ids": drow["supporting_rubric_atom_ids_or_patch_atom_ids"],
                "material_atom_ids": drow["supporting_material_atom_ids"],
                "reason": drow["reason"],
                "core_codebook_use": "no",
            }
        )

    write_csv(OUT_CODEBOOK, fields, rows)
    write_csv(OUT_MAP, fields, rows)
    write_csv(OUT_OPEN, open_fields, open_rows)

    md = [
        "# Provisional Codebook v1 Expansion Draft",
        "",
        "This is not a final framework. It is a codebook expansion draft after GPT-5.5 Pro + Claude Opus/Cowork cross-validation and P0 atom patching.",
        "",
        f"- code rows: {len(rows)}",
        "- new core candidate added: CODE_COWORK_008",
        "- existing codes revised: CODE_COWORK_001, CODE_COWORK_002, CODE_COWORK_004, CODE_COWORK_006, CODE_COWORK_007",
        "- open/reject rows are stored separately and do not support core nodes.",
        "",
        "## Code Rows",
        "",
    ]
    for r in rows:
        q_count = len([x for x in r["supporting_question_ids"].split("|") if x])
        md.extend(
            [
                f"### {r['code_id']} — {r['temporary_label']}",
                "",
                f"- status: {r['status']}",
                f"- supporting_question_count: {q_count}",
                f"- supporting_question_ids: {r['supporting_question_ids']}",
                f"- key judgment: {r['what_student_must_judge']}",
                f"- material trigger: {r['material_trigger_pattern']}",
                f"- sentence pattern: {r['full_score_sentence_pattern']}",
                f"- risk: empty_value={r['risk_of_empty_value_talk']}; legal_exam={r['risk_of_legal_exam_overanalysis']}; boundary={r['module_boundary_risk']}",
                "",
            ]
        )
    OUT_MD.write_text("\n".join(md), encoding="utf-8")

    risks = [
        "# Codebook v1 Expansion Risks",
        "",
        "- `CODE_COWORK_008` is accepted only with the trimmed six-question support set; do not restore `CC0143` or `RECOVER_2026_西城_二模_18_2` as core support.",
        "- `CODE_COWORK_007` must be pressure-tested as two subpatterns, not as one over-broad remedy bucket.",
        "- `CODE_COWORK_002` can absorb principle/institution/case significance, but governance-heavy digital-modernization expressions remain open container.",
        "- `CC0364` cannot be counted as strong 004/006 support until its giant atom is split.",
        "- Reference-only rows remain excluded from core support.",
        "- This draft authorizes pressure testing, not framework_v2 or final handbook generation.",
        "",
    ]
    OUT_RISKS.write_text("\n".join(risks), encoding="utf-8")

    print(f"Wrote {OUT_CODEBOOK}")
    print(f"Rows: {len(rows)}")
    print(f"Open/reject rows: {len(open_rows)}")


if __name__ == "__main__":
    main()
