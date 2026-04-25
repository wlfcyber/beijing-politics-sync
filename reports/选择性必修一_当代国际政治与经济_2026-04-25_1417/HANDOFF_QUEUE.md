# Handoff Queue

No open evidence-processing blockers remain in the current run.

## Closed Items

- OCR/protected-source bucket closed: 20 scan PDFs OCR-reviewed; 1 selected-compulsory-three old `.doc` excluded by module boundary.
- Choice-question bucket closed: 148 wrong-option trigger rows generated and entered into coverage.
- Former 国家安全 framework blocker closed: anchored to 2024朝阳一模21, with only the selected-compulsory-one mixed-question portion retained.
- Candidate sweep merged: hard scoring sources from OCR and mapper reports were merged or explicitly excluded.

## Remaining Action

- Await final Governor rerun and update `FINAL_ACCEPTANCE_REPORT.md` from ready state to final pass/fail.

## Cache-First Handoff Update

All running Beijing politics research threads must switch to cache-first mode:

- First read `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\CACHE_FIRST_DIRECTIVE.md`.
- Check `manifest.csv`, `gpt_index.jsonl`, `gpt_sources`, `gpt_suite_bundles`, and `renders` before bulk-converting raw Word/PDF/PPT files.
- Cache-first is not cache-only. If cached text, GPT bundles, rendered pages, or metadata are confusing, incomplete, unreadable, or insufficient for an evidence judgment, return to the original source file.
- When falling back to raw files, record the cache path checked, why it was insufficient, the original file opened, and what evidence was confirmed.
- `自动化检测者` should reject bulk raw conversion that ignored the cache, but should not block targeted raw-file verification when the cache is unclear.
