你现在继续执行“必修四哲学三年模拟全触发全链条”OCR-needed 漏项回收。上一轮 S001 被中断，是因为指令把“不要沿用旧结论”说得太粗，导致你倾向于重复转换源文件。现在纠正：旧分析结论不能当证据；但从原始试卷、答案、细则转换出来的 txt、suite bundle、render 图片属于一手来源缓存，必须优先使用。

# 模型与工作方式

- 你当前应由外部用 Opus 4.7 / adaptive 或 max effort 启动；如果 CLI 只能传 `--model opus --effort max`，请在运行日志里确认真实模型为 Opus 系列。
- 本轮唯一任务是 `S001 / 2024东城一模`，不得跳卷，不得处理下一套。
- 必须 cache-first：先读已有可读缓存、bundle、render 页面；只有缓存缺失、不完整或无法支持证据判断时，才回到原始 PDF/PPT/Office 文件。
- 不得沿用旧版 v2/v3/v4 的分析结论、旧 candidate json、旧框架条目、旧 CSV 推断作为证据。它们最多只能作为“可能需要复核的线索”。
- 如果长时间卡住，先根据进程状态、stream-json 增量、debug log、输出文件 mtime、tool call、网络/auth 错误判断是否真卡住；不要因为可见正文停顿就自我终止。确实需要重启时，优先重启同一套完整卷或写 checkpoint，不要把任务改成只处理别人摘好的片段，也不得绕过 S001 跳下一套。

# S001 已确认的一手来源缓存

请按以下顺序使用：

1. `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/suite_bundles/S001_2024东城一模.txt`
2. `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/suite_focus_bundles/S001_2024东城一模.txt`
3. `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/extracted_texts/S001_2024东城一模_scoring_rubric_4b2073bcc9e2_细则.pptx.txt`
4. `/Users/wanglifei/Desktop/政治模拟题_故事化返工_20260427_Codex重做_v2/00_benchmark_15/texts/2024东城一模_rubric.txt`
5. `/Users/wanglifei/Desktop/政治模拟题_故事化返工_20260427_Codex重做_v2/00_benchmark_15/texts/2024东城一模_paper.txt`
   - 注意：这个 paper txt 可能是 0 字节。若为空，要在审计中记录“paper txt cache empty”，然后使用已渲染图片补证。
6. 已有渲染图片，不要重复渲染：
   - `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/rendered_pages/S001_2024东城一模/page_*.png`
   - `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/rendered_pages/S001_2024东城一模_split/page*_strip*.png`
   - `/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/rendered_pages/S001_2024东城一模_ans/page_01.png`

只有这些缓存仍不能确认完整设问、材料关键句、题号、答案键或图像信息时，才打开原始源文件，并在审计里写明为什么缓存不够。

# 本次要解决的 S001 漏项

请从整套卷与整套细则出发复核，不要只看以下关键词；但以下位置必须查清：

- 第16题/中华文明新形态：必须补全完整设问，材料摘取触发关键句；核清哲学点与文化点边界。
- 传统产业与未来产业/新质生产力：必须查清题号、完整设问、材料触发句；不能留下“题号待补证”。
- 首都都市圈/通勤圈/功能圈/产业圈：必须查清题号、完整设问、材料触发句；不能只抄细则。
- 客观题：必须尽力从试卷与答案键确认第1-15题中涉及必修四哲学的题号、答案和错项。若答案 PDF 图片只给答案键，就记录证据边界；不能凭细则反推选择题。

# 主观题输出硬标准

每个入框架条目必须写：

1. 原理方法论归属，放在用户原有框架节点下，不要按题号组织。
2. 完整设问，一字不偷懒；材料只摘触发该原理的关键句，但要足够让学生看懂。
3. 材料触发句/触发词。
4. 触发逻辑：从知识上解释“材料里的哪句话/哪种关系为什么会想到这个原理方法论”。不要写“因为细则写了所以可以放”。
5. 回应设问：必须写成能放进答案的具体逻辑链。比如“因为 A 原理，所以材料中 B 主体应/能够/需要 C，最终回答题目问的 D”。不能写“本原理用于回应设问”这种空话。
6. 细则摘录/参考答案边界：这里才放“细则如何支持或限制归属”。
7. 若证据不足，写“待补证据/边界排除”，不得硬塞。

# 选择题输出硬标准

每个选择题条目必须写：

- 题号、完整题面或足够复原的题干；
- 官方答案键来源；
- 正确项为什么对应某个哲学知识；
- 错项设错方式；
- 若图像/漫画/表格不可见，必须使用 render 图片读图，不得凭答案反推。

# 输出文件

请写入：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/S001_2024东城一模.md`

并追加/更新：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/OCR_RERUN_RESULTS.md`

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/OCR_RERUN_AUDIT.md`

审计文件可以出现路径、缓存名、页码、渲染日志；学生最终正文不得出现 source path、L24、F04、slide、OCR log 等工程信息。

# 质量底线

- 不得无中生有题号、题面、细则、答案键。
- 不得把“细则摘录”当成“触发逻辑”。
- “回应设问”必须是这道题的实际作答链条。
- 如果 S001 中某个旧版本条目不成立，要明确标注删除理由。
- 完成后给出简短结论：S001 是否回收成功、回收了哪些主观题/选择题、还有哪些证据仍缺。
