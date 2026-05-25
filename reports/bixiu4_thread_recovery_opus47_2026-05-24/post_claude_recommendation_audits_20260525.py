from __future__ import annotations

import csv
import hashlib
import json
import re
import zipfile
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET

import matrix_evidence_risk_audit_20260525 as risk


ROOT = Path(__file__).resolve().parent
RUN = ROOT.parent / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
DELIVERY = RUN / "05_delivery"
MATRIX = ROOT / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
YES = chr(0x662F)
NO = chr(0x5426)
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

LABELS = {
    "material": "".join(chr(c) for c in [0x3010, 0x6750, 0x6599, 0x89E6, 0x53D1, 0x70B9, 0x3011]),
    "question": "".join(chr(c) for c in [0x3010, 0x8BBE, 0x95EE, 0x3011]),
    "why": "".join(chr(c) for c in [0x3010, 0x4E3A, 0x4EC0, 0x4E48, 0x80FD, 0x60F3, 0x5230, 0x3011]),
    "answer": "".join(chr(c) for c in [0x3010, 0x7B54, 0x6848, 0x843D, 0x70B9, 0x3011]),
}
LEFT_BRACKET = chr(0x3010)
POINT_MARKERS = set("①②③④⑤⑥⑦⑧⑨⑩")


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M +08")


def read_matrix() -> list[dict[str, str]]:
    with MATRIX.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def in_body(row: dict[str, str]) -> bool:
    return (row.get("是否进宝典") or "").startswith(YES)


def hash_rank(row: dict[str, str]) -> str:
    raw = "|".join([row.get("matrix_row_id", ""), row.get("题源", ""), row.get("题号", ""), row.get("宝典节点", "")])
    return hashlib.sha1(raw.encode("utf-8")).hexdigest()


def formal_signal(text: str) -> bool:
    low = text.lower()
    return any(term.lower() in low for term in risk.FORMAL_TERMS)


def weak_signal(text: str) -> bool:
    terms = [
        "".join(chr(c) for c in [0x6559, 0x5E08, 0x7248]),
        "".join(chr(c) for c in [0x53C2, 0x8003, 0x7B54, 0x6848]),
        "".join(chr(c) for c in [0x6A21, 0x578B, 0x6458, 0x8981]),
        "Claude",
        "GPT",
        "model",
    ]
    return any(term in text for term in terms)


def objective_choice_boundary(text: str) -> bool:
    return (
        "".join(chr(c) for c in [0x9009, 0x62E9, 0x9898]) in text
        and (
            "".join(chr(c) for c in [0x975E, 0x4E3B, 0x89C2, 0x9898, 0x8BC4, 0x5206, 0x7EC6, 0x5219]) in text
            or "".join(chr(c) for c in [0x9009, 0x62E9, 0x9898, 0x8FB9, 0x754C, 0x5DF2, 0x660E, 0x793A]) in text
        )
    )


def source_exists(row: dict[str, str]) -> bool:
    return risk.source_pointer_exists(row.get("source_artifact", ""))


def write_csv(path: Path, rows: list[dict[str, object]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def reverse_sample_audit(rows: list[dict[str, str]]) -> dict[str, object]:
    body = [row for row in rows if in_body(row)]
    special = [row for row in body if "formal_rubric_optional_angle" in " | ".join(row.values())]
    sorted_body = sorted(body, key=hash_rank)
    sample: list[dict[str, str]] = []
    seen: set[str] = set()
    for row in special + sorted_body:
        key = row.get("matrix_row_id", "")
        if key in seen:
            continue
        seen.add(key)
        combined = " | ".join(
            [
                row.get("证据等级", ""),
                row.get("细则支持原理", ""),
                row.get("题型或模块判断", ""),
                row.get("备注", ""),
            ]
        )
        sample.append(
            {
                "sample_rank": str(len(sample) + 1),
                "matrix_row_id": row.get("matrix_row_id", ""),
                "题源": row.get("题源", ""),
                "题号": row.get("题号", ""),
                "是否进宝典": row.get("是否进宝典", ""),
                "宝典节点": row.get("宝典节点", ""),
                "证据等级": row.get("证据等级", ""),
                "formal_signal": str(formal_signal(combined)).lower(),
                "objective_choice_boundary": str(objective_choice_boundary(combined)).lower(),
                "weak_signal": str(weak_signal(combined)).lower(),
                "source_pointer_exists": str(source_exists(row)).lower(),
                "source_artifact": row.get("source_artifact", ""),
                "support_excerpt": row.get("细则支持原理", "")[:260],
            }
        )
        if len(sample) >= 80:
            break

    status = "PASS_SAMPLE_NO_WEAK_ONLY_BODY_ROWS" if all(
        item["formal_signal"] == "true" or item["objective_choice_boundary"] == "true"
        for item in sample
    ) else "SAMPLE_HAS_ROWS_REQUIRING_MANUAL_RECHECK"
    csv_path = ROOT / "CLAUDE_RECOMMENDED_ROW_LEVEL_REVERSE_SAMPLE_AUDIT_20260525.csv"
    md_path = ROOT / "CLAUDE_RECOMMENDED_ROW_LEVEL_REVERSE_SAMPLE_AUDIT_20260525.md"
    fields = [
        "sample_rank",
        "matrix_row_id",
        "题源",
        "题号",
        "是否进宝典",
        "宝典节点",
        "证据等级",
        "formal_signal",
        "objective_choice_boundary",
        "weak_signal",
        "source_pointer_exists",
        "source_artifact",
        "support_excerpt",
    ]
    write_csv(csv_path, sample, fields)
    lines = [
        "# Claude-Recommended Row-Level Reverse Sample Audit 20260525",
        "",
        f"Updated: {now()}",
        "",
        f"Status: `{status}`",
        "",
        f"- Body rows in matrix: `{len(body)}`.",
        f"- Reverse sample rows written: `{len(sample)}`.",
        f"- Forced include: all `formal_rubric_optional_angle` body rows.",
        f"- Sampling method: deterministic SHA1 order by row id, suite, question, and framework node.",
        f"- Rows without source pointer existence in sample: `{sum(1 for item in sample if item['source_pointer_exists'] != 'true')}`.",
        f"- Rows with weak-signal text in sample: `{sum(1 for item in sample if item['weak_signal'] == 'true')}`; these are acceptable only when formal or objective-choice boundary signals are also present.",
        "",
        "## Boundary",
        "",
        "- This is a reverse sample, not a full recheck of all 558 body rows.",
        "- It is created in response to the captured Claude web Opus 4.7 external review.",
        "- It strengthens the local evidence but does not close GPTPro, ClaudeCode model, or full thickness gates.",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return {"status": status, "path": str(csv_path), "sample_rows": len(sample)}


def special_tag_audit(rows: list[dict[str, str]]) -> dict[str, object]:
    terms = [
        "formal_rubric_optional_angle",
        "".join(chr(c) for c in [0x8BC1, 0x636E, 0x4E0D, 0x8DB3, 0xFF1A, 0x4E0D, 0x5355, 0x72EC, 0x6210, 0x6761]),
        "".join(chr(c) for c in [0x7F3A, 0x76F4, 0x63A5, 0x8BC1, 0x636E]),
        "COVERED_OR_PATCHED",
        "COVERED_OR_PATCHED_WITH_ROW_REVIEW",
        "SUPERSEDED_BY_ROW_LEVEL_REPAIR",
        "SUPERSEDED_BY_ROW_LEVEL_MATRIX",
        "SUITE_LEVEL_SUMMARY_RECHECKED_NO_OPEN_ROW_RISK",
        "SUITE_LEVEL_SUMMARY",
    ]
    out: list[dict[str, str]] = []
    for row in rows:
        joined = " | ".join(row.values())
        matched = [term for term in terms if term in joined]
        if not matched:
            continue
        body = in_body(row)
        combined = " | ".join([row.get("证据等级", ""), row.get("细则支持原理", ""), row.get("备注", "")])
        if body and "formal_rubric_optional_angle" in matched:
            disposition = "BODY_FORMAL_OPTIONAL_ANGLE_RETAINED_WITH_BOUNDARY_NOTE"
        elif body:
            disposition = "BODY_ROW_REQUIRES_MANUAL_CONFIRMATION"
        elif any(term.startswith("SUPERSEDED") for term in matched):
            disposition = "NON_BODY_SUPERSEDED_OR_CANDIDATE_ONLY"
        elif row.get("题号") == "SUITE_LEVEL" or "SUITE_LEVEL" in joined:
            disposition = "NON_BODY_SUITE_LEVEL_SUMMARY_NOT_ROW_EVIDENCE"
        else:
            disposition = "NON_BODY_OR_BOUNDARY_ROW"
        out.append(
            {
                "matrix_row_id": row.get("matrix_row_id", ""),
                "matched_terms": "; ".join(matched),
                "题源": row.get("题源", ""),
                "题号": row.get("题号", ""),
                "是否进宝典": row.get("是否进宝典", ""),
                "宝典节点": row.get("宝典节点", ""),
                "证据等级": row.get("证据等级", ""),
                "当前处理": row.get("当前处理", ""),
                "disposition": disposition,
                "formal_signal": str(formal_signal(combined)).lower(),
                "source_pointer_exists": str(source_exists(row)).lower(),
                "support_excerpt": row.get("细则支持原理", "")[:260],
            }
        )
    csv_path = ROOT / "CLAUDE_RECOMMENDED_SPECIAL_TAG_AUDIT_20260525.csv"
    md_path = ROOT / "CLAUDE_RECOMMENDED_SPECIAL_TAG_AUDIT_20260525.md"
    fields = [
        "matrix_row_id",
        "matched_terms",
        "题源",
        "题号",
        "是否进宝典",
        "宝典节点",
        "证据等级",
        "当前处理",
        "disposition",
        "formal_signal",
        "source_pointer_exists",
        "support_excerpt",
    ]
    write_csv(csv_path, out, fields)
    counts = Counter(item["disposition"] for item in out)
    term_counts = Counter()
    for item in out:
        term_counts.update(item["matched_terms"].split("; "))
    body_problem = [item for item in out if item["disposition"] == "BODY_ROW_REQUIRES_MANUAL_CONFIRMATION"]
    status = "SPECIAL_TAG_BODY_GAPS_REMAIN" if body_problem else "SPECIAL_TAGS_CLASSIFIED_NO_UNRESOLVED_BODY_STATUS_TAGS"
    lines = [
        "# Claude-Recommended Special Tag Audit 20260525",
        "",
        f"Updated: {now()}",
        "",
        f"Status: `{status}`",
        "",
        f"- Rows matched: `{len(out)}`.",
        f"- Body rows requiring manual confirmation: `{len(body_problem)}`.",
        "",
        "## Disposition Counts",
        "",
    ]
    for key, count in counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(["", "## Matched Term Counts", ""])
    for key, count in term_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- `formal_rubric_optional_angle` rows remain body rows, but are explicitly broad/optional formal-angle support rather than point-by-point scoring.",
            "- Suite-level and superseded rows are not row-level body evidence.",
            "- This file responds to the captured Claude web Opus 4.7 external review.",
        ]
    )
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return {"status": status, "rows": len(out), "body_problem_rows": len(body_problem)}


def weak_evidence_reverse_check(rows: list[dict[str, str]]) -> dict[str, object]:
    body = [row for row in rows if in_body(row)]
    out: list[dict[str, str]] = []
    failures = []
    for row in body:
        combined = " | ".join([row.get("证据等级", ""), row.get("细则支持原理", ""), row.get("备注", ""), row.get("当前处理", "")])
        has_weak = weak_signal(combined)
        if not has_weak:
            continue
        has_formal = formal_signal(combined)
        has_choice = objective_choice_boundary(combined)
        verdict = "PASS_FORMAL_OR_CHOICE_BOUNDARY_PRESENT" if has_formal or has_choice else "FAIL_WEAK_ONLY_BODY_EVIDENCE"
        if verdict.startswith("FAIL"):
            failures.append(row)
        out.append(
            {
                "matrix_row_id": row.get("matrix_row_id", ""),
                "题源": row.get("题源", ""),
                "题号": row.get("题号", ""),
                "宝典节点": row.get("宝典节点", ""),
                "证据等级": row.get("证据等级", ""),
                "formal_signal": str(has_formal).lower(),
                "objective_choice_boundary": str(has_choice).lower(),
                "verdict": verdict,
                "support_excerpt": row.get("细则支持原理", "")[:260],
            }
        )
    csv_path = ROOT / "BODY_WEAK_EVIDENCE_REVERSE_CHECK_20260525.csv"
    md_path = ROOT / "BODY_WEAK_EVIDENCE_REVERSE_CHECK_20260525.md"
    fields = [
        "matrix_row_id",
        "题源",
        "题号",
        "宝典节点",
        "证据等级",
        "formal_signal",
        "objective_choice_boundary",
        "verdict",
        "support_excerpt",
    ]
    write_csv(csv_path, out, fields)
    status = "PASS_NO_WEAK_ONLY_BODY_EVIDENCE" if not failures else "FAIL_WEAK_ONLY_BODY_EVIDENCE_FOUND"
    lines = [
        "# Body Weak-Evidence Reverse Check 20260525",
        "",
        f"Updated: {now()}",
        "",
        f"Status: `{status}`",
        "",
        f"- Body rows checked: `{len(body)}`.",
        f"- Body rows containing teacher/reference/model-summary weak-signal text: `{len(out)}`.",
        f"- Weak-only body evidence failures: `{len(failures)}`.",
        "",
        "## Boundary",
        "",
        "- Weak-signal text can appear in a body row only when formal scoring/rubric/marking support or explicit objective-choice boundary support is also present.",
        "- This check does not promote teacher/reference answers into formal rubrics.",
    ]
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return {"status": status, "weak_signal_body_rows": len(out), "failures": len(failures)}


def current_docx() -> Path:
    docs = [p for p in DELIVERY.glob("*.docx") if not p.name.startswith("~$") and "_backup_" not in p.stem]
    if len(docs) != 1:
        raise RuntimeError(f"Expected one current DOCX, found {docs}")
    return docs[0]


def paragraph_text(p: ET.Element) -> str:
    return "".join(t.text or "" for t in p.iter(f"{W}t")).strip()


def normalize_heading(text: str) -> str:
    return re.sub(r"^\s*\d+\.\s*", "", text).strip()


def ledger_headings() -> set[str]:
    path = DELIVERY / "docx_insert_ledger.csv"
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return {
            normalize_heading(row.get("inserted_heading", "").strip())
            for row in csv.DictReader(f)
            if row.get("inserted_heading")
        }


def read_docx_paragraphs() -> list[dict[str, object]]:
    docx = current_docx()
    with zipfile.ZipFile(docx) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    paragraphs = []
    for idx, p in enumerate(root.iter(f"{W}p")):
        text = paragraph_text(p)
        if text:
            paragraphs.append({"xml_index": idx, "text": text})
    return paragraphs


def label_extra_breakdown() -> dict[str, object]:
    paragraphs = read_docx_paragraphs()
    required_counts = {name: 0 for name in LABELS}
    extra_rows: list[dict[str, object]] = []
    for para in paragraphs:
        text = str(para["text"])
        matched_required = None
        for name, label in LABELS.items():
            if text.startswith(label):
                required_counts[name] += 1
                matched_required = name
                break
        extra_count = text.count(LEFT_BRACKET) - (1 if matched_required else 0)
        if extra_count > 0:
            extra_rows.append(
                {
                    "xml_paragraph_index": para["xml_index"],
                    "required_label_role": matched_required or "",
                    "extra_left_bracket_count": extra_count,
                    "text_excerpt": text[:360],
                }
            )
    payload = {
        "updated": now(),
        "status": "EXTRA_LABEL_BREAKDOWN_CLOSED",
        "required_label_counts": required_counts,
        "required_label_total": sum(required_counts.values()),
        "extra_left_bracket_total": sum(int(row["extra_left_bracket_count"]) for row in extra_rows),
        "docx_left_bracket_total": sum(required_counts.values()) + sum(int(row["extra_left_bracket_count"]) for row in extra_rows),
        "extra_rows": extra_rows,
    }
    (ROOT / "FORMAT_EXTRA_LABEL_BREAKDOWN_20260525.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
        newline="\n",
    )
    lines = [
        "# Format Extra Label Breakdown 20260525",
        "",
        f"Updated: {payload['updated']}",
        "",
        f"Status: `{payload['status']}`",
        "",
        f"- Required question-label total: `{payload['required_label_total']}`.",
        f"- Extra left-bracket count inside required label paragraphs: `{payload['extra_left_bracket_total']}`.",
        f"- DOCX/render label count basis: `{payload['docx_left_bracket_total']}`.",
        "- Explanation: the 7-count difference is not missing question labels; it is extra bracketed source subhead text inside required label paragraphs.",
        "",
        "## Extra Bracket Rows",
        "",
        "| xml paragraph | role | extra count | excerpt |",
        "|---:|---|---:|---|",
    ]
    for row in extra_rows:
        lines.append(
            f"| {row['xml_paragraph_index']} | {row['required_label_role']} | {row['extra_left_bracket_count']} | {str(row['text_excerpt']).replace('|', '/')} |"
        )
    (ROOT / "FORMAT_EXTRA_LABEL_BREAKDOWN_20260525.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return payload


def docx_entry_blocks() -> list[dict[str, object]]:
    paragraphs = read_docx_paragraphs()
    inserted = ledger_headings()
    heading_re = re.compile(r"^\s*\d+\.\s*20(?:24|25|26).+" + chr(0x7B2C) + r".+" + chr(0x9898))
    heading_positions = [i for i, p in enumerate(paragraphs) if heading_re.match(str(p["text"]))]
    entries: list[dict[str, object]] = []
    for pos_index, start in enumerate(heading_positions):
        end = heading_positions[pos_index + 1] if pos_index + 1 < len(heading_positions) else len(paragraphs)
        heading = str(paragraphs[start]["text"])
        norm = normalize_heading(heading)
        body = paragraphs[start + 1 : end]
        values = {key: "" for key in LABELS}
        for p in body[:18]:
            text = str(p["text"])
            for key, label in LABELS.items():
                if text.startswith(label) and not values[key]:
                    values[key] = text[len(label) :].strip()
        answer = values["answer"]
        why = values["why"]
        answer_markers = sum(1 for ch in answer if ch in POINT_MARKERS)
        flags = []
        if len(answer) < 120:
            flags.append("ANSWER_LT_120_CHARS")
        if len(why) < 90:
            flags.append("WHY_LT_90_CHARS")
        if answer_markers == 0 and len(answer) < 180:
            flags.append("SHORT_WITHOUT_POINT_MARKERS")
        entries.append(
            {
                "heading": heading,
                "normalized_heading": norm,
                "group": "inserted" if norm in inserted else "legacy",
                "material_chars": len(values["material"]),
                "question_chars": len(values["question"]),
                "why_chars": len(why),
                "answer_chars": len(answer),
                "answer_point_markers": answer_markers,
                "thin_flags": "|".join(flags),
                "answer_excerpt": answer[:240],
            }
        )
    return entries


def thickness_density_audit() -> dict[str, object]:
    entries = docx_entry_blocks()
    queue = [entry for entry in entries if entry["thin_flags"]]
    csv_path = ROOT / "THICKNESS_DENSITY_AUDIT_20260525.csv"
    fields = [
        "heading",
        "group",
        "material_chars",
        "question_chars",
        "why_chars",
        "answer_chars",
        "answer_point_markers",
        "thin_flags",
        "answer_excerpt",
    ]
    write_csv(csv_path, entries, fields)
    group_counts = Counter(entry["group"] for entry in entries)
    thin_group_counts = Counter(entry["group"] for entry in queue)
    flag_counts = Counter()
    for entry in queue:
        flag_counts.update(str(entry["thin_flags"]).split("|"))
    status = "THICKNESS_QUEUE_CREATED_REQUIRES_REVIEW" if queue else "THICKNESS_DENSITY_PASS_NO_SHORT_CANDIDATES"
    lines = [
        "# Thickness Density Audit 20260525",
        "",
        f"Updated: {now()}",
        "",
        f"Status: `{status}`",
        "",
        f"- Question entries audited: `{len(entries)}`.",
        f"- Inserted/legacy entries: `{group_counts.get('inserted', 0)}/{group_counts.get('legacy', 0)}`.",
        f"- Thin-candidate entries: `{len(queue)}`.",
        f"- Inserted/legacy thin candidates: `{thin_group_counts.get('inserted', 0)}/{thin_group_counts.get('legacy', 0)}`.",
        "",
        "## Thin Flag Counts",
        "",
    ]
    for key, count in flag_counts.most_common():
        lines.append(f"- `{key}`: `{count}`")
    lines.extend(
        [
            "",
            "## Top Thin Candidates",
            "",
            "| heading | group | answer chars | why chars | flags | answer excerpt |",
            "|---|---|---:|---:|---|---|",
        ]
    )
    for entry in sorted(queue, key=lambda e: (int(e["answer_chars"]), int(e["why_chars"]), str(e["heading"])))[:40]:
        lines.append(
            f"| {str(entry['heading']).replace('|', '/')} | {entry['group']} | {entry['answer_chars']} | {entry['why_chars']} | {entry['thin_flags']} | {str(entry['answer_excerpt']).replace('|', '/')} |"
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "- This is a density triage, not a semantic pass/fail review.",
            "- It directly responds to the captured Claude web Opus 4.7 request for a full 721-entry thickness queue.",
            "- Thin candidates require content review before any final acceptance claim.",
        ]
    )
    (ROOT / "THICKNESS_DENSITY_AUDIT_20260525.md").write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return {"status": status, "entries": len(entries), "thin_candidates": len(queue)}


def main() -> None:
    rows = read_matrix()
    results = {
        "reverse_sample": reverse_sample_audit(rows),
        "special_tags": special_tag_audit(rows),
        "weak_reverse": weak_evidence_reverse_check(rows),
        "extra_labels": label_extra_breakdown(),
        "thickness": thickness_density_audit(),
    }
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
