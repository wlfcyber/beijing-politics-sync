# ClaudeCode Visible-Window Phase 11C Prompt

You are ClaudeCode running in a real visible ClaudeCode window, not `claude -p`, not a hidden background job. Continue in:

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

## User Correction

The user reviewed the Word:

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_完全模仿哲学宝典返工_2026-05-04/04_delivery/选必三逻辑与思维_完全模仿哲学宝典_学生版_2026-05-04.docx`

and said the content is very bad. The four elements under each question are insufficient and unclear. Treat this as a hard failure, not a style nit.

## Must Read

1. `/Users/wanglifei/.codex/skills/feige-politics-garden/SKILL.md`
2. `/Users/wanglifei/.codex/skills/feige-politics-garden-book-orchestrator/SKILL.md`
3. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/SKILL.md`
4. `/Users/wanglifei/.codex/skills/feige-politics-garden-xuanbisan/references/xuanbisan-hard-rules-notebook.md`
5. `08_review/phase11C_bad_word_four_element_failure_audit.md`
6. Bad artifact Markdown: `/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_完全模仿哲学宝典返工_2026-05-04/04_delivery/选必三逻辑与思维_完全模仿哲学宝典_学生版_2026-05-04.md`
7. Philosophy benchmark Markdown: `/Users/wanglifei/Desktop/北京高考政治/必修四终极融合版_2026-05-02/outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_终极融合版.md`
8. Current evidence/student files:
   - `09_student_draft/phase11A_student_body_PATCHED_REVIEW_ONLY.md`
   - `09_student_draft/phase11B_batch01_P1_candidate_entries.md`
   - `09_student_draft/phase10_5_source_repair_priority_queue.csv`
   - `progress.md`
   - `00_control/DECISION_LOG.md`

## Output Directory

Write only under:

`claudecode_lane/phase11C_bad_word_content_audit_visible/`

Do not edit the student body, do not generate Word, do not generate PDF, do not claim final pass.

## Required Outputs

1. `phase11C_visible_status.md`
   - confirm you are in visible-window ClaudeCode mode;
   - confirm the new account is recognized from the visible window if visible;
   - confirm the bad Word is frozen as failure sample only.

2. `bad_word_four_element_failure_matrix.csv`
   - scan all 181 bad-artifact entries;
   - columns: entry_no, heading, qid_or_title, fake_prompt, meta_answer_instruction, node_specific, trigger_sufficient, answer_sentence_sufficient, action;
   - action values: `rewrite_from_source`, `quarantine_until_source`, `choice_trap_rebuild`, `reasoning_type_rebuild`.

3. `bad_word_four_element_failure_report.md`
   - explain the structural failures in Chinese;
   - compare with philosophy benchmark;
   - name at least 10 representative bad entries and why they fail.

4. `four_element_gold_contract.md`
   - define the new required four-element standard:
     - `材料触发点`: concrete signal;
     - `设问`: real question prompt;
     - `为什么能想到`: signal -> total hat -> small method -> trigger logic;
     - `答案落点`: direct student answer sentence.
   - include forbidden phrases: `本题要求结合材料说明其体现的思维方法`, `卷面要把`, `先写`, `要写`, `本题需要`, `设问要求`, `采分点`.

5. `rewrite_samples_10_entries.md`
   - rewrite 10 representative entries only as samples, not final merge;
   - include at least:
     - `2026顺义一模 Q19(2)`;
     - `2025东城期末 Q18(2)`;
     - `2026通州期末 Q11` as choice-trap style;
     - one pure reasoning/formal-logic boundary sample;
     - one multi-node same-question sample showing how the same source must be rewritten differently under different framework nodes.
   - If exact prompt/source is not available, write `BLOCKED_NEEDS_SOURCE` instead of guessing.

6. `next_rebuild_plan.md`
   - propose the next controlled rebuild sequence;
   - do not propose “polish Word”;
   - propose rebuilding Markdown content first, then GPT/Claude content review, then Word only after content gate passes.

7. `progress.md`
   - record what files were read and written.

## Non-Negotiable

- The bad Word is not a base. It is a failure sample.
- The next real product must be built from source/evidence rows and current locked materials.
- Four elements must be explanatory enough for a weak student to transfer, not merely labels.
- Do not use generic placeholders.
- Do not write final/终稿/宝典成品/pass.
