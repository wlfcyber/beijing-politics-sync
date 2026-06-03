# 选必二《法律与生活》预处理进度

日期：2026-04-30

## 2026-05-04 最终交付闭环

- [x] 已完成最终清洁交付版：`delivery/选必二法律题处理合集_最终交付版_2026-05-04.md/.docx/.pdf`。
- [x] 已完成最终清洁框架版：`delivery/选必二法律与生活最终进化框架_最终交付版_2026-05-04.md/.docx/.pdf`。
- [x] 最终入框法律题 `112` 道：主观题 `43` 道、选择题 `69` 道；选择题答案待锁 `0`。
- [x] 已剔除 2025 顺义一模第21题：该题为家风/文化综合题，非显性法律设问，无对应法律细则锁定，不进入最终法律题框架。
- [x] 已完成 Codex、ClaudeCode、Claude Opus 4.7 Adaptive、ChatGPT 网页 Pro 四线留痕与融合裁决。
- [x] 已完成 Governor 与 Confucius：`governor_confucius/FINAL_GOVERNOR_CONFUCIUS_STATUS_2026-05-04.md`。
- [x] 已完成最终验收报告：`delivery/FINAL_ACCEPTANCE_REPORT_2026-05-04.md`。
- [x] DOCX 结构读取通过；PDF 由 PyMuPDF 生成并经 pypdf/PyMuPDF 读取与页面预览验证。

- [x] STEP_01: 已按用户要求删除旧选必二独立产物、旧选必二监管报告、旧选必二选择题处理台账、旧连续任务目录；保留原始试卷资料和总路由 skill。
- [x] STEP_02: 已建立本轮新目录、小本本、任务说明、开发计划、进度文件、空台账和预处理脚本。
- [x] STEP_03: 已从原始三年模拟题资料池扫描套卷、试卷、细则、答案、评标、阅卷总结和讲评材料，共扫描 `54` 套。
- [x] STEP_04: 已判定含选必二 / 无选必二 / 不确定套卷；确认无选必二套卷 `3` 套，不确定或缺 OCR/转换 `15` 条。
- [x] STEP_05: 已对确认或疑似含选必二的套卷自动锁定法律选择题和主观题候选题号，共 `85` 个候选题。
- [x] STEP_06: 已为主观题候选项匹配对应细则原文；未匹配或证据不足项目写入 `MISSING_OR_UNCERTAIN.md`。
- [x] STEP_07: 已为自动锁定的选择题生成“两层结构”预处理，共 `48` 道选择题；主观题预处理 `37` 道。
- [x] STEP_08: 已输出 Markdown/CSV 与扫描摘要；下一轮需人工抽查若干套，修正 OCR/自动抽题误差。

## 2026-05-03 v2 返工

- [x] 已判定旧预处理不能作为正式证据源继续使用：存在证据等级误标、选择题 rubric 串段、题号切分错误和非选必二误吸风险。
- [x] 已新增独立脚本 `scripts/preprocess_xuanbier_v2.py`，输出到 `preprocess_v2_2026-05-03/`，不覆盖旧 CSV/MD。
- [x] 已新增 `scripts/curate_preprocess_v2.py`，将 v2 raw 候选分为 `FORMAL_ACCEPTED / ACCEPTED / DEFERRED / REJECTED`。
- [x] 当前正式框架可用池为 `preprocess_v2_2026-05-03/curated/FORMAL_ACCEPTED_SUBJECTIVE_SOURCE_PACKS_V2.csv`：20 道主观题，全部 `formal_or_scoring_source`。
- [x] `18.4千克` 被误切成第18题的问题已修正；混合模块题已从 accepted 移入 deferred，等待拆分小问。
- [ ] 下一步：用 `FORMAL_ACCEPTED_*` 重跑框架样本；用 `DEFERRED_*` 做 OCR/小问拆分和缺细则补丁。

## 2026-05-03 全量法律题合集与本地框架稿

- [x] 已新增 `scripts/build_legal_collection_and_framework.py`，从 v2 题源、curated 闸门和 `text_cache` 二次检索生成全量法律题解释链。
- [x] 已输出 `final_legal_outputs/选必二法律题全量处理合集_2026-05-03.md`：入册法律题 `94` 道，含设问、材料触发、细则/答案锚点、答案落点、命题逻辑、完整解释链。
- [x] 已输出 `final_legal_outputs/选必二法律与生活最终进化框架_2026-05-03.md`：保留一核二线三问四步，把 `94` 道题全部回填到框架节点。
- [x] 已输出 `final_legal_outputs/legal_question_chain_ledger_2026-05-03.csv` 和 `FRAMEWORK_PLACEMENT_MATRIX_2026-05-03.csv` 作为 QA/追溯台账。
- [x] 客观题答案已全部从同套试卷/细则/答案表文本层锁定；当前 `choice_answer_pending=0`。
- [x] 已生成同名 `.docx` 结构版；`unzip -t` 与 `python-docx` 结构读取通过。
- [ ] 本机缺少 `soffice/LibreOffice` 且无 `brew`，暂无法执行 documents skill 的 DOCX 渲染成图 QA；当前 Word 版为结构验证通过，正式排版验收待有渲染器后补跑。
- [ ] 真实 GPT-5.5 Pro 网页端与 Claude Opus 4.7 Adaptive Thinking 网页端交叉审议尚未完成，故当前框架仍为本地证据稿，不标 Governor PASS。
- [ ] 少数扫描或题面未锁套卷仍需 OCR/人工回原文件复核，当前输出已在文件尾部列出。

## 2026-05-04 四线纠偏与候选融合

- [x] 已纠正 2026-05-03 旧统计：当前入框法律题为 `113`，不是 `94`；客观题官方答案待锁为 `9`，不是 `0`。
- [x] 已真实回收并落盘 Claude Opus 4.7 Adaptive 网页初评与对 GPT 的交叉批判。
- [x] 已真实回收并落盘 ChatGPT 网页 Pro 模式初评与对 Claude 的交叉批判；UI 未逐字显示 GPT-5.5 Pro，已在 gate 文件如实标注。
- [x] 已完成 ClaudeCode B 独立生产线，输出 `CLAUDECODE_B_*` 文件。
- [x] 已修正框架：保留用户原始“一核二线三问四步五域”，前台五域合计 `113`，后台八域只作索引。
- [x] 已把命题路径改成 6 类：裁判依据题、程序救济题、表格补全题、观点评析题、意义认识题、选择题。
- [x] 已刷新两份 Markdown 与 DOCX，并生成 `fusion/CODEX_LOCAL_MODEL_COUNCIL_FUSION_2026-05-04.md`、`00_control/FOUR_LANE_GATE_STATUS_2026-05-04.md`、`delivery/FINAL_ACCEPTANCE_REPORT_2026-05-04.md`。
- [x] DOCX 已通过 `unzip -t`、`python-docx` 结构读取、Microsoft Word 打开保存、Quick Look 首屏缩略图检查。
- [ ] `soffice` 缺失，`render_docx.py` 全页 PNG 渲染未通过；Word 导出 PDF 尝试无产出，已中止。
- [ ] Final Governor PASS 阻塞：`rubric_match_pending=26`、`choice_answer_pending=9`、`included_needs_review=14`。
- [ ] Confucius 学会性闭环阻塞：当前两份交付仍含后台审计语言；若要学生最终版，需要另抽 clean student artifact。
