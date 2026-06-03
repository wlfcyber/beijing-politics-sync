# Split Upload Plan For GPTPro / Claude Opus

created_at: 2026-05-21 07:27:48

Use the full zip first if the web UI accepts it:

- `/Users/wanglifei/Desktop/北京高考政治/选必二法律主观题框架_从题源生长/05_reasoner_packets/v7_method_learning_batched_rebuild_20260521.zip`

If the full zip fails, upload in this order:

1. `v7_method_learning_batched_rebuild_20260521_METHOD_PACK.zip`
   - prior framework DNA
   - rendered prior samples
   - current V6.9 candidate and failure-audit files
   - master prompt
2. `v7_method_learning_batched_rebuild_20260521_BATCH_01.zip`
3. `v7_method_learning_batched_rebuild_20260521_BATCH_02.zip`
4. `v7_method_learning_batched_rebuild_20260521_BATCH_03.zip`
5. `v7_method_learning_batched_rebuild_20260521_BATCH_04.zip`

Important:

- Paste `VISIBLE_PROMPT_FOR_WEB_UPLOAD_UTF8_20260521.txt` only once after the method pack or full pack.
- Do not repeatedly press send in Claude. Upload, paste, send once, then wait.
- If a model says it cannot see a batch, upload only the missing batch zip and ask it to continue from the last completed section.
