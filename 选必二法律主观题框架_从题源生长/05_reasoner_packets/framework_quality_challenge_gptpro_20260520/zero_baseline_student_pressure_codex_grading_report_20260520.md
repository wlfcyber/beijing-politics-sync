# Zero Baseline Student Pressure Test - Codex Grading Report

created_at: 2026-05-20T00:58:00+08:00

## Inputs

- Learning-only packet: `05_reasoner_packets/zero_baseline_student_pressure_20260520.zip`
- Hidden Codex grading key: `10_framework_validation/zero_baseline_student_pressure_20260520/grading_key_for_codex_only.csv`
- Internal agent output: `10_framework_validation/zero_baseline_student_pressure_20260520/internal_agent_zero_baseline_student_answers_20260520.md`
- Claude Cowork output: `10_framework_validation/zero_baseline_student_pressure_20260520/claude_cowork_zero_baseline_student_answers_20260520.md`
- GPTPro output: `10_framework_validation/zero_baseline_student_pressure_20260520/gptpro_zero_baseline_student_answers_20260520.md`

## Bottom Line

The guarded v2 framework is strong for core, high-frequency private-law questions, especially table questions, court-rationale questions, labor disputes, and ordinary private-law fact-to-rule cases. A smart zero-baseline student can use the current documents to start quickly and produce high-scoring answers for T1, T2, T3, and T4, but not all of those answers are yet reliably full-score without a few missing one-page prompts.

The framework is also doing the right thing on open-container and boundary questions: T5 and T6 are not falsely converted into core templates. The brake works. What is still weak is the post-brake answer scaffold: students can avoid the wrong framework, but still need a compact "what to write instead" rule.

## Cross-Lane Consensus

All three lanes independently found the same pattern:

- T1 table entry works well. Remaining loss risk is exact rubric wording for "rights and obligations unity" in the labor meaning cell.
- T2 court-rationale entry works, but weaker student answers omit the final value/reality layer.
- T3 mixed contract/tort is answerable, but the student page must explicitly tell students to split contract validity/breach from tort facts/liability.
- T4 consumer fraud is answerable, but the student page currently under-teaches the two-claim structure: contract formation and fraud-induced invalid/revocable contract first, then Consumer Protection Law article 55 triple compensation.
- T5 open-container ecology can be written by "law provision -> case -> concrete function", but it should remain open-container rather than a core portable template.
- T6 boundary gate works. Students correctly avoid selected-compulsory-2 private-law templates, but need a fallback for legislation / judicial practice / platform efficiency / mediation-value.

## Question-Level Verdict

| Test | Verdict | Reason |
| --- | --- | --- |
| T1 | PASS with minor wording patch | Table entry is clear. Add exact phrase "权利和义务相统一" to student hints. |
| T2 | PASS, but value layer needs a prompt | Strong core entry. Add final layer: 用工自主权 / 权利义务相统一 / 劳动关系稳定. |
| T3 | PASS, patch needed | Core framework works, but mixed liability needs one sentence telling students how to separate contract and tort. |
| T4 | PARTIAL-to-PASS after patch | All lanes got fraud/triple compensation, but weaker answers missed contract成立、违背真实意思、合同无效或可撤销. This is the biggest one-page gap. |
| T5 | PARTIAL/open-container | The frame helps, but should not claim stable full-score core closure. Add open-container three-step fallback. |
| T6 | Boundary PASS, non-core | Boundary brake works and should remain explicit. Add post-brake material-summary fallback. |

## Required Student-Page Patch

Add five concise rules to `framework_v2_student_one_page.md`:

1. Mixed liability: when contract facts and personal/property damage appear together, write contract成立/有效/违约 first, then tort事实/损害/因果/责任.
2. Consumer fraud: when hidden fees, bundling, inability to know/refuse, or misleading discounts appear, write two claims: contract成立 but fraud causes contrary intention and invalid/revocable contract; then article 55 triple compensation.
3. Labor court-rationale value layer: after legality, add 用工自主权、劳动者权利义务相统一、劳动关系稳定.
4. Open-container fallback: law provision -> case fact -> concrete function verb; avoid empty rule-of-law slogans.
5. Boundary fallback: if the subject is China/state/governance/涉外法治/依法行政, stop using private-law templates and answer by material actions:制度/机制/程序/效果.

Patch status: applied after this report was written. Updated files include `11_final_framework/framework_v2_student_one_page.md`, `11_final_framework/framework_v2.md`, `11_final_framework/framework_v2_teacher_guide.md`, and the regenerated baodian Markdown/DOCX. The patched DOCX was exported by Microsoft Word and rendered as PDF with 115 pages and 0 blank-page suspects.

## Current Quality Judgment

Do not say "a zero-baseline student can immediately full-score every included question." That would overclaim.

Safe claim:

> For core selected-compulsory-2 private-law subjective questions, the guarded v2 framework has strong launch power and can bring a smart zero-baseline student close to full-score performance. After a small student-page patch for mixed liability, consumer fraud, labor value layer, open-container fallback, and boundary fallback, the framework becomes much more teachable and safer for classroom use. Open-container and boundary rows remain guarded and should not be flattened into core full-score claims.
