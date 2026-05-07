# P2G012 Progress Log

> 小规模 source_id 级 P2 复核子任务，对单一 source `012_Desktop_2025模拟题_2025各区期末_2025东城期末_试卷_试卷.pdf` 下 4 行 P2 choice_trap（Q5/Q13/Q14/Q15）执行源验证。

Run timestamp: 2026-05-07
Lane: ClaudeCode
Trigger: P2 全量复核多次 stall 后由 supervisor 切片到单 source 子组（详见 `claudecode_lane/p2_recheck/SUPERVISOR_PATCH_01_FULL_P2_STALL_SPLIT.md`）。继 P2G017 闭合后续接此子任务。
Prompt: `claudecode_lane/p2_recheck/CLAUDECODE_P2G012_PROMPT.md`。

## Step 1: 输入识读

- 读 `fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv`，grep `012_Desktop_2025模拟题_2025各区期末_2025东城期末` 共命中 8 行：
  - 4 行 P0（Q-2025东城期末-18-2 跨节点重复参考行，超出本次 P2 范围）
  - 4 行 P2（本次范围）：
    - Q-2025东城期末-5（辩证思维>整体性+动态性+矛盾分析法，B-choice-signal）
    - Q-2025东城期末-13（推理>演绎推理>三段论·中项不周延，B-choice-signal）
    - Q-2025东城期末-14（推理>判断>性质判断·主谓项周延，B-choice-signal）
    - Q-2025东城期末-15（推理>演绎推理>充分条件假言推理，B-choice-signal）
- 读 `fusion/p2_recheck_sources/P2_SOURCE_TEXT_INDEX.csv` 第8-10行，定位 012 源三份提取文本：
  - paper.txt（62 115 字节）
  - support__2025东城期末细则.pptx.txt（11 755 字节）
  - support__2025。1东城讲评_修改.pdf.txt（9 247 字节）

## Step 2: 题面（stem & options）核验

- 打开 paper.txt 全文：62 115 字节，含 Q1-Q15 完整客观题题面 + Q16-Q21 完整主观题题干 + 第8-20页"参考答案"段（教师版试卷嵌入的逐题分析+故选）。
- Q5（行40-48）、Q13（行110-117）、Q14（行118-124）、Q15（行125-131）四题 stem 与四个选项均能逐字核验。

## Step 3: 答案核验（关键成功路径，与 P2G017 对照）

- **关键差异（与 P2G017 相比）**：017 源 paper.txt 仅含题面副本而无答案表，故 P2G017 三行全部走 source_insufficient；**012 源 paper.txt 是教师版**，第8-20页直接嵌入"参考答案"段，含 Q1-Q15 全部客观题的逐项分析+"故选"标识，故 P2G012 四行全部源充分，可走 confirmed_with_patch 路径。
- 检查 paper.txt 答案段：
  - 第5题：行318-346，'本题考查：辩证思维的含义及特征'+整体性/动态性教材原文+'故选：**C**'+①③错项与②④对项的逐项解释。
  - 第13题：行490-509，'本题考查：三段论推理'+三段论保真四规则教材原文+'故选：**B**'+①③中项不周延+②大项不当扩大+④四概念错误的逐项分析。
  - 第14题：行510-542，'本题考查：性质判断'+判断含义/分类（直言判断六种基本形式）+关系判断（对称/传递）+'故选：**D**'+四项逐项分析。
  - 第15题：行543-564，'本题考查：假言推理及其方法'+三种假言推理规则原文+'故选：**B**'+四项逐项分析。
- 检查 support 文件（仅作交叉核验，不构成必要条件）：
  - 2025东城期末细则.pptx.txt：SLIDE 3-7/12-22/29-34 仅 16/17/18(1)(2)/19(1)(2)(3)/20/21 主观题阅卷细则，**全文不含 Q1-Q15 客观题**（与 paper.txt 答案不冲突，仅作不冲突性核验）。
  - 2025。1东城讲评_修改.pdf.txt：PAGE 4-17 仅 16/17/18(1)(2)/19(1)(2)(3)/20/21 主观题讲评，**全文不含 Q1-Q15 客观题**（与 paper.txt 答案不冲突）。
- → 四行客观题答案在 012 源 paper.txt 内**直接可见且逐项可核验**。

## Step 4: framework_node 锁定

- Q-2025东城期末-5 → 辩证思维>整体性+动态性+矛盾分析法：源解析中"②对应辩证思维的整体性+动态性、④对应辩证思维的矛盾分析法"三合一锁定 ✅
- Q-2025东城期末-13 → 推理>演绎推理>三段论·中项不周延：源解析中"①③共同犯'中项不周延'错误"精确锁定 ✅
- Q-2025东城期末-14 → 推理>判断>性质判断·主谓项周延：源解析中"D项是简单性质判断、肯定判断谓项不周延"精确锁定 ✅
- Q-2025东城期末-15 → 推理>演绎推理>充分条件假言推理：源解析中"B项肯前+否后，违反充分条件假言推理'肯前必肯后'规则"精确锁定 ✅

## Step 5: 决策

按 P2 硬规则：
1. **'Verify stem/options and answer key before confirming choice-trap rows'** → 四行 stem/options/answer 均已逐字核验，可以 confirm。
2. **'Use the manifest evidence_level exactly unless the source genuinely proves the row is misclassified'** → 四行 evidence_level=B-choice-signal 维持不变（源证据强度与 B-choice-signal 完全匹配；无需上调到 A-formal）。
3. **'Do not invent options, answers, rubrics, or source files'** → 四行 patched_answer_sentence 直引 paper.txt 行号+"故选"原文，未捏造任何答案。
4. framework_first_fusion_P1_PATCHED.md 第142/543/643/667行该四行仍标'需 Codex 回源复核'，本次复核完成后应在后续 fusion patch 中去除该标记并锁定答案 C/B/D/B → 故 decision=**confirmed_with_patch**，patch_needed=yes，can_enter_fusion=yes。

## Step 6: 输出件落盘

| 文件 | 状态 |
|------|------|
| P2G012_RECHECK_DECISIONS.csv | 写 1 表头 + 4 数据行 ✅ |
| P2G012_RECHECK_PATCHES.jsonl | 写 4 行 JSON ✅ |
| P2G012_SOURCE_EVIDENCE.md | 写 ✅ |
| P2G012_RECHECK_ACCEPTANCE.md | 写（含 NOT_FINAL 声明） ✅ |
| P2G012_PROGRESS.md | 当前文件 ✅ |

## Step 7: 完成状态

- exact row count 4 ✅
- patch count 4 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 四行 decision 均为 confirmed_with_patch ✅
- evidence_level 维持 manifest 原值 B-choice-signal ✅
- four answer keys（5.C / 13.B / 14.D / 15.B）均已通过 paper.txt 行级核验 ✅
- 未涉及 001/003/006/017/035/040/042/044/046 等其他 P2 source_id ✅

## Notes & 待处理

- framework_first_fusion P1版第142/543/643/667行的 Q-2025东城期末-5/13/14/15 四处仍标'需 Codex 回源复核'；本任务结论应在后续独立 fusion patch 中落地（去除回源复核标记+锁定答案 C/B/D/B），但该 patch 不在 P2G012 这一小规模子任务输出范围内。
- 与 P2G017（三行全部 source_insufficient）的对比说明：差异完全由源类型决定——017 源 paper.txt 仅含题面副本，故 source_insufficient；012 源 paper.txt 是教师版（嵌入参考答案段），故 confirmed_with_patch。两个子组的处理路径分别覆盖了 P2 复核硬规则的两端（答案缺失走 source_insufficient、答案在源走 confirmed/confirmed_with_patch）。
- 余下 P2 source_id（001/003/006/035/040/042/044/046 等）应继续按相同的 source_id 切片模式承接独立子任务。
