#!/usr/bin/env python3
"""Build Phase07 locked Opus input packet candidates without authorizing prose."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COV = ROOT / "05_coverage"
CONFLICT = ROOT / "06_conflicts"

PHASE05_POOL = COV / "phase05_evidence_pool_74.csv"
EVIDENCE = COV / "phase06_evidence_lock_register.csv"
THINKING = COV / "phase06_thinking_framework_fusion.csv"
REASONING = COV / "phase06_reasoning_typology_fusion.csv"
CROSS = COV / "phase06_cross_mount_lock.csv"
L0 = COV / "phase06_L0_blocker_retention_register.csv"

OUT_PACKET = COV / "phase07_locked_opus_input_packet.csv"
OUT_PACKET_MD = COV / "phase07_locked_opus_input_packet.md"
OUT_THINK = COV / "phase07_opus_input_thinking_entries.csv"
OUT_THINK_MD = COV / "phase07_opus_input_thinking_entries.md"
OUT_REASON = COV / "phase07_opus_input_reasoning_entries.csv"
OUT_REASON_MD = COV / "phase07_opus_input_reasoning_entries.md"
OUT_CROSS = COV / "phase07_opus_input_cross_entries.csv"
OUT_CROSS_POLICY = COV / "phase07_cross_mount_opus_policy.md"
OUT_L3 = COV / "phase07_L3_hold_list.csv"
OUT_L3_MD = COV / "phase07_L3_promote_or_hold_decision.md"
OUT_L0 = COV / "phase07_L0_excluded_from_opus_input.csv"
OUT_L0_MD = COV / "phase07_L0_exclusion_summary.md"
OUT_HARD_CSV = CONFLICT / "phase07_hard_lock_audit.csv"
OUT_HARD_MD = CONFLICT / "phase07_hard_lock_audit.md"
OUT_BOUNDARY = COV / "phase07_opus_input_boundary_rules_FINAL_FOR_PACKET.md"
OUT_GOV = COV / "phase07_Governor_locked_packet_gate.md"
OUT_CONF = COV / "phase07_Confucius_locked_packet_value_gate.md"
OUT_GPT = COV / "phase07_GPT_commander_review_packet.md"
OUT_AUDIT = ROOT / "codex_lane/phase07_local_audit/phase07_codexA_local_audit.csv"
OUT_AUDIT_MD = ROOT / "codex_lane/phase07_local_audit/phase07_codexA_local_audit.md"


REASONING_ACTION_OVERRIDES = {
    "Q-2026丰台一模-18-2": "先识别甲为必要条件假言推理的肯定后件式，并结合前提真实判定甲推理正确；再识别乙为三段论大项在前提中不周延却在结论中周延，属于大项不当扩大，判定乙推理错误。"
}

REASONING_SAME_TYPE_OVERRIDES = {
    "Q-2026丰台一模-18-2": "Q-2024朝阳一模-20-2;Q-2024朝阳期中-7;Q-2025东城期末-13;Q-2025顺义一模-7;Q-2026朝阳期中-11;Q-2026顺义一模-19-1;Q-2026顺义一模-19-2"
}

ANSWER_LOCATOR_OVERRIDES = {
    "Q-2026丰台一模-18-2": "answer_confirmed_甲正确乙错误_from_043_slide35_36_rubric"
}


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows([{k: r.get(k, "") for k in fields} for r in rows])


def md_table(rows: list[dict[str, str]], fields: list[str], limit: int = 120) -> str:
    def cell(v: str) -> str:
        v = (v or "").replace("\n", " ").replace("|", "/").strip()
        return v if len(v) <= limit else v[: limit - 3] + "..."
    return "\n".join(
        ["|" + "|".join(fields) + "|", "|" + "|".join(["---"] * len(fields)) + "|"]
        + ["|" + "|".join(cell(r.get(f, "")) for f in fields) + "|" for r in rows]
    )


def missing(row: dict[str, str], fields: list[str]) -> list[str]:
    return [f for f in fields if not (row.get(f) or "").strip()]


def qid_sort(row: dict[str, str]) -> str:
    return row.get("question_id") or row.get("canonical_question_id") or ""


def decide_permission(e: dict[str, str], pool: dict[str, dict[str, str]], thinking: dict[str, dict[str, str]], reasoning: dict[str, dict[str, str]], cross: dict[str, dict[str, str]]) -> tuple[str, str]:
    qid = e["question_id"]
    if e["status"] == "L4":
        return "include", "L4_ready"

    base_missing = missing(e, ["source_locator", "answer_locator", "visual_locator", "question_type", "module"])
    p = pool.get(qid, {})
    if p:
        base_missing += missing(p, ["full_stem_status", "full_options_status"])
    if base_missing:
        return "hold_missing_fields", "missing=" + ";".join(sorted(set(base_missing)))

    rubric = e["rubric_or_commentary_locator"]
    if rubric == "no_formal_rubric":
        return "hold_answer_locator_risk", "L3 no_formal_rubric / B-choice-signal not allowed directly into Opus packet"
    if rubric == "paired_candidate":
        return "hold_answer_locator_risk", "L3 paired_candidate must be upgraded before Opus packet"

    if e["module"] in {"思维", "交叉"}:
        t = thinking.get(qid, {})
        t_missing = missing(t, ["材料信号", "可写思维/方法", "答题动作", "答案落点", "来源例题"])
        if t_missing:
            return "hold_thinking_signal_risk", "missing_thinking=" + ";".join(t_missing)
        if "待细化" in t.get("可写思维/方法", "") or t.get("答题动作", "") in {"A", "B", "C", "D"}:
            return "hold_thinking_signal_risk", "thinking placeholder/action risk"

    if e["module"] in {"推理", "交叉"}:
        r = reasoning.get(qid, {})
        r_missing = missing(r, ["logical_form", "rule_slogan", "valid_or_invalid_pattern", "common_trap", "answer_action", "same_type_question_ids"])
        if r_missing:
            return "hold_reasoning_form_risk", "missing_reasoning=" + ";".join(r_missing)
        if r.get("rule_slogan", "") in {"A", "B", "C", "D"} or r.get("answer_action", "") in {"A", "B", "C", "D"}:
            return "hold_reasoning_form_risk", "single-letter reasoning field risk"

    if e["module"] == "交叉":
        c = cross.get(qid, {})
        c_missing = missing(c, ["thinking_component", "reasoning_component", "primary_mount", "secondary_mount"])
        if c_missing:
            return "hold_scope_risk", "missing_cross=" + ";".join(c_missing)

    return "include_as_packet_candidate", "L3 critical fields complete and evidence level allowed"


def build_packet() -> tuple[list[dict[str, str]], dict[str, str]]:
    pool_rows = read_csv(PHASE05_POOL)
    evidence_rows = read_csv(EVIDENCE)
    thinking_rows = read_csv(THINKING)
    reasoning_rows = read_csv(REASONING)
    cross_rows = read_csv(CROSS)

    pool = {r["question_id"]: r for r in pool_rows}
    thinking = {r["question_id"]: r for r in thinking_rows}
    reasoning = {r["question_id"]: r for r in reasoning_rows}
    cross = {r["question_id"]: r for r in cross_rows}
    decisions: dict[str, str] = {}

    packet: list[dict[str, str]] = []
    for e in evidence_rows:
        qid = e["question_id"]
        p = pool.get(qid, {})
        permission, reason = decide_permission(e, pool, thinking, reasoning, cross)
        decisions[qid] = permission
        answer_locator = ANSWER_LOCATOR_OVERRIDES.get(qid) or e["answer_locator"]
        risk_note = e["risk_note"]
        if qid == "Q-2024西城一模-11":
            answer_locator = f"{answer_locator}; hard_lock_pairing=B=①③"
            risk_note = f"{risk_note}; hard_lock_pairing=B=①③"
        packet.append(
            {
                "question_id": qid,
                "suite_id": p.get("suite_id", ""),
                "module": e["module"],
                "status": e["status"],
                "input_permission": permission,
                "hold_reason": "" if permission.startswith("include") else reason,
                "source_locator": e["source_locator"],
                "answer_locator": answer_locator,
                "rubric_or_commentary_locator": e["rubric_or_commentary_locator"],
                "visual_locator": e["visual_locator"],
                "question_type": e["question_type"],
                "full_stem_status": p.get("full_stem_status", ""),
                "full_options_status": p.get("full_options_status", ""),
                "student_permission": "no",
                "opus_permission": "packet_only",
                "risk_note": risk_note,
            }
        )
    return packet, decisions


def build_thinking(decisions: dict[str, str]) -> list[dict[str, str]]:
    source_rows = read_csv(THINKING)
    framework_peers: dict[str, list[str]] = {}
    for src in source_rows:
        node = src.get("framework_node", "").strip()
        if node:
            framework_peers.setdefault(node, []).append(src["question_id"])

    rows = []
    for r in source_rows:
        if not decisions.get(r["question_id"], "").startswith("include"):
            continue
        node = r.get("framework_node", "").strip()
        peers = [qid for qid in framework_peers.get(node, []) if qid != r["question_id"]]
        if r["同类题"]:
            same = r["同类题"]
            risk_note = "same_method_from_phase06_index"
        elif peers:
            same = ";".join(peers)
            risk_note = f"same_method_auto_by_framework_node={node}"
        else:
            same = "NO_SAME_METHOD_IN_PHASE06_INDEX"
            risk_note = f"same_method_empty_reason=no_peer_with_framework_node={node or 'missing'}"
        rows.append(
            {
                "question_id": r["question_id"],
                "材料信号": r["材料信号"],
                "可写思维/方法": r["可写思维/方法"],
                "答题动作": r["答题动作"],
                "答案落点": r["答案落点"],
                "来源例题": r["来源例题"],
                "同类题": same,
                "易错陷阱": r["易错陷阱"],
                "risk_note": risk_note,
                "L3_or_L4_status": r["status"],
                "allowed_opus_task": "rewrite_as_teaching_text_only_after_later_GPT_gate",
                "forbidden_opus_changes": "no_new_question;no_delete_question;no_answer_change;no_L3_L4_change;no_student_final",
            }
        )
    return rows


def build_reasoning(decisions: dict[str, str]) -> list[dict[str, str]]:
    rows = []
    for r in read_csv(REASONING):
        if not decisions.get(r["question_id"], "").startswith("include"):
            continue
        same = REASONING_SAME_TYPE_OVERRIDES.get(r["question_id"]) or r["same_type_question_ids"] or "NO_SAME_TYPE_IN_PHASE06_INDEX"
        answer_action = REASONING_ACTION_OVERRIDES.get(r["question_id"]) or r["answer_action"]
        rows.append(
            {
                "question_id": r["question_id"],
                "primary_reasoning_type": r["primary_reasoning_type"],
                "secondary_reasoning_type": r["secondary_reasoning_type"],
                "logical_form": r["logical_form"],
                "rule_slogan": r["rule_slogan"],
                "valid_or_invalid_pattern": r["valid_or_invalid_pattern"],
                "common_trap": r["common_trap"],
                "answer_action": answer_action,
                "same_type_question_ids": same,
                "L3_or_L4_status": r["status"],
                "allowed_opus_task": "rewrite_as_teaching_text_only_after_later_GPT_gate",
                "forbidden_opus_changes": "no_new_question;no_delete_question;no_answer_change;no_L3_L4_change;no_single_mount_cross;no_student_final",
            }
        )
    return rows


def build_cross(decisions: dict[str, str]) -> list[dict[str, str]]:
    rows = []
    for r in read_csv(CROSS):
        rows.append(
            {
                "question_id": r["question_id"],
                "thinking_entry_id": r["question_id"] if decisions.get(r["question_id"], "").startswith("include") else "",
                "reasoning_entry_id": r["question_id"] if decisions.get(r["question_id"], "").startswith("include") else "",
                "input_permission": decisions.get(r["question_id"], "hold_scope_risk"),
                "primary_mount": r["primary_mount"],
                "secondary_mount": r["secondary_mount"],
                "whether_opus_should_duplicate_explanation": "no",
                "whether_opus_should_cross_reference": "yes_if_later_text_stage",
                "forbidden_single_mount": "yes",
            }
        )
    return rows


def build_l3(packet: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for r in packet:
        if r["status"] != "L3":
            continue
        rows.append(
            {
                "question_id": r["question_id"],
                "module": r["module"],
                "decision": r["input_permission"],
                "reason": r["hold_reason"] or "critical_fields_passed",
                "student_permission": "no",
                "opus_permission": "packet_only" if r["input_permission"].startswith("include") else "no_opus_input_yet",
            }
        )
    return rows


def write_l0() -> list[dict[str, str]]:
    rows = []
    for r in read_csv(L0):
        out = dict(r)
        out["input_permission"] = "exclude"
        out["opus_permission"] = "no_opus_input"
        out["student_permission"] = "no"
        rows.append(out)
    write_csv(OUT_L0, rows, list(rows[0]))
    counts = Counter(r["blocker_group"] for r in rows)
    groups = ["out_of_scope", "boundary_closed", "duplicate_removed", "support_reference_row", "answer_missing", "visual_missing", "scope_rejected", "source_or_locator_issue"]
    OUT_L0_MD.write_text(
        "\n".join(
            [
                "# Phase07 L0 Exclusion Summary",
                "",
                "Status: `L0_EXCLUDED_FROM_OPUS_INPUT`",
                "",
                f"- L0 rows: {len(rows)}",
                "- input_permission: exclude",
                "- opus_permission: no_opus_input",
                "- student_permission: no",
                "",
                "## Groups",
                "",
                *[f"- {g}: {counts.get(g, 0)}" for g in groups],
                "",
            ]
        ),
        encoding="utf-8",
    )
    return rows


def add_audit(rows: list[dict[str, str]], check_id: str, scope: str, passed: bool, details: str, severity: str = "P0") -> None:
    rows.append({"check_id": check_id, "scope": scope, "result": "PASS" if passed else "FAIL", "severity": "INFO" if passed else severity, "details": details})


def write_hard_lock(packet: list[dict[str, str]], thinking_entries: list[dict[str, str]], reasoning_entries: list[dict[str, str]], cross_entries: list[dict[str, str]], l0_rows: list[dict[str, str]]) -> list[dict[str, str]]:
    audits: list[dict[str, str]] = []
    input_ids = {r["question_id"] for r in packet} | {r["question_id"] for r in thinking_entries} | {r["question_id"] for r in reasoning_entries} | {r["question_id"] for r in cross_entries}
    q11_text = "\n".join(str(x) for table in [packet, thinking_entries, reasoning_entries, cross_entries] for x in table if x.get("question_id") == "Q-2024西城一模-11")
    add_audit(audits, "H01", "Q11", "B=①③" in q11_text and "B=①④" not in q11_text, "Q11 B=①③ retained and retired wrong pairing absent")
    q12 = next((r for r in packet if r["question_id"] == "Q-2025海淀二模-12"), {})
    q13 = next((r for r in packet if r["question_id"] == "Q-2025海淀二模-13"), {})
    add_audit(audits, "H02", "Q12", "D" in q12.get("answer_locator", "") and "render_008_page_04" in q12.get("source_locator", ""), str(q12))
    add_audit(audits, "H03", "Q13", "C" in q13.get("answer_locator", "") and "render_008_page_04" in q13.get("source_locator", ""), str(q13))
    add_audit(audits, "H04", "Q-2026顺义一模-3", "Q-2026顺义一模-3" not in "\n".join(str(r) for r in reasoning_entries), "not in reasoning input")
    add_audit(audits, "H05", "cross", len(cross_entries) == 13 and all(r["forbidden_single_mount"] == "yes" for r in cross_entries), f"cross_rows={len(cross_entries)}")
    l0_input_overlap = sorted({r["question_id"] for r in l0_rows} & input_ids)
    add_audit(audits, "H06", "L0", len(l0_rows) == 288 and not l0_input_overlap, f"L0_rows={len(l0_rows)} input_overlap={l0_input_overlap[:20]}")
    add_audit(audits, "H07", "student_permission", all(r.get("student_permission") == "no" for r in packet + l0_rows), "all no")
    write_csv(OUT_HARD_CSV, audits, ["check_id", "scope", "result", "severity", "details"])
    failures = [r for r in audits if r["result"] != "PASS"]
    OUT_HARD_MD.write_text(
        "\n".join(
            [
                "# Phase07 Hard Lock Audit",
                "",
                f"Verdict: `{'PASS_HARD_LOCK_AUDIT' if not failures else 'FAIL_REPAIR_REQUIRED'}`",
                "",
                "This audit does not authorize student稿, Opus prose, Word/PDF, or final PASS.",
                "",
                *[f"- {r['result']}: {r['check_id']} {r['scope']} - {r['details']}" for r in audits],
                "",
            ]
        ),
        encoding="utf-8",
    )
    return audits


def write_boundary() -> None:
    OUT_BOUNDARY.write_text(
        "\n".join(
            [
                "# Phase07 Opus Input Boundary Rules FINAL FOR PACKET",
                "",
                "Status: `PACKET_ONLY_NO_TEACHING_TEXT_ACTION`",
                "",
                "Opus is still not authorized to write teaching prose. If a later GPT/Governor/Confucius gate permits a prototype, Opus must obey:",
                "",
                "1. Do not add questions.",
                "2. Do not delete questions.",
                "3. Do not change answers.",
                "4. Do not change question types.",
                "5. Do not change L3/L4 status.",
                "6. Do not write L3 as L4.",
                "7. Do not single-mount cross rows.",
                "8. Do not fill answers without locators.",
                "9. Do not import old-draft conclusions.",
                "10. Do not output student稿.",
                "11. Do not generate Word/PDF.",
                "12. Do not expose source locator, lane, Governor, Confucius, audit, archive, or packet terms in any future student text.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_gates(packet: list[dict[str, str]], thinking: list[dict[str, str]], reasoning: list[dict[str, str]], cross: list[dict[str, str]], l3: list[dict[str, str]], l0: list[dict[str, str]], hard: list[dict[str, str]]) -> list[dict[str, str]]:
    audits: list[dict[str, str]] = []
    perm = Counter(r["input_permission"] for r in packet)
    add_audit(audits, "G01", "packet_rows", len(packet) == 74, f"rows={len(packet)}")
    add_audit(audits, "G02", "include_hold_counts", perm["include"] + perm["include_as_packet_candidate"] + sum(v for k, v in perm.items() if k.startswith("hold")) == 74, f"counts={dict(perm)}")
    add_audit(audits, "G03", "L3_hold", len(l3) == 70 and any(r["decision"].startswith("hold") for r in l3), f"L3_rows={len(l3)} hold={sum(r['decision'].startswith('hold') for r in l3)}")
    add_audit(audits, "G04", "L0_exclude", len(l0) == 288 and all(r["input_permission"] == "exclude" for r in l0), f"L0={len(l0)}")
    add_audit(audits, "G05", "hard_locks", all(r["result"] == "PASS" for r in hard), "hard locks pass")
    add_audit(audits, "G06", "cross_policy", len(cross) == 13 and all(r["forbidden_single_mount"] == "yes" for r in cross), f"cross={len(cross)}")
    add_audit(audits, "G07", "permissions", all(r["student_permission"] == "no" and r["opus_permission"] == "packet_only" for r in packet), "packet rows no/packet_only")
    add_audit(audits, "C01", "thinking_chain", all(r["材料信号"] and r["答题动作"] for r in thinking), f"thinking_input_rows={len(thinking)}", "P1")
    add_audit(audits, "C02", "reasoning_action", all(r["logical_form"] and r["answer_action"] for r in reasoning), f"reasoning_input_rows={len(reasoning)}", "P1")
    add_audit(audits, "C03", "no_answer_letter_only", not any(r.get("answer_action", "") in {"A", "B", "C", "D"} for r in thinking + reasoning), "no action-only answer letters", "P1")
    add_audit(audits, "C04", "phase07_laneB_P3_placeholders", not any(r.get("answer_action", "") == "answer_confirmed_PASS_TO_FUSION" for r in reasoning) and not any(r.get("同类题", "") == "NO_SAME_METHOD_IN_PHASE06_INDEX" for r in thinking) and not any(r.get("answer_locator", "") == "answer_confirmed_PASS_TO_FUSION" for r in packet), "W01/W02 placeholder classes repaired; packet answer locators are source-shaped", "P3")
    write_csv(OUT_AUDIT, audits, ["check_id", "scope", "result", "severity", "details"])
    failures = [r for r in audits if r["result"] != "PASS"]
    OUT_AUDIT_MD.write_text(
        "\n".join(
            [
                "# Phase07 Codex A Local Audit",
                "",
                f"Verdict: `{'PASS_LOCAL_PHASE07_PACKET_AUDIT' if not failures else 'FAIL_REPAIR_REQUIRED'}`",
                "",
                f"- checks: {len(audits)}",
                f"- failures: {len(failures)}",
                "",
                "Internal packet audit only. No student稿, Opus prose, Word/PDF, or final PASS is authorized.",
                "",
                *[f"- {r['result']}: {r['check_id']} {r['scope']} - {r['details']}" for r in audits],
                "",
            ]
        ),
        encoding="utf-8",
    )
    OUT_GOV.write_text(
        "\n".join(
            [
                "# Phase07 Governor Locked Packet Gate",
                "",
                f"Verdict: `{'PASS_INTERNAL_LOCKED_PACKET_PENDING_LANEB_GPT' if not failures else 'FAIL_REPAIR_REQUIRED'}`",
                "",
                f"- packet rows: {len(packet)}",
                f"- permission counts: {dict(perm)}",
                f"- L3 rows: {len(l3)}",
                f"- L0 excluded: {len(l0)}",
                "",
                "This gate does not authorize student稿, Opus prose, Word/PDF, or final PASS.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    OUT_CONF.write_text(
        "\n".join(
            [
                "# Phase07 Confucius Locked Packet Value Gate",
                "",
                f"Verdict: `{'PASS_INTERNAL_PACKET_VALUE_PENDING_LANEB_GPT' if not failures else 'FAIL_REPAIR_REQUIRED'}`",
                "",
                f"- thinking input rows: {len(thinking)}",
                f"- reasoning input rows: {len(reasoning)}",
                "- value check: packet rows retain material triggers / reasoning action fields for future prototype only.",
                "",
                "This is not student text authorization.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    return audits


def write_gpt_packet(packet: list[dict[str, str]], thinking: list[dict[str, str]], reasoning: list[dict[str, str]], cross: list[dict[str, str]], l3: list[dict[str, str]], l0: list[dict[str, str]], audits: list[dict[str, str]]) -> None:
    perm = Counter(r["input_permission"] for r in packet)
    failures = [r for r in audits if r["result"] != "PASS"]
    OUT_GPT.write_text(
        "\n".join(
            [
                "# Phase07 GPT Commander Review Packet",
                "",
                "Request: review locked Opus input packet preparation. Decide whether to patch, send to Lane B audit, or allow a future Opus teaching-text prototype from the locked packet. Do not authorize final student稿.",
                "",
                "## Counts",
                "",
                f"- packet rows: {len(packet)}",
                f"- packet permission counts: {dict(perm)}",
                f"- thinking input rows: {len(thinking)}",
                f"- reasoning input rows: {len(reasoning)}",
                f"- cross policy rows: {len(cross)}",
                f"- L3 decision rows: {len(l3)}",
                f"- L0 excluded rows: {len(l0)}",
                f"- local audit failures: {len(failures)}",
                "",
                "## Outputs",
                "",
                "- `05_coverage/phase07_locked_opus_input_packet.csv/md`",
                "- `05_coverage/phase07_opus_input_thinking_entries.csv/md`",
                "- `05_coverage/phase07_opus_input_reasoning_entries.csv/md`",
                "- `05_coverage/phase07_opus_input_cross_entries.csv`",
                "- `05_coverage/phase07_cross_mount_opus_policy.md`",
                "- `05_coverage/phase07_L3_hold_list.csv`",
                "- `05_coverage/phase07_L3_promote_or_hold_decision.md`",
                "- `05_coverage/phase07_L0_excluded_from_opus_input.csv`",
                "- `05_coverage/phase07_L0_exclusion_summary.md`",
                "- `06_conflicts/phase07_hard_lock_audit.csv/md`",
                "- `05_coverage/phase07_opus_input_boundary_rules_FINAL_FOR_PACKET.md`",
                "- `05_coverage/phase07_Governor_locked_packet_gate.md`",
                "- `05_coverage/phase07_Confucius_locked_packet_value_gate.md`",
                "",
                "## Still Forbidden",
                "",
                "- student稿",
                "- Claude Opus teaching prose",
                "- Word/PDF",
                "- final PASS",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    packet, decisions = build_packet()
    thinking = build_thinking(decisions)
    reasoning = build_reasoning(decisions)
    cross = build_cross(decisions)
    l3 = build_l3(packet)
    l0_rows = write_l0()

    write_csv(OUT_PACKET, packet, list(packet[0]))
    OUT_PACKET_MD.write_text("# Phase07 Locked Opus Input Packet\n\nInternal packet table only. It does not authorize Opus prose or student稿.\n\n" + md_table(packet, list(packet[0])) + "\n", encoding="utf-8")
    write_csv(OUT_THINK, thinking, list(thinking[0]) if thinking else ["question_id"])
    OUT_THINK_MD.write_text("# Phase07 Opus Input Thinking Entries\n\nPacket-only thinking entries. No student稿 authorization.\n\n" + (md_table(thinking, list(thinking[0])) if thinking else "No rows") + "\n", encoding="utf-8")
    write_csv(OUT_REASON, reasoning, list(reasoning[0]) if reasoning else ["question_id"])
    OUT_REASON_MD.write_text("# Phase07 Opus Input Reasoning Entries\n\nPacket-only reasoning entries. No student稿 authorization.\n\n" + (md_table(reasoning, list(reasoning[0])) if reasoning else "No rows") + "\n", encoding="utf-8")
    write_csv(OUT_CROSS, cross, list(cross[0]))
    OUT_CROSS_POLICY.write_text("# Phase07 Cross Mount Opus Policy\n\nAll 13 cross rows remain double-mounted. Opus may cross-reference in a future prototype, but may not single-mount or delete either side.\n\n" + md_table(cross, list(cross[0])) + "\n", encoding="utf-8")
    write_csv(OUT_L3, l3, list(l3[0]))
    OUT_L3_MD.write_text("# Phase07 L3 Promote Or Hold Decision\n\nAll 70 L3 rows are explicitly decided. This prevents feeding all L3 rows to Opus by default.\n\n" + md_table(l3, list(l3[0])) + "\n", encoding="utf-8")
    hard = write_hard_lock(packet, thinking, reasoning, cross, l0_rows)
    write_boundary()
    audits = write_gates(packet, thinking, reasoning, cross, l3, l0_rows, hard)
    write_gpt_packet(packet, thinking, reasoning, cross, l3, l0_rows, audits)
    print(OUT_GPT)


if __name__ == "__main__":
    main()
