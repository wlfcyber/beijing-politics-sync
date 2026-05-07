# EXHAUSTIVENESS_AUDIT

## 当前结论

`NOT_EXHAUSTIVE_BUT_CONTROL_BASE_CLOSED_AT_LEDGER_LEVEL`

本轮（B 线 ClaudeCode 厚内容矿）按套卷关闭题源覆盖，并不是一次写完整本宝典。

经 SUPERVISOR_PATCH_01 修补：
- 528 → 534 行（补 Phase12 后增 6 个 canonical qids：Q-2025海淀二模-12/13、Q-2026丰台一模-4/7/8/9，全部为 blocked-需独立扫描）。
- 本轮结论字段已规整到 4 桶：`入正文 / 同类索引 / blocked / excluded`，不再保留 pending。

## 边界

1. **2026 二模**：本机 source roots 未发现任何 2026 二模套卷。本轮扫描边界：`C:/Users/Administrator/Desktop/2026各区模拟题/**/*二模*` 无返回；`preprocessed_corpus/texts` 无对应文件。**不写成尚未开考**，写成 `本轮 source roots 未发现`。
2. **2026 石景山期末**：按用户既往裁定排除；不再回扫。
3. **纯形式逻辑题**：进入索引和边界，不进思维主观题主链。共 95 行。
4. **其他模块题**：本机虽有，但只作题源说明。共 19 行直接归 C-boundary-other-module；另 ~60-80 行散落在 117 行 pending 中（需回源后再判）。

## 本轮 534 行控制基（528 + 6 Phase12 canonical）本轮结论分布

| 本轮结论 | 行数 | 含义 |
| --- | --- | --- |
| 入正文 | 80 | A-formal/A-support 主观题正例 + B-choice-signal 选择题正例（含已写 entries 的硬样本） |
| 同类索引 | 4 | B-choice-signal 选择题陷阱（边界陷阱不进正文，但进陷阱库） |
| blocked | 336 | 缺题面/选项/答案/细则/视觉核读（绝大多数是 GitHub label 含思维方法术语但本轮未读完整子问；或选择题待回源补完整选项；或 Phase12 canonical 新增需独立扫描） |
| excluded | 114 | 纯形式逻辑/推理边界（95行）+ 其他模块（必修四/选必一/选必二/经济与社会/政治与法治，19行） |
| **合计** | **534** |  |

84 行（80 入正文 + 4 同类索引）已有可融合厚内容/边界陷阱；336 行 blocked 等待 fusion 前回源闭合；114 行 excluded（不进选必三主链，按规则确定排除）。

## 本轮 entries 文件

| 文件 | 类型 | 行数 |
| --- | --- | --- |
| `entries/hard_samples.jsonl` | main + choice | 11 |
| `entries/additional_main.jsonl` | main | 12 |
| `entries/additional_choice.jsonl` | choice | 9 |
| **合计** | | **32 entries** |

## 已完成的关闭

按套卷 suite_report 写：

| 套卷 | 题源完整 | 评分证据 | 主观题入库 | 选择题入库 | 边界标注 | suite_report | 状态 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2024 朝阳一模 | ✅ | A-formal | ✅(2) | ✅(1) | ✅ | ✅ | 关闭 |
| 2024 朝阳二模 | ✅ | A-formal partial | (Q19 全 C-boundary-other-module) | ✅(1) | ✅ | ✅ | 关闭 |
| 2024 朝阳期中 | ⚠ RTF 未拆 | A-support | ✅(1 占位) | (Q9 待回源) | ✅ | ✅ | 部分关闭 |
| 2024 海淀二模 | ✅ | A-formal | ✅(2 硬样本) | — | ✅ | ✅ | 关闭 |
| 2024 西城一模 | ✅ | A-formal | not_in_control_base | not_in_control_base | ✅ | ✅ | 候选 |
| 2025 东城期末 | ✅ | A-formal | ✅(1 硬样本) | (Q1/2/5 待回源) | ✅ | ✅ | 主链关闭 |
| 2025 丰台期末 | ✅ | A-support | ✅(1) | ✅(2) | ✅ | ✅ | 部分关闭 |
| 2025 海淀二模 | ⚠ PDF 是图像 | A-formal | ✅(1 硬样本) | (无) | ✅ | ✅ | 主观题关闭 |
| 2025 海淀期末 | ✅ | A-support | ✅(占位) | (Q2 待回源) | ✅ | ✅ | 占位+索引 |
| 2025 西城二模 | ✅ | A-support | ✅(1 边界硬样本) | — | ✅ | ✅ | 部分关闭 |
| 2025 顺义一模 | ✅ | A-support | ✅(1) | ✅(1 硬样本警示) | ✅ | ✅ | 部分关闭 |
| 2026 东城一模 | ✅ | A-formal partial | ✅(4 占位) | C-boundary | ✅ | ✅ | 占位 |
| 2026 东城期末 | ✅ | A-formal | ✅(2) | ✅(1) | ✅ | ✅ | 关闭 |
| 2026 丰台一模 | ⚠ PDF 待扫 | A-support | ✅(1) | — | ✅ | ✅ | 部分关闭 |
| 2026 朝阳期中 | ✅ | A-formal | ✅(2 双硬样本) | ✅(1) | ✅ | ✅ | 关闭 |
| 2026 通州期末 | ✅ | A-formal | (Q11 在选择题硬样本) | ✅(4) | ✅ | ✅ | 关闭 |
| 2026 顺义一模 | ✅ | A-formal | ✅(2 硬样本) | (Q3/5/6/9 待回源) | ✅ | ✅ | 部分关闭 |

## 未关闭的缺口（按 fusion 优先级）

经 SUPERVISOR_PATCH_01 后，原 pending 已规整到 blocked。336 行 blocked 中：

### 高优先 — 影响硬样本完整性（主观题 blocked，原 pending-evidence-recheck）
- 约 117 行主观题：每行 GitHub label 含思维方法术语，但本轮未独立读完整子问细则给分链。需要 fusion 前回源对应细则文件。重点套卷：2025 海淀期末（Q17/18/22）、2024 朝阳期中（Q19，RTF 整文档 186917 字符未拆题）、2025 西城二模（Q16(1)/(3)）、2025 顺义一模（Q3/Q7/Q16）、2026 东城一模（Q19 4 子问 PPTX）、2026 丰台一模（Q18(2) PPTX）。

### 中优先 — 选择题题面+四选项 blocked（原 同类索引-pending）
- 约 213 行选择题：需回源原卷补完整选项+正确项理由+错项陷阱。包括 6 行 Phase12 canonical 新增（2025海淀二模-12/13；2026丰台一模-4/7/8/9）需独立扫描 PDF。

### 关键 source 障碍
- 2025 海淀二模试卷 PDF 是图像扫描型（pypdf 提取 0 字符）；Q2-Q15 选必三相关选择题需视觉/OCR 进入。
- 2024 朝阳期中 RTF 细则需按题号拆分。
- 2026 东城一模、2026 丰台一模 PPTX 子问未汇总。

### 低优先 — 扩展题源（not_in_control_base）
- 30+ 套候选（见 SOURCE_LEDGER 行 18-31）。

### blocked / excluded 严格分类
- 2026 二模整批：blocked（本轮 source roots 未发现）。
- 2026 石景山期末：excluded（用户裁定整模块排除）。
- 推理边界（纯形式逻辑）95 行：excluded。
- 其他模块边界（哲学/国政经/法律/经济社会/政治法治）19 行：excluded。

## 不能穷尽的具体原因

1. **细则格式异质**：PPTX 多套卷按题号独立拆分文件（2026 东城一模、2024 东城二模等），需独立打开每个文件汇总；本轮无法一次性读完所有 PPTX 子文件。
2. **图像扫描型 PDF**：2025 海淀二模试卷 PDF 没有文本层（pypdf 提取 0 字符），需要视觉/OCR 进入。
3. **RTF 未按题号拆**：2024 朝阳期中细则.rtf 是 186917 字符的整文档，未按题号 grep 出 19 题；fusion 前必须做 RTF 分题。
4. **GitHub control matrix 知识节点标签不能单独决定归属**：例如 2024 朝阳一模 19(1) 标 "动态性+联言+辩证"，但实际是按子问区分（19(1) 动态性+类比；19(2) 联言判断；19(3) 综合理解）；多数 117 行 pending 行需要类似按子问拆开。
5. **2026 二模整批未提供**：本机源未发现任何 2026 二模套卷。
6. **用户对 2026 石景山期末的整体排除决定持续生效**。

## 不写为终稿的原因（硬规则§十四+§二十二复盘）

- 不能进入 Word/PDF final gate；不能写 final/PASS/终稿/最终稿/宝典成品。
- 本轮交付仅为 B 线厚内容矿——可融合的 thick body、entries、framework node matrix、coverage、blockers、suite reports。
- 是否进入 fusion，应由 Codex 按本文件 + 控制矩阵 + entries 决定。
- 不假装 GPT-5.5 Pro 或 Claude Opus 网页外审已参与。

## SUPERVISOR_PATCH_01 应用记录

`SUPERVISOR_PATCH_01.md` 来自 Codex 监管 verdict=`HARD_FAIL_NOT_CLOSED_YET`。本轮：
- ✅ 补 6 行 Phase12 canonical 缺失 qids（全部 blocked-需独立扫描）。
- ✅ `本轮结论` 已规整到 4 桶 `入正文 / 同类索引 / blocked / excluded`。
- ✅ `reason` / `blocker` 字段保留细分原因。
- ⚠ 30+ 套 `not_in_control_base` 扩展候选未本轮处理；监管 Patch 未要求强行扫描，但留作下轮 fusion 前的扩展任务。

监管的 PASS 条件未达：本轮仍非穷尽。Codex/fusion 阶段必须按 336 行 blocked 名单回源补题面、选项、细则、子问拆分。
