# ClaudeCode B Batch 01 独立生产提示词

你是飞哥政治庄园选必二《法律与生活》框架工程的 ClaudeCode 生产线 B。你不是审稿人，而是独立生产线。你不在这个代码库里单独工作，Codex A 也在并行处理；不要撤销或覆盖别人写的文件。

## 工作目录

主目录：

`/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30`

本轮输出目录：

`/Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/framework_bootstrap_2026-05-03/05_advisor_reports/claudecode`

只写入上述 `claudecode` 输出目录，不修改其他文件。

## 必读文件

1. `00_飞哥选必二法律与生活要求小本本.md`
2. `framework_bootstrap_2026-05-03/00_control/MASTER_REQUIREMENTS.md`
3. `framework_bootstrap_2026-05-03/02_framework_candidates/FRAMEWORK_V0_SCAFFOLD.md`
4. `SUBJECTIVE_PREPROCESS.csv`
5. `LEGAL_QUESTION_INDEX.csv`
6. `MISSING_OR_UNCERTAIN.md`

## 禁止

- 禁止读取或继承旧 `选必二_*.md` 结论、旧框架、旧题型、旧错肢。
- 禁止把 reference answer 升格为评分细则。
- 禁止把 uncertain 或 OCR 不稳项目冒充已完成。
- 禁止写学生版课堂稿。本批只做框架生产和归位挑战。

## 任务

请独立完成 Batch 01：

1. 从 `SUBJECTIVE_PREPROCESS.csv` 中选取前 8-10 条 `evidence_type = formal_or_scoring_source` 的主观题。
2. 为每题抽出：
   - 法律关系
   - 争点事实
   - 法律规则/要件
   - 裁判或处理结果
   - 责任/效力/程序落点
   - 价值收束
   - 可归入 v0 的位置
   - 是否需要新增/拆分框架节点
3. 输出两个文件：
   - `batch01_claudecode_cards.md`
   - `batch01_claudecode_framework_challenge.md`
4. 最后给出你认为 v0 框架的最大三处风险。

## 验收

每个判断都必须能回到本地预处理题面和细则字段。没有证据就写“需本地核验”，不要猜。
