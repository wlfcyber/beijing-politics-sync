你现在执行“必修四哲学三年模拟全触发全链条”OCR-needed 漏项回收。用户明确要求：本轮必须由 Claude Code 亲自跑，不要使用 Codex 自己写的结论替代。

唯一任务：S001 / 2024东城一模。不得跳卷，不得处理下一套。

工作目录：C:\bp_sync_visible
资料包目录：C:\bp_sync_visible\cloudcode\s001_windows_package
输出目录：C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28

重要禁止：
- 不要读取或沿用 C:\bp_sync_visible\reports\ocr_rerun_windows_2026-04-28；那是 Codex 临时审计草稿，不是你的证据。
- 不要读取旧 final_deliverables 或 artifacts 作为证据。旧结论最多只能当“可能要查的线索”。
- 不得凭旧框架、旧 CSV、旧候选项反推答案。

必须 cache-first。可用一手来源缓存和渲染页如下：
- C:\bp_sync_visible\cloudcode\s001_windows_package\suite_bundle.md
- C:\bp_sync_visible\cloudcode\s001_windows_package\rubric_source.md
- C:\bp_sync_visible\cloudcode\s001_windows_package\rubric_text.txt
- C:\bp_sync_visible\cloudcode\s001_windows_package\paper_pages\page_001.png 至 page_012.png
- C:\bp_sync_visible\cloudcode\s001_windows_package\answer_pages\answer_page_001.png

原始源文件如果缓存不够再打开：
- C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\试卷\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治试卷(1).pdf
- C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\其他材料\北京市东城区2023-2024学年度第二学期高三综合练习（一）思想政治答案(1).pdf
- C:\Users\Administrator\Desktop\2024各区模拟题\2024各区一模\2024东城一模\细则\2024东城一模细则.pptx

你必须完成：
1. 从整套卷和整套细则出发复核 S001，不只看关键词。
2. 第16题/中华文明新形态：补完整设问、材料触发句、哲学点与文化点边界、触发逻辑、具体答案落点、细则支持边界。
3. 传统产业与未来产业/新质生产力：查清题号、完整设问、材料触发句、模块边界；不得把非必修四设问硬塞进必修四。
4. 首都都市圈/通勤圈/功能圈/产业圈：查清题号、完整设问、材料触发句、哲学触发链、具体答案落点。
5. 客观题：从试卷和答案键确认第1-15题中涉及必修四哲学/文化的题号、答案和错项边界；不能凭细则反推选择题。
6. 输出结论必须说明：S001 是否回收成功；回收了哪些主观题/选择题；哪些旧条目应降级、删除或迁出；还有哪些证据缺口。

输出文件：
- C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\S001_2024东城一模.md
- C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\OCR_RERUN_RESULTS.md
- C:\bp_sync_visible\reports\ocr_rerun_claudecode_2026-04-28\OCR_RERUN_AUDIT.md

学生可读正文要求：
- 完整设问要抄全。
- 材料只摘触发关键句，但要足够学生看懂。
- 触发逻辑要解释“材料里的哪句话/哪种关系为什么想到这个原理方法论”。
- 回应设问必须写具体答案链：因为什么原理，所以材料中的主体应/能够/需要怎么做，最终回答题目问的什么。
- 不得出现 source path、hash、page、OCR log、debug 语句。

审计文件可以写来源路径、缓存名、页码和证据边界。

质量底线：
- 不得无中生有题号、题面、细则、答案键。
- 不得把“细则摘录”当“触发逻辑”。
- 不得把“参考答案/拓展答案/讲评角度”冒充正式评分细则。
- 如果某个旧版本条目不成立，要明确标注删除或降级理由。
