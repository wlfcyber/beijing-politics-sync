# Opus 4.7 ClaudeCode Final-Only Recheck Prompt - Batch16 2026丰台一模

Runtime target remains Claude Opus 4.7, max effort, adaptive thinking. If runtime evidence cannot machine-prove max effort/adaptive thinking, set `model_gate` to `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

Do not call tools. Produce only the required Markdown result.

The full tool-bearing Batch16 ClaudeCode attempt was launched with:

`claude -p --model claude-opus-4-7 --effort max --permission-mode auto --output-format stream-json --verbose --debug-file ... --no-session-persistence`

It produced raw stream evidence under:

`reports\bixiu4_thread_recovery_opus47_2026-05-24\OPUS47_CLAUDECODE_BATCH16_2026_FENGTAI_YIMO_EVIDENCE_PACKET_STREAM_RAW_UTF8.jsonl`

The stream shows `model: claude-opus-4-7`, thinking blocks/signatures, and content-bearing verification messages. It also shows the run exceeded the local 300-second wrapper before it could emit the final report. During that attempt, the production lane verified:

- DOCX heading counts match exactly: Q4=1, Q5=2, Q6=1, Q16=8, Q21=3, total 15.
- Source verification passes against the answer-version PDF and source packet.
- Render verification passes; page 2 is an intentional “前言” divider, not a blank defect.
- Page 182 visually confirms the new Q4 entry renders correctly.
- The lane stated: “All checks pass. Writing the final report.”

Codex-side evidence to be reflected:

- Answer key: `1B 2A 3D 4A 5A 6D 7B 8C 9D 10C 11D 12B 13A 14A 15C`.
- Q4 answer A entered only under `实践是认识的基础`; correct item ② is 选必三综合思维 and not counted as a 必修四哲学 node.
- Q5 answer A entered under `根据固有联系建立新的具体联系` and `认识对实践的反作用`.
- Q6 answer D entered under `联系的多样性`; item ④ is culture/aesthetic support only.
- Q1-Q3, Q7-Q15, Q17-Q20 are module boundaries and not inserted.
- Q16 early blocked/unknown rows are resolved by source review and existing final-DOCX registrations; not duplicated.
- Q21 is registered as existing DOCX coverage only, with evidence `answer-version reference answer + broad PPT angle`; not upgraded to point-by-point scoring-rule evidence.
- Matrix has 33 `2026丰台一模` rows and 0 open-ish rows for this suite.
- Ledger/accepted contain 15 `2026丰台一模` records.
- Render manifest: PDF pages/rendered PNG = `247/247`; label count DOCX/PDF = `2292/2292`; Q4/Q5/Q6 headings located on pages `182`, `60/184`, and `63`; Q16 and Q21 headings located; page 2 is intentional divider.
- Sonnet/Haiku/model-unknown must not be counted as qualified evidence.
- GPTPro web / external Claude Opus full-artifact review remains `real_call_pending`.

Required Markdown keys:

- `model_gate`
- `content_result`
- `sonnet_haiku_used`
- `answer_key_check`
- `matrix_check`
- `docx_ledger_accepted_check`
- `boundary_check`
- `render_check`
- `required_fixes`
