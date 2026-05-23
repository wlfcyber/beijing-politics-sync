from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document


RUN = Path(__file__).resolve().parents[1]
REPO = RUN.parents[1]
CACHE = Path.home() / "Desktop" / "beijing_politics_research" / "data" / "preprocessed_corpus"
DOCX = next((Path.home() / "Desktop").glob("*2026二模补题版.docx"))
V3_INVENTORY = REPO / "reports" / "philosophy_v3_reaudit_2026-04-26" / "artifacts" / "framework_entry_inventory.csv"
SECOND_MOCK_JSON = REPO / "reports" / "bixiu4_philosophy_accepted_base_second_mock_patch_2026-05-23" / "04_fusion" / "fused_entries_2026_second_mock.json"

DISTRICTS = "海淀|西城|东城|朝阳|丰台|石景山|门头沟|房山|顺义|延庆|昌平|通州"
STAGES = "一模|二模|期中|期末|上期中|上期末"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, object]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def norm_stage(text: str) -> str:
    text = text or ""
    if "一模" in text:
        return "一模"
    if "二模" in text:
        return "二模"
    if "期中" in text:
        return "期中"
    if "期末" in text:
        return "期末"
    return text.strip()


def extract_suite_question(text: str) -> tuple[str, str, str, str]:
    year = ""
    district = ""
    stage = ""
    q = ""
    m = re.search(r"(20\d{2})", text)
    if m:
        year = m.group(1)
    m = re.search(DISTRICTS, text)
    if m:
        district = m.group(0)
    m = re.search(STAGES, text)
    if m:
        stage = norm_stage(m.group(0))
    m = re.search(r"第\s*(\d+)\s*[（(]?\s*([123456一二三四五六])?\s*[）)]?\s*题", text)
    if not m:
        m = re.search(r"第\s*(\d+)\s*题\s*第?\s*[（(]\s*([123456一二三四五六])\s*[）)]", text)
    if m:
        q = m.group(1)
        if len(m.groups()) >= 2 and m.group(2):
            q = f"{q}({m.group(2)})"
    return year, district, stage, q


def base_q(q: str) -> str:
    m = re.search(r"\d+", q or "")
    return m.group(0) if m else ""


def suite_key(year: str, district: str, stage: str, q: str | None = None) -> tuple[str, str, str, str]:
    return (year or "", district or "", norm_stage(stage or ""), base_q(q or ""))


def extract_handbook_entries() -> tuple[list[dict[str, object]], set[tuple[str, str, str, str]], str]:
    doc = Document(str(DOCX))
    rows: list[dict[str, object]] = []
    text_parts = []
    for i, p in enumerate(doc.paragraphs):
        t = p.text.strip()
        if not t:
            continue
        text_parts.append(t)
        style = p.style.name if p.style else ""
        if style == "Heading 3":
            y, d, s, q = extract_suite_question(t)
            rows.append(
                {
                    "paragraph_index": i,
                    "title": t,
                    "year": y,
                    "district": d,
                    "stage": s,
                    "question": q,
                    "base_question": base_q(q),
                    "key": "|".join(suite_key(y, d, s, q)),
                }
            )
    keys = {suite_key(str(r["year"]), str(r["district"]), str(r["stage"]), str(r["question"])) for r in rows}
    return rows, keys, "\n".join(text_parts)


def inventory_rows(handbook_keys: set[tuple[str, str, str, str]]) -> list[dict[str, object]]:
    rows = []
    for r in read_csv(V3_INVENTORY):
        grade = r.get("evidence_grade_initial", "")
        nature = r.get("question_nature", "")
        if not ((nature == "subjective" and grade in {"A", "B"}) or (nature == "choice" and grade == "C")):
            continue
        y, d, s, q = r.get("year", ""), r.get("district", ""), norm_stage(r.get("stage", "")), base_q(r.get("question", ""))
        key = suite_key(y, d, s, q)
        rows.append(
            {
                **r,
                "norm_year": y,
                "norm_district": d,
                "norm_stage": s,
                "norm_question": q,
                "norm_key": "|".join(key),
                "covered_by_latest_docx": key in handbook_keys,
            }
        )
    return rows


def second_mock_rows(handbook_keys: set[tuple[str, str, str, str]]) -> list[dict[str, object]]:
    if not SECOND_MOCK_JSON.exists():
        return []
    data = json.loads(SECOND_MOCK_JSON.read_text(encoding="utf-8"))
    rows = []
    for item in data:
        y, d, s, q = extract_suite_question(item.get("source", ""))
        key = suite_key(y, d, s, q)
        rows.append(
            {
                "source": item.get("source", ""),
                "section": item.get("section", ""),
                "kind": item.get("kind", ""),
                "norm_key": "|".join(key),
                "covered_by_latest_docx": key in handbook_keys,
            }
        )
    return rows


def source_keyword_scan() -> list[dict[str, object]]:
    keywords = [
        "主要矛盾",
        "次要矛盾",
        "主次矛盾",
        "矛盾的主要方面",
        "矛盾主要方面",
        "矛盾的次要方面",
        "主流",
        "支流",
        "两点论",
        "重点论",
    ]
    roots = []
    if (CACHE / "texts").exists():
        roots.extend((CACHE / "texts").glob("*.txt"))
    second_text_root = REPO / "reports" / "bixiu4_philosophy_accepted_base_second_mock_patch_2026-05-23" / "01_source_texts"
    if second_text_root.exists():
        roots.extend(second_text_root.glob("*.txt"))

    rows: list[dict[str, object]] = []
    for p in roots:
        try:
            text = p.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        hits = [kw for kw in keywords if kw in text]
        if not hits:
            continue
        lines = text.splitlines()
        for i, line in enumerate(lines):
            line_hits = [kw for kw in keywords if kw in line]
            if not line_hits:
                continue
            ctx = " / ".join(lines[max(0, i - 1) : min(len(lines), i + 2)])
            y, d, s, q = extract_suite_question(p.name + " " + ctx)
            rows.append(
                {
                    "source_text": str(p),
                    "filename": p.name,
                    "line_no": i + 1,
                    "hits": ";".join(line_hits),
                    "context": re.sub(r"\s+", " ", ctx)[:500],
                    "norm_key_guess": "|".join(suite_key(y, d, s, q)),
                }
            )
    return rows


def main() -> None:
    hb_rows, hb_keys, hb_text = extract_handbook_entries()
    inv_rows = inventory_rows(hb_keys)
    second_rows = second_mock_rows(hb_keys)
    kw_rows = source_keyword_scan()

    out = RUN / "01_codex_lane"
    write_csv(out / "latest_handbook_entry_index.csv", hb_rows, ["paragraph_index", "title", "year", "district", "stage", "question", "base_question", "key"])
    write_csv(
        out / "v3_inventory_vs_latest_docx.csv",
        inv_rows,
        [
            "audit_id",
            "source",
            "norm_year",
            "norm_district",
            "norm_stage",
            "norm_question",
            "question_nature",
            "evidence_grade_initial",
            "covered_by_latest_docx",
            "section",
            "material",
            "trigger",
            "logic",
            "bundle_path",
            "norm_key",
        ],
    )
    write_csv(out / "second_mock_vs_latest_docx.csv", second_rows, ["source", "section", "kind", "norm_key", "covered_by_latest_docx"])
    write_csv(out / "high_risk_contradiction_keyword_scan.csv", kw_rows, ["source_text", "filename", "line_no", "hits", "context", "norm_key_guess"])

    missing_subj = [r for r in inv_rows if r["question_nature"] == "subjective" and not r["covered_by_latest_docx"]]
    missing_choice = [r for r in inv_rows if r["question_nature"] == "choice" and not r["covered_by_latest_docx"]]
    key_counter = Counter((r["norm_year"], r["norm_district"], r["norm_stage"]) for r in inv_rows)
    missing_counter = Counter((r["norm_year"], r["norm_district"], r["norm_stage"]) for r in missing_subj + missing_choice)
    principle_counts = {
        "主要矛盾": hb_text.count("主要矛盾"),
        "次要矛盾": hb_text.count("次要矛盾"),
        "矛盾的主要方面": hb_text.count("矛盾的主要方面") + hb_text.count("矛盾主要方面"),
        "矛盾的次要方面": hb_text.count("矛盾的次要方面"),
        "主流": hb_text.count("主流"),
        "支流": hb_text.count("支流"),
        "两点论": hb_text.count("两点论"),
        "重点论": hb_text.count("重点论"),
    }

    suite_rows = []
    for key, total in sorted(key_counter.items()):
        suite_rows.append(
            {
                "suite": "".join(key),
                "candidate_rows": total,
                "missing_candidate_rows": missing_counter[key],
                "status": "HAS_POSSIBLE_GAP" if missing_counter[key] else "COVERED_BY_LATEST_DOCX_KEYS",
            }
        )
    write_csv(out / "suite_gap_summary.csv", suite_rows, ["suite", "candidate_rows", "missing_candidate_rows", "status"])

    report = [
        "# Codex 全覆盖扫描报告",
        "",
        f"- 最新宝典：{DOCX}",
        f"- 最新宝典 Heading 3 条目数：{len(hb_rows)}",
        f"- V3 库中纳入扫描的哲学候选：{len(inv_rows)}",
        f"- 其中主观 A/B 候选未被最新宝典套卷题号覆盖：{len(missing_subj)}",
        f"- 其中选择 C 候选未被最新宝典套卷题号覆盖：{len(missing_choice)}",
        f"- 高风险矛盾关键词源文本命中行：{len(kw_rows)}",
        "",
        "## 最新宝典中重点原理词频",
    ]
    for k, v in principle_counts.items():
        report.append(f"- {k}: {v}")
    report.extend(["", "## 缺口最多的套卷", ""])
    for (y, d, s), count in missing_counter.most_common(20):
        report.append(f"- {y}{d}{s}: {count}")
    report.append("")
    report.append("## 直接结论")
    report.append("")
    report.append("最新宝典虽然已经有主次矛盾和矛盾主次方面词条内容，但没有独立二级节点；需要补两个独立节点，且用高风险词扫描中的正式证据题落库。")
    (out / "CODEX_FULL_COVERAGE_SCAN_REPORT.md").write_text("\n".join(report), encoding="utf-8")
    print("\n".join(report))


if __name__ == "__main__":
    main()
