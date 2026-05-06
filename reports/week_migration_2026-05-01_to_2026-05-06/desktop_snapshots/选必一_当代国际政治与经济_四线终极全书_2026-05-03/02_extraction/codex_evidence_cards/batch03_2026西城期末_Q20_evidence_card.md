# Batch 03 Evidence Card: 2026西城期末 Q20

Status: `codex_local_visual_recheck_pre_worker`

This card records Codex total-control extraction from visually checked local sources. It is not a student handout and does not replace the Worker/Patcher/Governor loop.

## Source Lock

- Question: 2026西城期末 Q20.
- Full prompt: `结合材料，运用《国际政治与经济》知识，阐释参与全球气候治理的中国实践。`
- Paper source: teacher PDF page 8, rendered locally.
- Scoring source: formal scoring PDF pages 4-5, rendered and visually read locally.
- Evidence level: `P0_formal_scoring_rule_visual`.
- Boundary: teacher-paper answer text can help wording, but scoring atoms come from the visual scoring rule only.

## Material Triggers

- China submitted its 2035 NDC target to the United Nations.
- NDC is the core of the Paris Agreement and is submitted every five years.
- Table fields include energy structure, forest carbon sink, greenhouse-gas reduction, green transport, market mechanism, and climate adaptation.
- Materials show climate governance as a global non-traditional security/governance issue requiring multilateral cooperation.

## Scoring Structure

### Angle 1: 中国实践是什么, 2 points

- Role: `建设者 / 引领者 / 做负责任的大国`, 1 point.
- Practice: `坚持绿色发展 / 新发展理念，有为政府 + 有效市场`, 1 point.

### Angle 2: 中国为什么要参与该实践, 3 points, 4 choose 3

- International background: `和平发展合作共赢是时代潮流 / 非传统安全威胁`, 1 point.
- Cooperation basis: `共同利益`, 1 point.
- China concepts: `命运共同体 / 全人类共同价值 / 正确义利观 / 共商共建共享 / 践行真正的多边主义 / 坚持互利共赢`, 1 point.
- Duty and responsibility: `自觉履行国际义务 / 遵循国际法 / 承担国际责任`, 1 point.

Counting rule: these four items are alternatives under a 3-point 4-choose-3 scoring area. The six expressions inside `China concepts` are same-slot variants and must not inflate frequency.

### Angle 3: 实践效果怎么样, 3 points

- International effect: `促进全球可持续发展 / 建设清洁世界`, 1 point.
- Governance effect: `维护联合国的核心作用 / 完善全球治理体系`, 1 point.
- China contribution: `贡献中国智慧 / 中国力量`, 1 point.

## Six-Bucket Placement

| scoring atom | main bucket | cross bucket | placement note |
|---|---|---|---|
| 建设者 / 引领者 / 做负责任的大国 | 中国 | 时代背景 | China role in global climate governance; do not turn into a generic major-country slogan. |
| 坚持绿色发展 / 新发展理念，有为政府 + 有效市场 | 中国 | 经济全球化 | Record as practice support in global climate governance, not a central book-one economic core. |
| 和平发展合作共赢是时代潮流 / 非传统安全威胁 | 时代背景 | 理论 | Same climate-governance reason slot; keep as background trigger. |
| 共同利益 | 理论 | 中国 | Cooperation basis; do not merge with correct义利观. |
| 命运共同体 / 全人类共同价值 / 正确义利观 / 共商共建共享 / 真正的多边主义 / 互利共赢 | 中国 | 政治多极化; 联合国 | Same scoring slot variants under China's global-governance concepts. |
| 自觉履行国际义务 / 遵循国际法 / 承担国际责任 | 中国 | 联合国 | Responsibility and international-law duty; separate from HMC value slot. |
| 促进全球可持续发展 / 建设清洁世界 | 中国 | 时代背景 | Effect of practice; usable as answer result, not independent mandatory theory. |
| 维护联合国的核心作用 / 完善全球治理体系 | 联合国 | 中国 | Keep UN core role explicit; do not generalize to all international organizations. |
| 贡献中国智慧 / 中国力量 | 中国 | 联合国 | Merge with existing China-contribution group as a climate-governance variant. |

## Candidate Student Answer Skeleton

中国积极参与全球气候治理，是全球气候治理的建设者、引领者，展现负责任大国担当。中国围绕能源结构、碳汇、减排、绿色交通、市场机制和气候适应提出 NDC 目标，坚持绿色发展理念，把有效市场和有为政府结合起来推进绿色低碳转型。

气候变化属于需要各国共同应对的全球性问题。中国参与气候治理，顺应和平、发展、合作、共赢的时代潮流，回应各国共同利益，也体现人类命运共同体理念、真正的多边主义和互利共赢要求。中国提交并落实 NDC，是自觉履行国际义务、遵循国际法、承担国际责任的表现。

中国实践有利于促进全球可持续发展、建设清洁美丽世界，也有利于维护联合国在国际事务中的核心作用、完善全球治理体系。中国以自身行动为全球气候治理贡献中国智慧和中国力量。

## Merge Guardrails

- `共同利益` stays as cooperation-basis theory, not correct义利观.
- `共商共建共享` in this question belongs to the China-concepts scoring slot for global climate governance, not the same count as a separate open-cooperation point.
- `维护联合国的核心作用` can update the UN-system group, but it should remain explicit and cannot be replaced by generic `多边主义`.
- `绿色发展 / 新发展理念 / 有为政府 + 有效市场` is a scoring atom in this question, but final book-one promotion needs boundary wording because parts are cross-module.
- `促进全球可持续发展 / 建设清洁世界` should be used as result language unless more rubrics make it a reusable core.
