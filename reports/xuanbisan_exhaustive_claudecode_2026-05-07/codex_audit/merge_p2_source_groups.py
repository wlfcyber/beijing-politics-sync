import csv
import json
import re
from collections import Counter
from pathlib import Path


RUN_DIR = Path(__file__).resolve().parents[1]
FUSION_DIR = RUN_DIR / "fusion" / "framework_first_fusion"
MANIFEST = FUSION_DIR / "RECHECK_MANIFEST_ENRICHED.csv"
P2_DIR = RUN_DIR / "claudecode_lane" / "p2_recheck"

DECISION_FIELDS = [
    "priority",
    "question_id",
    "parent_question_id",
    "source_batch",
    "type",
    "framework_node",
    "evidence_level",
    "decision",
    "decision_reason",
    "source_evidence",
    "patch_needed",
    "can_enter_fusion",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=DECISION_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def read_jsonl(path: Path) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def source_to_prefix(source_id: str) -> str:
    match = re.match(r"(\d{3})_", source_id)
    if not match:
        raise ValueError(f"Cannot derive P2 prefix from source_id: {source_id}")
    return f"P2G{match.group(1)}"


def row_key(row: dict[str, str]) -> tuple[str, str]:
    return row["question_id"], row["framework_node"]


def main() -> None:
    manifest_rows = [row for row in read_csv(MANIFEST) if row.get("priority") == "P2"]
    if not manifest_rows:
        raise SystemExit("No P2 rows found in manifest")

    decisions_by_prefix: dict[str, dict[tuple[str, str], dict[str, str]]] = {}
    patches_by_prefix: dict[str, dict[tuple[str, str], dict[str, object]]] = {}
    qa_by_prefix: dict[str, dict[str, object]] = {}

    for source_id in sorted({row["source_id"] for row in manifest_rows}):
        prefix = source_to_prefix(source_id)
        qa_path = P2_DIR / f"{prefix}_QA.json"
        if not qa_path.exists():
            raise FileNotFoundError(qa_path)
        qa = json.loads(qa_path.read_text(encoding="utf-8"))
        if qa.get("verdict") != f"{prefix}_QA_OK_NOT_FINAL":
            raise RuntimeError(f"{prefix} is not QA OK: {qa.get('verdict')}")
        qa_by_prefix[prefix] = qa

        decision_rows = read_csv(P2_DIR / f"{prefix}_RECHECK_DECISIONS.csv")
        patch_rows = read_jsonl(P2_DIR / f"{prefix}_RECHECK_PATCHES.jsonl")
        decisions_by_prefix[prefix] = {row_key(row): row for row in decision_rows}
        patches_by_prefix[prefix] = {(str(row["question_id"]), str(row["framework_node"])): row for row in patch_rows}

    merged_decisions: list[dict[str, str]] = []
    merged_patches: list[dict[str, object]] = []
    missing: list[dict[str, str]] = []

    for manifest in manifest_rows:
        prefix = source_to_prefix(manifest["source_id"])
        key = row_key(manifest)
        decision = decisions_by_prefix[prefix].get(key)
        patch = patches_by_prefix[prefix].get(key)
        if decision is None or patch is None:
            missing.append(
                {
                    "prefix": prefix,
                    "question_id": key[0],
                    "framework_node": key[1],
                    "missing_decision": str(decision is None),
                    "missing_patch": str(patch is None),
                }
            )
            continue
        merged_decisions.append({field: decision.get(field, "") for field in DECISION_FIELDS})
        merged_patches.append(patch)

    if missing:
        raise RuntimeError(json.dumps({"missing": missing}, ensure_ascii=False, indent=2))

    write_csv(P2_DIR / "P2_RECHECK_DECISIONS.csv", merged_decisions)
    (P2_DIR / "P2_RECHECK_PATCHES.jsonl").write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in merged_patches) + "\n",
        encoding="utf-8",
    )

    evidence_parts = [
        "# P2 Source Evidence",
        "",
        "This file merges the source-group evidence after each source group passed QA.",
        "",
    ]
    for source_id in sorted({row["source_id"] for row in manifest_rows}):
        prefix = source_to_prefix(source_id)
        evidence_path = P2_DIR / f"{prefix}_SOURCE_EVIDENCE.md"
        evidence_parts.extend(
            [
                f"## {prefix} `{source_id}`",
                "",
                evidence_path.read_text(encoding="utf-8", errors="replace").strip(),
                "",
            ]
        )
    (P2_DIR / "P2_SOURCE_EVIDENCE.md").write_text("\n".join(evidence_parts).rstrip() + "\n", encoding="utf-8")

    decision_counts = Counter(row["decision"] for row in merged_decisions)
    evidence_counts = Counter(row["evidence_level"] for row in merged_decisions)
    enter_counts = Counter(row["can_enter_fusion"] for row in merged_decisions)
    qa_lines = [f"- {prefix}: `{qa['verdict']}`" for prefix, qa in sorted(qa_by_prefix.items())]

    acceptance = [
        "# P2 Recheck Acceptance",
        "",
        "Verdict: `P2_RECHECK_MERGED_READY_FOR_TOTAL_QA_NOT_FINAL`",
        "",
        f"- expected rows: `{len(manifest_rows)}`",
        f"- merged decision rows: `{len(merged_decisions)}`",
        f"- merged patch rows: `{len(merged_patches)}`",
        f"- decision counts: `{dict(decision_counts)}`",
        f"- evidence counts: `{dict(evidence_counts)}`",
        f"- can enter fusion counts: `{dict(enter_counts)}`",
        "- Word: no",
        "- PDF: no",
        "- delivery/final: no",
        "",
        "## Source Group QA",
        "",
        *qa_lines,
        "",
        "## Boundary",
        "",
        "- This is only the P2 recheck merge acceptance.",
        "- It does not authorize Word, PDF, delivery, or four-line finalization.",
    ]
    (P2_DIR / "P2_RECHECK_ACCEPTANCE.md").write_text("\n".join(acceptance) + "\n", encoding="utf-8")

    progress = [
        "# P2 Recheck Progress",
        "",
        "- status: source groups merged; total QA pending",
        f"- source groups: `{len(qa_by_prefix)}`",
        f"- rows merged: `{len(merged_decisions)}/{len(manifest_rows)}`",
        f"- decision counts: `{dict(decision_counts)}`",
        f"- evidence counts: `{dict(evidence_counts)}`",
        f"- can enter fusion counts: `{dict(enter_counts)}`",
        "- Word/PDF/delivery: no",
        "- four-line finalization: no",
    ]
    (P2_DIR / "PROGRESS.md").write_text("\n".join(progress) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "verdict": "P2_SOURCE_GROUPS_MERGED_NOT_FINAL",
                "source_groups": len(qa_by_prefix),
                "rows": len(merged_decisions),
                "decision_counts": dict(decision_counts),
                "evidence_counts": dict(evidence_counts),
                "can_enter_fusion_counts": dict(enter_counts),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
