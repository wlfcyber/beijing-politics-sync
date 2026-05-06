# GPT-5.5 Pro Phase 02 Digest

- raw reply: `phase_02_gpt55_raw.md`
- verdict: `CONDITIONAL GO`
- allowed next phase: Phase 03 full suite question scan and classification
- still forbidden: student manuscript, Claude/Opus teaching rewrite, Word/PDF, final PASS

## Binding Conditions

1. Every question must return to a raw source locator.
2. Old drafts remain locator-only and cannot supply conclusions.
3. Every question needs a stable locator and must appear in either the thinking signal-chain matrix, the reasoning attachment matrix, or the blocked list.
4. Reasoning questions must not become generic method summaries; they need typology, logical form, rule slogan, trap, answer action, and same-type question IDs.
5. Thinking questions must not become concept lists; they need material signal, usable thinking/method, answer action, why-triggered logic, answer landing, and source example.
6. Visual-risk sources require visual fallback records: PPTX images/annotations, thin-text PDFs, DOCX tables/images, cartoons, and graph questions.
7. HS02 remains `LOCKED_PENDING_VISUAL` and cannot enter the student manuscript until final visual/source location checks are complete.

## Required Phase 03 Outputs

- `phase03_raw_source_registry.csv/.md`
- `phase03_locator_only_removed_or_isolated.md`
- `phase03_source_reading_methods.md`
- `phase03_source_failures_and_fallbacks.md`
- `phase03_suite_registry.csv/.md`
- `phase03_suite_duplicate_map.csv`
- `phase03_missing_expected_sources.md`
- `phase03_2026_二模_missing_or_blocked.md`
- `phase03_question_coverage_matrix.csv/.xlsx/.md`
- `phase03_thinking_signal_chain_matrix.csv/.md`
- `phase03_reasoning_typology_tree.md`
- `phase03_reasoning_question_attachment_matrix.csv/.xlsx`
- `phase03_reasoning_rule_slogans.md`
- `phase03_reasoning_trap_matrix.md`
- `phase03_reasoning_action_templates.md`
- `phase03_visual_fallback_queue.csv`
- `phase03_visual_fallback_results.md`
- `phase03_pptx_embedded_image_review.md`
- `phase03_pdf_render_review_log.md`
- `phase03_docx_table_and_image_review.md`
- `phase03_laneA_full_scan.csv`
- `phase03_laneB_full_scan.csv`
- `phase03_AB_question_diff.csv`
- `phase03_AB_classification_diff.csv`
- `phase03_AB_source_diff.csv`
- `phase03_resolved_conflicts.md`
- `phase03_unresolved_conflicts.md`
- `phase03_blocked_questions.csv`
- `phase03_GPT_commander_review_packet.md`
- `phase03_Governor_interim_gate.md`
- `phase03_Confucius_interim_learning_value_check.md`

## Phase 03 Execution Order

1. Clean raw-source registry and isolate locator-only rows.
2. Build suite registry and missing/duplicate source tables.
3. Cut every suite into question IDs and sub-question IDs.
4. In parallel, attach each question to thinking, reasoning, cross, pending, or blocked.
5. Build thinking signal-chain and reasoning typology matrices.
6. Run ClaudeCode lane B independently from raw sources.
7. Diff lane A and lane B at question, source, classification, answer, visual-risk, and blocked-status level.
8. Resolve conflicts only by returning to source.
9. Produce Phase 03 commander review packet for GPT-5.5 Pro.

## Risk Warnings To Enforce

- Coverage rows are not enough unless they include material signal or logical form.
- Extracted sources are not enough unless visual-risk pages/slides/tables/images are checked.
- Reasoning chapters fail if they contain rules plus selected examples instead of all-question attachment.
- Integrated reasoning questions cannot be stored under a vague `综合推理` bucket; every rule inside must be split.
- Main-question angle pools must distinguish required points, optional pools, high-value substitutes, and material-best paths.

## HS02 Decision

Accept the Codex fusion, with wording tightened:

`三个可选角度池中，至少锁定两个与材料贴合度最高的角度展开；辩证否定经评标实录确认可作为有效替代或补充角度，但最终学生稿应标注其适用触发信号，避免学生见到改革、创新、突破就机械套辩证否定。`

Required before student use:

- final visual confirmation of original paper stem/material/question;
- source location for main rubric table;
- source location for lecture PDF "choose 2 angles, each 1+2";
- source location for evaluation record confirming 辩证否定 and replaceable 辩证思维特征 route.

## Phase 03 Core Acceptance Sentence

每一道题都必须能从 source locator 回到原题，并且能在思维链矩阵或推理挂载矩阵中找到自己的位置。
