# Codex Response To Advice

phase: Phase 01 Workspace And Initial Source Inventory
gpt_raw_file: `08_review/gpt_phase_advice/phase_01_gpt_raw.md`
codex_status: `G10_digest_written`
local_authority_rule: GPT-5.5 Pro is strategic advice only. Local source evidence, branch skill rules, user notebook, Governor gates, and Codex evidence checks decide whether anything enters the artifact.

## Invalid GPT Attempts

The first two Safari/ChatGPT UI deliveries are rejected and excluded from advice:

- `Failed UI Delivery`: multiline Computer Use `type_text` fragmented the prompt into separate ChatGPT user bubbles, so GPT answered broken fragments rather than the phase report.
- `Failed Single-Line Type Delivery`: single-line `type_text` kept one bubble but corrupted/dropped Chinese content.

Only the clipboard-paste delivery into the already-open Safari ChatGPT Pro conversation is accepted as the Phase 01 GPT raw advice.

## Local Digestion

| suggestion_id | raw_gpt_suggestion_summary | decision | reason | local_task_created | local_evidence_to_check | execution_status | affects_student_doc | follow_up_phase |
|---|---|---|---|---|---|---|---|---|
| G10-01 | Phase 02 may proceed only after GPT raw, Codex response, task-plan conversion, and GPT authority boundary are logged. | accepted | This matches the whole-book SOP and prevents a fake GPT checkpoint. | Update `codex_response_to_advice.md`, `MODEL_ADVICE_LOG.md`, `task_plan.md`, `DECISION_LOG.md`, and Governor status. | Confirm raw GPT file exists and references only the valid clipboard-paste response. | in_progress | no | Phase 01 close / Phase 02 entry |
| P02-01 | Name Phase 02 as source locking and P0/P2 evidence matrix construction. | accepted | This is the right next bottleneck before large-scale term production. | Rename current phase target in `task_plan.md` and add Phase 02 outputs. | Check `SOURCE_INVENTORY.csv`, `SUITE_INVENTORY.csv`, `COVERAGE_MATRIX.csv`. | in_progress | no | Phase 02 |
| P02-02 | Build suite-by-suite and question-by-question matrix for xuanbiyi subjective questions. | accepted | The current suite matrix is not enough for final closure. | Create `suite_question_matrix.csv` and `xuanbiyi_subjective_index.csv`. | Reopen primary source papers/scoring files; verify question numbers and module boundary. | pending | no | Phase 02 |
| P02-03 | Recheck all 98 P0 candidates instead of trusting filenames. | accepted | This is the largest false-evidence risk. | Create `evidence_level_recheck.csv`; classify P0/P1/P2/P3/unknown with reasons. | Inspect file content for actual scoring/rubric/marking language versus reference answers or teaching language. | pending | no | Phase 02 |
| P02-04 | Split P2 materials into marking-mouthpiece, ordinary lecture, and student handout language. | partially_accepted | Accepted for evidence tracking, but P2 cannot become scoring authority unless locally verified or user-confirmed. | Add `p2_role` / notes in evidence recheck. | Check PPT/DOC/PDF context and whether it explicitly cites marking or scoring rules. | pending | no | Phase 02 |
| P02-05 | Use 2026通州期末 Q20 and 2026朝阳期中 Q17 as hard samples. | accepted | These are user-notebook hard samples and already have current-run Codex entries. | Write `hard_sample_review_2026_tongzhou_q20.md` and `hard_sample_review_2026_chaoyang_q17.md`. | Reopen original paper/scoring files; ensure six Tongzhou points and all Chaoyang layers are preserved. | pending | yes | Phase 02 |
| P02-06 | Create Phase 02 JSONL entries with source/evidence/status fields. | accepted | This provides a clean bridge from source lock to later student-facing fusion. | Create `xuanbiyi_subjective_entries_phase02.jsonl`; do not treat it as final student document. | Verify every entry's `evidence_source_type` and avoid old-final evidence pollution. | pending | yes | Phase 02 |
| CLC-01 | Give ClaudeCode a Phase 02 independent inventory/index/evidence task. | accepted with local rewrite | GPT cannot directly order ClaudeCode; Codex will translate it into a local worker prompt and preserve Claude's independent evidence lane. | Send/append a scoped ClaudeCode corrective task if current Claude output lacks Phase 02 matrix fields. | Check ClaudeCode process/log/artifacts and avoid overwriting its independent results. | pending | no | Phase 02 |
| REV-01 | GPT content review is not yet triggered for final artifacts; only a light template/hard-sample precheck may occur. | accepted | No completed outline, section batch, final Markdown, or Word/PDF exists yet. | Record G11 trigger state as `not_triggered`. | Confirm no artifact was falsely marked as content-reviewed. | in_progress | no | Phase 02 |
| GOV-01 | Add a temporary G2.5 Source Eligibility Gate and strict evidence-boundary checks. | accepted | The current risk is evidence inflation, not document polishing. | Update `GOVERNOR_GATES.md`; enforce source-id, verified evidence level, exclusion reason, and unknown handling. | Verify 177 files, 57 suites, status counts, and unknown handling plan. | in_progress | no | Phase 02 |
| RISK-01 | Do not start whole-book final term document until matrix and P0 recheck are closed. | accepted | Prevents the old failure mode of impressive-looking but under-verified summaries. | Mark final-doc production blocked until Phase 02 gate passes. | Confirm `student_doc_*` placeholders remain non-final. | in_progress | yes | Phase 02 / Phase 05 |

## Rejected Or Deferred Items

- No GPT advice is rejected on substance yet.
- Any advice that would use GPT as evidence authority is pre-rejected by rule, even if later phrased implicitly.
- Any Phase 02 light content precheck is deferred until the two hard-sample reviews are written from local evidence.

## G11 Trigger State

| trigger | status | note |
|---|---|---|
| outline | not_triggered | No student-facing outline is complete. |
| section_batch | not_triggered | No accepted section batch exists. |
| final_markdown | not_triggered | No final Markdown exists. |
| word_pdf | not_triggered | No Word/PDF delivery artifact exists. |

## Immediate Local Tasks

1. Finish this G10 logging set and mark Phase 01 as conditionally enterable, not fully final-delivered.
2. Create Phase 02 matrix artifacts: `suite_question_matrix.csv`, `evidence_level_recheck.csv`, `xuanbiyi_subjective_index.csv`, `xuanbiyi_subjective_entries_phase02.jsonl`.
3. Recheck current hard samples against original sources and write their hard-sample review files.
4. Inspect ClaudeCode current output and correct its tasking if it is producing entries without the required matrix/evidence recheck layer.
