# Beijing Politics Preprocessed Corpus

This directory is the reusable first-read cache for all book/module workflows.

- `manifest.csv`: source-level cache manifest with file hash, status, text path, render path, and GPT markdown path.
- `manifest.jsonl`: same data as JSON Lines for programmatic filtering.
- `texts/`: raw extracted UTF-8 text, one file per source hash.
- `renders/`: cached page images for scan-only PDFs that need OCR or visual reading.
- `gpt_sources/`: one Markdown packet per source file, with metadata and extracted text.
- `gpt_suite_bundles/`: one Markdown packet per suite folder, combining papers, answer keys, rubrics, reports, and lectures.
- `gpt_index.jsonl`: compact GPT-facing index of source markdown and suite membership.

For a new book/module, read `manifest.csv` or `gpt_index.jsonl` first. Return to raw Office/PDF files only when the source hash changed or the cache status requires OCR/conversion repair.
