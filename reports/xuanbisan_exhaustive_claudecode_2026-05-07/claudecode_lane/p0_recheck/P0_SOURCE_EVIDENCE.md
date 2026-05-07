# P0 Source Evidence - Codex Corrected

本文件覆盖 ClaudeCode 原始证据说明中的错误判断。ClaudeCode 曾把若干非空细则误判为“细则.pptx空”或讲评/教师版来源；Codex 已回源复核并修正。

## 021 · 2024 朝阳二模

- P0 rows: 3
- source: 2024朝阳二模试卷 + 2024朝阳二模细则.pdf
- evidence: Q19(1) 参考答案“①动态性 ②类比”；Q19(2) “该判断是联言判断”“当且仅当组成它的各个联言支都是真的”。
- level: A-formal

## 012 · 2025 东城期末

- P0 rows: 4
- source: 2025东城期末试卷 + 2025东城期末细则.pptx
- evidence: SLIDE 29 明确 Q18(2) 阅卷细则，第一层次“思路新、方法新、结果新/多向性、跨越性、独特性”1分；第二层次给出发散聚合、联想、超前三个方法点及给分规则。
- level: A-formal
- correction: ClaudeCode 把该组误降为 A-support；已恢复 A-formal。

## 044 · 2026 东城期末

- P0 rows: 3
- source: 2026东城期末教师版试卷；细则.pptx未提供Q17(2)主观细则。
- evidence: Q17(2) 三项主张题面 + 参考答案“运用矛盾律、充分条件假言推理、必要条件假言推理等逻辑规则进行分析”。
- level: A-support
- note: “三段论·中项不周延”由题面三段论结构与“等逻辑规则”支撑，后续融合需保守标注。

## 042 · 2026 丰台一模

- P0 rows: 2
- source: 2026丰台一模细则.pptx
- evidence: SLIDE 29 明确甲为必要条件假言推理肯定后件式、乙为三段论大项不当扩大；SLIDE 30 给出变通答案和1分级点位。
- level: A-formal
- note: 试卷PDF文本抽取空，学生稿仍需回原图补题面背景，但推理结构与评分点可由细则独立支撑。

## 006 · 2026 通州期末

- P0 rows: 3
- source: 2026通州期末试卷 + 2026通州期末细则.pptx
- Q11 evidence: 题面、四选项、答案表C齐全。
- Q19(2) evidence: SLIDE 4-5 明确推理①充分条件假言推理肯定前件式，推理②必要条件假言推理肯定前件式无效，并给出1分+1分+1分细则。
- levels: Q11 = B-choice-signal；Q19(2) = A-formal
- correction: ClaudeCode 把Q19(2)误降为 A-support；已恢复 A-formal。

## 001 · 2026 顺义一模

- P0 rows: 4
- source: 2026顺义一模试卷 + 2026顺义一模细则.pptx
- Q19(1) evidence: SLIDE 8 完整列出三段论推论、设问和阅卷细则；推理错误1分，前提不真实1分，推理结构正确1分。
- Q19(2) evidence: SLIDE 9 给出科学思维客观性、预见性、可检验性三条参考答案，并标明知识1分+材料1分。
- level: A-formal
- correction: ClaudeCode 把细则误判为空，并把Q19(1)判成source_insufficient；已改为 confirmed_with_patch，可进入fusion。

## Corrected Summary

| level | rows |
| --- | ---: |
| A-formal | 15 |
| A-support | 3 |
| B-choice-signal | 1 |
| source_insufficient / missing | 0 |

Total P0 rows: 19. Can enter fusion: 19. No Word/PDF generated. No final authorization.
