#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import csv
import re
from pathlib import Path


RUN = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531")
MATCH = RUN / "01_inputs" / "QUESTION_SOURCE_MATCH.csv"
TEXT_MANIFEST = RUN / "01_inputs" / "FINAL_SOURCE_TEXT_MANIFEST.csv"
SEED_AUDIT = Path("/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/25_claude_philosophy_aligned_source_audit_20260531/02_audit/AUTOMATED_AUDIT.csv")
OUT_DIR = RUN / "02_source_cards" / "raw_cards"
INDEX = RUN / "02_source_cards" / "RAW_CARD_INDEX.csv"
MANUAL_TEXT_OVERRIDES = {
    "/Users/wanglifei/Desktop/2024模拟题/2024海淀期中/试卷/试卷.pdf": RUN / "01_inputs" / "manual_ocr" / "试卷.ocr.txt",
    "/Users/wanglifei/Desktop/2026模拟题/2026各区二模/2026海淀二模/细则/26海淀高三政治二模讲评.pdf": RUN / "01_inputs" / "manual_ocr" / "26海淀高三政治二模讲评.ocr.txt",
}


def split_paths(value):
    return [p.strip() for p in (value or "").split(" || ") if p.strip()]


def load_text_map():
    rows = list(csv.DictReader(TEXT_MANIFEST.open(encoding="utf-8-sig")))
    text_map = {r["path"]: r for r in rows}
    for source_path, override_path in MANUAL_TEXT_OVERRIDES.items():
        if source_path in text_map and override_path.exists():
            text_map[source_path] = dict(text_map[source_path])
            text_map[source_path]["final_text_path"] = str(override_path)
            text_map[source_path]["manual_override"] = "YES"
    return text_map


def load_seed_hints():
    rows = list(csv.DictReader(SEED_AUDIT.open(encoding="utf-8-sig")))
    hints = {}
    for row in rows:
        key = (row["year"], row["district"], row["exam_type"], row["q_no"], row["q_sub"])
        item = hints.setdefault(key, {"prompts": set(), "scores": set(), "surfaces": set()})
        if row.get("prompt"):
            item["prompts"].add(row["prompt"])
        if row.get("score_layers"):
            item["scores"].add(row["score_layers"])
        if row.get("surface_sentence"):
            item["surfaces"].add(row["surface_sentence"])
    return hints


def normalize(text):
    return (text or "").replace("\r", "\n")


def patterns_for(q_no, q_sub):
    base = re.escape(q_no)
    full = re.escape(str(q_no).translate(str.maketrans("0123456789", "０１２３４５６７８９")))
    bases = [base]
    if full != base:
        bases.append(full)
    q = fr"(?<![0-9０-９])(?:{'|'.join(bases)})(?![0-9０-９])"
    pats = []
    if q_sub:
        sub = re.escape(q_sub)
        full_sub = re.escape(str(q_sub).translate(str.maketrans("0123456789", "０１２３４５６７８９")))
        subs = [sub]
        if full_sub != sub:
            subs.append(full_sub)
        s = fr"(?:{'|'.join(subs)})"
        pats.extend([
            fr"{q}\s*[\(（]\s*{s}\s*[)）]",
        ])
    pats.extend([
        fr"(?m)(^|\n)\s*{q}\s*[．\.\、􀆰]",
        fr"(?m)(^|\n)\s*第\s*{q}\s*题",
        fr"{q}\s*[．\.\、􀆰]",
        fr"第\s*{q}\s*题",
        fr"{q}\s*[\(（]",
    ])
    return [re.compile(p) for p in pats]


def chunks(value):
    value = re.sub(r"\s+", "", value or "")
    value = re.sub(r"[，。；：、（）()《》“”\"'？?！!]", "", value)
    out = []
    for size in [18, 14, 10, 8]:
        for i in range(0, max(0, len(value) - size + 1), max(1, size // 2)):
            part = value[i:i + size]
            if len(part) == size:
                out.append(part)
    return out


def find_by_hints(text, hints):
    compact = re.sub(r"\s+", "", text)
    for hint in hints:
        for chunk in chunks(hint):
            pos = compact.find(chunk)
            if pos >= 0:
                # Approximate compact index back in normal text by searching chunk's first half.
                needle = chunk[: max(4, len(chunk) // 2)]
                normal_pos = re.sub(r"\s+", "", text[:pos]).__len__()
                m = re.search(re.escape(needle), re.sub(r"\s+", "", text))
                return max(0, pos - 500)
    return -1


def snippet(text, q_no, q_sub, radius=1800, path="", hints=None):
    text = normalize(text)
    for pat in patterns_for(q_no, q_sub):
        m = pat.search(text)
        if m:
            pos = m.start()
            start = max(0, pos - 300)
            end = min(len(text), pos + radius)
            return text[start:end].strip(), "FOUND"
    hint_pos = find_by_hints(text, hints or [])
    if hint_pos >= 0:
        start = max(0, hint_pos - 300)
        end = min(len(text), hint_pos + radius)
        return text[start:end].strip(), "FOUND_BY_HINT"
    name = Path(path).name if path else ""
    if q_no and (f"{q_no}题" in name or f"{q_no}." in name or f"{q_no}（" in name or f"{q_no}(" in name):
        return text[:radius].strip(), "FOUND_BY_FILENAME"
    return "", "NOT_FOUND"


def make_id(row):
    sub = f"_{row['q_sub']}" if row["q_sub"] else ""
    return f"{row['year']}_{row['district']}_{row['exam_type']}_Q{row['q_no']}{sub}"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    text_map = load_text_map()
    seed_hints = load_seed_hints()
    rows = list(csv.DictReader(MATCH.open(encoding="utf-8-sig")))
    out_rows = []
    for row in rows:
        card_id = make_id(row)
        if row["match_status"] != "READY_FOR_CARD":
            out_rows.append({
                "card_id": card_id,
                "status": "BLOCKED_SOURCE_GAP",
                "paper_found": "NO",
                "rubric_found": "NO",
                "card_path": "",
                "note": row["match_status"],
            })
            continue
        paper_blocks = []
        rubric_blocks = []
        paper_found = False
        rubric_found = False
        key = (row["year"], row["district"], row["exam_type"], row["q_no"], row["q_sub"])
        hints = seed_hints.get(key, {"prompts": set(), "scores": set(), "surfaces": set()})
        for p in split_paths(row["matched_papers"]):
            info = text_map.get(p)
            if not info:
                continue
            text = Path(info["final_text_path"]).read_text(encoding="utf-8")
            snip, status = snippet(text, row["q_no"], row["q_sub"], radius=2600, path=p, hints=hints["prompts"])
            paper_found = paper_found or status.startswith("FOUND")
            paper_blocks.append((p, status, snip))
        for p in split_paths(row["matched_rubrics"]):
            info = text_map.get(p)
            if not info:
                continue
            text = Path(info["final_text_path"]).read_text(encoding="utf-8")
            rubric_hints = list(hints["scores"]) + list(hints["surfaces"]) + list(hints["prompts"])
            snip, status = snippet(text, row["q_no"], row["q_sub"], radius=2200, path=p, hints=rubric_hints)
            rubric_found = rubric_found or status.startswith("FOUND")
            rubric_blocks.append((p, status, snip))
        status = "RAW_CARD_READY" if paper_found and rubric_found else "RAW_CARD_NEEDS_MANUAL_LOCATE"
        card_path = OUT_DIR / f"{card_id}.md"
        lines = [
            f"# {card_id}",
            "",
            f"- source_labels: {row['source_labels']}",
            f"- entry_count_from_seed: {row['entry_count']}",
            f"- raw_status: {status}",
            "",
            "## 原卷片段",
            "",
        ]
        for path, found, snip in paper_blocks:
            lines.extend([f"### {found}｜{path}", "", "```text", snip or "[未自动定位题号片段]", "```", ""])
        lines.extend(["## 细则片段", ""])
        for path, found, snip in rubric_blocks:
            lines.extend([f"### {found}｜{path}", "", "```text", snip or "[未自动定位题号片段]", "```", ""])
        card_path.write_text("\n".join(lines), encoding="utf-8")
        out_rows.append({
            "card_id": card_id,
            "status": status,
            "paper_found": "YES" if paper_found else "NO",
            "rubric_found": "YES" if rubric_found else "NO",
            "card_path": str(card_path),
            "note": "",
        })
    with INDEX.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        w.writeheader()
        w.writerows(out_rows)
    print("cards", len(out_rows))
    print("ready", sum(1 for r in out_rows if r["status"] == "RAW_CARD_READY"))
    print("needs_manual", sum(1 for r in out_rows if r["status"] == "RAW_CARD_NEEDS_MANUAL_LOCATE"))
    print("blocked", sum(1 for r in out_rows if r["status"] == "BLOCKED_SOURCE_GAP"))


if __name__ == "__main__":
    main()
