# GAP006 Source Lock: 2024西城二模 Q18(1)

Status: `source_locked_pending_external_review`

This file advances GAP006 at the local source-evidence level only. It does not close the 2024 suite backlog, GPT Pro, Claude V4/V5/V29, Governor, Confucius, or final delivery gates.

## Source

- paper cache: `gpt_sources/0dbd7271f7bf108d_高三模拟测试思想政治试卷.md:162-172`
- reference-answer cache: `gpt_sources/85ebe0578ce81b18_高三模拟测试思想政治答案.md:43-47`
- formal marking-rule cache: `gpt_sources/f2e1772f20ed2085_2024西城二模细则.md:62-75`
- raw paper: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区二模\2024西城二模\试卷\高三模拟测试思想政治试卷.docx`
- raw reference answer: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区二模\2024西城二模\其他材料\高三模拟测试思想政治答案.docx`
- raw marking rule: `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区二模\2024西城二模\细则\2024西城二模细则.docx`

The formal marking-rule docx cache is the evidence authority. The paper and reference answer caches lock the exact prompt and baseline answer.

## Q0063 2024西城二模 Q18(1)

Evidence level: `A-formal`

Question:

> 阅读下表，按提示在空栏处填写。（8分）

Prompt frame:

- 研究过程（部分）
- 在研究过程中找出一个推理类型
- 解释推理过程，以及探求因果联系的方法

Material signal:

- 研究人员收集全球各地 352 种不同品系的高粱，分析它们对盐碱的耐受程度。
- 通过全基因组关联分析技术，定位克隆到与高粱耐碱性显著相关的基因位点 AT1。
- 将 AT1 基因从高粱中提取出来再转到高粱中，高粱耐盐碱能力减弱；将该基因“剪切”后，高粱耐盐碱能力增强。
- 由此说明 AT1 基因在高粱盐碱胁迫响应过程中起负调控作用，缺失 AT1 基因的高粱更耐盐碱。

Formal rubric signal:

- 推理类型 2 分；相应推理过程及方法 6 分。
- Acceptable type: 归纳推理 / 不完全归纳推理 / 科学归纳推理。
- The process can be explained as: from 352 varieties with AT1-related salt-alkali tolerance, infer a general conclusion that absence of AT1 makes sorghum more alkali-tolerant.
- Cause-finding methods include共变法, 求异法, 求同法, or共变法和求异法并用.
- Scoring warning: reasoning type and method should match; if using求同求异并用法, 求同法 and求异法 must be on the same level, otherwise no score for that label.

## Local Decision

Promote Q18(1) as `Q0063` reasoning main-question row.

This is a strong归纳推理 sample because the formal rule forces students to write both the reasoning type and the cause-finding method, not just say “researchers did an experiment”.

## Student-Usable Trigger Chain

- `352种不同品系` -> from many particular samples to a general conclusion -> 不完全归纳 / 科学归纳.
- `AT1基因增加 -> 耐盐碱能力减弱; AT1基因剪切 -> 耐盐碱能力增强` -> one factor changes with the result -> 共变法.
- `提取/转入 vs 剪切 AT1` -> compare conditions with AT1 present/absent -> 求异法.
- `缺失AT1基因的高粱都更耐碱` -> if framed across many varieties, can be read as求同法; do not mechanically write求同求异并用 unless both methods are at the same level.

Answer sentence: 研究人员运用了不完全归纳推理或科学归纳推理。他们考察 352 种不同品系高粱，由缺失 AT1 基因的高粱都更耐碱，推出缺失 AT1 基因的高粱更耐碱的一般性结论；同时通过 AT1 基因增加时耐盐碱能力减弱、AT1 基因剪切后耐盐碱能力增强，运用共变法和求异法探求 AT1 基因与高粱耐盐碱能力之间的因果联系。

## Gate Decision

Add Q0063 to the coverage matrix, source-packet queue, reasoning-form ledger, and reasoning V2 body draft as `source_locked_pending_external_review`.

GAP006 remains open because the 2024 suite-by-suite backlog is not exhausted.
