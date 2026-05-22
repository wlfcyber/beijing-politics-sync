你现在是“选必二《法律与生活》主观题框架从题源生长工程”的恢复复核者。

任务：读取 boundary recovery packet，对 v1 压测中非 PASS 的 33 道题做独立复核。重点判断 Codex 的恢复裁决是否正确：哪些应恢复为选必二法律主观题正文/开放容器，哪些应剔除，哪些必须拆小问或重抽。

硬规则：
1. 不得把参考答案升为评分细则。
2. 不得把必修三、经济、哲学、逻辑题因为有“法律/权利/法治”字样就恢复。
3. 小问混合题必须拆分，不得整题计入。
4. 对每个裁决必须给出 question_id、rubric_atom_id 或 source_locator。
5. 本轮不是重写框架；只复核 recovery_decision。

输出字段：
question_id
model_decision: agree / disagree / uncertain
recommended_status: recover_core / keep_reference_open / split_or_deduplicate / reextract_needed / exclude_nonlaw / exclude_duplicate_mismatch
reason
required_source_check
can_enter_revised_baodian: yes/no/partial
can_support_core_code: yes/no
notes

最后输出：
1. 可恢复正文题清单
2. 只能开放容器题清单
3. 必须剔除题清单
4. 必须重抽/拆分题清单
5. 对 framework_v2 和宝典的修订建议
