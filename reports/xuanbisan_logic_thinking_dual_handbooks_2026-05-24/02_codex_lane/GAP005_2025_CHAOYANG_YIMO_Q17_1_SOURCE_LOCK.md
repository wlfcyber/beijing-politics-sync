# GAP005 Source Lock: 2025朝阳一模 Q17(1)

Status: `source_locked_pending_external_review`

This file advances GAP005 at the local source-evidence level only. It does not close the 2025 suite backlog, GPT Pro, Claude V4/V5/V20, Governor, Confucius, or final delivery gates.

## Source

- paper and teacher-version cache: `gpt_sources/e051761a7fc68fef_2025北京朝阳高三一模政治_教师版.md:190-198,309-315`
- formal marking-rule PDF cache metadata: `gpt_sources/f5f683a900508fd2_2025朝阳一模细则.md:1-16`
- formal marking-rule rendered page visually checked: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\f5f683a900508fd2\page_001.png`
- support marking summary cache: `gpt_sources/f0b3ab889aa0b17b_20250329高3阅卷总结17_1题_具身智能_任会波组_阐释论证.md:25-57,80-97`
- raw paper: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025朝阳一模\试卷\2025北京朝阳高三一模政治（教师版）.pdf`
- raw formal marking rule: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025朝阳一模\细则\2025朝阳一模细则.pdf`
- raw support material: `C:\Users\Administrator\Desktop\2025各区模拟题\2025各区一模\2025朝阳一模\其他材料\20250329高3阅卷总结17 1题 具身智能 任会波组 阐释论证.doc`

The formal marking-rule rendered page is the evidence authority. The support marking summary contains extractable text that aligns with the rendered formal page.

## Q0052 2025朝阳一模 Q17(1)

Evidence level: `A-formal`

Question:

> 我们想要实现虚拟与现实的深度融合，就必须要让人工智能拥有一个智能硬件载体。所以，让人工智能拥有一个智能载体，就能实现虚拟与现实的深度融合。运用《逻辑与思维》知识，判断该推理正确与否，并说明理由。

Formal rubric signal:

- 该推理不正确。1 分。
- 能够运用充分条件或必要条件进行分析。1 分。
- 能够准确说明充分条件假言或必要条件假言的推理规则。1 分。
- 在充分条件形式中，原判断可写为“如果想要实现虚拟与现实的深度融合，就必须让人工智能拥有智能硬件载体”；肯定后件不能推出肯定前件。
- 在必要条件形式中，原判断可写为“只有让人工智能拥有智能硬件载体，才能实现虚拟与现实的深度融合”；肯定前件不能推出肯定后件。
- 结合材料说明：没有智能硬件载体就不能实现虚拟与现实深度融合，1 分；实现虚拟与现实深度融合不仅要智能载体，还需要其他更多条件，1 分。

## Local Decision

Promote as `Q0052` reasoning main-question row.

The row should teach one thing sharply: a necessary condition cannot be converted into a sufficient condition. Do not route it to创新思维、辩证思维 or general AI-topic analysis.

## Student-Usable Trigger Chain

- Let `P` = 实现虚拟与现实深度融合; `Q` = 人工智能拥有智能硬件载体.
- Original statement: `P -> Q`, or necessary-condition wording `只有 Q 才 P`.
- Given/assumed: `Q`.
- Invalid conclusion: therefore `P`.
- Error: in sufficient-condition form, this is肯定后件不能肯定前件; in necessary-condition form, this is肯定前件不能肯定后件.

Answer sentence: 该推理不正确。“想要实现虚拟与现实深度融合，就必须让人工智能拥有智能硬件载体”说明智能硬件载体是实现深度融合的必要条件，而不是充分条件；必要条件假言推理中，肯定前件不能必然肯定后件，因此仅有智能载体不能推出一定能实现虚拟与现实深度融合。

## Gate Decision

Add Q0052 to the coverage matrix, source-packet queue, reasoning-form ledger, and reasoning V2 body draft as `source_locked_pending_external_review`.

GAP005 remains open because the 2025 suite-by-suite backlog is not exhausted.
