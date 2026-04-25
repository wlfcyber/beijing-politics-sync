# Cache-First Directive For Running Threads

All Beijing politics research threads should use this cache before opening or converting raw Word/PDF/PPT files.

Cache root:

`C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus`

Use:

- `manifest.csv` / `manifest.jsonl` for source-level lookup.
- `gpt_index.jsonl` for GPT-friendly source routing.
- `gpt_sources\*.md` for one source file with metadata and extracted text.
- `gpt_suite_bundles\*.md` for all cached materials in one suite.
- `texts\*.txt` for programmatic search.
- `renders\<hash>\page_*.png` for scan-only PDF pages already rendered.

Rules:

1. Check the cache before converting raw files.
2. Do not re-render or re-convert files whose `sha256` row already exists and whose status is usable.
3. Use raw files only when the cache is missing, changed, or insufficient for a specific evidence judgment.
4. Record cache usage in the worker report, handoff queue, or decision log.
5. `自动化检测者` should reject bulk raw-file conversion that ignores this cache.

Fallback rule:

The cache is the first place to look, not the final authority. If a thread cannot understand the cached text, GPT bundle, rendered page, or metadata well enough to make a reliable teaching/research judgment, it should return to the original source file. Record the cache path checked, the problem, and the original file used.

Resume prompt for another Codex thread:

```text
继续当前政治教研任务，但立即切换为 cache-first 模式。

先读：
C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\CACHE_FIRST_DIRECTIVE.md
C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\manifest.csv
C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_index.jsonl

以后不得在未检查缓存的情况下批量重新转换 Word/PDF/PPT。
优先使用 gpt_suite_bundles 和 gpt_sources；扫描 PDF 用 renders 里的页面图。
如果缓存内容看不懂、不完整、或不足以支撑证据判断，回原始文件查证，并记录原因。
继续推进原任务，并在 HANDOFF_QUEUE.md 或 DECISION_LOG.md 记录已切换为 cache-first。
```
