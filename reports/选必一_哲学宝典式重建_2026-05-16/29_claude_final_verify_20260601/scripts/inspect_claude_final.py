#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from docx import Document


CLAUDE_DOCX = Path(
    "/Users/wanglifei/Library/Application Support/Claude/local-agent-mode-sessions/"
    "2c0a1a14-78ce-4ddc-8f72-9d4f74dbff6e/703c2d6a-ade6-4ee8-94a4-92b2abb47bf1/"
    "local_ea19f1a6-c672-4010-9aa6-235ad1631aa4/outputs/"
    "选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.docx"
)
CODEX_DOCX = Path(
    "/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终审修订版_20260601.docx"
)
RUN_DIR = Path(
    "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/"
    "选必一_哲学宝典式重建_2026-05-16/29_claude_final_verify_20260601"
)
AUDIT_DIR = RUN_DIR / "01_audit"


ENTRY_RE = re.compile(r"^(?:（\d+）|\d+[.．])\s+")
CORE_RE = re.compile(r"^核心答题点[:：]")
H_STYLE_RE = re.compile(r"^Heading ([12])$")


@dataclass
class Para:
    idx: int
    text: str
    style: str


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_paras(path: Path) -> list[Para]:
    doc = Document(str(path))
    return [
        Para(i, p.text.strip(), p.style.name if p.style else "")
        for i, p in enumerate(doc.paragraphs)
    ]


def metrics(path: Path) -> dict[str, int | str]:
    paras = load_paras(path)
    text = "\n".join(p.text for p in paras)
    core_texts = [p.text for p in paras if CORE_RE.match(p.text)]
    entries = [p.text for p in paras if ENTRY_RE.match(p.text)]
    h1h2 = [p.text for p in paras if H_STYLE_RE.match(p.style)]
    return {
        "file": str(path),
        "sha256": sha256(path),
        "paragraphs": len(paras),
        "nonempty_paragraphs": sum(1 for p in paras if p.text),
        "entries": len(entries),
        "core_points": len(core_texts),
        "unique_core_points": len(set(core_texts)),
        "why_fields": text.count("【为什么能想到】"),
        "answer_fields": text.count("【答案落点】"),
        "question_fields": text.count("【设问】"),
        "trigger_fields": text.count("【材料触发点】"),
        "h1_h2": len(h1h2),
        "template_这不是单个材料细节": text.count("这不是单个材料细节"),
        "template_通向该术语": text.count("通向该术语"),
        "template_抓住这条线": text.count("抓住这条线"),
        "book_missing_exact": text.count("《国际政治与经济》"),
        "book_full_exact": text.count("《当代国际政治与经济》"),
        "fake_page_exact": text.count("原卷第8页") + text.count("原卷第 8 页"),
        "fengtai_qimo_q20": text.count("2026丰台期末Q20"),
        "dongcheng_q19_3": text.count("东城一模Q19(3)"),
        "three_global_initiatives": text.count("三大全球倡议"),
        "four_global_initiatives": text.count("四大全球倡议"),
        "rubric_evidence_label": text.count("细则依据"),
        "local_path_residue": text.count("/Users/wanglifei"),
    }


def nearest_context(paras: list[Para], idx: int) -> dict[str, str]:
    h1 = ""
    h2 = ""
    core = ""
    entry = ""
    for j in range(idx, -1, -1):
        p = paras[j]
        if not entry and ENTRY_RE.match(p.text):
            entry = p.text
        if not core and CORE_RE.match(p.text):
            core = p.text
        if not h2 and p.style == "Heading 2":
            h2 = p.text
        if not h1 and p.style == "Heading 1":
            h1 = p.text
        if h1 and h2 and core and entry:
            break
    return {"h1": h1, "h2": h2, "core": core, "entry": entry}


def entry_block(paras: list[Para], entry_idx: int) -> str:
    end = len(paras)
    for j in range(entry_idx + 1, len(paras)):
        if ENTRY_RE.match(paras[j].text) or CORE_RE.match(paras[j].text):
            end = j
            break
    return "\n".join(p.text for p in paras[entry_idx:end] if p.text)


def find_entry_index(paras: list[Para], idx: int) -> int:
    for j in range(idx, -1, -1):
        if ENTRY_RE.match(paras[j].text):
            return j
    return idx


def suspicious_entries(paras: list[Para]) -> list[dict[str, str | int]]:
    out: list[dict[str, str | int]] = []
    for p in paras:
        if "东城一模Q19(3)" in p.text:
            eidx = find_entry_index(paras, p.idx)
            block = entry_block(paras, eidx)
            ctx = nearest_context(paras, eidx)
            flag = []
            if "强链补链" in block and ("制度型开放" in block or "高水平对外开放" in block):
                flag.append("强链补链与制度型开放/高水平开放同块")
            if "龙头企业" in block and "制度型开放" in block:
                flag.append("龙头企业与制度型开放同块")
            if "而不是" in block and ("就要落到开放举措本身" in block or "不是只写强链补链" in block):
                flag.append("解释文字内部有修正痕迹")
            out.append(
                {
                    "para_idx": eidx,
                    "flag": "；".join(flag) or "未触发自动疑点",
                    **ctx,
                    "block": block,
                }
            )
    return out


def fengtai_entries(paras: list[Para]) -> list[dict[str, str | int]]:
    out: list[dict[str, str | int]] = []
    seen: set[int] = set()
    for p in paras:
        if "2026丰台期末Q20" in p.text:
            eidx = find_entry_index(paras, p.idx)
            if eidx in seen:
                continue
            seen.add(eidx)
            ctx = nearest_context(paras, eidx)
            out.append({"para_idx": eidx, **ctx, "block": entry_block(paras, eidx)})
    return out


def residue_hits(paras: list[Para], terms: list[str]) -> list[dict[str, str | int]]:
    hits: list[dict[str, str | int]] = []
    for p in paras:
        found = [t for t in terms if t in p.text]
        if found:
            hits.append({"para_idx": p.idx, "terms": "；".join(found), "text": p.text})
    return hits


def write_csv(path: Path, rows: list[dict[str, str | int]]) -> None:
    keys: list[str] = []
    for row in rows:
        for key in row:
            if key not in keys:
                keys.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=keys)
        w.writeheader()
        for row in rows:
            w.writerow(row)


def md_table(rows: list[dict[str, int | str]], keys: list[str]) -> str:
    lines = ["|" + "|".join(keys) + "|", "|" + "|".join(["---"] * len(keys)) + "|"]
    for row in rows:
        lines.append("|" + "|".join(str(row.get(k, "")).replace("|", "\\|") for k in keys) + "|")
    return "\n".join(lines)


def main() -> int:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    claude_paras = load_paras(CLAUDE_DOCX)
    codex_paras = load_paras(CODEX_DOCX)
    metric_rows = [metrics(CLAUDE_DOCX), metrics(CODEX_DOCX)]
    with (AUDIT_DIR / "metrics.json").open("w", encoding="utf-8") as f:
        json.dump(metric_rows, f, ensure_ascii=False, indent=2)

    fengtai = fengtai_entries(claude_paras)
    dongcheng = suspicious_entries(claude_paras)
    residues = residue_hits(
        claude_paras,
        [
            "这不是单个材料细节",
            "通向该术语",
            "抓住这条线",
            "《国际政治与经济》",
            "原卷第8页",
            "原卷第 8 页",
            "细则依据",
            "/Users/wanglifei",
        ],
    )
    write_csv(AUDIT_DIR / "claude_fengtai_2026_qimo_q20_entries.csv", fengtai)
    write_csv(AUDIT_DIR / "claude_dongcheng_q19_3_entries.csv", dongcheng)
    write_csv(AUDIT_DIR / "claude_residue_hits.csv", residues)

    claude = metric_rows[0]
    codex = metric_rows[1]
    report = [
        "# Claude Final Verification Summary",
        "",
        "## File Identity",
        "",
        f"- Claude DOCX: `{CLAUDE_DOCX}`",
        f"- Prior local Codex handoff: `{CODEX_DOCX}`",
        f"- Claude SHA256: `{claude['sha256']}`",
        f"- Codex SHA256: `{codex['sha256']}`",
        "",
        "## Structure Metrics",
        "",
        md_table(
            metric_rows,
            [
                "file",
                "entries",
                "core_points",
                "unique_core_points",
                "why_fields",
                "answer_fields",
                "question_fields",
                "trigger_fields",
                "template_这不是单个材料细节",
                "book_missing_exact",
                "fake_page_exact",
                "fengtai_qimo_q20",
                "dongcheng_q19_3",
            ],
        ),
        "",
        "## Auto Findings",
        "",
        f"- Claude file is not byte-identical to prior local Codex handoff and has different structure counts.",
        f"- Template residue in Claude file: {claude['template_这不是单个材料细节']} / {claude['template_通向该术语']} / {claude['template_抓住这条线']}.",
        f"- Exact missing-book-title `《国际政治与经济》` occurrences: {claude['book_missing_exact']}.",
        f"- Exact fake-page references `原卷第8页` / `原卷第 8 页`: {claude['fake_page_exact']}.",
        f"- `2026丰台期末Q20` entries restored in Claude file: {len(fengtai)} blocks.",
        f"- `东城一模Q19(3)` blocks found in Claude file: {len(dongcheng)} blocks.",
        f"- Residue hits requiring manual inspection: {len(residues)} rows in `claude_residue_hits.csv`.",
        "",
        "## Manual-Review Queues",
        "",
        "- `claude_fengtai_2026_qimo_q20_entries.csv`: restored Q20 blocks; source closure must be checked against desktop paper and rubric.",
        "- `claude_dongcheng_q19_3_entries.csv`: all Dongcheng Q19(3) blocks with automatic flags.",
        "- `claude_residue_hits.csv`: template, fake page, book-title, backend-label, and path residue hits.",
        "",
    ]
    (AUDIT_DIR / "CLAUDE_FINAL_VERIFY_SUMMARY.md").write_text("\n".join(report), encoding="utf-8")
    print(AUDIT_DIR / "CLAUDE_FINAL_VERIFY_SUMMARY.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
