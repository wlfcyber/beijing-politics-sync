# Claude External Review Result V0

Status: `EXTERNAL_REVIEW_DONE_NOT_PASS`

Reviewer lane: independent Claude external review. Distinct from ClaudeCode B 线 production. This file is the only authoritative deliverable of this lane.

Scope: read TASK_BRIEF / DEVELOPMENT_PLAN / PROGRESS / 00_硬性要求记事本 / 04_fusion 三件 / 03_claudecode_lane 三件；spot-check 02_codex_lane 三件 + QUESTION_COVERAGE_MATRIX；回源核验 2026顺义一模 Q19(2) 与 2024海淀二模 Q17(1) 两题原始题面/细则。

## Verdict

**NOT_READY_FOR_FINAL — REWRITE_BEFORE_V1.**

理由（concise）：

1. 思维宝典含一处 **Critical 错路由**（Q0011 / 2024海淀二模 Q17(1)），其官方细则把 7 分拆成 科学思维 2 + 创新思维 3 + 辩证思维 2 三模块并列；当前 draft 反向把三个角度都挂到 "科学思维 单角度"，并在 "安全边界" 中提醒学生 *不要* 写成三模块并列。若学生按 draft 写，最坏只能拿 2/7 分。这恰是 BLK-001 留的逃生条款 "若新源出现三模块并列则提请用户裁定"，但 draft 已先于裁定收录。
2. 思维 / 推理条目普遍未满足 TASK_BRIEF §产物一 / §产物二 规定的 4 / 5 必答要素；尤其 "为什么能从该材料想到这个方法" 这一教学桥段近乎全缺。drafts 读起来更像查找表，达不到"必修四宝典制作质量"。
3. 选择题条目（Q0004 / Q0012 / Q0015 / Q0016 / Q0017）只给"正确选 X" 与少量陷阱评述，**未抄录 A/B/C/D 选项原文**。学生离开试卷无法独立校验，违反 TASK_BRIEF §工作方式 "Claude 优先查教学语言、迁移性、学生误读风险"。
4. fusion_candidates 中已有 10 行 B-line `A-formal / high / accept` 候选**尚未进入** Codex A 的 coverage matrix（FC-MT-005/006/007、FC-RE-014/015/016/017/018/019/020），其中至少 3 行（不完全归纳、选言判断、类比推理）正好对应推理册 §五 自己点出的"待扩容"节点。说"找不到"是错的，实际是 A 线 source-lock 落后于 B 线。
5. 至少 3 条 blocker (BLK-001 / BLK-003 / BLK-004) 仍 `open`，但其对应条目（Q0011 / Q0012 / Q0008）已被收入 review draft。promotion gate 未生效。
6. 与硬规则 "本轮必须结合 2024-2026 三年所有涉及选必三的考题，不得只做代表例题小册子" 比较：当前 17 条 source-locked / 思维 7 entries / 推理 ~10 entries，距离 全量穷尽仍很远。覆盖压力远未释放。

未达可发布门槛。下一步只能进入 V1 重写，不得对外宣称已完成 / 已审完 / 已通过。

## Findings Table

| # | 严重度 | 文件 / 位置 | 问题 | 必须修正 |
|---|---|---|---|---|
| F1 | **Critical** | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §二.1 (Q0011 段) + `02_codex_lane/FAMILY_SOURCE_PACKETS_Q0006_Q0012.md` §Q0011 | Q0011 (2024海淀二模 17(1)) framework_node 写 "科学思维 -> 客观性/探索性/整体性"，draft "本题安全边界" 主张 "答案主帽仍是科学思维，不要扩写成三模块并列"。回源 `gpt_sources/227192d22e10241b_2024海淀二模细则.md:30-54`：官方细则把 7 分拆为 **科学思维角度（2分） + 创新思维角度（3分） + 辩证思维角度（2分）**；探索性 / 三新 / 发散聚合 / 超前 均属创新思维；整体性 / 分析与综合 / 矛盾分析法 属辩证思维。draft 不仅类别归错，**还给出与阅卷相反的安全边界**，学生照写最坏只得 2/7。这正是 BLK-001 留的"若新源出现三模块并列则提请用户裁定"escape clause 被触发的情形，但 draft 已先于裁定收录条目。 | (a) MAIN_THINKING_LEDGER 中 Q0011 重新分类为"三模块复合题（科 2 / 创 3 / 辩 2）"。(b) 思维宝典中拆为三块挂三个节点（科学思维 / 创新思维 / 辩证思维），互相 cross-ref。(c) 完整删除原 "本题安全边界" 段，改写为 "本题分值结构：科 2 / 创 3 / 辩 2，必须三模块都写；只写科学思维上限 2 分"。(d) 触发口诀分清：客观性→科学；探索性 / 三新 / 发散聚合 / 超前→创新；整体性 / 分阶段 / 分析与综合→辩证。(e) BLK-001 在闭合时显式写明 "新源 = 227192d22e10241b:30-54 三模块并列已裁定"。 |
| F2 | High | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` 全体 vs `TASK_BRIEF.md` §产物一 | TASK_BRIEF 规定每条思维条目必须回答四点：① 材料动作触发；② 为什么能从该材料想到这个方法；③ 卷面答案句；④ 易错/边界。当前 7 条条目缺项普遍：Q0011 缺 ②③④（只有触发口诀 + 一条错位安全边界）；Q0014 缺 ④；Q0003 缺 ③；Q0017 缺 ③；Q0004 ③隐式。**第②条 "为什么联想到该方法" 几乎全缺**——这是把宝典与试题汇编区分开的核心教学桥段。 | 强制 4 块结构模板：`① 材料动作 / ② 联想理由 / ③ 卷面答案句 / ④ 易错 + 边界`。在每条条目顶部用同一格式写齐，缺块的不得入 V1 review draft，更不得入正稿。 |
| F3 | High | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §五 Q0017；`04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` §三.3 Q0015 / §三.4 Q0012 / §四.2 Q0016 | 选择题条目反复出现"正确选 D / 选 B / 选 A / A 是错误分析"，**未抄录 A/B/C/D 四选项原文**。学生脱离试卷无法校验分析，且该书 §排雷只批"B、C 是把治理流程误挂为创新思维 / 发散思维"，连 B、C 原文是什么都没写。Claude 外审重点之一就是"学生误读风险"，这条直接踩雷。 | 每条选择题条目内联粘贴四选项原文（A 原文 / B 原文 / C 原文 / D 原文），逐项给"为什么对 / 为什么错（错在哪条规则）"。正确答案后面 **必须** 跟"为什么 A 不对 / B 不对 / C 不对"逐项解释。 |
| F4 | High | `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` 大部分条目 vs `TASK_BRIEF.md` §产物二 | TASK_BRIEF 规定每条推理条目必须答：① 推理形式 ② 可检查的逻辑式子 ③ 有效式 / 无效式 / 谬误点 ④ 同类题对比差别。Q0013 / Q0015 / Q0016 / Q0012 缺 ② 逻辑式子；Q0006/Q0008/Q0009 有自然语言形式但缺符号化（如 `p→q, ¬q ⊢ ¬p`）；几乎所有条目缺 ④ 同类题对比（书内 Q0006↔Q0008↔Q0009 三条充分条件不同变形，本应横向对照），只是按 question 顺序罗列。 | 每条加 `形式化` 块（用 "若 p 则 q；非 q；故非 p" 的可读符号化形式）+ `同类题对比` 块（明确点 Q-ID 链接：例如 Q0006 否后否前↔Q0008 肯后否定↔Q0009 充分肯前→必要肯前，并写出"差别在哪里"）。 |
| F5 | High | `03_claudecode_lane/fusion_candidates.csv` vs `01_source_inventory/QUESTION_COVERAGE_MATRIX.csv` | 以下 10 行被 B 线标 `A-formal / high / accept`，**全部未进 A 线 coverage matrix / 未分配 Q-ID**：FC-MT-005 (2026朝阳一模 17(1) 联想思维)、FC-MT-006 (2026海淀期末 20(2) 超前三件套)、FC-MT-007 (2026海淀一模 17(2) 四类思维)、FC-RE-014 (2024.11朝阳期中 18 不完全归纳+类比)、FC-RE-015 (2026朝阳一模 17(1)前半 归纳)、FC-RE-016 (2026海淀期末 20(1) 充分肯后)、FC-RE-017 (2026海淀一模 17(1) 划分+选言)、FC-RE-018/019/020 (2026西城一模 19(3) 三村民形式逻辑三视角)。其中 FC-RE-014 / FC-RE-015 / FC-RE-017 直接对应推理宝典 §五 自己点的"待扩容"节点（类比 / 不完全归纳 / 选言）。**说"找不到"是错的——B 线已经找到了，A 线 source-lock 落后了。** | 把这 10 行立刻提到 A 线 source-lock 优先级队首，分配 Q0018-Q0027，本轮不要再去找新候选；先把 B 线已找到的回源锁齐。 |
| F6 | High | `03_claudecode_lane/blockers.csv` BLK-001 vs `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §二.1 Q0011 | BLK-001 状态 open，next_action 写 "Codex 回源核验028/029完整答案；若新源出现三模块并列则提请用户裁定"。但是：(a) 已 spot-check 227192d22e10241b:30-54 = 三模块并列已实质出现；(b) 用户 / 飞哥 裁定记录不存在；(c) Q0011 已被收入 review draft。**promotion gate 失效。** | 立刻执行二选一：要么按 F1 改写后闭合 BLK-001（写明裁定证据 + 时间），要么把 Q0011 从 draft 拉回；不得"blocker open 且 entry 已上"两态共存。 |
| F7 | High | `03_claudecode_lane/blockers.csv` BLK-003 / BLK-004 vs review draft | BLK-003：声称 2025顺义一模 Q7 "选项与答案 letter 待回源"；但 `02_codex_lane/FAMILY_SOURCE_PACKETS_Q0006_Q0012.md` §Q0012 已写 "正确选 A，因为 A 选项中的推理实际犯'大项不当扩大'..." 且引 `gpt_sources/9dd43cae...:88-115`。两边账目不一致。同样 BLK-004（2025西城二模 16(2)）与 Q0008 source packet（已引 `cfb0f19...:52-53`）也存在 open blocker + entry already imported 矛盾。 | 二选一同上：要么用引用证据**显式闭合** BLK-003 / BLK-004（在 `blockers.csv` 改状态 + 写闭合证据行号），要么把 Q0012 / Q0008 拉回。account state 必须自洽。 |
| F8 | Medium | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §三.1 Q0003 "满分安全线" | 写 "细则明确，满分需要三新之外至少两个创新解决问题的方法"。但条目里没有逐字摘抄细则原文。学生 / 阅卷老师如要复核给分阶梯，必须自己去找 `885e694...:142-151`。教学权威性弱化为二手叙述。 | 在每个"满分安全线 / 阅卷提醒 / 阅卷反向"块下加 `细则原文摘录` sub-block，逐字粘贴 1-3 行评分规则原文 + 行号。同问题在 Q0002 阅卷提醒、Q0010 大项不当扩大判定中也要补。 |
| F9 | Medium | `04_fusion/REASONING_BAODIAN_REVIEW_DRAFT.md` §五 vs fusion_candidates | §五 写 "选言推理 / 归纳推理 / 类比推理 当前 A 线尚未 source-lock 代表题"。但 FC-RE-014（不完全归纳+类比，accept/high）、FC-RE-017（选言，accept/high）、FC-RE-015（归纳，accept/high）已是 B 线 accept 行。措辞过谦或误导：让人以为"无源"，实情是"已发现，未编入"。 | 改写 §五：分两栏 — "已被 B 线锁定待 A 线编入"列出 FC-RE-014 / 015 / 017 等具体行号；"两线都未发现"留作真未覆盖。让 PROGRESS 看得见。 |
| F10 | Medium | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §二.1 Q0002 答题模板 | 整段 ~110 字一句到底，五个辩证角度叠在同一句。评标实录显示学生最常漏 "辩证否定"，但本条 "阅卷提醒" 只警告 "只答分析或只答综合"，没有提醒 "辩证否定 / 质量互变 / 动态性 三者最易漏"。 | 答题模板拆 5 个短句，一句一角度（分析与综合 / 整体性 / 质量互变 / 动态性 / 辩证否定）；阅卷提醒列出 5 个角度名 + 标"最易漏 / 最易混"。 |
| F11 | Medium | `04_fusion/A_B_DIFF_SNAPSHOT.md` "Fusion Rule Going Forward" | 现规则 "B-line rows with full source paths and no blocker can be imported only after A backcheck" 太软：未明确定义 "imported into" 是指 ledger 还是 review draft；未规定"BLK open 时 entry 必须挂起"；未规定 4/5 必答要素是入册门槛。Q0011 + Q0008 + Q0012 三起越权已发生。 | 增加显式 **Promotion Gate**：一条 Q-row 进入 `*_REVIEW_DRAFT_*` 必须同时满足 (i) 关联 BLK-* 已闭合；(ii) 4 元素（思维）或 5 元素（推理）模板填全；(iii) A∩B 共识 或 有 A backcheck 文件记录；(iv) 选择题必含选项原文。任一项不满足，挂 `04_fusion/PROMOTION_HOLD.md` 而不是进 draft。 |
| F12 | Low | `04_fusion/THINKING_BAODIAN_REVIEW_DRAFT.md` §四.1 Q0004 | 选择题排雷写 "见'融合、整合'不一定就是系统优化"，是有用的边界，但缺正例对照——学生无法校准"什么情况下融合 / 整合 *就是* 系统优化"。 | 待 FC-MT-006 (2026海淀期末 20(2) 超前三件套 / 含系统优化场景) 落 A 后，挂为正例对照；当前先标注 "正例待 Q0018+" 不要装作完备。 |
| F13 | Low | `PROGRESS.md` 末行状态码 | `CLAUDECODE_RUNNING_A_LINE_17_LOCKED_B_BACKCHECK_PARTIAL` 准确但读不出体量。思维 7 entries / 推理 10 entries / 已 source-locked 17 题 vs 估计候选 60+，对硬规则 "结合三年所有题、不只做代表例题" 的差距没暴露在状态码里。 | 状态码后追加 "drafts 覆盖率 ~17/估计 60+ 题，距全量穷尽相差 ≥ 70%"。让后续接手者一眼看到剩余压力。 |

## Coverage Pressure List

按需要优先释放的压力倒序：

1. **三模块复合题节点**：Q0011 重写后即成首条；2024 海淀二模这类"题干说 A 思维 / 细则收 B+C+D 思维"型题在 2024-2025 各区试卷中很可能不止一道，需要专门扫一遍（关键词触发：题干 "如何体现 X 思维"；细则出现 "Y 思维角度 _ 分 / Z 思维角度 _ 分"）。
2. **B-line 已 accept 但 A-line 未 source-lock 的 10 行**（F5 名单）。**这是最高 ROI 的下一动作**：免去搜寻成本，直接 review-into-coverage。
3. **类比推理 / 选言推理 / 归纳推理 / 概念划分** 四类推理形式：FC-RE-014（不完全归纳+类比，2024.11朝阳期中 18）、FC-RE-017（划分+选言，2026海淀一模 17(1)）、FC-RE-015（归纳，2026朝阳一模 17(1)前半）是现成入口。
4. **2025 全套主观题 backlog**（BLK-008）：仅 2025海淀二模 Q20 + 2025西城二模 Q16(2) + 2025顺义一模 Q7 落定；2025各区一模/二模/期末 全集未扫。
5. **2024 全套主观题 backlog**（BLK-009）：仅 2024朝阳一模 Q20(1)(2)、2024海淀二模 Q17(1)、2024.11朝阳期中 Q18 落定。
6. **2026 全套主观题 backlog**：通州/东城/顺义/朝阳/海淀/丰台 部分锁定；FC-RE-018/019/020 (2026西城一模 19(3)) 在 B 线 accept 队但未入 matrix；2026石景山期末按 BLK-011 排除（用户已确认无细则）。
7. **24年北京高考 Q19(2) 青海防沙治沙** (BLK-010)：需新建北京高考 suite，本轮未启动。
8. **选择题陷阱语料**（BLK-006/007）：2026顺义一模 Q1-Q15、2026朝阳一模 Q1-Q15 未逐题判断哪些是选必三选择题。当前 choice_trap 只有 Q11 / Q9 两条代表，远不足支撑"选择题陷阱"作为独立模块。
9. **真实 GPT Pro 外审**（BLK-013）：未提交。所有 draft 都不能跨过 `REVIEW_DRAFT_NOT_FINAL` 状态线。
10. **评标实录 / 讲评 PPT 三角证据**：当前仅 Q0002 有 A-formal 细则 + 讲评 + 评标实录 三重。其余 A-formal 条目大多只靠细则一种证据。增加教学权威性应优先补 Q0003 / Q0011 重写版的讲评层。

## Fusion Recommendations

V0 → V1 的最快、最少返工路径：

1. **冻结新条目录入。** 17 条尚未健康，再加只会放大 F2/F3/F4 模板债务。
2. **F1 优先：重写 Q0011。** 这是唯一的 Critical，且测试 promotion-gate 是否能真正生效。
3. **执行 F11 promotion gate**：在 04_fusion 下创建 `PROMOTION_GATE.md`（规则）+ `PROMOTION_LOG.md`（每条 Q-row 通过门控的逐项打钩证据）。Q0001-Q0017 全部重新过门。
4. **F2 / F3 / F4 模板回填**：全部 17 条按 4 元素（思维）/ 5 元素（推理）补齐；选择题全部补 A/B/C/D 选项原文 + 逐项错因。
5. **F5 候选晋升**：把 10 行 B-accept 候选分配 Q0018-Q0027，源锁 + 入模板 + 进 matrix。优先补 §五 自爆缺口的 FC-RE-014 / 015 / 017。
6. **F6 / F7 blocker 状态对账**：BLK-001 / BLK-003 / BLK-004 三条要么用证据闭合并归档，要么撤回对应条目。`blockers.csv` 与 `*_REVIEW_DRAFT_*` 必须互相自洽。
7. **F8 细则原文摘录**：补 Q0002 / Q0003 / Q0010 的细则原文 1-3 行 + 行号。
8. **F9 推理册 §五 重写**：分"待 A 编入" / "两线未发现" 两栏。
9. **F10 Q0002 答题模板拆句 + 阅卷提醒列五角度**。
10. **不要提交 GPT Pro 外审，直到 F1-F7 全部闭合**。在已有 Critical 错路由的 draft 上烧外审 quota = 浪费一轮真实外审证据。
11. **不要生成 DOCX / PDF**。当前 markdown 都未稳定。
12. **下一次 Claude 外审 V1 packet 中**：必须把 (a) Q0011 重写后版本 (b) 选择题完整选项后版本 (c) PROMOTION_LOG.md 三者纳入审阅。否则等同绕过本轮发现。

## Forbidden Final Claims

下列说法在任何 user-facing 产物（宝典 MD / DOCX / PDF / README / 进度小结 / 移交消息 / 用户对话）中**均不得书写、不得显示、不得暗示**：

- 不得写 "选必三《逻辑与思维》宝典 已完成 / 终稿 / 定稿 / V1 / 最终版"。
- 不得写 "已穷尽 2024-2026 三年北京选必三考题"、"全量覆盖"、"已覆盖所有选必三题"。
- 不得写 "已经过 Claude 外审 / 通过 Claude review / Claude PASS"。本审显式不写 PASS。
- 不得写 "已经过 GPT Pro 外审 / GPT Pro 已通过"（BLK-013：未提交）。
- 不得用 "思维宝典涵盖 X 种思维方法 / 推理宝典涵盖 Y 种推理形式" 来暗示完备性。
- 不得宣称 "Q0011 / 2024海淀二模 17(1) 是科学思维单角度标准例题"（F1：官方细则是 三模块复合 2+3+2）。
- 不得宣称 "BLK-001 已闭合"（除非 F1 重写已落地并显式闭合）。
- 不得宣称 "BLK-003 已闭合 / BLK-004 已闭合"（除非 F7 对账并显式闭合）。
- 不得写 "可作为学生练习材料 / 可直接发学生 / 可印刷下发"（选择题缺选项原文，F3）。
- 不得写 "A/B 双线已对齐 / 双线闭合 / 双线一致"（10 行 B-accept 仍在 A coverage 之外，F5）。
- 不得写 "已交付 / delivered / ready-to-ship / 入正稿"。
- 不得给区/年份/试卷-级完成率数字。当前 17/估计 60+ 仍极小，公布数字会误导。
- 不得引用本审结果反过来说 "Claude 已确认 Q0001-Q0010 没问题"。本审只 spot-check 了 Q0001 + Q0011 两条原始题面与细则；其余 15 条只做账面比对，未逐题回源。
- 不得在 PROGRESS.md 状态码中把 `EXTERNAL_REVIEW_DONE_NOT_PASS` 简写为 "external review done"——必须保留 NOT_PASS 后缀。

下一可达状态（建议命名）：`V0_EXTERNAL_REVIEWED_REQUIRES_REWRITE_BEFORE_V1`。

— Claude 外审 (独立 lane) · 完
