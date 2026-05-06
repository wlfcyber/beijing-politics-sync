#!/usr/bin/env python3
"""Enrich logic candidate hits with known source-inventory suite metadata."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


XUANBIYI_INVENTORY = Path(
    "/Users/wanglifei/Desktop/北京高考政治/"
    "选必一_当代国际政治与经济_四线终极全书_2026-05-03/01_source_inventory/SOURCE_INVENTORY.csv"
)
XUANBIER_LEDGER = Path(
    "/Users/wanglifei/Desktop/北京高考政治/"
    "选必二重做_2026-04-30/preprocess_v2_2026-05-03/SOURCE_MATCH_LEDGER_V2.csv"
)


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def hash_tokens(text: str) -> list[str]:
    tokens = re.findall(r"(?:SRC_)?([0-9a-f]{8,16})", text)
    return sorted(set(tokens), key=len, reverse=True)


def build_mapping() -> dict[str, dict[str, str]]:
    mapping: dict[str, dict[str, str]] = {}

    for row in load_csv(XUANBIYI_INVENTORY):
        searchable = " ".join(str(v) for v in row.values())
        raw_root = row.get("root_path", "") or row.get("root", "")
        rel = row.get("relative_path", "")
        original_path = f"{raw_root.rstrip('/')}/{rel}" if raw_root and rel else rel
        year = row.get("year_hint", "") or row.get("year", "")
        district = row.get("district_hint", "") or row.get("district", "")
        stage = row.get("stage_hint", "") or row.get("stage", "")
        meta = {
            "year": year,
            "district": district,
            "stage": stage,
            "suite_name": "".join(x for x in [year, district, stage] if x),
            "inventory_source_id": row.get("source_id", ""),
            "original_path": original_path,
            "source_priority": row.get("evidence_guess", "") or row.get("priority", ""),
            "source_type": row.get("file_flags", "") or row.get("suffix", ""),
            "inventory_origin": str(XUANBIYI_INVENTORY),
        }
        for token in hash_tokens(searchable):
            mapping.setdefault(token[:12], meta)
            mapping.setdefault(token[:16], meta)
        sid = row.get("source_id", "")
        if sid.startswith("SRC_"):
            token = sid[4:]
            mapping.setdefault(token[:12], meta)

    for row in load_csv(XUANBIER_LEDGER):
        searchable = " ".join(str(v) for v in row.values())
        suite_name = row.get("suite_name", "")
        meta_base = {
            "year": row.get("year", ""),
            "district": row.get("district", ""),
            "stage": row.get("stage", ""),
            "suite_name": suite_name,
            "inventory_source_id": row.get("suite_id", ""),
            "source_priority": "",
            "source_type": "",
            "inventory_origin": str(XUANBIER_LEDGER),
        }
        path_fields = [
            ("paper_files", "paper"),
            ("rubric_files", "rubric"),
            ("support_files", "support"),
        ]
        for field, kind in path_fields:
            paths = row.get(field, "")
            if not paths:
                continue
            for original in re.split(r"\n|;", paths):
                original = original.strip()
                if not original:
                    continue
                meta = dict(meta_base)
                meta["original_path"] = original
                meta["source_type"] = kind
                for token in hash_tokens(original + " " + searchable):
                    mapping.setdefault(token[:12], meta)
                    mapping.setdefault(token[:16], meta)
        for token in hash_tokens(searchable):
            meta = dict(meta_base)
            meta["original_path"] = row.get("suite_path", "")
            meta["source_type"] = "suite"
            mapping.setdefault(token[:12], meta)
            mapping.setdefault(token[:16], meta)

    return mapping


def suite_rows() -> list[dict[str, str]]:
    return load_csv(XUANBIER_LEDGER)


def parse_original_from_title(title_hint: str) -> str:
    m = re.search(r"source:\s*(.*?)\s*\|\s*status:", title_hint)
    return m.group(1).strip() if m else ""


def meta_from_original_path(original_path: str, rows: list[dict[str, str]]) -> dict[str, str]:
    if not original_path:
        return {}
    best: dict[str, str] = {}
    best_len = -1
    for row in rows:
        suite_path = row.get("suite_path", "")
        paths = "\n".join(
            [
                row.get("paper_files", ""),
                row.get("rubric_files", ""),
                row.get("support_files", ""),
                suite_path,
            ]
        )
        if original_path in paths or (suite_path and original_path.startswith(suite_path)):
            score = len(suite_path)
            if score <= best_len:
                continue
            kind = "suite"
            if original_path in row.get("paper_files", ""):
                kind = "paper"
            elif original_path in row.get("rubric_files", ""):
                kind = "rubric"
            elif original_path in row.get("support_files", ""):
                kind = "support"
            best = {
                "year": row.get("year", ""),
                "district": row.get("district", ""),
                "stage": row.get("stage", ""),
                "suite_name": row.get("suite_name", ""),
                "inventory_source_id": row.get("suite_id", ""),
                "original_path": original_path,
                "source_priority": "",
                "source_type": kind,
                "inventory_origin": str(XUANBIER_LEDGER),
            }
            best_len = score
    return best


def extract_candidate_hash(file_name: str) -> str:
    m = re.search(r"SRC_([0-9a-f]{8,16})", file_name)
    if m:
        return m.group(1)
    m = re.search(r"^([0-9a-f]{8,16})_", file_name)
    if m:
        return m.group(1)
    return ""


def infer_question_anchor(text: str) -> str:
    anchors = re.findall(r"(?:^|[^\d])([1-2]?\d)[\.．、]\s*(?:\(|（|结合|阅读|[^\d])", text)
    anchors += re.findall(r"([1-2]?\d)\s*[（(][12一二三][）)]", text)
    anchors = [a for a in anchors if a.isdigit() and 1 <= int(a) <= 21]
    if not anchors:
        return ""
    counts = Counter(anchors)
    return ",".join(a for a, _ in counts.most_common(3))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-dir", required=True)
    args = parser.parse_args()
    run_dir = Path(args.run_dir)
    src = run_dir / "01_source_inventory" / "logic_candidate_hits.csv"
    rows = load_csv(src)
    mapping = build_mapping()
    known_suites = suite_rows()

    enriched = []
    for row in rows:
        token = extract_candidate_hash(row.get("file_name", ""))
        meta = mapping.get(token[:16]) or mapping.get(token[:12]) or {}
        title_original = parse_original_from_title(row.get("title_hint", ""))
        if title_original:
            path_meta = meta_from_original_path(title_original, known_suites)
            if path_meta:
                meta = path_meta
        context = row.get("context", "")
        hit = row.get("hit_line", "")
        row2 = dict(row)
        row2.update(
            {
                "cache_hash": token,
                "source_group": row.get("source_group", ""),
                "year": meta.get("year", ""),
                "district": meta.get("district", ""),
                "stage": meta.get("stage", ""),
                "suite_name": meta.get("suite_name", ""),
                "inventory_source_id": meta.get("inventory_source_id", ""),
                "original_path": meta.get("original_path", ""),
                "source_priority": meta.get("source_priority", ""),
                "inventory_source_type": meta.get("source_type", ""),
                "inventory_origin": meta.get("inventory_origin", ""),
                "question_anchor_guess": infer_question_anchor(hit + " " + context),
                "promotion_status": "candidate_only_needs_original_source_check",
            }
        )
        enriched.append(row2)

    out = run_dir / "01_source_inventory" / "logic_candidate_hits_enriched.csv"
    fields = [
        "year",
        "district",
        "stage",
        "suite_name",
        "question_anchor_guess",
        "category",
        "topic",
        "matched_term",
        "source_status",
        "source_priority",
        "inventory_source_type",
        "inventory_source_id",
        "source_group",
        "cache_hash",
        "file_name",
        "line_no",
        "hit_line",
        "context",
        "original_path",
        "file",
        "promotion_status",
    ]
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(enriched)

    by_suite = defaultdict(Counter)
    for row in enriched:
        if row["source_group"] == "old_xuanbisan_index_only":
            continue
        suite = row.get("suite_name") or "UNKNOWN_SUITE"
        key = f"{row['category']}::{row['topic']}"
        by_suite[suite][key] += 1

    md = [
        "# 候选题套卷聚合账",
        "",
        "本文件把缓存命中聚合回套卷维度。它不是证据闭环；后续每套必须回到原试卷、答案和细则核验。",
        "",
    ]
    for suite, counter in sorted(by_suite.items()):
        md.append(f"## {suite}")
        for key, count in counter.most_common(12):
            md.append(f"- {key}: {count}")
        md.append("")
    report = run_dir / "01_source_inventory" / "candidate_suite_summary.md"
    report.write_text("\n".join(md), encoding="utf-8")

    print(
        json.dumps(
            {
                "input_rows": len(rows),
                "enriched_rows": len(enriched),
                "mapped_rows": sum(1 for r in enriched if r.get("original_path")),
                "output_csv": str(out),
                "output_report": str(report),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
