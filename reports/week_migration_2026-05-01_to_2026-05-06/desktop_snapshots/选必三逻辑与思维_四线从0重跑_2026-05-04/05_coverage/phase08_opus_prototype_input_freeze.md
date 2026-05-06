# Phase08 Opus Prototype Input Freeze

- freeze_time: 2026-05-05 00:15:57 CST
- source_packet: `05_coverage/phase07_locked_opus_input_packet.csv`
- output_csv: `05_coverage/phase08_opus_prototype_input_freeze.csv`
- status: `FROZEN_FOR_PHASE08_REVIEW_ONLY_PROTOTYPE`
- prototype_status: `review_only`
- student_permission: `no`
- word_pdf_permission: `no`
- final_pass_permission: `no`

## Counts

- total Phase07 packet rows: 74
- include rows: 4
- include_as_packet_candidate rows: 25
- total prototype input rows: 29
- hold rows excluded from prototype: 45
- L0 rows excluded from Opus: 288

## Phase07 Permission Distribution

- hold_answer_locator_risk: 25
- hold_reasoning_form_risk: 20
- include: 4
- include_as_packet_candidate: 25

## Status Distribution

- L3: 70
- L4: 4

## Allowed Module Distribution

- 交叉: 5
- 思维: 13
- 推理: 11

## Hard Boundaries

- Opus may only rewrite/structure the 29 rows in this freeze file as a review-only teaching prototype.
- Opus may not add questions, delete questions, change answers, change source locators, change L3/L4 status, change cross pairing, or promote a hold row.
- `hold_answer_locator_risk`, `hold_reasoning_form_risk`, and all L0 rows remain excluded from prototype body.
- The output must keep `question_id` visible so Codex A and GPT can audit every line.

## Allowed Question IDs

- Q-2024朝阳一模-20-1 | 推理 | L3 | include_as_packet_candidate
- Q-2024朝阳一模-20-2 | 推理 | L3 | include_as_packet_candidate
- Q-2024朝阳一模-7 | 思维 | L3 | include_as_packet_candidate
- Q-2024朝阳一模-9 | 思维 | L3 | include_as_packet_candidate
- Q-2024朝阳二模-19-1 | 交叉 | L3 | include_as_packet_candidate
- Q-2024朝阳二模-19-2 | 交叉 | L3 | include_as_packet_candidate
- Q-2024朝阳期中-7 | 推理 | L3 | include_as_packet_candidate
- Q-2024朝阳期中-9 | 交叉 | L3 | include_as_packet_candidate
- Q-2024海淀二模-17-1 | 思维 | L3 | include_as_packet_candidate
- Q-2024海淀二模-17-2 | 思维 | L3 | include_as_packet_candidate
- Q-2024西城一模-19-2 | 推理 | L3 | include_as_packet_candidate
- Q-2024西城一模-19-3 | 推理 | L3 | include_as_packet_candidate
- Q-2024西城一模-19-5 | 推理 | L3 | include_as_packet_candidate
- Q-2025东城期末-13 | 推理 | L3 | include_as_packet_candidate
- Q-2025丰台期末-7 | 思维 | L3 | include_as_packet_candidate
- Q-2025丰台期末-8 | 思维 | L3 | include_as_packet_candidate
- Q-2025海淀二模-20 | 思维 | L4 | include
- Q-2025海淀期末-17-1 | 思维 | L3 | include_as_packet_candidate
- Q-2025海淀期末-18 | 思维 | L3 | include_as_packet_candidate
- Q-2025西城二模-16-2 | 推理 | L4 | include
- Q-2025西城二模-16-3 | 思维 | L4 | include
- Q-2025顺义一模-7 | 推理 | L3 | include_as_packet_candidate
- Q-2026东城一模-19-4 | 思维 | L3 | include_as_packet_candidate
- Q-2026丰台一模-18-2 | 推理 | L4 | include
- Q-2026朝阳期中-20 | 思维 | L3 | include_as_packet_candidate
- Q-2026朝阳期中-21-2 | 思维 | L3 | include_as_packet_candidate
- Q-2026通州期末-19-2 | 推理 | L3 | include_as_packet_candidate
- Q-2026顺义一模-19-1 | 交叉 | L3 | include_as_packet_candidate
- Q-2026顺义一模-19-2 | 交叉 | L3 | include_as_packet_candidate
