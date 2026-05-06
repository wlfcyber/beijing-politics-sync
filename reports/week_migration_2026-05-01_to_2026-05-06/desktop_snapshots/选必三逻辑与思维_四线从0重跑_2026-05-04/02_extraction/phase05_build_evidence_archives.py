#!/usr/bin/env python3
"""Build Phase05 evidence-only archives from the cleaned Phase04 control base."""

from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "05_coverage/phase04_control_base_status_after_batch03_cleaned.csv"
OUT_POOL_CSV = ROOT / "05_coverage/phase05_evidence_pool_74.csv"
OUT_POOL_MD = ROOT / "05_coverage/phase05_evidence_pool_74.md"
OUT_THINK_CSV = ROOT / "05_coverage/phase05_thinking_signal_archive.csv"
OUT_THINK_MD = ROOT / "05_coverage/phase05_thinking_signal_archive.md"
OUT_REASON_CSV = ROOT / "05_coverage/phase05_reasoning_typology_archive.csv"
OUT_REASON_MD = ROOT / "05_coverage/phase05_reasoning_typology_archive.md"
OUT_CROSS_CSV = ROOT / "05_coverage/phase05_cross_question_split_matrix.csv"
OUT_SAME_TYPE_MD = ROOT / "05_coverage/phase05_reasoning_same_type_index.md"
OUT_L0_MD = ROOT / "05_coverage/phase05_L0_blocker_reason_summary.md"
OUT_BACKCHECK = ROOT / "06_conflicts/phase05_archive_backcheck_report.md"


DETAIL_SOURCES = [
    ROOT / "claudecode_lane/phase04_laneB_targeted_verification_results.csv",
    ROOT / "claudecode_lane/phase04_Aonly_76_review_batch01.csv",
    ROOT / "05_coverage/phase03_codex_local_patch_addendum.csv",
    ROOT / "claudecode_lane/phase03_laneB_patch_addendum.csv",
    ROOT / "claudecode_lane/phase04_batch02_laneB_results_normalized.csv",
    ROOT / "claudecode_lane/opus47_batch03_subjective/phase04_batch03_A_subjective_results.csv",
    ROOT / "claudecode_lane/opus47_batch03_choice/phase04_batch03_B_choice_results_normalized.csv",
]

ID_ALIASES = {
    "FT01_Q18_2": "Q-2026丰台一模-18-2",
    "HS02_Q20": "Q-2025海淀二模-20",
}

THINKING_TERMS = [
    "科学思维",
    "辩证思维",
    "创新思维",
    "系统观念",
    "系统思维",
    "整体性",
    "动态性",
    "分析与综合",
    "质量互变",
    "辩证否定",
    "发散",
    "聚合",
    "联想",
    "逆向",
    "超前",
    "迁移",
    "思维抽象",
    "思维具体",
    "感性具体",
]

REASONING_TERMS = [
    "三段论",
    "假言",
    "充分条件",
    "必要条件",
    "联言",
    "选言",
    "归纳",
    "类比",
    "换质",
    "换位",
    "概念",
    "判断",
    "矛盾律",
    "周延",
    "推理",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(newline="", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows([{k: row.get(k, "") for k in fieldnames} for row in rows])


def clean_text(text: str, limit: int = 220) -> str:
    text = re.sub(r"\s+", " ", (text or "").replace("\U001001b0", " ")).strip()
    return text[:limit]


def sanitize_retired_pairing(text: str, qid: str) -> str:
    """Remove retired wrong-option strings from downstream Phase05 archives."""
    if qid != "Q-2024西城一模-11":
        if qid == "Q-2024朝阳二模-7":
            text = text.replace(
                "A三段论中项不周延",
                "A小项不当周延/小项扩大（娱乐工具在前提中不周延，结论中周延）",
            )
            text = text.replace(
                "A三段论中项不周延;B归纳推理结论确定性夸大;C必要条件假言推理误用",
                "A小项不当周延/小项扩大（娱乐工具在前提中不周延，结论中周延）;B归纳推理结论确定性夸大;C必要条件假言推理误用",
            )
        return text
    text = text.replace("任务描述称answer B=①④，但", "旧错误选项归属已废弃；")
    text = text.replace("Codex A原声明存在选项归属错误。", "旧归属错误不得进入后续融合。")
    text = text.replace("正确答案B=①③", "正确答案B=①③")
    text = text.replace("正确选项归属B=①③", "正确选项归属B=①③")
    return text.replace("B=①④", "旧错误归属")


def first_nonempty(*vals: str) -> str:
    for val in vals:
        if val:
            return val
    return ""


def load_details() -> dict[str, dict[str, str]]:
    details: dict[str, dict[str, str]] = {}
    for path in DETAIL_SOURCES:
        for row in read_csv(path):
            qid = row.get("target_id") or row.get("question_id") or ""
            qid = ID_ALIASES.get(qid, qid)
            if not qid:
                continue
            current = details.setdefault(qid, {})
            normalized = {
                "detail_source": str(path.relative_to(ROOT)),
                "node": first_nonempty(row.get("node", ""), row.get("reasoning_or_thinking_node", ""), row.get("rule_or_thinking_node", ""), row.get("primary_type", "")),
                "logical_or_method_form": first_nonempty(row.get("logical_or_method_form", ""), row.get("logical_form", ""), row.get("logical_form_or_thinking_chain", ""), row.get("rule_or_thinking_node", "")),
                "rule_slogan": first_nonempty(row.get("rule_slogan", ""), row.get("answer_or_scoring", "")),
                "trap_or_boundary": row.get("trap_or_boundary", ""),
                "source_evidence": first_nonempty(row.get("source_evidence", ""), row.get("source_locator", "")),
                "notes": first_nonempty(row.get("notes", ""), row.get("blocker_reason", "")),
                "answer_status": first_nonempty(row.get("answer_status", ""), row.get("answer_or_scoring", "")),
                "rubric_status": row.get("rubric_status", ""),
                "visual_status": first_nonempty(row.get("visual_status", ""), row.get("视觉核读状态", "")),
                "secondary_type": row.get("secondary_type", ""),
            }
            current.update({k: v for k, v in normalized.items() if v})
    return details


def status_short(level: str) -> str:
    if level == "L4_LOCKED_FOR_FUSION":
        return "L4_LOCKED_FOR_FUSION"
    if level == "L3_A_PLUS_B_TARGET_CONFIRMED":
        return "L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE"
    return level


def taxonomy(text: str, terms: list[str]) -> list[str]:
    found = []
    for term in terms:
        if term in text and term not in found:
            found.append(term)
    return found


def reason_type(row: dict[str, str], detail: dict[str, str]) -> str:
    text = ";".join(
        [
            detail.get("logical_or_method_form", ""),
            detail.get("node", ""),
            row.get("reasoning_node", ""),
            row.get("knowledge_node", ""),
        ]
    )
    found = taxonomy(text, REASONING_TERMS)
    if "充分条件" in found or "必要条件" in found:
        if "假言" not in found:
            found.insert(0, "假言")
    if not found and "推理" in row.get("section_scope", ""):
        found = ["推理"]
    return "；".join(found) if found else "PENDING_REASONING_TYPE"


def thinking_type(row: dict[str, str], detail: dict[str, str]) -> str:
    text = ";".join(
        [
            detail.get("logical_or_method_form", ""),
            detail.get("node", ""),
            row.get("knowledge_node", ""),
            row.get("reasoning_node", ""),
        ]
    )
    found = taxonomy(text, THINKING_TERMS)
    if not found and "思维" in row.get("section_scope", ""):
        found = ["思维方法待细化"]
    return "；".join(found) if found else "PENDING_THINKING_METHOD"


def missing_fields(row: dict[str, str]) -> str:
    missing = [k for k, v in row.items() if k in {"材料信号", "可写思维/方法", "logical_form", "rule_slogan", "source_locator", "answer_locator"} and not v]
    return ";".join(missing)


def main() -> None:
    rows = read_csv(CLEAN)
    details = load_details()
    evidence_rows = [r for r in rows if r["phase04_level"] in {"L4_LOCKED_FOR_FUSION", "L3_A_PLUS_B_TARGET_CONFIRMED"}]
    evidence_by_id = {r["canonical_question_id"]: r for r in evidence_rows}

    pool_rows = []
    for row in evidence_rows:
        qid = row["canonical_question_id"]
        detail = details.get(qid, {})
        pool_rows.append(
            {
                "question_id": qid,
                "suite_id": row["suite_id"],
                "source_locator": first_nonempty(detail.get("source_evidence", ""), row["stable_locator"]),
                "question_type": row["question_type"],
                "module": row["section_scope"],
                "status": status_short(row["phase04_level"]),
                "answer_locator": first_nonempty(detail.get("answer_status", ""), row["answer_pairing_status"]),
                "rubric_locator": first_nonempty(detail.get("rubric_status", ""), row["rubric_pairing_status"]),
                "visual_locator": first_nonempty(detail.get("visual_status", ""), row["visual_status"]),
                "full_stem_status": "excerpt_present" if row.get("excerpt") else "missing_excerpt",
                "full_options_status": "choice_options_or_subjective_prompt_present" if row["question_type"] == "选择题" else "subjective_prompt_present",
                "student_permission": row["student稿_permission"],
                "risk_note": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("trap_or_boundary", ""), detail.get("notes", ""), row.get("blocker_reason", "")), qid), 260),
            }
        )

    pool_fields = list(pool_rows[0])
    write_csv(OUT_POOL_CSV, pool_rows, pool_fields)

    same_thinking: dict[str, list[str]] = defaultdict(list)
    same_reasoning: dict[str, list[str]] = defaultdict(list)
    row_profiles: dict[str, dict[str, str]] = {}
    for row in evidence_rows:
        qid = row["canonical_question_id"]
        detail = details.get(qid, {})
        t_type = thinking_type(row, detail)
        r_type = reason_type(row, detail)
        if row["section_scope"] in {"思维", "交叉"}:
            same_thinking[t_type].append(qid)
        if row["section_scope"] in {"推理", "交叉"}:
            same_reasoning[r_type].append(qid)
        row_profiles[qid] = {"thinking_type": t_type, "reasoning_type": r_type}

    thinking_rows = []
    for row in evidence_rows:
        if row["section_scope"] not in {"思维", "交叉"}:
            continue
        qid = row["canonical_question_id"]
        detail = details.get(qid, {})
        t_type = row_profiles[qid]["thinking_type"]
        archive_row = {
            "question_id": qid,
            "材料信号": clean_text(row.get("excerpt", ""), 160),
            "可写思维/方法": t_type,
            "答题动作": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("rule_slogan", ""), f"围绕材料信号调用{t_type}，说明路径、作用或限制。"), qid), 220),
            "答案落点": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("notes", ""), detail.get("logical_or_method_form", ""), row.get("knowledge_node", "")), qid), 220),
            "来源例题": f"{qid} | {row['suite_id']} | {row['stable_locator']}",
            "同类题": ";".join(x for x in same_thinking[t_type] if x != qid),
            "易错陷阱": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("trap_or_boundary", ""), row.get("blocker_reason", "")), qid), 220),
            "status": status_short(row["phase04_level"]),
            "missing_fields": "",
        }
        archive_row["missing_fields"] = missing_fields(archive_row)
        thinking_rows.append(archive_row)

    thinking_fields = list(thinking_rows[0])
    write_csv(OUT_THINK_CSV, thinking_rows, thinking_fields)

    reasoning_rows = []
    for row in evidence_rows:
        if row["section_scope"] not in {"推理", "交叉"}:
            continue
        qid = row["canonical_question_id"]
        detail = details.get(qid, {})
        r_type = row_profiles[qid]["reasoning_type"]
        archive_row = {
            "question_id": qid,
            "primary_reasoning_type": r_type,
            "secondary_reasoning_type": detail.get("secondary_type", ""),
            "logical_form": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("logical_or_method_form", ""), row.get("reasoning_node", ""), row.get("knowledge_node", "")), qid), 260),
            "rule_slogan": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("rule_slogan", ""), "PENDING_RULE_SLOGAN_REVIEW"), qid), 220),
            "valid_or_invalid_pattern": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("notes", ""), detail.get("rule_slogan", ""), row.get("blocker_reason", "")), qid), 220),
            "trap": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("trap_or_boundary", ""), row.get("blocker_reason", "")), qid), 220),
            "answer_action": clean_text(sanitize_retired_pairing(first_nonempty(detail.get("notes", ""), detail.get("answer_status", ""), row.get("answer_pairing_status", "")), qid), 220),
            "same_type_question_ids": ";".join(x for x in same_reasoning[r_type] if x != qid),
            "status": status_short(row["phase04_level"]),
            "missing_fields": "",
        }
        archive_row["missing_fields"] = missing_fields(archive_row)
        reasoning_rows.append(archive_row)

    reasoning_fields = list(reasoning_rows[0])
    write_csv(OUT_REASON_CSV, reasoning_rows, reasoning_fields)

    cross_rows = []
    for row in evidence_rows:
        if row["section_scope"] != "交叉":
            continue
        qid = row["canonical_question_id"]
        t = row_profiles[qid]["thinking_type"]
        r = row_profiles[qid]["reasoning_type"]
        cross_rows.append(
            {
                "question_id": qid,
                "thinking_component": t,
                "reasoning_component": r,
                "primary_archive_destination": "thinking_archive_and_reasoning_archive",
                "secondary_archive_destination": "same_type_index",
                "是否双挂载": "yes",
                "risk_note": clean_text(sanitize_retired_pairing(first_nonempty(details.get(qid, {}).get("trap_or_boundary", ""), row.get("blocker_reason", "")), qid), 220),
            }
        )
    write_csv(OUT_CROSS_CSV, cross_rows, list(cross_rows[0]))

    write_pool_md(pool_rows)
    write_thinking_md(thinking_rows)
    write_reasoning_md(reasoning_rows, same_reasoning)
    write_l0_summary(rows)
    write_backcheck(rows, pool_rows, thinking_rows, reasoning_rows, cross_rows)

    print(f"wrote {OUT_POOL_CSV}")
    print(f"wrote {OUT_THINK_CSV}")
    print(f"wrote {OUT_REASON_CSV}")
    print(f"wrote {OUT_CROSS_CSV}")
    print(f"wrote {OUT_BACKCHECK}")


def write_pool_md(pool_rows: list[dict[str, str]]) -> None:
    counts = Counter(r["module"] for r in pool_rows)
    lines = [
        "# Phase05 Evidence Pool 74",
        "",
        "Status: `EVIDENCE_ARCHIVE_ONLY_NO_STUDENT_DRAFT`.",
        "",
        f"- total evidence rows: {len(pool_rows)}",
        *(f"- {k}: {v}" for k, v in counts.items()),
        "",
        "## Rows",
        "",
        "| question_id | module | type | status | answer_locator | risk_note |",
        "|---|---|---|---|---|---|",
    ]
    for row in pool_rows:
        lines.append(f"| {row['question_id']} | {row['module']} | {row['question_type']} | {row['status']} | {row['answer_locator']} | {row['risk_note']} |")
    OUT_POOL_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_thinking_md(rows: list[dict[str, str]]) -> None:
    by_type: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_type[row["可写思维/方法"]].append(row)
    lines = [
        "# Phase05 Thinking Signal Archive",
        "",
        "Status: `EVIDENCE_ARCHIVE_ONLY_NO_STUDENT_DRAFT`.",
        "",
        f"- rows: {len(rows)}",
        "",
    ]
    for method, items in sorted(by_type.items()):
        lines.extend([f"## {method}", ""])
        for row in items:
            lines.append(f"- `{row['question_id']}` | 信号: {row['材料信号']} | 动作: {row['答题动作']} | status={row['status']}")
        lines.append("")
    OUT_THINK_MD.write_text("\n".join(lines), encoding="utf-8")


def write_reasoning_md(rows: list[dict[str, str]], same_reasoning: dict[str, list[str]]) -> None:
    by_type: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        by_type[row["primary_reasoning_type"]].append(row)
    lines = [
        "# Phase05 Reasoning Typology Archive",
        "",
        "Status: `EVIDENCE_ARCHIVE_ONLY_NO_STUDENT_DRAFT`.",
        "",
        f"- rows: {len(rows)}",
        "",
    ]
    index_lines = [
        "# Phase05 Reasoning Same-Type Index",
        "",
        "Status: `EVIDENCE_ARCHIVE_ONLY_NO_STUDENT_DRAFT`.",
        "",
    ]
    for typ, items in sorted(by_type.items()):
        lines.extend([f"## {typ}", ""])
        index_lines.extend([f"## {typ}", ""])
        index_lines.append("; ".join(same_reasoning[typ]))
        index_lines.append("")
        for row in items:
            lines.append(f"- `{row['question_id']}` | form: {row['logical_form']} | rule: {row['rule_slogan']} | trap: {row['trap']} | status={row['status']}")
        lines.append("")
    OUT_REASON_MD.write_text("\n".join(lines), encoding="utf-8")
    OUT_SAME_TYPE_MD.write_text("\n".join(index_lines), encoding="utf-8")


def write_l0_summary(rows: list[dict[str, str]]) -> None:
    l0 = [r for r in rows if r["phase04_level"] == "L0_BLOCKED"]
    by_reason = Counter(r["blocker_reason"] or r["fusion_status"] for r in l0)
    lines = [
        "# Phase05 L0 Blocker Reason Summary",
        "",
        "Status: `L0_RETAINED_NOT_DISCARDED`.",
        "",
        f"- L0 rows: {len(l0)}",
        "",
        "## Counts",
        "",
    ]
    lines.extend(f"- {reason}: {count}" for reason, count in by_reason.most_common())
    OUT_L0_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_backcheck(all_rows: list[dict[str, str]], pool: list[dict[str, str]], thinking: list[dict[str, str]], reasoning: list[dict[str, str]], cross: list[dict[str, str]]) -> None:
    evidence = [r for r in all_rows if r["phase04_level"] in {"L4_LOCKED_FOR_FUSION", "L3_A_PLUS_B_TARGET_CONFIRMED"}]
    pool_ids = {r["question_id"] for r in pool}
    thinking_ids = {r["question_id"] for r in thinking}
    reasoning_ids = {r["question_id"] for r in reasoning}
    cross_ids = {r["question_id"] for r in cross}
    q11_archive_rows = [
        *(r for r in pool if r["question_id"] == "Q-2024西城一模-11"),
        *(r for r in thinking if r["question_id"] == "Q-2024西城一模-11"),
        *(r for r in reasoning if r["question_id"] == "Q-2024西城一模-11"),
        *(r for r in cross if r["question_id"] == "Q-2024西城一模-11"),
    ]
    q11_ok = bool(q11_archive_rows) and all("B=①④" not in str(r) for r in q11_archive_rows) and any("B=①③" in str(r) for r in q11_archive_rows)
    q12q13_ok = all(
        any(r["question_id"] == q and r["answer_locator"] for r in pool)
        for q in ["Q-2025海淀二模-12", "Q-2025海淀二模-13"]
    )
    q16_ok = "Q-2025西城二模-16-2" in pool_ids and "Q-2026东城期末-16-1" not in {r["canonical_question_id"] for r in all_rows if r["suite_id"] == "S-2026东城期末"}
    checks = [
        ("74 evidence rows all in pool", len(pool) == 74 and pool_ids == {r["canonical_question_id"] for r in evidence}),
        ("23 thinking rows plus 13 cross rows in thinking archive", len(thinking) == 36),
        ("38 reasoning rows plus 13 cross rows in reasoning archive", len(reasoning) == 51),
        ("13 cross rows split", len(cross) == 13),
        ("L4 4 rows retained", sum(1 for r in pool if r["status"] == "L4_LOCKED_FOR_FUSION") == 4),
        ("Q11 pairing lock respected", q11_ok),
        ("Q12/Q13 answer locator retained", q12q13_ok),
        ("Q16 cleanup did not remove L4 Q16(2) and removed split rows", q16_ok),
        ("student permission still no", all(r["student_permission"].startswith("NO_STUDENT_DRAFT") for r in pool)),
    ]
    status = "PASS_INTERNAL_ARCHIVE_BACKCHECK" if all(ok for _, ok in checks) else "FAIL_REPAIR_REQUIRED"
    lines = [
        "# Phase05 Archive Backcheck Report",
        "",
        f"Status: `{status}`.",
        "",
        "This is an internal archive gate only. It does not authorize student稿, Claude/Opus 成文化, Word/PDF, or final PASS.",
        "",
        "## Checks",
        "",
    ]
    for name, ok in checks:
        lines.append(f"- {'PASS' if ok else 'FAIL'}: {name}")
    OUT_BACKCHECK.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
