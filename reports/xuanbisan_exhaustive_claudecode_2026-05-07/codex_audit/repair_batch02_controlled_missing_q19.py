import csv
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
BASE = RUN / "codex_lane" / "QUESTION_COVERAGE_MATRIX.csv"
CONTROL = RUN / "fusion" / "batch02_chaoyang_controlled_input" / "QUESTION_DECISIONS.csv"
PATCH_NOTE = RUN / "fusion" / "batch02_chaoyang_controlled_input" / "SUPERVISOR_PATCH_CODEX_01_MISSING_Q19_BOUNDARY.md"

MISSING_QIDS = [
    "Q-2026朝阳期中-19-1",
    "Q-2026朝阳期中-19-2",
    "Q-2026朝阳期中-19-3",
]


def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f)), csv.DictReader(open(path, "r", encoding="utf-8-sig", newline="")).fieldnames


def main():
    with BASE.open("r", encoding="utf-8-sig", newline="") as f:
        base_rows = list(csv.DictReader(f))
    with CONTROL.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        fieldnames = reader.fieldnames or []

    existing = {r["question_id"] for r in rows}
    by_qid = {r["question_id"]: r for r in base_rows}
    added = []

    for qid in MISSING_QIDS:
        if qid in existing:
            continue
        src = by_qid[qid]
        rows.append(
            {
                "question_id": qid,
                "suite_id": src["suite_id"],
                "original_qno": src["original_qno"],
                "question_type": src["question_type"],
                "codex_current_decision": src["current_exhaustive_conclusion"],
                "claudecode_decision": "excluded",
                "decision_reason": (
                    "Codex overall closure patch: 534-row控制基座已裁定为"
                    f"{src['current_exhaustive_conclusion']} / {src['evidence_level']}；"
                    f"{src['decision_reason']}；不入选必三思维主链，但必须保留题级裁决。"
                ),
                "needs_codex_recheck": "no",
            }
        )
        added.append(qid)

    if added:
        with CONTROL.open("w", encoding="utf-8-sig", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)
        PATCH_NOTE.write_text(
            "# Codex Patch 01: missing Q19 boundary rows\n\n"
            "Overall 534-row closure audit found three base rows absent from "
            "`fusion/batch02_chaoyang_controlled_input/QUESTION_DECISIONS.csv`.\n\n"
            "Added as `excluded` boundary rows, without changing any ClaudeCode thick-content ledgers:\n\n"
            + "\n".join(f"- `{qid}`" for qid in added)
            + "\n\nThese rows are not body entries and do not authorize final Word/PDF.\n",
            encoding="utf-8",
        )

    print({"added": added, "final_rows": len(rows)})


if __name__ == "__main__":
    main()
