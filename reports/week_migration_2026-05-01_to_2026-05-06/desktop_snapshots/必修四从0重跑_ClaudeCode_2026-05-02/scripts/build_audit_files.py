#!/usr/bin/env python3
"""从 audit/entries/*.jsonl 自动生成审计三件套：
- audit/证据索引.csv
- audit/覆盖验收表.csv
- audit/问题与边界清单.md（聚合各 entry 的 boundary_note）
"""
from __future__ import annotations

import json
import re
import csv
from pathlib import Path
from collections import defaultdict

ROOT = Path("/Users/wanglifei/Desktop/北京高考政治/必修四从0重跑_ClaudeCode_2026-05-02")
ENTRIES = ROOT / "audit" / "entries"


def load_all():
    items = []
    for f in sorted(ENTRIES.glob("*.jsonl")):
        for ln, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            line = line.strip()
            if not line:
                continue
            try:
                items.append(json.loads(line))
            except Exception as e:
                print(f"WARN bad json {f.name}:{ln} {e}")
    return items


def build_evidence_index(entries):
    out = ROOT / "audit" / "证据索引.csv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["entry_id","suite_id","question_no","sub_part","target_node",
                    "evidence_level","rubric_excerpt_short","evidence_path","boundary_note"])
        for e in entries:
            rub = (e.get("rubric_excerpt","") or "")[:200]
            bn = (e.get("boundary_note","") or "")[:300]
            w.writerow([
                e.get("entry_id",""),
                e.get("suite_id",""),
                e.get("question_no",""),
                e.get("sub_part",""),
                e.get("target_node_path",""),
                e.get("evidence_level",""),
                rub,
                e.get("evidence_path",""),
                bn,
            ])
    print(f"OK 证据索引 -> {out}（{len(entries)} 行）")


def build_coverage_matrix(entries):
    """生成 root COVERAGE_MATRIX.csv，并同步生成 audit/覆盖验收表.csv 汇总。"""
    suites = defaultdict(lambda: {
        "philosophy_main_in_student": 0,
        "philosophy_choice_in_student": 0,
        "objective_main": set(),  # main subjective question numbers as set
    })
    for e in entries:
        sid = e.get("suite_id","")
        if not sid:
            continue
        qno = e.get("question_no","")
        qtype = e.get("question_type","subjective")
        if qtype in {"objective","choice"}:
            suites[sid]["philosophy_choice_in_student"] += 1
        else:
            suites[sid]["philosophy_main_in_student"] += 1
            suites[sid]["objective_main"].add(qno)

    # 也读 source_ledger 中的所有 suite_id
    ledger = ROOT / "SOURCE_LEDGER.csv"
    all_suites = []
    with open(ledger, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            all_suites.append(row["suite_id"])

    by_suite = defaultdict(list)
    for e in entries:
        by_suite[e.get("suite_id", "")].append(e)

    root_out = ROOT / "COVERAGE_MATRIX.csv"
    with open(root_out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["suite_id","question_no","question_type","is_philosophy",
                    "evidence_level","status","target_node","brief"])
        for sid in all_suites:
            rows = by_suite.get(sid, [])
            if rows:
                for e in sorted(rows, key=lambda x: (str(x.get("question_no","")), str(x.get("sub_part","")), str(x.get("entry_id","")))):
                    qtype = e.get("question_type", "")
                    status = "objective-key-only" if qtype in {"objective", "choice"} else "included"
                    w.writerow([
                        sid,
                        (str(e.get("question_no","")) + str(e.get("sub_part","") or "")),
                        qtype,
                        "yes",
                        e.get("evidence_level",""),
                        status,
                        e.get("target_node_path",""),
                        (e.get("entry_id","") or "")[:120],
                    ])
            else:
                status = "excluded-by-skill-rule" if sid == "2026_石景山_期末" else "module-boundary-excluded"
                if not (ENTRIES / f"{sid}.jsonl").exists():
                    status = "source-missing"
                w.writerow([sid, "", "suite_boundary", "no", "", status, "", "无进入学生版条目；详见套卷报告或边界清单"])
    print(f"OK COVERAGE_MATRIX -> {root_out}")

    out = ROOT / "audit" / "覆盖验收表.csv"
    with open(out, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["suite_id","哲学主观题数(同题多原理记1)","主观入学生条目数",
                    "选择入学生条目数","module-boundary-excluded","状态"])
        for sid in all_suites:
            d = suites.get(sid, {"philosophy_main_in_student":0,"philosophy_choice_in_student":0,"objective_main":set()})
            main_q = len(d["objective_main"])
            main_in = d["philosophy_main_in_student"]
            obj_in = d["philosophy_choice_in_student"]
            state = "included" if (main_in + obj_in) > 0 else "module-boundary-excluded"
            if sid == "2026_石景山_期末":
                state = "excluded-by-skill-rule"
            w.writerow([sid, main_q, main_in, obj_in, "", state])
    print(f"OK 覆盖验收表 -> {out}（{len(all_suites)} 行）")


def build_boundary_notes(entries):
    """聚合 boundary_note，按 suite 输出问题/边界清单。"""
    out = ROOT / "audit" / "问题与边界清单.md"
    by_suite = defaultdict(list)
    for e in entries:
        bn = e.get("boundary_note","")
        if not bn:
            continue
        sid = e.get("suite_id","")
        eid = e.get("entry_id","")
        by_suite[sid].append((eid, bn))

    lines = ["# 问题与边界清单（按套卷聚合）", ""]
    for sid in sorted(by_suite.keys()):
        lines.append(f"## {sid}")
        lines.append("")
        for eid, bn in by_suite[sid]:
            lines.append(f"- **{eid}**：{bn}")
        lines.append("")

    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"OK 问题与边界清单 -> {out}")


def main():
    entries = load_all()
    print(f"加载 {len(entries)} 条 entries")
    build_evidence_index(entries)
    build_coverage_matrix(entries)
    build_boundary_notes(entries)


if __name__ == "__main__":
    main()
