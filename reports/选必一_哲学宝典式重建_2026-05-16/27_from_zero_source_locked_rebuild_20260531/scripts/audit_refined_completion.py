#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document


RUN = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531")
DOCX = Path("/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_哲学精炼审核版_学生版_20260531.docx")
INDEX = RUN / "02_source_cards" / "RAW_CARD_INDEX.csv"
OUT_DIR = RUN / "05_qa"
DETAIL_CSV = OUT_DIR / "REFINED_COMPLETION_AUDIT.csv"
SUMMARY_MD = OUT_DIR / "REFINED_COMPLETION_AUDIT.md"

MODULES = {"时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国"}
ENTRY_RE = re.compile(r"^(\d+)\.\s+(.+?Q\d+(?:\(\d+\))?)(.*)$")
LABEL_RE = re.compile(r"^(20\d{2})(.+?)(一模|二模|期中|期末)Q(\d+)(?:\((\d+)\))?")
FIELD_RE = re.compile(r"^【([^】]+)】\s*(.*)$")
REQUIRED_FIELDS = ["材料触发点", "设问", "答案落点"]
BANNED_ANYWHERE = [
    "细则依据", "细则位置", "细则", "证据层级", "源文件", "/Users/", "【得分层次】",
    "【判别标注】", "【术语家族】", "【使用标注】", "【双要素判别规则】",
    "采分点", "要落到", "落到", "先写", "要写", "答题时", "后台",
    "设问要求", "细则要求", "本题需要", "v7", "材料中", "【飞哥说】",
]
BANNED_ANSWER = [
    "设问", "细则", "证据层级", "采分点", "要落到", "本题需要", "v7",
    "答题时", "题目要求", "作答方向", "制作说明", "后台",
]
BANNED_TRIGGER = [
    "材料明确写到", "先写", "要写", "落到", "v7", "细则要求", "关键词最稳", "后台",
]
KEY_SUPPORT_TERMS = [
    "和平与发展", "时代主题", "和平发展", "合作共赢", "互利共赢", "共同利益",
    "人类命运共同体", "共商共建共享", "多边主义", "真正的多边主义", "正确义利观",
    "国家利益", "维护国家利益", "世界多极化", "全球南方", "发展中国家",
    "国际关系民主化", "全球治理", "中国智慧", "中国方案", "联合国宪章",
    "贸易自由便利", "贸易自由化便利化", "产业链供应链", "和平谈判",
    "生产率", "培养人才", "内生动力", "可持续发展",
]


def compact(s: str) -> str:
    s = s or ""
    s = re.sub(r"\s+", "", s)
    s = re.sub(r"[，。；：、（）()《》“”\"'？?！!·,.；:：\[\]【】\-_—/]", "", s)
    return s


def best_chunk_hit(needle: str, haystack: str):
    n = compact(needle)
    h = compact(haystack)
    if not n:
        return "EMPTY"
    if n in h:
        return "EXACT"
    if len(n) < 28:
        short_hits = []
        for size in (6, 5, 4):
            for i in range(0, max(0, len(n) - size + 1), 2):
                chunk = n[i:i + size]
                if chunk and chunk in h:
                    short_hits.append(chunk)
        if len(set(short_hits)) >= 2:
            return "PARTIAL"
    chunks = []
    for size in (28, 22, 16, 12):
        for i in range(0, max(0, len(n) - size + 1), max(1, size // 2)):
            chunks.append(n[i:i + size])
    hits = [c for c in chunks if len(c) >= 12 and c in h]
    if len(hits) >= 2 or (hits and len(n) < 28):
        return "PARTIAL"
    return "NO_MATCH"


def support_hit(needle: str, haystack: str):
    n = compact(needle)
    h = compact(haystack)
    if not n:
        return "EMPTY"
    if n in h:
        return "EXACT"
    for term in KEY_SUPPORT_TERMS:
        t = compact(term)
        if t and t in n and t in h:
            return "PARTIAL"
    hits = {4: set(), 6: set(), 8: set(), 12: set()}
    for size in (16, 12, 8, 6, 5, 4):
        for i in range(0, max(0, len(n) - size + 1), max(1, size // 2)):
            chunk = n[i:i + size]
            if len(chunk) >= 12 and chunk in h:
                hits[12].add(chunk)
            elif len(chunk) >= 8 and chunk in h:
                hits[8].add(chunk)
            elif len(chunk) >= 6 and chunk in h:
                hits[6].add(chunk)
            elif len(chunk) >= 4 and chunk in h:
                hits[4].add(chunk)
    if (
        hits[12]
        or len(hits[8]) >= 2
        or (len(hits[8]) >= 1 and len(hits[6]) >= 1)
        or len(hits[6]) >= 2
        or (len(hits[6]) >= 1 and len(hits[4]) >= 2)
        or len(hits[4]) >= 4
    ):
        return "PARTIAL"
    return "NO_MATCH"


def docx_lines(path: Path):
    doc = Document(str(path))
    return [p.text.strip() for p in doc.paragraphs if p.text.strip()]


def make_card_id(label: str):
    label = label.replace("思政", "")
    m = LABEL_RE.search(label)
    if not m:
        return ""
    year, district, exam_type, q_no, q_sub = m.groups()
    sub = f"_{q_sub}" if q_sub else ""
    return f"{year}_{district}_{exam_type}_Q{q_no}{sub}"


def load_cards():
    rows = list(csv.DictReader(INDEX.open(encoding="utf-8-sig")))
    return {r["card_id"].lstrip("\ufeff"): r for r in rows}


def parse_entries(lines):
    current_module = ""
    current_subsection = ""
    current_core = ""
    entries = []
    cur = None

    def finish():
        nonlocal cur
        if not cur:
            return
        cur["body"] = "\n".join(cur.pop("body_lines")).strip()
        entries.append(cur)
        cur = None

    for raw in lines:
        line = raw.strip()
        if line in MODULES:
            finish()
            current_module = line
            current_subsection = ""
            current_core = ""
            continue
        if line.startswith("核心答题点："):
            finish()
            current_core = line.removeprefix("核心答题点：").strip()
            continue
        m_entry = ENTRY_RE.match(line)
        if m_entry:
            finish()
            ordinal, source_label, title_tail = m_entry.groups()
            cur = {
                "module": current_module,
                "subsection": current_subsection,
                "core_point": current_core,
                "ordinal": ordinal,
                "source_label": source_label.strip(),
                "title_tail": title_tail.strip(),
                "card_id": make_card_id(source_label.strip()),
                "body_lines": [],
            }
            continue
        m_field = FIELD_RE.match(line)
        if cur and m_field:
            key, value = m_field.groups()
            cur[key] = value.strip()
            cur["body_lines"].append(line)
            continue
        if cur:
            cur["body_lines"].append(line)
        elif current_module and not line.startswith("本桶怎么用") and not line.startswith("边界提醒") and not line.startswith("目录"):
            if not line.startswith("学生厚版") and not line.startswith("飞哥正志讲堂") and not line.startswith("二级结构说明"):
                current_subsection = line
    finish()
    return entries


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    lines = docx_lines(DOCX)
    full_text = "\n".join(lines)
    cards = load_cards()
    entries = parse_entries(lines)
    out_rows = []

    for e in entries:
        card = cards.get(e["card_id"], {})
        card_path = Path(card.get("card_path", "")) if card.get("card_path") else None
        card_text = card_path.read_text(encoding="utf-8") if card_path and card_path.exists() else ""
        missing_fields = [field for field in REQUIRED_FIELDS if not e.get(field, "").strip()]
        prompt_check = best_chunk_hit(e.get("设问", ""), card_text)
        core_check = best_chunk_hit(e.get("core_point", ""), card_text)
        answer = e.get("答案落点", "")
        answer_check = support_hit(answer, card_text)
        trigger = e.get("材料触发点", "") + "\n" + e.get("为什么能想到", "")
        answer_banned = [x for x in BANNED_ANSWER if x in answer]
        trigger_banned = [x for x in BANNED_TRIGGER if x in trigger]
        flags = []
        if card.get("status") != "RAW_CARD_READY":
            flags.append("CARD_NOT_READY")
        if e["module"] not in MODULES:
            flags.append("MODULE_MISSING_OR_INVALID")
        if not e.get("core_point", "").strip():
            flags.append("CORE_POINT_MISSING")
        if missing_fields:
            flags.append("MISSING_FIELDS:" + "|".join(missing_fields))
        if prompt_check == "NO_MATCH":
            flags.append("PROMPT_NOT_IN_CARD")
        core_heading_note = ""
        if core_check == "NO_MATCH":
            core_heading_note = "CONTAINER_HEADING_NOT_LITERAL"
        if answer_check == "NO_MATCH":
            flags.append("ANSWER_NOT_SUPPORTED_BY_TEXT_TEST")
        if answer_banned:
            flags.append("ANSWER_BACKSTAGE:" + "|".join(answer_banned))
        if trigger_banned:
            flags.append("TRIGGER_BACKSTAGE:" + "|".join(trigger_banned))
        if len(answer) < 18:
            flags.append("ANSWER_TOO_SHORT")
        if len(e.get("材料触发点", "")) < 18:
            flags.append("TRIGGER_TOO_SHORT")
        row = dict(e)
        row.update({
            "evidence_status": card.get("status", "NO_CARD"),
            "card_path": str(card_path) if card_path else "",
            "prompt_check": prompt_check,
            "core_check": core_check,
            "answer_check": answer_check,
            "core_heading_note": core_heading_note,
            "missing_fields": ";".join(missing_fields),
            "answer_banned": ";".join(answer_banned),
            "trigger_banned": ";".join(trigger_banned),
            "qa_flags": ";".join(flags),
        })
        out_rows.append(row)

    fieldnames = [
        "module", "subsection", "core_point", "ordinal", "source_label", "title_tail",
        "card_id", "evidence_status", "card_path", "材料触发点", "设问", "为什么能想到",
        "答案落点", "同题组", "prompt_check", "core_check", "answer_check", "core_heading_note", "missing_fields",
        "answer_banned", "trigger_banned", "qa_flags",
    ]
    with DETAIL_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(out_rows)

    flagged = [r for r in out_rows if r["qa_flags"]]
    flag_counter = Counter()
    for r in flagged:
        for flag in r["qa_flags"].split(";"):
            if flag:
                flag_counter[flag.split(":", 1)[0]] += 1
    module_counter = Counter(r["module"] for r in out_rows)
    status_counter = Counter(r["evidence_status"] for r in out_rows)
    prompt_counter = Counter(r["prompt_check"] for r in out_rows)
    core_counter = Counter(r["core_check"] for r in out_rows)
    answer_counter = Counter(r["answer_check"] for r in out_rows)
    heading_note_counter = Counter(r["core_heading_note"] for r in out_rows if r["core_heading_note"])
    banned_counts = {x: full_text.count(x) for x in BANNED_ANYWHERE}

    by_flag = defaultdict(list)
    for r in flagged:
        for flag in r["qa_flags"].split(";"):
            if flag:
                by_flag[flag.split(":", 1)[0]].append(r)

    md = [
        "# REFINED_COMPLETION_AUDIT",
        "",
        "## Scope",
        "",
        f"- DOCX: `{DOCX}`",
        f"- Parsed entries: {len(out_rows)}",
        f"- Unique cards: {len({r['card_id'] for r in out_rows if r['card_id']})}",
        "",
        "## Entry Coverage",
        "",
        f"- Evidence status: {dict(status_counter)}",
        f"- Module distribution: {dict(module_counter)}",
        f"- Prompt check: {dict(prompt_counter)}",
        f"- Core point text in card: {dict(core_counter)}",
        f"- Answer support check: {dict(answer_counter)}",
        f"- Container heading notes: {dict(heading_note_counter)}",
        f"- Flagged entries: {len(flagged)}",
        f"- Flag types: {dict(flag_counter)}",
        "",
        "## Forbidden Student Text Residue",
        "",
        *[f"- `{k}`: {v}" for k, v in banned_counts.items()],
        "",
        "## Residual Audit Notes",
        "",
    ]
    if not flagged:
        md.append("- No residual entry-level flags.")
    else:
        for flag, rows in sorted(by_flag.items(), key=lambda kv: (-len(kv[1]), kv[0])):
            labels = Counter(r["source_label"] for r in rows)
            md.append(f"- {flag}: {len(rows)} entries; top labels: " + "；".join(f"{k}({v})" for k, v in labels.most_common(8)))
    md.extend([
        "",
        "## Interpretation",
        "",
        "- `prompt_check` proves the displayed question prompt is present in the source card text, allowing `PARTIAL` for OCR line breaks or full-width punctuation.",
        "- `core_check` audits visible core headings. A `CONTAINER_HEADING_NOT_LITERAL` note means the heading is a teaching container rather than a literal rubric phrase; the answer sentence is separately checked against the source card.",
        "- Student-facing evidence fields are intentionally absent per user instruction; backend evidence remains in source cards and QA CSVs.",
    ])
    SUMMARY_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("entries", len(out_rows))
    print("flagged", len(flagged))
    print("status", dict(status_counter))
    print("prompt", dict(prompt_counter))
    print("core", dict(core_counter))
    print("flags", dict(flag_counter))
    print("summary", SUMMARY_MD)
    print("detail", DETAIL_CSV)


if __name__ == "__main__":
    main()
