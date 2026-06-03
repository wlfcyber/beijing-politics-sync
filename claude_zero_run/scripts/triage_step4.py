#!/usr/bin/env python3
"""Step 4: split source-locked candidates into core / reference / pending+excluded."""
import csv
from pathlib import Path

INDEX = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/03_source_lock_index.csv")
CORE = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/04_core_questions.csv")
REF = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/04_reference_questions.csv")
PEND = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/04_pending_or_excluded.csv")
REPORT = Path("/Users/wanglifei/Desktop/北京高考政治/claude_zero_run/04_corpus_status_report.md")

def main():
    with INDEX.open() as f:
        rows = list(csv.DictReader(f))
    core, ref, pend = [], [], []
    for r in rows:
        if r["decision"] == "core_candidate" and r["evidence_level"] in ("formal","lecture_explicit_scoring"):
            core.append(r)
        elif r["decision"] == "reference_candidate" or r["evidence_level"] == "reference_only":
            ref.append(r)
        else:
            pend.append(r)

    for path, data in [(CORE,core),(REF,ref),(PEND,pend)]:
        with path.open("w", newline="", encoding="utf-8") as f:
            if not data:
                f.write("question_id,suite,qno,subq,decision,reason,category,evidence_level,paper_file,rubric_file,card_file\n")
                continue
            w = csv.DictWriter(f, fieldnames=data[0].keys())
            w.writeheader()
            for r in data:
                w.writerow(r)

    # Build status report
    from collections import Counter
    def cat_count(rs):
        cc = Counter()
        for r in rs:
            for c in (r["category"] or "").split(", "):
                if c: cc[c] += 1
        return cc
    lines = ["# 04 Corpus Status Report",
             "",
             f"- Total source-locked sub-Q decisions: {len(rows)}",
             f"- A 核心题（formal/lecture 细则 + 真实设问 + 真实材料）: {len(core)}",
             f"- B 参考题（reference_only / 仅参考答案）: {len(ref)}",
             f"- C 待补/剔除（无细则匹配、非选必二、模块边界不明）: {len(pend)}",
             "",
             "## A 核心题（按类别分布）",
             ""]
    for cat, n in cat_count(core).most_common():
        lines.append(f"- {cat}: {n}")
    lines += ["", "### 核心题清单", ""]
    for r in core:
        lines.append(f"- `{r['question_id']}` 子问{r['subq'] or '0'} | {r['category']} | {r['evidence_level']} | card: {r['card_file']}")
    lines += ["", "## B 参考题清单", ""]
    for r in ref:
        lines.append(f"- `{r['question_id']}` 子问{r['subq'] or '0'} | {r['category']} | {r['evidence_level']}")
    lines += ["", "## C 待补 / 剔除清单", ""]
    for r in pend:
        lines.append(f"- `{r['question_id']}` 子问{r['subq'] or '?'} | reason: {r['reason']} | category: {r['category']}")
    lines += ["",
              "## 口径说明",
              "- A 类必须同时满足：真实设问可识别（运用《法律与生活》或同义法律线索）+ 真实材料可与设问对应 + 正式细则/讲评/评标可逐条匹配。",
              "- B 类只用于 `08_开放容器与待补题.md` 的参考池，不进入框架统计。",
              "- C 类中 `no law sub-Q found` 多为必修三/必修四/经济/逻辑题，按用户硬规则剔除；`no rubric found` 是缺正式给分口径，待用户补充细则后才可上探到 A 或 B。",
              "- 旧 v8/v9/v10/v11/v12 的题链/结论本轮一律不继承；本表与旧表不互通。",
             ]
    REPORT.write_text("\n".join(lines), encoding="utf-8")
    print(f"core={len(core)} ref={len(ref)} pend={len(pend)}")

if __name__ == "__main__":
    main()
