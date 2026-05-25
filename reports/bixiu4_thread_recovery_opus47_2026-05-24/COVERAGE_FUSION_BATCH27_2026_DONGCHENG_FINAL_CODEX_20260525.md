# Coverage Fusion Batch27 - 2026东城期末

Status: `LOCAL_CLOSED_CONTENT_RENDER_PASS_WITH_MODEL_GATE_BLOCKED`

## Execution Summary

- DOCX backup before Batch27 edit: `C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_baodian_52_base_insert_second_mock_first_mock_audit_2026-05-24\05_delivery\哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24_backup_before_batch27_2026_dongcheng_final_20260525_093130.docx`.
- Existing unregistered DOCX entries recovered: `7`.
- New DOCX entries inserted: `6`.
- Governed DOCX entries for `2026东城期末` after Batch27: `13`.
- Ledger rows added: `13`.
- Accepted JSONL records added: `13`.
- Matrix rows added for `2026东城期末`: `33` total, `13` body rows, `20` boundary rows.
- Global raw-suite remaining gap after Batch27: `8`.

## Placement Verdict

- `2026东城期末` had 7 existing DOCX headings but no recovery-matrix rows; Batch27 repaired that ledger/matrix gap.
- Six new DOCX entries were inserted: Q3 矛盾就是对立统一 objective row; Q4 联系的客观性 and 认识对实践的反作用 objective rows; Q16 意识能动作用 and 价值判断与价值选择; Q21 规律的客观性.
- Q1/Q2/Q5-Q15/Q17-Q20 and non-philosophy parts of Q16/Q21 were registered as boundary exclusions.
- Q19 was explicitly kept out of the philosophy “改革” node because its set question and scoring rules are 《政治与法治》.

## Remaining Gates

- Render QA passed after Batch27 DOCX modification.
- ClaudeCode Opus 4.7 recheck result is `pass`.
- Real runtime evidence was recorded, but model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED` because auxiliary Haiku was observed and max-effort/adaptive proof is not treated as a fully closing gate.
- GPTPro web and external Claude Opus full-artifact review remain `real_call_pending`.
- Whole-project status remains non-final.


## Render QA Result

- Render status: `RENDER_PASS_CONTENT_RECHECK_PASS_MODEL_GATE_BLOCKED`.
- PDF pages/rendered PNGs: `261/261`.
- DOCX/PDF label count: `2447/2447`.
- DOCX/Word-layout visible suite mentions: `13/13`.
- Raw PDF exact text-extraction suite mentions: `0`.
- Hit pages: `29, 44, 60, 69, 74, 123, 137, 195, 231, 243, 257`.
- Manifest: `word_render_qa_20260525_batch27_word/render_manifest.json`.


## ClaudeCode Recheck Result

- Result artifact: `OPUS47_CLAUDECODE_BATCH27_2026_DONGCHENG_FINAL_RECHECK_RESULT.md`.
- `content_result`: `pass`.
- `local_policy_result`: `pass_with_model_gate_blocked`.
- `batch27_status`: `LOCAL_CLOSED_CONTENT_RENDER_PASS_WITH_MODEL_GATE_BLOCKED`.
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- Observed models: `claude-haiku-4-5-20251001, claude-opus-4-7`.
- Debug model mentions: `claude-haiku-4-5-20251001, claude-opus-4-7`.
- Whole-project status remains non-final.
