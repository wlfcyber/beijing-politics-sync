from __future__ import annotations

import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document


RUN = Path(__file__).resolve().parents[1]
GOV = RUN / "06_governor_confucius"
DELIVERY = RUN / "05_delivery"
OUT_CSV = GOV / "INHERITED_2024_2025_SECOND_MOCK_ROW_EXTRACT_20260524.csv"
OUT_MD = GOV / "INHERITED_2024_2025_SECOND_MOCK_ROW_EXTRACT_20260524.md"

ENTRY_RE = re.compile(r"^\s*\d+\.\s*(20[2456].+?第.+?题.+?）)\s*$")
SUITE_RE = re.compile(r"(20[2456][^第]{0,12}?二模)")
FIELD_RE = re.compile(r"^【([^】]+)】\s*(.*)$")


def final_docx() -> Path:
    return next(p for p in DELIVERY.glob("*.docx") if "backup" not in p.name)


def inherited_suites() -> list[str]:
    p = GOV / "FULL_SOURCE_VS_DOCX_COVERAGE_AUDIT_20260524.csv"
    rows = []
    with p.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            if row.get("coverage_bucket") == "DOCX_BASE_COVERED_NOT_REOPENED_THIS_DELTA":
                rows.append(row["suite"])
    return sorted(rows)


def normalize_suite(text: str, suites: list[str]) -> str | None:
    for suite in suites:
        if suite in text:
            return suite
    # Known source folder normalization.
    if "2024顺义思政二模" in text:
        return "2024顺义二模"
    return None


def is_node_heading(text: str, style_name: str) -> bool:
    if not text:
        return False
    if ENTRY_RE.match(text):
        return False
    if text.startswith("【"):
        return False
    if style_name.startswith("Heading"):
        return True
    # Many inherited handbook node headings are plain paragraphs after conversion.
    if len(text) <= 40 and not re.search(r"20[2456].*第.+题", text):
        bad = ["目录", "前言", "飞哥", "三年模拟"]
        return not any(x in text for x in bad)
    return False


def extract() -> list[dict]:
    suites = inherited_suites()
    doc = Document(str(final_docx()))
    rows: list[dict] = []
    current_node = ""
    current: dict | None = None

    def flush() -> None:
        nonlocal current
        if current:
            rows.append(current)
            current = None

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        style_name = para.style.name if para.style is not None else ""
        m = ENTRY_RE.match(text)
        suite = normalize_suite(text, suites)
        if m and suite:
            flush()
            current = {
                "suite": suite,
                "heading": text,
                "principle_node": current_node,
                "material_trigger": "",
                "question_prompt": "",
                "why_trigger": "",
                "answer_landing": "",
            }
            continue
        if m:
            flush()
            continue
        if current is None:
            if is_node_heading(text, style_name):
                current_node = text
            continue

        field = FIELD_RE.match(text)
        if field:
            label, value = field.group(1), field.group(2)
            if "材料触发点" in label:
                current["material_trigger"] = value
            elif "设问" in label:
                current["question_prompt"] = value
            elif "为什么能想到" in label:
                current["why_trigger"] = value
            elif "答案落点" in label:
                current["answer_landing"] = value
            else:
                current.setdefault("other", "")
                current["other"] += f"【{label}】{value}\n"
        else:
            # Append continuation text to the previous non-empty field.
            for key in ("answer_landing", "why_trigger", "question_prompt", "material_trigger"):
                if current.get(key):
                    current[key] += "\n" + text
                    break

    flush()
    for row in rows:
        for key in ("material_trigger", "question_prompt", "why_trigger", "answer_landing"):
            row[f"{key}_chars"] = len(row.get(key, ""))
        row["has_all_fields"] = all(row.get(k) for k in ("material_trigger", "question_prompt", "why_trigger", "answer_landing"))
    return rows


def write_outputs(rows: list[dict]) -> None:
    fields = [
        "suite",
        "heading",
        "principle_node",
        "material_trigger_chars",
        "question_prompt_chars",
        "why_trigger_chars",
        "answer_landing_chars",
        "has_all_fields",
        "material_trigger",
        "question_prompt",
        "why_trigger",
        "answer_landing",
    ]
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    by_suite = Counter(row["suite"] for row in rows)
    by_node = Counter(row["principle_node"] for row in rows)
    weak = [
        row
        for row in rows
        if not row["has_all_fields"]
        or row["material_trigger_chars"] < 30
        or row["why_trigger_chars"] < 30
        or row["answer_landing_chars"] < 30
    ]
    lines = [
        "# Inherited 2024/2025 Second-Mock Row Extract",
        "",
        f"- final_docx: `{final_docx()}`",
        f"- inherited suites: {len(inherited_suites())}",
        f"- extracted rows: {len(rows)}",
        f"- weak/missing-field rows: {len(weak)}",
        "",
        "## Rows By Suite",
        "",
    ]
    for suite, count in sorted(by_suite.items()):
        lines.append(f"- {suite}: {count}")
    lines.extend(["", "## Rows By Principle Node", ""])
    for node, count in by_node.most_common():
        lines.append(f"- {node}: {count}")
    lines.extend(["", "## Weak Or Missing Field Rows", ""])
    if weak:
        for row in weak:
            lines.append(
                f"- {row['suite']} | {row['heading']} | node={row['principle_node']} | "
                f"lens={row['material_trigger_chars']}/{row['why_trigger_chars']}/{row['answer_landing_chars']} | all_fields={row['has_all_fields']}"
            )
    else:
        lines.append("- none")
    lines.extend(["", "## Row Index", ""])
    grouped: dict[str, list[dict]] = defaultdict(list)
    for row in rows:
        grouped[row["suite"]].append(row)
    for suite in sorted(grouped):
        lines.append(f"### {suite}")
        for row in grouped[suite]:
            lines.append(f"- {row['principle_node']} | {row['heading']}")
        lines.append("")
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    rows = extract()
    write_outputs(rows)
    print(OUT_CSV)
    print(OUT_MD)
    print(f"rows={len(rows)} suites={len(set(r['suite'] for r in rows))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
