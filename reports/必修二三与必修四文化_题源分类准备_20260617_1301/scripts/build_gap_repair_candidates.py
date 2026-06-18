#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
TRIAGE = RUN_DIR / "05_reports" / "question_gap_triage.csv"
CANDIDATES = RUN_DIR / "03_question_index" / "question_candidates.csv"
OUT_CSV = RUN_DIR / "05_reports" / "question_gap_repair_candidates.csv"
OUT_MD = RUN_DIR / "05_reports" / "question_gap_repair_candidates.md"

PRIMARY_SOURCE_TYPES = {"paper", "ocr-cache", "reference-answer"}
AUX_SOURCE_TYPES = {"rubric", "marking-report", "lecture"}
RAW_MARKER_SOURCE_TYPES = {"paper", "ocr-cache"}


def compact(text: str, limit: int = 360) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    return text[:limit]


def qsort(values: list[str]) -> list[str]:
    return sorted(values, key=lambda value: int(value) if value.isdigit() else 9999)


def load_candidates() -> tuple[dict[tuple[str, str], list[dict[str, str]]], dict[str, set[str]]]:
    by_key: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    text_paths: dict[str, set[str]] = defaultdict(set)
    with CANDIDATES.open("r", encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            suite = row["suite_id"]
            question = row["question"]
            if question.isdigit():
                by_key[(suite, question)].append(row)
            if row.get("source_type") in RAW_MARKER_SOURCE_TYPES and row.get("run_text_path"):
                text_paths[suite].add(row["run_text_path"])
    return by_key, text_paths


def marker_regex(question: str) -> re.Pattern[str]:
    q = re.escape(question)
    # Covers "4.", "4．", "4、", "4 " at the start of a line, and OCR cases
    # where the question number is alone on a line before the stem.
    return re.compile(rf"(?m)^\s*{q}\s*(?:[.．、]|$|\s)")


def next_marker_regex(question: str) -> re.Pattern[str] | None:
    try:
        nxt = str(int(question) + 1)
    except ValueError:
        return None
    n = re.escape(nxt)
    return re.compile(rf"(?m)^\s*{n}\s*(?:[.．、]|$|\s)")


def raw_marker_snippet(text_path: str, question: str) -> tuple[str, str]:
    path = Path(text_path)
    if not path.exists() or not path.is_file():
        return "", ""
    try:
        text = path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return "", ""
    match = marker_regex(question).search(text)
    if not match:
        return "", ""
    end = min(len(text), match.start() + 1200)
    nxt = next_marker_regex(question)
    if nxt:
        next_match = nxt.search(text, match.end())
        if next_match:
            end = min(end, next_match.start())
    return str(path), compact(text[match.start() : end])


def choose_action(
    triage_status: str,
    primary_rows: list[dict[str, str]],
    aux_rows: list[dict[str, str]],
    raw_path: str,
    raw_confidence: str,
) -> str:
    if raw_path and raw_confidence == "high":
        return "repair_primary_question_split_high_confidence"
    if raw_path:
        return "raw_marker_candidate_visual_check"
    if primary_rows:
        return "matrix_or_filter_repair"
    if aux_rows:
        return "raw_paper_repair_with_auxiliary_clue"
    if triage_status == "likely_actual_20_question_paper":
        return "accept_20_question_structure_after_source_spotcheck"
    return "raw_source_manual_inspection_needed"


def raw_marker_confidence(question: str, snippet: str) -> str:
    if not snippet:
        return ""
    body = re.sub(rf"^\s*{re.escape(question)}\s*", "", snippet).strip()
    # Low-confidence patterns are usually option-unit hits rather than top-level
    # question starts, e.g. "1 xxx 2 yyy 3 zzz 4 zzz A.12 ...".
    option_only = bool(re.search(r"\b2[\s\S]{0,90}\b3[\s\S]{0,90}\b4\b", body))
    choice_frame_match = re.search(r"下列|对此|这说明|分析正确|说法正确|合理的是|最适合的是|表述正确", body)
    option_match = re.search(r"\bA[.．、]?\s*|\bB[.．、]?\s*", body)
    has_abcd = bool(option_match) and bool(re.search(r"\bC[.．、]?\s*|\bD[.．、]?\s*", body))
    has_choice_frame_before_options = bool(choice_frame_match) and (
        not option_match or choice_frame_match.start() < option_match.start()
    )
    has_subjective_frame = bool(re.search(r"结合材料|运用|说明|分析|阐述|谈谈|分\)", body))
    try:
        qnum = int(question)
    except ValueError:
        qnum = 0
    if has_subjective_frame and qnum >= 16:
        return "high"
    if has_choice_frame_before_options and has_abcd and not option_only:
        return "high"
    if has_choice_frame_before_options and qnum >= 11:
        return "medium"
    return "low"


def main() -> int:
    candidate_rows, suite_text_paths = load_candidates()
    output_rows: list[dict[str, str]] = []

    with TRIAGE.open("r", encoding="utf-8", newline="") as f:
        for triage in csv.DictReader(f):
            suite = triage["suite_id"]
            missing = triage["missing_if_expected_1_to_21"].split()
            for question in qsort(missing):
                rows = candidate_rows.get((suite, question), [])
                primary_rows = [r for r in rows if r["source_type"] in PRIMARY_SOURCE_TYPES]
                aux_rows = [r for r in rows if r["source_type"] in AUX_SOURCE_TYPES]
                raw_path = ""
                raw_snippet = ""
                for text_path in sorted(suite_text_paths.get(suite, set())):
                    raw_path, raw_snippet = raw_marker_snippet(text_path, question)
                    if raw_path:
                        break

                best_rows = primary_rows or aux_rows
                best = best_rows[0] if best_rows else {}
                confidence = raw_marker_confidence(question, raw_snippet)
                action = choose_action(triage["triage_status"], primary_rows, aux_rows, raw_path, confidence)
                output_rows.append(
                    {
                        "suite_id": suite,
                        "missing_question": question,
                        "triage_status": triage["triage_status"],
                        "recommended_action": action,
                        "raw_marker_confidence": confidence,
                        "candidate_source_types": " ".join(sorted({r["source_type"] for r in rows})),
                        "candidate_count": str(len(rows)),
                        "best_candidate_file": best.get("file_path", ""),
                        "best_candidate_snippet": compact(best.get("snippet", "")),
                        "raw_marker_text_path": raw_path,
                        "raw_marker_snippet": raw_snippet,
                    }
                )

    fields = [
        "suite_id",
        "missing_question",
        "triage_status",
        "recommended_action",
        "raw_marker_confidence",
        "candidate_source_types",
        "candidate_count",
        "best_candidate_file",
        "best_candidate_snippet",
        "raw_marker_text_path",
        "raw_marker_snippet",
    ]
    with OUT_CSV.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(output_rows)

    counts = defaultdict(int)
    for row in output_rows:
        counts[row["recommended_action"]] += 1

    lines = [
        "# Question Gap Repair Candidates",
        "",
        f"- input_triage_rows: {sum(1 for _ in TRIAGE.open('r', encoding='utf-8')) - 1}",
        f"- output_rows: {len(output_rows)}",
        f"- csv: `{OUT_CSV}`",
        "",
        "## Recommended Actions",
        "",
    ]
    for key in sorted(counts):
        lines.append(f"- {key}: {counts[key]}")
    lines.extend(["", "## Non-20-Structure Repair Rows", ""])
    for row in output_rows:
        if row["triage_status"] == "likely_actual_20_question_paper":
            continue
        clue = row["raw_marker_snippet"] or row["best_candidate_snippet"] or "NO_SNIPPET"
        lines.append(
            f"- {row['suite_id']} Q{row['missing_question']}: "
            f"{row['recommended_action']}; sources={row['candidate_source_types'] or 'none'}; "
            f"clue={compact(clue, 180)}"
        )
    lines.extend(
        [
            "",
            "## Governor Note",
            "",
            "- This file is a repair packet, not a coverage closure.",
            "- Rows with `repair_primary_question_split_high_confidence` show a likely missing top-level question marker in primary OCR/text and should be used to patch the question splitter or add explicit blocked rows after inspection.",
            "- Rows with `raw_marker_candidate_visual_check` contain a possible raw marker but may be an option-number false hit; inspect visually before repair.",
            "- Rows with `raw_paper_repair_with_auxiliary_clue` have auxiliary evidence only and must return to the original paper/OCR before any matrix inclusion.",
        ]
    )
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(OUT_CSV)
    print(OUT_MD)
    print("actions", dict(sorted(counts.items())))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
