#!/usr/bin/env python3
from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from extract_and_classify import classify_text, compact_snippet


RUN_DIR = Path(__file__).resolve().parents[1]
IN_QUEUE = RUN_DIR / "05_reports" / "manual_subquestion_split_queue.csv"
OUT_DIR = RUN_DIR / "05_reports"
OUT_MATRIX = RUN_DIR / "04_module_classification" / "subquestion_split_matrix.csv"
OUT_UNRESOLVED = OUT_DIR / "manual_subquestion_split_unresolved.csv"
OUT_SUMMARY = OUT_DIR / "manual_subquestion_split_resolution_summary.md"

SAFE_SOURCE_TYPES = {"paper", "ocr-cache"}
TARGET_MODULES = {"B2_ECONOMICS", "B3_POLITICS_RULE_OF_LAW", "B4_CULTURE"}


PART_RE = re.compile(r"(?<![\dA-Za-z])([（(])([1-9][0-9]?)([)）])")
SCORE_RE = re.compile(r"[（(]\s*\d+\s*分\s*[)）]")
NEXT_MATERIAL_RE = re.compile(r"(材料[一二三四五六七八九十]|\n?=====)")


def normalize_part_no(value: str) -> str:
    mapping = {
        "一": "1",
        "二": "2",
        "三": "3",
        "四": "4",
        "五": "5",
        "六": "6",
        "七": "7",
        "八": "8",
        "九": "9",
        "十": "10",
    }
    return mapping.get(value, value)


def split_subquestions(text: str) -> list[dict[str, str]]:
    matches = list(PART_RE.finditer(text))
    raw_parts: list[dict[str, str]] = []
    for idx, match in enumerate(matches):
        marker = "".join(match.groups())
        part_no = normalize_part_no(match.group(2))
        start = match.start()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(text)
        segment = text[start:end].strip()
        if len(segment) < 12:
            continue
        raw_parts.append(
            {
                "part_no": part_no,
                "part_marker": marker,
                "part_text": segment,
            }
        )
    parts: list[dict[str, str]] = []
    seen: dict[str, dict[str, str]] = {}
    for part in raw_parts:
        if part["part_no"] in seen:
            seen[part["part_no"]]["part_text"] = f"{seen[part['part_no']]['part_text']} {part['part_text']}"
            continue
        seen[part["part_no"]] = dict(part)
        parts.append(seen[part["part_no"]])
    return parts


def trim_to_parent_question(text: str, question: str) -> str:
    if not question.isdigit():
        return text
    current = int(question)
    cut_points = []
    for next_q in range(current + 1, 22):
        pattern = re.compile(rf"(?<!\d){next_q}\s*[（(]\s*\d+\s*分\s*[)）]?")
        match = pattern.search(text)
        if match and match.start() > 80:
            cut_points.append(match.start())
    if cut_points:
        return text[: min(cut_points)].strip()
    return text


def extract_prompt_text(part_text: str) -> str:
    """Use the question prompt for module routing; later material often belongs to the next part."""
    cut_points = []
    score_match = SCORE_RE.search(part_text)
    if score_match:
        cut_points.append(score_match.end())
    material_match = NEXT_MATERIAL_RE.search(part_text)
    if material_match and material_match.start() > 8:
        cut_points.append(material_match.start())
    if cut_points:
        return part_text[: min(cut_points)].strip()
    return part_text[:350].strip()


def prompt_override(prompt_text: str, base: dict[str, str]) -> dict[str, str]:
    mixed_explicit = (
        ("《政治与法治》" in prompt_text and "《当代国际政治与经济》" in prompt_text)
        or ("《经济与社会》" in prompt_text and "《逻辑与思维》" in prompt_text)
        or ("《经济与社会》" in prompt_text and "《当代国际政治与经济》" in prompt_text)
        or ("《经济与社会》" in prompt_text and "《法律与生活》" in prompt_text)
    )
    if mixed_explicit:
        return base

    module = ""
    status = ""
    next_action = ""
    terms: list[str] = []
    if "政协" in prompt_text or "人民政协" in prompt_text:
        module = "B3_POLITICS_RULE_OF_LAW"
        status = "included"
        next_action = "future_baodian_intake"
        terms.append("政协")
    elif "经济信息" in prompt_text or "从经济角度" in prompt_text:
        module = "B2_ECONOMICS"
        status = "included"
        next_action = "future_baodian_intake"
        terms.append("经济信息/经济角度")
    elif "哲学" in prompt_text:
        module = "B4_PHILOSOPHY_EXCLUDED"
        status = "module-boundary-excluded"
        next_action = "exclude_from_three_target_lines"
        terms.append("哲学")

    if not module:
        return base

    return {
        "book_module": module,
        "status": status,
        "next_action": next_action,
        "decision_reason": json.dumps(
            {
                "override": "prompt_router",
                "prompt_terms": terms,
                "classification_text": compact_snippet(prompt_text, 300),
                "base_decision": base.get("decision_reason", ""),
            },
            ensure_ascii=False,
        ),
    }


def resolution_status(classified: dict[str, str], source_type: str) -> str:
    if source_type not in SAFE_SOURCE_TYPES:
        return "unresolved_source_not_paper"
    if classified["status"] == "included" and classified["book_module"] in TARGET_MODULES:
        return "resolved_target_subquestion"
    if classified["status"] == "module-boundary-excluded":
        return "resolved_boundary_subquestion"
    return "unresolved_needs_manual_review"


def main() -> int:
    rows = list(csv.DictReader(IN_QUEUE.open("r", encoding="utf-8", newline="")))
    out_fields = [
        "suite_id",
        "year",
        "district",
        "stage",
        "parent_question",
        "subquestion",
        "part_no",
        "source_type",
        "source_path",
        "book_module",
        "status",
        "resolution_status",
        "next_action",
        "part_text",
        "classification_text",
        "decision_reason",
    ]
    unresolved_fields = [
        "suite_id",
        "question",
        "source_type",
        "reason",
        "snippet",
    ]
    split_rows: list[dict[str, str]] = []
    unresolved_rows: list[dict[str, str]] = []
    parent_resolution: dict[tuple[str, str], list[str]] = defaultdict(list)

    for row in rows:
        source_type = row.get("candidate_source_type", "")
        snippet = trim_to_parent_question(row.get("snippet", ""), row["question"])
        parts = split_subquestions(snippet)
        parent_key = (row["suite_id"], row["question"])
        if source_type not in SAFE_SOURCE_TYPES:
            unresolved_rows.append(
                {
                    "suite_id": row["suite_id"],
                    "question": row["question"],
                    "source_type": source_type,
                    "reason": "source_not_paper_or_ocr_cache",
                    "snippet": compact_snippet(snippet, 500),
                }
            )
            parent_resolution[parent_key].append("unresolved_source_not_paper")
            continue
        if len(parts) < 2:
            unresolved_rows.append(
                {
                    "suite_id": row["suite_id"],
                    "question": row["question"],
                    "source_type": source_type,
                    "reason": "could_not_find_two_or_more_subquestion_markers",
                    "snippet": compact_snippet(snippet, 500),
                }
            )
            parent_resolution[parent_key].append("unresolved_no_split")
            continue

        for part in parts:
            classification_text = extract_prompt_text(part["part_text"])
            classified = classify_text(classification_text, row.get("candidate_file_path", ""), source_type)
            classified = prompt_override(classification_text, classified)
            res_status = resolution_status(classified, source_type)
            parent_resolution[parent_key].append(res_status)
            split_rows.append(
                {
                    "suite_id": row["suite_id"],
                    "year": row["year"],
                    "district": row["district"],
                    "stage": row["stage"],
                    "parent_question": row["question"],
                    "subquestion": f"{row['question']}({part['part_no']})",
                    "part_no": part["part_no"],
                    "source_type": source_type,
                    "source_path": row.get("candidate_file_path", ""),
                    "book_module": classified["book_module"],
                    "status": classified["status"],
                    "resolution_status": res_status,
                    "next_action": classified["next_action"],
                    "part_text": compact_snippet(part["part_text"], 1000),
                    "classification_text": compact_snippet(classification_text, 500),
                    "decision_reason": classified["decision_reason"],
                }
            )

    OUT_MATRIX.parent.mkdir(parents=True, exist_ok=True)
    with OUT_MATRIX.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=out_fields)
        writer.writeheader()
        writer.writerows(split_rows)

    with OUT_UNRESOLVED.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=unresolved_fields)
        writer.writeheader()
        writer.writerows(unresolved_rows)

    res_counts = Counter(row["resolution_status"] for row in split_rows)
    module_counts = Counter(row["book_module"] for row in split_rows)
    parent_counts = Counter()
    for statuses in parent_resolution.values():
        if statuses and all(status.startswith("resolved_") for status in statuses):
            parent_counts["fully_resolved_by_subquestion_draft"] += 1
        elif any(status.startswith("resolved_") for status in statuses):
            parent_counts["partially_resolved_by_subquestion_draft"] += 1
        else:
            parent_counts["unresolved_by_subquestion_draft"] += 1

    lines = [
        "# Manual Subquestion Split Resolution Summary",
        "",
        "- purpose: Conservative draft split for rows marked `manual_subquestion_split_needed`; this does not by itself close final coverage.",
        f"- input_rows: {len(rows)}",
        f"- output_subquestion_rows: {len(split_rows)}",
        f"- unresolved_parent_rows: {len(unresolved_rows)}",
        f"- output_matrix: `{OUT_MATRIX}`",
        f"- unresolved_file: `{OUT_UNRESOLVED}`",
        "",
        "## Parent Resolution Counts",
        "",
    ]
    for key, value in parent_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Subquestion Resolution Counts", ""])
    for key, value in res_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(["", "## Subquestion Module Counts", ""])
    for key, value in module_counts.most_common():
        lines.append(f"- {key}: {value}")
    lines.extend(
        [
            "",
            "## Governor Note",
            "",
            "- Rows with `resolved_target_subquestion` can be considered draft-ready for future B2/B3/B4_CULTURE intake only after parent matrix integration.",
            "- Rows with `resolved_boundary_subquestion` should remain visible as excluded subparts, so future handbooks do not silently lose them.",
            "- Classification uses the subquestion prompt up to the first score marker when available; the longer `part_text` is retained only as evidence context.",
            "- Any unresolved row must be checked against the original paper or a longer OCR extract before changing the parent matrix.",
        ]
    )
    OUT_SUMMARY.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print(OUT_MATRIX)
    print(OUT_UNRESOLVED)
    print(OUT_SUMMARY)
    print(f"input_rows={len(rows)} split_rows={len(split_rows)} unresolved_parent_rows={len(unresolved_rows)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
