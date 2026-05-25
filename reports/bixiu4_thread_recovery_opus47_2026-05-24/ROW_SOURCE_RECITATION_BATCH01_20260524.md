# ROW_SOURCE_RECITATION_BATCH01_20260524

Status: `CODEX_ROW_SOURCE_RECITATION_BATCH01_DONE__CLAUDECODE_CONTENT_RECHECK_DONE_MODEL_GATE_BLOCKED`

Timestamp: 2026-05-24 23:33 +08

## Scope

This batch covers the 9 accepted-body rows that the Opus 4.7 observation flagged for row-level source recitation:

- `student_patch_entries.accepted.jsonl` rows 21, 22, 23, 24, 25, 26, 34, 35, 36.
- This began as a Codex source-recitation pass. A later real ClaudeCode Opus 4.7 row-source recheck was also run and wrote `OPUS47_CLAUDECODE_ROW_SOURCE_RECHECK_RESULT.md`; it found no content corrections required but remained model-gate blocked because effort/adaptive proof was not exposed.

## Decisions

| accepted row | suite / question | framework node | source evidence | decision |
|---:|---|---|---|---|
| 21 | 2025海淀一模 Q22 | 系统观念 | `2025海淀一模.md:101-112` gives Q22 scoring frame and system-concept scoring; `:117-130` explains system view, global/local, major/minor relations, and comprehensive reform as a complex system project. | `KEEP` |
| 22 | 2025海淀一模 Q22 | 主次矛盾 / 全局局部 | `2025海淀一模.md:117-122` explicitly includes 全局和局部、主要矛盾和次要矛盾. | `KEEP` |
| 23 | 2026通州一模 Q18 | 矛盾对立统一 | `2026通州一模.md:169-173`, `:181-182`, `:190` explicitly score 对立统一 / 矛盾对立统一 with analysis. | `KEEP` |
| 24 | 2026通州一模 Q18 | 辩证否定 / 守正创新 | `2026通州一模.md:173-184`, `:190-191` explicitly score 辩证否定观 and allow development-view substitution. | `KEEP` |
| 25 | 2026海淀二模 Q16 | 联系观点 | `2026海淀二模_Q16_readable_evidence.md` cites source lines `1092-1094` for the question and `1140-1141`, `1162-1163` for the answer/rubric text: 可从联系、实践与认识等角度作答. | `KEEP_AS_LECTURE_SCORING_OPTION` |
| 26 | 2026海淀二模 Q16 | 实践与认识 | Same evidence as row 25. This supports practice/knowledge as an authorized optional angle, not a cumulative independent point. | `KEEP_AS_LECTURE_SCORING_OPTION` |
| 34 | 2026石景山二模 Q17(3) | 联系观点 | `2026石景山二模.md:125-126` gives the 良法/善治 question; `:148` explicitly allows 联系、矛盾、实践与认识关系等角度. | `KEEP_OPTIONAL_PATH` |
| 35 | 2026石景山二模 Q17(3) | 矛盾对立统一 | Same source as row 34. The original material trigger mixed in irrelevant 隆福寺-style examples; corrected in accepted JSONL and DOCX. | `KEEP_AFTER_MATERIAL_TRIGGER_FIX` |
| 36 | 2026石景山二模 Q17(3) | 实践与认识 | Same source as row 34. This is an optional path, not a third cumulative point. | `KEEP_OPTIONAL_PATH` |

## Evidence Boundary

`2026海淀二模 Q16` is not promoted to formal point-by-point rubric. The source is a readable lecture/scoring support file under the suite's `细则` material and explicitly names the allowed angles. Therefore the two rows remain valid as optional lecture-supported angles, but should not be described as formal per-point scoring detail.

`2026石景山二模 Q17(3)` explicitly allows three philosophy pathways. These rows are retained only as optional paths. They must not be taught as three cumulative answer points.

## Correction Applied During This Batch

Patched row:

- `2026石景山二模 Q17(3)` / `矛盾就是对立统一`

Old issue:

- The material trigger included off-question examples such as 保护与利用、传承与创新、历史与现代. Those examples fit 隆福寺-style culture renovation, not 良法/善治.

New student-facing trigger:

- `“良法”强调制度规范和立法起点，“善治”强调治理成效和目标实现；材料说良法只是起点、善治才是目标，说明二者有区别又统一于同一法治建设过程。良法为善治提供规范基础，善治检验并实现良法价值，必须在二者关系中理解双方。`

Files updated:

- `04_fusion_audit/student_patch_entries.accepted.jsonl`
- `05_delivery/哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`

Rerender result:

- PDF page count: 235.
- Page image count: 235 plus contact sheet.
- Visual check: page 121 shows corrected row 35 wording and consistent label style.

## Remaining Boundary

This batch reduces the 9-row source-recitation blocker on the Codex lane. It does not close:

1. Qualified ClaudeCode/Opus 4.7 row recheck remains model-gate blocked even though content recheck completed.
2. GPTPro full-artifact review.
3. Claude Opus external full-artifact review.
4. The 546 unresolved production candidate rows in the recovery matrix.
5. Full every-page manual typography inspection.
