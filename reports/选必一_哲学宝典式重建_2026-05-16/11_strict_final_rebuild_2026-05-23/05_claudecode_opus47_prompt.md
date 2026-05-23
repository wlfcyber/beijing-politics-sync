# ClaudeCode Opus 4.7 严格最终版复核与补写任务

你是本项目的 ClaudeCode 独立生产/复核线。当前运行命令会使用 `--model opus --effort max`，请按 Opus 高强度方式工作。

## 工作边界

项目根目录：
`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

只读重点材料：
- `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/04_review_queue.csv`
- `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/04_source_packets/`
- `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/05_codex_first_pass_adjudication.csv`
- `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/01_extraction_log.csv`
- `reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/01_extracted_text/`
- `reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_合并题例_初稿回源拆分审计.md`
- `reports/选必一_哲学宝典式重建_2026-05-16/06_final_handbook/选必一_当代国际政治与经济_主观题术语宝典_学生版.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md`

输出目录：
`reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/05_claudecode_opus47/`

请只在上述输出目录新建/更新文件，不要修改最终宝典正文、不要改脚本、不要改原始材料。

## 硬规则

1. 只做主观题。
2. 主表只能收录选必一《当代国际政治与经济》相关采分点。
3. 主链证据必须来自评分细则、评标、阅卷细则、讲评 PPT/讲评材料。普通参考答案不能冒充主链细则；最多作为降级迁移参考，并标明不能入主表。
4. 题例层面必须单题展示。严禁把两个题合并成一个案例。
5. 对 12 条反合并残留，必须回到初稿/ClaudeCode 独立条目来源重写；不得从终稿合并条目望文生义拆分。
6. 术语必须尽量使用评分源原词；不能为了“好看”自造概括。
7. 分类边界必须遵守：
   - “合作共赢的新型国际关系”属于“政治多极化”，不能放到“理论”。
   - “独立自主和平外交与和平共处五项原则”属于“中国”，不能放到“理论”或“政治多极化”。
   - “经济全球化”内部不能把表述相距很远的术语强行归为同类；即使本质相近，也要看评分源表述和材料触发是否接近。
8. 若题面疑似选必一但没有定位同题细则，判定为 `NEEDS_EVIDENCE`，不要补写进主表。

## 你的任务

请独立复核 `04_review_queue.csv` 的 93 条队列，并结合 `05_codex_first_pass_adjudication.csv`，完成：

1. 逐题裁决：
   - `INCLUDE_STRICT_MAIN`
   - `EXCLUDE_OTHER_MODULE`
   - `NEEDS_EVIDENCE`
   - `DOWNGRADED_REFERENCE_ONLY`
2. 对每条 `INCLUDE_STRICT_MAIN`，写出可直接合入学生版的单题条目草稿，字段必须为：
   - `【细则术语】`
   - `【卷面使用】`
   - `【材料触发点】`
   - `【设问】`
   - `【为什么能想到】`
   - `【答案落点】`
   - `【细则位置】`
   - `【来源】`
3. 对 12 条反合并残留，回读 `选必一_合并题例_初稿回源拆分审计.md` 中列出的原始来源，逐个单题重写；如果某一单题只有普通参考答案或证据不够，明确排除或降级。
4. 输出覆盖风险：哪些题目前疑似选必一但仍缺细则，后续必须继续回源。

## 输出文件

请写入三个文件：

1. `CLAUDECODE_STRICT_ADJUDICATION.md`
   - 93 条队列逐题裁决表。
2. `CLAUDECODE_STRICT_PATCH_ENTRIES.md`
   - 只放 `INCLUDE_STRICT_MAIN` 的可合入单题条目。
   - 按六桶组织：时代背景、理论、经济全球化、政治多极化、中国、联合国。
   - 每条必须单题独立，不得出现标题里用 `；` 合并两个题源。
3. `CLAUDECODE_COVERAGE_RISK_LOG.md`
   - 继续缺细则题、普通答案降级题、其他模块误命中题、你认为 Codex 第一轮误判的地方。

最后在 stdout 简要报告：写入文件路径、`INCLUDE_STRICT_MAIN` 数量、`NEEDS_EVIDENCE` 数量、`EXCLUDE_OTHER_MODULE` 数量、反合并残留中成功重写数量。
