#!/usr/bin/env python3
import csv
import json
import re
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[2]
SOURCE_INVENTORY = RUN_DIR / "01_source_inventory" / "SOURCE_INVENTORY.csv"
SUITE_INVENTORY = RUN_DIR / "01_source_inventory" / "SUITE_INVENTORY.csv"


HARD_SAMPLE_SUITES = {
    "2026_通州_期末": {
        "question": "Q20",
        "module": "选必一",
        "status": "codex_source_checked",
        "paper_source_ids": {"SRC_b66cc2d35877"},
        "scoring_source_ids": {"SRC_35ef9424281a"},
    },
    "2026_朝阳_期中": {
        "question": "Q17",
        "module": "选必一",
        "status": "codex_source_checked",
        "paper_source_ids": {"SRC_cdafdcaa0136"},
        "scoring_source_ids": {"SRC_763b7470b96b", "SRC_1babd6c525fe"},
    },
    "2025_海淀_期中": {
        "question": "Q16(2);Q21(2)",
        "module": "选必一",
        "status": "codex_source_checked",
        "paper_source_ids": {"SRC_e3da1b6b45ca"},
        "scoring_source_ids": {"SRC_cda046c2d36d"},
    },
}


KNOWN_SPECIAL_SUITES = {
    "2026_石景山_期末": "excluded_not_relevant",
    "2026_海淀_期末": "unknown_needs_current_no_module_check",
}


def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path, rows, fields):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def suite_id(row):
    year = row.get("year_hint") or "unknown_year"
    district = row.get("district_hint") or "unknown_district"
    stage = row.get("stage_hint") or "unknown_stage"
    if district == "北京" and row.get("root_label"):
        district = "mixed_or_compilation"
    return f"{year}_{district}_{stage}"


def bool_text(value):
    return "yes" if value else "no"


def verified_level(row, sid):
    source_id = row["source_id"]
    guess = row.get("evidence_guess", "")
    if sid in KNOWN_SPECIAL_SUITES:
        return KNOWN_SPECIAL_SUITES[sid]
    if sid in HARD_SAMPLE_SUITES and source_id in HARD_SAMPLE_SUITES[sid]["scoring_source_ids"]:
        if sid == "2025_海淀_期中":
            return "P0_verified_rubric"
        if row.get("file_flags") == "ppt":
            return "P0_verified_scoring_rule"
        return "P0_verified_marking_detail"
    if sid in HARD_SAMPLE_SUITES and source_id in HARD_SAMPLE_SUITES[sid]["paper_source_ids"]:
        return "P3_paper_only"
    if guess.startswith("P0"):
        return "pending_content_recheck"
    if guess.startswith("P1"):
        return "P1_reference_answer"
    if guess.startswith("P2"):
        return "P2_teaching_or_lecture_pending_role_check"
    if guess.startswith("P3"):
        return "P3_paper_only_pending_question_scan"
    return "unknown_needs_visual_check"


def source_flags(row):
    flags = row.get("file_flags", "")
    suffix = row.get("suffix", "").lower()
    return {
        "has_pdf_visual_risk": bool_text("pdf" in flags),
        "has_ppt_visual_risk": bool_text("ppt" in flags),
        "has_image_or_table": bool_text(any(x in flags for x in ["image", "table"]) or suffix in [".png", ".jpg", ".jpeg"]),
        "needs_ocr": bool_text("pdf" in flags or suffix in [".png", ".jpg", ".jpeg"]),
    }


def build_source_ledgers(source_rows):
    rows = []
    for row in source_rows:
        sid = suite_id(row)
        guess = row.get("evidence_guess", "")
        verified = verified_level(row, sid)
        flags = source_flags(row)
        sample = HARD_SAMPLE_SUITES.get(sid)
        contains_xuanbiyi = "yes" if sample else "unknown"
        contains_subjective = "yes" if sample else "unknown"
        qnums = sample["question"] if sample else ""
        if sid == "2026_石景山_期末":
            contains_xuanbiyi = "no"
            contains_subjective = "no"
        if sid == "2026_海淀_期末":
            contains_xuanbiyi = "user_confirmed_no_pending_current_check"
            contains_subjective = "unknown"
        rows.append(
            {
                "source_id": row["source_id"],
                "year": row.get("year_hint", ""),
                "district_or_exam_scope": row.get("district_hint", ""),
                "exam_type": row.get("stage_hint", ""),
                "suite_id": sid,
                "file_type": row.get("suffix", ""),
                "raw_category": row.get("relative_path", ""),
                "candidate_evidence_level": guess,
                "verified_evidence_level": verified,
                "contains_xuanbiyi": contains_xuanbiyi,
                "contains_subjective_question": contains_subjective,
                "question_numbers_detected": qnums,
                "has_scoring_detail": bool_text(guess.startswith("P0")),
                "has_reference_answer": bool_text(guess.startswith("P1")),
                "has_teaching_or_lecture": bool_text(guess.startswith("P2")),
                **flags,
                "status": "source_checked" if sample else "pending_phase02_recheck",
                "blocker": "" if sample else ("excluded by user rule" if sid == "2026_石景山_期末" else ""),
            }
        )
    fields = [
        "source_id",
        "year",
        "district_or_exam_scope",
        "exam_type",
        "suite_id",
        "file_type",
        "raw_category",
        "candidate_evidence_level",
        "verified_evidence_level",
        "contains_xuanbiyi",
        "contains_subjective_question",
        "question_numbers_detected",
        "has_scoring_detail",
        "has_reference_answer",
        "has_teaching_or_lecture",
        "has_pdf_visual_risk",
        "has_ppt_visual_risk",
        "has_image_or_table",
        "needs_ocr",
        "status",
        "blocker",
    ]
    write_csv(RUN_DIR / "01_source_inventory" / "source_ledger_updated.csv", rows, fields)
    write_csv(RUN_DIR / "03_entries" / "evidence_level_recheck.csv", rows, fields)
    return rows, fields


def build_suite_question_matrix(suite_rows, source_ledger_rows):
    by_suite = {}
    for row in source_ledger_rows:
        by_suite.setdefault(row["suite_id"], []).append(row)
    out = []
    for suite in suite_rows:
        sid = suite["suite_id"]
        sample = HARD_SAMPLE_SUITES.get(sid)
        source_rows = by_suite.get(sid, [])
        verified_counts = {}
        for row in source_rows:
            key = row["verified_evidence_level"]
            verified_counts[key] = verified_counts.get(key, 0) + 1
        out.append(
            {
                "suite_id": sid,
                "year": suite.get("year", ""),
                "district": suite.get("district", ""),
                "exam_type": suite.get("stage", ""),
                "question_no": sample["question"] if sample else "",
                "module_status": sample["module"] if sample else ("excluded" if sid == "2026_石景山_期末" else "pending_question_scan"),
                "contains_xuanbiyi_subjective": "yes" if sample else ("no" if sid == "2026_石景山_期末" else "unknown"),
                "paper_source_ids": "|".join(sorted(sample["paper_source_ids"])) if sample else "",
                "scoring_source_ids": "|".join(sorted(sample["scoring_source_ids"])) if sample else "",
                "verified_evidence_counts": json.dumps(verified_counts, ensure_ascii=False, sort_keys=True),
                "status": sample["status"] if sample else suite.get("status", "pending_question_scan"),
                "blocker": suite.get("notes", ""),
            }
        )
    fields = [
        "suite_id",
        "year",
        "district",
        "exam_type",
        "question_no",
        "module_status",
        "contains_xuanbiyi_subjective",
        "paper_source_ids",
        "scoring_source_ids",
        "verified_evidence_counts",
        "status",
        "blocker",
    ]
    write_csv(RUN_DIR / "03_entries" / "suite_question_matrix.csv", out, fields)


def parse_entry_file(path, suite_id_value, sample, question=None):
    text = path.read_text(encoding="utf-8")
    entries = []
    headers = []
    stack = {}
    for m in re.finditer(r"^(##+)\s+(.+)$", text, re.M):
        level = len(m.group(1))
        stack[level] = m.group(2).strip()
        for old_level in list(stack):
            if old_level > level:
                del stack[old_level]
        path_title = " / ".join(stack[k] for k in sorted(stack) if k >= 2)
        headers.append((m.start(), path_title))
    term_matches = list(re.finditer(r"^\*\*术语：(.+?)\*\*", text, re.M))
    for idx, term_match in enumerate(term_matches):
        question_no = question or sample["question"]
        start = term_match.start()
        end = term_matches[idx + 1].start() if idx + 1 < len(term_matches) else len(text)
        part = text[start:end]
        current_bucket = ""
        for pos, title in headers:
            if pos < start:
                current_bucket = title
            else:
                break
        term_match = re.search(r"\*\*术语：(.+?)\*\*", part)
        if not term_match:
            continue
        def field(name):
            m = re.search(rf"^- {name}：(.+)$", part, re.M)
            return m.group(1).strip() if m else ""
        entries.append(
            {
                "entry_id": f"{suite_id_value}_{question_no}_{len(entries)+1:02d}",
                "source_id": "|".join(sorted(sample["scoring_source_ids"])),
                "year": suite_id_value.split("_")[0],
                "district_or_exam_scope": suite_id_value.split("_")[1],
                "exam_type": suite_id_value.split("_")[2],
                "question_no": question_no,
                "sub_question_no": "",
                "question_type": "主观题",
                "module": "选必一",
                "unit_or_topic": current_bucket,
                "material_trigger": field("材料触发"),
                "scoring_term": term_match.group(1).strip(),
                "term_function": current_bucket,
                "why_this_term": field("材料触发"),
                "answer_landing": field("答案句"),
                "evidence_level": "P0_current_run_source_checked",
                "evidence_source_type": "formal_scoring_or_marking_detail",
                "needs_visual_check": "no",
                "needs_claudecode_compare": "yes",
                "old_final_quality_reference_used": "no",
                "status": "phase02_hard_sample_codex_checked",
            }
        )
    return entries


def build_subjective_entries():
    all_entries = []
    file_map = [
        ("2026_通州_期末", "Q20", RUN_DIR / "codex_lane" / "entries" / "2026通州期末_Q20.md"),
        ("2026_朝阳_期中", "Q17", RUN_DIR / "codex_lane" / "entries" / "2026朝阳期中_Q17.md"),
        ("2025_海淀_期中", "Q16(2)", RUN_DIR / "codex_lane" / "entries" / "2025海淀期中_Q16(2).md"),
        ("2025_海淀_期中", "Q21(2)", RUN_DIR / "codex_lane" / "entries" / "2025海淀期中_Q21(2).md"),
    ]
    for sid, question, path in file_map:
        if path.exists():
            all_entries.extend(parse_entry_file(path, sid, HARD_SAMPLE_SUITES[sid], question=question))
    fields = [
        "entry_id",
        "source_id",
        "year",
        "district_or_exam_scope",
        "exam_type",
        "question_no",
        "sub_question_no",
        "question_type",
        "module",
        "unit_or_topic",
        "material_trigger",
        "scoring_term",
        "term_function",
        "why_this_term",
        "answer_landing",
        "evidence_level",
        "evidence_source_type",
        "needs_visual_check",
        "needs_claudecode_compare",
        "old_final_quality_reference_used",
        "status",
    ]
    write_csv(RUN_DIR / "03_entries" / "xuanbiyi_subjective_index.csv", all_entries, fields)
    jsonl = RUN_DIR / "03_entries" / "xuanbiyi_subjective_entries_phase02.jsonl"
    with jsonl.open("w", encoding="utf-8") as f:
        for row in all_entries:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")
    return all_entries


def write_report(source_rows, entry_rows):
    counts = {}
    for row in source_rows:
        key = row["verified_evidence_level"]
        counts[key] = counts.get(key, 0) + 1
    out = RUN_DIR / "08_review" / "phase_reports" / "phase02_codex_source_lock_report.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Phase 02 Codex Source Lock Report",
        "",
        "status: initial_matrix_built",
        "",
        "## Current Counts",
        "",
        f"- source rows: {len(source_rows)}",
        f"- hard-sample entries indexed: {len(entry_rows)}",
        "- verified evidence counts:",
    ]
    for key in sorted(counts):
        lines.append(f"  - {key}: {counts[key]}")
    lines.extend(
        [
            "",
            "## Boundary Notes",
            "",
            "- This is an initial Phase 02 matrix, not a final term document.",
            "- `pending_content_recheck` rows still require content-level inspection before use.",
            "- Old final artifacts are not evidence and are not used in the indexed hard samples.",
            "- GPT advice is not evidence; it only triggered this local matrix task.",
            "",
            "## Hard Samples Included",
            "",
            "- 2026通州期末 Q20: 6 Codex entries indexed from current-run paper PDF and scoring PPTX locators.",
            "- 2026朝阳期中 Q17: 3 Codex entries indexed from current-run paper PDF and scoring DOCX locators.",
            "- 2025海淀期中 Q16(2)/Q21(2): 6 Codex entries indexed from current-run paper PDF and embedded scoring-image DOCX locators.",
        ]
    )
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    source_rows = read_csv(SOURCE_INVENTORY)
    suite_rows = read_csv(SUITE_INVENTORY)
    source_ledger_rows, _ = build_source_ledgers(source_rows)
    build_suite_question_matrix(suite_rows, source_ledger_rows)
    entry_rows = build_subjective_entries()
    write_report(source_ledger_rows, entry_rows)


if __name__ == "__main__":
    main()
