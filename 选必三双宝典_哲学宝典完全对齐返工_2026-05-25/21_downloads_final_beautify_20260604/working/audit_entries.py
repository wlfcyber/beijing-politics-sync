from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

RUN = Path(__file__).resolve().parents[1]
WORK = RUN / "working"

METHODS = [
    "追求认识的客观性",
    "结果具有预见性",
    "结果具有可检验性",
    "整体性",
    "动态性",
    "分析与综合",
    "矛盾分析法",
    "量变与质变",
    "适度原则",
    "辩证否定",
    "认识发展历程",
    "特点与三新",
    "联想思维",
    "发散思维与聚合思维",
    "逆向思维",
    "超前思维",
]
CATEGORIES = ["一、科学思维", "二、辩证思维", "三、创新思维"]

METHOD_KEYWORDS = {
    "追求认识的客观性": ["客观性", "从实际出发", "客观对象", "立足实际"],
    "结果具有预见性": ["预见性", "预判", "预测", "趋势"],
    "结果具有可检验性": ["可检验", "检验", "验证"],
    "整体性": ["整体", "系统", "协同", "统筹"],
    "动态性": ["动态", "变化", "渐进", "发展过程"],
    "分析与综合": ["分析", "综合", "整合", "分别", "统一"],
    "矛盾分析法": ["矛盾", "对立统一", "全面", "优势", "劣势", "机遇", "挑战"],
    "量变与质变": ["量变", "质变", "积累", "渐进", "跃升"],
    "适度原则": ["适度", "度", "界限", "分寸"],
    "辩证否定": ["辩证否定", "扬弃", "保留", "克服"],
    "认识发展历程": ["感性具体", "思维抽象", "思维具体", "抽象"],
    "特点与三新": ["创新思维", "思路新", "方法新", "结果新", "三新", "创新"],
    "联想思维": ["联想", "迁移", "由此及彼", "联系"],
    "发散思维与聚合思维": ["发散", "聚合", "多向", "收束", "筛选"],
    "逆向思维": ["逆向", "反向", "反过来", "转换"],
    "超前思维": ["超前", "提前", "预判", "前瞻"],
}

ANSWER_BAD_PATTERNS = [
    "采分点",
    "本题需要",
    "设问要求",
    "细则要求",
    "答案写",
    "答案应",
    "卷面要",
    "要写",
    "先写",
]

STUDENT_CLEAN_RISK_PATTERNS = [
    "参考答案",
    "评标",
    "细则",
    "证据边界",
    "细则边界",
    "使用提醒",
    "讲评复练",
    "分类汇编",
    "不计正式题源",
    "缺独立",
    "推理宝典",
    "逻辑规则线",
    "终审报告",
    "本册只取",
]


EXPECTED_GROUPS = [
    ("2024东城一模18(3)", ["2024东城一模", "第18题第(3)问"], 2),
    ("2024丰台二模18(2)", ["2024丰台二模", "第18题第(2)问"], 3),
    ("2024分类汇编模拟政协", ["2024各区一模分类汇编", "模拟政协题"], 3),
    ("2024石景山一模19(3)", ["2024石景山一模", "第19题第(3)问"], 2),
    ("2025东城期末18(2)", ["2025东城期末", "第18题第(2)问"], 2),
    ("2025丰台一模18(1)", ["2025丰台一模", "第18题第(1)问"], 3),
    ("2025延庆一模18", ["2025延庆一模", "第18题"], 2),
    ("2025昌平二模19", ["2025昌平二模", "第19题"], 2),
    ("2025海淀期末18", ["2025海淀期末", "第18题"], 2),
    ("2025石景山一模19", ["2025石景山一模", "第19题"], 3),
    ("2025西城一模17", ["2025西城一模", "第17题"], 3),
    ("2025门头沟一模21(1)", ["2025门头沟一模", "第21题第(1)问"], 5),
    ("2026东城一模19(4)", ["2026东城一模", "第19题第(4)问"], 3),
    ("2026丰台二模21", ["2026丰台二模", "第21题"], 2),
    ("2026丰台期末20", ["2026丰台期末", "第20题"], 6),
    ("2026延庆一模18(2)", ["2026延庆一模", "第18题第(2)问"], 3),
    ("2026朝阳期中21(2)", ["2026朝阳期中", "第21题第(2)问"], 5),
    ("2026海淀一模17建议", ["2026海淀一模", "第17题"], 4),
    ("2026海淀二模18(1)", ["2026海淀二模", "第18题第(1)问"], 4),
    ("2026石景山一模17(2)", ["2026石景山一模", "第17题第(2)问"], 4),
    ("2026西城二模18(4)", ["2026西城二模", "第18题第(4)问"], 3),
    ("2026通州一模17(2)", ["2026通州一模", "第17题第(2)问"], 6),
    ("2026门头沟一模18(2)", ["2026门头沟一模", "第18题第(2)问"], 2),
    ("2026顺义一模19(2)", ["2026顺义一模", "第19题第(2)问"], 3),
]

PREVIOUS_GROUPS = [
    ("2025海淀二模20", ["2025海淀二模", "第20题"], 5),
    ("2026房山一模18(1)", ["2026房山一模", "第18题第(1)问"], 3),
    ("2026朝阳期中20", ["2026朝阳期中", "第20题"], 4),
]


def norm(s: str) -> str:
    return (
        s.replace("（", "(")
        .replace("）", ")")
        .replace(" ", "")
        .replace("\t", "")
        .replace("第(一)", "第(1)")
    )


def load_rows() -> list[dict]:
    with (WORK / "doc_paragraphs.tsv").open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def load_entries() -> list[dict]:
    return json.loads((WORK / "entries.json").read_text(encoding="utf-8"))


def attach_sections(entries: list[dict], rows: list[dict]) -> None:
    current_category = ""
    current_method = ""
    sections_by_p: dict[int, tuple[str, str]] = {}
    for row in rows:
        text = row["text"].strip()
        if text in CATEGORIES:
            current_category = text
            current_method = ""
        elif text in METHODS:
            current_method = text
        sections_by_p[int(row["p_index"])] = (current_category, current_method)
    for e in entries:
        category, method = sections_by_p.get(int(e["start_p"]), ("", ""))
        e["category"] = category
        e["method"] = method


def entry_text(e: dict) -> str:
    return "\n".join(e.get("raw", []))


def group_hits(entries: list[dict], includes: list[str]) -> list[dict]:
    wanted = [norm(x) for x in includes]
    hits = []
    for e in entries:
        title = norm(e["title"])
        if all(x in title for x in wanted):
            hits.append(e)
    return hits


def main() -> None:
    rows = load_rows()
    entries = load_entries()
    attach_sections(entries, rows)

    missing_core = []
    duplicate_notes = []
    answer_bad = []
    method_keyword_missing = []
    student_clean_risks = []
    hard_exclusions = []

    for e in entries:
        fields = e["fields"]
        for name in ["材料触发点", "设问", "为什么能想到", "答案落点"]:
            if not fields.get(name, "").strip():
                missing_core.append({"entry_no": e["entry_no"], "title": e["title"], "field": name})
        raw_text = entry_text(e)
        if raw_text.count("【同题说明】") > 1:
            duplicate_notes.append({"entry_no": e["entry_no"], "title": e["title"], "count": raw_text.count("【同题说明】")})
        answer = fields.get("答案落点", "")
        for pat in ANSWER_BAD_PATTERNS:
            if pat in answer:
                answer_bad.append({"entry_no": e["entry_no"], "title": e["title"], "pattern": pat, "answer": answer})
        method = e.get("method", "")
        if method in METHOD_KEYWORDS and not any(k in answer for k in METHOD_KEYWORDS[method]):
            method_keyword_missing.append({"entry_no": e["entry_no"], "title": e["title"], "method": method, "answer": answer})
        for pat in STUDENT_CLEAN_RISK_PATTERNS:
            if pat in raw_text:
                student_clean_risks.append({"entry_no": e["entry_no"], "title": e["title"], "pattern": pat})
        if "2026石景山期末" in e["title"]:
            hard_exclusions.append({"entry_no": e["entry_no"], "title": e["title"], "method": e.get("method", "")})

    group_results = []
    for label, includes, expected_count in EXPECTED_GROUPS + PREVIOUS_GROUPS:
        hits = group_hits(entries, includes)
        group_results.append(
            {
                "label": label,
                "expected_count": expected_count,
                "actual_count": len(hits),
                "all_have_note": all(bool(e["fields"].get("同题说明", "").strip()) for e in hits) if hits else False,
                "missing_note_entries": [e["entry_no"] for e in hits if not e["fields"].get("同题说明", "").strip()],
                "entry_numbers": [e["entry_no"] for e in hits],
                "methods": [e.get("method", "") for e in hits],
            }
        )

    by_category = Counter(e.get("category", "") for e in entries)
    by_method = Counter(e.get("method", "") for e in entries)
    other_labels = Counter(label for e in entries for label in [n["label"] for n in e.get("other_notes", [])])
    same_note_entries = [e for e in entries if e["fields"].get("同题说明", "").strip()]

    summary = {
        "entry_count": len(entries),
        "paragraph_count": len(rows),
        "same_question_note_count": len(same_note_entries),
        "missing_core_count": len(missing_core),
        "duplicate_same_note_count": len(duplicate_notes),
        "answer_bad_pattern_count": len(answer_bad),
        "method_keyword_missing_count": len(method_keyword_missing),
        "student_clean_risk_entry_count": len({r["entry_no"] for r in student_clean_risks}),
        "student_clean_risk_occurrence_count": len(student_clean_risks),
        "hard_exclusion_count": len(hard_exclusions),
        "by_category": dict(by_category),
        "by_method": dict(by_method),
        "other_note_labels": dict(other_labels),
    }
    audit = {
        "summary": summary,
        "group_results": group_results,
        "missing_core": missing_core,
        "duplicate_notes": duplicate_notes,
        "answer_bad": answer_bad,
        "method_keyword_missing": method_keyword_missing,
        "student_clean_risks": student_clean_risks,
        "hard_exclusions": hard_exclusions,
    }
    (WORK / "audit_results.json").write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")

    with (WORK / "same_question_group_check.csv").open("w", encoding="utf-8", newline="") as f:
        fieldnames = ["label", "expected_count", "actual_count", "all_have_note", "missing_note_entries", "entry_numbers", "methods"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(group_results)

    with (WORK / "content_issue_candidates.csv").open("w", encoding="utf-8", newline="") as f:
        fieldnames = ["kind", "entry_no", "title", "method", "pattern", "detail"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for item in hard_exclusions:
            writer.writerow({"kind": "hard_exclusion", **item, "pattern": "2026石景山期末", "detail": "Hard-rule notebook excludes this suite unless new scoring source is provided."})
        for item in answer_bad:
            writer.writerow({"kind": "answer_bad_pattern", "entry_no": item["entry_no"], "title": item["title"], "method": "", "pattern": item["pattern"], "detail": item["answer"][:220]})
        for item in method_keyword_missing:
            writer.writerow({"kind": "method_keyword_missing", "entry_no": item["entry_no"], "title": item["title"], "method": item["method"], "pattern": "", "detail": item["answer"][:220]})
        for item in student_clean_risks:
            writer.writerow({"kind": "student_clean_risk", "entry_no": item["entry_no"], "title": item["title"], "method": "", "pattern": item["pattern"], "detail": ""})

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
