# 决策与边界日志

## 2026-05-02 启动

- 本轮按 `SUPERVISOR_DIRECTIVE_2026-05-02.md` 执行：只做必修四哲学线，不做文化线；按套卷闭环推进；不继承旧 `artifacts/`、`reports/`、`必修四框架重做_2026-04-29/outputs/`、旧 audit/qa 等。
- 用户要求把“小本本里的所有注意事项”和“曾经提过的所有要求”全部传达给 ClaudeCode，并明确授权 ClaudeCode 处理 PDF 等各种格式、需要授权就都给他。已新增 `MASTER_REQUIREMENTS_FOR_CLAUDECODE_2026-05-02.md` 作为最高优先级总指令，并修改启动脚本把该文件拼入 ClaudeCode 启动 prompt。
- 用户补充 Microsoft Word 已登录激活并可用。最终 `.docx` 验收口径更新：脚本生成 `.docx` 只是中间状态，最终必须用 Microsoft Word 打开、保存并检查首页、前言页、正文洁净度、图片显示、中文排版和无损坏/权限弹窗；可行时导出 PDF 或截图作版式审计附件。
- 2026-05-02 02:22 心跳督工发现当前雏形成品存在硬失败：学生版 Markdown 中仍出现 `细则/参考答案/评标` 等审计话术；`COVERAGE_MATRIX.csv` 仍为空表头；`FINAL_ACCEPTANCE_REPORT.md` 仍是旧快照；`2026_朝阳_期中`、`2026_丰台_期末`、`2026_通州_期末` 缺 entries/reports 边界。已新增 `SUPERVISOR_PATCH_2026-05-02_HEARTBEAT_CLEAN_FINAL.md` 并修改启动脚本，要求 ClaudeCode 进入收尾返修模式。
- 工具基线：用本地 `scripts/extract_text.py`（PyMuPDF / python-docx / python-pptx）解析；机器无 `pdftoppm`，扫描 PDF 用 PyMuPDF `get_pixmap`。
- 已存在 `source_excerpts/2026海淀一模/{paper,rubric}/page_*.png`：判定为本轮启动前为本目录预渲染的技术性 source-cache（非旧结论）。本轮仍以原始 `试卷.pdf`、`细则.pdf` 为准回源核证据，渲染图仅作 OCR/读图辅助。
- 2026 石景山期末按 SKILL `Non-Negotiable Rules`（用户已逐题复核确认无可用细则）整套排除，不进入本轮处理与最终学生版。该套卷不写 suite_report。
- 套卷优先顺序：2026→2025→2024；同一年内海淀→西城→东城→朝阳→丰台→其他区。
- 评分证据等级口径（`evidence_level` 字段取值）：
  - `rubric-formal`：正式评分细则、阅卷评标、讲评评分页或用户确认评分文件。
  - `reference-only`：仅为参考答案，不能冒充评分细则。
  - `none`：无任何答案/细则可用。
- `status` 取值：`included`、`objective-key-only`、`module-boundary-excluded`、`reference-only`、`source-missing`、`ocr-needed`、`duplicate-or-drift`、`blocked`。
- 高风险哲学词（辩证否定 / 量变质变 / 两点论与重点论 / 主次矛盾 / 矛盾主次方面 / 价值观导向）必须有原文等值表述才能进学生版。

## 边界与暂记

- 2024 东城一模无独立答案 docx，只有 pptx 细则与扫描版答案 pdf；将以 pptx 与 pdf 共同作为正式细则证据。
- 2025 丰台二模只有逐题分题评标（doc/docx），无单文件总细则；逐题评标即正式评分证据。
- 2026 海淀期中无 `细则.*` 单文件，只有 `期中讲评20251106.pdf`；将以讲评 pdf 为评分证据来源，逐题确认讲评页含明确评分要点；若仅为参考答案口径，则将该题评分等级标为 `reference-only` 并不进入学生版。
- 2025 海淀期末试卷为 docx 版式，细则为 pptx 评标。
- 2026 西城期末有总细则 pdf 与评标 pptx，二者互为补充。
- 2026 东城一模分题评标 pptx 在 `分题细则/东城一模评标细则（勿传）/`，按用户存档使用，不公开传播；本仓库不复制其原始文件，仅在 audit 文件中引用路径。

## 2026-05-02 02:31 Codex 督工接管收尾

- ClaudeCode 按 02:22 补丁重启后仍未落盘修复结果；独立扫描确认学生版继续残留 `细则/参考答案/评标` 等审计话术，`COVERAGE_MATRIX.csv` 仍为空表头，`FINAL_ACCEPTANCE_REPORT.md` 仍写未达终态。
- 回源抽查缺口套卷后确认：`2026_通州_期末` 有都江堰哲学主观题及 pptx 评分细则，`2026_丰台_期末` 有“留白”哲学主观题及 PDF 评分细则，`2026_朝阳_期中` 有 AI 情绪价值哲学主观题及 docx 阅卷细则；缺口不是自然边界，而是 ClaudeCode 漏闭环。
- 为避免后台进程继续覆盖收尾文件，督工已停止 `claude --name 必修四从0重跑_2026-05-02` 进程，转由 Codex 在本目录直接补齐缺失 entries/reports、清理学生字段、重建覆盖矩阵、重合成学生版与 Word，并将结果作为后续与 Codex 5.2 版合并的素材。
