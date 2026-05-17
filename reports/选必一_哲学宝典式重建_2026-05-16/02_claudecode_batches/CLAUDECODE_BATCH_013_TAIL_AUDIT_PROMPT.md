# ClaudeCode Tail Audit Prompt

You are the ClaudeCode production lane for the user's 选必一《当代国际政治与经济》宝典式重建 workflow.

Task: independently audit whether a valid Batch 013 exists after Batch 012.

You are not alone in the codebase. Do not revert or overwrite other work. Write your result to:

`reports/选必一_哲学宝典式重建_2026-05-16/02_claudecode_batches/BATCH_013_CLAUDECODE_TAIL_AUDIT.md`

Use this local workspace:

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible`

Required files to read first:

- `reports/选必一_哲学宝典式重建_2026-05-16/00_control/TAIL_RECONCILIATION_AFTER_BATCH_012.md`
- `reports/选必一_哲学宝典式重建_2026-05-16/01_source_packets/BATCH_001_SOURCE_PACKET.md` through `BATCH_012_SOURCE_PACKET.md`
- `reports/选必一_哲学宝典式重建_2026-05-16/05_governor/BATCH_001_GOVERNOR_FINAL_AUDIT.md` through `BATCH_012_GOVERNOR_FINAL_AUDIT.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md`

Evidence to verify:

- Corpus candidate sweep searched `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts` for 选必一 main-question prompts.
- The only apparently unprocessed tail candidate found so far is `2026丰台期末Q20`, cached at `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\texts\dbc93cbfd3a93eff_2026丰台期末细则.txt:400-418`.
- Its PDF is `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区期末和期中\2026丰台期末\细则\2026丰台期末细则.pdf`.
- Local page check found: page 64 contains Q20 `五大工程`/中拉利益汇合点, page 65 only says knowledge and ability board, page 66 begins a `五年规划` rubric that does not match Q20. Lines 348-390 contain a `四大全球倡议` rubric block that also does not exactly match Q20.

Output requirements:

1. State whether Batch 013 can be formed as a five-question source-locked batch.
2. For `2026丰台期末Q20`, decide whether it can enter the formal main term table under the current source hierarchy.
3. If you find any missed admissible candidate, list the exact source path, line/page, prompt, scoring source, and why it was missed.
4. If no admissible Batch 013 exists, say that clearly and recommend moving to cumulative synthesis/delivery after GPT Pro and Claude Opus review of the closure.

Hard rules:

- Do not invent rubrics.
- Do not use reference answers as formal scoring terms unless they are explicitly confirmed.
- Do not promote mismatched scoring pages into Q20 scoring support.
- Keep the six top-level buckets fixed: 时代背景、理论、经济全球化、政治多极化、中国、联合国.
- Final student-facing entries must require exactly these fields: 术语、完整设问、细则位置、来源、材料触发、答案句.
