# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import json
import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET


def u(s: str) -> str:
    return s.encode("ascii").decode("unicode_escape")


REPO = Path(__file__).resolve().parents[3]
RUN = Path(__file__).resolve().parents[1]
DESKTOP = Path.home() / "Desktop"

YI_MOCK = u(r"\u4e00\u6a21")
ER_MOCK = u(r"\u4e8c\u6a21")
ROOTS = [
    ("2024", DESKTOP / ("2024" + u(r"\u5404\u533a\u6a21\u62df\u9898"))),
    ("2025", DESKTOP / ("2025" + u(r"\u5404\u533a\u6a21\u62df\u9898"))),
    ("2026", DESKTOP / ("2026" + u(r"\u5404\u533a\u6a21\u62df\u9898"))),
]

PAPER_TERMS = [u(r"\u8bd5\u5377"), u(r"\u8bd5\u9898"), u(r"\u6559\u5e08\u7248"), u(r"\u5b66\u751f\u7248")]
RUBRIC_TERMS = [u(r"\u7ec6\u5219"), u(r"\u8bc4\u6807"), u(r"\u9605\u5377"), u(r"\u8bc4\u5206"), u(r"\u8bb2\u8bc4")]
ANSWER_TERMS = [u(r"\u7b54\u6848"), u(r"\u53c2\u8003")]
NOISE_TERMS = [u(r"\u653f\u6cbb"), u(r"\u601d\u653f"), u(r"\u9ad8\u4e09"), u(r"\u5317\u4eac")]


def write_csv(path: Path, rows: list[dict], fieldnames: list[str] | None = None) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if fieldnames is None:
        keys = []
        for row in rows:
            for key in row.keys():
                if key not in keys:
                    keys.append(key)
        fieldnames = keys
    with path.open("w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def docx_text(path: Path) -> str:
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    chunks: list[str] = []
    with zipfile.ZipFile(path) as zf:
        root = ET.fromstring(zf.read("word/document.xml"))
        for para in root.findall(".//w:p", ns):
            text = "".join(t.text or "" for t in para.findall(".//w:t", ns))
            if text:
                chunks.append(text)
    return "\n".join(chunks)


def accepted_base_paths() -> tuple[Path | None, Path | None]:
    base_dir = REPO / "reports" / "bixiu4_philosophy_accepted_base_second_mock_patch_2026-05-23" / "accepted_base"
    docx = next(base_dir.glob("*.docx"), None) if base_dir.exists() else None
    pdf = next(base_dir.glob("*.pdf"), None) if base_dir.exists() else None
    return docx, pdf


def discover_suites() -> list[dict]:
    suites: list[dict] = []
    for year, root in ROOTS:
        if not root.exists():
            suites.append({
                "suite": f"{year}_ROOT_MISSING",
                "year": year,
                "phase": "root_missing",
                "source_dir": str(root),
                "status": "root_missing",
            })
            continue
        wanted_phases = [YI_MOCK] + ([ER_MOCK] if year == "2026" else [])
        for group in sorted(root.iterdir(), key=lambda x: x.name):
            if not group.is_dir():
                continue
            phase = next((x for x in wanted_phases if x in group.name), None)
            if phase is None:
                continue
            for p in sorted(group.iterdir(), key=lambda x: x.name):
                if not p.is_dir():
                    continue
                if phase not in p.name or u(r"\u5404\u533a") in p.name:
                    continue
                suites.append({
                    "suite": p.name,
                    "year": year,
                    "phase": phase,
                    "source_dir": str(p),
                    "status": "in_scope_inventory",
                })
    return suites


def category_counts(source_dir: Path) -> dict:
    files = [p for p in source_dir.rglob("*") if p.is_file()] if source_dir.exists() else []

    def has_any(path: Path, terms: list[str]) -> bool:
        name = path.name
        return any(term in name for term in terms)

    return {
        "file_count": len(files),
        "paper_files": sum(1 for p in files if has_any(p, PAPER_TERMS)),
        "rubric_files": sum(1 for p in files if has_any(p, RUBRIC_TERMS)),
        "answer_files": sum(1 for p in files if has_any(p, ANSWER_TERMS)),
        "file_list": " | ".join(str(p) for p in files[:80]),
    }


def suite_variants(name: str) -> list[str]:
    variants = {name}
    m = re.search(r"(202[456])(.+?)(" + re.escape(YI_MOCK) + "|" + re.escape(ER_MOCK) + ")", name)
    if m:
        year, district, phase = m.group(1), m.group(2), m.group(3)
        compact = district
        for t in NOISE_TERMS:
            compact = compact.replace(t, "")
        variants.update({
            year + compact + phase,
            year + district + phase,
        })
    return [v for v in variants if len(v) >= 3]


def count_base_mentions(base_text: str, suite: str) -> int:
    return sum(base_text.count(v) for v in suite_variants(suite))


def cache_hit_count(suite: str) -> int:
    cache = DESKTOP / "beijing_politics_research" / "data" / "preprocessed_corpus"
    manifest = cache / "manifest.csv"
    if not manifest.exists():
        return 0
    count = 0
    with manifest.open("r", encoding="utf-8-sig", errors="ignore", newline="") as f:
        for row in csv.DictReader(f):
            hay = " ".join(str(v) for v in row.values())
            if any(v in hay for v in suite_variants(suite)):
                count += 1
    return count


def load_second_mock_candidates() -> list[dict]:
    p = REPO / "reports" / "bixiu4_philosophy_accepted_base_second_mock_patch_2026-05-23" / "04_fusion" / "fused_entries_2026_second_mock.json"
    if not p.exists():
        return []
    data = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("entries", [])
    rows: list[dict] = []
    for i, item in enumerate(data, 1):
        if not isinstance(item, dict):
            continue
        row = {"candidate_id": f"old_2026_2mock_{i:03d}"}
        for key, value in item.items():
            if isinstance(value, (str, int, float)) or value is None:
                row[key] = value
            else:
                row[key] = json.dumps(value, ensure_ascii=False)
        rows.append(row)
    return rows


def main() -> None:
    inv_dir = RUN / "01_source_inventory"
    base_docx, base_pdf = accepted_base_paths()
    base_text = ""
    if base_docx:
        base_text = docx_text(base_docx)
        (inv_dir / "accepted_base_docx_text.txt").write_text(base_text, encoding="utf-8")

    source_rows: list[dict] = []
    coverage_rows: list[dict] = []
    for row in discover_suites():
        counts = category_counts(Path(row["source_dir"]))
        ch = cache_hit_count(row["suite"])
        source_row = {**row, **counts, "cache_hits": ch}
        source_rows.append(source_row)
        mentions = count_base_mentions(base_text, row["suite"]) if base_text else 0
        base_status = "base_mentions_found" if mentions else "base_name_not_found_needs_question_audit"
        coverage_rows.append({
            "suite": row["suite"],
            "year": row["year"],
            "phase": row["phase"],
            "source_dir": row["source_dir"],
            "file_count": counts["file_count"],
            "paper_files": counts["paper_files"],
            "rubric_files": counts["rubric_files"],
            "answer_files": counts["answer_files"],
            "cache_hits": ch,
            "accepted_base_mentions": mentions,
            "base_status": base_status,
            "next_action": "question_level_audit_required",
        })

    write_csv(inv_dir / "source_suite_inventory.csv", source_rows)
    write_csv(inv_dir / "base_coverage_by_suite.csv", coverage_rows)

    candidates = load_second_mock_candidates()
    if candidates:
        keys: list[str] = []
        for row in candidates:
            for key in row.keys():
                if key not in keys:
                    keys.append(key)
        write_csv(inv_dir / "second_mock_candidate_entries.csv", candidates, keys)

    missing_like = [r for r in coverage_rows if int(r["accepted_base_mentions"]) == 0]
    thin_like = [r for r in coverage_rows if 0 < int(r["accepted_base_mentions"]) < 3]
    summary = [
        "# 初始源清单与母版覆盖扫描",
        "",
        f"- accepted_base_docx: {base_docx}",
        f"- accepted_base_pdf: {base_pdf}",
        f"- target_suites: {len(coverage_rows)}",
        f"- base_name_not_found_needs_question_audit: {len(missing_like)}",
        f"- base_mentions_1_or_2_needs_thinness_audit: {len(thin_like)}",
        f"- old_second_mock_candidates_loaded: {len(candidates)}",
        "",
        "## 母版未直接命中套卷名的高风险清单",
    ]
    for r in missing_like:
        summary.append(f"- {r['suite']} | files={r['file_count']} | rubrics={r['rubric_files']} | cache={r['cache_hits']}")
    summary.extend(["", "## 母版命中少于 3 次的薄弱清单"])
    for r in thin_like:
        summary.append(f"- {r['suite']} | mentions={r['accepted_base_mentions']} | files={r['file_count']} | rubrics={r['rubric_files']} | cache={r['cache_hits']}")
    (inv_dir / "inventory_summary.md").write_text("\n".join(summary), encoding="utf-8")


if __name__ == "__main__":
    main()
