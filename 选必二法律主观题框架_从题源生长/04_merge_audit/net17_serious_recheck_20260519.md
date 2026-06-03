# Net-17 Serious Recheck - 70 to 53 Gap

- generated_at: 2026-05-19T15:00:00+08:00
- original merged rows: 70
- boundary-patched rows: 53
- important math: 20 original rows were removed from the 70-row table, and 3 new split legal rows were added, so the net difference is 17. Therefore the auditable object is 20 removed original rows, not literally 17 source IDs.

## Bottom Line

The user challenge is partially confirmed. The 53-row package is not source-exhaustive for all non-midterm legal subjective questions. Three non-midterm suites had a non-law row correctly excluded, but a different legal subjective question in the same suite was missed and must be recovered:
- `RECOVER_2024_顺义_二模_17` from `2024 顺义 二模`: 原剔除的 Q19 是国际/经济综合题，剔除本身成立；但同套卷漏掉 Q17 财产制度助力经济社会发展，答案细则涉及财产制度规范民事主体财产关系、物权平等保护、财产权保护。 Evidence: 题面 F0069 lines 112-113；答案/细则 F0068 lines 17-20。
- `RECOVER_2025_海淀_二模_18` from `2025 海淀 二模`: 原剔除的 Q20 共享/粮食安全题剔除成立；但同套卷漏掉 Q18 模拟法庭/恶意抢注/商标权/程序法/证据题。 Evidence: 题面 rendered_pages/F0123/page_006.png；细则 F0121 lines 4-16；讲评 F0120 lines 309-335, 381-386。
- `RECOVER_2026_通州_一模_20` from `2026 通州 一模`: 原剔除的 Q17(2) 是《逻辑与思维》AI 辩证思维，剔除成立；但同套卷漏掉 Q20 民法典自甘风险/安全保障义务/侵权责任题。 Evidence: 题面 rendered_pages/F0173/page_008.png；细则 F0172 lines 215-228。

There are also two pending rows that should remain out of closure until split/dedup source work is done:
- `CC0094_2025_东城_期末_19_3` -> CC0094_2025_东城_期末_19_3_LAW_PENDING: 仍需拆出可能的相邻关系法律层；当前 rubric atoms 串题，不能闭合。
- `CC0118_2025_丰台_期末_18_2` -> CC0118_2025_丰台_期末_18_2_LAW: 当前行绑定经济题；尹某劳动合同给分口径可能与 CC0119 重复，不能新增计数。

Additional red flag found outside the exact removed-row set:
- `题面 rendered_pages/F0208/page_007.png；评标 F0207 lines 180-212。该题不在原70移出行内，但排查时发现应列 uncertain/mixed，而不是默默丢弃。`

## Count Impact

- Current 53 should be downgraded from source-exhaustive closure to boundary-patched release candidate with newly found omissions.
- Minimum corrected candidate count after adding the three clearly missed non-midterm law questions would be 56, before rerunning material/rubric atoms, model observations, framework validation, and handbook sections.
- If `2026丰台期末 Q18` is accepted as mixed legal/open evidence after source review, the visible candidate pool may become 57, but it should not be promoted directly as core evidence because the prompt says 法治知识 and the scoring combines 政治与法治 + 法律与生活.

## Removed Original Rows Rechecked

| source_question_id | stage | old bucket | same-suite kept in 53 | verdict | recover/reopen | note |
| --- | --- | --- | --- | --- | --- | --- |
| `CC0001_2024_丰台_一模_16` | 2024丰台一模 Q16 | excluded | CC0002_2024_丰台_一模_17 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0002；本行 Q16 是《政治与法治》四下基层，ask 串入 CC0002。 |
| `CC0026_2024_朝阳_二模_18` | 2024朝阳二模 Q18 | excluded | CC0025_2024_朝阳_二模_17 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0025；本行主干是全过程人民民主/政治与法治。 |
| `CC0047_2024_海淀_二模_21` | 2024海淀二模 Q21 | excluded | CC0045_2024_海淀_二模_19 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0045；本行是新质/民生综合题，不是法律采分。 |
| `CC0070_2024_顺义_二模_19` | 2024顺义二模 Q19 | excluded | none | recover_needed_missed_same_suite_law | yes RECOVER_2024_顺义_二模_17 | 原剔除的 Q19 是国际/经济综合题，剔除本身成立；但同套卷漏掉 Q17 财产制度助力经济社会发展，答案细则涉及财产制度规范民事主体财产关系、物权平等保护、财产权保护。 |
| `CC0091_2025_东城_期末_19` | 2025东城期末 Q19 | not_counted_parent_unit | CC0092_2025_东城_期末_19_1 | confirmed_parent_not_counted | no  | 父题不应整题计数；同套法律小问 CC0092 已保留，CC0094 另列 pending。 |
| `CC0094_2025_东城_期末_19_3` | 2025东城期末 Q19 | pending_split_not_open | CC0092_2025_东城_期末_19_1 | pending_split_recheck | pending CC0094_2025_东城_期末_19_3_LAW_PENDING | 仍需拆出可能的相邻关系法律层；当前 rubric atoms 串题，不能闭合。 |
| `CC0118_2025_丰台_期末_18_2` | 2025丰台期末 Q18 | duplicate_or_reextract_pending | CC0119_2025_丰台_期末_19 | pending_dedup_reextract | pending CC0118_2025_丰台_期末_18_2_LAW | 当前行绑定经济题；尹某劳动合同给分口径可能与 CC0119 重复，不能新增计数。 |
| `CC0132_2025_房山_一模_20` | 2025房山一模 Q20 | excluded | CC0131_2025_房山_一模_19 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0131；本行奋斗主题综合论述，不是法律规则采分。 |
| `CC0168_2025_海淀_二模_20` | 2025海淀二模 Q20 | excluded | none | recover_needed_missed_same_suite_law | yes RECOVER_2025_海淀_二模_18 | 原剔除的 Q20 共享/粮食安全题剔除成立；但同套卷漏掉 Q18 模拟法庭/恶意抢注/商标权/程序法/证据题。 |
| `CC0182_2025_海淀_期末_22` | 2025海淀期末 Q22 | excluded | CC0180_2025_海淀_期末_20;CC0181_2025_海淀_期末_21 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0180、CC0181；本行愚公精神综合论述，法律片段为串页/干扰。 |
| `CC0218_2025_顺义_一模_16` | 2025顺义一模 Q16 | excluded | CC0223_2025_顺义_一模_19 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0223；本行哪吒/哲学文化题，不是法律题。 |
| `CC0240_2026_东城_二模_21` | 2026东城二模 Q21 | excluded | CC0238_2026_东城_二模_19 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0238；本行金融五篇大文章/经济/辩证思维。 |
| `CC0250_2026_丰台_一模_19` | 2026丰台一模 Q19 | excluded | CC0251_2026_丰台_一模_20 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0251；本行人类命运共同体/2030议程，不应作为法律开放容器。 |
| `CC0259_2026_丰台_期中_19` | 2026丰台期中 Q19 | pending_missing_legal_rubric | none | confirmed_mislocated_duplicate_not_2026_fengtai_midterm | no  | 该材料在 F0207/F0388 中标注为“2024海淀二模”样例，非 2026丰台期中/期末本卷题；对应遗赠扶养协议已由 2024海淀二模 CC0045/相关恢复样本承载，不能按 2026丰台新增计数。 |
| `CC0294_2026_朝阳_二模_20_2` | 2026朝阳二模 Q20 | excluded | CC0289_2026_朝阳_二模_18 | confirmed_exclude_row_only | no  | 同套法律题已保留为 CC0289；本行当代国际政治与经济/人类命运共同体/系统思维。 |
| `CC0305_2026_海淀_一模_18` | 2026海淀一模 Q18 | not_counted_parent_unit | CC0305_2026_海淀_一模_18_3 | confirmed_parent_replaced_by_split | no CC0305_2026_海淀_一模_18_3 | 父题不计；法律小问已拆入 CC0305_2026_海淀_一模_18_3。 |
| `CC0358_2026_通州_一模_17` | 2026通州一模 Q17 | excluded | none | recover_needed_missed_same_suite_law | yes RECOVER_2026_通州_一模_20 | 原剔除的 Q17(2) 是《逻辑与思维》AI 辩证思维，剔除成立；但同套卷漏掉 Q20 民法典自甘风险/安全保障义务/侵权责任题。 |
| `CC0363_2026_通州_期中_19` | 2026通州期中 Q19 | not_counted_parent_unit | CC0364_2026_通州_期中_19_1 | confirmed_parent_duplicate | no CC0364_2026_通州_期中_19_1 | 父题不计；同套法律小问已由 CC0364 承载。 |
| `CC0373_2026_顺义_一模_17` | 2026顺义一模 Q17 | not_counted_parent_unit | CC0373_2026_顺义_一模_18 | confirmed_parent_replaced_by_split | no CC0373_2026_顺义_一模_18 | 旧行首是 Q17 政治题；法律题已重抽为 CC0373_2026_顺义_一模_18。 |
| `CC0380_2026_顺义_二模_18` | 2026顺义二模 Q18 | not_counted_parent_unit | CC0380_2026_顺义_二模_18_2 | confirmed_parent_replaced_by_split | no CC0380_2026_顺义_二模_18_2 | 父题含逻辑与法律小问；法律小问已拆入 CC0380_2026_顺义_二模_18_2。 |

## Required Next Actions

1. Create recovered question rows, material atoms, ask atoms, and rubric atoms for `RECOVER_2024_顺义_二模_17`, `RECOVER_2025_海淀_二模_18`, and `RECOVER_2026_通州_一模_20`.
2. Add `2026丰台期末 Q18` to an `uncertain_mixed_law_boundary` review table, not directly into core closure.
3. Rebuild canonical corpus and sidecars after recovery; do not continue claiming the 53-row package is exhaustive.
4. Keep `CC0094` and `CC0118` pending until split/dedup evidence is locked.

