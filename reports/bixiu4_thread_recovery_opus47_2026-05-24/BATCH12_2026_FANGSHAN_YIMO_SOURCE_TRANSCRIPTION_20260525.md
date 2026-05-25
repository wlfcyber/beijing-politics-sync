# Batch12 Source Transcription - 2026房山一模

timestamp: 20260525_041022
operator: Codex recovery thread
suite: 2026房山一模
status: SOURCE_PACKET_PARTIAL_WITH_CHOICE_ANSWER_KEY_BLOCKER

## Source Files Checked

- paper PDF: `2026各区模拟题/2026各区一模/2026房山一模/2026北京房山高三一模政治.pdf`
- rendered paper pages: `preprocessed_corpus/renders/e37482eff39f3618/page_001.png` to `page_011.png`
- rubric/marking file: `2026各区模拟题/2026各区一模/2026房山一模/26 房山一模评标 全.docx`
- detail rule file: `2026各区模拟题/2026各区一模/2026房山一模/细则/2026房山一模细则.docx`

## Choice Questions Q1-Q15

The PDF has no text layer in the preprocessed cache and the available rubric/docx files only cover the subjective questions. No reliable official answer key for Q1-Q15 was found in the current source directory. Therefore Q1-Q15 were added to `FULL_QUESTION_COVERAGE_AND_PLACEMENT_MATRIX.csv` as per-question rows with `NEED_ANSWER_KEY_BATCH12`; none of these choice questions were inserted into the DOCX body.

Page map:

- Q1: `preprocessed_corpus/renders/e37482eff39f3618/page_001.png`
- Q2-Q4: `preprocessed_corpus/renders/e37482eff39f3618/page_002.png`
- Q5-Q7: `preprocessed_corpus/renders/e37482eff39f3618/page_003.png`
- Q8-Q10: `preprocessed_corpus/renders/e37482eff39f3618/page_004.png`
- Q11-Q13: `preprocessed_corpus/renders/e37482eff39f3618/page_005.png`
- Q14-Q15: `preprocessed_corpus/renders/e37482eff39f3618/page_006.png`

## Q16(2)

Prompt: 结合材料一和材料二，运用哲学知识，谈谈你对“因地制宜，本质就是实事求是”的理解。（7分）

Rubric paragraphs 13-21 support:

- 矛盾普遍性和特殊性的统一
- 一切从实际出发 / 开展调查研究 / 从客观存在的事物出发
- 尊重客观规律
- 发挥主观能动性
- 联系的观点 / 在大局中找准定位
- 高档要求：融入大局中找定位 / 系统 / 整体

Disposition: retain/register existing entries for 实事求是、规律与主观能动性、联系观、矛盾普遍性与特殊性; add/register 整体与部分.

## Q17

Rubric paragraphs 23-41 show Q17(1) is 民事法律关系 and Q17(2) is 法治知识. The value-related wording appears inside a law/rule-of-law answer path and is not a standalone 必修四价值观 placement.

Disposition: module-boundary excluded.

## Q18(1)

Prompt: 结合材料一，运用辩证思维方法，分析北京是如何通过科学治理实现“常态蓝天”的。（6分）

Rubric paragraphs 42-49 support:

- 整体性 / 分析与综合 / 联系 / 系统优化
- 矛盾分析法 / 具体问题具体分析 / 两点论与重点论统一 / 分析与综合
- 动态性 / 质量互变 / 发展
- 立足实践 / 注重实践

Disposition: retain/register existing 系统观念、量变质变、具体问题具体分析 entries; add/register 两点论与重点论.

## Q19

Prompt/rubric paragraphs 61-68 require 《当代国际政治与经济》 and discuss 海南自由贸易港封关助力国际循环.

Disposition: module-boundary excluded.

## Q20

Prompt: 结合材料，综合运用所学，谈谈你对“坚持依法治国和依规治党有机统一”的认识。

Rubric paragraphs 69-81 support:

- 矛盾等
- 联系 / 对立统一于中国式现代化建设进程中
- 认识与实践
- 系统优化等

Disposition: retain/register existing 系统观念 and 实践与认识 entries; add/register 矛盾就是对立统一.
