#!/usr/bin/env python3
import argparse
import csv
import re
from collections import defaultdict
from pathlib import Path


def suite_id(row):
    year = row.get("year_hint") or "unknown_year"
    district = row.get("district_hint") or "unknown_district"
    stage = row.get("stage_hint") or "unknown_stage"
    if district == "北京" and row.get("root_label"):
        district = "mixed_or_compilation"
    return f"{year}_{district}_{stage}"


def role(row):
    ev = row.get("evidence_guess", "")
    if ev.startswith("P0"):
        return "scoring"
    if ev.startswith("P1"):
        return "reference_answer"
    if ev.startswith("P2"):
        return "teaching_or_lecture"
    if ev.startswith("P3"):
        return "paper"
    return "unknown"


def append_sample(samples, text, limit=4):
    if not text:
        return
    if len(samples) < limit:
        samples.append(text)


def status_for(sid):
    if sid == "2026_石景山_期末":
        return "excluded"
    if sid == "2026_海淀_期末":
        return "no_module_user_confirmed_pending_current_check"
    if "unknown" in sid:
        return "needs_classification"
    return "not_started"


def note_for(sid):
    if sid == "2026_石景山_期末":
        return "User-confirmed no usable scoring rules; excluded for all modules unless new scoring source appears."
    if sid == "2026_海淀_期末":
        return "User-confirmed no xuanbiyi; current-run check should confirm exclusion."
    if "unknown" in sid:
        return "File-level metadata insufficient; classify manually."
    return ""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-inventory", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    rows = list(csv.DictReader(open(args.source_inventory, encoding="utf-8-sig")))
    suites = defaultdict(
        lambda: {
            "source_ids": [],
            "paper_samples": [],
            "scoring_samples": [],
            "reference_samples": [],
            "teaching_samples": [],
            "unknown_samples": [],
            "counts": defaultdict(int),
            "years": set(),
            "districts": set(),
            "stages": set(),
        }
    )

    for row in rows:
        sid = suite_id(row)
        bucket = suites[sid]
        bucket["source_ids"].append(row["source_id"])
        bucket["counts"]["total_files"] += 1
        bucket["counts"][role(row)] += 1
        bucket["years"].add(row.get("year_hint", ""))
        bucket["districts"].add(row.get("district_hint", ""))
        bucket["stages"].add(row.get("stage_hint", ""))
        rel = row.get("relative_path", "")
        r = role(row)
        if r == "paper":
            append_sample(bucket["paper_samples"], rel)
        elif r == "scoring":
            append_sample(bucket["scoring_samples"], rel)
        elif r == "reference_answer":
            append_sample(bucket["reference_samples"], rel)
        elif r == "teaching_or_lecture":
            append_sample(bucket["teaching_samples"], rel)
        else:
            append_sample(bucket["unknown_samples"], rel)

    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "suite_id",
        "status",
        "year",
        "district",
        "stage",
        "total_files",
        "paper_count",
        "scoring_count",
        "reference_answer_count",
        "teaching_or_lecture_count",
        "unknown_count",
        "paper_samples",
        "scoring_samples",
        "reference_samples",
        "teaching_samples",
        "unknown_samples",
        "notes",
    ]
    def sort_key(item):
        sid = item[0]
        m = re.match(r"(\d{4})_", sid)
        year = int(m.group(1)) if m else 9999
        priority = ["海淀", "西城", "东城", "朝阳", "丰台"]
        district_score = 99
        for idx, d in enumerate(priority):
            if f"_{d}_" in sid:
                district_score = idx
                break
        return (year, district_score, sid)

    with out.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for sid, bucket in sorted(suites.items(), key=sort_key):
            parts = sid.split("_")
            counts = bucket["counts"]
            writer.writerow(
                {
                    "suite_id": sid,
                    "status": status_for(sid),
                    "year": parts[0] if len(parts) > 0 else "",
                    "district": parts[1] if len(parts) > 1 else "",
                    "stage": parts[2] if len(parts) > 2 else "",
                    "total_files": counts["total_files"],
                    "paper_count": counts["paper"],
                    "scoring_count": counts["scoring"],
                    "reference_answer_count": counts["reference_answer"],
                    "teaching_or_lecture_count": counts["teaching_or_lecture"],
                    "unknown_count": counts["unknown"],
                    "paper_samples": " | ".join(bucket["paper_samples"]),
                    "scoring_samples": " | ".join(bucket["scoring_samples"]),
                    "reference_samples": " | ".join(bucket["reference_samples"]),
                    "teaching_samples": " | ".join(bucket["teaching_samples"]),
                    "unknown_samples": " | ".join(bucket["unknown_samples"]),
                    "notes": note_for(sid),
                }
            )

    summary = out.with_suffix(".summary.md")
    with summary.open("w", encoding="utf-8") as f:
        f.write("# Suite Inventory Summary\n\n")
        f.write(f"- suites: {len(suites)}\n")
        status_counts = defaultdict(int)
        for sid in suites:
            status_counts[status_for(sid)] += 1
        for key in sorted(status_counts):
            f.write(f"- {key}: {status_counts[key]}\n")


if __name__ == "__main__":
    main()
