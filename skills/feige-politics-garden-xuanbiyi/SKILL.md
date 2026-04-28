---
name: feige-politics-garden-xuanbiyi
description: "Use when Codex needs 飞哥政治庄园-选必一 for 选择性必修一《当代国际政治与经济》 Beijing district-paper main-question work: scoring-rubric terms, marking-rule term accumulation, full prompts, exact 细则位置, material-trigger logic, module-boundary filtering, and cumulative Markdown/Word deliverables. Use for 主观题 unless the user explicitly asks otherwise."
---

# 飞哥政治庄园-选必一

This branch handles 选择性必修一《当代国际政治与经济》 work. Its core output is not a general answer bank; it is a scoring-term accumulation document built from rubrics and marking rules.

If the final artifact is `.docx`, also use the `documents` skill and render every DOCX before delivery.

## Load First

Before processing any 选必一主观题 batch, read:

- `references/xuanbiyi-term-protocol.md`: required format, classification rules, merge rules, negative examples, and sample entries.

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
- `完整设问` must appear under every term entry, even when multiple entries come from the same question.
- `材料触发` must explain the trigger logic. It is not a paraphrase of the material.
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

## Quality Gate

Before delivering a sample or batch, check:

- Every entry has `完整设问`, `细则位置`, `来源`, `材料触发`, and `答案句`.
- The phrase after `术语：` is from the scoring source, not invented.
- Same-position scoring phrases have been merged.
- `材料触发` starts from the task relation: question type, cooperation/competition/governance/opening relation, then the term.
- Module-boundary terms are excluded or separately noted.
