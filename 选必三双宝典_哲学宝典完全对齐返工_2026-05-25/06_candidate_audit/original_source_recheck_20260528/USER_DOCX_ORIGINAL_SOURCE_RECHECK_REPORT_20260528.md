# USER_DOCX_ORIGINAL_SOURCE_RECHECK_REPORT_20260528

verdict: `V78_WITHDRAWN_RECHECKED_FROM_ORIGINAL_SOURCES`

## 范围

- 对象：用户校对 Word 的 84 条思维宝典正文。
- 方法：旧表只用于定位原始文件；逐条重新打开原试卷、原细则/评标/评分材料抽证后裁决。
- 输出表：`06_candidate_audit/original_source_recheck_20260528/USER_DOCX_ORIGINAL_SOURCE_RECHECK_ADJUDICATION_20260528.csv`。

## 源文件抽取

- 独立原题：42 道。
- 原始文件路径：80 个。
- 文本直接抽出：73 个；扫描/评标 PDF 文本为空需视觉页或既有 OCR 页辅助：7 个。
- 本轮不把旧正文、旧 source-lock 字段当裁决证据；只把它们当找原文件的路标。

## 裁决统计

- 总条目：84
- PASS_CORE_SUPPORTED: 24
- P3_PROMPT_MINOR_DELTA: 4
- P2_PROMPT_RESTORE_EXACT: 3
- ACCEPT_KEEP_NODE_REJECT_EXTRA_NOTE: 1
- P3_NOTE_VALIDITY_NOT_FULLY_BLOCKING_MOVE_TO_AUDIT: 38
- ACCEPT_KEEP_REJECT_OVEREXPANDED_NOTE: 2
- ACCEPT_KEEP_REWRITE_NECESSARY_NOT_SUFFICIENT: 3
- ACCEPT_KEEP_REJECT_WRONG_OFFICIAL_HINT: 5
- ACCEPT_SOURCE_WORDING_RESTORE_RENYONG: 1
- REJECT_CURRENT_NODE_MOVE_TO_发散思维与聚合思维: 1
- ACCEPT_AS_AUXILIARY_WITH_REDLINE_REMOVED: 1
- ACCEPT_KEEP_AFTER_ORIGINAL_RUBRIC_RECHECK: 1

## 关键裁决

- 第4条｜4. 2024海淀二模 第17题第（1）问（主观题）｜追求认识的客观性 -> 追求认识的客观性｜ACCEPT_KEEP_NODE_REJECT_EXTRA_NOTE：原卷只问“如何体现科学思维”，原细则支持客观性，同时还出现思路新/方法新/整体安排；但按用户框架不得把“方法更新/整体安排”做科学思维独立节点，本条只保留客观性，提示不进学生版。
- 第10条｜10. 2026西城二模 第18题第（4）问（主观题）｜追求认识的客观性 -> 追求认识的客观性｜ACCEPT_KEEP_REJECT_OVEREXPANDED_NOTE：原评标第18(4)问视觉页显示角度1为追求认识客观性；没有把可检验性、矛盾分析、发散聚合列为此角度给分点，相关提示过扩，删除。
- 第15条｜4. 2024丰台二模 第18题第（2）问（主观题）｜结果具有预见性 -> 结果具有预见性｜ACCEPT_KEEP_REWRITE_NECESSARY_NOT_SUFFICIENT：原细则表述为“准确预测冰雪经济发展前景是必要条件，但不是唯一条件”，并提示不要按充分条件评析；正文必须写成必要非充分/非唯一条件。
- 第21条｜1. 2025海淀二模 第20题（主观题）｜整体性 -> 整体性｜ACCEPT_KEEP_REJECT_WRONG_OFFICIAL_HINT：原细则把整体性/系统优化列为2025海淀二模第20题可用角度；“官方只采整体性+动态性+辩证否定、分析综合/量质变只是延伸”的提示不成立，删除。
- 第28条｜1. 2025海淀二模 第20题（主观题）｜动态性 -> 动态性｜ACCEPT_KEEP_REJECT_WRONG_OFFICIAL_HINT：原细则支持动态性/质量互变角度，提示中排除量质变的说法不成立，删除。
- 第30条｜1. 2025海淀二模 第20题（主观题）｜分析与综合 -> 分析与综合｜ACCEPT_KEEP_REJECT_WRONG_OFFICIAL_HINT：原细则明确出现分析与综合/系统优化/整体性，不能把分析与综合降为知识延伸，删除错误提示。
- 第31条｜2. 2024石景山一模 第19题第（3）问（主观题）｜分析与综合 -> 分析与综合｜ACCEPT_SOURCE_WORDING_RESTORE_RENYONG：原试卷 DOCX 设问为“任用一种辩证思维方法”，全文未检出“任选一种”；保留原卷字样，不擅自顺改。
- 第40条｜4. 2024丰台二模 第18题第（2）问（主观题）｜矛盾分析法 -> 矛盾分析法｜ACCEPT_KEEP_REWRITE_NECESSARY_NOT_SUFFICIENT：原细则表述为“准确预测冰雪经济发展前景是必要条件，但不是唯一条件”，并提示不要按充分条件评析；正文必须写成必要非充分/非唯一条件。
- 第41条｜1. 2025海淀二模 第20题（主观题）｜量变与质变 -> 量变与质变｜ACCEPT_KEEP_REJECT_WRONG_OFFICIAL_HINT：原细则支持质量互变/动态性，不采纳“量质变只是延伸”的提示，删除。
- 第44条｜1. 2025海淀二模 第20题（主观题）｜辩证否定 -> 辩证否定｜ACCEPT_KEEP_REJECT_WRONG_OFFICIAL_HINT：原细则支持辩证否定，本节点保留；错误官方提示删除。
- 第55条｜7. 2026西城二模 第18题第（4）问（主观题）｜三性与三新 -> 三性与三新｜ACCEPT_KEEP_REJECT_OVEREXPANDED_NOTE：原评标第18(4)问角度3为坚持创新思维：寻找新思路、新方法、新结果（或逆向思维）；不支持把该节点扩成可检验性、联系/矛盾、发散聚合，删除过扩提示。
- 第60条｜3. 2026东城一模 第19题第（4）问（主观题）｜联想思维 -> 发散思维与聚合思维｜REJECT_CURRENT_NODE_MOVE_TO_发散思维与聚合思维：原细则19(4)的创新思维分析明确写“坚持发散与聚合思维统一”，并另写超前思维；“联想”只在知识列表泛列，未作为分析得分点。本条从联想思维移到发散思维与聚合思维。
- 第69条｜5. 2024丰台一模 第19题第（2）问（主观题）｜发散思维与聚合思维 -> 发散思维与聚合思维｜ACCEPT_AS_AUXILIARY_WITH_REDLINE_REMOVED：原细则要求卷面具体研究方法必须写问卷调查法、访谈法等；发散聚合只能用于理由/拓展说明，不能当作“具体研究方法”。本条可保留但答案必须强调具体方法优先，红线转后台。
- 第79条｜7. 2025海淀期末 第18题（主观题）｜超前思维 -> 超前思维｜ACCEPT_KEEP_AFTER_ORIGINAL_RUBRIC_RECHECK：原细则PPT第23-24页除逆向、联想外，还列出发散/聚合与超前思维；超前角度对应京津冀公共服务功能新文化地标和资源共建共享条件，故不是纯自创，但学生版需提醒优先写更稳得分角度。
- 第84条｜12. 2024丰台二模 第18题第（2）问（主观题）｜超前思维 -> 超前思维｜ACCEPT_KEEP_REWRITE_NECESSARY_NOT_SUFFICIENT：原细则表述为“准确预测冰雪经济发展前景是必要条件，但不是唯一条件”，并提示不要按充分条件评析；正文必须写成必要非充分/非唯一条件。

## 结论

- V78 的最终声明撤回是必要的；本报告才是按原卷和细则重做后的裁决底表。
- 当前应先按表修正文稿：删除全部审稿提示块；第60条改挂；第31条修设问错字；第15/40/84条统一必要非充分表述；第10/55条删除过扩提示；第21/28/30/41/44条删除错误“官方只采”提示。
- 本报告仍只处理思维宝典；推理宝典未包含在本次84条裁决中。
