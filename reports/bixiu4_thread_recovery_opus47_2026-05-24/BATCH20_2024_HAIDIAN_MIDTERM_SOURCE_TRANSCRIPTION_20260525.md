# Batch20 Source Transcription - 2024海淀期中

Status: `SOURCE_REVIEW_CLOSED_MODULE_BOUNDARY`

## Source Packet

- Suite bundle: `C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区期中__2024海淀期中.md`
- Rubric/scoring source: `C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/gpt_sources/fee5258a9b7359d5_2024海淀期中细则.md`
- Paper source cache: `C:/Users/Administrator/Desktop/beijing_politics_research/data/preprocessed_corpus/gpt_sources/16c75dff224a222c_海淀区2024_2025学年第一学期期中练习政治试题.md`
- Original rubric PDF: `C:/Users/Administrator/Desktop/2024各区模拟题/2024各区期中/2024海淀期中/细则/2024海淀期中细则.pdf`
- Original paper PDF: `C:/Users/Administrator/Desktop/2024各区模拟题/2024各区期中/2024海淀期中/试卷/海淀区2024～2025学年第一学期期中练习政治试题.pdf`

## Cache Finding

- The suite bundle and rubric cache are readable and sufficient for module-boundary classification.
- The paper cache text is not readable for full question extraction. Because this batch does not add student-facing entries and the formal rubric gives the full module distribution plus Q18/Q19/Q20/Q21 scoring boundaries, no new DOCX prompt is generated from the bad paper cache.

## Formal Module Distribution

细则套卷结构表明：客观题1-6为必修2，7-11为必修3，12-15为选择性必修1；主观题16(1)、17、20为必修2，18、19、21(1)为必修3，16(2)、21(2)为选择性必修1。

## Q18 Misplacement Evidence

第18题细则明确知识板块为《政治与法治》基层民主，评分角度为党的领导、全过程人民民主、基层民主、协商民主/民主决策/民主监督/民主管理、多元主体共建共治；没有必修四哲学原理方法论。

Removed old DOCX entries:

- `系统观念 / 系统优化` -> `1. 2024海淀期中 第18题（主观题）`
- `矛盾的特殊性 / 具体问题具体分析` -> `2. 2024海淀期中 第18题（主观题）`
- `人民群众` -> `2. 2024海淀期中 第18题（主观题）`

## Decision

- No `2024海淀期中` question enters the 必修四哲学宝典正文.
- All questions are represented in the matrix as module-boundary rows.
- The three old Q18 philosophy entries are treated as misplaced and removed from the student-facing DOCX.
