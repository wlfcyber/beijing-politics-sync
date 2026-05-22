# REASONER_INPUT_PACKET

generated_at: 2026-05-19T10:56:58+08:00
packet_version: v2_full_context

## Why This Packet Replaces The 35-Question Trial

The earlier packet only included `formal + keep + high-confidence` rows, producing 35 questions. That was too narrow for this project. The official input must expose the whole merged subjective-law universe while preserving evidence gates.

## Engineering Goal

从 2024-2026 北京各区选必二《法律与生活》主观题与其评分证据中，开放归纳命题机制、判分机制和学生作答机制。本轮只做 observation，不写框架。

## Scope Rules

- Only subjective questions.
- Do not analyze multiple-choice questions or options.
- Do not use textbook目录、法学理论、旧框架、漂亮概念 as structure sources.
- Do not output any final framework, total map, mnemonic, or baodian outline in this round.
- Every observation must include question_id, rubric_atom_id, and material_atom_id.
- Reference answers are not rubrics.
- Missing evidence cannot support an observation.

## Data Range

- Full merged candidate questions in packet: 74
- Observation-eligible questions: 57
- Strong formal/user_confirmed questions: 54
- Weak reference_only questions: 3
- Missing-evidence questions included only for补证/边界 awareness: 17
- Material atoms: 1025
- Ask atoms: 74
- Rubric/answer atoms: 426

## Evidence Level Counts

- formal: 54
- missing: 17
- reference_only: 3

## Merge Status Counts

- keep: 36
- pending_evidence: 17
- pending_locator_check: 21

## Input Files

- merged_subjective_law_questions_for_reasoners.csv
- merged_material_atoms_subjective_for_reasoners.csv
- merged_ask_atoms_subjective_for_reasoners.csv
- merged_rubric_atoms_subjective_for_reasoners.csv
- merge_audit_report_for_reasoners.md
- REASONER_INPUT_PACKET.md

## Task For GPT-5.5 Pro And Claude Opus

Use the same input and the same prompt. Independently discover observations about:

1. module boundary;
2. ask-task type;
3. minimum necessary judgment;
4. material fact -> legal language -> rubric reward;
5. score mechanism;
6. full-score sentence pattern;
7. transfer potential and codebook qualification.

## Output Format

Each observation must contain:

observation_id, plain_observation, question_ids, rubric_atom_ids, material_atom_ids, ask_type, evidence_type, evidence_level, what_student_must_judge, material_trigger, legal_knowledge_or_rule_triggered, rubric_reward, knowledge_material_value_type, full_score_sentence_pattern, must_have_keywords, risk_of_empty_value_talk, risk_of_legal_exam_overanalysis, module_boundary_risk, transfer_potential, counterexamples, confidence, should_enter_codebook, reason.

Final grouping:

1. 强观察：可以进入代码本的观察。
2. 弱观察：证据不足，但值得下一轮验证。
3. 冲突观察：证据内部存在矛盾，需要回源核查。
4. 不应上升为框架的观察。
5. 下一轮需要补充或重点验证的主观题类型。

Again: this round is open observation only. Do not output a framework.
