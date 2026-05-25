# OPUS47 ClaudeCode Batch17 Recheck Result - 2025门头沟一模

Timestamp: 2026-05-25 05:56 +08  
Lane: ClaudeCode production lane  
Raw evidence: `OPUS47_CLAUDECODE_BATCH17_2025_MENTOUGOU_YIMO_RECHECK_STREAM_RAW_UTF8.jsonl`

## Gate Summary

| field | value |
|---|---|
| model_gate | `BLOCKED_MODEL_CONFIRMATION_REQUIRED` |
| content_result | `pass_with_notes` |
| sonnet_haiku_used | `no` |
| answer_key_check | `pass` |
| matrix_check | `pass` |
| docx_check | `pass` |
| render_check | `pass` |
| required_fixes | none blocking |

## Model Gate

The raw stream and debug log identify `claude-opus-4-7`; the command was run with `--model claude-opus-4-7 --effort max`, and the stream contains thinking blocks. The runtime still does not expose machine-readable proof that adaptive thinking/max effort was active, so the local policy keeps this batch at `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

No Sonnet, Haiku, or model-unknown output is counted as qualified evidence. Debug/model mentions include `claude-haiku-4-5-20251001` only as auxiliary/runtime usage, not as accepted evidence.

## Content Result

ClaudeCode content result is `pass_with_notes`.

- Answer key verified: `1C 2A 3B 4A 5D 6C 7C 8B 9A 10A 11B 12B 13B 14D 15D`.
- Matrix verified: `2025门头沟一模` has 30 rows and 0 open-ish rows.
- Current DOCX verified: suite mentions 10; Q6=1, Q7=1, Q16=4, Q21=4.
- Render decision verified: no DOCX/PDF body changed in Batch17, so Batch16 render evidence remains controlling.

## Boundary Checks

- Q6 and Q7 are objective-choice answer-key chains only; they are not treated as subjective scoring-rule evidence.
- Q16 is already covered in the current DOCX under the formal scoring-rule-supported philosophy add-on points: 联系、发展、对立统一、价值判断与价值选择. No duplicate insertion was made.
- Q21(1) remains excluded as selected-compulsory-3 scientific thinking.
- Q21(2) remains existing DOCX coverage only under secondary-module support. It is not upgraded into point-by-point main-chain scoring-rule evidence.
- Q1-Q5 except Q6/Q7, Q8-Q15, and Q17-Q20 are source-reviewed module boundaries or old term-hit false positives.

## Remaining Blockers

- Model proof: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
- GPTPro web full-artifact review: `real_call_pending`.
- External Claude Opus full-artifact review: `real_call_pending`.

This file does not assert final strict acceptance.
