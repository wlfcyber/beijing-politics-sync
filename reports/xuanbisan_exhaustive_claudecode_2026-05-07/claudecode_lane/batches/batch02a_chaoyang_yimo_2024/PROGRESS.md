# Batch02a 2024朝阳一模 单套闭合 PROGRESS

## 启动 — 2026-05-07

任务边界：本小批仅闭合 `S-2024朝阳一模` 一套套卷，用于修正 Batch02 大批启动后长时间无输出的停滞问题。按用户穷尽口径产出 4 类结论 (`入正文 / 同类索引 / blocked / excluded`)，并对入正文题写厚内容；不写终稿、不写 PASS、不生成 Word/PDF。

## 控制源（已读）

- `claudecode_lane/QUESTION_COVERAGE_MATRIX.csv` — 抽出本套 23 行 Q-2024朝阳一模 候选；其中 Q6/Q7/Q9/Q20-1/Q20-2 在 SUPERVISOR_PATCH_01 之前已被锁定为 B-choice-signal 或 A-formal 等级；其余按 patch 改 blocked/excluded。
- `codex_lane/QUESTION_COVERAGE_MATRIX.csv` — 提供 phase12 362_rescan 的 23 行完整题面 + 答案对位（Q6 标注 new_body_candidate / Q7 / Q9 / Q20-1 / Q20-2 标注 covered_by_74_review_body 与 L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE）。
- `phase05_thinking_signal_archive.csv` — 命中 Q-2024朝阳一模-7（创新思维 + 发散/聚合/逆向/超前/迁移）与 Q-2024朝阳一模-9（系统观念 / 整体性）。
- `phase05_reasoning_typology_archive.csv` — 命中 Q-2024朝阳一模-20-1（充分条件假言推理·否定后件式）与 Q-2024朝阳一模-20-2（必要条件假言推理）。
- 源目录三件套（已实读）：
  - 试卷 PDF：`030_Desktop_2024模拟题_2024朝阳一模_试卷_试卷.pdf`（codex 矩阵已含完整题面 23 行 OCR 文本）。
  - 参考答案：`其他材料/202404朝阳高三政治质量检测一参考答案 上交版.docx`（已 unzip 解析 word/document.xml；选择题 1–15 答案 + 主观题 16–21 给分要点全部抽取完毕）。
  - 试卷讲评：`细则/2024朝阳一模细则.pptx`（已 unzip 解析 ppt/slides；Q20(1) 给分链拿到细则 31：充分条件假言推理 1 分 + 前真后必真后假前必假 2 分 + 推理成立 2 分；Q20(2) 给分要点拿到细则 45–46：必要条件假言推理结构补全）。

## 套卷推进

| suite_id | 候选行数 | 已扫源文件 | 已读细则 | 已读试卷 | 已读答案 | 状态 |
|---|---|---|---|---|---|---|
| S-2024朝阳一模 | 23 | ✓ | ✓ pptx 51 张幻灯片（重点扫 14/27/31/33/43/45 给分细节） | ✓ codex 矩阵全 23 行 OCR 文本 | ✓ docx 答案 1–21 全部解析 | 闭合 |

## 决定分布

- 入正文（5 行）：Q6（逻辑三律 + 概念划分）、Q7（创新思维 / 发散聚合超前迁移）、Q9（系统观念 / 整体性）、Q20-1（充分条件假言推理·否定后件式）、Q20-2（必要条件假言推理）。
- 同类索引（0 行）：本套无跨套同类索引镜像；Q20-1/Q20-2 已与 Q-2026通州期末-19-2、Q-2024朝阳二模-7 等在 phase05 archive 内互锁，暂不在本批新建索引。
- blocked（0 行）：本批所有题面 + 答案 + 给分链均已落地，没有真正"待回源"的题。
- excluded（18 行）：18 题超出选必三《逻辑与思维》范围（政治、经济、法律、哲学与文化、当代国际政治等），逐题在 BLOCKED_OR_BOUNDARY.md 写明所属其他模块。

## 优先厚写题（已确认证据等级）

| question_id | 证据等级 | 来源 | 落点 |
|---|---|---|---|
| Q-2024朝阳一模-6 | B-choice-signal_needs_answer_key_check（本批通过 docx 答案核对升级为 B-choice-signal_LOCKED） | docx 答案 = B；试卷 OCR + 讲评细则 | 逻辑与思维 / 遵循逻辑思维规则 / 排中律·矛盾律·概念划分规则（划分子项不得相容、矛盾律违反、三段论媒项错误） |
| Q-2024朝阳一模-7 | L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE | phase05 thinking_signal_archive | 提高创新思维能力 / 发散聚合超前迁移 / 创新思维与逻辑思维边界 |
| Q-2024朝阳一模-9 | L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE | phase05 thinking_signal_archive | 树立系统观念 / 系统优化的方法 / 整体性 |
| Q-2024朝阳一模-20-1 | L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE / A-formal | phase05 reasoning_typology_archive + 讲评细则 31 | 假言推理 / 充分条件假言推理 / 否定后件式 |
| Q-2024朝阳一模-20-2 | L3_CONFIRMED_FOR_EVIDENCE_ARCHIVE / A-formal | phase05 reasoning_typology_archive + 讲评细则 45–46 | 假言推理 / 必要条件假言推理 / 补充推理结构 |

## 已识别 blocker

- 本批无 suite-level blocker：试卷 OCR / 答案 docx / 讲评 pptx 三源齐全；选择题答案逐题对位、主观题给分链 Q20 已读到细则 31/45/46。
- Q-2024朝阳一模-18(2) 题面 OCR 截断（"倡..."），但 docx 答案显示其落点是哲学与文化（"两点论与重点论""具体问题具体分析""文化强国"），不进入本批主线；标 excluded 并附 needs_codex_recheck=yes 备份字段，供 codex_lane 在跨模块 cross-tag 时复核是否切回选必三辩证思维系统观念。
- Q-2024朝阳一模-4 docx 答案 = A（"建立新的联系"），命中"联系/属性"哲学共有概念，未独立触发选必三系统观念或辩证思维特定术语，按硬规则保守归 excluded，不进入本批正文池。

## 下一步（已完成）

1. ✓ 读 codex 矩阵抽 Q-2024朝阳一模 23 行（含完整 OCR 题面+phase12 决定）。
2. ✓ 读 docx 答案：选择题 1–15 答案 + Q16–Q21 给分要点全部确认。
3. ✓ 读 pptx 讲评：Q20(1)/Q20(2) 给分链精确到 1/2 分点。
4. ✓ 读 phase05 两本档案：抽到 Q7/Q9/Q20-1/Q20-2 的 L3 锁定证据。
5. ✓ 写 PROGRESS.md（本文件）、QUESTION_DECISIONS.csv、MAIN_THINKING_LEDGER.csv、CHOICE_TRAP_LEDGER.csv、FRAMEWORK_NODE_MATRIX.csv、BLOCKED_OR_BOUNDARY.md、entries/batch02a_entries.jsonl、SUITE_REPORT.md、BATCH02A_ACCEPTANCE.md。

## 最终交付清单（已应用 SUPERVISOR_PATCH_02 + SUPERVISOR_PATCH_03 修补）

| 文件 | 行数 | 说明 |
|---|---|---|
| `PROGRESS.md` | 本文件 | 单套套卷闭环+推进记录（不写 PASS） |
| `QUESTION_DECISIONS.csv` | 24 行（含表头）/ 8 列 | 23 个候选题给出 `入正文/同类索引/blocked/excluded` 结论与理由；重写时改用 csv.writer + QUOTE_MINIMAL 保证含逗号字段被正确转义；needs_codex_recheck 列只允许 yes/no |
| `MAIN_THINKING_LEDGER.csv` | 3 行（含表头）/ 11 列 | Q20-1 / Q20-2 两道主观题厚内容（推理类型识别 + 补充推理结构） |
| `CHOICE_TRAP_LEDGER.csv` | 4 行（含表头）/ 9 列 | Q6 / Q7 / Q9 三道选择题厚陷阱分析（逻辑三律 + 创新思维 + 系统观念） |
| `FRAMEWORK_NODE_MATRIX.csv` | 9 行（含表头）/ 6 列 | 8 条 (framework_node, 挂载题id) 详挂载行（重写后 Q6 拆出 4 个挂载节点：排中律/矛盾律/划分规则/三段论媒项规则） |
| `FRAMEWORK_NODE_MATRIX_SUMMARY.csv` | 9 行（含表头）/ 10 列 | 8 个 unique framework_node 的聚合视图（按 batch01 同名文件 schema） |
| `BLOCKED_OR_BOUNDARY.md` | — | 18 条 excluded（逐题写明所属其他模块）+ 0 条 blocked + 0 条同类索引边界 |
| `entries/batch02a_entries.jsonl` | 5 行 | 每条厚内容一行 JSON（subjective + choice 两类，含 `question_id, type, framework_node, material_signal, trigger_logic, answer_sentence, evidence_level, needs_codex_recheck, source_batch` 必需字段；Python json.loads + 必需字段集合检查 missing == [] 全部通过） |
| `SUITE_REPORT.md` | — | 1 套套卷闭环报告 |
| `suite_reports/S-2024朝阳一模.md` | — | 与 `SUITE_REPORT.md` 同源，按 batch01 同名目录 schema 复制一份保留 |
| `BATCH02A_ACCEPTANCE.md` | — | 验收说明（口径、行数、签核条件、已应用的两次 SUPERVISOR_PATCH） |

## 套卷统计

- 候选总数：23 题
- 入正文：5 题（Q6 / Q7 / Q9 / Q20-1 / Q20-2，均锁 B-choice-signal 或 A-formal/L3_CONFIRMED）
- 同类索引：0 题
- blocked：0 题（试卷+答案+讲评三源齐全）
- excluded：18 题（政治 6 / 经济 5 / 法律 4 / 哲学与文化 1 / 哲学（人生价值）1 / 当代国际政治与经济 1）
- 优先厚写题清单中 5 题全部完成厚内容

## 监督备忘

- 厚内容字段（材料动作 / 总帽子 / 小方法 / 触发逻辑 / 答案句）一律用学生面向白话写；未出现"固定分析流程"这个栏目或措辞。
- 厚内容字段未出现 `评标 / 参考答案 / 答案写 / 可从…角度作答 / yes / pass / filled / correct_option_chain / A-formal / B-choice-signal / phase / phase05 / source_pool / question_id / file id / line id / OCR / debug / /Users/... / C:\\...` 等审计或后台话术作正文。
- 审计字段（证据等级、来源 path、phase 状态、是否可入学生稿）只出现在 csv/jsonl 的元数据列，不进 `答案落点`/`为什么能想到` 等学生面向字段。
- Q-2024朝阳一模-20(1) 严格按硬规则十六/十八锁定为充分条件假言推理（否定后件式），照细则 31 给分链：推理类型 1 分 + 前真后必真后假前必假 2 分 + 推理成立 2 分。
- Q-2024朝阳一模-20(2) 按细则 45–46 拿到必要条件假言推理结构补全的 4 分给分链：前提 1（只有……才……）2 分 + 前提 2（古代 A 区域广泛生长着竹子）2 分。
- 此 batch 不写终稿、不写 PASS、不生成 Word/PDF；整套交付以"可融合材料 + 闭环裁决"为目标。
