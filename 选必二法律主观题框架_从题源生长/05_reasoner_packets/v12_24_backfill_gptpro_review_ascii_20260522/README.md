# v12_24_backfill GPT Pro Review Packet

This packet is for external GPT Pro review of `v12_24_question_backfill`.

## What GPT Should Review

Primary review target:

- `v12_24_question_backfill/`

Reference baseline:

- `v11_1_written_chain_patch/`

Prompt to paste into GPT:

- `PROMPT_FOR_GPTPRO_V12_24_BACKFILL_REVIEW_20260522.md`

## Current Codex Claim

Codex does **not** claim final completion.

Current status:

- `V11_1_WRITTEN_CHAIN_PATCH_PASS`
- `NOT_FINAL_BAODIAN`
- `v12_24_question_backfill`: `CONDITIONAL_PASS`

v12 result:

- 24 source-lock cards created.
- 18 questions backfilled.
- 6 questions moved out of student body as unable to lock source.
- v12 student chain body currently contains 47 source-locked questions, not all 53.

## Six Unfilled Questions

- `CC0251_2026_丰台_一模_20`
- `CC0276_2026_房山_二模_17`
- `CC0277_2026_房山_二模_18`
- `CC0317_2026_海淀_期中_18`
- `CC0318_2026_海淀_期中_18_2`
- `CC0319_2026_海淀_期中_19`

GPT should decide whether this is acceptable as `CONDITIONAL_PASS`, should be `FAIL`, or can be upgraded to `V12_24_BACKFILL_PASS`.

## Hard Review Rule

Do not expand to 65/70 candidates. Do not include pending questions. Do not allow final baodian or DOCX yet unless GPT explicitly states the blockers are resolved or acceptable.
