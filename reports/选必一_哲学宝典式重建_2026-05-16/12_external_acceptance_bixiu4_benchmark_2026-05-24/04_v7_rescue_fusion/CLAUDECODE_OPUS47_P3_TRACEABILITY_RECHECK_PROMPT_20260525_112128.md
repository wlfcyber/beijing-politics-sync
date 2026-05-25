你是飞哥政治庄园选必一项目的 ClaudeCode 生产 B 线复核员，不是普通 reviewer。

本轮任务是对 Codex P3 局部修复做独立复核。请只依据本地文件，不要凭空补结论。

需要读取的文件：

1. 最终学生版：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\选必一_当代国际政治与经济_主观题术语宝典_学生版_FINAL_20260525.md`

2. 本轮根因修复记录：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\P3_ROOT_CAUSE_AND_SCOPE_REPAIR_20260525_112128.md`

3. 本轮未回连标题证据调和表：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\12_external_acceptance_bixiu4_benchmark_2026-05-24\04_v7_rescue_fusion\P3_UNMATCHED_HEADING_SOURCE_RECONCILIATION_20260525_112128.md`

4. 相关旧批次 source ledger：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\00_control\SOURCE_LEDGER_BATCH_001.csv`
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\00_control\SOURCE_LEDGER_BATCH_002.csv`
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\00_control\SOURCE_LEDGER_BATCH_005.csv`
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\00_control\SOURCE_LEDGER_BATCH_011.csv`
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\选必一_哲学宝典式重建_2026-05-16\00_control\SOURCE_LEDGER_BATCH_013.csv`

5. 原始/缓存文本用于核对顺义 Q19(3)错误来源：
`C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts\8d19592ca0679f21_2026顺义一模.txt`
`C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts\de758e5e79500dd0_2026顺义一模细则.txt`

请完成以下判断：

1. P3 删除 `2026顺义一模Q19(3)` 是否正确？请说明它为什么不应留在选必一学生主链。
2. 最终学生版是否已经不含 `2026顺义一模Q19(3)`、`2026石景山期末`、`TODO/FIXME/待补/待核`？
3. `人才是综合国力竞争和自主创新的关键资源` 频次改为 `出现1次` 是否与正文独立题例一致？
4. P3 未回连标题证据调和表中列出的 23 个当前标题，是否都能在旧 source ledger 中找到对应来源或被标注为边界/参考证据？
5. 是否还发现明显把非选必一设问或错误题号塞入学生主链的问题？如果有，请列出精确标题和理由；如果没有，请写明你抽检了哪些模式。

输出格式：

```
VERDICT: PASS / PASS_WITH_RISKS / FAIL
MODEL_LANE: ClaudeCode Opus 4.7 production-lane recheck

1. deletion_verdict
2. final_text_sanity
3. frequency_check
4. source_reconciliation_check
5. remaining_risks
6. must_fix_now
```

注意：
- 不要新增正文。
- 不要把 GPT/Claude 外部网页审核说成已经完成。
- 如果只能确认本地 ClaudeCode 复核，请明确写 `external GPT Pro / Claude App gates still pending`。
