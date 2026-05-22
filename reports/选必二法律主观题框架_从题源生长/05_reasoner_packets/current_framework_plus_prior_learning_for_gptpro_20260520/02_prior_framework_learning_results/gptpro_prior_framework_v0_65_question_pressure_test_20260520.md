# GPTPro Prior-Framework v0 65-Question Pressure Test

## Verdict

`CONDITIONAL_PASS_NEEDS_PATCHES`

GPTPro v0 比之前的审计式版本更像学生框架，但仍不能直接升为最终框架。它可以启动多数题，真正的门槛在于：reference_only 锁死、边界综合题不升核心、低频 singleton 只进容器、设问缺失题先回源。

## Corpus

- Questions tested: 65
- Evidence levels: {'formal': 61, 'reference_only': 4}

## Status Counts

- PASS_CANDIDATE: 35
- PARTIAL_SOURCE_CHECK: 18
- PARTIAL_LOW_FREQ_CONTAINER: 5
- PARTIAL_REFERENCE_ONLY: 4
- PARTIAL_BOUNDARY_OPEN: 3

## Node Coverage

- LAW_V0_N03:切责成链: 63
- LAW_V0_N07:补价值: 58
- LAW_V0_N02:先判后证: 47
- LAW_V0_N05:走救济: 42
- LAW_V0_N04:护创新: 29
- LAW_V0_N06:划边界: 26
- LAW_V0_N01:一格一答: 8

## Rows Needing Patch Or Guard

- CC0011_2024_丰台_二模_17: PARTIAL_LOW_FREQ_CONTAINER (low_freq_singleton)
- CC0019_2024_朝阳_一模_19: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0040_2024_海淀_一模_19: PARTIAL_REFERENCE_ONLY (reference_only_lock)
- CC0077_2025_东城_一模_19: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0084_2025_东城_二模_19: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0092_2025_东城_期末_19_1: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0131_2025_房山_一模_19: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0157_2025_朝阳_期末_20: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0162_2025_海淀_一模_18: PARTIAL_REFERENCE_ONLY (reference_only_lock)
- CC0180_2025_海淀_期末_20: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0189_2025_石景山_一模_20: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0195_2025_西城_一模_20: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0213_2025_门头沟_一模_20: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0214_2025_门头沟_一模_20_2: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0245_2026_东城_期末_18_2: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0254_2026_丰台_二模_18: PARTIAL_LOW_FREQ_CONTAINER (low_freq_singleton)
- CC0276_2026_房山_二模_17: PARTIAL_BOUNDARY_OPEN (ask_source_check|formal_boundary_open)
- CC0277_2026_房山_二模_18: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0311_2026_海淀_二模_18_2: PARTIAL_REFERENCE_ONLY (reference_only_lock)
- CC0317_2026_海淀_期末_18: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0318_2026_海淀_期末_18_2: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0319_2026_海淀_期末_19: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0325_2026_石景山_一模_18: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0332_2026_石景山_二模_19: PARTIAL_LOW_FREQ_CONTAINER (low_freq_singleton)
- CC0340_2026_西城_一模_17: PARTIAL_LOW_FREQ_CONTAINER (low_freq_singleton)
- CC0353_2026_西城_期末_17: PARTIAL_REFERENCE_ONLY (ask_source_check|reference_only_lock)
- CC0305_2026_海淀_一模_18_3: PARTIAL_SOURCE_CHECK (ask_source_check)
- CC0380_2026_顺义_二模_18_2: PARTIAL_BOUNDARY_OPEN (ask_source_check|formal_boundary_open)
- RECOVER_2024_东城_一模_19: PARTIAL_LOW_FREQ_CONTAINER (low_freq_singleton)
- RECOVER_2026_西城_二模_18_3: PARTIAL_BOUNDARY_OPEN (formal_boundary_open)

## Promotion Rule

Only `PASS_CANDIDATE` rows may be used to draft core student answer examples, and even those require rubric-atom sentence matching before entering a new宝典. `PARTIAL_*` rows can appear only as reference, boundary, open-container, or teacher caution examples.

## Next Step

Build a revised framework draft from the passing core while writing a separate open-container chapter for partial rows. Do not flatten all 65 into equal full-score templates.
