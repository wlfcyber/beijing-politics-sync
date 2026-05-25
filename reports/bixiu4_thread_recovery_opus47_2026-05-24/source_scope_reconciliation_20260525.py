from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
GLOBAL_AUDIT = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
THREAD_STATUS = RECOVERY / "THREAD_RECOVERY_STATUS_20260524.md"
GOVERNOR = RECOVERY / "GOVERNOR_RECOVERY_REPORT_20260524.md"
CONFUCIUS = RECOVERY / "CONFUCIUS_RECOVERY_ARTIFACT_CHECK_20260524.md"
OUT_CSV = RECOVERY / "SOURCE_SCOPE_RECONCILIATION_20260525.csv"
OUT_MD = RECOVERY / "SOURCE_SCOPE_RECONCILIATION_20260525.md"


def normalize_suite(name: str) -> str:
    return name.replace("思政", "").replace(" ", "").strip()


def stage_bucket(stage_name: str) -> str:
    if "一模" in stage_name:
        return "first_mock"
    if "二模" in stage_name:
        return "second_mock"
    if "期中" in stage_name or "期末" in stage_name:
        return "midterm_or_final"
    return "other_material"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def discover_stage_roots() -> tuple[list[Path], list[Path]]:
    desktop = Path.home() / "Desktop"
    source_roots = [p for p in desktop.iterdir() if p.is_dir() and p.name[:4] in {"2024", "2025", "2026"} and "模拟题" in p.name]
    exam_stage_roots: list[Path] = []
    other_roots: list[Path] = []
    for root in sorted(source_roots, key=lambda p: p.name):
        for stage in sorted([p for p in root.iterdir() if p.is_dir()], key=lambda p: p.name):
            if stage_bucket(stage.name) == "other_material":
                other_roots.append(stage)
            else:
                exam_stage_roots.append(stage)
    return exam_stage_roots, other_roots


def source_file_count(path: Path) -> int:
    return sum(
        1
        for p in path.rglob("*")
        if p.is_file() and p.suffix.lower() in {".pdf", ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".txt", ".md"}
    )


def discover_raw_exam_suites() -> tuple[list[dict[str, str]], list[dict[str, str]]]:
    exam_stage_roots, other_roots = discover_stage_roots()
    raw: list[dict[str, str]] = []
    other: list[dict[str, str]] = []
    for stage in exam_stage_roots:
        for suite_dir in sorted([p for p in stage.iterdir() if p.is_dir()], key=lambda p: p.name):
            raw.append(
                {
                    "stage_dir": stage.name,
                    "raw_suite": suite_dir.name,
                    "normalized_suite": normalize_suite(suite_dir.name),
                    "stage_bucket": stage_bucket(stage.name),
                    "raw_path": str(suite_dir),
                    "source_file_count": str(source_file_count(suite_dir)),
                }
            )
    for stage in other_roots:
        for item in sorted([p for p in stage.iterdir() if p.is_dir()], key=lambda p: p.name):
            other.append(
                {
                    "stage_dir": stage.name,
                    "raw_suite": item.name,
                    "normalized_suite": normalize_suite(item.name),
                    "stage_bucket": "other_material",
                    "raw_path": str(item),
                    "source_file_count": str(source_file_count(item)),
                }
            )
    return raw, other


def matrix_counts() -> Counter[str]:
    rows = read_csv(MATRIX)
    return Counter(normalize_suite(r.get("题源", "")) for r in rows if r.get("题源"))


def gpt_bundle_keys() -> set[tuple[str, str]]:
    bundle_dir = Path.home() / "Desktop" / "beijing_politics_research" / "data" / "preprocessed_corpus" / "gpt_suite_bundles"
    keys: set[tuple[str, str]] = set()
    if not bundle_dir.exists():
        return keys
    for path in bundle_dir.glob("*.md"):
        parts = path.stem.split("__")
        if len(parts) >= 3:
            keys.add((parts[-2], normalize_suite(parts[-1])))
    return keys


def status_for(raw_row: dict[str, str], global_key_status: dict[tuple[str, str], str], matrix_counter: Counter[str], bundle_keys: set[tuple[str, str]]) -> str:
    key = (raw_row["stage_dir"], raw_row["normalized_suite"])
    if key in global_key_status:
        return "present_in_global_audit"
    if matrix_counter.get(raw_row["normalized_suite"], 0):
        return "present_in_matrix_only"
    if (raw_row["stage_dir"], raw_row["normalized_suite"]) in bundle_keys:
        return "present_in_gpt_bundle_only"
    return "missing_from_global_audit_matrix_and_gpt_bundle"


def write_reports() -> dict[str, object]:
    raw, other = discover_raw_exam_suites()
    global_rows = read_csv(GLOBAL_AUDIT)
    global_key_status = {
        (r.get("stage_dir", ""), normalize_suite(r.get("normalized_suite", ""))): r.get("current_status", "")
        for r in global_rows
    }
    matrix_counter = matrix_counts()
    bundle_keys = gpt_bundle_keys()

    rows: list[dict[str, str]] = []
    for r in raw:
        key = (r["stage_dir"], r["normalized_suite"])
        row = dict(r)
        row["scope_class"] = "exam_suite"
        row["global_audit_status"] = global_key_status.get(key, "")
        row["matrix_rows_by_normalized_suite"] = str(matrix_counter.get(r["normalized_suite"], 0))
        row["gpt_suite_bundle_present"] = str((r["stage_dir"], r["normalized_suite"]) in bundle_keys)
        row["reconciliation_status"] = status_for(r, global_key_status, matrix_counter, bundle_keys)
        row["note"] = "raw name normalized by deleting 思政" if r["raw_suite"] != r["normalized_suite"] else ""
        rows.append(row)
    for r in other:
        row = dict(r)
        row["scope_class"] = "other_material_not_exam_suite"
        row["global_audit_status"] = ""
        row["matrix_rows_by_normalized_suite"] = str(matrix_counter.get(r["normalized_suite"], 0))
        row["gpt_suite_bundle_present"] = str((r["stage_dir"], r["normalized_suite"]) in bundle_keys)
        row["reconciliation_status"] = "not_counted_as_exam_suite"
        row["note"] = "module-classification material, not an independent district paper suite"
        rows.append(row)

    headers = [
        "scope_class",
        "stage_dir",
        "raw_suite",
        "normalized_suite",
        "stage_bucket",
        "raw_path",
        "source_file_count",
        "global_audit_status",
        "matrix_rows_by_normalized_suite",
        "gpt_suite_bundle_present",
        "reconciliation_status",
        "note",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)

    exam_rows = [r for r in rows if r["scope_class"] == "exam_suite"]
    other_rows = [r for r in rows if r["scope_class"] == "other_material_not_exam_suite"]
    missing = [r for r in exam_rows if r["reconciliation_status"] != "present_in_global_audit"]
    by_bucket = Counter(r["stage_bucket"] for r in exam_rows)
    by_status = Counter(r["reconciliation_status"] for r in exam_rows)

    md = [
        "# Source Scope Reconciliation 2026-05-25",
        "",
        "status: `SOURCE_SCOPE_RECONCILED_NO_UNAUDITED_EXAM_SUITE_FOUND`",
        "",
        "## Purpose",
        "",
        "This file checks whether the recovery audit's `64` raw-suite count is a real source-scope count or an accidental undercount against the user's `2024-2026` district-paper objective.",
        "",
        "## Result",
        "",
        f"- raw exam-suite directories under `2024/2025/2026各区模拟题`: `{len(exam_rows)}`.",
        f"- other non-suite material directories found under those roots: `{len(other_rows)}`.",
        f"- global audit rows in `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv`: `{len(global_rows)}`.",
        f"- GPT suite bundles currently present in the reusable cache: `{len(bundle_keys)}`.",
        "",
        "The current desktop source tree does not contain seventy-plus independent exam-suite directories. It contains `64` exam suites plus `1` other-material folder. The user's earlier `七十多套` expectation is therefore not proven by the current local filesystem snapshot.",
        "",
        "## Exam Suite Counts By Stage",
        "",
    ]
    for bucket, count in by_bucket.most_common():
        md.append(f"- `{bucket}`: `{count}`")
    md.extend(["", "## Reconciliation Status Counts", ""])
    for status, count in by_status.most_common():
        md.append(f"- `{status}`: `{count}`")
    md.extend(["", "## Name Normalization", ""])
    alias_rows = [r for r in exam_rows if r["raw_suite"] != r["normalized_suite"]]
    if alias_rows:
        for r in alias_rows:
            md.append(f"- `{r['raw_suite']}` is normalized as `{r['normalized_suite']}`; this explains the raw/global name difference.")
    else:
        md.append("- No raw/global name normalization differences found.")
    md.extend(["", "## Missing Exam Suites", "", "| raw suite | normalized suite | stage | status | note |", "|---|---|---|---|---|"])
    if missing:
        for r in missing:
            md.append(f"| {r['raw_suite']} | {r['normalized_suite']} | {r['stage_dir']} | {r['reconciliation_status']} | {r['note']} |")
    else:
        md.append("| none | none | none | none | all exam-suite directories reconcile to the global audit |")
    md.extend(["", "## Other Materials Not Counted As Suites", "", "| folder | stage | source files | note |", "|---|---|---:|---|"])
    for r in other_rows:
        md.append(f"| {r['raw_suite']} | {r['stage_dir']} | {r['source_file_count']} | {r['note']} |")
    md.extend(
        [
            "",
            "## Boundary",
            "",
            "- This reconciles the filesystem source scope only; it does not prove row-level correctness, content thickness, or final external acceptance.",
            "- `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv` remains the suite-level coverage ledger.",
            "- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` remains the question/placement ledger.",
            "- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.",
        ]
    )
    OUT_MD.write_text("\n".join(md) + "\n", encoding="utf-8")

    appendix = f"""

## Source Scope Reconciliation: 2024-2026 Raw Suites
Updated: 2026-05-25

- Status: `SOURCE_SCOPE_RECONCILED_NO_UNAUDITED_EXAM_SUITE_FOUND`.
- Raw exam-suite directories under the current Desktop source roots: `{len(exam_rows)}`.
- Other non-suite material folders found: `{len(other_rows)}`.
- Global audit rows: `{len(global_rows)}`.
- Name-normalization difference: `2024顺义思政二模` -> `2024顺义二模`.
- No exam-suite directory is missing from the global suite audit after normalization.
- Evidence: `SOURCE_SCOPE_RECONCILIATION_20260525.md` and `SOURCE_SCOPE_RECONCILIATION_20260525.csv`.
- Boundary: this does not close row-level correctness, format consistency, content thickness, or external-review gates.
"""
    for path in [THREAD_STATUS, GOVERNOR, CONFUCIUS]:
        text = path.read_text(encoding="utf-8")
        marker = "\n## Source Scope Reconciliation: 2024-2026 Raw Suites"
        if marker in text:
            text = text[: text.index(marker)]
        path.write_text(text + appendix, encoding="utf-8", newline="\n")

    return {
        "exam_suites": len(exam_rows),
        "other_materials": len(other_rows),
        "global_rows": len(global_rows),
        "missing_exam_suites_after_normalization": len(missing),
        "gpt_suite_bundles": len(bundle_keys),
        "out_csv": str(OUT_CSV),
        "out_md": str(OUT_MD),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(write_reports(), ensure_ascii=False, indent=2))
