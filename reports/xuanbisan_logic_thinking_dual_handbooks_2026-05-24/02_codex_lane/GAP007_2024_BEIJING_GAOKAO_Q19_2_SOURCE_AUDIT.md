# GAP007 source audit: 2024 北京高考 Q19(2) 青海防沙治沙

Status: `source_identified_original_question_not_locked`

## Current finding

This row cannot be promoted into the student-facing thinking handbook yet.

The current run has a strong scoring-reference signal, but not the original paper/question text:

- Scoring-reference signal: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\gpt_sources\dbc93cbfd3a93eff_2026丰台期末细则.md:311-351`
- The local source explicitly labels the item as `24年北京高考19题 第二问`, with knowledge block `逻辑与思维`, ability block `解释与论证`.
- It gives rubric-like scoring points for scientific thinking, dialectical thinking, innovation thinking / divergent-convergent thinking / association / forward-looking thinking, plus a substitution note for strategic/system thinking.
- However, this file is a 2026 丰台期末细则 / commentary source, not the original 2024 北京高考 paper or official 2024 scoring source.

## Rubric signal captured

- Scientific thinking: `追求认识的客观性`; material link is 青海防沙治沙 recognizing objective laws in practice, mastering native species survival strategies, and providing scientific basis for sand prevention and control.
- Dialectical thinking: contradiction analysis, analysis and synthesis, correct handling of the relationship between humans and nature, wholeness, concrete analysis of concrete problems, unified in the process of sand prevention and control.
- Innovation thinking options: innovation thinking, divergent and convergent thinking, association thinking, forward-looking thinking; students may choose two angles and match the chosen method to material analysis about precise prevention/control and ecological construction.
- Substitution note: strategic thinking / system thinking may replace one angle when supported by material, but cannot be double-counted.
- Typical error signal: philosophy-module answer only receives low credit; this is a useful boundary warning for the 必修四 vs 选必三 overlap.

## Original-paper recovery check

Public source checked in this round:

- Page: `https://www.gaokzx.com/gk/shitiku/124914.html`
- Downloaded PDF: `https://cdn.gaokzx.com/17204312471322024%E5%8C%97%E4%BA%AC%E9%AB%98%E8%80%83%E6%94%BF%E6%B2%BB%E8%AF%95%E9%A2%98%E5%8F%8A%E7%AD%94%E6%A1%88.pdf`
- Local copy: `01_source_inventory/web_gaokao_2024_beijing_politics/2024北京高考政治试题及答案.pdf`

PyMuPDF text scan result:

- PDF has 14 pages.
- Search terms `青海`, `防沙`, `治沙`, `逻辑与思维`, `科学思维` do not recover this 青海防沙治沙 item.
- In this PDF, page 6 text shows Q19 as `法安天下，德润人心` legal cases, and page 12 answer text also treats Q19 as legal/infringement and emergency assistance, not 青海防沙治沙.

Therefore the public PDF currently available through this source is not a match for the GAP007 scoring-reference signal.

## Decision

Do not add this item to `MAIN_THINKING_LEDGER.csv` as a source-locked main-question row.

Do add a coverage/audit row so the gap does not disappear:

- evidence level: `missing`
- status: `source_identified_original_question_not_locked`
- decision reason: scoring-reference signal exists, but original 2024 Beijing paper text is not locked and a checked public PDF mismatches.

## Next action

Recover one of the following before promotion:

1. the original 2024 北京高考 paper page containing 青海防沙治沙 Q19(2);
2. an official or formal 2024 scoring source matched to that original question;
3. a verified image/render from a trustworthy 2024 北京高考 source showing the exact material and set question.

Until then, this item can only be used as an audit blocker and method-risk signal, not as a student-facing source-locked sample.
