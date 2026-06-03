#!/usr/bin/env python3
"""Build a human-review listing of every excluded / deferred sub-Q + brief content snippet."""
import csv
from pathlib import Path

INDEX = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/03_source_lock_index.csv")
CANDS = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/02_candidate_subjective_law_questions.csv")
OUT = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/04_excluded_review.md")

def main():
    cmap = {}
    with CANDS.open() as f:
        for r in csv.DictReader(f):
            cmap[r["question_id"]] = r
    with INDEX.open() as f:
        rows = list(csv.DictReader(f))
    lines = ["# 04 Excluded / Deferred Review (for human eyes)",
             "",
             "本表列出所有未进入 A 核心题的子问，供监督核验。每条给出：候选行的 prompt 片段、material 片段，以及剔除/挂起原因。",
             ""]
    by_decision = {}
    for r in rows:
        by_decision.setdefault(r["decision"], []).append(r)
    for d in ("excluded","deferred","reference_candidate"):
        if d not in by_decision: continue
        lines.append(f"## decision = {d} ({len(by_decision[d])} sub-Q)")
        lines.append("")
        for r in by_decision[d]:
            qid = r["question_id"]
            c = cmap.get(qid, {})
            prompt = (c.get("real_prompt_excerpt","") or "")[:300]
            material = (c.get("real_material_excerpt","") or "")[:300]
            why_not = c.get("why_maybe_not","") or ""
            paper_kind = c.get("paper_source_kind","")
            evid = r["evidence_level"]
            lines.append(f"### {qid}  sub={r['subq'] or '0'}")
            lines.append(f"- reason: {r['reason']}")
            lines.append(f"- evidence_level: {evid}")
            lines.append(f"- paper_kind: {paper_kind}")
            lines.append(f"- prompt: {prompt}")
            lines.append(f"- material: {material}")
            lines.append(f"- why_maybe_not: {why_not}")
            lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}, total non-core sub-Qs={sum(len(by_decision.get(d,[])) for d in ('excluded','deferred','reference_candidate'))}")

if __name__ == "__main__":
    main()
