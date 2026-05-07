import csv
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
FUSION = RUN / "fusion" / "framework_first_fusion"
BASE = RUN / "codex_lane" / "QUESTION_COVERAGE_MATRIX.csv"
MANIFEST = FUSION / "RECHECK_MANIFEST.csv"
OUT = FUSION / "RECHECK_MANIFEST_ENRICHED.csv"


def main():
    with BASE.open("r", encoding="utf-8-sig", newline="") as f:
        base_rows = list(csv.DictReader(f))
    base_by_qid = {row["question_id"]: row for row in base_rows}
    suite_source = {}
    for row in base_rows:
        if row.get("suite_id") and row.get("source_id"):
            suite_source.setdefault(row["suite_id"], row["source_id"])
    suite_stable_prefix = {}
    for row in base_rows:
        stable = row.get("stable_locator", "")
        if row.get("suite_id") and stable and "::" in stable:
            suite_stable_prefix.setdefault(row["suite_id"], stable.split("::", 1)[0])

    def resolve_parent(qid):
        if qid in base_by_qid:
            return qid
        current = qid
        while "-" in current:
            current = current.rsplit("-", 1)[0]
            if current in base_by_qid:
                return current
        return qid

    with MANIFEST.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
        old_fields = f.readline if False else None

    fields = [
        "priority",
        "question_id",
        "parent_question_id",
        "source_batch",
        "type",
        "framework_node",
        "evidence_level",
        "source",
        "source_id",
        "stable_locator",
        "base_decision_reason",
        "recheck_reason",
    ]
    enriched = []
    for row in rows:
        parent_qid = resolve_parent(row["question_id"])
        base = base_by_qid.get(parent_qid, {})
        node = row.get("framework_node", "")
        qid = row.get("question_id", "")
        priority = "P2"
        if row.get("evidence_level") == "A-formal":
            priority = "P1"
        if any(marker in qid + node for marker in ["顺义一模-19", "通州期末-11", "通州期末-19", "东城期末-17", "东城期末-18", "丰台一模-18", "朝阳二模-19"]):
            priority = "P0"
        source_id = base.get("source_id", "") or suite_source.get(base.get("suite_id", ""), "")
        stable_locator = base.get("stable_locator", "")
        if not stable_locator and suite_stable_prefix.get(base.get("suite_id", "")):
            stable_locator = f"{suite_stable_prefix[base.get('suite_id', '')]}::Q{base.get('original_qno', '')}"
        enriched.append(
            {
                "priority": priority,
                **row,
                "parent_question_id": parent_qid,
                "source_id": source_id,
                "stable_locator": stable_locator,
                "base_decision_reason": base.get("decision_reason", ""),
            }
        )

    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(sorted(enriched, key=lambda r: (r["priority"], r["source_batch"], r["question_id"], r["framework_node"])))

    counts = {}
    for row in enriched:
        counts[row["priority"]] = counts.get(row["priority"], 0) + 1
    print({"rows": len(enriched), "priority_counts": counts, "output": str(OUT)})


if __name__ == "__main__":
    main()
