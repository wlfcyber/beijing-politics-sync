# Governor Gates

| Gate | Status | Current Evidence / Requirement |
|---|---|---|
| G0 startup | pass | Dedicated run folder and numbered layout created. |
| G1 notebook | pass | Xuanbiyi notebook/current requirements and term protocol read. |
| G2 source inventory | in_progress | 177 files scanned; suite inventory currently 57 suites; source/question eligibility still pending. |
| G2.5 source eligibility | active_pending | New Phase 02 gate: every source must have source_id, verified evidence level, xuanbiyi/subjective status, visual-risk state, and exclusion/blocker reason if applicable. |
| G3 non-text handling | pending | PDF/Word/PPT/image/table/OCR risks must be routed before evidence closure. |
| G4 evidence levels | pending | P0 candidates cannot be trusted by filename; 98 P0 candidates require content recheck. |
| G5 coverage | pending | Suite-level matrix exists; question-level matrix still required. |
| G6 conflicts | pending | ClaudeCode comparison not yet evidence-checked. |
| G7 student transfer | pending | No accepted student section batch exists. |
| G8 Word/PDF visual QA | pending | No Word/PDF artifact exists. |
| G9 Confucius | pending | Final artifact-only verification not reached. |
| G10 GPT phase mechanism | in_progress | Valid GPT raw saved after clipboard recovery; invalid UI outputs rejected; Codex digestion and task-plan conversion being written. |
| G11 GPT content review | not_triggered | outline, section_batch, final_markdown, and word_pdf are not triggered yet and must not be marked PASS. |
| G12 overnight delivery | active_pending | User authorized sleep-run final delivery. PASS requires final Markdown, DOCX, PDF, acceptance report, updated督工状态, ClaudeCode comparison or logged fallback, GPT content review/fallback, Governor, Confucius, and visual/text QA. |

## G11 Trigger State

| Trigger | Status | Note |
|---|---|---|
| outline | not_triggered | No student-facing outline is complete. |
| section_batch | not_triggered | No accepted section batch exists. |
| final_markdown | not_triggered | No final Markdown exists. |
| word_pdf | not_triggered | No Word/PDF delivery artifact exists. |

## Overnight Final PASS Addendum

- Claude advisor can guide ClaudeCode only through Codex digestion; any model-only claim without local source evidence fails G4/G6.
- A student-facing final artifact cannot contain local paths, audit fields, source ids, debug/OCR notes, model chatter, or backstage scoring language.
- If GPT-5.5 Pro is delayed overnight, each skipped trigger must be logged as fallback and late-reviewed before promotion if GPT becomes available.
- If Word rendering or Microsoft Word validation is unavailable, record the exact unavailable tool and perform the strongest local DOCX/PDF text and visual checks available.
