# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
from collections import Counter
from datetime import datetime
from pathlib import Path


DESKTOP = Path(r"C:\Users\Administrator\Desktop")
RUN_DIR = DESKTOP / "飞哥的政治庄园" / "reports" / "选必三_穷尽性重审_ClaudeCode厚内容_2026-05-07"
CODEX_DIR = RUN_DIR / "codex_lane"
SYNC_BASE = (
    DESKTOP
    / "02_代码项目与工具"
    / "mac-thread-restore"
    / "beijing-politics-sync-visible"
    / "reports"
    / "week_migration_2026-05-01_to_2026-05-06"
    / "desktop_snapshots"
    / "选必三逻辑与思维_四线从0重跑_2026-05-04"
)
COVERAGE = SYNC_BASE / "05_coverage"
STUDENT_DRAFT = SYNC_BASE / "09_student_draft"


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def key_phase03(row: dict[str, str]) -> tuple[str, str, str, str]:
    return (
        row.get("question_id", ""),
        row.get("stable_locator", ""),
        row.get("source_id", ""),
        (row.get("excerpt", "") or "")[:160],
    )


def normalize_action(action: str, category: str, section_scope: str) -> str:
    if action in {"covered_by_74_review_body", "body_after_362_repair"}:
        return "入正文"
    if action == "excluded_keep_out" or category == "out_of_scope" or section_scope == "边界":
        return "excluded"
    if action == "blocked_keep_out":
        return "blocked"
    if category in {"answer_missing", "visual_missing", "blocked"}:
        return "blocked"
    return "blocked"


def action_reason(p12: dict[str, str]) -> str:
    note = p12.get("phase12_rescan_note", "")
    blocker = p12.get("blocker_reason", "")
    category = p12.get("phase12_rescan_category", "")
    action = p12.get("phase12_final_action", "")
    parts = [f"phase12_action={action}", f"phase12_category={category}"]
    if blocker:
        parts.append(f"blocker={blocker}")
    if note:
        parts.append(f"note={note}")
    return "；".join(parts)


def evidence_level_for(row: dict[str, str], conclusion: str) -> str:
    qtype = row.get("question_type") or row.get("题型", "")
    rubric = row.get("rubric_pairing_status") or row.get("是否有评分细则", "")
    answer = row.get("answer_pairing_status") or row.get("是否有答案", "")
    if conclusion == "入正文" and qtype == "主观题":
        if "formal" in rubric or "yes" in rubric or "confirmed" in rubric:
            return "A-formal_or_phase12_source_confirmed"
        return "A-support_or_needs_formal_label_check"
    if conclusion == "入正文" and qtype == "选择题":
        if "confirmed" in answer or "yes" in answer:
            return "B-choice-signal"
        return "B-choice-signal_needs_answer_key_check"
    if conclusion == "excluded":
        return "C-boundary_or_duplicate"
    return "missing_or_blocked"


def main() -> None:
    phase03 = read_csv(COVERAGE / "phase03_question_coverage_matrix.csv")
    signals = read_csv(COVERAGE / "phase03_thinking_signal_chain_matrix.csv")
    phase05 = read_csv(COVERAGE / "phase05_evidence_pool_74.csv")
    phase12 = read_csv(COVERAGE / "phase12_362_control_base_rescan_matrix.csv")
    body77 = read_csv(STUDENT_DRAFT / "phase12_expanded_body_FROM_362_control_matrix.csv")
    duplicates = read_csv(COVERAGE / "phase03_laneA_duplicate_or_reference_rows.csv")

    p12_by_qid = {r.get("canonical_question_id", ""): r for r in phase12}
    p05_by_qid = {r.get("question_id", ""): r for r in phase05}
    body_by_qid = {r.get("question_id", ""): r for r in body77}
    duplicate_keys = {key_phase03(r) for r in duplicates}
    nonduplicate_qids = {r.get("question_id", "") for r in phase03 if key_phase03(r) not in duplicate_keys}
    represented_body_qids: set[str] = set()

    matrix_rows: list[dict[str, str]] = []
    duplicate_audit_rows: list[dict[str, str]] = []
    phase03_qids = {r.get("question_id", "") for r in phase03}

    for r in phase03:
        qid = r.get("question_id", "")
        duplicate_match = key_phase03(r) in duplicate_keys
        p12 = p12_by_qid.get(qid)
        body = body_by_qid.get(qid)
        p05 = p05_by_qid.get(qid)

        p12_conclusion = ""
        if p12:
            p12_conclusion = normalize_action(
                p12.get("phase12_final_action", ""),
                p12.get("phase12_rescan_category", ""),
                p12.get("section_scope", ""),
            )

        if duplicate_match and p12_conclusion == "入正文" and qid not in nonduplicate_qids and qid not in represented_body_qids:
            conclusion = "入正文"
            represented_body_qids.add(qid)
            basis = "phase12_body_representative_from_duplicate_source_row"
            reason = (
                "该题在 phase03 仅以重复/参考源行形态出现；"
                "为保证 528-row audit 中 body canonical 不消失，保留首个重复源行作为 canonical body representative；"
                + action_reason(p12)
            )
        elif duplicate_match:
            canonical_conclusion = ""
            if p12:
                canonical_conclusion = p12_conclusion
            conclusion = "同类索引"
            basis = "phase03_duplicate_or_reference_row"
            reason = (
                "重复/参考源行，不作为独立题计入正文；"
                f"canonical_question_id={qid}; canonical_conclusion={canonical_conclusion or 'not_found'}"
            )
        elif p12:
            conclusion = p12_conclusion
            if conclusion == "入正文":
                represented_body_qids.add(qid)
            basis = "phase12_362_rescan"
            reason = action_reason(p12)
        elif p05 or body:
            conclusion = "入正文"
            basis = "phase05_or_phase12_body_without_p12_match"
            reason = "旧证据池/77行扩容稿存在该题，但未在362回扫矩阵匹配；需要回源确认 canonical id"
        else:
            part = r.get("部分归属", "")
            if part == "边界":
                conclusion = "excluded"
                reason = "phase03 边界行，未进入 phase12 canonical；按边界保留审计"
            elif part == "missing":
                conclusion = "blocked"
                reason = "phase03 missing 行，未进入 phase12 canonical；缺题面/答案/证据"
            else:
                conclusion = "blocked"
                reason = "phase03 候选行未进入 phase12 canonical，也非重复行；需回源确认或补入下一轮 batch"
            basis = "phase03_fallback_after_phase12"

        out = {
            "question_id": qid,
            "suite_id": r.get("suite_id", ""),
            "source_id": r.get("source_id", ""),
            "stable_locator": r.get("stable_locator", ""),
            "original_qno": r.get("原始题号", ""),
            "question_type": r.get("题型", ""),
            "phase03_section_scope": r.get("部分归属", ""),
            "phase03_knowledge_node": r.get("知识节点", ""),
            "phase03_reasoning_node": r.get("题型节点", ""),
            "phase03_blocked_status": r.get("blocked_status", ""),
            "phase03_final_classification": r.get("final_classification", ""),
            "phase12_category": p12.get("phase12_rescan_category", "") if p12 else "",
            "phase12_action": p12.get("phase12_final_action", "") if p12 else "",
            "phase12_blocker_reason": p12.get("blocker_reason", "") if p12 else "",
            "body77_status": body.get("current_body_status", "") if body else "",
            "body77_decision": body.get("phase12_decision", "") if body else "",
            "phase05_status": p05.get("status", "") if p05 else "",
            "current_exhaustive_conclusion": conclusion,
            "evidence_level": evidence_level_for(p12 or r, conclusion),
            "decision_basis": basis,
            "decision_reason": reason,
            "duplicate_or_reference": "yes" if duplicate_match else "no",
            "excerpt": r.get("excerpt", ""),
        }
        matrix_rows.append(out)
        if duplicate_match:
            duplicate_audit_rows.append(out)

    for qid, p12 in sorted(p12_by_qid.items()):
        if not qid or qid in phase03_qids:
            continue
        conclusion = normalize_action(
            p12.get("phase12_final_action", ""),
            p12.get("phase12_rescan_category", ""),
            p12.get("section_scope", ""),
        )
        matrix_rows.append({
            "question_id": qid,
            "suite_id": p12.get("suite_id", ""),
            "source_id": "",
            "stable_locator": "",
            "original_qno": p12.get("original_qno", ""),
            "question_type": p12.get("question_type", ""),
            "phase03_section_scope": "",
            "phase03_knowledge_node": "",
            "phase03_reasoning_node": "",
            "phase03_blocked_status": "",
            "phase03_final_classification": "not_in_phase03_added_from_phase12",
            "phase12_category": p12.get("phase12_rescan_category", ""),
            "phase12_action": p12.get("phase12_final_action", ""),
            "phase12_blocker_reason": p12.get("blocker_reason", ""),
            "body77_status": body_by_qid.get(qid, {}).get("current_body_status", ""),
            "body77_decision": body_by_qid.get(qid, {}).get("phase12_decision", ""),
            "phase05_status": p05_by_qid.get(qid, {}).get("status", ""),
            "current_exhaustive_conclusion": conclusion,
            "evidence_level": evidence_level_for(p12, conclusion),
            "decision_basis": "phase12_extra_canonical_not_in_phase03",
            "decision_reason": "Phase12 canonical row not present in the original 528-row phase03 matrix; added so the current audit matrix is not narrower than the later control base. " + action_reason(p12),
            "duplicate_or_reference": "no",
            "excerpt": "",
        })

    canonical_rows: list[dict[str, str]] = []
    for p12 in phase12:
        qid = p12.get("canonical_question_id", "")
        conclusion = normalize_action(
            p12.get("phase12_final_action", ""),
            p12.get("phase12_rescan_category", ""),
            p12.get("section_scope", ""),
        )
        body = body_by_qid.get(qid, {})
        p05 = p05_by_qid.get(qid, {})
        canonical_rows.append({
            "question_id": qid,
            "suite_id": p12.get("suite_id", ""),
            "original_qno": p12.get("original_qno", ""),
            "question_type": p12.get("question_type", ""),
            "section_scope": p12.get("section_scope", ""),
            "knowledge_node": p12.get("knowledge_node", ""),
            "reasoning_node": p12.get("reasoning_node", ""),
            "phase04_level": p12.get("phase04_level", ""),
            "answer_pairing_status": p12.get("answer_pairing_status", ""),
            "rubric_pairing_status": p12.get("rubric_pairing_status", ""),
            "visual_status": p12.get("visual_status", ""),
            "phase12_category": p12.get("phase12_rescan_category", ""),
            "phase12_action": p12.get("phase12_final_action", ""),
            "current_exhaustive_conclusion": conclusion,
            "evidence_level": evidence_level_for(p12, conclusion),
            "body77_status": body.get("current_body_status", ""),
            "body77_decision": body.get("phase12_decision", ""),
            "phase05_status": p05.get("status", ""),
            "decision_reason": action_reason(p12),
        })

    signal_rows: list[dict[str, str]] = []
    for s in signals:
        qid = s.get("question_id", "")
        p12 = p12_by_qid.get(qid)
        body = body_by_qid.get(qid)
        p05 = p05_by_qid.get(qid)
        if body:
            conclusion = "入正文"
            reason = f"phase12 expanded body row: {body.get('phase12_decision', '')}"
        elif p12:
            conclusion = normalize_action(
                p12.get("phase12_final_action", ""),
                p12.get("phase12_rescan_category", ""),
                p12.get("section_scope", ""),
            )
            reason = action_reason(p12)
        elif p05:
            conclusion = "同类索引"
            reason = "phase05 evidence archive has this signal, but current body matrix lacks it; needs source/body/index finalization"
        else:
            conclusion = "blocked"
            reason = "signal row lacks current source pairing/body/index decision"
        signal_rows.append({
            "question_id": qid,
            "suite_id": s.get("suite_id", ""),
            "stable_locator": s.get("stable_locator", ""),
            "thinking_node": s.get("思维知识节点", ""),
            "source_example": s.get("来源例题", ""),
            "student_draft_flag": s.get("是否可入学生稿", ""),
            "current_exhaustive_conclusion": conclusion,
            "decision_reason": reason,
            "why_trigger": s.get("为什么能想到", ""),
            "answer_landing": s.get("答案落点", ""),
        })

    matrix_fields = [
        "question_id", "suite_id", "source_id", "stable_locator", "original_qno", "question_type",
        "phase03_section_scope", "phase03_knowledge_node", "phase03_reasoning_node",
        "phase03_blocked_status", "phase03_final_classification", "phase12_category",
        "phase12_action", "phase12_blocker_reason", "body77_status", "body77_decision",
        "phase05_status", "current_exhaustive_conclusion", "evidence_level", "decision_basis",
        "decision_reason", "duplicate_or_reference", "excerpt",
    ]
    canonical_fields = [
        "question_id", "suite_id", "original_qno", "question_type", "section_scope",
        "knowledge_node", "reasoning_node", "phase04_level", "answer_pairing_status",
        "rubric_pairing_status", "visual_status", "phase12_category", "phase12_action",
        "current_exhaustive_conclusion", "evidence_level", "body77_status", "body77_decision",
        "phase05_status", "decision_reason",
    ]
    signal_fields = [
        "question_id", "suite_id", "stable_locator", "thinking_node", "source_example",
        "student_draft_flag", "current_exhaustive_conclusion", "decision_reason",
        "why_trigger", "answer_landing",
    ]

    write_csv(CODEX_DIR / "CODEX_EXHAUSTIVE_DECISION_MATRIX.csv", matrix_rows, matrix_fields)
    write_csv(CODEX_DIR / "CODEX_EXHAUSTIVE_CANONICAL_DECISION_MATRIX.csv", canonical_rows, canonical_fields)
    write_csv(CODEX_DIR / "CODEX_DUPLICATE_OR_REFERENCE_AUDIT.csv", duplicate_audit_rows, matrix_fields)
    write_csv(CODEX_DIR / "CODEX_SIGNAL_CLOSURE_MATRIX.csv", signal_rows, signal_fields)

    counts = {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "phase03_total_rows": len(phase03),
        "union_decision_matrix_rows": len(matrix_rows),
        "canonical_phase12_rows": len(phase12),
        "phase05_evidence_pool_rows": len(phase05),
        "phase12_expanded_body_rows": len(body77),
        "duplicate_or_reference_rows_matched": len(duplicate_audit_rows),
        "decision_counts_union_matrix": dict(Counter(r["current_exhaustive_conclusion"] for r in matrix_rows)),
        "decision_counts_canonical": dict(Counter(r["current_exhaustive_conclusion"] for r in canonical_rows)),
        "signal_decision_counts": dict(Counter(r["current_exhaustive_conclusion"] for r in signal_rows)),
        "phase12_action_counts": dict(Counter(r.get("phase12_final_action", "") for r in phase12)),
        "phase12_category_counts": dict(Counter(r.get("phase12_rescan_category", "") for r in phase12)),
    }
    (CODEX_DIR / "CODEX_EXHAUSTIVE_DECISION_SUMMARY.json").write_text(
        json.dumps(counts, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    md = [
        "# Codex 穷尽性底账合并报告",
        "",
        "Status: `NOT_FINAL_SOURCE_EXHAUSTION_IN_PROGRESS`",
        "",
        "本报告只说明当前 528-row control base 已被逐行转成可追踪的当前判定；它不授权 Word/PDF/final。",
        "",
        "## 输入底账",
        "",
        f"- Phase03 control base: {len(phase03)} rows",
        f"- Current union decision matrix: {len(matrix_rows)} rows",
        f"- Phase04/12 canonical rescan: {len(phase12)} rows",
        f"- Phase05 evidence archive: {len(phase05)} rows",
        f"- Phase12 expanded review-only body: {len(body77)} rows",
        f"- Phase03 duplicate/reference rows matched: {len(duplicate_audit_rows)} rows",
        "",
        "## 528+ 当前判定",
        "",
    ]
    for k, v in counts["decision_counts_union_matrix"].items():
        md.append(f"- {k}: {v}")
    md.extend([
        "",
        "## Canonical 362 当前判定",
        "",
    ])
    for k, v in counts["decision_counts_canonical"].items():
        md.append(f"- {k}: {v}")
    md.extend([
        "",
        "## 73-row signal 当前判定",
        "",
    ])
    for k, v in counts["signal_decision_counts"].items():
        md.append(f"- {k}: {v}")
    md.extend([
        "",
        "## 必须继续的缺口",
        "",
        "- ClaudeCode 大进程当前还没有有效 ledger rows，不能用它替代 B 线厚内容。",
        "- `blocked` 行不是删除，而是题面、选项、答案、细则、视觉核读或模块边界尚未闭合。",
        "- `同类索引` 多数是重复/参考源行或只作索引训练的行，不得冒充新增正文题。",
        "- 2026 二模在本轮 source roots 扫描中为 0，口径只能写“本轮 source roots 未发现”。",
        "",
        "## 输出文件",
        "",
        "- `CODEX_EXHAUSTIVE_DECISION_MATRIX.csv`",
        "- `CODEX_EXHAUSTIVE_CANONICAL_DECISION_MATRIX.csv`",
        "- `CODEX_DUPLICATE_OR_REFERENCE_AUDIT.csv`",
        "- `CODEX_SIGNAL_CLOSURE_MATRIX.csv`",
        "- `CODEX_EXHAUSTIVE_DECISION_SUMMARY.json`",
        "",
    ])
    (CODEX_DIR / "CODEX_PHASE05_PHASE12_BASELINE.md").write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(counts, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
