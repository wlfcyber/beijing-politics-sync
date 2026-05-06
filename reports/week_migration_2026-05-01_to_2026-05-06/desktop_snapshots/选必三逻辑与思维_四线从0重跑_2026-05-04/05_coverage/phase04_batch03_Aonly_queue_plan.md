# Phase04 Batch03 A-only Queue Plan

- source_control_base: `05_coverage/phase04_control_base_status_after_batch02.csv`
- all_queue: `05_coverage/phase04_batch03_Aonly_queue.csv`
- first_queue_for_claudecode: `05_coverage/phase04_batch03_A_subjective_queue.csv`
- second_queue: `05_coverage/phase04_batch03_B_choice_queue.csv`
- student_doc_status: blocked for all rows

## Counts

- total L1 rows: 112
- by batch: {'B03B_choice_second': 56, 'B03A_subjective_first': 56}
- by question_type: {'选择题': 56, '主观题': 56}
- by section_scope: {'推理': 66, '交叉': 16, '思维': 27, '边界': 3}
- by gap_priority: {'P0': 1, 'P1': 78, 'P2': 33}

## Top Suites In Full Queue

- S-2025东城期末: 14
- S-2026东城期末: 11
- S-2026顺义一模: 9
- S-2025顺义一模: 9
- S-2025丰台期末: 8
- S-2024朝阳期中: 8
- S-2024朝阳二模: 7
- S-2026东城一模: 7
- S-2024海淀二模: 7
- S-2024西城一模: 7
- S-2026通州期末: 6
- S-2024朝阳一模: 5
- S-2026朝阳期中: 5
- S-2025海淀期末: 5
- S-2025西城二模: 4

## First Batch: B03A Subjective First

Rationale: subjective rows carry the highest risk of missing formal rubric boundaries, incomplete prompts, and source-level answer logic. They are also the rows most likely to damage the final book if promoted too early.

- S-2024西城一模: 6
- S-2024朝阳二模: 5
- S-2025东城期末: 5
- S-2026东城期末: 5
- S-2025丰台期末: 4
- S-2026朝阳期中: 4
- S-2025海淀期末: 4
- S-2026东城一模: 4
- S-2026顺义一模: 3
- S-2024朝阳一模: 3
- S-2024海淀二模: 3
- S-2025西城二模: 3
- S-2025顺义一模: 3
- S-2026通州期末: 2
- S-2024朝阳期中: 2

## Second Batch: B03B Choice Second

Rationale: choice rows require full stem/options plus reliable answer pairing and trap logic. They remain blocked until independent verification.

- S-2025东城期末: 9
- S-2026顺义一模: 6
- S-2024朝阳期中: 6
- S-2025顺义一模: 6
- S-2026东城期末: 6
- S-2024海淀二模: 4
- S-2025丰台期末: 4
- S-2026通州期末: 4
- S-2026东城一模: 3
- S-2024朝阳一模: 2
- S-2024朝阳二模: 2
- S-2025西城二模: 1
- S-2024西城一模: 1
- S-2026朝阳期中: 1
- S-2025海淀期末: 1

## Hard Gates

- No row can enter student稿 in Batch03.
- `2024西城一模 Q11` correction remains binding: correct answer pairing is `B=①③`.
- `2025海淀二模 Q12/Q13` must keep answer-source locators.
- Archive skeletons are internal checking tools only.
