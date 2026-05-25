# ClaudeCode Batch21 Recheck Result - 2025 Dongcheng Final

Parsed from raw stream:

- `OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RECHECK_STREAM_RAW_UTF8.jsonl`
- `OPUS47_CLAUDECODE_BATCH21_2025_DONGCHENG_FINAL_RUNTIME_EVIDENCE.json`

## Result

- `content_result`: `pass`
- `local_policy_result`: `pass_with_model_gate_blocked`
- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
- `required_fixes`: see ClaudeCode final response below; none recorded by parser if `content_result` is pass/pass_with_notes.

## Evidence Checked

- Matrix target: Batch21 should have `25` rows, covering Q1-Q21/subparts.
- Body target: four governed DOCX entries for Q4, Q16, Q21 value judgment, and Q21 people.
- Render target: `249/249` pages/images, labels `2315/2315`, visible suite mentions `4/4`, pages `20, 127, 216, 233`.
- Ledger target: four governed records in both `docx_insert_ledger.csv` and `student_patch_entries.accepted.jsonl`.
- Global scope target: remaining raw midterm/final source gap `14` suites.

## Model Evidence Boundary

- Runtime observed models: `claude-api, claude-opus-4-7`.
- Command lane used `--model claude-opus-4-7 --effort max`.
- Stream thinking block/signature seen: `true`.
- Debug model mentions: `claude-haiku-4-5-20251001, claude-opus-4-7`.
- Sonnet/Haiku/model-unknown output is not counted as qualified evidence.
- Machine-readable adaptive/max-effort proof is still insufficient, so the model gate remains `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.

## ClaudeCode Final Response

I'll recheck the Codex Batch21 work from source evidence. First, let me state the runtime gate clearly: my environment reports `claude-opus-4-7` as the model, but I cannot independently prove `max effort + adaptive thinking` runtime configuration from inside the conversation — that will be reflected in `model_gate`.

Let me inspect the required files in parallel.Let me find the docx_insert_ledger and check additional files.All artifacts inspected. Producing the recheck output now.

---

# ClaudeCode Opus 4.7 Recheck — Batch21 2025 东城期末

- **content_result**: `pass`
- **local_policy_result**: `pass_with_model_gate_blocked`
- **model_gate**: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`
  - Environment reports `claude-opus-4-7`, but max-effort + adaptive-thinking runtime cannot be independently proven from inside the conversation. No Codex/Codex-derived artifact upgrades this gate.
- **sonnet_haiku_used**: `no` — all current-batch artifacts are Codex production-lane outputs verified against source files; no Sonnet/Haiku/model-unknown content is counted as qualified evidence. ClaudeCode/external full-artifact reviews remain pending and are NOT being substituted by lower-tier models.

## matrix_check

- `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` contains exactly **25** rows tagged `codex_batch21_2025_dongcheng_final` (M0968-M0992).
- Coverage: Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17, Q18(1), Q18(2), Q19(1), Q19(2), Q19(3), Q20, Q21×2 = **25** items.
- Body rows = 4 (Q4, Q16, Q21-人民群众, Q21-价值判断与价值选择); boundary rows = 21. Matches the Codex declaration `25 (4 body, 21 boundary)`.
- Evidence-level discipline correct: Q4 is `教师版客观答案/解析+题面正确项；非主观评分细则` — objective-only as required (not promoted to subjective rubric). Q16/Q21 use `正式讲评/评分细则` evidence. Q5/Q18(2) Logic-Thinking, Q17/Q19 Law-Politics, Q20 国际政治与经济 are all explicitly `MODULE_BOUNDARY_EXCLUDED_BATCH21_DONGCHENG_FINAL`.

## docx_check

Exactly the four governed entries are present, matching the spec line-for-line:

| Heading | Node | Status |
|---|---|---|
| `8. 2025东城期末 第16题（主观题）` | 主观能动性 / 意识的能动作用 | REGISTERED_EXISTING |
| `30. 2025东城期末 第4题（选择题）` | 矛盾就是对立统一 | REGISTERED_EXISTING |
| `26. 2025东城期末 第21题（主观题）` | 人民群众 | INSERTED |
| `10. 2025东城期末 第21题（主观题）` | 价值判断与价值选择 | REFRESHED |

- `docx_insert_ledger.csv` Batch21 rows: **4** ✓
- `student_patch_entries.accepted.jsonl` Batch21 records: **4** ✓
- Q21 value-judgment refresh is materially thicker, not a one-line landing — `答案落点` chains 社会发展规律 → 人民立场 → 民生为大 → 发展/立法/司法/公共服务/文化惠民评价尺度 → 收入/医保/教育/基层立法/民生小案件/文化惠民 material grounding → 价值取向转化为实践要求. Student-facing structure (材料触发点 / 设问 / 为什么能想到 / 答案落点) intact.

## render_check

From `word_render_qa_20260525_batch21_word/render_manifest.json` and `FORMAT_RENDER_QA_20260524.md` Batch21 section, all numbers cohere:

- `pages` = 249, `rendered_png` = 249 ✓
- `docx_label_count` = 2315, `pdf_label_count` = 2315 ✓
- `docx_suite_mentions` = 4, `pdf_suite_mentions` = 4 ✓
- `suite_hit_pages` = `[20, 127, 216, 233]` matching headings 8/30/26/10 ✓
- `pdf_text_suite_mentions` = 0 — confirmed as PyMuPDF CJK text-extraction limitation; visible/visual evidence (Word-layout heading hits + contact sheet + pages 233/234 inspection) confirms 4/4 visibility. Not a visibility miss.
- `blank_like_pages_excluding_cover_foreword` = `[]` ✓

## global_scope_check

`GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md` reports:
- raw suite directories: 64; covered: 50; remaining midterm/final: **14** ✓
- Listed 14 gap suites: 2025丰台期末/朝阳期末/海淀期中/海淀期末/西城期末 + 2026东城/丰台/朝阳期中/朝阳/海淀期中/海淀/石景山/西城/通州 期末 — table line count = 14 ✓
- Audit explicitly disclaims whole-project final acceptance and keeps GPTPro / external Opus / model gate flagged as pending.

## required_fixes

No content-level corrections required for Batch21 local closure. Disciplinary notes for the lane (not blockers):

1. None of the Batch21 artifacts make a project-wide acceptance claim. Maintain that posture in any roll-up note.
2. Q4 ledger / matrix / JSONL all carry `非主观评分细则` boundary text — keep this language in any downstream consolidation; do not let later summarizers conflate objective key + 解析 with subjective rubric.
3. Q21 value-judgment entry has been thickened; keep `boundary_note` clarifying that 综合题 is not collapsed to a single philosophy node.

## remaining_project_blockers

- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED` — max-effort + adaptive-thinking runtime proof cannot be issued from inside the conversation; this recheck stands as evidence of content-correctness, not as a model-effort attestation.
- GPTPro web review: `real_call_pending`.
- External Claude Opus full-artifact review: `real_call_pending`.
- Global raw-suite gap of `14` midterm/final suites remains outside the current first/second-mock-scoped strict coverage audit; whole-project final acceptance MUST NOT be declared on the basis of Batch21 alone.

Batch21 may be treated as **locally closed at the content layer**, pending the three external/model gates above.
