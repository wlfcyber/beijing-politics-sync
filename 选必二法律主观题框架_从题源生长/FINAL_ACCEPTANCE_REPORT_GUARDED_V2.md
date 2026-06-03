# Guarded v2 Final Acceptance Report

generated_at: 2026-05-19T23:50:00+08:00

## Verdict

ACCEPTED_WITH_GUARDS

This run is accepted as the current guarded 65-question selected-compulsory-2 law subjective-question framework and handbook package. It is not accepted as a claim that all 65 questions are core full-score templates.

## Corpus

- questions: 65
- formal: 61
- reference_only: 4
- missing: 0
- material atoms: 482
- ask atoms: 65
- rubric/answer atoms after GPTPro cleanup: 377

## Validation

- pressure status: PASS 45, PARTIAL 20, FAIL 0
- core full-score supported rows: 43
- boundary-gate pass rows: 2
- formal open-container partial rows: 14
- reference_only demo rows: 4
- open-container-only rows: 2

## GPTPro Review

- real GPT-5.5 Pro guarded-v2 review was captured.
- raw response: `tool_outputs/gpt55pro_guarded_v2_review_response_20260519.md`
- canonical copy: `06_open_observations/gpt55pro_guarded_v2_review_20260519.md`
- verdict: `YES_WITH_GUARDS`

Applied cleanup:

- 46 non-scoring/problem/teaching/other-question atoms marked as risk/non-core material.
- 7 patch scoring atoms preserved for CC0245 and CC0251.
- CC0077, CC0084, CC0150, CC0245, CC0251 answer-generation columns cleaned.
- CC0380 moved to `OPEN_CONTAINER_ONLY`.
- `CODE_COWORK_007` split into 007A/B/C/D framework subnodes.
- Answer-column forbidden-text scan passed with 0 hits.

## DOCX/PDF QA

- DOCX: `12_final_baodian/选必二法律主观题满分宝典.docx`
- Word-exported PDF: `12_final_baodian/选必二法律主观题满分宝典_GUARDED_V2_WORD_EXPORT.pdf`
- QA report: `12_final_baodian/DOCX_QA_GUARDED_V2.md`
- PDF page count: 114
- rendered pages: `12_final_baodian/visual_qa_guarded_v2/pdf_pages/`
- blank-page detections: 0

## Remaining Guardrails

- Do not collapse 43 core + 2 boundary + 20 partial into "65 core full-score closures".
- reference_only rows cannot support core framework nodes.
- formal open-container rows can be taught as source cases, but not promoted into stable templates without repeated formal evidence and cross-validation.
- boundary rows remain useful as negative-route examples, not as selected-compulsory-2 answer templates.

## 2026-05-20 Zero-Baseline Student Pressure Addendum

After guarded-v2 acceptance, a learning-only pressure test was run through three lanes: internal Codex agent, Claude Cowork/Opus 4.7, and GPTPro web (`进阶专业`). The test used six sampled questions without rubrics and asked each lane to act as a smart but zero-baseline high-school student.

Result: the core framework launch path is strong, but the student one-page needed short safety prompts for mixed contract/tort liability, consumer-fraud claim structure, labor value-layer closure, open-container fallback, and boundary fallback. These prompts were added as a teaching micro-patch; they do not change the 65-row evidence split.

Updated QA after the micro-patch:

- patched DOCX: `12_final_baodian/选必二法律主观题满分宝典.docx`
- patched Word-export PDF: `12_final_baodian/选必二法律主观题满分宝典_GUARDED_V2_ZERO_BASELINE_PATCH_WORD_EXPORT.pdf`
- QA report: `12_final_baodian/DOCX_QA_GUARDED_V2.md`
- PDF page count: 115
- blank-page suspects: 0

Updated final claim: guarded v2 remains accepted with guards, now with a stronger zero-baseline student page. Do not call the micro-patch a new core-node expansion.
