# 心跳督工补丁：当前雏形成品不得封板，必须返修

本文件是 2026-05-02 02:22 心跳检查后的最高优先级补丁令，优先级高于 `CLAUDECODE_START_PROMPT.md`、`MASTER_REQUIREMENTS_FOR_CLAUDECODE_2026-05-02.md` 和 `SUPERVISOR_DIRECTIVE_2026-05-02.md`。

你已经生成了本轮雏形产物，但现在不得写 `TASK_COMPLETE`，不得告诉用户已完成。Codex 督工发现以下硬失败点，必须修完才能封板：

## 1. 学生版混入审计话术，必须全局清理

当前 `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.md` 出现了大量学生版禁词/审计话术，典型包括：

- `细则Q21...`
- `细则原文等值...`
- `细则示例答案逐字给出...`
- `细则参考答案强调...`
- `评标...`
- `参考答案...`

这些词不得出现在学生版的 `材料触发点`、`设问`、`为什么能想到`、`答案落点` 或节点占位说明中。审计来源只能留在 `audit/证据索引.csv`、`audit/问题与边界清单.md`、`rubric_excerpt`、`boundary_note` 等审计文件里。

必须做两件事：

1. 回到 `audit/entries/*.jsonl`，把学生字段里的 `细则/评标/参考答案/答案示例/可从...角度` 等来源话术移到审计字段，学生字段改写为材料信号和知识逻辑。
2. 重新生成学生版 Markdown 和 Word，确保学生版全文 `rg '细则|评标|参考答案|答案写|答案核|答案/补充|可从.*角度|/Users/|\\.pdf|\\.docx|\\.pptx|OCR|debug|slide|line id|file id|PASS|correct_option_chain|filled' outputs/*_学生版.md` 为 0 命中。若有文化材料词本身出现在材料内容中，可以保留；但文化节点、文化章节、文化功能原理不得进入最终哲学框架。

尤其要修复当前明确失败样例：

- `2024_朝阳_二模__Q16_2__价值观` 的 `材料触发点` 不能写 `细则参考答案强调...`，必须改成原题材料中的 AI 与人类未来关系、技术风险、伦理边界、为人类服务等真实材料信号。
- 所有以 `细则Q...`、`细则原文...`、`细则示例答案...` 开头或包含这些字样的 `为什么能想到` 必须改成“材料里的哪个词/关系/主体行动为什么触发这个原理”。
- 所有 `暂无稳定挂点；如有原题需要补入，请回到原题与评分细则补证据` 这类占位话术不得出现在学生版。无条目节点可以省略，或写成不带来源/审计话术的学生可读空节点说明。

## 2. `quality_check.py` 目前漏检，必须升级

当前 `scripts/quality_check.py` 报 0 issues，但学生版实际有大量 `细则` 字样，说明质检脚本不能作为最终验收依据。必须升级质检：

- 检查 `audit/entries/*.jsonl` 中学生字段：`材料触发点`、`设问`、`为什么能想到`、`答案落点`。
- 检查最终学生版 Markdown 文本。
- 禁止学生字段和学生版正文出现：`细则`、`评标`、`参考答案`、`答案写`、`答案核`、`答案/补充`、`可从.*角度`、`/Users/`、`.pdf`、`.docx`、`.pptx`、`OCR`、`debug`、`slide`、`line id`、`file id`、`PASS`、`correct_option_chain`、`filled`。
- `rubric_excerpt`、`boundary_note`、`evidence_path` 是审计字段，可以保留来源话术和路径，但不得被合成进学生版。

最终 `quality_check.py` 必须能抓住上述失败；修复后再跑到 0 issues。

## 3. `COVERAGE_MATRIX.csv` 仍为空，必须补齐

当前 `COVERAGE_MATRIX.csv` 只有表头：

`suite_id,question_no,question_type,is_philosophy,evidence_level,status,target_node,brief`

这是硬失败。必须从 `SOURCE_LEDGER.csv` 和 `audit/entries/*.jsonl` 重新生成 `COVERAGE_MATRIX.csv`，至少做到：

- 每个进入学生版的 entry 对应一行；
- module-boundary、reference-only、source-missing、excluded-by-skill-rule 等套卷边界至少有套卷级/题级占位行；
- 覆盖 54 行 ledger 中所有套卷，不能只有 audit/覆盖验收表.csv；
- `status` 使用受控词：`included`、`objective-key-only`、`module-boundary-excluded`、`reference-only`、`source-missing`、`ocr-needed`、`duplicate-or-drift`、`blocked`、`excluded-by-skill-rule`。

`audit/覆盖验收表.csv` 可以继续作为汇总表，但不能替代 `COVERAGE_MATRIX.csv`。

## 4. 未闭环套卷必须补边界报告

心跳检查显示：

- `SOURCE_LEDGER.csv`：54 套；
- `audit/entries/*.jsonl`：51 套；
- `suite_reports/*.md`：51 套；
- 缺少 entries/reports 的套卷：`2026_朝阳_期中`、`2026_丰台_期末`、`2026_通州_期末`。

如果这 3 套没有哲学可用题或缺评分证据，必须写套卷报告并在 `COVERAGE_MATRIX.csv` 标成 `module-boundary-excluded`、`reference-only`、`source-missing` 或其他受控边界，不能让它们在控制文件里消失。

## 5. FINAL_ACCEPTANCE_REPORT 过期，必须重写

当前 `FINAL_ACCEPTANCE_REPORT.md` 仍写“剩余 12 套未生成 entries / 未达终态”，但实际 entries 已到 51 套，suite_reports 也到 51 套，说明报告过期。

最终封板前必须重写报告：

- 写清 54 套 ledger、53 套候选处理、1 套 2026 石景山期末排除；
- 写清每套状态；
- 写清学生版 Markdown/Word 是否重新合成；
- 写清 `quality_check.py` 和独立 `rg` 禁词检查是否 0 命中；
- 写清 `COVERAGE_MATRIX.csv` 已补齐；
- 写清 Word 是否已用 Microsoft Word 打开、保存并验收；
- 只有全部通过后，才在文末写 `TASK_COMPLETE`。

## 6. Word 验收仍未完成

用户已登录并激活 Microsoft Word。最终 `.docx` 不能只由 python-docx 生成。

必须：

1. 重新生成 `.docx`；
2. 用 Microsoft Word 打开；
3. 保存；
4. 检查首页、前言页、正文禁词、图片显示、中文排版；
5. 可行时导出 PDF 或截图作为 `audit/word_validation/` 下的验收附件；
6. 把验收结果写入 `FINAL_ACCEPTANCE_REPORT.md`。

## 7. 收尾方式

不要从 0 重新扫描全部题源。当前 `audit/entries/*.jsonl`、`suite_reports/`、`source_excerpts/` 是本轮从 0 重跑产物，可以作为当前轮工作成果继续修复。你的任务是：补边界、清理学生字段、升级质检、重建覆盖矩阵、重新合成学生版、Word 验收、最终报告封板。

现在立刻执行。不得因为已经有 Markdown/Word 雏形就停止。

---

# 心跳督工补丁二：02:58 复查后的最终收口，不得漏掉控制文件

Codex 督工在 2026-05-02 02:58 左右复查到：前一轮返修已经解决了大部分硬失败，但还没有达到可封板状态。你本次重启后不要重新扫描全量题源，只做以下收尾验收和控制文件修复。

## A. 已通过但必须写进最终报告的事实

- `audit/entries/*.jsonl` 已覆盖 54 套 ledger；`suite_reports/*.md` 也已覆盖 54 套。
- 原先缺失的 `2026_朝阳_期中`、`2026_丰台_期末`、`2026_通州_期末` 已补齐 entries/reports，并已入 `COVERAGE_MATRIX.csv`。
- 独立 `rg` 检查学生版 Markdown：`细则|评标|参考答案|答案写|答案核|答案/补充|可从.*角度|/Users/|\.pdf|\.docx|\.pptx|OCR|debug|slide|line id|file id|PASS|correct_option_chain|filled` 为 0 命中。
- `python3 scripts/quality_check.py` 当前返回 0 issues。
- `audit/word_validation/claude_student.WordSaved.docx` 已存在，说明最终 docx 已经由 Microsoft Word 打开并保存过；`audit/word_validation/quicklook/claude_student.docx.png` 已存在，可作为版式截图附件。

你仍必须重新独立运行这些检查，并把结果写入最终报告，不能只引用本补丁文字。

## B. 当前仍未通过的硬失败

1. `COVERAGE_MATRIX.csv` 仍没有 `2026_石景山_期末` 行。该套卷按 SKILL 用户确认整套排除，但覆盖矩阵必须覆盖 ledger 中 54 套；请添加一行：
   - `suite_id=2026_石景山_期末`
   - `question_no=ALL`
   - `question_type=boundary`
   - `is_philosophy=no`
   - `evidence_level=user-confirmed-skill-rule`
   - `status=excluded-by-skill-rule`
   - `target_node=` 留空
   - `brief=用户已确认无可用评分细则，整套从所有模块主链排除`
2. `FINAL_ACCEPTANCE_REPORT.md` 还是旧快照，仍写“未达终态/剩余 3 套/agent 处理中”，必须重写为当前真实状态。
3. `GOVERNOR_CHECKLIST.md` 还是旧快照，仍写“47/53”“剩余 6 套”，必须更新为 54 ledger、53 候选处理、1 套 skill-rule 排除、entries/reports/COVERAGE 均闭环。
4. `PROGRESS.md` 仍保留旧的待办项，必须更新为当前真实完成/边界/验收状态。
5. Word PDF 导出尝试没有产出 `WordExport.pdf`，不要因此阻塞最终验收；原要求是“可行时导出 PDF 或截图”。若再次导出 PDF 成功，把 PDF 放进 `audit/word_validation/`；若仍失败，最终报告必须如实写：Microsoft Word 打开保存已完成，QuickLook 截图已生成，PDF 导出未成功且不作为硬阻塞。

## C. 最终封板门槛

完成 B 后必须再次运行：

1. `python3 scripts/quality_check.py`
2. 学生版 Markdown 独立禁词 `rg`
3. `COVERAGE_MATRIX.csv` 行数/状态检查，必须包含 `2026_石景山_期末` 的 `excluded-by-skill-rule`
4. `SOURCE_LEDGER.csv`、`audit/entries`、`suite_reports` 对齐检查
5. WordSaved docx 段落抽检和 `audit/word_validation/quicklook/claude_student.docx.png` 存在性检查

只有这些全部通过，才能在 `FINAL_ACCEPTANCE_REPORT.md` 文末写 `TASK_COMPLETE`。否则继续留“未达终态”，并写清具体未过项。
