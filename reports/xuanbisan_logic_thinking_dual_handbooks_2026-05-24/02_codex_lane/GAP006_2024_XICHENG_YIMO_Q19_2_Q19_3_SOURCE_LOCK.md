# GAP006 Source Lock: 2024西城一模 Q19(2)-Q19(3)

Status: `source_locked_pending_external_review`

This file advances GAP006 at the local source-evidence level only. It does not close the 2024 suite backlog, GPT Pro, Claude V4/V5/V33, Governor, Confucius, or final delivery gates.

## Source

- paper cache: `gpt_sources/2aa2ee045f75ecd8_2024.4高三统一测试思想政治试卷.md:226-278`
- reference-answer cache: `gpt_sources/91e28443e7a1bb0e_2024.4高三统一测试思想政治答案.md:53-62`
- formal marking-rule cache: `gpt_sources/f7bcf000f212cc69_2024西城一模细则.md:65-78`
- raw paper: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024西城一模\试卷\2024.4高三统一测试思想政治试卷.docx`
- raw reference answer: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024西城一模\其他材料\2024.4高三统一测试思想政治答案.docx`
- raw marking rule: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024西城一模\细则\2024西城一模细则.docx`

The formal marking-rule docx cache is the evidence authority. The paper and reference-answer caches lock the exact prompt and baseline answer.

## Q0067 2024西城一模 Q19(2)

Evidence level: `A-formal`

Question:

> 有研究者给“举国体制”下了一个定义。阅读文本信息，按下图中的序号写出其构成。（2分）

Text definition:

> 举国体制是利用国家力量动员规模性资源、实现国家目标的一种任务组织方式和体制机制安排。

Formal rubric signal:

- ① 举国体制
- ② 是
- ③ 利用国家力量动员规模性资源、实现国家目标
- ④ 一种任务组织方式和体制机制安排
- 任意2个考点都答对给1分；内容丢字、简写、错别字不影响大意也给分。

Local decision: Promote Q19(2) as `Q0067` reasoning main-question row for definition components.

## Q0068 2024西城一模 Q19(3)

Evidence level: `A-formal`

Question:

> “举国体制”与“新型举国体制”的外延是 ____ 关系。（1分）

Formal rubric signal:

- `相容` 或 `属种`。

Local decision: Promote Q19(3) as `Q0068` reasoning main-question row for concept extension relation.

## Student-Usable Trigger Chain

- Definition question: `A 是 B 的 C` -> find 被定义项、定义联项、种差、属概念. Here, 举国体制 is the defined term, 是 is the definition link, 利用国家力量动员规模性资源、实现国家目标 is the species difference, and 一种任务组织方式和体制机制安排 is the genus.
- Extension question: `新型举国体制` still belongs inside `举国体制`, but has added socialist-market-economy and key-core-technology features. Therefore the relation is compatible, more precisely genus-species.

Answer sentence: Q19(2) 可写：①举国体制，②是，③利用国家力量动员规模性资源、实现国家目标，④一种任务组织方式和体制机制安排。Q19(3) 可写：“举国体制”与“新型举国体制”的外延是相容关系，也可写属种关系。

## Gate Decision

Add Q0067 and Q0068 to the coverage matrix, source-packet queue, reasoning-form ledger, and reasoning V2 body draft as `source_locked_pending_external_review`.

GAP006 remains open because the 2024 suite-by-suite backlog is not exhausted.
