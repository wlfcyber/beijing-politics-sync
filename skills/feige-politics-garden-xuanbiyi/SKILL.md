---
name: feige-politics-garden-xuanbiyi
description: "Use when Codex needs 飞哥政治庄园-选必一 for 选择性必修一《当代国际政治与经济》 Beijing district-paper main-question work: scoring-rubric terms, marking-rule term accumulation, full prompts, exact 细则位置, material-trigger logic, module-boundary filtering, and cumulative Markdown/Word deliverables. Use for 主观题 unless the user explicitly asks otherwise."
---

# 飞哥政治庄园-选必一

This branch handles 选择性必修一《当代国际政治与经济》 work. Its core output is not a general answer bank; it is a scoring-term accumulation document built from rubrics and marking rules.

If the final artifact is `.docx`, also use the `documents` skill and render every DOCX before delivery.

## Load First

Before processing any 选必一主观题 batch, first pass the project three-layer SOP by reading the master governor report under `reports/master_governor/` and the shared SOP at `../feige-politics-garden/references/project-governor-three-layer-sop.md`. Then read:

- `references/current-user-requirements.md`: the user's currently pinned delivery requirements, including the required six-bucket structure, required fields per entry, and the rule that the main framework document must not show frequency counts.
- `references/xuanbiyi-term-protocol.md`: required format, classification rules, merge rules, negative examples, and sample entries.

If the master governor report is missing or stale, refresh it with `scripts/master_governor.py` before worker execution. If this lane is flagged for false closure, missing governor, missing coverage, or pending real advisor calls, repair those control files before adding正文.

Use the shared corpus cache first:

- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.csv`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts\*.txt`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\<hash>\page_*.png`

Cache-first is not cache-only. If cached text is garbled, missing, incomplete, or not enough to verify a scoring point, return to the original Word/PDF/PPT or rendered page image.

## Required Output Unit

Every accumulated term entry must include:

```markdown
**术语：<rubric original phrase(s)>**

- 完整设问：<copy the full question prompt>
- 细则位置：<suite, question, scoring section, exact point, score, required/optional status>
- 来源：<suite and question>
- 材料触发：<why this prompt/material relation triggers this scoring term>
- 答案句：<a concrete sentence that can enter the answer>
```

Do not add a `真题规律` section or field.

`细则位置` is the highest-priority field. Do not keep an entry if its scoring source and scoring location are not clear enough to audit.

## Core Rules

- `术语：` must preserve scoring-rubric terms or marking-rule phrases. Do not put your own summary after the colon.
- If you need your own summary phrase, use it only as a heading container.
- 同一采分核心必须先合并，再做表述积累。不要把“时代主题”“和平与发展”“中国做法符合和平与发展时代主题”拆成三个术语；它们属于同一核心点，后两者应进入该核心点的可用表述/答案句积累。
- 合并后的核心采分点必须保留最高信息量的细则原词，不能抽象成空泛标签。比如核心点应写成`推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展`，不能只写`经济全球化正确方向`；后者只能作为表述积累或辅助说明。
- 判断同类项时看采分功能和教材核心，不只看字面是否完全相同。`推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展` 与 `经济全球化方向：普惠、平衡、共赢` 属于同一核心；`合作共赢的新型国际关系` 的不同题面表述也应归并到同一核心。
- 合并后保留差异，不抹平差异：在同一核心点下记录“表述积累 / 题型用法 / 来源题目”，让学生背一个点、会多种写法。
- `完整设问` must appear under every term entry, even when multiple entries come from the same question.
- `材料触发` must explain the trigger logic. It is not a paraphrase of the material.
- `答案句` means the exact sentence/point a candidate could write on the answer sheet. It must contain the scoring term, the material fact for this question, and the reasoning/result chain. Do not write process/meta language such as `要落到……采分点`, `并结合材料说明`, `本题需要写`, `设问要求`, or `细则要求`.
- When a rubric has `总说/分说`, `宏观概括/细化解释`, or angle-plus-material layers, audit and preserve both the general layer and every relevant sub-layer. Do not keep only the total/general phrase.
- Treat ordinary reference answers as reference answers, not scoring terms, unless the user confirms they are scoring rules.
- Accumulate 主观题 terms by default. Process choice questions only when the user explicitly asks.

## Framework Buckets

Use the user's six top-level buckets unless a scoring term truly cannot fit:

1. 时代背景
2. 理论
3. 经济全球化
4. 政治多极化
5. 中国
6. 联合国

Second-level and third-level headings are reluctant containers. Merge whenever the scoring function is the same.

## Boundary Control

- 必修二 terms such as `扩大国际市场`, `推进高水平对外开放`, and `落实开放发展理念` do not enter the 选必一 main table. Put them in a boundary note or a cross-book table only if useful.
- Terms from 选必二、选必三、政治与法治、法律、逻辑, or 必修四 must not be forced into the 选必一 table.
- Result or landing phrases in a reference answer are not automatically scoring terms. For example, `全球产业链供应链稳定` is not the term when the marked scoring point is `坚持创新驱动发展战略`.
- 2026石景山期末：用户逐题复核确认没有可用评分细则；本套卷所有书、所有模块都排除。除非用户明确提供新的评分细则来源，不得再用答案及评分参考补入。

## Quality Gate

Before delivering a sample or batch, check:

- Every entry has `完整设问`, `细则位置`, `来源`, `材料触发`, and `答案句`.
- The phrase after `术语：` is from the scoring source, not invented.
- Same-position scoring phrases have been merged, and cross-question same-core phrases have been归并成一个核心点 with expression accumulation.
- For repeated core points, the student-facing index must show one core term row plus multiple expression variants, not several near-duplicate rows.
- `材料触发` starts from the task relation: question type, cooperation/competition/governance/opening relation, then the term.
- No answer sentence contains meta-scoring language such as `采分点`, `要落到`, `并结合材料说明`, `设问`, `细则`, `证据层级`, or `v7`.
- Every `答案句` reads as a candidate's answer-sheet point: scoring term + material fact + because/therefore/effect. Reject vague slogans that only say a title "顺应时代潮流" or merely repeat the term.
- `答案句` should not use the clumsy prefix `材料中`; write the material fact directly as answer-sheet prose.
- Module-boundary terms are excluded or separately noted.
