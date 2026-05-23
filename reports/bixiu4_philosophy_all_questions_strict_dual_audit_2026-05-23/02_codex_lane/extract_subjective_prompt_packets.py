from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


DESKTOP = Path.home() / "Desktop"
ROOT = DESKTOP / "02_代码项目与工具" / "mac-thread-restore" / "beijing-politics-sync-visible"
RUN = ROOT / "reports" / "bixiu4_philosophy_all_questions_strict_dual_audit_2026-05-23"
STRICT = ROOT / "reports" / "bixiu4_philosophy_strict_v8_2026-05-23"
SRC = STRICT / "old_subjective_rows_present_but_quality_failed_v8.csv"
OUT_CSV = RUN / "02_codex_lane" / "unique_subjective_prompt_packets.csv"
OUT_MD = RUN / "02_codex_lane" / "unique_subjective_prompt_packets.md"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def find_prompt_snippet(bundle_text: str, q: str) -> tuple[str, str]:
    patterns = [
        rf"(?m)^.*?{q}\s*[．.、]\s*.*$",
        rf"(?m)^.*?第\s*{q}\s*题.*$",
        rf"(?m)^.*?{q}\s*[（(]\d+[）)].*$",
        rf"(?m)^.*?{q}\s*[．.].*结合材料.*$",
    ]
    positions: list[int] = []
    for pat in patterns:
        for m in re.finditer(pat, bundle_text):
            positions.append(m.start())
    if not positions:
        idx = bundle_text.find(f"第{q}题")
        if idx >= 0:
            positions.append(idx)
    if not positions:
        return "", "NOT_FOUND"
    # Prefer a hit that is near “结合材料” or “运用”.
    best = positions[0]
    best_score = -1
    for pos in positions:
        window = bundle_text[pos : pos + 1600]
        score = 0
        for term in ["结合材料", "运用", "谈谈", "说明", "分析", "阐释", "认识"]:
            if term in window:
                score += 1
        if score > best_score:
            best = pos
            best_score = score
    snippet = bundle_text[best : best + 2200]
    cut_points = [m.start() for m in re.finditer(r"(?m)^\s*(?:答案|【答案】|评分标准|学生问题|选择题第|\d+[．.])", snippet[200:])]
    if cut_points:
        snippet = snippet[: 200 + cut_points[0]]
    return clean(snippet), "FOUND"


def main() -> None:
    rows = read_csv(SRC)
    grouped: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    for r in rows:
        grouped[(r["suite_name"], r["question_no_norm"])].append(r)

    out_rows: list[dict[str, str]] = []
    md = ["# 18 道旧主观漏项回源设问包", ""]
    for idx, ((suite, q), items) in enumerate(sorted(grouped.items()), 1):
        bundle_rel = items[0].get("bundle_path", "")
        bundle_path = ROOT / bundle_rel
        bundle_text = bundle_path.read_text(encoding="utf-8", errors="replace") if bundle_path.exists() else ""
        snippet, status = find_prompt_snippet(bundle_text, q)
        triggers = "；".join(dict.fromkeys(clean(i.get("trigger", "")) for i in items if clean(i.get("trigger", ""))))
        materials = "；".join(dict.fromkeys(clean(i.get("material", "")) for i in items if clean(i.get("material", ""))))[:1200]
        logics = "；".join(dict.fromkeys(clean(i.get("logic", "")) for i in items if clean(i.get("logic", ""))))[:1600]
        row = {
            "suite_name": suite,
            "question_no": q,
            "entry_count": str(len(items)),
            "bundle_path": bundle_rel,
            "prompt_extract_status": status,
            "prompt_snippet": snippet,
            "triggers": triggers,
            "materials": materials,
            "logic_summary": logics,
        }
        out_rows.append(row)
        md.extend(
            [
                f"## {idx}. {suite} 第{q}题（{len(items)} 条触发链）",
                "",
                f"- 回源状态：{status}",
                f"- 触发知识：{triggers}",
                "",
                "### 原文设问摘录",
                "",
                snippet or "未抽到，必须回原文件。",
                "",
                "### 已有材料触发/逻辑",
                "",
                f"- 材料：{materials}",
                f"- 逻辑：{logics}",
                "",
            ]
        )
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CSV.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(out_rows[0].keys()))
        writer.writeheader()
        writer.writerows(out_rows)
    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"unique_subjective_questions={len(out_rows)}")
    print(f"found={sum(1 for r in out_rows if r['prompt_extract_status']=='FOUND')}")
    print(OUT_MD)


if __name__ == "__main__":
    main()
