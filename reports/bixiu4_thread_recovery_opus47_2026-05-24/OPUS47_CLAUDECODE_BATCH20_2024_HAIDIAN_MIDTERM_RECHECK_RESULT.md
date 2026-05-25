# ClaudeCode Batch20 Recheck Result - 2024海淀期中

Parsed from raw stream:

- `OPUS47_CLAUDECODE_BATCH20_2024_HAIDIAN_MIDTERM_RECHECK_STREAM_RAW_UTF8.jsonl`
- `OPUS47_CLAUDECODE_BATCH20_2024_HAIDIAN_MIDTERM_RUNTIME_EVIDENCE.json`

## Result

- `content_result`: `pass`
- `local_policy_result`: `pass_with_model_gate_blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `required_fixes`: none for Batch20 content.

## Evidence Checked

- Matrix coverage: pass. Batch20 has `26` rows, `M0942-M0967`, covering Q1-Q15, Q16(1), Q16(2), Q17, Q18, Q19, Q20, Q21(1), Q21(2), plus three removed Q18 misplacement records.
- Q18 misplacement: pass. Formal rubric places Q18 under 《政治与法治》基层民主, so the old philosophy entries under `系统观念 / 系统优化`, `矛盾的特殊性 / 具体问题具体分析`, and `人民群众` are correctly removed.
- DOCX/PDF clean state: pass. Current DOCX/PDF contain `0/0` mentions of `2024海淀期中`.
- Render manifest: pass. Current render reports `249` PDF pages, `249` page PNGs, label count `2311/2311`, no blank-like pages excluding the cover/foreword, and suite mentions `0/0`.
- Global source gap: pass for this batch. Remaining raw midterm/final suite gap is now `15`.

## Model Evidence Boundary

- Runtime observed model: `claude-opus-4-7`.
- Command lane used `--effort max`.
- Stream contains a thinking block.
- Debug stream also mentions auxiliary `claude-haiku-4-5-20251001`; this is not counted as qualified evidence.
- Machine-readable adaptive/max-effort proof is still insufficient, so the model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## Remaining Project Blockers

- GPTPro web full-artifact review: `real_call_pending`.
- External Claude Opus full-artifact review: `real_call_pending`.
- `15` raw midterm/final suites remain outside the governed coverage system.
- Whole-project final acceptance is not claimed.
