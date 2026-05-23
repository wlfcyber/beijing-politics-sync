# ClaudeCode Opus Independent Thick Draft Lane

You are the ClaudeCode independent production lane for the Xuanbiyi strict final rebuild.
The command that launches you should use `--model opus --effort max`. Treat this as a high-effort Opus run.

## Workspace

Repository root:
`C:\Users\Administrator\Desktop\02_???????\mac-thread-restore\beijing-politics-sync-visible`

Output directory:
`reports/选必一_哲学宝典式重建_2026-05-16/11_strict_final_rebuild_2026-05-23/06_claudecode_independent_opus47`

## Read-only inputs

Read these inputs only:

- `reports/???_???????_2026-05-16/11_strict_final_rebuild_2026-05-23/04_review_queue.csv`
- `reports/???_???????_2026-05-16/11_strict_final_rebuild_2026-05-23/04_source_packets/`
- `reports/???_???????_2026-05-16/11_strict_final_rebuild_2026-05-23/01_extracted_text/`
- `reports/???_???????_2026-05-16/06_final_handbook/???_????_????????.md` only for the 12 anti-merge residual source references
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\current-user-requirements.md`
- `C:\Users\Administrator\.codex\skills\feige-politics-garden-xuanbiyi\references\xuanbiyi-term-protocol.md`

Do not read these Codex-side or earlier Claude-side conclusion files:
- `05_codex_first_pass_adjudication.csv`
- `05_claudecode_opus47/CLAUDECODE_STRICT_ADJUDICATION.md`
- `05_claudecode_opus47/CLAUDECODE_STRICT_PATCH_ENTRIES.md`
- `05_claudecode_opus47/CLAUDECODE_COVERAGE_RISK_LOG.md`
- the current student handbook as an authority for whether an entry should be included

The point of this run is independent draft generation from the shared source packets and source evidence.

## Hard rules

1. Subjective questions only.
2. Main-table entries require scoring rubrics, marking rules, rubric PPTs, lecture scoring material, or user-confirmed scoring material. Ordinary answer keys may only be downgraded reference material.
3. Use `NEEDS_EVIDENCE` when a question looks relevant but same-question scoring evidence is not located.
4. Every included item must be a single-question example. Do not merge two source questions into one case, one heading, or one answer paragraph.
5. For the 12 anti-merge residuals, go back to the original source references in the audit/source packets; do not infer from the merged final version.
6. Preserve rubric wording after the term label. Do not invent attractive umbrella terms.
7. Classification boundaries:
   - New-type international relations / cooperation-win international relations belongs under political multipolarity, not theory.
   - Independent foreign policy of peace / Five Principles of Peaceful Coexistence belongs under China.
   - Economic globalization internal grouping must be expression-sensitive; do not merge distant terms merely because they are conceptually similar.
8. If a question mainly belongs to other modules/books, mark `EXCLUDE_OTHER_MODULE`.

## Output schema

Write exactly these files into the output directory:

1. `CLAUDECODE_INDEPENDENT_ADJUDICATION.md`
   - adjudicate every queue item with one of: `INCLUDE_STRICT_MAIN`, `EXCLUDE_OTHER_MODULE`, `NEEDS_EVIDENCE`, `DOWNGRADED_REFERENCE_ONLY`.
   - include source key, reason, and evidence level.

2. `CLAUDECODE_INDEPENDENT_THICK_DRAFT.md`
   - only include `INCLUDE_STRICT_MAIN` items.
   - organize by the six buckets: ????, ??, ?????, ?????, ??, ???.
   - each entry must include these labels exactly: `??????`, `??????` if helpful, `???????`, `????`, `????????`, `??????`, `??????`, `????`.
   - no heading may contain two source questions joined by semicolon or list punctuation.

3. `CLAUDECODE_INDEPENDENT_RISK_LOG.md`
   - list relevant questions still lacking scoring evidence.
   - list downgraded ordinary-answer items.
   - list any source packet or extracted text reliability risks.

At the end, print a concise stdout summary with counts for included, excluded, needs evidence, downgraded, and anti-merge residuals successfully rewritten.
