#!/usr/bin/env python3
"""Parse model codebook-expansion decisions from Markdown into CSV.

The external models were asked to emit one section per EXP_DEC_* item with
field bullets such as "- decision: ...". This script keeps that conversion
mechanical so Codex can compare GPT and Claude outputs without retyping.
"""

from __future__ import annotations

import argparse
import csv
import re
from pathlib import Path


FIELDS = [
    "expansion_decision_id",
    "source_suggestion_id",
    "candidate_label",
    "decision",
    "new_or_revised_code_label",
    "affected_existing_code_ids",
    "supporting_question_ids",
    "supporting_rubric_atom_ids_or_patch_atom_ids",
    "supporting_material_atom_ids",
    "evidence_level_summary",
    "what_student_must_judge",
    "material_trigger_pattern",
    "legal_knowledge_or_rule_pattern",
    "rubric_reward_pattern",
    "full_score_sentence_pattern",
    "risk_of_empty_value_talk",
    "risk_of_legal_exam_overanalysis",
    "module_boundary_risk",
    "counterexamples_or_limits",
    "confidence",
    "reason",
]


SECTION_RE = re.compile(r"^###\s+(EXP_DEC_\d+)\b.*$")
FIELD_RE = re.compile(r"^-\s+([a-zA-Z0-9_]+):\s*(.*)$")


def clean_value(value: str) -> str:
    value = value.strip()
    value = value.replace("**", "")
    value = re.sub(r"\s+", " ", value)
    return value


def parse_markdown(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    current: dict[str, str] | None = None
    current_field: str | None = None

    for line in text.splitlines():
        section = SECTION_RE.match(line)
        if section:
            if current:
                rows.append(current)
            current = {field: "" for field in FIELDS}
            current["expansion_decision_id"] = section.group(1)
            current_field = None
            continue

        if current is None:
            continue

        field_match = FIELD_RE.match(line)
        if field_match:
            field, value = field_match.groups()
            if field in current:
                current[field] = clean_value(value)
                current_field = field
            else:
                current_field = None
            continue

        if current_field and line.startswith("  "):
            extra = clean_value(line)
            if extra:
                current[current_field] = clean_value(
                    f"{current[current_field]} {extra}".strip()
                )

    if current:
        rows.append(current)
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_md", type=Path)
    parser.add_argument("output_csv", type=Path)
    args = parser.parse_args()

    rows = parse_markdown(args.input_md.read_text(encoding="utf-8"))
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    with args.output_csv.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"wrote {len(rows)} rows to {args.output_csv}")


if __name__ == "__main__":
    main()
