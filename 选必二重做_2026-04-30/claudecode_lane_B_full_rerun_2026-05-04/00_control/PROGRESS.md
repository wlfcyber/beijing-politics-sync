# PROGRESS — ClaudeCode 生产线 B 独立重跑

## Round 1 — 2026-05-04

### 已完成
- 读取并锁定五份绑定文件：feige-politics-garden 总路由、book-orchestrator、xuanbier 分支、选必二小本本（含 2026-04-30、2026-05-03、2026-05-04 全部追加要求）。
- 工作区 AGENTS.md 在 `/Users/wanglifei/Desktop/北京高考政治/` 路径下不存在，规则内容由用户当面给出，已并入 MASTER_REQUIREMENTS。
- 三个源目录形态已盘点：
  - 2024模拟题：66 文件，150MB，14 套区考；2024 东城二模有"分题细则/阅卷总结"嵌套。
  - 2025模拟题：61 文件，94MB，三大类（一模/二模/期末）；含**显式阅卷总结 doc**（合同欺诈、社区治理等）。
  - 2026模拟题：50 文件，668MB；东城一模"评标细则（勿传）"含逐题 PPTX 卡组（16/17/19/20）— 单题级 L1 证据。
- 无 iCloud 占位文件；无现成 OCR 文本；全部需重做解析。
- 独立重跑目录已建：`claudecode_lane_B_full_rerun_2026-05-04/`，子目录 9 个（00_control / source_inventory / subjective / choice / framework_versions / situation_bank / claudecode_lane / governor_confucius / delivery）。
- 按本轮"不调外部模型"裁决，未建 gpt55_review/、opus47_review/、fusion/。
- 已写：MASTER_REQUIREMENTS.md（v1）、PROGRESS.md（本文件）、DECISION_LOG.md（v1）。

### 待办（按依赖顺序）
1. **Round 2**：源文件 OCR/解析与 SOURCE_LEDGER.csv 全量盘点（按套卷×文件×证据等级三维落库）。本轮决定：先用 docx/pptx 文本提取（python-docx, python-pptx）+ pdftotext + 必要时 OCR；阅卷总结 doc/讲评 pptx 列入 L1。
2. **Round 3**：逐套扫题、识别选必二题、产出 SUBJECTIVE_QUESTION_PACK.csv 与 CHOICE_QUESTION_PACK.csv 草表。
3. **Round 4**：每道主观题做命题路径反推 + 细则 RUBRIC_MATCH_LEDGER.csv。
4. **Round 5**：框架 v0 → v1 收敛（一核二线三问四步五域），生成 FRAMEWORK_PLACEMENT_MATRIX.csv 与 FRAMEWORK_GAP_LOG.md。
5. **Round 6**：情境穷尽 SITUATION_BANK 表（主观题 / 选择题分开）。
6. **Round 7**：本地 Governor 报告。
7. **Round 8**：Confucius 学生视角验收，必要时回到 4-6 修改。
8. **Round 9**：生成框架版 Word + 情境版 Word + PDF。
9. **Round 10**：FINAL_ACCEPTANCE_REPORT.md，三份学生文档洁净扫描。

### 阻塞 / 待用户裁决
- 暂无。Round 2 直接开扫源。

### 真实状态
- 本轮**未**做证据级工作；只完成准备与控制层。这不是"完成"，是"开工"。

## Round 2 — 2026-05-04 小样本试跑

### 已完成
- 解析栈选型 + 安装：python-docx / python-pptx / pdfplumber / rapidocr-onnxruntime（全部经 `pip install --user`）+ macOS 原生 `textutil`。无需 brew、LibreOffice、tesseract 二进制。
- 8 个测试样本全部跑通（A 阅卷总结doc / B 阅卷总结docx / C 评标pptx 单题 / D 试卷数字PDF / E 细则扫描PDF→失败 / F 评标pptx 多题 / G 补充材料数字PDF / H OCR兜底）。
- 写出 [EXTRACTION_TRIAL.md](source_inventory/EXTRACTION_TRIAL.md)，含每个测试结果 + 6 条关键陷阱。
- 真实证据样本已落盘 8 份在 `source_inventory/extraction_trial/`。

### 关键发现（影响 Round 3+）
- **题号不能信文件名**：识题阶段必须按题面内容过滤（`17(1).docx`/`19(1).pptx`/`18+选择7、13.pptx` 三个真实陷阱）。
- **L1 证据池超预期丰富**：2025 朝阳一模阅卷总结 doc + 2026 东城一模"评标细则（勿传）"PPTX 都含"不重复给分""材料3个条件必须写全""'保护法'不给分"等极硬卡口。这进一步证实小本本 2026-05-03 v2 返工要求："标 missing 多半是没找到/没识别"。
- **细则 PDF 双版本**：主目录版常为扫描件（需 OCR），补充材料版常为数字版（直读）。同套必须双查。
- 2026 东城一模识到选必二第 10、11 题（宅基地+夫妻共同债务、AIGC 数字人格权侵权），主观题 18 题（调解+知产惩罚性赔偿+恶意诉讼）。

## Round 3 — 2026-05-04 全量解析

### 已完成
- `claudecode_lane/extract_all.py` 跑全量 176 文件，983 秒（含 OCR）。
- 172 解析成功 / 21 OCR / 3 失败（2 个为 Word 锁文件 `~$`，1 个 PPTX 损坏但同套有备份 L1）/ 1 永久排除（2026 石景山期末）。
- 落盘 `source_inventory/extracted/{2024,2025,2026}/{套卷_slug}/{文件}.txt`。
- 落盘 `00_control/SOURCE_LEDGER.csv`（v1，按文件名规则归类，过严）。

## Round 3.5 — 2026-05-04 等级二次扫描

### 已完成
- `claudecode_lane/reclassify.py` 同时按 文件名 + 文件内容 关键词重新归类。
- L1 内容关键词（rubric-only 独占式）：评分细则 / 答案变通 / 不重复给 / 不给分 / 才得分 / 选N给M分 / 满分卷|N分卷 / 阅卷总结|阅卷反馈 / 等级水平|水平4|3|2|1 / 替代知识 / 主观题细则|分题细则|评标实录 / "必须有X字样"。
- 加 SOURCE_INDEX 类（汇编锁定，不计独立证据）。
- 过滤 2 个 `~$` Word 锁文件。
- 输出 `00_control/SOURCE_LEDGER_v2.csv`，95 条等级升级，最终 L1=133, SOURCE_PAPER=32, SOURCE_INDEX=7, L2=2。
- 抽查 5 份被升的"试卷"型文件，全部确认含 `等级水平/水平4/评分细则` 真 L1 内容。

### 真实状态
唯一无 L1 的套卷：`2026 石景山期末`（永久排除）。其余 50+ 套都有至少一份 L1 级证据可挖。

### 重要提醒（写进 Round 4）
**文件级 L1 ≠ 选必二题级 L1**：很多"试卷+答案+等级水平表"合订本里的等级水平表是给**论述题（必修三/四）**用的，不是给选必二题的。Round 4 必须做**逐题匹配**：先识别每套有哪些选必二题，再在该套 L1 文件里找该题号对应的细则段落。文件 L1 等级仅说明"该文件含细则证据"，不能直接推到"该文件有该题的细则"。

### Round 4 计划（待用户点头）
逐题识别 + 选必二筛选 + 套卷分类：
1. 每个 .txt 内容做题号切分（识别"10."、"19."等题号边界，避开"18.4 千克"陷阱）；
2. 用关键词分类器把每道题判为：选必二 / 非选必二（必修一二三四+选必一三）/ uncertain；
3. 套卷级状态：`has_xuanbier_main` / `has_xuanbier_choice_only` / `no_xuanbier` / `uncertain`；
4. 输出 `LEGAL_QUESTION_INDEX.csv`（题级一行）+ `SUITE_STATUS.csv`（套级一行）。

### 阻塞 / 待用户裁决
- 暂无。等用户点头开 Round 4。
