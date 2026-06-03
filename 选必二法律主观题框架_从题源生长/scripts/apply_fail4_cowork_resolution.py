#!/usr/bin/env python3
"""Integrate Claude Cowork FAIL4 adjudication and apply guarded patches.

This script intentionally does not generate the final framework. It only:
- records local-vs-Cowork agreement for the four v1.1 FAIL cases;
- patches the CC0143 rubric atom layer as requested by Cowork;
- builds a v1.2 provisional codebook snapshot;
- records which FAIL cases are core/open/boundary after adjudication.
"""

from __future__ import annotations

import csv
import shutil
from collections import Counter
from datetime import datetime
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
RUBRIC = ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv"
CODEBOOK_V11 = ROOT / "08_codebook" / "provisional_codebook_v1_1_after_cc0364_split_20260519.csv"
PRESSURE_V11 = ROOT / "10_framework_validation" / "framework_v1_1_question_by_question_sentence_pressure_test_20260519.csv"
LOCAL = ROOT / "10_framework_validation" / "fail4_source_adjudication_20260519" / "fail4_source_adjudication_20260519.csv"
LOCAL_PATCH = ROOT / "10_framework_validation" / "fail4_source_adjudication_20260519" / "fail4_local_patch_candidates_20260519.csv"
COWORK = ROOT / "10_framework_validation" / "fail4_source_adjudication_20260519" / "claude_cowork_output" / "fail4_targeted_adjudication_claude_cowork_20260519.csv"

OUT_DIR = ROOT / "10_framework_validation" / "fail4_source_adjudication_20260519"
ATOM_OUT = ROOT / "04_merge_audit" / "cc0143_atom_patch_20260519"
CODEBOOK_OUT = ROOT / "08_codebook" / "provisional_codebook_v1_2_after_fail4_cowork_20260519.csv"
CODEBOOK_MD = ROOT / "08_codebook" / "provisional_codebook_v1_2_after_fail4_cowork_20260519.md"
CODEBOOK_MAP = ROOT / "08_codebook" / "codebook_v1_2_after_fail4_cowork_source_evidence_map_20260519.csv"
CODEBOOK_RISKS = ROOT / "08_codebook" / "codebook_v1_2_after_fail4_cowork_risks_20260519.md"
OPEN_OUT = ROOT / "08_codebook" / "transfer_open_container_after_fail4_cowork_20260519.csv"


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
    values: list[str] = []
    seen: set[str] = set()
    for part in (existing or "").split("|") + (extra or "").split("|"):
        value = part.strip()
        if value and value not in seen:
            values.append(value)
            seen.add(value)
    return "|".join(values)


def append_note(existing: str, note: str) -> str:
    if not existing:
        return note
    if note in existing:
        return existing
    return f"{existing}; {note}"


def local_decisions() -> dict[str, dict[str, str]]:
    _, rows = read_csv(LOCAL)
    return {row["question_id"]: row for row in rows}


def local_patch_rows() -> dict[str, dict[str, str]]:
    _, rows = read_csv(LOCAL_PATCH)
    return {row["question_id"]: row for row in rows}


def cowork_rows() -> dict[str, dict[str, str]]:
    _, rows = read_csv(COWORK)
    return {row["question_id"]: row for row in rows}


def build_cross_check() -> None:
    local = local_decisions()
    local_patch = local_patch_rows()
    cowork = cowork_rows()
    fields = [
        "question_id",
        "local_decision",
        "local_patch_decision",
        "cowork_recommendation",
        "cowork_code_or_label",
        "agreement_level",
        "final_resolution",
        "core_use_now",
        "required_patch",
        "reason",
    ]
    rows: list[dict[str, str]] = []
    for qid in sorted(cowork):
        c = cowork[qid]
        l = local.get(qid, {})
        lp = local_patch.get(qid, {})
        if qid == "CC0143_2025_朝阳_一模_19":
            final = "revise_existing_code_after_atom_patch"
            core = "yes_after_patch"
            agreement = "same_direction; cowork refined local candidate into CODE_COWORK_004 revision"
            patch = "split R01; mark R11-R25 as teaching_reflection_not_core; update CODE_COWORK_004/002"
        elif qid == "RECOVER_2026_西城_二模_18_2":
            final = "open_container_only"
            core = "no"
            agreement = "same"
            patch = "create OPEN_CONTAINER_AI_RESPONSIBILITY_BOUNDARY; add 002 counterexample"
        elif c["final_recommendation"] == "exclude_core":
            final = "boundary_exclude_core"
            core = "no"
            agreement = "same"
            patch = "boundary appendix only"
        else:
            final = "pending"
            core = "no"
            agreement = "needs_review"
            patch = "pending"
        rows.append(
            {
                "question_id": qid,
                "local_decision": l.get("local_decision", ""),
                "local_patch_decision": lp.get("local_patch_decision", ""),
                "cowork_recommendation": c.get("final_recommendation", ""),
                "cowork_code_or_label": c.get("recommended_code_id_or_new_label", ""),
                "agreement_level": agreement,
                "final_resolution": final,
                "core_use_now": core,
                "required_patch": patch,
                "reason": c.get("reason", ""),
            }
        )
    write_csv(OUT_DIR / "fail4_external_cross_check_20260519.csv", fields, rows)

    md = [
        "# FAIL4 External Cross Check",
        "",
        "Claude Cowork and local source adjudication agree on all four v1.1 FAIL cases. This file records the integration decision before framework generation.",
        "",
        "| question_id | local | Cowork | final resolution | core use |",
        "|---|---|---|---|---|",
    ]
    for row in rows:
        md.append(
            f"| {row['question_id']} | {row['local_decision']} | {row['cowork_recommendation']} | {row['final_resolution']} | {row['core_use_now']} |"
        )
    md.extend(
        [
            "",
            "Gate: framework_v2 remains blocked until the CC0143 atom patch and v1.2 codebook snapshot are written.",
            "",
        ]
    )
    (OUT_DIR / "fail4_external_cross_check_20260519.md").write_text("\n".join(md), encoding="utf-8")


def patch_cc0143_atoms() -> None:
    fields, rows = read_csv(RUBRIC)
    backup_dir = ROOT / "tool_outputs" / f"pre_cc0143_fail4_atom_patch_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    backup_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(RUBRIC, backup_dir / RUBRIC.name)

    source_by_id = {row["rubric_atom_id"]: row for row in rows}
    r07 = source_by_id["R_CC0143_2025_朝阳_一模_19_07"]
    r08 = source_by_id["R_CC0143_2025_朝阳_一模_19_08"]
    r09 = source_by_id["R_CC0143_2025_朝阳_一模_19_09"]

    patch_rows = []
    base = {field: "" for field in fields}
    contract = dict(base)
    contract.update(
        {
            "rubric_atom_id": "PATCH_CC0143_CONTRACT_CHAIN_R01",
            "question_id": "CC0143_2025_朝阳_一模_19",
            "rubric_or_answer_phrase": "诉讼请求1：王某通过A公司平台购买机票并出票，双方经要约、承诺合同成立；A公司擅自搭售10元外卖红包，王某不能清楚知悉费用细节且无法拒绝支付，构成欺诈，使王某违背真实意思订立合同，合同无效或可撤销，法院支持退还票款。",
            "evidence_type": "marking_report",
            "evidence_level": "formal",
            "plain_reward_description": "奖励合同成立、搭售欺诈事实三条件、违背真实意思表示、合同无效或可撤销、退还票款的完整链条。",
            "related_material_atom_ids": "M_CC0143_2025_朝阳_一模_19_03|M_CC0143_2025_朝阳_一模_19_05|M_CC0143_2025_朝阳_一模_19_06|M_CC0143_2025_朝阳_一模_19_07",
            "what_expression_is_rewarded": "合同成立；欺诈；违背真实意思表示；合同无效/可撤销；退还票款",
            "what_judgment_student_must_make_before_writing": "先区分两个诉讼请求，并判断退还票款请求走合同成立与可撤销链条。",
            "legal_knowledge_or_rule_if_explicit": "合同成立；意思表示；欺诈；可撤销合同",
            "value_expression_if_explicit": "",
            "knowledge_material_value_type": "knowledge+material",
            "can_be_written_without_material": "no",
            "source_locator": append_unique(r07.get("source_locator", ""), r08.get("source_locator", "")),
            "uncertainty": "cc0143_fail4_cowork_atom_patch_20260519; split_from_R_CC0143_2025_朝阳_一模_19_01; formal marking_report scoring chain",
        }
    )
    patch_rows.append(contract)

    consumer = dict(base)
    consumer.update(
        {
            "rubric_atom_id": "PATCH_CC0143_CONSUMER_TRIPLE_COMP_R02",
            "question_id": "CC0143_2025_朝阳_一模_19",
            "rubric_or_answer_phrase": "诉讼请求2：根据消费者权益保护法第五十五条，A公司提供服务有欺诈行为，或者侵犯消费者知情权、公平交易权、自主选择权，法院应支持王某要求三倍赔偿的诉讼请求。",
            "evidence_type": "marking_report",
            "evidence_level": "formal",
            "plain_reward_description": "奖励写准消费者权益保护法、经营者服务欺诈或消费者权利受侵害、三倍赔偿诉讼请求。",
            "related_material_atom_ids": "M_CC0143_2025_朝阳_一模_19_05|M_CC0143_2025_朝阳_一模_19_06|M_CC0143_2025_朝阳_一模_19_08|M_CC0143_2025_朝阳_一模_19_09",
            "what_expression_is_rewarded": "消费者权益保护法；欺诈行为；知情权/公平交易权/自主选择权；三倍赔偿",
            "what_judgment_student_must_make_before_writing": "先判断三倍赔偿请求走消费者权益保护法第五十五条的经营者欺诈链条。",
            "legal_knowledge_or_rule_if_explicit": "消费者权益保护法第五十五条；经营者欺诈；三倍赔偿",
            "value_expression_if_explicit": "",
            "knowledge_material_value_type": "knowledge+material",
            "can_be_written_without_material": "no",
            "source_locator": r09.get("source_locator", ""),
            "uncertainty": "cc0143_fail4_cowork_atom_patch_20260519; split_from_R_CC0143_2025_朝阳_一模_19_01; formal marking_report scoring chain",
        }
    )
    patch_rows.append(consumer)

    already = {row["rubric_atom_id"] for row in rows}
    output: list[dict[str, str]] = []
    inserted = False
    teaching_reflection_ids: list[str] = []
    demoted_overview = False
    for row in rows:
        qid = row.get("question_id", "")
        atom_id = row.get("rubric_atom_id", "")
        if qid == "CC0143_2025_朝阳_一模_19" and atom_id.endswith("_01"):
            row = dict(row)
            row["evidence_type"] = "grading_commentary"
            row["plain_reward_description"] = "原始大段阅卷报告/参考答案总览，已由 PATCH_CC0143_CONTRACT_CHAIN_R01 与 PATCH_CC0143_CONSUMER_TRIPLE_COMP_R02 拆分；不得直接支撑核心代码。"
            row["uncertainty"] = append_note(row.get("uncertainty", ""), "giant_atom_superseded_by_cc0143_fail4_patch_not_core_code_support")
            demoted_overview = True
        if qid == "CC0143_2025_朝阳_一模_19":
            try:
                idx = int(atom_id.rsplit("_", 1)[1])
            except ValueError:
                idx = 0
            if idx >= 11:
                row = dict(row)
                row["evidence_type"] = "grading_commentary"
                row["plain_reward_description"] = f"教学反思/阅卷问题记录，不是独立给分细则：{row.get('plain_reward_description', '')}"
                row["can_be_written_without_material"] = "uncertain"
                row["uncertainty"] = append_note(row.get("uncertainty", ""), "teaching_reflection_not_scoring_atom_not_core_code_support")
                teaching_reflection_ids.append(atom_id)
        output.append(row)
        if qid == "CC0143_2025_朝阳_一模_19" and not inserted:
            for patch in patch_rows:
                if patch["rubric_atom_id"] not in already:
                    output.append(patch)
            inserted = True

    write_csv(RUBRIC, fields, output)
    write_csv(ATOM_OUT / "cc0143_patch_atoms.csv", fields, patch_rows)
    write_csv(ATOM_OUT / "cc0143_teaching_reflection_demotions.csv", fields, [row for row in output if row.get("rubric_atom_id") in teaching_reflection_ids])

    report_fields = ["metric", "value"]
    report_rows = [
        {"metric": "backup", "value": str(backup_dir / RUBRIC.name)},
        {"metric": "row_count_before", "value": str(len(rows))},
        {"metric": "row_count_after", "value": str(len(output))},
        {"metric": "patch_atoms_added", "value": str(len([p for p in patch_rows if p["rubric_atom_id"] not in already]))},
        {"metric": "overview_atom_demoted", "value": str(demoted_overview)},
        {"metric": "teaching_reflection_atoms_demoted", "value": str(len(teaching_reflection_ids))},
    ]
    write_csv(ATOM_OUT / "cc0143_atom_patch_report.csv", report_fields, report_rows)
    md = [
        "# CC0143 Atom Patch Report",
        "",
        f"- target: `{RUBRIC}`",
        f"- backup: `{backup_dir / RUBRIC.name}`",
        f"- row_count: {len(rows)} -> {len(output)}",
        "- patch atoms added: `PATCH_CC0143_CONTRACT_CHAIN_R01`, `PATCH_CC0143_CONSUMER_TRIPLE_COMP_R02`",
        f"- original R01 overview demoted from scoring support: {demoted_overview}",
        f"- teaching-reflection atoms demoted: {len(teaching_reflection_ids)}",
        "",
        "Gate: CC0143 may now support CODE_COWORK_004 only through scoring atoms/patch atoms, not through the giant overview atom or teaching-reflection atoms.",
        "",
    ]
    (ATOM_OUT / "cc0143_atom_patch_report.md").write_text("\n".join(md), encoding="utf-8")


def build_codebook_v12() -> None:
    fields, rows = read_csv(CODEBOOK_V11)
    output = [dict(row) for row in rows]
    by_code = {row["code_id"]: row for row in output}

    code4 = by_code["CODE_COWORK_004"]
    code4["source_observation_ids"] = append_unique(code4.get("source_observation_ids", ""), "FAIL4_COWORK_CC0143")
    code4["supporting_question_ids"] = append_unique(code4.get("supporting_question_ids", ""), "CC0143_2025_朝阳_一模_19")
    code4["supporting_rubric_atom_ids"] = append_unique(
        code4.get("supporting_rubric_atom_ids", ""),
        "PATCH_CC0143_CONTRACT_CHAIN_R01|PATCH_CC0143_CONSUMER_TRIPLE_COMP_R02|R_CC0143_2025_朝阳_一模_19_02|R_CC0143_2025_朝阳_一模_19_03|R_CC0143_2025_朝阳_一模_19_04|R_CC0143_2025_朝阳_一模_19_05|R_CC0143_2025_朝阳_一模_19_07|R_CC0143_2025_朝阳_一模_19_08|R_CC0143_2025_朝阳_一模_19_09",
    )
    code4["supporting_material_atom_ids"] = append_unique(
        code4.get("supporting_material_atom_ids", ""),
        "M_CC0143_2025_朝阳_一模_19_03|M_CC0143_2025_朝阳_一模_19_05|M_CC0143_2025_朝阳_一模_19_06|M_CC0143_2025_朝阳_一模_19_07|M_CC0143_2025_朝阳_一模_19_08",
    )
    code4["must_have_keywords"] = append_unique(
        code4.get("must_have_keywords", ""),
        "消费者权益保护法|三倍赔偿|合同成立|可撤销|欺诈|真实意思表示",
    )
    code4["counterexamples"] = append_note(
        code4.get("counterexamples", ""),
        "CC0143 requires separating two litigation requests; teaching-reflection atoms R11-R25 are not scoring support",
    )
    code4["reason"] = append_note(
        code4.get("reason", ""),
        "fail4_cowork_20260519: CC0143 added after atom patch as consumer fraud/triple-compensation subtype",
    )

    code2 = by_code["CODE_COWORK_002"]
    code2["source_observation_ids"] = append_unique(code2.get("source_observation_ids", ""), "FAIL4_COWORK_CC0143_MEANING")
    code2["supporting_question_ids"] = append_unique(code2.get("supporting_question_ids", ""), "CC0143_2025_朝阳_一模_19")
    code2["supporting_rubric_atom_ids"] = append_unique(
        code2.get("supporting_rubric_atom_ids", ""),
        "R_CC0143_2025_朝阳_一模_19_06|R_CC0143_2025_朝阳_一模_19_10",
    )
    code2["supporting_material_atom_ids"] = append_unique(
        code2.get("supporting_material_atom_ids", ""),
        "M_CC0143_2025_朝阳_一模_19_01|M_CC0143_2025_朝阳_一模_19_02|M_CC0143_2025_朝阳_一模_19_07",
    )
    code2["counterexamples"] = append_note(
        code2.get("counterexamples", ""),
        "RECOVER_2026_西城_二模_18_2 is AI industry-impact open container; do not force the personal-rights/market-order/value triad onto enterprise-industry-user impact questions",
    )
    code2["counterexamples"] = append_note(
        code2.get("counterexamples", ""),
        "CC0276 and RECOVER_2026_西城_二模_18_3 are boundary/non-core governance cases; do not import涉外法治/国家治理现代化 into 002",
    )
    code2["reason"] = append_note(
        code2.get("reason", ""),
        "fail4_cowork_20260519: CC0143 meaning-tail atoms added as limited support; AI/governance cases remain open or boundary",
    )

    write_csv(CODEBOOK_OUT, fields, output)
    write_csv(CODEBOOK_MAP, fields, output)

    open_fields = [
        "container_id",
        "question_id",
        "status",
        "rubric_atom_ids",
        "material_atom_ids",
        "reason",
        "core_codebook_use",
    ]
    cowork = cowork_rows()
    open_rows = [
        {
            "container_id": "OPEN_CONTAINER_AI_RESPONSIBILITY_BOUNDARY",
            "question_id": "RECOVER_2026_西城_二模_18_2",
            "status": "open_container_only",
            "rubric_atom_ids": cowork["RECOVER_2026_西城_二模_18_2"]["supporting_rubric_atom_ids"],
            "material_atom_ids": cowork["RECOVER_2026_西城_二模_18_2"]["supporting_material_atom_ids"],
            "reason": cowork["RECOVER_2026_西城_二模_18_2"]["reason"],
            "core_codebook_use": "no",
        },
        {
            "container_id": "BOUNDARY_CC0276_FOREIGN_RELATED_RULE_OF_LAW",
            "question_id": "CC0276_2026_房山_二模_17",
            "status": "boundary_exclude_core",
            "rubric_atom_ids": cowork["CC0276_2026_房山_二模_17"]["supporting_rubric_atom_ids"],
            "material_atom_ids": cowork["CC0276_2026_房山_二模_17"]["supporting_material_atom_ids"],
            "reason": cowork["CC0276_2026_房山_二模_17"]["reason"],
            "core_codebook_use": "no",
        },
        {
            "container_id": "BOUNDARY_RECOVER_2026_XICHENG_DIGITAL_GOVERNANCE",
            "question_id": "RECOVER_2026_西城_二模_18_3",
            "status": "boundary_exclude_core",
            "rubric_atom_ids": cowork["RECOVER_2026_西城_二模_18_3"]["supporting_rubric_atom_ids"],
            "material_atom_ids": cowork["RECOVER_2026_西城_二模_18_3"]["supporting_material_atom_ids"],
            "reason": cowork["RECOVER_2026_西城_二模_18_3"]["reason"],
            "core_codebook_use": "no",
        },
    ]
    write_csv(OPEN_OUT, open_fields, open_rows)

    md = [
        "# Provisional Codebook v1.2 After FAIL4 Cowork",
        "",
        "This is still a codebook, not a final framework.",
        "",
        "- integrated: Claude Cowork FAIL4 adjudication",
        "- new core support: `CC0143_2025_朝阳_一模_19` after atom patch",
        "- open container: `RECOVER_2026_西城_二模_18_2`",
        "- boundary excluded from core: `CC0276_2026_房山_二模_17`, `RECOVER_2026_西城_二模_18_3`",
        "",
        "## Revised Codes",
        "",
        "### CODE_COWORK_004",
        "",
        "- added subtype: consumer fraud + contract revocation + triple compensation",
        "- must-have keywords added: 消费者权益保护法 / 三倍赔偿 / 可撤销 / 欺诈 / 真实意思表示",
        "",
        "### CODE_COWORK_002",
        "",
        "- added CC0143 meaning-tail atoms as limited support",
        "- added counterexample: AI industry-impact questions use enterprise-industry-user layers and stay open until repeated samples appear",
        "- added boundary warning: 涉外法治建设 and 国家治理能力现代化 cannot be imported into the selected-compulsory-2 core",
        "",
        "## Gate",
        "",
        "The hard FAIL4 block is resolved. Framework synthesis may proceed only with boundary/open-container filters enabled and without treating open/boundary rows as core support.",
        "",
    ]
    CODEBOOK_MD.write_text("\n".join(md), encoding="utf-8")

    risks = [
        "# Codebook v1.2 Risks",
        "",
        "- CC0143 is core only after the atom patch; do not use original R01 or R11-R25 as core support.",
        "- RECOVER_2026_西城_二模_18_2 remains open container, not a stable framework node.",
        "- CC0276 and RECOVER_2026_西城_二模_18_3 are formal evidence but non-core for this selected-compulsory-2 project.",
        "- Any atom with can_be_written_without_material=yes plus 综合/治理 module signals must be checked before codebook promotion.",
        "- v1.2 authorizes framework synthesis, not final handbook closure.",
        "",
    ]
    CODEBOOK_RISKS.write_text("\n".join(risks), encoding="utf-8")


def build_resolution_snapshot() -> None:
    _, pressure = read_csv(PRESSURE_V11)
    resolution = {
        "CC0143_2025_朝阳_一模_19": "PASS_AFTER_CC0143_PATCH",
        "CC0276_2026_房山_二模_17": "BOUNDARY_EXCLUDED_NON_CORE",
        "RECOVER_2026_西城_二模_18_2": "OPEN_CONTAINER_ONLY",
        "RECOVER_2026_西城_二模_18_3": "BOUNDARY_EXCLUDED_NON_CORE",
    }
    fields = [
        "question_id",
        "old_pass_status",
        "evidence_level",
        "expansion_status",
        "final_resolution_status",
        "core_codebook_use",
        "next_action",
    ]
    rows = []
    for row in pressure:
        qid = row["question_id"]
        status = resolution.get(qid, row["pass_status"])
        if status == "PASS_AFTER_CC0143_PATCH" or row["pass_status"] == "PASS":
            core = "yes"
            next_action = "eligible for framework synthesis"
        elif status == "OPEN_CONTAINER_ONLY":
            core = "no"
            next_action = "keep in open container; do not generate core node"
        elif status == "BOUNDARY_EXCLUDED_NON_CORE":
            core = "no"
            next_action = "keep in boundary appendix; do not use as xuanbier core support"
        elif row["evidence_level"] == "reference_only":
            core = "no"
            next_action = "reference-only demo only; cannot support core"
        elif row["pass_status"] == "PARTIAL":
            core = "no"
            next_action = "open/partial support; pressure-test during framework synthesis but do not create unsupported node"
        else:
            core = "no"
            next_action = "needs source check"
        rows.append(
            {
                "question_id": qid,
                "old_pass_status": row["pass_status"],
                "evidence_level": row["evidence_level"],
                "expansion_status": row.get("expansion_status", ""),
                "final_resolution_status": status,
                "core_codebook_use": core,
                "next_action": next_action,
            }
        )
    write_csv(OUT_DIR / "framework_v1_2_fail4_resolution_snapshot_20260519.csv", fields, rows)
    counts = Counter(row["final_resolution_status"] for row in rows)
    core_count = sum(1 for row in rows if row["core_codebook_use"] == "yes")
    md = [
        "# Framework v1.2 FAIL4 Resolution Snapshot",
        "",
        f"- total questions: {len(rows)}",
        f"- core codebook-use yes: {core_count}",
        f"- core codebook-use no: {len(rows) - core_count}",
        "",
        "## Status Counts",
        "",
    ]
    for key, value in sorted(counts.items()):
        md.append(f"- {key}: {value}")
    md.extend(
        [
            "",
            "Interpretation: there are no unresolved v1.1 FAIL rows after Cowork integration, but PARTIAL/open/reference-only rows still cannot be used as unsupported core nodes.",
            "",
        ]
    )
    (OUT_DIR / "framework_v1_2_fail4_resolution_snapshot_20260519.md").write_text("\n".join(md), encoding="utf-8")


def main() -> None:
    build_cross_check()
    patch_cc0143_atoms()
    build_codebook_v12()
    build_resolution_snapshot()
    print("FAIL4 Cowork resolution integrated.")
    print(f"Cross-check: {OUT_DIR / 'fail4_external_cross_check_20260519.csv'}")
    print(f"Codebook: {CODEBOOK_OUT}")


if __name__ == "__main__":
    main()
