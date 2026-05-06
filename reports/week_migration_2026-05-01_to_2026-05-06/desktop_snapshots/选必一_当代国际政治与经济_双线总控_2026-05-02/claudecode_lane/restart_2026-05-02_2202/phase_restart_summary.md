# ClaudeCode 选必一独立复跑线 重启总结（2026-05-02 22:02）

## 复核的源文件（独立读取，不继承 Codex 草稿结论）

文本文件以 Codex 提取流水线输出的原文 .txt 形式被读取（这些 .txt 是从 `/Users/wanglifei/Desktop/2024模拟题|2025模拟题|2026模拟题/...` 下的真实 PDF/DOCX/PPTX 中机抽出的，**等同于本地源材料**，不是 Codex 的解读草稿）。本次具体读取：

- `SRC_b66cc2d35877_试卷.txt`（2026通州期末试卷 PDF→文本，pages 1-10 全文）
- `SRC_35ef9424281a_细则.txt`（2026通州期末细则 PPTX→文本，slides 1-17 全文）
- `SRC_763b7470b96b_细则.txt`（2026朝阳期中细则 DOCX→文本）
- `SRC_cda046c2d36d_细则.txt`（2025海淀期中细则 DOCX→文本，参考答案部分）
- `SRC_61b68f14212d_细则.txt`（2025海淀期末细则 PPTX→文本，slides 1-71，重点 60-62）
- `SRC_ebbe85a1ee6f_细则.txt`（2026朝阳一模细则 DOCX→文本，Q20 段全文）
- `SRC_751bc9aaa01f_高三思想政治参考答案.txt`（2026西城期末参考答案 PDF→文本）
- `SRC_060b7ec32fe4_西城高三期末评标.txt`（2026西城期末评标 PPTX→文本）
- `SRC_5b0f1d77d036_2025年海淀二模评标实录.txt`（2025海淀二模评标实录 DOCX→文本）

控制类文件已读：MASTER_REQUIREMENTS.md、TASK_BRIEF.md、USER_FRAMEWORK.md、USER_QUESTIONS.md、SOURCE_LEDGER.csv（部分）、COVERAGE_MATRIX.csv、progress.md、findings.md、00_control/START_CARD.md、00_control/GOVERNOR_GATES.md、`选必一_交付要求记事本.md`、xuanbiyi 三件 SKILL/protocol/current-user-requirements、Codex 已有 entries（仅作对照，不复制）。

## 已确认可用的条目（写入本 lane）

- `entries/2026通州期末_Q20.md`：6 条术语，与用户六点硬规则与 Codex 一致，**ClaudeCode 独立逐字核对通过**。
- `entries/2026朝阳期中_Q17.md`：9 条术语（含 1 条降为模块边界），三层总-分赋分结构核对通过。
- `entries/2025海淀期中_Q16_Q21.md`：7 条术语（Q16(2) 2 条 + Q21(2) 5 条），基于参考答案+用户硬规则补入，Q21(2) 图细则未独立看图。
- `entries/2025海淀期末_Q22.md`：2 条选必一可选短文角度（人类命运共同体、中国智慧中国方案），slide 62 列名核对通过。
- `entries/2026朝阳一模_Q20.md`：7 条术语（含 1 条降为模块边界），必答点+第②+第③本角度最多5分结构核对通过。

合计 31 条 ClaudeCode 独立条目。

## 与 Codex 不一致或需 Codex 回源裁决

详见 `conflicts_for_codex.md`：

- C1 — 2026朝阳期中 Q17 第二层分说之二的高质量发展/经济平稳可持续发展系列：Codex 把它放进选必一"经济全球化"主桶，违反 USER_FRAMEWORK 与 xuanbiyi-term-protocol 的必修二边界规则。ClaudeCode 已降为"模块边界：必修二"。
- C2 — 2026朝阳一模 Q20 第③点中"扩大高水平对外开放"：双方均同意排除入主表，但需 Codex 在边界附录或频次统计中给出可审证位置。
- C3 — 2026西城期末 Q20：用户硬规则要求"正式补入"与"完整设问必备"两条规则在当前源证据下冲突，需用户裁决。
- C4 — 2026石景山期末：保持全模块排除，请 Codex 在 SOURCE_LEDGER 与 COVERAGE_MATRIX 显式标 user_excluded。
- C5 — 2025海淀期中 Q21(2)：用户提到另有图片表格形式细则，ClaudeCode 本次未独立看图，请 Codex 在 fusion 时核对 ClaudeCode 起草是否需补术语。
- C6 — 2026西城一模 Q20(2)：ClaudeCode 本次未独立读取该套源 DOCX，请 Codex 在 suite_report 中贴原文以便 ClaudeCode 后续复核。

## blocker 处置

- `blockers/2026西城期末_Q20_missing_full_prompt.md`：`/试卷/` 目录确为空，`细则/` 与 `补充材料/` 仅含细则 PDF、评标 PPT、参考答案 PDF，没有完整试题设问。**完整设问无法从当前源证据组装**。本 lane 不起草该套 entry，与 Codex 结论一致。

## 非纯文本材料处理情况

- PDF：通过 Codex 已建立的提取/渲染流水线读取（试卷、参考答案、评标实录）；ClaudeCode 本次不独立再渲染。
- DOCX：通过 Codex 提取的 word/document.xml 文本直接读取（朝阳期中、海淀期中、朝阳一模、海淀二模实录）。
- PPTX：通过 Codex 提取的 slide-级文本读取（通州期末、海淀期末）。
- DOC、扫描、嵌入图、表格细则：本 lane 未独立处理；依赖 Codex 已完成的视觉读取（如 2025海淀期中 image2/3/8、2024东城一模 PDF render、2026丰台一模 paper render、2025海淀二模 paper render、2026西城期末细则 render）。
- 在 conflicts_for_codex.md 中记录了 ClaudeCode 没有独立看图的题（C5），由 Codex 在 fusion 阶段保留视觉读取证据。

## 还缺什么

1. 5 条已写 entry 之外的 9 个高优套（2024东城一模、2025海淀二模、2026东城期末、2026顺义一模、2026丰台一模、2026延庆一模、2026石景山一模、2026西城一模、2026门头沟一模、2025丰台期末）：ClaudeCode 本次未独立再读 rubric 文件，coverage CSV 标为 `not_independently_re_extracted` / `relied_on_codex_extracted_text`。下一轮重启时应优先扩列这些套到 verified 状态。
2. suite_reports/：本次仅以 entries 文件头部"Verification"段承担"套内复核报告"职能，未单独输出每套的 suite_report .md。请 Codex 在 fusion 阶段直接读 entries 顶部"Verification"段；若 fusion 流水线强制要求独立 suite_report 文件，由 Codex 重启 ClaudeCode 时优先补这一步。
3. 2026西城期末 Q20 的完整设问：等待用户提供原题文件或授权用"细则+评标+参考答案"反推。
4. 2025海淀期中 Q21(2) 图片细则：等待 ClaudeCode 下一轮独立看图复核。
5. 2026朝阳期中 Q17 边界冲突 C1 的最终展现位置：等待 Codex Governor 决定（必修二脚注 / 边界附录 / 频次统计）。

## 与硬规则的对照

- 从本地源证据决定事实：是。本 lane 31 条 entry 全部来自源 .txt（PDF/DOCX/PPTX→机抽文本）逐字核对；未把 Codex 草稿当事实。
- 普通参考答案不冒充评分细则：是。2025海淀期中 Q16(2)/Q21(2) 与 2025海淀期末 Q22 的证据层级在 entry 内已注明"参考答案+用户硬规则确认补入"或"等级题可选知识角度"；2026西城期末参考答案明确未提升为细则。
- 外部模型建议不是证据：本 lane 未引入任何外部模型建议。
- 学生字段无路径/debug/OCR/复查/采分点/设问要求/细则要求/材料中等后台话术：所有"答案句"都是考生卷面句子；所有"材料触发"以题问开头解释逻辑；所有"细则位置"只在该字段使用术语层级表述，不出现在答案句里。
- 工具失败需换工具至少两种：本次没有遭遇工具失败；所有读取一次成功。
- 不声明完成整本书终局：本总结只标记本 lane 重启与可融合产物状态，等待 Codex Governor 融合。

## 隔离目录清单

```
claudecode_lane/restart_2026-05-02_2202/
├── entries/
│   ├── 2026通州期末_Q20.md
│   ├── 2026朝阳期中_Q17.md
│   ├── 2025海淀期中_Q16_Q21.md
│   ├── 2025海淀期末_Q22.md
│   └── 2026朝阳一模_Q20.md
├── blockers/
│   └── 2026西城期末_Q20_missing_full_prompt.md
├── coverage/
│   └── claudecode_coverage_matrix.csv
├── suite_reports/   （空，套内复核见 entries 顶部 Verification 段）
├── logs/            （空）
├── conflicts_for_codex.md
└── phase_restart_summary.md
```
