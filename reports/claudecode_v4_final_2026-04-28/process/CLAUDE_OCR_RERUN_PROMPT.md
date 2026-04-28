你现在继续“必修四哲学材料-知识触发框架 v4”的 OCR-needed 回收任务。不要把这次当作聊天答复，要直接在本地文件里工作。

本次运行要求：

1. 模型要求：使用当前命令指定的 Opus / max effort。不要降级为 Sonnet。若你能检测到实际不是 Opus，请立刻写入 `outputs_v4/ocr_rerun/STOP_MODEL_MISMATCH.md` 并停止。
2. 不许抄旧 v2/v3 结论。旧缓存只能作为索引，不能作为证据。证据必须来自本套试卷、答案、细则、评标、讲评或 OCR 后的页面。
3. 遇到 `ocr-needed` 不许继续留待办。必须尝试渲染扫描 PDF 页面并逐页读取；如果无法视觉读取，要写清楚工具缺口和已经生成的页面图片位置。
4. 不许把答案喂到嘴边后只改一小句。每套都要回到整套试卷、整份细则、整份答案/评标，从来源重新判断。
5. 主观题进入框架的硬标准：完整设问、材料触发词/句、知识解释、具体答案落点、细则摘录或明确边界。答案落点必须是这道题能写进答案的实际句子，不得写“要回应设问”“服务设问”这种空话。
6. 选择题进入补充库的硬标准：题面+选项+可靠答案键齐全；正确项触发逻辑、错肢错误类型和边界都要能回到材料/选项。
7. 最终学生版规则暂不改动最终 Word；本次先生成 OCR 回收中间成果和审计文件。不要在学生版中留下路径、line id、file id、slide id、OCR/debug 日志。

项目根目录：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27`

核心输入：

- `outputs_v4/codex_claude_compare/08_OCR-needed重跑控制清单.md`
- `outputs_v4/SUITE_REVIEW.csv`
- `outputs_v4/FOLLOWUP_OR_BLOCKED_ITEMS.csv`
- `outputs_v4/suite_bundles/`
- `outputs_v4/extracted_texts/`
- 本地原始三年试卷目录：
  - `/Users/wanglifei/Desktop/2024模拟题`
  - `/Users/wanglifei/Desktop/2025模拟题`
  - `/Users/wanglifei/Desktop/2026模拟题`

可用 PDF 渲染依赖：

系统没有 `tesseract/ocrmypdf/pdftoppm`。我已安装 PyMuPDF 到：

`/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/python_libs`

如需渲染 PDF，可使用：

`PYTHONPATH=/Users/wanglifei/Desktop/claude_bixiu4_independent_rerun_2026-04-27/outputs_v4/ocr_rerun/python_libs /Users/wanglifei/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3`

你应优先处理以下任务：

## 第一优先级：整套 OCR 漏项回收

逐套处理，并为每套写一个结果文件：

- `outputs_v4/ocr_rerun/S001_2024东城一模.md`
- `outputs_v4/ocr_rerun/S009_2024丰台二模.md`
- `outputs_v4/ocr_rerun/S038_2026丰台一模.md`
- `outputs_v4/ocr_rerun/S040_2026房山一模.md`
- `outputs_v4/ocr_rerun/S042_2026海淀一模.md`
- `outputs_v4/ocr_rerun/S048_2026丰台期末.md`
- `outputs_v4/ocr_rerun/S050_2026朝阳期末.md`
- `outputs_v4/ocr_rerun/S052_2026海淀期末.md`

每个结果文件必须包含：

- 已读取的原始文件清单；
- OCR/渲染方式和页面范围；
- 可进入 framework_entries 的条目，按原框架节点组织，不按题号流水账；
- 每条的完整设问、材料触发句、为什么触发、答案落点、细则/评分对应；
- 不能进入的题目及原因。

## 第二优先级：误判修复

处理：

- `S046_2026顺义一模`

这套不是缺文件。试卷 PDF 可读，细则 PPTX 第 2 页有 Q16 评分内容，PPTX 第 1 页有 1-15 答案键。请直接回源修复 Q16，并补可闭环的选择题。

输出：

- `outputs_v4/ocr_rerun/S046_2026顺义一模_误判修复.md`

## 第三优先级：真缺源记录，不许伪造

核查但不得硬写：

- `S044_2026西城一模`：缺 1-15 客观题答案键。
- `S053_2026西城期末`：本地 `试卷/`目录无试卷正文，只有参考答案、评标、细则。
- `S055_2026石景山期末`：本地只见答案及评分参考，无试卷正文。

先在本地重复目录、压缩包、已有 benchmark/cache 中搜索；若仍找不到，写：

- `outputs_v4/ocr_rerun/SOURCE_MISSING_CONFIRMED.md`

## 汇总文件

完成或阶段性完成后，写：

- `outputs_v4/ocr_rerun/OCR_RERUN_RESULTS.md`
- `outputs_v4/ocr_rerun/OCR_RERUN_AUDIT.md`

`OCR_RERUN_RESULTS.md` 面向合并，内容要干净；`OCR_RERUN_AUDIT.md` 保留路径、渲染、OCR、边界判断等审计信息。

现在开始。先读取 `08_OCR-needed重跑控制清单.md`，确认 A/B/C 三类，然后从 S042 和 S001 优先开始：S042 是用户刚刚点名怀疑“物质决定意识”走偏的关键套卷，S001 是最早整套 OCR 漏项。

