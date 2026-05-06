# Batch 02 Merge Register Updates

Status: `candidate_with_fixes`

Inputs:

- `codex_lane/agents/worker/worker_batch02_entries.md`
- `codex_lane/agents/worker/worker_batch02_source_notes.csv`
- `codex_lane/agents/patcher/patcher_batch02_review.md`
- `codex_lane/agents/governor/governor_batch02_gate.md`

## Gate Result

Batch02 may enter fusion atoms and merge register updates. It is still not final, not coverage closed, and not a student handout. Claude Opus teaching-text review remains uncaptured.

## New / Updated Merge Groups

### M15 当前国际竞争的实质 + 创新驱动战略

- Main bucket: `理论`
- Core name: `当前国际竞争的实质是以经济和科技实力为基础的综合国力较量；坚持创新驱动战略`
- Sources:
  - 2026朝阳一模 Q20, P0, 第①点 2分(1+1) 必答点.
- Guardrail:
  - Do not replace this with the result phrase `全球产业链供应链稳定`; that phrase can appear in answer sentence only.

### M16 推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展

- Main bucket: `经济全球化`
- Core name: `推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展`
- Sources:
  - 2026朝阳一模 Q20, P0, full wording.
  - 2026顺义一模 Q20, P0, variant `经济全球化方向：普惠、平衡、共赢`.
- Rule:
  - The shorter 顺义 wording is expression accumulation only.
  - Never collapse this core into `经济全球化正确方向`.

### M17 贸易投资自由化便利化

- Main bucket: `经济全球化`
- Core name: `推动贸易投资自由化便利化`
- Sources:
  - 2026朝阳一模 Q20, P0.
- Related but separate:
  - `促进人才、商品、服务和生产要素在全球范围内流动` is a factor-flow mechanism and may later merge with a factor-flow core if additional rubrics support it.

### M18 共同利益是国家合作的基础

- Main bucket: `理论`
- Core name: `共同利益`
- Sources:
  - 2026顺义一模 Q20, P0, 必答 1分.
- Non-merge:
  - Do not merge with `正确义利观`. Common interests explain why cooperation can happen; correct义利观 is China's value orientation in cooperation.

### M19 联合国地位和作用

- Main bucket: `联合国`
- Core name: `联合国是当今世界最具普遍性、代表性和权威性的政府间国际组织；集体安全机制的核心；实践多边主义的最佳场所`
- Sources:
  - 2025海淀二模 Q21, `P1 structured scoring answer + P0 marking-record support`, 2分任意两条.
- Guardrail:
  - Not pure P0 frequency unless Governor later upgrades source type. Keep the conservative label.

### M20 联合国对中国的贡献

- Main bucket: `联合国`
- Core name: `联合国对中国的对外开放和现代化事业作出了独特贡献，成为中国开展多边合作的主要舞台`
- Sources:
  - 2025海淀二模 Q21, `P1 structured scoring answer + P0 marking-record support`.
- Student use:
  - Students need the meaning, not necessarily the exact long sentence.

### M21 中国的联合国身份与国际格局地位

- Main bucket: `中国`
- Core name: `中国作为联合国创始会员国/安理会常任理事国；世界上最大的发展中国家/国际政治经济格局中的重要力量`
- Sources:
  - 2025海淀二模 Q21, `P1 structured scoring answer + P0 marking-record support`.

## Updates To Existing Groups

### M01 和平与发展仍是时代主题

Add variants:

- 2026朝阳一模 Q20: `中国的做法符合时代主题和平与发展`
- 2026顺义一模 Q20: `时代主题：和平和发展（世界大势）`

Do not merge with:

- `维护世界和平、促进共同发展` as China diplomacy宗旨.

### M03 国际秩序方向 / 新型国际关系

Add variants:

- 2026朝阳一模 Q20: `推动建设合作共赢的新型国际关系`
- 2026顺义一模 Q20: `新型国际关系：合作共赢 / 互利共赢 / 共享发展成果`

Do not merge with:

- `共同利益`, which belongs to M18.

### M04 联合国宪章 / 联合国体系

Add:

- 2025海淀二模 Q21: `坚定维护以联合国为核心的国际体系；维护《联合国宪章》宗旨和原则`

Evidence caveat:

- Keep `P1 structured scoring answer + P0 marking-record support`; not pure P0.

### M05 / M06 / M07 中国外交价值与贡献

Add sources:

- 2026朝阳一模 Q20:
  - correct义利观 / 中国智慧中国方案 / 大国担当.
  - HMC.
- 2026顺义一模 Q20:
  - HMC / independent peace diplomacy / diplomacy purpose / 义利观 are same scoring-function alternatives.
- 2025海淀二模 Q21:
  - contribution of Chinese wisdom and Chinese solution point contains global governance, new type IR, common values, correct义利观, HMC.
- 2025海淀期末 Q22:
  - P2 optional HMC / Chinese wisdom and solution only.

Counting rule:

- Same scoring slot variants do not inflate frequency across M05/M06/M07.
- P2 optional knowledge does not inflate P0 frequency.

### M12 两个市场两种资源

Add:

- 2026朝阳一模 Q20, P0 `两个市场、两种资源`.

## Explicit New Non-Merges

| non_merge_id | Do Not Merge | Reason |
|---|---|---|
| NM07 | 顺义 `共同利益` with `正确义利观` | Cooperation basis vs China value orientation. |
| NM08 | 朝阳 `坚持共商共建共享` with 通州 `共商共建共享的全球治理观` | Open cooperation/development-potential context vs global governance view. |
| NM09 | 顺义 `普惠、平衡、共赢` as its own core | Must merge under full `开放、包容、普惠、平衡、共赢` wording. |
| NM10 | 2025海淀期末 Q22 P2 optional knowledge with P0 mandatory core | P2 optional short-essay knowledge cannot become P0 frequency or mandatory point. |

## Batch 02 Draft Gate

Allowed:

- Use `scoring_atom_table_batch02.csv` to prepare an internal `section_batch_draft_for_external_review`.

Forbidden:

- Student final.
- Word/PDF.
- Coverage closed.
- Pure P0 upgrade of 2025海淀二模 Q21.
- P0 upgrade of 2025海淀期末 Q22.
- Claimed Claude Opus review.

