# ClaudeCode Batch 013 Tail Production Prompt

你是 ClaudeCode 生产线。请基于下列源包，对 `2026朝阳期末Q20` 做独立选必一术语入链稿，并检查 Codex 初稿是否有概念错误、分桶错误、漏点或把参考答案冒充细则的问题。

工作目录：

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

必须读取：

- `reports\选必一_哲学宝典式重建_2026-05-16\01_source_packets\BATCH_013_SOURCE_PACKET.md`
- `reports\选必一_哲学宝典式重建_2026-05-16\02_codex_batches\BATCH_013_CODEX_DRAFT.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md`

硬规则：

1. 每个条目必须保留六字段：`术语、完整设问、细则位置、来源、材料触发、答案句`。
2. `术语` 必须来自 Q20 阅卷细则原词，不要自造概括。
3. 六桶固定为：`时代背景`、`理论`、`经济全球化`、`政治多极化`、`中国`、`联合国`。不要改名为“世界多极化”。
4. `答案句` 必须像学生卷面答案，不要写后台制作语言。
5. `2026丰台期末Q20` 仍是 blocked_prompt_only，不得入正式条目。

请输出并写入：

`reports\选必一_哲学宝典式重建_2026-05-16\02_claudecode_batches\BATCH_013_CLAUDECODE_DRAFT.md`

输出结构：

1. 独立结论：是否同意 `2026朝阳期末Q20` 正式入链。
2. 对 Codex 初稿的修改意见。
3. 你自己的最终建议条目。
4. 对 `2026丰台期末Q20` 的阻断确认。

