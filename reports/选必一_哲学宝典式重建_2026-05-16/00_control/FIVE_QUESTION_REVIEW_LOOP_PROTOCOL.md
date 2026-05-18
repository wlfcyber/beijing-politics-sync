# Five-Question Review Loop Protocol

Date: 2026-05-16

This is the hard workflow for every five-question batch in the rebuilt xuanbiyi宝典.

## Loop Order

1. Lock the five-question source packet: original question, material signals, scoring rules, exact source position, and module boundary.
2. Codex and ClaudeCode produce independent initial drafts.
3. Codex fuses the two drafts into a source-based fused draft.
4. Submit the fused draft to user-visible GPT Pro advanced/deeper-thinking mode.
5. GPT Pro must audit and propose modifications. Its raw response is saved before any patching.
6. Codex adjudicates every GPT proposal against the source packet and writes a post-GPT patched draft.
7. Submit the post-GPT patched draft to user-visible Claude Opus 4.7 Adaptive Thinking.
8. Claude Opus must audit and propose modifications. Its raw response is saved before any patching.
9. Codex adjudicates every Claude proposal against the source packet and writes the saved batch final draft.
10. Governor checks fields, source fidelity, module boundaries, answer-sentence quality, and no unverified model suggestion.
11. Only after the batch final draft is saved and Governor passes may the system start the next five questions.

## File Contract Per Batch

- `01_source_packets/BATCH_XXX_SOURCE_PACKET.md`
- `02_codex_batches/BATCH_XXX_CODEX_DRAFT.md`
- `02_claudecode_batches/BATCH_XXX_CLAUDECODE_DRAFT.md`
- `03_fusion/BATCH_XXX_FUSED_DRAFT.md`
- `03_external_review/BATCH_XXX_GPT_PRO_ADVANCED_REVIEW.md`
- `04_adjudication/BATCH_XXX_GPT_PRO_DECISION_LOG.csv`
- `03_fusion/BATCH_XXX_AFTER_GPT_PRO_PATCH.md`
- `03_external_review/BATCH_XXX_CLAUDE_OPUS_ADAPTIVE_REVIEW.md`
- `04_adjudication/BATCH_XXX_CLAUDE_OPUS_DECISION_LOG.csv`
- `03_fusion/BATCH_XXX_FINAL_AFTER_GPT_AND_CLAUDE.md`
- `05_governor/BATCH_XXX_GOVERNOR_FINAL_AUDIT.md`

## Non-Negotiable Rule

GPT Pro and Claude Opus can diagnose and propose modifications, but they are not source authorities. Codex must verify each proposed change against the locked source packet before editing the draft.

No next batch begins until the current batch has:

- raw GPT Pro review saved,
- post-GPT Codex patch saved,
- raw Claude Opus review saved,
- post-Claude Codex patch saved,
- final Governor audit passed.
