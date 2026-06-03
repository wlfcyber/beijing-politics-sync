# REASONING_SAMPLE_PROMPT_BACKFILL_AUDIT_20260525

audit_time: 2026-05-25T23:54:48+08:00

verdict: `PARTIAL_LOCK_7_OF_8_THEN_RESOLVED_BY_BATCH2`

本文件只审计样章中推理主观题的 `【设问】` 回源状态。初始结论：8 个占位中 7 个已锁定为原卷原句，1 个只能锁到评分细则口径。后续 2026-05-26T00:48:00+08:00 已由 `06_candidate_audit/REASONING_REMAINING_PROMPT_LOCK_BATCH2_20260526.md` 用页图锁定并回填。

## 锁定清单

| 样章条目 | 状态 | 已写入样章的设问 | 回源位置 |
| --- | --- | --- | --- |
| 2024朝阳一模 Q20(1) | `locked` | 推理一属于哪种推理类型？其成立的理由是什么？（5分） | `data/preprocessed_corpus/gpt_sources/25b655e73b7424e7_202404朝阳高三一模试题.md:238` |
| 2025西城二模 Q16(2) | `locked` | 工作人员在某雨水收集池同时观察到雕鸮和红嘴蓝鹊，能否确定此时一定有岩松鼠活动？解释推理过程。（4分） | `data/preprocessed_corpus/gpt_sources/06c08602a2f5c20b_2025北京西城高三二模政治_教师版.md:192-197` |
| 2024朝阳一模 Q20(2) | `locked` | 根据材料二，补充完整推理二。（4分） | `data/preprocessed_corpus/gpt_sources/25b655e73b7424e7_202404朝阳高三一模试题.md:239-241` |
| 2026通州期末 Q19(2) | `locked` | 根据材料，判断推理①和②的逻辑正误，并结合《逻辑与思维》知识说明理由。 | `data/preprocessed_corpus/gpt_sources/7f3083ea306ea1e9_2026北京通州高三_上_期末政治_教师版.md:226-233` |
| 2026东城期末 Q17(2) / 三段论 | `locked` | 运用形式逻辑知识，论证三项主张是否符合逻辑。（6分） | `data/preprocessed_corpus/gpt_sources/15664381470d8300_2026北京东城高三_上_期末政治_教师版.md:210-218` |
| 2024朝阳期中 Q18 | `locked` | 阅读材料，运用《逻辑与思维》相关知识，分别评析楚王和晏子的推理。 | `data/preprocessed_corpus/gpt_sources/0a50f76fd1e1c50f_202411朝阳高三政治_期中1试题.md:198-206` |
| 2026东城期末 Q17(2) / 矛盾律 | `locked` | 运用形式逻辑知识，论证三项主张是否符合逻辑。（6分） | `data/preprocessed_corpus/gpt_sources/15664381470d8300_2026北京东城高三_上_期末政治_教师版.md:210-218` |

## 当时未锁项（后续已解决）

| 样章条目 | 状态 | 当前证据 | 处理 |
| --- | --- | --- | --- |
| 2026海淀一模 Q17(1) | `resolved_by_batch2` | 原先只锁到 `data/preprocessed_corpus/gpt_sources/9b5ac8fd0cfe59cb_2026海淀一模细则.md:35-38`；后续已用页图锁定原卷设问与问卷选项。 | 已在候选稿中回填原卷设问，详见 `06_candidate_audit/REASONING_REMAINING_PROMPT_LOCK_BATCH2_20260526.md`。 |

后续裁决：2026海淀一模 Q17(1) 原卷页图已锁定真实设问为 `运用《逻辑与思维》知识，指出上述调查问卷中的逻辑错误。（2分）`，并锁定问卷问题1、问题2选项，详见 `06_candidate_audit/REASONING_REMAINING_PROMPT_LOCK_BATCH2_20260526.md`。

## 门禁结论

- 可以删除 7 个“本题设问需回源锁定”的泛占位。
- 2026海淀一模 Q17(1) 已经由后续页图锁定，不再是当前 prompt blocker。
- 推理宝典全书扩展前，必须把所有主观题做同等级别 prompt lock；选择题还必须锁定完整题干、完整选项和答案。
