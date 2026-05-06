你是 GPT-5.5 Pro，担任“飞哥政治庄园”选必三《逻辑与思维》四线从0重跑的总指挥/内容审稿人。

你需要基于下面的阶段报告，判断是否允许进入下一阶段：全量逐套逐题扫描与分类。请严格审稿，不要安慰。

背景：
- 工作目录：/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04
- 本轮要求：完全模仿成功的哲学宝典工作流；从0开始；旧稿只可定位，不继承结论；思维部分按哲学宝典式“材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题”；推理部分按“题型 -> 规则 -> 常见陷阱 -> 同类真题归档 -> 解题动作”；不准偷懒；最终要直接达到终稿级别。
- 四线：Codex 总控+生产；ClaudeCode 独立生产/复核；GPT-5.5 Pro 作为阶段指挥/内容压力测试；Claude/Opus 后续负责成文化但必须等证据锁定后。
- 你上轮给出 CONDITIONAL GO：只允许 source inventory、coverage/diff、reasoning attachment、有限样本回源；禁止学生稿、Word/PDF、PASS。

本阶段完成事项：

1. 用户上传框架 PDF 学习
- 思维框架 PDF：14页，文本层薄，已全部渲染页面并视觉初读。
- 推理框架 PDF：21页，文本层薄，已全部渲染页面并视觉初读。
- 产物：02_extraction/framework_pdfs/framework_visual_digest.md
- 结论：思维部分可仿哲学宝典做“材料信号 -> 可写思维/方法 -> 答题动作 -> 来源例题”；推理部分必须按题型树整理，不能只写抽象总结。

2. 五个硬样本 Codex lane A 回源
- HS01 2026顺义一模 Q19(2)：科学思维特征，锁客观性+预见性+可检验性。
- HS02 2025海淀二模 Q20：辩证思维，原卷文本层弱，已视觉核读；细则/讲评/评标锁定三个可选角度池。
- HS03 2026朝阳期中 Q21(2)：创新思维，锁超前+联想+逆向/转换性思考，发散+聚合为有效路径。
- HS04 2026通州期末 Q11：选择题，锁完整题干四选项与答案C，考感性具体->思维抽象->思维具体。
- HS05 2026东城期末 Q17(2)：推理部分，形式逻辑综合，锁矛盾律+充分条件假言推理误用+三段论中项不周延。
- 产物：03_entries/phase02_hard_sample_entries_internal.md, 05_coverage/reasoning_question_attachment_matrix.csv, COVERAGE_MATRIX.csv 五行初表。

3. ClaudeCode lane B 独立复核
- ClaudeCode 按指令没有读取 Codex 的 Phase 02 结论，独立处理五个硬样本。
- 产物：
  - claudecode_lane/phase02_hard_sample_crosscheck.md
  - claudecode_lane/phase02_hard_sample_matrix.csv
  - claudecode_lane/phase02_disagreements_and_blockers.md
  - 04_suite_reports/claudecode_suite_reports/phase02_hard_samples_report.md
- ClaudeCode 结论总体一致，但提出 5 个分歧候选和 4 个阻塞项。

4. Codex A/B 融合裁决
- 产物：06_conflicts/phase02_AB_fusion.md, resolved_conflicts.md, unresolved_conflicts.md。
- 关键裁决：
  - HS01 LOCKED：科学思维三特征。
  - HS02 LOCKED_PENDING_VISUAL：辩证思维三个可选角度池，不是三点全必答。
  - HS03 LOCKED：创新思维多路径，逆向/转换性合并，发散+聚合是有效路径。
  - HS04 LOCKED：选择题答案C，必须保留四选项和陷阱解析。
  - HS05 LOCKED：推理部分，不入思维主链。

5. 重要纠错：HS02 海淀二模 Q20
- ClaudeCode 矩阵里一度写成“3点×2分/2+2+2”，Codex 二次回源后修正。
- 主细则表格显示三个角度：分析与综合/系统优化/整体性；质量互变/动态性；辩证否定。
- 讲评 PDF 明确：从3个角度选择2个，每一角度按照1+2赋分。
- 评标实录明确：辩证否定显然有效；辩证思维特征角度可替代给分。
- 融合结论：最终文档应把 HS02 写成“三个可选角度池，优先选材料最顺的两条写深；辩证否定是高价值补充/替代角度”，不能写成三点全部必答。

6. 优先队列源文件批量抽取
- 从 01_source_inventory/PRIORITY_SOURCE_QUEUE.md 读取原始源文件 56 个。
- 全部 extracted，missing=0，errors=0。
- 类型：PDF 21、PPTX 17、DOCX 17、RTF 1。
- 方法：PDF 用 PyMuPDF 文本+命中页渲染；PPTX 用 python-pptx；DOCX 用 python-docx；RTF 用 textutil。
- 产物：02_extraction/priority_queue_sources/priority_queue_extraction_manifest.csv, text/, renders/。
- 意义：当前优先队列已无文件形式借口，后续必须逐题穷尽。

当前未解除阻塞：
- HS02 原卷仍需最终视觉/模型审稿确认后才能进学生稿。
- HS01 Q19(1) 可能是推理候选，后续全量扫描要处理。
- PPTX 内嵌学生答卷图片/图形批注尚未全部视觉读取；若涉及边界案例必须补。
- top-level SOURCE_LEDGER.csv 仍含旧稿 locator 行，最终 PASS 前必须换成干净 raw-source registry。
- 全书 coverage 目前只做五个硬样本，不可声称穷尽。
- 2026二模在已扫 source roots 未发现，必须保持 missing/blocked，除非新文件出现。

请你给出：
1. 是否允许进入下一阶段“全量逐套逐题扫描与分类”？请用 GO / CONDITIONAL GO / NO-GO。
2. 下一阶段必须产出的文件清单。
3. 下一阶段扫描顺序：思维部分与推理部分怎么并行/分工。
4. 你认为现在最大的内容风险是什么。
5. 对 HS02 的融合结论是否同意；如果不同意，请指出应如何改。
6. 对推理部分宝典结构给出硬要求，避免它再次写成泛泛总结。
