#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync")
RUN_DIR = ROOT / "reports/philosophy_v3_reaudit_2026-04-26"
FRAMEWORK = RUN_DIR / "freeze/必修四哲学材料-知识触发总框架_持续更新版_v2.md"
BUNDLE_DIR = ROOT / "data/preprocessed_corpus/gpt_suite_bundles"
OUT_DIR = RUN_DIR / "artifacts"


DISTRICTS = [
    "东城",
    "西城",
    "朝阳",
    "海淀",
    "丰台",
    "石景山",
    "门头沟",
    "房山",
    "通州",
    "顺义",
    "昌平",
    "延庆",
    "跨区",
]
STAGES = ["一模", "二模", "期中", "期末"]
D_MARKERS = [
    "reference-only",
    "非逐点评分细则",
    "参考答案",
    "答案及评分参考",
    "教师版参考答案",
    "等级描述",
    "答题方向参考",
    "方向参考",
]
A_MARKERS = [
    "正式阅卷细则",
    "阅卷细则",
    "评分细则",
    "答案细则",
    "评分标准",
    "阅卷总结",
    "阅卷报告",
    "评标细则",
    "本题标准和变通",
    "评分细则、答案变通说明",
]
B_MARKERS = ["评标.pptx", "评标PPT", "讲评PPT", "讲评 PPT", "评标 PPT", "PPTX", "pptx"]


def clean_cell(cell: str) -> str:
    return re.sub(r"\s+", " ", cell.replace("`", "")).strip()


def split_md_row(line: str) -> list[str]:
    parts = [clean_cell(p) for p in line.strip().strip("|").split("|")]
    return parts


def current_source_context(lines: list[str], idx: int) -> str:
    context = []
    for j in range(idx, min(idx + 6, len(lines))):
        context.append(lines[j].strip())
    return "\n".join(context)


def parse_labeled_entries(lines: list[str]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    i = 0
    heading = ""
    while i < len(lines):
        line = lines[i]
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
        m = re.match(r"^\s*\d+\.\s+\*\*来源\*\*：(.+?)\s*$", line)
        if not m:
            i += 1
            continue

        source = clean_cell(m.group(1))
        material = trigger = logic = ""
        start_line = i + 1
        j = i + 1
        while j < len(lines):
            nxt = lines[j]
            if re.match(r"^\s*\d+\.\s+\*\*来源\*\*：", nxt) or nxt.startswith("#### ") or nxt.startswith("### ") or nxt.startswith("## "):
                break
            mat = re.match(r"^\s*-\s*材料信息：(.+)", nxt)
            tri = re.match(r"^\s*-\s*触发知识：(.+)", nxt)
            log = re.match(r"^\s*-\s*逻辑链：(.+)", nxt)
            if mat:
                material = clean_cell(mat.group(1))
            elif tri:
                trigger = clean_cell(tri.group(1))
            elif log:
                logic = clean_cell(log.group(1))
            j += 1
        entries.append(
            {
                "entry_type": "label4",
                "source": source,
                "material": material,
                "trigger": trigger,
                "logic": logic,
                "section": heading,
                "line": str(start_line),
            }
        )
        i = j
    return entries


def parse_table_entries(lines: list[str]) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    heading = ""
    in_table = False
    col_count = 0
    for idx, line in enumerate(lines):
        if line.startswith("#"):
            heading = line.lstrip("#").strip()
        if line.startswith("| 来源 |") and "逻辑链" in line:
            in_table = True
            col_count = len(split_md_row(line))
            continue
        if in_table and re.match(r"^\|\s*-", line):
            continue
        if in_table and not line.startswith("|"):
            in_table = False
            continue
        if not in_table or not line.startswith("|"):
            continue
        cols = split_md_row(line)
        if len(cols) < 4 or cols[0] == "来源" or not re.search(r"20\d{2}", cols[0]) or "第" not in cols[0]:
            continue
        source, material, trigger, logic = cols[:4]
        if not source or not material or not trigger or not logic:
            continue
        entries.append(
            {
                "entry_type": "table",
                "source": source,
                "material": material,
                "trigger": trigger,
                "logic": logic,
                "section": heading,
                "line": str(idx + 1),
                "table_cols": str(col_count),
            }
        )
    return entries


def extract_year(text: str) -> str:
    m = re.search(r"(20\d{2})", text)
    return m.group(1) if m else ""


def extract_district(text: str) -> str:
    for d in DISTRICTS:
        if d in text:
            return d
    return ""


def extract_stage(text: str) -> str:
    for s in STAGES:
        if s in text:
            return s
    if "高三（上）" in text or "高三上" in text:
        return "期末"
    return ""


def extract_question(text: str) -> tuple[str, int | None]:
    m = re.search(r"第\s*([0-9]{1,2})\s*题(?:第?（?([0-9一二三四五六七八九十]+)）?问|（([0-9一二三四五六七八九十]+)）)?", text)
    if not m:
        return "", None
    q = f"第{m.group(1)}题"
    if m.group(2):
        q += f"第（{m.group(2)}）问"
    elif m.group(3):
        q += f"（{m.group(3)}）"
    return q, int(m.group(1))


def nature_from_qnum(qnum: int | None) -> str:
    if qnum is None:
        return "unknown"
    return "choice" if qnum <= 15 else "subjective"


def grade_entry(entry: dict[str, str], qnum: int | None) -> tuple[str, str]:
    text = "\n".join([entry.get("source", ""), entry.get("material", ""), entry.get("trigger", ""), entry.get("logic", ""), entry.get("section", "")])
    if qnum is not None and qnum <= 15:
        return "C", "选择题正确项触发或选择题链，需答案表+题面支持"
    if any(marker in text for marker in D_MARKERS):
        return "D", "reference-only/答案及评分参考/参考答案/等级描述风险"
    if any(marker in text for marker in A_MARKERS):
        return "A", "细则/阅卷/评分标准类显性来源"
    if any(marker in text for marker in B_MARKERS) or re.search(r"可从.+角度|角度作答|允许从", text):
        return "B", "评标或讲评角度清单，材料链需标整理者解释"
    if "用户确认" in text:
        return "B", "用户确认可用来源，但仍需回源标注证据层级"
    return "E", "未由启发式识别出可靠证据等级"


def bundle_index() -> list[tuple[str, Path]]:
    if not BUNDLE_DIR.exists():
        return []
    return [(p.name, p) for p in sorted(BUNDLE_DIR.glob("*.md"))]


def find_bundle(year: str, district: str, stage: str, bundles: list[tuple[str, Path]]) -> tuple[str, str]:
    if not year or not district:
        return "", "missing-year-or-district"
    exact_suite = f"{year}{district}{stage}" if stage else ""
    if exact_suite:
        exact_candidates = []
        for name, path in bundles:
            suite_label = name.rsplit("__", 1)[-1]
            if exact_suite in suite_label:
                exact_candidates.append(path)
        if exact_candidates:
            if len(exact_candidates) > 1:
                return str(exact_candidates[0].relative_to(ROOT)), f"multiple:{len(exact_candidates)}"
            return str(exact_candidates[0].relative_to(ROOT)), "found"
    candidates = []
    for name, path in bundles:
        if year in name and district in name and (not stage or stage in name):
            candidates.append(path)
    if not candidates:
        for name, path in bundles:
            if year in name and district in name:
                candidates.append(path)
    if not candidates:
        return "", "not-found"
    if len(candidates) > 1:
        return str(candidates[0].relative_to(ROOT)), f"multiple:{len(candidates)}"
    return str(candidates[0].relative_to(ROOT)), "found"


def keyword_hits(entry: dict[str, str], bundle_path: str) -> tuple[str, str]:
    if not bundle_path:
        return "0", ""
    path = ROOT / bundle_path
    if not path.exists():
        return "0", ""
    text = path.read_text(encoding="utf-8", errors="ignore")
    raw_terms = re.split(r"[/；;、，, ]+", entry.get("trigger", ""))
    terms = []
    for term in raw_terms:
        term = clean_cell(term)
        if len(term) >= 2 and term not in {"观点", "角度", "方法", "文化", "哲学", "正确项"}:
            terms.append(term)
    hits = []
    for term in terms[:12]:
        if term and term in text:
            hits.append(term)
    return str(len(hits)), ";".join(hits[:8])


def review_status(grade: str, bundle_state: str, nature: str) -> str:
    if bundle_state in {"not-found", "missing-year-or-district"}:
        return "source-not-mapped"
    if grade == "E":
        return "needs-source-proof"
    if grade == "D":
        return "downgrade-or-boundary-review"
    if grade == "B":
        return "angle-list-review"
    if grade == "C":
        return "choice-answer-review"
    if grade == "A":
        return "rubric-source-review"
    return "needs-review"


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def main() -> None:
    lines = FRAMEWORK.read_text(encoding="utf-8").splitlines()
    bundles = bundle_index()
    entries = parse_labeled_entries(lines) + parse_table_entries(lines)
    rows: list[dict[str, str]] = []
    for idx, entry in enumerate(entries, 1):
        source = entry["source"]
        year = extract_year(source)
        district = extract_district(source)
        stage = extract_stage(source)
        question, qnum = extract_question(source)
        nature = nature_from_qnum(qnum)
        grade, grade_reason = grade_entry(entry, qnum)
        bundle_path, bundle_state = find_bundle(year, district, stage, bundles)
        hit_count, hit_terms = keyword_hits(entry, bundle_path)
        status = review_status(grade, bundle_state, nature)
        rows.append(
            {
                "audit_id": f"V3-FW-{idx:04d}",
                "line": entry.get("line", ""),
                "entry_type": entry.get("entry_type", ""),
                "section": entry.get("section", ""),
                "source": source,
                "year": year,
                "district": district,
                "stage": stage,
                "question": question,
                "question_nature": nature,
                "material": entry.get("material", ""),
                "trigger": entry.get("trigger", ""),
                "logic": entry.get("logic", ""),
                "evidence_grade_initial": grade,
                "grade_reason": grade_reason,
                "bundle_path": bundle_path,
                "bundle_state": bundle_state,
                "trigger_hit_count_in_bundle": hit_count,
                "trigger_hit_terms_in_bundle": hit_terms,
                "review_status": status,
            }
        )

    fields = [
        "audit_id",
        "line",
        "entry_type",
        "section",
        "source",
        "year",
        "district",
        "stage",
        "question",
        "question_nature",
        "evidence_grade_initial",
        "grade_reason",
        "bundle_path",
        "bundle_state",
        "trigger_hit_count_in_bundle",
        "trigger_hit_terms_in_bundle",
        "review_status",
        "material",
        "trigger",
        "logic",
    ]
    write_csv(OUT_DIR / "framework_entry_inventory.csv", rows, fields)

    grade_counts = Counter(row["evidence_grade_initial"] for row in rows)
    status_counts = Counter(row["review_status"] for row in rows)
    type_counts = Counter(row["entry_type"] for row in rows)
    nature_counts = Counter(row["question_nature"] for row in rows)
    district_counts = Counter(row["district"] or "未识别" for row in rows)
    source_counts = defaultdict(int)
    for row in rows:
        source_counts[(row["year"], row["district"], row["stage"], row["source"])] += 1
    high_risk = [row for row in rows if row["review_status"] in {"source-not-mapped", "needs-source-proof", "downgrade-or-boundary-review", "angle-list-review"}]

    md_lines = [
        "# v3 框架触发条目 inventory 摘要",
        "",
        f"- 总条目数：{len(rows)}",
        f"- 四行体例条目：{type_counts.get('label4', 0)}",
        f"- 表格体例条目：{type_counts.get('table', 0)}",
        "",
        "## 按证据等级初判",
        "",
    ]
    for key in ["A", "B", "C", "D", "E"]:
        md_lines.append(f"- {key}: {grade_counts.get(key, 0)}")
    md_lines.extend(["", "## 按复核状态", ""])
    for key, value in sorted(status_counts.items()):
        md_lines.append(f"- {key}: {value}")
    md_lines.extend(["", "## 按题型", ""])
    for key, value in sorted(nature_counts.items()):
        md_lines.append(f"- {key}: {value}")
    md_lines.extend(["", "## 按区县", ""])
    for key, value in sorted(district_counts.items()):
        md_lines.append(f"- {key}: {value}")
    md_lines.extend(["", "## 高风险条目前 80 条", ""])
    md_lines.append("| audit_id | line | grade | status | source | trigger | reason |")
    md_lines.append("|---|---:|---|---|---|---|---|")
    for row in high_risk[:80]:
        md_lines.append(
            "| {audit_id} | {line} | {evidence_grade_initial} | {review_status} | {source} | {trigger} | {grade_reason} |".format(
                **{k: str(v).replace("|", "／") for k, v in row.items()}
            )
        )
    (OUT_DIR / "framework_entry_inventory.md").write_text("\n".join(md_lines) + "\n", encoding="utf-8")

    source_rows = []
    for (year, district, stage, source), count in sorted(source_counts.items()):
        probe = next(row for row in rows if row["source"] == source)
        source_rows.append(
            {
                "source_key": f"{year}-{district}-{stage}-{source}",
                "year": year,
                "district": district,
                "stage": stage,
                "source": source,
                "entry_count": str(count),
                "bundle_path": probe["bundle_path"],
                "bundle_state": probe["bundle_state"],
                "max_risk_grade": max((row["evidence_grade_initial"] for row in rows if row["source"] == source), default=""),
                "review_statuses": ";".join(sorted(set(row["review_status"] for row in rows if row["source"] == source))),
            }
        )
    write_csv(
        OUT_DIR / "source_review_matrix.csv",
        source_rows,
        ["source_key", "year", "district", "stage", "source", "entry_count", "bundle_path", "bundle_state", "max_risk_grade", "review_statuses"],
    )

    source_summary = [
        "# v3 来源复核矩阵摘要",
        "",
        f"- 不同来源键数量：{len(source_rows)}",
        f"- 已映射到 cache bundle：{sum(1 for r in source_rows if r['bundle_path'])}",
        f"- 未映射来源：{sum(1 for r in source_rows if not r['bundle_path'])}",
        "",
        "## 未映射来源",
        "",
        "| source | count | status |",
        "|---|---:|---|",
    ]
    for row in source_rows:
        if not row["bundle_path"]:
            source_summary.append(f"| {row['source']} | {row['entry_count']} | {row['review_statuses']} |")
    source_summary.extend(["", "## 需优先人工复核来源", "", "| source | count | statuses | bundle |", "|---|---:|---|---|"])
    for row in source_rows:
        if any(x in row["review_statuses"] for x in ["source-not-mapped", "needs-source-proof", "downgrade-or-boundary-review", "angle-list-review"]):
            source_summary.append(f"| {row['source']} | {row['entry_count']} | {row['review_statuses']} | {row['bundle_path']} |")
    (OUT_DIR / "source_review_summary.md").write_text("\n".join(source_summary) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
