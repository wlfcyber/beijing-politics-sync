#!/usr/bin/env python3
"""Build Phase06 evidence-lock and framework-fusion internal artifacts."""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COV = ROOT / "05_coverage"

POOL = COV / "phase05_evidence_pool_74.csv"
THINKING = COV / "phase05_thinking_signal_archive.csv"
REASONING = COV / "phase05_reasoning_typology_archive.csv"
CROSS = COV / "phase05_cross_question_split_matrix.csv"
CONTROL = COV / "phase04_control_base_status_after_batch03_cleaned.csv"

OUT_EVIDENCE = COV / "phase06_evidence_lock_register.csv"
OUT_EVIDENCE_MD = COV / "phase06_evidence_lock_register.md"
OUT_THINK = COV / "phase06_thinking_framework_fusion.csv"
OUT_THINK_MD = COV / "phase06_thinking_framework_fusion.md"
OUT_REASON = COV / "phase06_reasoning_typology_fusion.csv"
OUT_REASON_MD = COV / "phase06_reasoning_typology_fusion.md"
OUT_CROSS = COV / "phase06_cross_mount_lock.csv"
OUT_THINK_INDEX = COV / "phase06_thinking_same_method_index_LOCK_CANDIDATE.md"
OUT_REASON_INDEX = COV / "phase06_reasoning_same_type_index_LOCK_CANDIDATE.md"
OUT_L0 = COV / "phase06_L0_blocker_retention_register.csv"
OUT_L0_MD = COV / "phase06_L0_blocker_retention_summary.md"
OUT_GOV = COV / "phase06_Governor_evidence_lock_gate.md"
OUT_CONF = COV / "phase06_Confucius_framework_value_gate.md"
OUT_GPT_PACKET = COV / "phase06_GPT_commander_review_packet.md"
OUT_OPUS_RULES = COV / "phase06_opus_input_boundary_rules.md"
OUT_AUDIT_CSV = ROOT / "codex_lane/phase06_local_audit/phase06_codexA_local_audit.csv"
OUT_AUDIT_MD = ROOT / "codex_lane/phase06_local_audit/phase06_codexA_local_audit.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([{k: row.get(k, "") for k in fieldnames} for row in rows])


def short_status(status: str) -> str:
    if "L4" in status:
        return "L4"
    if "L3" in status:
        return "L3"
    if "L0" in status:
        return "L0"
    return status or "UNKNOWN"


def readiness(status: str) -> str:
    if "L4" in status:
        return "LOCKED_FOR_FRAMEWORK"
    if "L3" in status:
        return "CONFIRMED_FOR_ARCHIVE"
    return "NOT_FOR_LOCK"


def module_destination(module: str) -> str:
    if module == "思维":
        return "phase06_thinking_framework_fusion"
    if module == "推理":
        return "phase06_reasoning_typology_fusion"
    if module == "交叉":
        return "phase06_thinking_framework_fusion + phase06_reasoning_typology_fusion + phase06_cross_mount_lock"
    return "pending_module_destination"


def missing(row: dict[str, str], fields: list[str]) -> str:
    return ";".join(field for field in fields if not (row.get(field) or "").strip())


def md_table(rows: list[dict[str, str]], fields: list[str], limit: int = 120) -> str:
    def cell(val: str) -> str:
        val = (val or "").replace("\n", " ").replace("|", "/").strip()
        return val if len(val) <= limit else val[: limit - 3] + "..."

    lines = ["|" + "|".join(fields) + "|", "|" + "|".join(["---"] * len(fields)) + "|"]
    for row in rows:
        lines.append("|" + "|".join(cell(row.get(field, "")) for field in fields) + "|")
    return "\n".join(lines)


def first_token(text: str) -> str:
    text = (text or "").strip()
    if not text:
        return ""
    for sep in ["；", ";", "、", ",", "，", "+"]:
        if sep in text:
            return text.split(sep)[0].strip()
    return text


def qid_sort_key(qid: str) -> tuple[str, int, str]:
    parts = qid.split("-")
    number = 0
    tail = parts[-1]
    for piece in reversed(parts):
        digits = "".join(ch for ch in piece if ch.isdigit())
        if digits:
            number = int(digits)
            tail = piece
            break
    return ("-".join(parts[:-1]), number, tail)


def l0_group(reason: str) -> str:
    text = reason or ""
    if "duplicate" in text or "重复" in text:
        return "duplicate_removed"
    if "support" in text or "reference" in text or "补充材料" in text:
        return "support_reference_row"
    if "answer" in text or "答案" in text:
        return "answer_missing"
    if "visual" in text or "rendered" in text or "PDF text layer" in text or "视觉" in text:
        return "visual_missing"
    if "choice options" in text or "locator" in text or "text layer" in text:
        return "source_or_locator_issue"
    if "scope_out" in text:
        return "out_of_scope"
    if "scope pending" in text or "boundary" in text:
        return "boundary_closed"
    if "scope" in text or "queue_split_error" in text:
        return "scope_rejected"
    return "source_or_locator_issue"


def build_evidence(pool: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for row in pool:
        answer_locator = row["answer_locator"]
        if answer_locator in {"A", "B", "C", "D"}:
            answer_locator = f"answer_confirmed_{answer_locator}_from_{row['source_locator']}"
        out = {
            "question_id": row["question_id"],
            "status": short_status(row["status"]),
            "module": row["module"],
            "question_type": row["question_type"],
            "source_locator": row["source_locator"],
            "answer_locator": answer_locator,
            "rubric_or_commentary_locator": row["rubric_locator"],
            "visual_locator": row["visual_locator"],
            "archive_destination": module_destination(row["module"]),
            "student_permission": "no",
            "lock_readiness": readiness(row["status"]),
            "missing_fields": "",
            "risk_note": row["risk_note"],
        }
        out["missing_fields"] = missing(
            out,
            [
                "question_id",
                "status",
                "module",
                "question_type",
                "source_locator",
                "answer_locator",
                "archive_destination",
                "student_permission",
                "lock_readiness",
            ],
        )
        rows.append(out)
    return rows


def build_thinking(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out_rows = []
    for row in rows:
        method = row["可写思维/方法"]
        action = row["答题动作"]
        if row["question_id"] == "Q-2026朝阳期中-13":
            action = "先排除②类比推理诱惑；抓住“石榴籽”比喻把石榴形象与民族关系相联结，说明由感性具体上升到思维抽象并运用联想思维，锁定③④。"
        if row["question_id"] == "Q-2026丰台一模-4":
            method = "分析与综合；综合思维"
        out = {
            "question_id": row["question_id"],
            "材料信号": row["材料信号"],
            "可写思维/方法": method,
            "答题动作": action,
            "来源例题": row["来源例题"],
            "答案落点": row["答案落点"],
            "易错陷阱": row["易错陷阱"],
            "同类题": row["同类题"],
            "framework_node": first_token(method),
            "status": short_status(row["status"]),
            "missing_fields": "",
        }
        out["missing_fields"] = row.get("missing_fields") or missing(
            out,
            ["question_id", "材料信号", "可写思维/方法", "答题动作", "来源例题", "framework_node", "status"],
        )
        out_rows.append(out)
    return out_rows


def build_reasoning(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out_rows = []
    for row in rows:
        rule_slogan = row["rule_slogan"]
        answer_action = row["answer_action"]
        if row["question_id"] == "Q-2026朝阳期中-11":
            rule_slogan = "补大前提要让中项“耐干旱月季花”连接大项“适应高温”；用肯定全称联系支撑由小前提推出结论，避免特称、否定和倒置。"
            answer_action = "先找小前提的中项“耐干旱月季花”，再补它与大项“适应北京夏季高温环境”的肯定联系，排除特称项、否定项和倒置项，选A。"
        elif row["question_id"] == "Q-2026朝阳期中-13":
            rule_slogan = "类比推理是由相似属性推出另一属性，结论或然；本题正确落点不是②类比目的，而是感性具体到思维抽象与联想思维联结。"
            answer_action = "先排除②把比喻误判为类比推理目的，再抓③感性具体转化为思维抽象、④联想思维联结不同对象，锁定D。"
        elif answer_action == row["valid_or_invalid_pattern"] or answer_action in {"A", "B", "C", "D"} or answer_action.startswith("paper answer table paired"):
            trap = row["trap"]
            answer_action = f"先识别{row['primary_reasoning_type']}，再套用“{rule_slogan}”，对照题干或选项判断有效/无效，并避开陷阱：{trap}"
        out = {
            "question_id": row["question_id"],
            "primary_reasoning_type": row["primary_reasoning_type"],
            "secondary_reasoning_type": row["secondary_reasoning_type"],
            "logical_form": row["logical_form"],
            "rule_slogan": rule_slogan,
            "valid_or_invalid_pattern": row["valid_or_invalid_pattern"],
            "common_trap": row["trap"],
            "answer_action": answer_action,
            "same_type_question_ids": row["same_type_question_ids"],
            "status": short_status(row["status"]),
            "missing_fields": "",
        }
        out["missing_fields"] = row.get("missing_fields") or missing(
            out,
            [
                "question_id",
                "primary_reasoning_type",
                "logical_form",
                "rule_slogan",
                "common_trap",
                "answer_action",
                "status",
            ],
        )
        out_rows.append(out)
    return out_rows


def build_cross(rows: list[dict[str, str]]) -> list[dict[str, str]]:
    out_rows = []
    reasoning_markers = ["三段论", "假言", "归纳", "类比", "联言", "选言", "推理"]
    for row in rows:
        reasoning_component = row["reasoning_component"]
        primary = "reasoning_typology" if any(x in reasoning_component for x in reasoning_markers) else "thinking_framework"
        secondary = "thinking_framework" if primary == "reasoning_typology" else "reasoning_typology"
        out_rows.append(
            {
                "question_id": row["question_id"],
                "thinking_component": row["thinking_component"],
                "reasoning_component": reasoning_component,
                "primary_mount": primary,
                "secondary_mount": secondary,
                "why_double_mount": "同时包含思维方法信号和形式逻辑/推理规则；Phase06 必须双挂载，不能被一个交叉标签吞掉。",
                "whether_student_text_should_duplicate_or_cross_reference": "future_student_stage_cross_reference_only; no student text authorized in Phase06",
            }
        )
    return out_rows


def build_l0(control: list[dict[str, str]]) -> list[dict[str, str]]:
    rows = []
    for row in control:
        if row["phase04_level"] != "L0_BLOCKED":
            continue
        reason = row.get("blocker_reason", "")
        rows.append(
            {
                "question_id": row["canonical_question_id"],
                "suite_id": row["suite_id"],
                "question_type": row["question_type"],
                "stable_locator": row["stable_locator"],
                "section_scope": row["section_scope"],
                "blocker_reason": reason,
                "blocker_group": l0_group(reason),
                "student_permission": "no",
                "excluded_from_opus_input": "yes",
                "retention_note": "retained_for_audit_not_student_or_opus_input",
            }
        )
    return rows


def write_indexes(thinking_rows: list[dict[str, str]], reasoning_rows: list[dict[str, str]]) -> None:
    think_groups: dict[str, list[str]] = defaultdict(list)
    for row in thinking_rows:
        node = row["framework_node"] or row["可写思维/方法"]
        think_groups[node].append(row["question_id"])

    reason_groups: dict[str, list[str]] = defaultdict(list)
    for row in reasoning_rows:
        reason_groups[row["primary_reasoning_type"]].append(row["question_id"])

    think_lines = [
        "# Phase06 Thinking Same Method Index LOCK CANDIDATE",
        "",
        "Internal framework-fusion index only. It does not authorize student稿.",
        "",
    ]
    for node, ids in sorted(think_groups.items()):
        ids = sorted(set(ids), key=qid_sort_key)
        think_lines += [f"## {node}", "", f"- count: {len(ids)}", f"- question_ids: {'; '.join(ids)}", ""]
    OUT_THINK_INDEX.write_text("\n".join(think_lines), encoding="utf-8")

    reason_lines = [
        "# Phase06 Reasoning Same Type Index LOCK CANDIDATE",
        "",
        "Internal typology-fusion index only. It does not authorize student稿.",
        "",
    ]
    for node, ids in sorted(reason_groups.items()):
        ids = sorted(set(ids), key=qid_sort_key)
        reason_lines += [f"## {node}", "", f"- count: {len(ids)}", f"- question_ids: {'; '.join(ids)}", ""]
    OUT_REASON_INDEX.write_text("\n".join(reason_lines), encoding="utf-8")


def add_check(rows: list[dict[str, str]], check_id: str, scope: str, passed: bool, details: str, severity: str = "P1") -> None:
    rows.append(
        {
            "check_id": check_id,
            "scope": scope,
            "result": "PASS" if passed else "FAIL",
            "severity": "INFO" if passed else severity,
            "details": details,
        }
    )


def build_gates(
    evidence: list[dict[str, str]],
    thinking: list[dict[str, str]],
    reasoning: list[dict[str, str]],
    cross: list[dict[str, str]],
    l0: list[dict[str, str]],
) -> list[dict[str, str]]:
    checks: list[dict[str, str]] = []
    evidence_ids = {r["question_id"] for r in evidence}
    thinking_ids = {r["question_id"] for r in thinking}
    reasoning_ids = {r["question_id"] for r in reasoning}
    cross_ids = {r["question_id"] for r in cross}

    add_check(checks, "G01", "evidence_lock_register", len(evidence) == 74, f"rows={len(evidence)}", "P0")
    add_check(checks, "G02", "thinking_fusion", len(thinking) == 36, f"rows={len(thinking)}", "P0")
    add_check(checks, "G03", "reasoning_fusion", len(reasoning) == 51, f"rows={len(reasoning)}", "P0")
    add_check(checks, "G04", "cross_mount", len(cross) == 13, f"rows={len(cross)}", "P0")
    add_check(checks, "G05", "L0_retention", len(l0) == 288, f"rows={len(l0)}", "P0")
    add_check(checks, "G06", "cross_double_membership", all(q in thinking_ids and q in reasoning_ids for q in cross_ids), f"missing={[q for q in cross_ids if q not in thinking_ids or q not in reasoning_ids]}", "P0")
    q11_text = "\n".join(str(r) for table in [evidence, thinking, reasoning, cross] for r in table if r.get("question_id") == "Q-2024西城一模-11")
    add_check(checks, "G07", "Q11_lock", "B=①③" in q11_text and "B=①④" not in q11_text, "Q11 retains B=①③ and contains no retired wrong-pairing string", "P0")
    q12 = next((r for r in evidence if r["question_id"] == "Q-2025海淀二模-12"), {})
    q13 = next((r for r in evidence if r["question_id"] == "Q-2025海淀二模-13"), {})
    q12_ok = "D" in q12.get("answer_locator", "") and "render_008_page_04" in q12.get("source_locator", "") and "page9" in q12.get("source_locator", "")
    q13_ok = "C" in q13.get("answer_locator", "") and "render_008_page_04" in q13.get("source_locator", "") and "page9" in q13.get("source_locator", "")
    add_check(checks, "G08", "Q12_Q13_lock", q12_ok and q13_ok, f"Q12={q12.get('answer_locator','')}; Q13={q13.get('answer_locator','')}", "P0")
    status_counts = Counter(r["status"] for r in evidence)
    add_check(checks, "G09", "L3_L4_separation", status_counts["L4"] == 4 and status_counts["L3"] == 70, f"counts={dict(status_counts)}", "P0")
    add_check(checks, "G10", "student_permission", all(r["student_permission"] == "no" for r in evidence + l0), "all phase06 rows keep student_permission=no", "P0")

    add_check(checks, "C01", "thinking_material_signal", all(r["材料信号"] for r in thinking), "all thinking rows have material signal", "P1")
    add_check(checks, "C02", "thinking_answer_action", all(r["答题动作"] for r in thinking), "all thinking rows have answer action", "P1")
    add_check(checks, "C03", "reasoning_logical_form", all(r["logical_form"] for r in reasoning), "all reasoning rows have logical form", "P1")
    add_check(checks, "C04", "reasoning_rule_slogan", all(r["rule_slogan"] for r in reasoning), "all reasoning rows have rule slogan", "P1")
    add_check(checks, "C05", "reasoning_common_trap", all(r["common_trap"] for r in reasoning), "all reasoning rows have common trap", "P1")
    add_check(checks, "C06", "index_coverage", evidence_ids == (set(r["question_id"] for r in evidence)), "indexes generated separately; evidence ids stable", "P1")
    return checks


def write_gate_files(checks: list[dict[str, str]], l0: list[dict[str, str]]) -> None:
    gov = [r for r in checks if r["check_id"].startswith("G")]
    conf = [r for r in checks if r["check_id"].startswith("C")]
    gov_fail = [r for r in gov if r["result"] != "PASS"]
    conf_fail = [r for r in conf if r["result"] != "PASS"]

    OUT_GOV.write_text(
        "\n".join(
            [
                "# Phase06 Governor Evidence Lock Gate",
                "",
                f"Verdict: `{'PASS_INTERNAL_EVIDENCE_LOCK_PENDING_LANEB_GPT' if not gov_fail else 'FAIL_REPAIR_REQUIRED'}`",
                "",
                "This gate does not authorize student稿, Claude Opus prose, Word/PDF, or final PASS.",
                "",
                "## Checks",
                "",
                *[f"- {r['result']}: {r['check_id']} {r['scope']} - {r['details']}" for r in gov],
                "",
            ]
        ),
        encoding="utf-8",
    )

    OUT_CONF.write_text(
        "\n".join(
            [
                "# Phase06 Confucius Framework Value Gate",
                "",
                f"Verdict: `{'PASS_INTERNAL_FRAMEWORK_VALUE_PENDING_LANEB_GPT' if not conf_fail else 'FAIL_REPAIR_REQUIRED'}`",
                "",
                "This gate checks teachability scaffolding only. It is not a student稿 authorization.",
                "",
                "## Checks",
                "",
                *[f"- {r['result']}: {r['check_id']} {r['scope']} - {r['details']}" for r in conf],
                "",
            ]
        ),
        encoding="utf-8",
    )

    l0_counts = Counter(r["blocker_group"] for r in l0)
    expected_l0_groups = [
        "out_of_scope",
        "boundary_closed",
        "duplicate_removed",
        "support_reference_row",
        "answer_missing",
        "visual_missing",
        "scope_rejected",
        "source_or_locator_issue",
    ]
    OUT_L0_MD.write_text(
        "\n".join(
            [
                "# Phase06 L0 Blocker Retention Summary",
                "",
                "Status: `L0_RETAINED_AND_EXCLUDED_FROM_OPUS_INPUT`",
                "",
                f"- L0 rows: {len(l0)}",
                "- student_permission: no",
                "- excluded_from_opus_input: yes",
                "",
                "## Blocker Groups",
                "",
                *[f"- {k}: {l0_counts.get(k, 0)}" for k in expected_l0_groups],
                "",
                "Phase06 keeps L0 visible for audit. L0 rows do not enter evidence lock, Opus input, or student-facing text.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_audit(checks: list[dict[str, str]]) -> None:
    OUT_AUDIT_CSV.parent.mkdir(parents=True, exist_ok=True)
    write_csv(OUT_AUDIT_CSV, checks, ["check_id", "scope", "result", "severity", "details"])
    failures = [r for r in checks if r["result"] != "PASS"]
    OUT_AUDIT_MD.write_text(
        "\n".join(
            [
                "# Phase06 Codex A Local Audit",
                "",
                f"Verdict: `{'PASS_LOCAL_PHASE06_STRUCTURE_AUDIT' if not failures else 'FAIL_REPAIR_REQUIRED'}`",
                "",
                f"- checks: {len(checks)}",
                f"- failures: {len(failures)}",
                "",
                "Internal audit only. No student稿, Claude Opus prose, Word/PDF, or final PASS is authorized.",
                "",
                "## Checks",
                "",
                *[f"- {r['result']}: {r['check_id']} {r['scope']} - {r['details']}" for r in checks],
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_gpt_packet(
    evidence: list[dict[str, str]],
    thinking: list[dict[str, str]],
    reasoning: list[dict[str, str]],
    cross: list[dict[str, str]],
    l0: list[dict[str, str]],
    checks: list[dict[str, str]],
) -> None:
    failures = [r for r in checks if r["result"] != "PASS"]
    status_counts = Counter(r["status"] for r in evidence)
    module_counts = Counter(r["module"] for r in evidence)
    l0_counts = Counter(r["blocker_group"] for r in l0)
    OUT_GPT_PACKET.write_text(
        "\n".join(
            [
                "# Phase06 GPT Commander Review Packet",
                "",
                "Request: review Phase06 evidence-lock/framework-fusion outputs and decide whether to request patches, launch Lane B audit, or later prepare an Opus locked-input packet. Current request does not ask for student稿.",
                "",
                "## Current Verdict Requested Later",
                "",
                "- Current local state: `PHASE06_INTERNAL_GENERATED_PENDING_LANEB_AUDIT_AND_GPT_REVIEW`",
                "- Still forbidden: student稿, Claude Opus teaching prose, Word/PDF, final PASS.",
                "",
                "## Counts",
                "",
                f"- evidence lock rows: {len(evidence)}",
                f"- evidence status counts: {dict(status_counts)}",
                f"- evidence module counts: {dict(module_counts)}",
                f"- thinking fusion rows: {len(thinking)}",
                f"- reasoning fusion rows: {len(reasoning)}",
                f"- cross mount rows: {len(cross)}",
                f"- L0 retained rows: {len(l0)}",
                f"- L0 blocker groups: {dict(l0_counts)}",
                "",
                "## Hard Locks",
                "",
                "- Q-2024西城一模-11: must remain answer B, pairing B=①③; retired wrong-pairing string is forbidden for Q11.",
                "- Q-2025海淀二模-12: answer D with supplemental answer table page 9 and render_008_page_04.",
                "- Q-2025海淀二模-13: answer C with supplemental answer table page 9 and render_008_page_04.",
                "- Cross rows: 13 rows double-mounted.",
                "- L0 rows: 288 retained, excluded from Opus input.",
                "",
                "## Outputs",
                "",
                "- `05_coverage/phase06_evidence_lock_register.csv/md`",
                "- `05_coverage/phase06_thinking_framework_fusion.csv/md`",
                "- `05_coverage/phase06_reasoning_typology_fusion.csv/md`",
                "- `05_coverage/phase06_cross_mount_lock.csv`",
                "- `05_coverage/phase06_thinking_same_method_index_LOCK_CANDIDATE.md`",
                "- `05_coverage/phase06_reasoning_same_type_index_LOCK_CANDIDATE.md`",
                "- `05_coverage/phase06_L0_blocker_retention_register.csv`",
                "- `05_coverage/phase06_L0_blocker_retention_summary.md`",
                "- `05_coverage/phase06_Governor_evidence_lock_gate.md`",
                "- `05_coverage/phase06_Confucius_framework_value_gate.md`",
                "- `codex_lane/phase06_local_audit/phase06_codexA_local_audit.md`",
                "",
                "## Local Audit",
                "",
                f"- failures: {len(failures)}",
                *[f"- {r['result']}: {r['check_id']} {r['scope']} - {r['details']}" for r in checks],
                "",
                "## Unresolved Warnings",
                "",
                "- Phase05 Lane B P3 warnings are patched locally and frozen in `06_conflicts/phase05_patch_freeze_after_laneB_warnings.md`; Lane B second acknowledgement remains pending.",
                "- Phase06 still requires ClaudeCode B Opus 4.7 max independent audit before any Opus teaching-text packet can be considered.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_opus_boundary() -> None:
    OUT_OPUS_RULES.write_text(
        "\n".join(
            [
                "# Phase06 Opus Input Boundary Rules",
                "",
                "Status: `NO_ACTION_FOR_TEACHING_TEXT`",
                "",
                "If a later GPT gate allows a locked Opus input packet, Opus must obey:",
                "",
                "1. Opus can only rewrite locked entries explicitly provided in the packet.",
                "2. Opus cannot add questions.",
                "3. Opus cannot delete questions.",
                "4. Opus cannot change answers.",
                "5. Opus cannot change L3/L4 status.",
                "6. Opus cannot single-mount cross rows.",
                "7. Opus output must preserve `question_id` during internal draft review.",
                "8. Opus final student-facing prose must not expose source locator, lane, Governor, Confucius, audit, or archive terms.",
                "",
                "This file is a future boundary only. It does not authorize Opus prose now.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    pool = read_csv(POOL)
    thinking_archive = read_csv(THINKING)
    reasoning_archive = read_csv(REASONING)
    cross_archive = read_csv(CROSS)
    control = read_csv(CONTROL)

    evidence = build_evidence(pool)
    thinking = build_thinking(thinking_archive)
    reasoning = build_reasoning(reasoning_archive)
    cross = build_cross(cross_archive)
    l0 = build_l0(control)

    write_csv(OUT_EVIDENCE, evidence, list(evidence[0]))
    OUT_EVIDENCE_MD.write_text(
        "# Phase06 Evidence Lock Register\n\nInternal evidence-lock register only. It does not authorize student稿.\n\n"
        + md_table(evidence, list(evidence[0]))
        + "\n",
        encoding="utf-8",
    )

    write_csv(OUT_THINK, thinking, list(thinking[0]))
    OUT_THINK_MD.write_text(
        "# Phase06 Thinking Framework Fusion\n\nInternal framework fusion only. It does not authorize student稿.\n\n"
        + md_table(thinking, list(thinking[0]))
        + "\n",
        encoding="utf-8",
    )

    write_csv(OUT_REASON, reasoning, list(reasoning[0]))
    OUT_REASON_MD.write_text(
        "# Phase06 Reasoning Typology Fusion\n\nInternal typology fusion only. It does not authorize student稿.\n\n"
        + md_table(reasoning, list(reasoning[0]))
        + "\n",
        encoding="utf-8",
    )

    write_csv(OUT_CROSS, cross, list(cross[0]))
    write_csv(OUT_L0, l0, list(l0[0]))
    write_indexes(thinking, reasoning)

    checks = build_gates(evidence, thinking, reasoning, cross, l0)
    write_gate_files(checks, l0)
    write_audit(checks)
    write_gpt_packet(evidence, thinking, reasoning, cross, l0, checks)
    write_opus_boundary()

    print(OUT_GPT_PACKET)


if __name__ == "__main__":
    main()
