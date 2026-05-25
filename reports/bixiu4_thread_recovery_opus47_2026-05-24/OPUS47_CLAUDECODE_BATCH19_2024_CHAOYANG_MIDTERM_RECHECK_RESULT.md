# Opus 4.7 ClaudeCode Batch19 Recheck Result - 2024朝阳期中

- `model_gate`: `BLOCKED_MODEL_CONFIRMATION_REQUIRED`. Runtime self-reports model id `claude-opus-4-7`, but I cannot independently expose machine-readable proof of `--effort max` and adaptive-thinking from inside this conversation. Aligns with the existing Governor verdict on prior batches.
- `content_result`: `pass_with_notes`. All Batch19 decisions verify against source, matrix, ledger, accepted, DOCX, and render evidence.
- `sonnet_haiku_used`: `no`. This invocation reports Opus 4.7; no Sonnet/Haiku evidence is being promoted in this recheck.
- `answer_key_check`: `pass`. Raw RTF (`2024朝阳期中细则.rtf`) decoded via GBK and stripped of RTF control words shows the answer table cells in order `1 2 3 4 5 6 7 8` → `B D D C A C B D` and `9 10 11 12 13 14 15` → `B D C C C A B`, exactly `1B 2D 3D 4C 5A 6C 7B 8D 9B 10D 11C 12C 13C 14A 15B`. Used only for objective-choice placement, not as subjective scoring rule.
- `matrix_check`: `pass`. 28 rows under `row_source = codex_batch19_2024_chaoyang_midterm` cover Q1–Q20 with 0 open rows. Evidence labels are bounded:
  - Q1/Q3/Q4(×2)/Q5/Q10 use `客观答案表+题面正确项；非主观评分细则`.
  - Q16 uses `正式阅卷细则+当前DOCX正文` against the four historical-materialism nodes (社会存在与社会意识 / 社会发展的两大基本规律和基本矛盾 / 改革 / 改革的实质 / 人民群众).
  - Q17 uses `正式阅卷细则（哲学2分开放角度）+当前DOCX正文` for five open philosophy add-on nodes (尊重客观规律与发挥主观能动性相结合, 辩证否定 / 守正创新, 矛盾就是对立统一, 矛盾的特殊性 / 具体问题具体分析, 价值判断与价值选择). Notes column explicitly reads `哲学2分为开放角度，登记时不说成逐点评分细则`.
  - Q2/Q6 culture; Q7–Q9/Q11/Q18/Q19 Logic and Thinking; Q12–Q15/Q20 economy/international politics boundaries — all closed with `答案键+题干+模块边界` or `题干+模块边界`.
- `docx_check`: `pass`. Current DOCX (`哲学宝典最终版-飞哥正志讲堂_2026二模与一模漏项补强版_2026-05-24.docx`, 400,952 bytes) carries exactly 15 `2024朝阳期中` student-facing headings with distribution `Q1=1, Q3=1, Q4=2, Q5=1, Q10=1, Q16=4, Q17=5`. Ledger and accepted JSONL each gained 15 governed records for this suite (139 total rows in both).
- `render_check`: `pass`. `render_manifest.json` shows Word COM PDF export with `pages=250`, `rendered_png=250`, `blank_like_pages_excluding_cover_foreword=[]`, `docx_label_count=2316`, `pdf_label_count=2316`, and `suite_hit_pages = [28, 32, 82, 101, 107, 114, 120, 136, 192, 199, 203, 205, 212, 236, 249]` — matches the prompt expectation exactly. PDF size 4,090,938 bytes.
- `global_scope_check`: `pass`. `GLOBAL_RAW_SUITE_EXHAUSTION_AUDIT_20260525.md` lists `remaining midterm/final raw suites = 16` (down from 17), with `2024朝阳期中` now `covered_by_batch19_recovery_matrix`; the 16 remaining suites still need disposition or explicit scope exclusion before whole-project acceptance.
- `required_fixes`: none for Batch19 content; no forbidden strict-final acceptance status is claimed. Outstanding gates carried over (not Batch19 regressions):
  1. Opus 4.7 max-effort/adaptive proof — still `BLOCKED_MODEL_CONFIRMATION_REQUIRED`.
  2. GPTPro web / external Claude Opus full-artifact reviews — `real_call_pending`.
  3. Global source-scope gap — 16 raw midterm/final suites still outside coverage.