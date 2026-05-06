#!/usr/bin/env python3
"""Build Phase12 74-row review-only expanded body from repaired entries.

This is a mechanical assembler. It does not create new content or approve final
delivery; it only gathers already reviewed Phase11D body rows plus Phase12
Batch01/02/03 repaired rows and writes audit matrices.
"""

from __future__ import annotations

import csv
import re
from dataclasses import dataclass
from pathlib import Path


BASE = Path("/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04")

SORT_MATRIX = BASE / "09_student_draft/phase12_sort_key_matrix.csv"
DECISION_MATRIX = BASE / "05_coverage/phase12_74row_expansion_decision_matrix.csv"

COMBINED_29 = BASE / "09_student_draft/phase11D_combined_source_verified_29_REVIEW_ONLY.md"
FALLBACK_30 = BASE / "09_student_draft/phase11B_batch01_student_body_30_REVIEW_ONLY.md"
BATCH_FILES = [
    BASE / "09_student_draft/phase12_batch01_repaired_entries_REVIEW_ONLY.md",
    BASE / "09_student_draft/phase12_batch02_repaired_entries_REVIEW_ONLY.md",
    BASE / "09_student_draft/phase12_batch03_repaired_entries_REVIEW_ONLY.md",
]

OUT_MD = BASE / "09_student_draft/phase12_expanded_body_FROM_74_REVIEW_ONLY.md"
OUT_CONTROL = BASE / "09_student_draft/phase12_expanded_body_control_matrix.csv"
OUT_GAP = BASE / "09_student_draft/phase12_expanded_body_gap_backcheck.csv"


@dataclass
class Section:
    title: str
    normalized_title: str
    body: str
    source_file: str
    priority: int


def normalize_title(title: str) -> str:
    title = title.strip()
    title = title.replace("（主观题）", "").replace("（选择题）", "")
    title = re.sub(r"\([^)]*题\)$", "", title).strip()
    return title


def clean_section_text(section_text: str) -> str:
    lines = section_text.splitlines()
    if lines and re.match(r"^#{2,3}\s+", lines[0]):
        lines = lines[1:]
    text = "\n".join(lines).strip()
    text = re.sub(r"\n-{3,}\s*$", "", text).strip()
    return text


def parse_sections(path: Path, priority: int) -> dict[str, Section]:
    text = path.read_text()
    matches = list(re.finditer(r"^(#{2,3})\s+(.+?)\s*$", text, re.M))
    sections: dict[str, Section] = {}
    for i, match in enumerate(matches):
        title = match.group(2).strip()
        if title in {"主观题", "选择题"}:
            continue
        if title.startswith("Phase"):
            continue
        start = match.start()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        normalized = normalize_title(title)
        body = clean_section_text(text[start:end])
        if not body:
            continue
        sections[normalized] = Section(title, normalized, body, path.name, priority)
    return sections


def load_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as f:
        return list(csv.DictReader(f))


def main() -> None:
    sort_rows = load_csv(SORT_MATRIX)
    decision_rows = {row["question_id"]: row for row in load_csv(DECISION_MATRIX)}

    batch_sections: dict[str, Section] = {}
    for path in BATCH_FILES:
        batch_sections.update(parse_sections(path, priority=100))
    combined_sections = parse_sections(COMBINED_29, priority=80)
    fallback_sections = parse_sections(FALLBACK_30, priority=50)

    body_parts: list[str] = [
        "# Phase12 Expanded Body From 74 Evidence Rows",
        "",
        "Status: `REVIEW_ONLY_NO_WORD_NO_FINAL`",
        "",
        "本稿把原 29 条 controlled body 与 Phase12 修复后的 45 条 non-body 候选合并为 74 条 review-only 扩展正文。它只用于继续审查、362 回扫、双索引和外部模型复核，不得命名为终稿、最终稿或宝典成品。",
        "",
        "- 条目总数：74",
        "- 主观题在前，选择题在后",
        "- 每类内部按海淀、西城、东城、朝阳、丰台、其他区；同一区内部按 2026、2025、2024 排序",
        "",
    ]

    control_rows: list[dict[str, str]] = []
    gap_rows: list[dict[str, str]] = []
    used_titles: dict[str, int] = {}
    current_group = None

    for order, row in enumerate(sorted(sort_rows, key=lambda r: r["sort_key"]), start=1):
        qid = row["question_id"]
        title = row["visible_title"]
        normalized = normalize_title(title)
        decision = row["phase12_decision"]
        matrix_row = decision_rows.get(qid, {})

        chosen = None
        chosen_pool = ""
        if normalized in batch_sections:
            chosen = batch_sections[normalized]
            chosen_pool = "phase12_batch_repair"
        elif normalized in combined_sections:
            chosen = combined_sections[normalized]
            chosen_pool = "phase11D_combined29"
        elif normalized in fallback_sections:
            chosen = fallback_sections[normalized]
            chosen_pool = "phase11B_fallback_for_missing_body_now"

        found = "yes" if chosen else "no"
        note = ""
        if chosen is None:
            section_body = "【待修复】本条在 Phase12 74-row matrix 中存在，但本轮扩展正文装配未找到可用正文块。不得合并进 Word。"
            note = "missing_section_block"
        else:
            section_body = chosen.body
            if chosen_pool == "phase11B_fallback_for_missing_body_now":
                note = "fallback_body_now_block_used; must be rechecked before final"
            elif chosen_pool == "phase12_batch_repair":
                note = "repaired_review_only_block_used"
            else:
                note = "existing_phase11D_block_used"

        group = row["question_type_group"]
        if group != current_group:
            body_parts.append(f"## {group}")
            body_parts.append("")
            current_group = group

        used_titles[normalized] = used_titles.get(normalized, 0) + 1
        body_parts.append(f"### {title}")
        body_parts.append("")
        body_parts.append(f"<!-- question_id: {qid}; phase12_decision: {decision}; source_pool: {chosen_pool or 'missing'} -->")
        body_parts.append("")
        body_parts.append(section_body)
        body_parts.append("")

        control_rows.append(
            {
                "order": str(order),
                "question_id": qid,
                "visible_title": title,
                "question_type_group": group,
                "module": matrix_row.get("module", ""),
                "district": row["district"],
                "year": row["year"],
                "exam_stage": row["exam_stage"],
                "sort_key": row["sort_key"],
                "phase12_decision": decision,
                "current_body_status": matrix_row.get("current_body_status", ""),
                "body_found": found,
                "source_pool": chosen_pool,
                "source_file": chosen.source_file if chosen else "",
                "note": note,
            }
        )
        gap_rows.append(
            {
                "question_id": qid,
                "visible_title": title,
                "expected_decision": decision,
                "body_found": found,
                "coverage_bucket": "body" if found == "yes" else "missing",
                "repair_or_blocker": note,
            }
        )

    OUT_MD.write_text("\n".join(body_parts).rstrip() + "\n")

    with OUT_CONTROL.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(control_rows[0].keys()))
        writer.writeheader()
        writer.writerows(control_rows)

    with OUT_GAP.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(gap_rows[0].keys()))
        writer.writeheader()
        writer.writerows(gap_rows)

    missing = [row for row in gap_rows if row["body_found"] != "yes"]
    print(f"written: {OUT_MD}")
    print(f"rows: {len(control_rows)}")
    print(f"missing: {len(missing)}")
    print(f"body_now: {sum(1 for row in control_rows if row['phase12_decision'] == 'body_now')}")
    print(f"body_after_repair: {sum(1 for row in control_rows if row['phase12_decision'] == 'body_after_repair')}")


if __name__ == "__main__":
    main()
