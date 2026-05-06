你是 ClaudeCode Lane B，正在参与飞哥政治庄园-选必三《逻辑与思维》四线从0重跑。你不是唯一工作者，Codex Lane A 同时在做矩阵去重与证据拆分；请不要改动 Codex Lane A 的输出文件，不要覆盖 A 线矩阵，不要生成学生稿、Word、PDF 或最终 PASS。

## 本次补丁目标

只做两个窄补丁，修复 Lane B Phase03 的关键漏项/锁定项：

1. 2026丰台一模 Q18(2)：你在 Phase03 把 S15/2026丰台一模记为扫描阻塞，并误判 043 细则只见哲学/政治。现在必须独立核读原卷渲染页和 043 细则，确认这道选必三推理主观题。
2. 2025海淀二模 Q20 / HS02：Codex A 已视觉核读 008 原卷 page_07，但仍要求 Lane B 独立视觉确认，确认后才能解除“pending Lane B visual confirmation”。

## 最高规则

- 从0证据边界仍然有效：旧稿/旧结论不可作为证据。
- 只用本轮 run folder 中的原始抽取、渲染页、细则文本和你自己的核读结论。
- 不要因为 OCR 不完美就放弃；PDF 扫描题必须用 render 图片视觉核读。
- 本次只写补丁文件和 Lane B addendum，不写学生稿。
- 如果有不确定，写明 `LOCKED` 和下一步，不要猜。

## 必读证据

Run folder:

`/Users/wanglifei/Desktop/北京高考政治/选必三逻辑与思维_四线从0重跑_2026-05-04`

### 2026丰台一模 Q18(2)

原卷渲染页：

`02_extraction/priority_queue_sources/renders/042_Desktop_2026模拟题_2026各区一模_2026丰台一模_试卷_试卷.pdf/page_07.png`

细则文本：

`02_extraction/priority_queue_sources/text/043_Desktop_2026模拟题_2026各区一模_2026丰台一模_细则_细则.pptx.txt`

请重点核读 043 文本中 `SLIDE 35`、`SLIDE 36`、`SLIDE 40` 附近：

- 甲：必要条件假言推理；前提真实；符合必要条件假言推理肯定后件式；正确。
- 乙：三段论推理；“带动居民消费”作为大项在前提中不周延、结论中周延；犯“大项不当扩大”；错误。
- 变通答案给分：必要条件假言推理 1 分、有效式/肯定后件式 1 分、前提真实/材料分析 1 分；三段论 1 分、规则 1 分、大项不当扩大 1 分。
- 复练题中还出现 2024北京18 三段论：中项不周延。

你必须确认原卷 page_07 上 Q18(2) 的设问是否是“分别写出上述推理的类型，判断是否正确，并说明理由。（6分）”或等义表达，并把甲乙推理材料读成你的补丁证据。

### 2025海淀二模 Q20 / HS02

原卷渲染页：

`02_extraction/priority_queue_sources/renders/008_Desktop_2025模拟题_2025各区二模_2025海淀二模_试卷_试卷.pdf/page_07.png`

细则/评标/讲评文本：

`02_extraction/priority_queue_sources/text/009_Desktop_2025模拟题_2025各区二模_2025海淀二模_细则_细则.docx.txt`

`02_extraction/priority_queue_sources/text/010_Desktop_2025模拟题_2025各区二模_2025海淀二模_细则_补充材料_2025年海淀二模评标实录.docx.txt`

`02_extraction/priority_queue_sources/text/011_Desktop_2025模拟题_2025各区二模_2025海淀二模_其他材料_2025届二模考试讲评0510.pdf.txt`

你必须独立确认：

- 原卷 page_07 含 Q20，共享发展理念推进共同富裕，设问要求运用辩证思维知识。
- 细则给的是角度池，不是三点全必答。可用角度包括分析与综合/整体性、质量互变/动态性、辩证否定，矛盾分析法最多 2 分。
- 若你无法视觉确认原卷页，就维持 `LOCKED_PENDING_VISUAL` 并说明具体原因。

## 必写输出

请写以下 4 个文件：

1. `claudecode_lane/phase03_patch_fengtai_q18_2.md`
   - 原卷视觉核读结论
   - 043 细则核读结论
   - 推理题型归档：必要条件假言推理 + 三段论/大项不当扩大
   - 可进入推理题型库的规则口令、易错点、同类题链接
   - `PASS_TO_FUSION` 或 `LOCKED` 结论

2. `claudecode_lane/phase03_patch_hs02_visual_confirmation.md`
   - 原卷视觉核读结论
   - 009/010/011 三源一致性或冲突
   - HS02 能否解除 Lane B 视觉锁
   - `PASS_TO_FUSION` 或 `LOCKED` 结论

3. `claudecode_lane/phase03_laneB_patch_addendum.csv`
   - 字段：
     `question_id,suite_id,source_locator,原始题号,部分归属,题型,证据等级,视觉核读状态,primary_type,secondary_type,logical_form_or_thinking_chain,rule_slogan,trap_or_boundary,final_patch_status`
   - 至少包含 2026丰台一模 Q18(2) 和 2025海淀二模 Q20。

4. 在 `claudecode_lane/progress.md` 顶部追加本次补丁记录。

## 禁止

- 禁止生成学生版正文。
- 禁止写“最终完成”。
- 禁止把 2026丰台一模 Q18(2) 继续说成无选必三题，除非你核读原卷和 043 后能给出更强的反证。
- 禁止把 HS02 写成“三点全部必答”；它只能按角度池处理。
