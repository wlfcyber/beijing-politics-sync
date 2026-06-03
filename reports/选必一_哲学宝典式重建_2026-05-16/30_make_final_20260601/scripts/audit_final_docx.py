#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

from docx import Document


RUN_DIR = Path(
    "/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/"
    "选必一_哲学宝典式重建_2026-05-16/30_make_final_20260601"
)
DOCX = RUN_DIR / "03_outputs/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.docx"
AUDIT_DIR = RUN_DIR / "02_audit"

ENTRY_RE = re.compile(r"^(?:（\d+）|\d+[.．])\s+")
CORE_RE = re.compile(r"^核心答题点[:：]")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def nearest_core(paras, idx: int) -> str:
    for i in range(idx, -1, -1):
        if CORE_RE.match(paras[i].text.strip()):
            return paras[i].text.strip()
    return ""


def block(paras, idx: int) -> str:
    end = len(paras)
    for i in range(idx + 1, len(paras)):
        t = paras[i].text.strip()
        if ENTRY_RE.match(t) or CORE_RE.match(t):
            end = i
            break
    return "\n".join(p.text.strip() for p in paras[idx:end] if p.text.strip())


def main() -> int:
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    doc = Document(str(DOCX))
    paras = doc.paragraphs
    text = "\n".join(p.text for p in paras)
    entries = [p.text for p in paras if ENTRY_RE.match(p.text.strip())]
    core_points = [p.text.strip() for p in paras if CORE_RE.match(p.text.strip())]

    metrics = {
        "file": str(DOCX),
        "sha256": sha256(DOCX),
        "paragraphs": len(paras),
        "nonempty_paragraphs": sum(1 for p in paras if p.text.strip()),
        "entries": len(entries),
        "core_points": len(core_points),
        "unique_core_points": len(set(core_points)),
        "why_fields": text.count("【为什么能想到】"),
        "answer_fields": text.count("【答案落点】"),
        "question_fields": text.count("【设问】"),
        "trigger_fields": text.count("【材料触发点】"),
        "fengtai_old_label": text.count("2026丰台期末Q20"),
        "fengtai_relabeled": text.count("2026丰台期末细则复练Q20"),
        "template_1": text.count("这不是单个材料细节"),
        "template_2": text.count("通向该术语"),
        "template_3": text.count("抓住这条线"),
        "book_missing_exact": text.count("《国际政治与经济》"),
        "book_full_exact": text.count("《当代国际政治与经济》"),
        "fake_page": text.count("原卷第8页") + text.count("原卷第 8 页"),
        "rubric_evidence_label": text.count("细则依据"),
        "local_path_residue": text.count("/Users/wanglifei"),
        "dongcheng_q19_3": text.count("东城一模Q19(3)"),
        "three_global_initiatives": text.count("三大全球倡议"),
        "four_global_initiatives": text.count("四大全球倡议"),
    }
    (AUDIT_DIR / "metrics.json").write_text(json.dumps(metrics, ensure_ascii=False, indent=2), encoding="utf-8")

    dongcheng_rows = []
    for i, p in enumerate(paras):
        if p.text.strip().startswith("2. 2026东城一模Q19(3)") and nearest_core(paras, i) == "核心答题点：中国扩大高水平对外开放与制度型开放":
            b = block(paras, i)
            dongcheng_rows.append({
                "idx": i,
                "core": nearest_core(paras, i),
                "has_strong_chain": "强链补链" in b or "龙头企业" in b,
                "block": b,
            })
    with (AUDIT_DIR / "dongcheng_target_check.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["idx", "core", "has_strong_chain", "block"])
        w.writeheader()
        w.writerows(dongcheng_rows)

    failures = []
    if metrics["core_points"] != 108 or metrics["unique_core_points"] != 108:
        failures.append("core point count not 108/108")
    if not (metrics["why_fields"] == metrics["answer_fields"] == metrics["question_fields"] == metrics["trigger_fields"] == 472):
        failures.append("field counts not 472")
    if metrics["fengtai_old_label"] != 0:
        failures.append("old Fengtai Q20 label remains")
    if metrics["fengtai_relabeled"] != 11:
        failures.append("Fengtai relabeled count not 11")
    for key in ["template_1", "template_2", "template_3", "book_missing_exact", "fake_page", "rubric_evidence_label", "local_path_residue"]:
        if metrics[key] != 0:
            failures.append(f"{key} not zero")
    if len(dongcheng_rows) != 1:
        failures.append(f"expected one target Dongcheng row, got {len(dongcheng_rows)}")
    elif dongcheng_rows[0]["has_strong_chain"]:
        failures.append("target Dongcheng row still has strong-chain material")

    report = [
        "# Final DOCX Audit",
        "",
        "## Metrics",
        "",
        "```json",
        json.dumps(metrics, ensure_ascii=False, indent=2),
        "```",
        "",
        "## Result",
        "",
        "PASS" if not failures else "FAIL",
    ]
    if failures:
        report.extend(["", "## Failures", "", *[f"- {x}" for x in failures]])
    (AUDIT_DIR / "FINAL_AUDIT.md").write_text("\n".join(report), encoding="utf-8")
    print(AUDIT_DIR / "FINAL_AUDIT.md")
    if failures:
        raise SystemExit("\n".join(failures))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
