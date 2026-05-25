from __future__ import annotations

import csv
import re
import zipfile
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RECOVERY = ROOT / "reports" / "bixiu4_thread_recovery_opus47_2026-05-24"
RUN = ROOT / "reports" / "bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24"
SOURCE_AUDIT = RUN / "06_governor_confucius" / "FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.csv"
MATRIX = RECOVERY / "FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv"
DELIVERY = RUN / "05_delivery"
OUT_CSV = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.csv"
OUT_MD = RECOVERY / "GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md"


def current_docx_text() -> str:
    docs = [p for p in DELIVERY.glob("*.docx") if "_backup_" not in p.stem and not p.name.startswith("~$")]
    if len(docs) != 1:
        raise RuntimeError(f"expected one current docx, found {docs}")
    with zipfile.ZipFile(docs[0]) as zf:
        xml = zf.read("word/document.xml").decode("utf-8", errors="replace")
    return re.sub(r"<[^>]+>", "", xml)


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def normalize_suite(name: str) -> str:
    return name.replace("思政", "").replace(" ", "").strip()


def stage_bucket(stage_name: str) -> str:
    if "一模" in stage_name:
        return "first_mock"
    if "二模" in stage_name:
        return "second_mock"
    if "期中" in stage_name or "期末" in stage_name:
        return "midterm_or_final"
    return "other"


def discover_raw_suites() -> list[dict[str, str]]:
    desktop = Path.home() / "Desktop"
    roots = [p for p in desktop.iterdir() if p.is_dir() and p.name[:4] in {"2024", "2025", "2026"}]
    rows: list[dict[str, str]] = []
    for root in sorted(roots, key=lambda p: p.name):
        year = root.name[:4]
        for stage in sorted([p for p in root.iterdir() if p.is_dir()], key=lambda p: p.name):
            bucket = stage_bucket(stage.name)
            if bucket == "other":
                continue
            for suite_dir in sorted([p for p in stage.iterdir() if p.is_dir()], key=lambda p: p.name):
                rows.append(
                    {
                        "raw_suite": suite_dir.name,
                        "normalized_suite": normalize_suite(suite_dir.name),
                        "year": year,
                        "stage_dir": stage.name,
                        "stage_bucket": bucket,
                        "raw_path": str(suite_dir),
                        "source_file_count": str(sum(1 for p in suite_dir.rglob("*") if p.is_file())),
                    }
                )
    return rows


def main() -> None:
    raw = discover_raw_suites()
    source_audit = read_csv(SOURCE_AUDIT)
    matrix = read_csv(MATRIX)
    docx_text = current_docx_text()

    source_by_suite = {normalize_suite(r.get("suite", "")): r for r in source_audit}
    matrix_counter = Counter(normalize_suite(r.get("题源", "")) for r in matrix)

    out_rows = []
    for row in raw:
        suite = row["normalized_suite"]
        in_source_audit = suite in source_by_suite
        matrix_rows = matrix_counter.get(suite, 0)
        docx_mentions = docx_text.count(suite)
        status = "covered_by_current_audit_or_matrix"
        blocker = ""
        if row["stage_bucket"] == "midterm_or_final" and not in_source_audit and matrix_rows == 0:
            status = "missing_from_current_47_suite_audit_scope"
            blocker = "raw midterm/final suite exists but current strict coverage audit is first/second mock scoped"
        elif not in_source_audit and matrix_rows == 0:
            status = "missing_from_current_audit_and_matrix"
            blocker = "raw suite exists but no current source-audit or matrix row"
        elif docx_mentions == 0:
            status = "no_docx_mention_after_normalization"
            blocker = "needs source review before assuming no relevant philosophy/culture entries"
        out = dict(row)
        out.update(
            {
                "in_full_source_vs_docx_audit": str(in_source_audit),
                "matrix_rows": str(matrix_rows),
                "current_docx_mentions": str(docx_mentions),
                "current_status": status,
                "blocker_or_next_action": blocker,
            }
        )
        out_rows.append(out)

    headers = [
        "raw_suite",
        "normalized_suite",
        "year",
        "stage_dir",
        "stage_bucket",
        "raw_path",
        "source_file_count",
        "in_full_source_vs_docx_audit",
        "matrix_rows",
        "current_docx_mentions",
        "current_status",
        "blocker_or_next_action",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(out_rows)

    by_bucket = Counter(r["stage_bucket"] for r in out_rows)
    by_status = Counter(r["current_status"] for r in out_rows)
    missing = [r for r in out_rows if r["current_status"] != "covered_by_current_audit_or_matrix"]
    missing_midterm = [r for r in missing if r["stage_bucket"] == "midterm_or_final"]
    missing_other = [r for r in missing if r["stage_bucket"] != "midterm_or_final"]

    md_lines = [
        "# Global Raw Suite Exhaustion Audit 2026-05-25",
        "",
        "status: `GLOBAL_SOURCE_SCOPE_GAP_FOUND`",
        "",
        "## Summary",
        "",
        f"- raw suite directories discovered under Desktop 2024-2026 stage folders: `{len(out_rows)}`",
        f"- first/second mock raw suites: `{by_bucket['first_mock'] + by_bucket['second_mock']}`",
        f"- midterm/final raw suites: `{by_bucket['midterm_or_final']}`",
        f"- current FULL_SOURCE_VS_DOCX audit rows: `{len(source_audit)}`",
        f"- current recovery matrix rows: `{len(matrix)}`",
        "",
        "## Status Counts",
        "",
    ]
    for status, count in by_status.most_common():
        md_lines.append(f"- `{status}`: `{count}`")
    md_lines.extend(
        [
            "",
            "## Finding",
            "",
            "The current recovery matrix can be internally closed while the full raw desktop source scope is still not fully proved.",
            "The existing 2026-05-24 full-source audit is explicitly first/second-mock scoped (`47` suites).",
            "The raw desktop source tree also contains midterm/final suites. These must be either brought into the coverage system or explicitly excluded by a user-approved scope rule before whole-goal completion can be claimed.",
            "",
            "## Missing Or Out-Of-Scope Raw Suites",
            "",
            "| suite | stage | status | next action |",
            "|---|---|---|---|",
        ]
    )
    for r in missing:
        md_lines.append(
            f"| {r['raw_suite']} | {r['stage_dir']} | {r['current_status']} | {r['blocker_or_next_action']} |"
        )
    md_lines.extend(
        [
            "",
            "## Next Work Queue",
            "",
            "1. Confirm whether the final benchmark scope is all raw stage folders or only first/second mocks. Until this is formally closed on disk, do not claim whole-project final acceptance.",
            "2. If midterm/final suites are in scope, create source bundles and per-question disposition rows for the `18` midterm/final suites before any final external review.",
            "3. If midterm/final suites are out of scope, write an explicit scope-exclusion ledger with source paths and rationale, then re-run this audit.",
            "",
            "## Evidence Files",
            "",
            f"- CSV detail: `{OUT_CSV.name}`",
            f"- current first/second mock audit: `{SOURCE_AUDIT}`",
            f"- current recovery matrix: `{MATRIX}`",
        ]
    )
    OUT_MD.write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    print(f"wrote {OUT_CSV}")
    print(f"wrote {OUT_MD}")
    print(f"raw={len(out_rows)} first_second={by_bucket['first_mock'] + by_bucket['second_mock']} midterm_final={by_bucket['midterm_or_final']} missing={len(missing)} missing_midterm={len(missing_midterm)} missing_other={len(missing_other)}")


if __name__ == "__main__":
    main()
