你现在继续执行“必修四哲学三年模拟全触发全链条”OCR-needed 漏项回收。

唯一任务：S001 / 2024东城一模。不得跳卷，不得处理下一套。

本轮是同一套 S001 的重启，不是缩小任务。上一轮 v4 没有产出正文，失败原因是读取了超过 2000px 的高分辨率答案图，触发 many-image 请求限制。你必须仍然复核整套 S001，但要遵守下面的图片读取限制。

## 工作目录

- 工作目录：`C:\bp_sync_visible`
- 资料包目录：`C:\bp_sync_visible\cloudcode\s001_windows_package`
- 输出目录：`C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28`

## 重要禁止

- 不要读取或沿用 `C:\bp_sync_visible\reports\ocr_rerun_windows_2026-04-28`；那是 Codex 临时审计草稿，不是你的证据。
- 不要读取旧 final_deliverables 或 artifacts 作为证据。
- 不得凭旧框架、旧 CSV、旧候选项、旧模型总结反推答案。
- `visible_runs\claude_ocr_rerun_S001_windows_stream_v4.jsonl` 只能作为失败原因记录，不能作为题目、答案或结论证据。

## Cache-First 来源

先读这些一手来源缓存：

- `C:\bp_sync_visible\cloudcode\s001_windows_package\suite_bundle.md`
- `C:\bp_sync_visible\cloudcode\s001_windows_package\rubric_source.md`
- `C:\bp_sync_visible\cloudcode\s001_windows_package\rubric_text.txt`
- `C:\bp_sync_visible\cloudcode\s001_windows_package\paper_pages\page_001.png` 至 `page_012.png`
- `C:\bp_sync_visible\cloudcode\s001_windows_package\answer_pages\answer_page_001.png`

原始源文件只有在缓存不够确认完整设问、材料、答案键、细则边界时再打开：

- `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\试卷\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治试卷(1).pdf`
- `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\其他材料\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治答案(1).pdf`
- `C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\细则\2024东城一模细则.pptx`

## 图片读取限制

- 不要读取任何宽或高超过 2000px 的图片。
- 不要读取 `hires_pages\answer_p01.png`、`answer_top_zoom.png`、`answer_bot_zoom.png`、`answer_subj_left_top.png`、`answer_subj_left_bot.png`、`answer_subj_right_top.png`、`answer_subj_right_bot.png`、`answer_table.png`。
- 如果答案页小图不够清楚，只读这些小裁图：`crops\answer_page_001_top.png`、`crops\answer_page_001_bot.png`、`crops\answer_page_001_table.png`、`crops\answer_table_full.png`、`crops\answer_table_zoom.png`、`crops\answer_left_body.png`、`crops\answer_right_col.png`。
- 如果试卷小图某页不够清楚，可读这些小裁图：`crops\page_005_top.png`、`crops\page_005_bot.png`、`crops\page_006_top.png`、`crops\page_006_bot.png`、`crops\page_009_top.png`、`crops\page_009_bot.png`。
- 不要在同一轮工具调用里读超过 4 张图片。需要多页时分批读。

## 必须完成

1. 从整套卷和整套细则出发复核 S001，不只看关键词。
2. 第16题/中华文明新形态：补完整设问、材料触发句、哲学点与文化点边界、触发逻辑、具体答案落点、细则支持边界。
3. 传统产业与未来产业/新质生产力：查清题号、完整设问、材料触发句、模块边界；不得把非必修四设问硬塞进必修四。
4. 首都都市圈/通勤圈/功能圈/产业圈：查清题号、完整设问、材料触发句、哲学触发链、具体答案落点。
5. 客观题：从试卷和答案键确认第1-15题中涉及必修四哲学/文化的题号、答案和错项边界；不能凭细则反推选择题。
6. 输出结论必须说明：S001 是否回收成功；回收了哪些主观题/选择题；哪些旧条目应降级、删除或迁出；还有哪些证据缺口。

## 输出文件

- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\S001_2024东城一模.md`
- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\OCR_RERUN_RESULTS.md`
- `C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\OCR_RERUN_AUDIT.md`

## 学生可读正文要求

- 完整设问要抄全。
- 材料只摘触发关键句，但要足够学生看懂。
- 触发逻辑要解释“材料里的哪句话/哪种关系为什么想到这个原理方法论”。
- 回应设问必须写具体答案链：因为什么原理，所以材料中的主体应/能够/需要怎么做，最终回答题目问的什么。
- 学生可读正文不得出现 source path、hash、page、OCR log、debug 语句。

审计文件可以写来源路径、缓存名、页码和证据边界。

## 质量底线

- 不得无中生有题号、题面、细则、答案键。
- 不得把“细则摘录”当“触发逻辑”。
- 不得把“参考答案/拓展答案/讲评角度”冒充正式评分细则。
- 如果某个旧版本条目不成立，要明确标注删除或降级理由。
