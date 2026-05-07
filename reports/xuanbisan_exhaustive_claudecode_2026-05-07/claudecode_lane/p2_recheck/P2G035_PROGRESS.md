# P2G035_PROGRESS

> Status: NOT_FINAL（小规模 source_id 级 P2 复核子产物，非交付件）
> Source_id: `035_GaokaoPolitics_2025各区模拟题_2025各区一模_2025顺义一模_2025北京顺义高三一模政治_教师版_.pdf`
> Scope: 仅本 source_id 下 P2 三行（Q-2025顺义一模-5/-6/-7）。

## 1. 任务背景

larger P2 多源 batch 复核多次 stall 无文件输出后，分拆为 source_id 级小批 recheck，本批为 P2G035（顺义2025一模教师版）。

## 2. 范围

- priority=P2 only；
- source_id ∈ {035_GaokaoPolitics_2025各区模拟题_2025各区一模_2025顺义一模_2025北京顺义高三一模政治_教师版_.pdf}；
- 严格 3 行：
  1. Q-2025顺义一模-5（判断-联言判断的矛盾命题（B正解））
  2. Q-2025顺义一模-6（判断-性质判断主项识别（①正解））
  3. Q-2025顺义一模-7（推理-三段论-大项不当扩大（A正解，硬样本：硬规则§十九））
- 同 source_id 下另 3 条 P1 行 Q-2025顺义一模-17-1 不在本批；
- 不混入其他 P2 source_id（001/003/006/012/017/040/042/044/046）。

## 3. 时序记录

| 时刻 | 动作 | 产物 |
|------|------|------|
| T0 | 读 RECHECK_MANIFEST_ENRICHED.csv 过滤出 source_id=035 的 3 条 P2 行 | manifest 切片 |
| T1 | 读 035_*paper.txt 行1-265 题面（Q1-Q21）；行265-268 答案表（1-15）；行270-624 教师版逐题【详解】 | 源端 stem/options/answer key/【详解】全量定位 |
| T2 | 读 035_*support__2025顺义一模细则.docx.txt 行1-2 顺义区2025年高三统一测试参考答案表；行3+ 主观题阅卷细则 | support 答案表与主观题细则 |
| T3 | Q5 stem/options/answer 三方核验 → confirmed_with_patch | paper 5=B + support 5.B + 【详解】德摩根推演 |
| T4 | Q6 stem/options/answer 三方对照 → 发现 paper '6 A' 与 support 行1 '6.C' 单点差异；结合教师版【详解】对 ①②正确/③④错误的逐项推演 + manifest framework_node '①正解'（仅与 A=①② 一致）+ 同源 .docx 在其余14题答案与 paper/【详解】完全一致 → 判定 035_*support 行1 '6.C' 为同源 .docx 单行答案抄写笔误，权威答案 A 由 paper+【详解】+manifest 三方锁定 → confirmed_with_patch | 三方对照表 + 笔误识别 |
| T5 | Q7 stem/options/answer 三方核验 → confirmed_with_patch | paper 7=A + support 7.A + 【详解】大项不当扩大推演 |
| T6 | 写 P2G035_RECHECK_DECISIONS.csv（3 行 + 1 表头） | DECISIONS.csv |
| T7 | 写 P2G035_RECHECK_PATCHES.jsonl（3 行 JSON） | PATCHES.jsonl |
| T8 | 写 P2G035_SOURCE_EVIDENCE.md（含三方答案表对照与 Q6 笔误识别记录） | SOURCE_EVIDENCE.md |
| T9 | 写 P2G035_RECHECK_ACCEPTANCE.md | ACCEPTANCE.md |
| T10 | 写 P2G035_PROGRESS.md（当前文件） | PROGRESS.md |

## 4. 关键判断

- 三行 decision 均为 `confirmed_with_patch`：fusion P1 第471/840/848 行已含完整识别正文但带'需 Codex 回源复核'前置标签，本 patch 锁定答案表/双源/笔误识别等源端证据后，仅去复核标签，不改写已有识别正文。
- evidence_level 全部维持 manifest 的 `B-choice-signal`，未做任何调整。
- Q6 的 support 行1 '6.C' 笔误识别基于：
  1. paper 答案表 '6 A'；
  2. 教师版【详解】对 ①②正确（性质判断主项=政策工具 + '不是A而是B'为联言判断）/③④错误（应为越级划分非划分标准不一 + 不存在逻辑必然反向否定故非典型反对称）的逐项完整推演；
  3. manifest framework_node `（①正解）` 仅与 A=①② 一致（C=②④ 不含 ①）；
  4. 同源 .docx 在其余 14 题答案上与 paper/【详解】完全一致（1A/2C/3B/4D/5B/7A/8C/9B/10A/11D/12C/13B/14D/15A）；
  5. fusion P1 第840-844 行已在 P1 阶段按 A=①② 写入完整识别正文。
- 未捏造任何选项/答案/细则/源文件；Q6 笔误判定仅记录在 source_evidence 字段，未替换或修改 source 原文。

## 5. 输出件

| 文件 | 路径 | 行数/状态 |
|------|------|---------|
| P2G035_RECHECK_DECISIONS.csv | claudecode_lane/p2_recheck/P2G035_RECHECK_DECISIONS.csv | 1 表头 + 3 数据行 |
| P2G035_RECHECK_PATCHES.jsonl | claudecode_lane/p2_recheck/P2G035_RECHECK_PATCHES.jsonl | 3 行 JSON |
| P2G035_SOURCE_EVIDENCE.md | claudecode_lane/p2_recheck/P2G035_SOURCE_EVIDENCE.md | 已写（含三方答案表对照与 Q6 笔误识别记录） |
| P2G035_RECHECK_ACCEPTANCE.md | claudecode_lane/p2_recheck/P2G035_RECHECK_ACCEPTANCE.md | 已写（NOT_FINAL；exact row count 3；patch count 3；无 Word/PDF/delivery） |
| P2G035_PROGRESS.md | claudecode_lane/p2_recheck/P2G035_PROGRESS.md | 当前文件 |

## 6. 后续动作（非本任务范围）

- 后续 fusion patch 应将 framework_first_fusion P1 第471/840/848 行三处'需 Codex 回源复核'前置标签按 confirmed_with_patch 路径处理：
  - Q5（第848行）：去复核标签，保留卷面句；
  - Q6（第840行）：去复核标签，并在卷面句末尾保留 'support 答案表行1 6.C 为同源 .docx 单行抄写笔误，权威答案 A 由 paper 答案表+教师版【详解】+manifest framework_node 三方锁定' 的简短源端注；
  - Q7（第471行）：去复核标签，并在硬规则§十九对应章节标注本题为该规则的核心硬样本。
- 三行均可从 needs_codex_recheck=yes 状态转入正常学生体保留路径（can_enter_fusion=yes）；
- 不在本 P2G035 任务的输出范围内。
