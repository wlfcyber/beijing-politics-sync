import csv
import json
from collections import Counter, defaultdict
from pathlib import Path


RUN = Path(__file__).resolve().parents[1]
OUT = RUN / "fusion" / "overall_batch_closure"

PRIMARY_SOURCES = [
    ("batch01_haidian_xicheng", RUN / "claudecode_lane" / "batches" / "batch01_haidian_xicheng"),
    ("batch02_chaoyang_controlled_input", RUN / "fusion" / "batch02_chaoyang_controlled_input"),
    ("batch03_dongcheng", RUN / "claudecode_lane" / "batches" / "batch03_dongcheng"),
    ("batch04_fengtai_shunyi_tongzhou", RUN / "claudecode_lane" / "batches" / "batch04_fengtai_shunyi_tongzhou"),
]

SUPPLEMENTAL_SOURCES = [
    ("batch02a_chaoyang_yimo_2024", RUN / "claudecode_lane" / "batches" / "batch02a_chaoyang_yimo_2024"),
    ("batch03a_dongcheng_qimo_2025", RUN / "claudecode_lane" / "batches" / "batch03a_dongcheng_qimo_2025"),
    ("batch04a_shunyi_yimo_2025", RUN / "claudecode_lane" / "batches" / "batch04a_shunyi_yimo_2025"),
]


def read_csv(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames or []


def jsonl_count(batch_dir):
    entries_dir = batch_dir / "entries"
    total = 0
    bad = 0
    type_counts = Counter()
    for path in entries_dir.glob("*.jsonl"):
        with path.open("r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                total += 1
                try:
                    data = json.loads(line)
                    type_counts[str(data.get("type", ""))] += 1
                except json.JSONDecodeError:
                    bad += 1
    return {"rows": total, "bad_json": bad, "type_counts": dict(type_counts)}


def suite_report_count(batch_dir):
    reports = batch_dir / "suite_reports"
    return len(list(reports.glob("*.md"))) if reports.exists() else 0


def main():
    OUT.mkdir(parents=True, exist_ok=True)

    base_rows, _ = read_csv(RUN / "codex_lane" / "QUESTION_COVERAGE_MATRIX.csv")
    base_by_qid = defaultdict(list)
    for row in base_rows:
        base_by_qid[row["question_id"]].append(row)

    merged_rows = []
    covered = defaultdict(list)
    source_stats = {}

    for source_name, batch_dir in PRIMARY_SOURCES:
        rows, fields = read_csv(batch_dir / "QUESTION_DECISIONS.csv")
        source_stats[source_name] = {
            "decision_rows": len(rows),
            "unique_question_ids": len({r["question_id"] for r in rows}),
            "decision_counts": dict(Counter(r["claudecode_decision"] for r in rows)),
            "suite_report_count": suite_report_count(batch_dir),
            "entries": jsonl_count(batch_dir),
        }
        for row in rows:
            qid = row["question_id"]
            out = dict(row)
            out["primary_source"] = source_name
            merged_rows.append(out)
            covered[qid].append((source_name, row["claudecode_decision"]))

    base_qids = set(base_by_qid)
    covered_qids = set(covered)
    missing_qids = sorted(base_qids - covered_qids)
    extra_qids = sorted(covered_qids - base_qids)
    conflicts = {
        qid: items
        for qid, items in covered.items()
        if len({decision for _, decision in items}) > 1
    }

    row_map_fields = [
        "question_id",
        "suite_id",
        "original_qno",
        "question_type",
        "base_conclusion",
        "batch_decision",
        "primary_source",
        "source_id",
        "stable_locator",
        "duplicate_or_reference",
        "base_decision_reason",
    ]
    decision_by_qid = {}
    for row in merged_rows:
        decision_by_qid[row["question_id"]] = row

    with (OUT / "CONTROL_BASE_WITH_BATCH_DECISIONS.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=row_map_fields, lineterminator="\n")
        writer.writeheader()
        for base in base_rows:
            qid = base["question_id"]
            decision = decision_by_qid.get(qid, {})
            writer.writerow(
                {
                    "question_id": qid,
                    "suite_id": base.get("suite_id", ""),
                    "original_qno": base.get("original_qno", ""),
                    "question_type": base.get("question_type", ""),
                    "base_conclusion": base.get("current_exhaustive_conclusion", ""),
                    "batch_decision": decision.get("claudecode_decision", ""),
                    "primary_source": decision.get("primary_source", ""),
                    "source_id": base.get("source_id", ""),
                    "stable_locator": base.get("stable_locator", ""),
                    "duplicate_or_reference": base.get("duplicate_or_reference", ""),
                    "base_decision_reason": base.get("decision_reason", ""),
                }
            )

    merged_fields = list(merged_rows[0].keys()) if merged_rows else []
    with (OUT / "QUESTION_DECISIONS_ALL.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=merged_fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(merged_rows)

    supplemental_stats = {}
    for source_name, batch_dir in SUPPLEMENTAL_SOURCES:
        qd = batch_dir / "QUESTION_DECISIONS.csv"
        if not qd.exists():
            continue
        rows, _ = read_csv(qd)
        supplemental_stats[source_name] = {
            "decision_rows": len(rows),
            "unique_question_ids": len({r["question_id"] for r in rows}),
            "decision_counts": dict(Counter(r["claudecode_decision"] for r in rows)),
            "suite_report_count": suite_report_count(batch_dir),
            "entries": jsonl_count(batch_dir),
            "role": "supplemental_cross_check_only",
        }

    audit = {
        "verdict": "OVERALL_BATCH_CLOSURE_OK_NOT_FINAL"
        if not missing_qids and not extra_qids and not conflicts
        else "OVERALL_BATCH_CLOSURE_FAIL",
        "base_rows": len(base_rows),
        "base_unique_question_ids": len(base_qids),
        "covered_unique_question_ids": len(covered_qids),
        "missing_unique_question_ids": missing_qids,
        "extra_unique_question_ids": extra_qids,
        "conflicts": conflicts,
        "overall_decision_counts": dict(Counter(v[0][1] for v in covered.values())),
        "source_stats": source_stats,
        "supplemental_stats": supplemental_stats,
    }

    (OUT / "OVERALL_COVERAGE_AUDIT.json").write_text(
        json.dumps(audit, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    report = [
        "# 选必三二线主批次总闭合审计",
        "",
        f"Verdict: `{audit['verdict']}`",
        "",
        "## 覆盖结论",
        "",
        f"- 控制基座行数：`{audit['base_rows']}`",
        f"- 控制基座唯一题号：`{audit['base_unique_question_ids']}`",
        f"- 主批次覆盖唯一题号：`{audit['covered_unique_question_ids']}`",
        f"- 缺失唯一题号：`{len(missing_qids)}`",
        f"- 越界唯一题号：`{len(extra_qids)}`",
        f"- 冲突裁决：`{len(conflicts)}`",
        f"- 裁决分布：`{audit['overall_decision_counts']}`",
        "",
        "## 主批次",
        "",
    ]
    for name, stats in source_stats.items():
        report.append(
            f"- `{name}`：decision rows `{stats['decision_rows']}`, "
            f"unique `{stats['unique_question_ids']}`, suite reports `{stats['suite_report_count']}`, "
            f"entries `{stats['entries']['rows']}`, decisions `{stats['decision_counts']}`"
        )
    report.extend(
        [
            "",
            "## 补充批次",
            "",
        ]
    )
    for name, stats in supplemental_stats.items():
        report.append(
            f"- `{name}`：只作交叉补充，decision rows `{stats['decision_rows']}`, "
            f"entries `{stats['entries']['rows']}`"
        )
    report.extend(
        [
            "",
            "## 闭合边界",
            "",
            "- 本报告只证明题级主批次闭合，可进入融合与回源核验。",
            "- 不授权终稿、Word 或 PDF。",
            "- 后续学生版必须按框架节点组织，不能按地区流水账展开。",
        ]
    )
    (OUT / "OVERALL_CLOSURE_REPORT.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(json.dumps(audit, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
