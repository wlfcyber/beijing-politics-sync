#!/usr/bin/env python3
"""Promote CC0364 into the expansion draft after its rubric atom split."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长")
IN_CODEBOOK = ROOT / "08_codebook" / "provisional_codebook_v1_expansion_draft_20260519.csv"
IN_OPEN = ROOT / "08_codebook" / "transfer_open_container_after_expansion_20260519.csv"
OUT_CODEBOOK = ROOT / "08_codebook" / "provisional_codebook_v1_1_after_cc0364_split_20260519.csv"
OUT_MD = ROOT / "08_codebook" / "provisional_codebook_v1_1_after_cc0364_split_20260519.md"
OUT_MAP = ROOT / "08_codebook" / "codebook_v1_1_after_cc0364_split_source_evidence_map_20260519.csv"
OUT_OPEN = ROOT / "08_codebook" / "transfer_open_container_after_cc0364_split_20260519.csv"
OUT_RISKS = ROOT / "08_codebook" / "codebook_v1_1_after_cc0364_split_risks_20260519.md"

QID = "CC0364_2026_通州_期末_19_1"
PATCH_ATOMS = "|".join(f"PATCH_CC0364_R{i:02d}" for i in range(1, 8))
MATERIAL_ATOMS = "|".join(f"M_CC0364_2026_通州_期末_19_1_{i:02d}" for i in range(1, 7))


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fields: list[str], rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def append_unique(existing: str, extra: str) -> str:
    values = []
    seen = set()
    for part in (existing or "").split("|") + (extra or "").split("|"):
        value = part.strip()
        if value and value not in seen:
            values.append(value)
            seen.add(value)
    return "|".join(values)


def main() -> None:
    fields, rows = read_csv(IN_CODEBOOK)
    for row in rows:
        if row["code_id"] not in {"CODE_COWORK_004", "CODE_COWORK_006"}:
            continue
        row["supporting_question_ids"] = append_unique(row["supporting_question_ids"], QID)
        row["supporting_rubric_atom_ids"] = append_unique(row["supporting_rubric_atom_ids"], PATCH_ATOMS)
        row["supporting_material_atom_ids"] = append_unique(row["supporting_material_atom_ids"], MATERIAL_ATOMS)
        row["evidence_level_summary"] = append_unique(
            row.get("evidence_level_summary", ""),
            "CC0364 formal split atoms PATCH_CC0364_R01-R07 added after source check",
        )
        row["reason"] = append_unique(
            row.get("reason", ""),
            "cc0364_split_20260519: giant atom split into法理/事实/意义; limited support added to 004/006",
        )
        row["status"] = "provisional_expanded_after_cc0364_split"

    open_fields, open_rows = read_csv(IN_OPEN)
    updated_open_rows = []
    for row in open_rows:
        qids = [p for p in row.get("question_ids", "").split("|") if p and p != QID]
        if qids:
            row["question_ids"] = "|".join(qids)
            updated_open_rows.append(row)

    write_csv(OUT_CODEBOOK, fields, rows)
    write_csv(OUT_MAP, fields, rows)
    write_csv(OUT_OPEN, open_fields, updated_open_rows)

    md = [
        "# Provisional Codebook v1.1 After CC0364 Split",
        "",
        "This remains a provisional codebook for pressure testing, not a final framework.",
        "",
        f"- source codebook: `{IN_CODEBOOK}`",
        "- CC0364 giant rubric atom split completed and added as limited support to `CODE_COWORK_004` and `CODE_COWORK_006`.",
        "- `PATCH_CC0364_R04` is an alternative/low-score fact-analysis atom and must not be cumulated with `PATCH_CC0364_R03` as extra factual points.",
        "- `PATCH_CC0364_R06` and `PATCH_CC0364_R07` are value-tail atoms; they cannot independently support a core framework node.",
        "",
        "## Code Rows",
        "",
    ]
    for row in rows:
        qids = [p for p in row["supporting_question_ids"].split("|") if p]
        md.extend(
            [
                f"### {row['code_id']} — {row['temporary_label']}",
                "",
                f"- status: {row['status']}",
                f"- supporting_question_count: {len(qids)}",
                f"- supporting_question_ids: {row['supporting_question_ids']}",
                f"- rubric_atom_ids: {row['supporting_rubric_atom_ids']}",
                "",
            ]
        )
    OUT_MD.write_text("\n".join(md), encoding="utf-8")

    risks = [
        "# Codebook v1.1 Risks After CC0364 Split",
        "",
        "- `CC0364` is now atom-split, but it is still limited support for 004/006; do not create a new standalone 相邻关系 framework node from one atom-split case alone.",
        "- `PATCH_CC0364_R04` is explicitly non-cumulative with `PATCH_CC0364_R03`; pressure tests must not generate over-scored answers.",
        "- Value atoms `PATCH_CC0364_R06/R07` must be written after law and fact, not as empty 必修三-style opening.",
        "- v1.1 authorizes full 65-question pressure testing only; framework_v2 and final handbook remain blocked until that test passes or records patches.",
        "",
    ]
    OUT_RISKS.write_text("\n".join(risks), encoding="utf-8")

    print(f"Wrote {OUT_CODEBOOK}")
    print(f"Open rows retained: {len(updated_open_rows)}")


if __name__ == "__main__":
    main()
