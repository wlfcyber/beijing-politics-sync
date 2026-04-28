"""V8 decode-version extraction pipeline.

Reads all 56 suite bundles named in SUITE_ROSTER.csv from the preprocessed cache,
extracts choice-question keys and main-question prompts/answers/rubrics, and emits
a single JSON intermediate that downstream scripts consume.

UTF-8 only. No reliance on prior conclusion files.
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"C:/bp_sync_visible/reports/final_56_v8_decode_claudecode_2026-04-29")
ROSTER_PATH = Path(r"C:/bp_sync_visible/reports/full_all_suites_independent_rerun_2026-04-29/SUITE_ROSTER.csv")
BUNDLE_DIR = Path(r"C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/gpt_suite_bundles")
OUT_JSON = ROOT / "audit" / "V8_DECODE_EXTRACTION.json"

CHOICE_KEY_RE = re.compile(r"(?<![0-9])([1-9]|1[0-5])\s*[．.\s]\s*([A-D])")
QUESTION_HEAD_RE = re.compile(r"(?m)^\s*(?:第\s*)?(\d{1,2})\s*[．.、]")
SUBJECTIVE_HEAD_RE = re.compile(r"(?m)^\s*(\d{1,2})\s*[．.、]\s*[(（]\s*(\d{1,2})\s*分\s*[)）]")


def load_roster() -> list[dict]:
    with open(ROSTER_PATH, "r", encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def strip_section_meta(block: str) -> str:
    """Remove the bundle's per-source metadata block, keeping only document text."""
    lines = block.splitlines()
    body: list[str] = []
    skip_meta = False
    for ln in lines:
        if ln.startswith("- source_path:") or ln.startswith("- status:") or ln.startswith("- method:") \
                or ln.startswith("- sha256:") or ln.startswith("- gpt_markdown_path:") or ln.startswith("- render_dir:"):
            continue
        body.append(ln)
    return "\n".join(body).strip()


def split_bundle(text: str) -> dict[str, str]:
    """Split a suite bundle into named sections keyed by their source path heading."""
    sections: dict[str, str] = {}
    parts = re.split(r"(?m)^---\s*$", text)
    current_name = "_header"
    for chunk in parts:
        chunk = chunk.strip()
        if not chunk:
            continue
        m = re.match(r"^##\s+(.+?)\n", chunk)
        if m:
            name = m.group(1).strip()
            body = chunk[m.end():]
            sections[name] = strip_section_meta(body)
        else:
            sections[current_name] = strip_section_meta(chunk)
    return sections


def detect_kind(name: str) -> str:
    n = name
    if "答案" in n and "细则" not in n:
        return "answer"
    if "细则" in n:
        return "rubric"
    if "试卷" in n or "试题" in n:
        return "paper"
    return "other"


def extract_choice_keys(text: str) -> dict[int, str]:
    """Find a 1..15 answer key block.

    Strategy 1: locate an anchor section (选择题/客观题/参考答案) and search the next
    1500 chars for `n．A` / `n.A` / `n A` matches.
    Strategy 2: find any consecutive run of >= 8 such matches (newlines allowed).
    Strategy 3: fall back to first 15 distinct numbered matches.
    Use the strategy that yields the most consecutive 1..15 entries with #1 present.
    """
    candidates: list[dict[int, str]] = []

    anchor_re = re.compile(r"(本部分共\s*15\s*题|选择题|客观题|参考答案|思想政治参考答案)")
    for am in anchor_re.finditer(text):
        window = text[am.end(): am.end() + 1500]
        d: dict[int, str] = {}
        for sm in re.finditer(r"(?<![0-9A-Za-z])([1-9]|1[0-5])\s*[．.、:：\s]*([A-D])(?![A-Z])", window):
            n = int(sm.group(1))
            if n not in d:
                d[n] = sm.group(2)
        if 1 in d and len(d) >= 8:
            candidates.append({k: v for k, v in d.items() if k <= 15})

    for m in re.finditer(
        r"((?:[1-9]|1[0-5])\s*[．.、:：\s]*[A-D]\s*[\s，,；;]*){8,}",
        text,
    ):
        run = m.group(0)
        d2: dict[int, str] = {}
        for sm in re.finditer(r"(?<![0-9A-Za-z])([1-9]|1[0-5])\s*[．.、:：\s]*([A-D])(?![A-Z])", run):
            n = int(sm.group(1))
            if n not in d2:
                d2[n] = sm.group(2)
        if 1 in d2 and len(d2) >= 8:
            candidates.append({k: v for k, v in d2.items() if k <= 15})

    fallback: dict[int, str] = {}
    for sm in re.finditer(r"(?<![0-9A-Za-z])([1-9]|1[0-5])\s*[．.、:：\s]*([A-D])(?![A-Z])", text):
        n = int(sm.group(1))
        if n not in fallback:
            fallback[n] = sm.group(2)
    if 1 in fallback and len(fallback) >= 10:
        candidates.append({k: v for k, v in fallback.items() if k <= 15})

    table_re = re.compile(
        r"1\s*[\s|]+2\s*[\s|]+3\s*[\s|]+4\s*[\s|]+5\s*[\s|]+6\s*[\s|]+7\s*[\s|]+8\s*[\s|]+9\s*[\s|]+10\s*[\s|]+11\s*[\s|]+12\s*[\s|]+13\s*[\s|]+14\s*[\s|]+15\s*[\s|]*\n+\s*([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])\s*[\s|]+([A-D])"
    )
    tm = table_re.search(text)
    if tm:
        d3: dict[int, str] = {i + 1: tm.group(i + 1) for i in range(15)}
        candidates.append(d3)

    vcol_re = re.compile(
        r"\n\s*1\s*\n\s*2\s*\n\s*3\s*\n\s*4\s*\n\s*5\s*\n\s*6\s*\n\s*7\s*\n\s*8\s*\n\s*9\s*\n\s*10\s*\n\s*11\s*\n\s*12\s*\n\s*13\s*\n\s*14\s*\n\s*15\s*\n[\s\S]{0,80}?\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])"
    )
    vm = vcol_re.search(text)
    if vm:
        d4: dict[int, str] = {i + 1: vm.group(i + 1) for i in range(15)}
        candidates.append(d4)

    split_re = re.compile(
        r"答案\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n[\s\S]{0,80}?答案\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])\s*\n\s*([A-D])"
    )
    sm = split_re.search(text)
    if sm:
        d5: dict[int, str] = {i + 1: sm.group(i + 1) for i in range(15)}
        candidates.append(d5)

    answer_block_re = re.compile(r"答案\s*\n((?:\s*[A-D]\s*\n){10,15})")
    abm = answer_block_re.search(text)
    if abm:
        letters = re.findall(r"[A-D]", abm.group(1))
        if len(letters) >= 10:
            d6: dict[int, str] = {i + 1: L for i, L in enumerate(letters[:15])}
            candidates.append(d6)

    if not candidates:
        return {}
    return max(candidates, key=lambda d: len(d))


_MAIN_HARD_STOP_RES = [
    re.compile(r"(?m)^高三思想政治参考答案"),
    re.compile(r"(?m)^海淀区\s*\d{4}"),
    re.compile(r"(?m)^西城区\s*\d{4}"),
    re.compile(r"(?m)^朝阳区\s*\d{4}"),
    re.compile(r"(?m)^东城区\s*\d{4}"),
    re.compile(r"(?m)^丰台区\s*\d{4}"),
    re.compile(r"(?m)^石景山区\s*\d{4}"),
    re.compile(r"(?m)^房山区\s*\d{4}"),
    re.compile(r"(?m)^门头沟区\s*\d{4}"),
    re.compile(r"(?m)^顺义区\s*\d{4}"),
    re.compile(r"(?m)^延庆区\s*\d{4}"),
    re.compile(r"(?m)^昌平区\s*\d{4}"),
    re.compile(r"(?m)^通州区\s*\d{4}"),
    re.compile(r"(?m)^本部分共\s*\d+\s*题"),
    re.compile(r"(?m)^第\s*[一二三四]\s*部分"),
    re.compile(r"(?m)^[一二三四]、\s*选择题"),
    re.compile(r"(?m)^[一二三四]、\s*非选择题"),
    re.compile(r"(?m)^一、命题说明"),
    re.compile(r"(?m)^客观题"),
    re.compile(r"PAGE\s*\\?\*?\s*MERGEFORMAT"),
    re.compile(r"(?m)^\s*\d{4}\s*年\s*\d{1,2}\s*月\s*$"),
    re.compile(r"考生务必将答案答在答题卡上"),
    re.compile(r"(?m)^\s*参考答案\s*$"),
    re.compile(r"(?m)^\s*【参考答案】"),
    re.compile(r"(?m)^\s*【命题立意】"),
    re.compile(r"(?m)^借助本题"),
    re.compile(r"(?m)^\s*1\s*[、.]\s*定[：:]"),
]


def extract_main_question(text: str, target_q: int) -> dict | None:
    """Look for a heading like '16．（7分）' or '16. (7分)' and capture the next ~2200 chars."""
    pat = re.compile(rf"(?m)(?:^|\n)\s*{target_q}\s*[．.、]\s*[（(]\s*(\d{{1,2}})\s*分\s*[)）]")
    m = pat.search(text)
    if not m:
        pat2 = re.compile(rf"(?m)(?:^|\n)\s*第?\s*{target_q}\s*[题]?\s*[．.、]")
        m = pat2.search(text)
        if not m:
            return None
        score = None
    else:
        score = int(m.group(1))
    start = m.start()
    end = min(start + 2200, len(text))
    next_m = re.search(rf"(?m)(?:^|\n)\s*{target_q + 1}\s*[．.、]", text[start + 5:])
    if next_m:
        end = min(end, start + 5 + next_m.start())
    for stop in _MAIN_HARD_STOP_RES:
        sm = stop.search(text, start + 30)
        if sm and sm.start() < end:
            end = sm.start()
    chunk = text[start:end].strip()
    return {"q": target_q, "score": score, "raw": chunk}


def extract_paper_question_prompt(paper_text: str, target_q: int) -> str:
    """Pull the paper-side prompt for a numbered subjective question."""
    if not paper_text:
        return ""
    pat = re.compile(rf"(?m)(?:^|\n)\s*{target_q}\s*[．.、]")
    m = pat.search(paper_text)
    if not m:
        return ""
    start = m.start()
    nxt = re.search(rf"(?m)(?:^|\n)\s*{target_q + 1}\s*[．.、]", paper_text[start + 5:])
    end = min(start + 3000, len(paper_text))
    if nxt:
        end = min(end, start + 5 + nxt.start())
    for stop in _MAIN_HARD_STOP_RES:
        sm = stop.search(paper_text, start + 30)
        if sm and sm.start() < end:
            end = sm.start()
    return paper_text[start:end].strip()


def parse_suite(bundle_path: Path) -> dict:
    text = bundle_path.read_text(encoding="utf-8")
    sections = split_bundle(text)
    paper_text = ""
    answer_text = ""
    rubric_text = ""
    for name, body in sections.items():
        kind = detect_kind(name)
        if kind == "paper" and len(body) > len(paper_text):
            paper_text = body
        elif kind == "answer" and len(body) > len(answer_text):
            answer_text = body
        elif kind == "rubric" and len(body) > len(rubric_text):
            rubric_text = body
        else:
            if not paper_text and "试" in name and len(body) > 1000:
                paper_text = body
            if not answer_text and "答案" in name and len(body) > 200:
                answer_text = body
            if not rubric_text and "细则" in name and len(body) > 200:
                rubric_text = body

    candidates_for_keys = [answer_text, rubric_text, paper_text, "\n".join(sections.values())]
    choice_keys: dict[int, str] = {}
    for src in candidates_for_keys:
        if not src:
            continue
        ck = extract_choice_keys(src)
        if len(ck) > len(choice_keys):
            choice_keys = ck
        if len(choice_keys) == 15:
            break

    main_qs: dict[int, dict] = {}
    for q in range(16, 22):
        ans = extract_main_question(answer_text + "\n\n" + rubric_text, q)
        prompt = extract_paper_question_prompt(paper_text, q)
        if ans or prompt:
            main_qs[q] = {
                "score": ans.get("score") if ans else None,
                "answer_block": ans["raw"] if ans else "",
                "paper_prompt": prompt,
            }
    return {
        "bundle_chars": len(text),
        "paper_chars": len(paper_text),
        "answer_chars": len(answer_text),
        "rubric_chars": len(rubric_text),
        "section_names": list(sections.keys()),
        "choice_keys": {str(k): v for k, v in sorted(choice_keys.items())},
        "main_questions": {str(k): v for k, v in main_qs.items()},
        "paper_text_excerpt_head": paper_text[:1200],
    }


def main() -> None:
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    roster = load_roster()
    out: dict = {"suites": {}}
    missing: list[str] = []
    for row in roster:
        sid = row["suite_id"]
        suite_name = row["suite_name"]
        bundle_path = Path(row["bundle_path"])
        if not bundle_path.exists():
            stem = bundle_path.name
            alt = BUNDLE_DIR / stem
            bundle_path = alt
        if not bundle_path.exists():
            missing.append(f"{sid} {suite_name}")
            out["suites"][sid] = {
                "suite_name": suite_name,
                "bundle_present": False,
                "year": row["year"],
                "stage": row["stage"],
                "district": row["district"],
            }
            continue
        parsed = parse_suite(bundle_path)
        parsed.update({
            "suite_name": suite_name,
            "bundle_present": True,
            "bundle_path": str(bundle_path),
            "year": row["year"],
            "stage": row["stage"],
            "district": row["district"],
        })
        out["suites"][sid] = parsed

    out["missing_bundles"] = missing
    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {OUT_JSON}")
    print(f"suites: {len(out['suites'])}; missing bundles: {len(missing)}")
    for m in missing:
        print("  miss:", m)


if __name__ == "__main__":
    main()
