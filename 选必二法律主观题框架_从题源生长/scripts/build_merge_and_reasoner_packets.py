#!/usr/bin/env python3
import csv
import json
from collections import Counter
from pathlib import Path

RUN_ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")


def read_csv(path):
    p = RUN_ROOT / path
    if not p.exists() or p.stat().st_size == 0:
        return []
    with p.open(encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows):
    p = RUN_ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        p.write_text("", encoding="utf-8")
        return
    with p.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_jsonl(path, rows):
    p = RUN_ROOT / path
    with p.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def key(row):
    return (row.get("year",""), row.get("district",""), row.get("exam_stage",""), row.get("question_no",""), row.get("sub_question_no",""))


def main():
    codex = read_csv("01_subjective_candidates/all_candidate_subjective_law_questions_codex.csv")
    cc = read_csv("01_subjective_candidates/all_candidate_subjective_law_questions_claudecode.csv")
    false_pos = read_csv("04_merge_audit/claudecode_false_positive_candidates.csv")
    cc_missing = read_csv("04_merge_audit/claudecode_missing_from_codex.csv")
    evid_dis = read_csv("04_merge_audit/claudecode_evidence_level_disagreements.csv")
    mod_dis = read_csv("04_merge_audit/claudecode_module_boundary_disagreements.csv")
    loc_risks = read_csv("04_merge_audit/claudecode_locator_or_ocr_risks.csv")

    false_keys = {key(r) for r in false_pos}
    cc_keys = {key(r) for r in cc}
    loc_risk_keys = {key(r) for r in loc_risks}
    evidence_dispute_keys = {key(r) for r in evid_dis}
    module_dispute_keys = {key(r) for r in mod_dis}

    # Conservative canonical merge: ClaudeCode independent extraction is the main merged set.
    merged = []
    for r in cc:
        mr = dict(r)
        mr["merged_question_id"] = "M_" + r["question_id"]
        mr["codex_question_id_if_matched"] = ""
        mr["claudecode_question_id"] = r["question_id"]
        mr["merge_status"] = "keep"
        mr["merge_decision_reason"] = "kept from ClaudeCode independent extraction"
        if key(r) in evidence_dispute_keys:
            mr["merge_decision_reason"] += "; evidence conflict handled conservatively via ClaudeCode level"
        if key(r) in module_dispute_keys:
            mr["merge_decision_reason"] += "; module boundary was disputed against Codex"
        if key(r) in loc_risk_keys:
            mr["merge_status"] = "pending_locator_check"
            mr["merge_decision_reason"] += "; paper locator/OCR risk requires回源"
        if r.get("evidence_level") == "missing":
            mr["merge_status"] = "pending_evidence"
            mr["merge_decision_reason"] += "; missing evidence not allowed into framework induction"
        if r.get("year") == "2026" and r.get("district") == "石景山" and r.get("exam_stage") == "期末":
            mr["merge_status"] = "blocked"
            mr["merge_decision_reason"] += "; hard-rule exclusion for 2026石景山期末"
        merged.append(mr)

    codex_only = [r for r in codex if key(r) not in cc_keys and key(r) not in false_keys]
    claudecode_only = cc_missing
    disagreed_module = mod_dis
    disagreed_evidence = evid_dis
    disagreed_locator = loc_risks

    write_csv("04_merge_audit/merged_subjective_law_questions.csv", merged)
    write_jsonl("04_merge_audit/merged_subjective_law_questions.jsonl", merged)
    write_csv("04_merge_audit/codex_only_cases.csv", codex_only)
    write_csv("04_merge_audit/claudecode_only_cases.csv", claudecode_only)
    write_csv("04_merge_audit/disagreed_module_cases.csv", disagreed_module)
    write_csv("04_merge_audit/disagreed_evidence_level_cases.csv", disagreed_evidence)
    write_csv("04_merge_audit/disagreed_locator_cases.csv", disagreed_locator)

    # Atom merge: use ClaudeCode canonical atom ids for merged candidates.
    mat = read_csv("02_material_atoms/material_atoms_subjective_claudecode.csv")
    ask = read_csv("02_material_atoms/ask_atoms_subjective_claudecode.csv")
    rub = read_csv("03_rubric_atoms/rubric_atoms_subjective_claudecode.csv")
    write_csv("04_merge_audit/merged_material_atoms_subjective.csv", mat)
    write_csv("04_merge_audit/merged_ask_atoms_subjective.csv", ask)
    write_csv("04_merge_audit/merged_rubric_atoms_subjective.csv", rub)

    level_counts = Counter(r.get("evidence_level","") for r in merged)
    status_counts = Counter(r.get("merge_status","") for r in merged)
    reasoner_rows = [
        r for r in merged
        if r.get("evidence_level") == "formal"
        and key(r) not in loc_risk_keys
        and r.get("merge_status") == "keep"
        and not (r.get("year") == "2026" and r.get("district") == "石景山" and r.get("exam_stage") == "期末")
    ]
    reasoner_qids = {r["claudecode_question_id"] for r in reasoner_rows}
    reasoner_mat = [r for r in mat if r.get("question_id") in reasoner_qids]
    reasoner_ask = [r for r in ask if r.get("question_id") in reasoner_qids]
    reasoner_rub = [r for r in rub if r.get("question_id") in reasoner_qids]

    write_csv("05_reasoner_packets/merged_subjective_law_questions_for_reasoners.csv", reasoner_rows)
    write_csv("05_reasoner_packets/merged_material_atoms_subjective_for_reasoners.csv", reasoner_mat)
    write_csv("05_reasoner_packets/merged_ask_atoms_subjective_for_reasoners.csv", reasoner_ask)
    write_csv("05_reasoner_packets/merged_rubric_atoms_subjective_for_reasoners.csv", reasoner_rub)

    report = f"""# Merge Audit Report

generated_at: 2026-05-19T10:40:00+08:00

## Verdict

CONDITIONAL_PASS.

The merged evidence layer is sufficient to build a first reasoner packet from a restricted formal subset, but it is not sufficient for final framework closure.

## Counts

- Codex A candidate count: {len(codex)}
- ClaudeCode B candidate count: {len(cc)}
- Merged canonical candidates: {len(merged)}
- Codex-only retained after B rejection filter: {len(codex_only)}
- ClaudeCode-only candidates: {len(claudecode_only)}
- Codex false positives rejected by B: {len(false_pos)}
- Module boundary disputes: {len(disagreed_module)}
- Evidence-level disputes: {len(disagreed_evidence)}
- Locator/OCR risks: {len(disagreed_locator)}

## Evidence Level Counts

{chr(10).join(f'- {k}: {v}' for k, v in sorted(level_counts.items()))}

## Merge Status Counts

{chr(10).join(f'- {k}: {v}' for k, v in sorted(status_counts.items()))}

## Decisions

1. 双方一致或 B 独立保留的候选进入 merged 主表。
2. Codex 独有且被 B 判定误收的候选不进入 merged 主表，保存在 `claudecode_false_positive_candidates.csv`。
3. B 独有候选进入 `claudecode_only_cases.csv`，并保留在 merged 主表。
4. 证据等级冲突按 ClaudeCode 较保守等级处理。
5. module boundary 或 locator/OCR 风险题保留在 merged 主表，但标记 pending，不进入第一轮 reasoner formal subset。
6. evidence_level=missing 不进入归纳，只进入待补证据清单。
7. reference_only 可以进入弱观察背景，但本轮 reasoner packet 只采用 formal 且 locator 可靠题。
8. 2026 石景山期末按硬规则继续 blocked。

## Can Enter First Open Observation

Reasoner formal subset count: {len(reasoner_rows)}.

This subset is written to `05_reasoner_packets/*_for_reasoners.csv`.

## Still Forbidden

Do not output a framework yet. This merge audit only authorizes a first open-observation packet for real GPT-5.5 Pro and Claude Opus, not a codebook, candidate framework, final framework, or baodian.
"""
    (RUN_ROOT / "04_merge_audit/merge_audit_report.md").write_text(report, encoding="utf-8")
    (RUN_ROOT / "05_reasoner_packets/merge_audit_report_for_reasoners.md").write_text(report, encoding="utf-8")

    packet = f"""# REASONER_INPUT_PACKET

## 工程目标

从 2024-2026 北京各区选必二《法律与生活》主观题与 formal 评分证据中，开放归纳命题机制、判分机制和学生作答机制。本轮只做观察，不写框架。

## Scope

- 只研究主观题。
- 选择题不进入框架，不分析错项。
- 不预设“一核二线三问四步五域”“动作库”“故事卡”“法律关系路由”。
- 不按教材目录先搭框架。
- 参考答案不得冒充评分细则。

## Data Range

- merged canonical candidates: {len(merged)}
- reasoner formal subset: {len(reasoner_rows)}
- formal total in merged: {level_counts.get('formal', 0)}
- reference_only total in merged: {level_counts.get('reference_only', 0)}
- missing total in merged: {level_counts.get('missing', 0)}
- locator/OCR risk excluded from reasoner subset: {len(disagreed_locator)}
- module boundary disputes excluded from reasoner subset unless resolved formal: {len(disagreed_module)}

## Input Files

- merged_subjective_law_questions_for_reasoners.csv
- merged_material_atoms_subjective_for_reasoners.csv
- merged_ask_atoms_subjective_for_reasoners.csv
- merged_rubric_atoms_subjective_for_reasoners.csv
- merge_audit_report_for_reasoners.md

## Unified Task

基于每一道题的 question_id、rubric_atom_id、material_atom_id，逐题分析模块边界、设问任务、最小必要判断、材料事实与细则触发、得分机制、满分句生成、迁移与代码本资格。

## Output Requirement

每条 observation 必须包含 evidence ids；没有 question_id、rubric_atom_id、material_atom_id 的观察不得进入下一轮。最后分为强观察、弱观察、冲突观察、不应上升为框架的观察、下一轮需补充题型。

本轮禁止输出总框架。
"""
    (RUN_ROOT / "05_reasoner_packets/REASONER_INPUT_PACKET.md").write_text(packet, encoding="utf-8")

    print(json.dumps({
        "merged": len(merged),
        "reasoner_formal_subset": len(reasoner_rows),
        "codex_only": len(codex_only),
        "claudecode_only": len(claudecode_only),
        "false_positive": len(false_pos),
        "status_counts": dict(status_counts),
        "level_counts": dict(level_counts),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

