# v12.2 Pending Source Check - 2026-05-22

Status: `source_checked_round01_not_final`

This check resolves the pending source-boundary items listed in `candidate_framework_v12_2_council.md`. It does not claim final PASS, a baodian, DOCX/PDF delivery, or TASK_COMPLETE.

Raw evidence extracts kept beside this report:

- `source_extract_pending_questions_20260522.csv`
- `source_extract_pending_rubric_atoms_20260522.csv`
- `source_extract_pending_core_rows_20260522.csv`
- `pending_source_check_20260522.csv`

## Decisions

| item | decision | framework effect |
|---|---|---|
| CC0137 | Formal locked. The source rewards two separate grid chains: AI copyright and credit-card contract/违约. | Keep in E1. Do not turn into a general AI innovation node. |
| CC0289 | Formal locked. The first part is three Q&A completions; the second part is `任选其一` rights protection by basis, action, and remedy. | Keep E1 as primary, E6 as secondary. |
| CC0223 | Formal locked. The rewarded action is dispute-resolution path across two cases, with value language derived from those cases. | Keep E6 as primary. Do not treat as pure meaning extraction. |
| CC0364 | Formal locked, but ID alias risk exists: v12.1 uses `期中`, merged source/rubric canonical row is `CC0364_2026_通州_期末_19_1`. | Keep E2 with alias note. Procedure legality is rewarded in this case only; separate 逻辑与思维 atoms must not enter the law framework. |
| CC0051 | PASS_RECOVERED source-locked through v12 core/source-lock card, but absent from this pass's 04_merge_audit extract. | Keep E4 as low-frequency recovered evaluation evidence. Do not create a legal-change trunk. |
| CC0195 | Formal locked. The rubric gives labor-law fairness and efficiency points through union platform, collective contract, worker protection, lawful employment, and production efficiency. | Keep E5. Do not classify as non-legal economics by default. |
| CC0162 | Reference-only. | Not promoted. |
| CC0040 | Reference-only. | Not promoted. |
| CC0353 | Reference-only, with 期中/期末 alias risk. | Not promoted. |
| CC0380 | Formal split patch but 综合 boundary and prompt/OCR risk remain. | Open boundary container only, not core support. |

## Detailed Notes

### CC0137

Source basis:

- `v11_source_locked_rebuild/source_snippets/CC0137_rubric.txt` locks the AI copyright scoring points and the credit-card contract scoring points.
- `merged_rubric_atoms_subjective.csv` contains `R_CC0137_2025_昌平_二模_20_02..14`.
- `core_42_v12_1.csv` already treats it as a source-locked core row.

Decision:

- The card supports E1 because each grid cell has its own legal chain.
- The AI grid is about copyright subject, originality/intellectual achievement, infringement, and responsibility.
- The credit-card grid is about contract validity, credit-card overdraft breach, 诚信/全面履行, and 违约责任.
- The framework must not generalize this into a broad "AI innovation" trunk.

### CC0289

Source basis:

- `v11_source_locked_rebuild/source_snippets/CC0289_rubric.txt` states the prompt and scoring structure: completion first, then `任选其一` rights protection.
- `merged_rubric_atoms_subjective.csv` contains `R_CC0289_2026_朝阳_二模_18_01..08`.

Decision:

- Primary placement remains E1 because the visible delivery begins with completing three Q&A answers and rewards precise legal terms.
- Secondary placement remains E6 because the later `任选其一` section rewards rights-protection path: legal basis, action boundary, remedy/responsibility.
- The rubric explicitly blocks false positives: choosing problem 1/2/3 itself is not scored, personal information is not scored, and 必修三 slogans are not scored.

### CC0223

Source basis:

- `merged_subjective_law_questions.csv` records formal source locator `F0098/F0097/F0314`.
- `merged_rubric_atoms_subjective.csv` contains six formal/recovered atoms: litigation mediation, common-area/reasonable use, neighboring relation, right-boundary value, suitable dispute path, and multi-dispute mechanism.
- The source-lock card confirms two cases and warns not to mix the second value question into the first law path.

Decision:

- Keep as E6 primary.
- The question is not merely "what is the value of rule of law"; it first asks how disputes are solved.
- Case 1 must write litigation mediation plus neighboring relation/common-area use.
- Case 2 must write market-regulator adjudication / administrative lawsuit / unfair competition and name-confusion logic.
- Value sentences are allowed only after the case mechanism is named.

### CC0364

Source basis:

- `merged_rubric_atoms_subjective.csv` canonical source row is `CC0364_2026_通州_期末_19_1`, not the v12.1 alias `期中`.
- `R_CC0364_2026_通州_期末_19_1_01` is the legal-subquestion atom: law basis 3, fact analysis 2, judgement meaning 3.
- `R_CC0364_2026_通州_期末_19_1_02..08` are the separate 逻辑与思维 subquestion atoms and must be excluded from the law framework.

Decision:

- Keep as E2.
- `程序合法` is rewarded here because the original answer and source-lock card tie it to legal proportion consent/procedure, glass design reducing impact, and fact finding on 采光.
- Do not make `程序合法` a universal first sentence for all judgement/reason questions.
- Future records should normalize to `CC0364_2026_通州_期末_19_1` or explicitly preserve the alias mapping.

### CC0051

Source basis:

- `core_42_v12_1.csv` and the source-lock card mark it `PASS_RECOVERED`.
- It did not appear in the 04_merge_audit extract used in this pass, so the audit trail must record that it is recovered/source-locked outside that file.

Decision:

- Keep as E4 low-frequency recovered evidence.
- It tests evaluation of a view using marriage-family law change and good-law criteria.
- It must not become a broad legal-change trunk or a 必修三 scientific-legislation slogan branch.

### CC0195

Source basis:

- `merged_rubric_atoms_subjective.csv` has formal atom `R_CC0195_2025_西城_一模_20_01`.
- The rubric explicitly splits fairness and efficiency through labor-law protection and collective consultation.

Decision:

- Keep as E5.
- It is mixed economics/legal language in the prompt, but the scoring anchor is legal: union platform, collective contract, worker rights, lawful employment, labor relationship, and efficiency.
- Therefore it should not be thrown out as non-legal economics.

## Boundary Records Not Promoted

| ID | source state | reason |
|---|---|---|
| CC0162 | reference_only | teacher reference answer only; no formal scoring source located. |
| CC0040 | reference_only | useful digital-person copyright direction, but no core formal rubric. |
| CC0353 | reference_only | canonical row appears as `期末`, and locator/OCR risk remains. |
| CC0380 | formal_boundary_split | useful future new-tech/data-risk evidence, but still 综合 and prompt/OCR boundary; not core support. |

## Framework State After Check

No new entrance is added.

Accepted corrections:

- E1 keeps CC0137 and keeps CC0289 as primary.
- E6 keeps CC0223 as primary and CC0289 as secondary.
- E2 keeps CC0364, but with a source-alias warning and a strict block against importing the logic subquestion.
- E4 keeps CC0051 only as recovered low-frequency evaluation evidence.
- E5 keeps CC0195 as legal-labor fairness/efficiency evidence.
- Open containers remain open; reference-only rows are still excluded from core.

Current verdict: `candidate_source_checked_round01_not_final`.

Still not allowed:

- final PASS
- baodian/handbook claim
- DOCX/PDF delivery claim
- TASK_COMPLETE
