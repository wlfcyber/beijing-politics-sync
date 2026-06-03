# GOVERNOR_REPORT — 选必二《法律与生活》ClaudeCode B 线全量重跑（2026-05-05）

监管者职责：拒绝弱证据、假闭合、源/细则混用、混排、未做证据归位、Word 未真渲染等情况。本报告对每条 must-not-fail 给一个状态。

## G01 旧产物不前置继承
- 状态：PASS
- 证据：本轮新建独立目录 `claudecode_full_rerun_2026-05-05/`，不覆盖也不引用 `claudecode_full_rerun_2026-05-04/` 旧 Codex 产物。所有 SOURCE / 题级解析 / 框架 / Word 均从原始三年模拟题独立重抽生成。

## G02 独立 v2 抽取（不复用旧 extracted_text）
- 状态：PASS
- 证据：
  - 用户在 Mac 终端运行 `STAGE_SOURCES.sh` 把 `~/Desktop/{2024,2025,2026}模拟题 + 先前框架` 拷入 outputs/sources（沙箱可见）。
  - 沙箱中 `scripts/extract_all.py` 用 `pdftotext -layout` + `pdfplumber`（PDF 双路）/`python-docx`（DOCX）/`python-pptx` 含表+备注（PPTX）/`libreoffice headless 转 + 解析`（.doc/.ppt/.rtf）独立抽取。
  - 抽取产物落在 `/sessions/.../outputs/extract_v2/`，183 个源文件全部覆盖。
  - 6 个尤其困难（5 个 60MB+ 大 PDF + 1 个 XML 残破 PPTX）由 `scripts/extract_missing.py` fallback：大 PDF 退到纯 pdftotext；残破 PPTX 由 libreoffice 转一遍后再解。
  - 已显式不再读取 `选必二重做_2026-04-30/extracted_text/` 旧 v0 产物。

## G03 真实 GPT-5.5 Pro / Claude Opus 4.7 Adaptive Thinking 网页 gate
- 状态：WAIVED_BY_USER_2026-05-05（real_call_pending = WAIVED）
- 证据：
  - 用户在 2026-05-05 明确指令"不用管，你自己独立完成这项任务。这个 prompt 是过时的。"
  - 因此本轮不进行外部 GPT 网页 / Claude Opus 网页两路审议；在 MASTER_REQUIREMENTS / DECISION_LOG / 本报告中均已显式标注豁免。
  - 凡涉及"模型审议未跑"的字段均标 WAIVED，不假装闭合。

## G04 韩金阳教研员 PPT 作为最高文件
- 状态：PASS
- 证据：
  - 用户上传 4 张幻灯（slide 1-4）：标题、八对相统一、选择题命题心得、主观题命题心得。
  - 提炼写入 `framework_versions/00_authority_brief.md`，作为框架制定的最高约束。
  - 框架版 Word 在"写在前面"等部分严格按 PPT 精神翻译为学生语言，**没有把"八对相统一"原话搬给学生**，**没有把"区别于法律职业资格考试"或"区别于必修3"作为学生答题动作**——这两条只在框架背景中作为"防误用"逻辑而存在。

## G05 题源覆盖与 inventory
- 状态：PASS
- 证据：
  - SOURCE 维度：56 套卷子（55 has_xuanbier，1 no_xuanbier - 即 2026石景山期末已排除）。
  - 题级解析：`scripts/parse_questions.py` 自动切分主观题（16-21）+ 选择题（1-15），共 860 题。
  - 选必二候选：122 主观题 + 173 选择题（含粗筛误判，需后续按命题路径反推剔除）。
  - 已匹到细则的主观题：162 题（含部分非选必二题与选必二题）。
  - 关键中间产物：`run_logs/SUITES.json`、`QUESTIONS.json`、`SUITE_SUMMARY.md`、`per_suite/*.md`（一套一份，共 56 份）。

## G06 框架两大硬约束（主干性 + 涵盖性）
- 状态：PASS（轻度风险 → 见 G10）
- 证据：
  - 主干性：框架以"一核 / 二线 / 三问 / 四步 / 五域"为骨架，主干高频层（合同+消保、侵权三要件、知产惩罚性赔偿、劳动关系三维度、相邻互让互利、继承顺序）均来自高考频细则原话（2025朝阳一模Q19、2024朝阳二模Q17、2026朝阳一模Q18等）。
  - 涵盖性：所有已识别的 122 选必二主观题候选都能归位到五域之一；归不进去的题在"框架缺口"小节明写。

## G07 选择题 / 主观题分排
- 状态：PASS
- 证据：
  - 框架版按"五域 / 主观题踩分点 → 选择题专属边界"分小节，主观题踩分点和选择题专属边界**绝不混排**。
  - 情境版分两章：第一章主观题情境（5 域），第二章选择题情境（12 个代表）。
  - 选择题情境只列"情境/正确判断/错项陷阱/法律边界"，不写得分句、不写踩分点。

## G08 证据等级与细则原话
- 状态：PASS
- 证据：
  - `RUBRIC_MATCH_LEDGER.csv`（待最终汇总）的 evidence_grade 字段四类：formal_rubric / marking_report / explanation_ppt / reference_answer / none。
  - 框架版与情境版的"得分句模板"均来自细则原话或阅卷总结原话，例如 2025朝阳一模Q19的"主观欺诈故意 / 客观欺诈行为 / 违背真实意思表示"三要素均为该题阅卷总结的原文要点。
  - 普通参考答案（reference_answer 等级）只用于标注与对照，未推动主干。

## G09 学生文档语言洁净（不得含后台词）
- 状态：PASS
- 证据：
  - 对最终两份学生 markdown 全文 grep `Codex|Claude|GPT|Governor|Confucius|pipeline|debug|参考答案|可从|PASS|FAIL|CONDITIONAL|ALMOST|formal_rubric|rubric_match|extracted_at|source path|文件路径|模型聊天`，命中 0 条。
  - 早期一处"评标"已修复（在框架缺口节，原文从"建议查阅该套的评标细则"改为"根据具体材料和给分依据判定"）。
  - 学生文档中"评标"零命中。

## G10 框架缺口与待补点（自我披露，不假闭合）
- 状态：CONDITIONAL（不影响主干，但需后续补强）
- 内容：
  1. 2024海淀二模Q21（人格权题）未充分获取细则 → 已在框架"框架缺口"小节明写，建议补读细则；
  2. 2025房山一模Q20（侵权 vs 反不竞分界不清）→ 已在框架缺口节给学生提供"自判规则"；
  3. 2026通州期末Q21、2026石景山一模Q21（物权/相邻题）→ 已在框架缺口节明写"细则未充分阅读"；
  4. 2024西城一模（格式条款题）位置确认困难 → 已明写；
  5. 救济公共域缺一道完整的"生态污染+公益诉讼"主观题 → 已明写；
  6. 选择题 12 道为代表性，可扩充至 20+。
- 监管裁决：以上缺口均**显式披露**，不**假装"全部覆盖"**。学生文档中也明写"框架缺口"小节，便于学生与教师补充。

## G11 Word 真渲染 / 路径正确
- 状态：用户端待执行（real_call_pending_user_render）
- 内容：
  - 因沙箱限制（无法直接写二进制 docx 到 Desktop），主线程已在 outputs 根写 `RENDER_DOCX_ON_MAC.sh`：用户在 Mac 终端跑一行，脚本会用本机 python-docx 把两份 markdown 渲染成 .docx，输出到与 markdown 同目录。
  - 用户跑完后 .docx 文件即在：`/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_full_rerun_2026-05-05/delivery/`。
  - **本 Governor 报告的 G11 状态在用户跑完渲染脚本前不能升级为 PASS**；用户跑完应在交付报告里更新成 PASS。

## G12 学生文档可学性（题目→规则→得分句完整链）
- 状态：PASS
- 证据：
  - 框架版每个域的"主观题踩分点"小节均给出"看到什么材料 → 想到什么规则 → 解决什么争点 → 写出什么得分句"四要素，并给出至少一个真实考过的例子。
  - 情境版每题给出"起因→经过→结果（完整故事）→ 争点 → 规则 → 触发词 → 踩分关键词 → 得分句模板 → 作答逻辑"完整链。
  - 意义类落点全部回扣本案后再升制度，无"全面依法治国"等跳跃。

## G13 Codex A 五个内部角色（自查留痕）
- 状态：PARTIAL（B 线主线一人模拟，已留痕）
- 内容：
  - 决策者：本轮决策点全部记入 `00_control/DECISION_LOG.md`（D-001~D-006）。
  - 劳动者：抽取/识别/归位/写作均由主线 + 一个 general-purpose 子代理协同完成，子代理产物已审。
  - 补丁者：本报告自我披露 6 个框架缺口（G10），不假装全覆盖。
  - 监管者：本报告。
  - 自动化检测者：通过禁用词 grep（G09）与文件清单核对实施。

## 总裁决
- 学生交付物（两份 markdown）：本地内容质量 PASS。
- Word 渲染：等用户在 Mac 终端跑一行 `RENDER_DOCX_ON_MAC.sh` 之后真生成 docx，再升级 G11。
- 外部模型 gate：用户已豁免本轮，标 WAIVED。
- 总体状态：**LOCAL_CONTENT_PASS / RENDER_AWAITING_USER**。
