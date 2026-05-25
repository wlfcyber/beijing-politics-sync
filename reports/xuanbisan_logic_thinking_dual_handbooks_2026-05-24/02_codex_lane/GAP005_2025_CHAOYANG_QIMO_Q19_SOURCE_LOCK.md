# GAP005 Source Lock: 2025朝阳期末 Q19

Status: `source_locked_pending_external_review`

This file advances GAP005 at the local source-evidence level only. It does not close the 2025 suite backlog, GPT Pro, Claude V4/V5/V17, Governor, Confucius, or final delivery gates.

## Source

- paper and teacher-version cache: `gpt_sources/ec82917288aa8774_2025北京朝阳高三_上_期末政治_教师版.md:221-227,326-336`
- support lecture / marking PPT cache: `gpt_sources/195324f05d7e2fea_朝阳高三期末2025.md:215-240`
- formal marking-rule PDF cache metadata: `gpt_sources/953eaee3f98d8598_2025朝阳期末细则.md:1-16`
- formal marking-rule rendered pages visually checked: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\953eaee3f98d8598\page_003.png`, `page_004.png`
- raw paper: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区期末\2025朝阳期末\试卷\2025北京朝阳高三（上）期末政治（教师版）.pdf`
- raw formal marking rule: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区期末\2025朝阳期末\细则\2025朝阳期末细则.pdf`
- raw support material: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx`

The formal marking-rule PDF rendered pages are the evidence authority. The PPT cache is support because it contains the same detailed point breakdown in extractable text.

## Q0049 2025朝阳期末 Q19

Evidence level: `A-formal`

Question:

> 某小区居民讨论冬季应该如何开展扫雪工作。甲：我不同意使用融雪剂，但是我也不同意禁止使用融雪剂。乙：扫雪工作既要快速完成方便居民出行，又要慢慢清扫以免遗漏任何一处积雪。丙：所有为维护小区美好环境付出辛勤劳动的行为都是值得赞扬的。居民在小区扫雪是为维护小区美好环境付出辛勤劳动的行为。所以，居民在小区扫雪是值得赞扬的。结合材料，运用《逻辑与思维》知识，分析上述居民的话是否合乎逻辑，说明理由。

Formal rubric signal:

- 要点1：能够写出甲、乙的话不符合逻辑，丙的话符合逻辑，给1分。
- 要点2：甲的话属于两不可错误，违反排中律，同时否定 A 和非 A；其中两点给2分。
- 要点3：乙的话属于自相矛盾错误，违反矛盾律，同时肯定 A 和非 A；其中两点给2分。
- 要点4：丙的话推理符合三段论推理规则，推理前提真实，推理结构正确；其中两点给2分。

## Local Decision

Promote as `Q0049` reasoning main-question row, with three reasoning-form ledger entries:

- 排中律 / 两不可错误；
- 矛盾律 / 自相矛盾错误；
- 三段论有效结构。

The reasoning handbook should not collapse the three statements into a vague “逻辑综合题”. It should teach the checking order: first judge each speaker, then map the speaker's statement to the exact rule.

## Student-Usable Trigger Chain

- 甲: 同时否定“使用融雪剂”和“禁止使用融雪剂” -> A 与非 A 不能同假 -> 排中律 / 两不可错误。
- 乙: 同时肯定“快速完成扫雪”和“慢慢清扫积雪” -> A 与非 A 不能同真 -> 矛盾律 / 自相矛盾错误。
- 丙: 所有 M 是 P；S 是 M；所以 S 是 P -> 前提真实、结构符合三段论规则 -> 结论符合逻辑。

## Gate Decision

Add Q0049 to the coverage matrix, source-packet queue, reasoning-form ledger, and reasoning V2 body draft as `source_locked_pending_external_review`.

GAP005 remains open because the 2025 suite-by-suite backlog is not exhausted.
