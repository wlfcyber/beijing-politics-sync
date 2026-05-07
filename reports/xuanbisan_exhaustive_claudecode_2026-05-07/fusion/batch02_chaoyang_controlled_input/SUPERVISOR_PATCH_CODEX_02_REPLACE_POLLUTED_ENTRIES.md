# Codex Patch 02: replace polluted Batch02 entries

Fusion precheck found that `entries\batch02_entries.jsonl` in this controlled input had structurally present but content-shifted fields:

- `evidence_level` contained reasoning text instead of evidence labels.
- `framework_node` and `answer_sentence` were shifted/truncated for many rows.
- The older structural QA did not catch this because it only checked required field presence.

Correction applied:

- Replaced this controlled input's `entries\batch02_entries.jsonl` with the clean 32-row file from `claudecode_lane\batches\batch02_output_repair\entries\batch02_entries.jsonl`.
- Preserved the repaired `QUESTION_DECISIONS.csv` with 93 rows, including the Codex-added excluded boundary rows for 2026 朝阳期中 19(1)(2)(3).
- Tightened `codex_audit\audit_batch_dir.py` so invalid JSONL `evidence_level` values now fail QA as `invalid_jsonl_evidence_level`.

This patch keeps Batch02 as fusion input only and does not authorize final Word/PDF.
