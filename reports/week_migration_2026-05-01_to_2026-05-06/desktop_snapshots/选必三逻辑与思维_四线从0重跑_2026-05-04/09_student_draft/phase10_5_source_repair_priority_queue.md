# Phase10.5 Source Repair Priority Queue

Status: `LOCAL_PREPARATION_ONLY_NO_PHASE_PROMOTION`

This queue does not authorize expansion. It orders the 45 non-body rows so later GPT/Governor-authorized repair can start from the highest-risk/highest-value rows.

## Counts

- `P0_PROTECTED_HOLD_DO_NOT_EXPAND`: 4
- `P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER`: 3
- `P2_REPAIR_INDEX_CLUSTER`: 10
- `P3_REPAIR_THINKING_OR_CROSS_SOURCE`: 5
- `P4_RECHECK_SUBJECTIVE_REASONING_FORM`: 4
- `P5_RECHECK_CHOICE_REASONING_FORM`: 19

## Queue


### P0_PROTECTED_HOLD_DO_NOT_EXPAND

- `Q-2026顺义一模-3` 2026 顺义一模第3题 | 思维 | 选择题 | refs=3 (Q-2024朝阳一模-9；Q-2025海淀二模-20；Q-2026朝阳期中-20) | hard-lock row; keep absent or index-only until explicit source repair plus later GPT/Governor authorization
- `Q-2025海淀二模-12` 2025 海淀二模第12题 | 思维 | 选择题 | refs=1 (Q-2025丰台期末-7) | hard-lock row; keep absent or index-only until explicit source repair plus later GPT/Governor authorization
- `Q-2024西城一模-11` 2024 西城一模第11题 | 推理 | 选择题 | refs=1 (Q-2024朝阳期中-9) | hard-lock row; keep absent or index-only until explicit source repair plus later GPT/Governor authorization
- `Q-2025海淀二模-13` 2025 海淀二模第13题 | 推理 | 选择题 | refs=0 (none) | hard-lock row; keep absent or index-only until explicit source repair plus later GPT/Governor authorization

### P1_REPAIR_HIGH_VALUE_INDEX_CLUSTER

- `Q-2025东城期末-18-2` 2025 东城期末第18题第(2)问 | 交叉 | 主观题 | refs=5 (Q-2024朝阳一模-7；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2) | already supports several Phase10 same-type links; repair source before any body expansion
- `Q-2026通州期末-9` 2026 通州期末第9题 | 思维 | 选择题 | refs=5 (Q-2024朝阳一模-7；Q-2025海淀期末-18；Q-2025西城二模-16-3；Q-2026东城一模-19-4；Q-2026朝阳期中-21-2) | already supports several Phase10 same-type links; repair source before any body expansion
- `Q-2024朝阳二模-7` 2024 朝阳二模第7题 | 交叉 | 选择题 | refs=3 (Q-2024海淀二模-17-1；Q-2024海淀二模-17-2；Q-2025海淀期末-17-1) | already supports several Phase10 same-type links; repair source before any body expansion

### P2_REPAIR_INDEX_CLUSTER

- `Q-2024朝阳期中-19` 2024 朝阳期中第19题 | 交叉 | 主观题 | refs=2 (Q-2024海淀二模-17-1；Q-2024海淀二模-17-2) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2026通州期末-11` 2026 通州期末第11题 | 交叉 | 选择题 | refs=2 (Q-2024朝阳一模-9；Q-2025海淀二模-20) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2025东城期末-5` 2025 东城期末第5题 | 思维 | 选择题 | refs=2 (Q-2024朝阳一模-9；Q-2025海淀二模-20) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2025海淀期末-2` 2025 海淀期末第2题 | 思维 | 选择题 | refs=2 (Q-2024朝阳一模-9；Q-2025海淀二模-20) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2026通州期末-5` 2026 通州期末第5题 | 思维 | 选择题 | refs=2 (Q-2024朝阳一模-9；Q-2025海淀二模-20) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2026通州期末-8` 2026 通州期末第8题 | 思维 | 选择题 | refs=2 (Q-2024朝阳一模-9；Q-2025海淀二模-20) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2026顺义一模-5` 2026 顺义一模第5题 | 交叉 | 选择题 | refs=1 (Q-2025丰台期末-8) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2026丰台一模-8` 2026 丰台一模第8题 | 推理 | 选择题 | refs=1 (Q-2025西城二模-16-2) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2026朝阳期中-11` 2026 朝阳期中第11题 | 推理 | 选择题 | refs=1 (Q-2026丰台一模-18-2) | already visible as same-type index; repair before deciding whether it deserves body treatment
- `Q-2026朝阳期中-14` 2026 朝阳期中第14题 | 推理 | 选择题 | refs=1 (Q-2024朝阳期中-9) | already visible as same-type index; repair before deciding whether it deserves body treatment

### P3_REPAIR_THINKING_OR_CROSS_SOURCE

- `Q-2026东城一模-6` 2026 东城一模第6题 | 交叉 | 选择题 | refs=0 (none) | thought/cross row absent from body; source-answer locator must be repaired first
- `Q-2026朝阳期中-13` 2026 朝阳期中第13题 | 交叉 | 选择题 | refs=0 (none) | thought/cross row absent from body; source-answer locator must be repaired first
- `Q-2026丰台一模-4` 2026 丰台一模第4题 | 思维 | 选择题 | refs=0 (none) | thought/cross row absent from body; source-answer locator must be repaired first
- `Q-2026丰台一模-7` 2026 丰台一模第7题 | 思维 | 选择题 | refs=0 (none) | thought/cross row absent from body; source-answer locator must be repaired first
- `Q-2026顺义一模-6` 2026 顺义一模第6题 | 思维 | 选择题 | refs=0 (none) | thought/cross row absent from body; source-answer locator must be repaired first

### P4_RECHECK_SUBJECTIVE_REASONING_FORM

- `Q-2024朝阳期中-18` 2024 朝阳期中第18题 | 推理 | 主观题 | refs=0 (none) | subjective row may carry teachable structure, but reasoning form must be rechecked before body use
- `Q-2025丰台期末-18-1` 2025 丰台期末第18题第(1)问 | 推理 | 主观题 | refs=0 (none) | subjective row may carry teachable structure, but reasoning form must be rechecked before body use
- `Q-2025顺义一模-17-1` 2025 顺义一模第17题第(1)问 | 推理 | 主观题 | refs=0 (none) | subjective row may carry teachable structure, but reasoning form must be rechecked before body use
- `Q-2026东城期末-17-2` 2026 东城期末第17题第(2)问 | 推理 | 主观题 | refs=0 (none) | subjective row may carry teachable structure, but reasoning form must be rechecked before body use

### P5_RECHECK_CHOICE_REASONING_FORM

- `Q-2025丰台期末-10` 2025 丰台期末第10题 | 交叉 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2024朝阳二模-6` 2024 朝阳二模第6题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2024朝阳期中-11` 2024 朝阳期中第11题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2024朝阳期中-8` 2024 朝阳期中第8题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2024海淀二模-6` 2024 海淀二模第6题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2024西城一模-13` 2024 西城一模第13题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2025东城期末-14` 2025 东城期末第14题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2025东城期末-15` 2025 东城期末第15题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2025丰台期末-9` 2025 丰台期末第9题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2025海淀期末-8` 2025 海淀期末第8题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2025西城二模-7` 2025 西城二模第7题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2025顺义一模-5` 2025 顺义一模第5题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2025顺义一模-6` 2025 顺义一模第6题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2026东城期末-6` 2026 东城期末第6题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2026东城期末-7` 2026 东城期末第7题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2026丰台一模-9` 2026 丰台一模第9题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2026朝阳期中-12` 2026 朝阳期中第12题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2026朝阳期中-15` 2026 朝阳期中第15题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
- `Q-2026顺义一模-4` 2026 顺义一模第4题 | 推理 | 选择题 | refs=0 (none) | choice row needs reasoning-form or answer-location recheck before any expansion
