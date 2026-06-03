# V7 Method-Learning-First Batched Rebuild Packet

created_at: 2026-05-21 07:27:48

This packet answers the user's newest correction:

> 让 GPT 和 Claude 先学会怎么做，把我的框架发给他们让他们学习后再创建新的。可以分批上传题。

## How to use

1. Upload this zip to GPT-5.5 Pro and Claude Opus 4.7 Adaptive in separate fresh chats.
2. Paste `VISIBLE_PROMPT_FOR_WEB_UPLOAD_UTF8_20260521.txt`.
3. If the web UI displays garbled text, paste `VISIBLE_PROMPT_ASCII_FALLBACK_20260521.txt` and tell the model to read the UTF-8 md files inside the zip.
4. Require the model to output all required sections in the prompt.

## Contents

- `prior_framework_learning/`: extracted DNA and rewrite spec from the user's prior strong frameworks.
- `rendered_prior_samples/`: visual samples from prior framework PDFs.
- `current_law_candidate/`: current V6.9 candidate and QA/audit files, to criticize rather than accept.
- `evidence_full/`: full evidence CSVs for back-reference.
- `batches/`: four legal question batches.
- `BATCH_MANIFEST.csv`: batch counts.
- `CURRENT_LAW_CORPUS_STATS.md/json`: 65-question corpus stats.

## Status

This is a handoff packet. It does not itself count as GPTPro or Claude Opus response.
Until the real web/app outputs are captured, mark the external model gate as `real_call_pending`.
