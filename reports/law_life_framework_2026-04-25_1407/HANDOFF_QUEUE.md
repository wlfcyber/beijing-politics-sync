# Handoff Queue

- On resume, read TASK_BRIEF, USER_FRAMEWORK, DEVELOPMENT_PLAN, PROGRESS, SOURCE_LEDGER, COVERAGE_MATRIX, and this file before acting.

## Cache-First Handoff Update

All running Beijing politics research threads must switch to cache-first mode:

- First read `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\CACHE_FIRST_DIRECTIVE.md`.
- Check `manifest.csv`, `gpt_index.jsonl`, `gpt_sources`, `gpt_suite_bundles`, and `renders` before bulk-converting raw Word/PDF/PPT files.
- Cache-first is not cache-only. If cached text, GPT bundles, rendered pages, or metadata are confusing, incomplete, unreadable, or insufficient for an evidence judgment, return to the original source file.
- When falling back to raw files, record the cache path checked, why it was insufficient, the original file opened, and what evidence was confirmed.
- `自动化检测者` should reject bulk raw conversion that ignored the cache, but should not block targeted raw-file verification when the cache is unclear.
