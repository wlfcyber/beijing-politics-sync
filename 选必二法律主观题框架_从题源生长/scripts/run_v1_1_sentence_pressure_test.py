#!/usr/bin/env python3
"""Run a conservative sentence-level pressure test for the 65-question corpus."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
QUESTIONS = ROOT / "04_merge_audit" / "merged_subjective_law_questions.csv"
MATERIALS = ROOT / "04_merge_audit" / "merged_material_atoms_subjective.csv"
RUBRICS = ROOT / "04_merge_audit" / "merged_rubric_atoms_subjective.csv"
CODEBOOK = ROOT / "08_codebook" / "provisional_codebook_v1_1_after_cc0364_split_20260519.csv"
SNAPSHOT = ROOT / "10_framework_validation" / "framework_v1_1_after_cc0364_split_pressure_snapshot_20260519.csv"

OUT_CSV = ROOT / "10_framework_validation" / "framework_v1_1_question_by_question_sentence_pressure_test_20260519.csv"
OUT_PASS = ROOT / "10_framework_validation" / "framework_v1_1_sentence_pressure_pass_report_20260519.md"
OUT_FAILURES = ROOT / "10_framework_validation" / "framework_v1_1_sentence_pressure_failure_cases_20260519.md"
OUT_PATCH = ROOT / "10_framework_validation" / "framework_v1_1_sentence_pressure_patch_suggestions_20260519.md"


FIELDS = [
    "question_id",
    "year",
    "district",
    "exam_stage",
    "question_no",
    "ask_text",
    "evidence_level",
    "expansion_status",
    "framework_entry_node",
    "why_this_entry",
    "ask_trigger",
    "material_trigger",
    "minimum_judgment_required",
    "material_layering",
    "legal_knowledge_triggered",
    "rubric_atom_ids_matched",
    "full_score_sentence_generated",
    "complete_answer_generated",
    "lost_points_if_any",
    "reason_for_loss",
    "module_boundary_risk",
    "risk_of_empty_value_talk",
    "risk_of_legal_exam_overanalysis",
    "pass_status",
    "patch_needed",
    "patch_type",
    "patch_suggestion",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def split_ids(value: str) -> list[str]:
    return [p.strip() for p in (value or "").split("|") if p.strip()]


def squash(value: str, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", (value or "").replace("\u3000", " ")).strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def scoring_rubrics(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    kept = []
    for row in rows:
        uncertainty = row.get("uncertainty", "")
        if "teaching_reflection_not_scoring_atom_not_core_code_support" in uncertainty:
            continue
        kept.append(row)
    return kept


def sentence_from_rubric(row: dict[str, str]) -> str:
    phrase = row.get("what_expression_is_rewarded") or row.get("rubric_or_answer_phrase") or row.get("plain_reward_description", "")
    phrase = phrase.replace("奖励：", "")
    phrase = re.sub(r"（[^）]{0,45}分[^）]*）", "", phrase)
    phrase = re.sub(r"\[[^\]]+\]", "", phrase)
    phrase = squash(phrase, 180)
    if not phrase:
        return ""
    if phrase.endswith(("。", "！", "？")):
        return phrase
    return phrase + "。"


def risk_from_codes(code_rows: list[dict[str, str]], field: str) -> str:
    values = []
    for row in code_rows:
        value = row.get(field, "")
        if value and value not in values:
            values.append(value)
    return " | ".join(values) if values else "未形成核心代码本判断"


def main() -> None:
    questions = read_csv(QUESTIONS)
    materials = read_csv(MATERIALS)
    rubrics = read_csv(RUBRICS)
    codes = read_csv(CODEBOOK)
    snapshot = {row["question_id"]: row for row in read_csv(SNAPSHOT)}

    mats_by_qid: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in materials:
        mats_by_qid[row["question_id"]].append(row)

    rubrics_by_qid: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rubrics:
        rubrics_by_qid[row["question_id"]].append(row)

    codes_by_qid: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in codes:
        for qid in split_ids(row["supporting_question_ids"]):
            codes_by_qid[qid].append(row)

    output = []
    for q in questions:
        qid = q["question_id"]
        status = snapshot.get(qid, {}).get("expansion_status", "NO_EXPANSION_SUPPORT_YET")
        evidence = q.get("evidence_level", "")
        q_codes = codes_by_qid.get(qid, [])
        q_mats = mats_by_qid.get(qid, [])
        q_rubrics = scoring_rubrics(rubrics_by_qid.get(qid, []))
        code_ids = [row["code_id"] for row in q_codes]

        material_layering = " / ".join(
            f"{row.get('material_atom_id')}: {squash(row.get('plain_description') or row.get('material_phrase'), 90)}"
            for row in q_mats[:8]
        )
        material_trigger = "；".join(
            squash(row.get("legal_signal_if_any") or row.get("material_phrase") or row.get("plain_description"), 80)
            for row in q_mats[:4]
        )
        rubric_ids = "|".join(row.get("rubric_atom_id", "") for row in q_rubrics if row.get("rubric_atom_id"))
        generated_sentences = [sentence_from_rubric(row) for row in q_rubrics]
        generated_sentences = [s for s in generated_sentences if s]

        if status == "CORE_CODEBOOK_SUPPORT":
            pass_status = "PASS"
            patch_needed = "no"
            patch_type = ""
            reason_for_loss = ""
            lost_points = ""
            why_entry = "question_id enters at least one dual-model/Codex-adjudicated core code; sentence generation is checked against current rubric atoms."
            patch_suggestion = "进入下一轮框架综合压测；注意仍需逐题人工润色成最终宝典语言。"
        elif status == "OPEN_CONTAINER_ONLY":
            pass_status = "PARTIAL"
            patch_needed = "yes"
            patch_type = "开放容器未升格"
            reason_for_loss = "有正式或可读证据，但双模型未同意升为核心代码；可生成题内句，不能证明学生可用主干框架稳定启动。"
            lost_points = "可能漏掉该题独有得分格；不能宣称满分闭环。"
            why_entry = "only open-container or transfer-only placement exists after expansion adjudication."
            patch_suggestion = "保留开放容器；若后续同型题增多，再回源验证是否增设低频节点。"
        elif status == "REFERENCE_OR_REJECT_NON_CORE":
            if evidence == "reference_only":
                pass_status = "PARTIAL"
                patch_needed = "yes"
                patch_type = "证据不足"
                reason_for_loss = "reference_only 不能支撑核心节点，只能作为弱示范或待补细则材料。"
                lost_points = "没有 formal 细则时不能宣称满分。"
                patch_suggestion = "补正式细则/评标后再决定是否进入代码本；当前不入核心。"
            else:
                pass_status = "FAIL"
                patch_needed = "yes"
                patch_type = "模块边界/非核心"
                reason_for_loss = "虽有 formal 证据，但双模型/本地裁决未将其作为选必二法律主干核心；存在必修三或综合法治边界。"
                lost_points = "若硬塞进法律框架，会把框架拉向泛法治或涉外法治表达。"
                patch_suggestion = "单列边界题，不进入核心框架；必要时交由必修三/综合法治线复核。"
            why_entry = "reference-only or rejected/non-core after dual-model adjudication."
        else:
            pass_status = "FAIL"
            patch_needed = "yes"
            patch_type = "无扩展支撑"
            reason_for_loss = "当前 65 题代码本扩展后仍无核心支撑或开放容器归位。"
            lost_points = "无法从现有框架稳定启动，必须回源或重送模型做专项审查。"
            why_entry = "no accepted codebook support after corrected expansion round."
            patch_suggestion = "专项回源：拆 rubric atoms、判断是否误排除，或将其作为明确反例/边界题。"

        legal_knowledge = "；".join(
            squash(row.get("legal_knowledge_or_rule_if_explicit"), 80)
            for row in q_rubrics
            if row.get("legal_knowledge_or_rule_if_explicit")
        )
        if not legal_knowledge:
            legal_knowledge = risk_from_codes(q_codes, "legal_knowledge_or_rule_pattern")

        answer = " ".join(generated_sentences[:12])
        if evidence == "reference_only":
            answer_prefix = "【reference_only，非满分闭环】"
        elif pass_status != "PASS":
            answer_prefix = "【压力测试草句，非最终满分稿】"
        else:
            answer_prefix = "【细则原子覆盖草句】"
        complete_answer = answer_prefix + (answer or "当前无可用细则句，需回源补原子。")

        output.append(
            {
                "question_id": qid,
                "year": q.get("year", ""),
                "district": q.get("district", ""),
                "exam_stage": q.get("exam_stage", ""),
                "question_no": q.get("question_no", ""),
                "ask_text": q.get("ask_text", ""),
                "evidence_level": evidence,
                "expansion_status": status,
                "framework_entry_node": "|".join(code_ids) if code_ids else snapshot.get(qid, {}).get("matched_code_or_container", ""),
                "why_this_entry": why_entry,
                "ask_trigger": squash(q.get("ask_text", ""), 180),
                "material_trigger": material_trigger,
                "minimum_judgment_required": risk_from_codes(q_codes, "what_student_must_judge")
                if q_codes
                else "先判断该题是否真属选必二法律规则/制度；再判断主体、行为、权利义务或程序路径。",
                "material_layering": material_layering,
                "legal_knowledge_triggered": legal_knowledge,
                "rubric_atom_ids_matched": rubric_ids,
                "full_score_sentence_generated": " | ".join(generated_sentences[:8]),
                "complete_answer_generated": complete_answer,
                "lost_points_if_any": lost_points,
                "reason_for_loss": reason_for_loss,
                "module_boundary_risk": q.get("module_boundary_risk", ""),
                "risk_of_empty_value_talk": risk_from_codes(q_codes, "risk_of_empty_value_talk"),
                "risk_of_legal_exam_overanalysis": risk_from_codes(q_codes, "risk_of_legal_exam_overanalysis"),
                "pass_status": pass_status,
                "patch_needed": patch_needed,
                "patch_type": patch_type,
                "patch_suggestion": patch_suggestion,
            }
        )

    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(output)

    counts = Counter(row["pass_status"] for row in output)
    evidence_counts = Counter(row["evidence_level"] for row in output)
    status_counts = Counter(row["expansion_status"] for row in output)

    pass_md = [
        "# Framework v1.1 Sentence-Level Pressure Test Pass Report",
        "",
        "This is still a pressure test, not final framework_v2 or final handbook authorization.",
        "",
        f"- total questions: {len(output)}",
        f"- PASS: {counts['PASS']}",
        f"- PARTIAL: {counts['PARTIAL']}",
        f"- FAIL: {counts['FAIL']}",
        f"- evidence formal: {evidence_counts['formal']}",
        f"- evidence reference_only: {evidence_counts['reference_only']}",
        "",
        "## Expansion Status Counts",
        "",
        "| expansion_status | count |",
        "|---|---:|",
    ]
    for status, count in status_counts.most_common():
        pass_md.append(f"| {status} | {count} |")
    pass_md.extend(
        [
            "",
            "## Gate Decision",
            "",
            "- `PASS` rows can enter framework synthesis pressure work.",
            "- `PARTIAL` rows must remain open-container/reference-only/boundary examples until more evidence or a low-frequency node is justified.",
            "- `FAIL` rows cannot be used to prove the current framework; they require source or module-boundary adjudication.",
            "- Therefore framework_v2 and final baodian are still blocked until the PARTIAL/FAIL policy is explicitly accepted or patched.",
            "",
        ]
    )
    OUT_PASS.write_text("\n".join(pass_md), encoding="utf-8")

    failures = [row for row in output if row["pass_status"] == "FAIL"]
    partials = [row for row in output if row["pass_status"] == "PARTIAL"]
    fail_md = ["# Framework v1.1 Sentence Pressure Failure Cases", ""]
    fail_md.append("## FAIL")
    fail_md.append("")
    for row in failures:
        fail_md.append(f"- `{row['question_id']}` — {row['patch_type']} — {row['reason_for_loss']}")
    fail_md.append("")
    fail_md.append("## PARTIAL")
    fail_md.append("")
    for row in partials:
        fail_md.append(f"- `{row['question_id']}` — {row['patch_type']} — {row['reason_for_loss']}")
    fail_md.append("")
    OUT_FAILURES.write_text("\n".join(fail_md), encoding="utf-8")

    patch_md = ["# Framework v1.1 Sentence Pressure Patch Suggestions", ""]
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in output:
        if row["patch_needed"] == "yes":
            grouped[row["patch_type"]].append(row)
    for patch_type, rows in sorted(grouped.items()):
        patch_md.append(f"## {patch_type}")
        patch_md.append("")
        for row in rows:
            patch_md.append(f"- `{row['question_id']}`: {row['patch_suggestion']}")
        patch_md.append("")
    OUT_PATCH.write_text("\n".join(patch_md), encoding="utf-8")

    print(f"Wrote {OUT_CSV}")
    print(dict(counts))


if __name__ == "__main__":
    main()
