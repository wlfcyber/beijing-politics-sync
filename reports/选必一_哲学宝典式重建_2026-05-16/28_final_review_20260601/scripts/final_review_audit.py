#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

from docx import Document


RUN = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/28_final_review_20260601")
PREV_RUN = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531")
DEFAULT_DOCX = Path("/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终极版_20260531.docx")
DOCX = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_DOCX
CARD_INDEX = PREV_RUN / "02_source_cards" / "RAW_CARD_INDEX.csv"
OUT_DIR = RUN / "01_audit"
TAG = sys.argv[2] if len(sys.argv) > 2 else ("FINAL_REVIEW" if DOCX == DEFAULT_DOCX else "REVISED_FINAL_REVIEW")
ENTRY_CSV = OUT_DIR / f"{TAG}_ENTRY_AUDIT.csv"
FLAG_CSV = OUT_DIR / f"{TAG}_FLAGS.csv"
SOURCE_CSV = OUT_DIR / f"{TAG}_SOURCE_PATHS.csv"
SUMMARY_MD = OUT_DIR / f"{TAG}_AUDIT_SUMMARY.md"

MODULES = {"时代背景", "理论", "经济全球化", "政治多极化", "中国", "联合国"}
ENTRY_RE = re.compile(r"^(\d+)\.\s+(.+?Q\d+(?:\(\d+\))?)(.*)$")
LABEL_RE = re.compile(r"^(20\d{2})(.+?)(一模|二模|期中|期末)Q(\d+)(?:\((\d+)\))?")
FIELD_RE = re.compile(r"^【([^】]+)】\s*(.*)$")
SOURCE_PATH_RE = re.compile(r"^###\s+FOUND[^｜]*｜(.+)$")
VALID_SAMEGROUP_MODULES = MODULES
FORBIDDEN_STUDENT = [
    "细则依据", "细则位置", "证据层级", "源文件", "/Users/", "【得分层次】",
    "【判别标注】", "【术语家族】", "【使用标注】", "【双要素判别规则】",
    "采分点", "要落到", "先写", "要写", "答题时", "后台", "设问要求",
    "细则要求", "本题需要", "v7", "材料中", "【飞哥说】", "235 条", "104 术语", "Claude",
]
FORBIDDEN_ANSWER = ["设问", "细则", "采分点", "要落到", "本题需要", "v7", "后台"]
FORBIDDEN_THINK = ["材料明确写到", "先写", "要写", "落到", "v7", "细则要求", "关键词最稳", "后台"]


def compact(s: str) -> str:
    s = s or ""
    s = re.sub(r"\s+", "", s)
    return re.sub(r"[，。；：、（）()《》“”\"'？?！!·,.；:：\[\]【】\-_—/]", "", s)


def best_chunk_hit(needle: str, haystack: str):
    n = compact(needle)
    h = compact(haystack)
    if not n:
        return "EMPTY"
    if n in h:
        return "EXACT"
    chunks = []
    for size in (28, 22, 16, 12):
        for i in range(0, max(0, len(n) - size + 1), max(1, size // 2)):
            chunk = n[i:i + size]
            if len(chunk) >= 12:
                chunks.append(chunk)
    hits = [c for c in chunks if c in h]
    if len(set(hits)) >= 2 or (hits and len(n) < 28):
        return "PARTIAL"
    return "NO_MATCH"


def make_card_id(label: str):
    label = label.replace("思政", "")
    m = LABEL_RE.search(label)
    if not m:
        return ""
    year, district, exam_type, q_no, q_sub = m.groups()
    return f"{year}_{district}_{exam_type}_Q{q_no}{'_' + q_sub if q_sub else ''}"


def load_cards():
    rows = list(csv.DictReader(CARD_INDEX.open(encoding="utf-8-sig")))
    cards = {}
    for r in rows:
        card_id = r["card_id"].lstrip("\ufeff")
        cards[card_id] = r
    return cards


def parse_docx():
    doc = Document(str(DOCX))
    entries = []
    core_headings = set()
    current_module = ""
    current_subsection = ""
    current_core = ""
    cur = None
    full_text_lines = []

    def finish():
        nonlocal cur
        if not cur:
            return
        cur["body"] = "\n".join(cur.pop("body_lines")).strip()
        entries.append(cur)
        cur = None

    for para_idx, paragraph in enumerate(doc.paragraphs, start=1):
        text = paragraph.text.strip()
        if not text:
            continue
        full_text_lines.append(text)
        if paragraph.style.name == "Heading 1" and text in MODULES:
            finish()
            current_module = text
            current_subsection = ""
            current_core = ""
            continue
        if paragraph.style.name == "Heading 2":
            finish()
            current_subsection = text
            current_core = ""
            continue
        if text.startswith("核心答题点："):
            finish()
            current_core = text.removeprefix("核心答题点：").strip()
            core_headings.add(current_core)
            continue
        m_entry = ENTRY_RE.match(text)
        if m_entry:
            finish()
            ordinal, source_label, tail = m_entry.groups()
            cur = {
                "paragraph": para_idx,
                "module": current_module,
                "subsection": current_subsection,
                "core_point": current_core,
                "ordinal": ordinal,
                "source_label": source_label.strip(),
                "title_tail": tail.strip(),
                "card_id": make_card_id(source_label.strip()),
                "samegroup_lines": [],
                "body_lines": [text],
            }
            continue
        m_field = FIELD_RE.match(text)
        if cur and m_field:
            key, value = m_field.groups()
            cur[key] = value.strip()
            cur["body_lines"].append(text)
            continue
        if cur:
            if text.startswith("· "):
                cur["samegroup_lines"].append(text)
            else:
                cur["body_lines"].append(text)
    finish()
    return entries, "\n".join(full_text_lines), core_headings


def parse_source_paths(card_text):
    paths = []
    for line in card_text.splitlines():
        m = SOURCE_PATH_RE.match(line.strip())
        if m:
            paths.append(m.group(1).strip())
    return paths


def audit():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cards = load_cards()
    entries, full_text, core_headings = parse_docx()
    all_core_points = core_headings | {e["core_point"] for e in entries if e.get("core_point")}
    source_rows = []
    audited = []
    seq_expected = defaultdict(lambda: 1)

    for e in entries:
        flags = []
        card = cards.get(e["card_id"], {})
        card_path = Path(card.get("card_path", "")) if card.get("card_path") else None
        card_text = card_path.read_text(encoding="utf-8") if card_path and card_path.exists() else ""
        prompt_check = best_chunk_hit(e.get("设问", ""), card_text)
        answer_check = best_chunk_hit(e.get("答案落点", ""), card_text)
        think_check = "PRESENT" if e.get("为什么能想到", "").strip() else "EMPTY"
        samegroup_check = "OK"

        if not e.get("module") or e["module"] not in MODULES:
            flags.append("BAD_MODULE")
        if not e.get("core_point"):
            flags.append("MISSING_CORE")
        if not e.get("card_id"):
            flags.append("CARD_ID_PARSE_FAIL")
        if not card:
            flags.append("CARD_NOT_FOUND")
        elif card.get("status") != "RAW_CARD_READY":
            flags.append("CARD_NOT_READY")
        if not card_path or not card_path.exists():
            flags.append("CARD_PATH_MISSING")
        if not e.get("设问", "").strip():
            flags.append("MISSING_PROMPT")
        elif prompt_check == "NO_MATCH":
            flags.append("PROMPT_NOT_IN_CARD")
        if not e.get("答案落点", "").strip():
            flags.append("MISSING_ANSWER")
        if not e.get("材料触发点", "").strip():
            flags.append("MISSING_TRIGGER")
        if think_check == "EMPTY":
            flags.append("MISSING_WHY")
        if any(x in e.get("答案落点", "") for x in FORBIDDEN_ANSWER):
            flags.append("ANSWER_BACKSTAGE_WORD")
        if any(x in (e.get("材料触发点", "") + e.get("为什么能想到", "")) for x in FORBIDDEN_THINK):
            flags.append("THINK_BACKSTAGE_WORD")
        seq_key = (e.get("module"), e.get("subsection"), e.get("core_point"))
        expected = seq_expected[seq_key]
        if int(e["ordinal"]) != expected:
            flags.append(f"BAD_SEQUENCE_EXPECT_{expected}")
            seq_expected[seq_key] = int(e["ordinal"]) + 1
        else:
            seq_expected[seq_key] += 1

        for line in e["samegroup_lines"]:
            m = re.match(r"^·\s*([^：:]+)[：:](.*)$", line)
            if not m:
                flags.append("SAMEGROUP_BAD_FORMAT")
                samegroup_check = "BAD_FORMAT"
                continue
            mod = m.group(1).strip()
            items = [x.strip() for x in re.split(r"[；;]", m.group(2)) if x.strip()]
            if mod not in VALID_SAMEGROUP_MODULES:
                flags.append(f"SAMEGROUP_BAD_MODULE:{mod}")
                samegroup_check = "BAD_MODULE"
            for item in items:
                if item and item not in all_core_points and item not in {"（本题8分）", "（本题10分）", "（本题5分）"}:
                    # This is a soft flag: same-group phrases may be condensed, but exact misses need review.
                    flags.append("SAMEGROUP_ITEM_NOT_CORE")
                    samegroup_check = "ITEM_NOT_CORE"
                    break

        for path_text in parse_source_paths(card_text):
            p = Path(path_text)
            source_rows.append({
                "card_id": e["card_id"],
                "source_label": e["source_label"],
                "source_path": path_text,
                "exists": "YES" if p.exists() else "NO",
                "is_desktop": "YES" if path_text.startswith("/Users/wanglifei/Desktop/") else "NO",
            })
            if not p.exists():
                flags.append("SOURCE_PATH_MISSING")

        audited.append({
            **e,
            "evidence_status": card.get("status", "NO_CARD"),
            "card_path": str(card_path) if card_path else "",
            "prompt_check": prompt_check,
            "answer_check": answer_check,
            "think_check": think_check,
            "samegroup_check": samegroup_check,
            "qa_flags": ";".join(sorted(set(flags))),
        })

    fieldnames = [
        "paragraph", "module", "subsection", "core_point", "ordinal", "source_label", "title_tail",
        "card_id", "evidence_status", "card_path", "材料触发点", "设问", "为什么能想到",
        "答案落点", "同题组", "prompt_check", "answer_check", "think_check", "samegroup_check",
        "qa_flags",
    ]
    with ENTRY_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(audited)
    flagged = [r for r in audited if r["qa_flags"]]
    with FLAG_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(flagged)
    with SOURCE_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        fieldnames2 = ["card_id", "source_label", "source_path", "exists", "is_desktop"]
        writer = csv.DictWriter(f, fieldnames=fieldnames2)
        writer.writeheader()
        writer.writerows(source_rows)

    forbidden_counts = {x: full_text.count(x) for x in FORBIDDEN_STUDENT}
    flag_counter = Counter()
    for r in flagged:
        for flag in r["qa_flags"].split(";"):
            if flag:
                flag_counter[flag.split(":", 1)[0]] += 1
    source_counter = Counter((r["exists"], r["is_desktop"]) for r in source_rows)
    md = [
        "# FINAL_REVIEW_AUDIT_SUMMARY",
        "",
        f"- DOCX: `{DOCX}`",
        f"- Parsed entries: {len(audited)}",
        f"- Unique card IDs: {len({r['card_id'] for r in audited})}",
        f"- Flagged entries: {len(flagged)}",
        f"- Flag types: {dict(flag_counter)}",
        f"- Prompt check: {dict(Counter(r['prompt_check'] for r in audited))}",
        f"- Answer text check: {dict(Counter(r['answer_check'] for r in audited))}",
        f"- Samegroup check: {dict(Counter(r['samegroup_check'] for r in audited))}",
        f"- Source path existence/Desktop: {dict(source_counter)}",
        "",
        "## Forbidden Residue",
        "",
        *[f"- `{k}`: {v}" for k, v in forbidden_counts.items()],
        "",
        "## Flag Examples",
        "",
    ]
    if not flagged:
        md.append("- No flags.")
    else:
        for row in flagged[:80]:
            md.append(f"- {row['source_label']} | {row['core_point']} | {row['qa_flags']}")
    SUMMARY_MD.write_text("\n".join(md) + "\n", encoding="utf-8")
    print("entries", len(audited))
    print("flagged", len(flagged))
    print("flags", dict(flag_counter))
    print("summary", SUMMARY_MD)


if __name__ == "__main__":
    audit()
