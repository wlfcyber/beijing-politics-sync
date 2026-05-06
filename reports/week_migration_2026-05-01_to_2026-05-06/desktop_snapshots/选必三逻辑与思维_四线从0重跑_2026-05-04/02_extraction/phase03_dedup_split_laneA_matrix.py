#!/usr/bin/env python3
"""Split Lane A Phase03 coverage into canonical paper rows and support evidence rows.

This is an audit/pre-fusion cleanup. It does not promote any row to student-facing
content; it only prevents rubric/reference text from masquerading as question text.
"""

from __future__ import annotations

import csv
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")
IN_CSV = ROOT / "05_coverage/phase03_question_coverage_matrix.csv"
OUT_CANONICAL = ROOT / "05_coverage/phase03_laneA_dedup_question_matrix.csv"
OUT_SUPPORT = ROOT / "05_coverage/phase03_laneA_support_evidence_matrix.csv"
OUT_REMOVED = ROOT / "05_coverage/phase03_laneA_duplicate_or_reference_rows.csv"
OUT_REPORT = ROOT / "05_coverage/phase03_laneA_dedup_report.md"

SUPPORT_MARKERS = ("细则", "评标", "讲评", "答案", "教师")
PAPER_MARKERS = ("试卷", "原卷", "扫描版")


def read_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def write_rows(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def source_kind(row: dict[str, str]) -> str:
    source_id = row.get("source_id", "")
    if any(marker in source_id for marker in SUPPORT_MARKERS):
        return "support_or_reference"
    if any(marker in source_id for marker in PAPER_MARKERS):
        return "paper"
    return "unknown"


def key_of(row: dict[str, str]) -> tuple[str, str]:
    return (row.get("suite_id", "").strip(), row.get("原始题号", "").strip())


def score_paper_row(row: dict[str, str]) -> int:
    source_id = row.get("source_id", "")
    stable = row.get("stable_locator", "")
    score = 0
    if "试卷" in source_id:
        score += 100
    if "原卷" in source_id or "扫描版" in source_id:
        score += 80
    if "render_page" in stable or "visual_recovered" in row.get("是否完整题干", ""):
        score += 60
    if row.get("blocked_status", "").startswith("locked_pending"):
        score += 20
    if row.get("blocked_status", "").startswith("suite_visual_blocker"):
        score -= 50
    if row.get("部分归属", "") not in ("待判", "missing", ""):
        score += 10
    if any(marker in source_id for marker in SUPPORT_MARKERS):
        score -= 100
    return score


def main() -> None:
    fields, rows = read_rows(IN_CSV)

    paper_rows: list[dict[str, str]] = []
    support_rows: list[dict[str, str]] = []
    unknown_rows: list[dict[str, str]] = []
    for row in rows:
        kind = source_kind(row)
        if kind == "paper":
            paper_rows.append(row)
        elif kind == "support_or_reference":
            support_rows.append(row)
        else:
            unknown_rows.append(row)

    support_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in support_rows:
        support_by_key[key_of(row)].append(row)

    paper_by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for row in paper_rows + unknown_rows:
        paper_by_key[key_of(row)].append(row)

    canonical: list[dict[str, str]] = []
    removed: list[dict[str, str]] = []

    extra_fields = [
        "laneA_dedup_status",
        "paired_support_source_ids_laneA_split",
        "duplicate_source_ids_laneA_split",
        "dedup_note",
    ]
    out_fields = fields + [field for field in extra_fields if field not in fields]

    for key in sorted(paper_by_key):
        candidates = paper_by_key[key]
        candidates_sorted = sorted(candidates, key=score_paper_row, reverse=True)
        winner = dict(candidates_sorted[0])
        duplicates = candidates_sorted[1:]
        supports = support_by_key.get(key, [])
        winner["laneA_dedup_status"] = "canonical_paper_question_row"
        winner["paired_support_source_ids_laneA_split"] = ";".join(
            sorted({r.get("source_id", "") for r in supports if r.get("source_id", "")})
        )
        winner["duplicate_source_ids_laneA_split"] = ";".join(
            sorted({r.get("source_id", "") for r in duplicates if r.get("source_id", "")})
        )
        notes = []
        if supports:
            notes.append(f"support_rows_split={len(supports)}")
        if duplicates:
            notes.append(f"duplicate_paper_rows_removed={len(duplicates)}")
        if key[1] == "UNPARSED":
            notes.append("suite_level_visual_blocker_kept_as_blocker")
        winner["dedup_note"] = "; ".join(notes)
        canonical.append(winner)

        for dup in duplicates:
            item = dict(dup)
            item["laneA_dedup_status"] = "removed_duplicate_paper_or_unknown_row"
            item["paired_support_source_ids_laneA_split"] = ""
            item["duplicate_source_ids_laneA_split"] = winner.get("source_id", "")
            item["dedup_note"] = "same suite/question retained stronger canonical paper row"
            removed.append(item)

    support_out_fields = fields + [
        "laneA_split_status",
        "matched_canonical_question_id",
        "support_note",
    ]
    canonical_key_to_qid = {key_of(row): row.get("question_id", "") for row in canonical}
    support_out: list[dict[str, str]] = []
    for row in support_rows:
        item = dict(row)
        item["laneA_split_status"] = "support_or_reference_row_split_from_question_matrix"
        item["matched_canonical_question_id"] = canonical_key_to_qid.get(key_of(row), "")
        item["support_note"] = "use only as answer/rubric/reference evidence after source hierarchy check; not original question text"
        support_out.append(item)

    for row in support_rows:
        item = dict(row)
        item["laneA_dedup_status"] = "moved_to_support_evidence_matrix"
        item["paired_support_source_ids_laneA_split"] = ""
        item["duplicate_source_ids_laneA_split"] = ""
        item["dedup_note"] = "support/reference source split out; not a canonical paper question row"
        removed.append(item)

    write_rows(OUT_CANONICAL, out_fields, canonical)
    write_rows(OUT_SUPPORT, support_out_fields, support_out)
    write_rows(OUT_REMOVED, out_fields, removed)

    original_keys = Counter(key_of(row) for row in rows)
    duplicate_keys = {key: count for key, count in original_keys.items() if count > 1}
    in_scope = [
        row
        for row in canonical
        if any(tag in row.get("部分归属", "") for tag in ("思维", "推理", "交叉"))
    ]
    locked = [row for row in canonical if row.get("blocked_status", "").startswith("locked")]
    blockers = [row for row in canonical if row.get("blocked_status", "")]

    report = [
        "# Phase 03 Lane A Dedup/Split Report",
        "",
        "Status: `CLEANUP_DONE_NOT_STUDENT_FACING`.",
        "",
        "## Counts",
        "",
        f"- Input rows: {len(rows)}",
        f"- Canonical paper/question rows: {len(canonical)}",
        f"- Support/reference rows split out: {len(support_rows)}",
        f"- Duplicate/removed rows logged: {len(removed)}",
        f"- Unknown rows treated as paper candidates: {len(unknown_rows)}",
        f"- Duplicate suite/question keys in input: {len(duplicate_keys)}",
        f"- Canonical in-scope or cross candidates: {len(in_scope)}",
        f"- Canonical locked rows: {len(locked)}",
        f"- Canonical rows with any blocker/status: {len(blockers)}",
        "",
        "## Output Files",
        "",
        f"- Canonical matrix: `{OUT_CANONICAL.relative_to(ROOT)}`",
        f"- Support evidence matrix: `{OUT_SUPPORT.relative_to(ROOT)}`",
        f"- Removed/reference log: `{OUT_REMOVED.relative_to(ROOT)}`",
        "",
        "## Gate Meaning",
        "",
        "- This pass separates original paper/question rows from answer/rubric/reference rows.",
        "- It does not resolve missing answers, choice options, or module boundary disputes.",
        "- It does not unlock HS02 or 2026丰台一模 Q18(2); those still need the focused Lane B patch.",
        "- Student稿、Claude Opus 成文化、Word/PDF、最终 PASS remain blocked.",
    ]
    OUT_REPORT.write_text("\n".join(report) + "\n", encoding="utf-8")
    print("\n".join(report[:18]))


if __name__ == "__main__":
    main()
