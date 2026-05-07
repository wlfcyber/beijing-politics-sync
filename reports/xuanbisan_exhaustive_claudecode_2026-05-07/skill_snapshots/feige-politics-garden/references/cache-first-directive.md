# Cache-First Directive

Use this directive for any new or running Beijing politics teaching/research thread.

## Mandatory Rule

Before reading or converting raw Word/PDF/PPT files, inspect the reusable preprocessed corpus cache:

- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.csv`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.jsonl`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_index.jsonl`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_suite_bundles`
- `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders`

The cache currently contains source-level packets for all supported 2024/2025/2026 mock-exam files. Use the cached text and suite bundles as the first-read layer.

## How To Use

1. Read `manifest.csv` or `gpt_index.jsonl` to find relevant source files.
2. Prefer `gpt_suite_bundles\*.md` when a worker needs all materials for a suite.
3. Prefer `gpt_sources\*.md` when a worker needs one exact source file with metadata.
4. Use `texts\*.txt` for programmatic search and extraction.
5. Use `renders\<hash>\page_*.png` for scan-only PDFs marked `rendered-ocr-needed`.

Return to raw Office/PDF files only when:

- the source is missing from the cache,
- the file hash changed,
- the cache status explicitly requires repair,
- or the cached text/page image is insufficient for a specific evidence judgment.
- the worker cannot confidently understand the cached packet, bundle, or rendered page.

Do not get stuck trying to interpret a bad cache representation. The cache is a fast first-read layer, not a substitute for source verification. If using the cache would create ambiguity or a weak evidence chain, open the original file and record the reason.

## Thread Compliance

For running long tasks, append a note to `HANDOFF_QUEUE.md` and `DECISION_LOG.md` stating that the thread has switched to cache-first mode.

`自动化检测者` must reject any worker batch that performs bulk raw-file conversion without first checking the preprocessed cache.

Worker reports should cite cache paths alongside original source paths when they rely on cached text or rendered pages.

If a worker falls back to the raw file, the report must say:

- what cache path was checked,
- why it was insufficient,
- which original source file was opened,
- what evidence was confirmed from the original.
