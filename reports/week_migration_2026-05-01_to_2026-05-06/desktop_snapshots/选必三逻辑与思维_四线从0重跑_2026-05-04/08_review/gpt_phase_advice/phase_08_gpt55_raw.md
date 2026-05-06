已按 Phase08 附件审阅。这次只裁 Phase08 到 Phase09 的门，不放 Word/PDF、final PASS 或成品口径。
Thought for 6m 11s
GO_TO_PHASE09_STUDENT_DRAFT_CONSTRUCTION_NO_WORD_NO_FINAL
verdict
认可 Phase08 在 warning patch 之后通过 review-only prototype gate，可以进入 Phase09 受控学生稿构建阶段。边界很窄：只允许把已通过 Phase08 的 29 行 prototype 转成受控学生稿草案，不允许扩展到 74 行全量证据池，不允许纳入 45 个 hold rows，不允许纳入 288 个 L0 rows，不允许 Word/PDF，不允许 final PASS，不允许称终稿、最终稿、宝典成品。Phase08 的关键门禁已经闭合：29 行输入、29 行 prototype CSV、29 个 Markdown question blocks；hold rows 与 L0 rows 未泄漏；Lane B blockers 为 0；Codex A post-patch failures 为 0；Governor 与 Confucius 均为 pending GPT 的 review-only pass；Lane B 原先发现的术语残留、两个选择题答案字母缺失、审稿味表达等均已 patch。
must-fix before Phase09 first draft freeze
Q-2025丰台期末-7 不能放入思维主链正文。它的当前表达明确指向哲学唯物论，从实际出发、从当下做起，选必三超前思维只是干扰项。Phase09 必须把它放进边界陷阱或易错辨析小节，标签建议为 boundary_trap，不得作为选必三思维方法正例。
Q-2025顺义一模-7 的答案落点存在高风险表述。prototype 写到 A 选项原归类正确而该选项陈述错，这个表述容易自相矛盾。Phase09 进入学生稿前，Codex A 必须回 Phase08 freeze 与原答案依据核验：正确选项 A 的原因到底是 A 对谬误判断错误，还是题干问法为逻辑分析错误。没有核验前，只能保留为待审表达，不得定稿化。
Q-2026顺义一模-19-2 虽然进入交叉双挂载，但内容主体是科学思维三特征，推理挂载写成三段论/判断/推理存在误导风险。Phase09 必须把主讲位置放在科学思维，推理侧只作为题目框架或共采分辅助，不得把它写成典型三段论题。
Q-2024朝阳二模-19-1 与 Q-2024朝阳二模-19-2 不能在学生稿中保留任何细则编号、文件编号、填空编号审稿味表达。Phase08 已 patch 掉 细则022 之类痕迹，Phase09 仍需复扫 generated student text，保证不回流。
Q-2024朝阳一模-20-1、Q-2024朝阳一模-20-2、Q-2026通州期末-19-2 都是假言推理题，Phase09 必须把充分条件、必要条件的有效式分开写，不得混用口诀。特别是必要条件假言推理，必须核准肯定后件、肯定前件的有效性表述。
Q-2026丰台一模-18-2 是 L4 hard sample，必须保留已锁动作链：甲为必要条件假言推理肯定后件式且前提真实，乙为三段论大项不当扩大。不得简写为甲正确乙错误，也不得改成演绎推理泛称。
Q-2025海淀二模-20 必须保持角度池写法。学生稿中只能写三个可选角度池中选材料最顺的两个写深，不能回到三点全必答，也不能写成 3 点乘 2 分。
Q-2024西城一模-11、Q-2025海淀二模-12、Q-2025海淀二模-13、Q-2026顺义一模-3 不得作为 Phase09 正文题条目进入。它们在 Phase08 中只是 hard-excluded 或同类题 ID 引用，不能借 Phase09 扩写时被展开。
allowed next
Phase09 可以启动，阶段名建议固定为：
Phase09 controlled student draft construction from Phase08 prototype only
允许产出：
09_student_draft/phase09_student_draft_CONTROLLED_FROM_29.md
09_student_draft/phase09_student_draft_control_matrix.csv
09_student_draft/phase09_question_id_backcheck.csv
09_student_draft/phase09_opus_or_codex_change_log.csv
09_student_draft/phase09_internal_terms_scan.md
09_student_draft/phase09_QID_risk_register.md
08_review/phase09_codexA_student_draft_verification.md
claudecode_lane/opus47_phase09_student_draft_audit/phase09_laneB_student_draft_audit.md
08_review/phase09_Governor_student_draft_boundary_gate.md
08_review/phase09_Confucius_learning_value_gate.md
08_review/phase09_GPT_commander_review_packet.md
Phase09 第一版只能来自 Phase08 29 行。任何新增题、扩题、补题，都必须回到 Phase07 packet 和本地源证据，不能由 Opus 或 GPT 直接补。
blocked
继续阻断：
Word
PDF
final PASS
终稿
最终稿
宝典成品
把 74 行全量证据池直接写成学生稿
把 45 个 hold rows 写入学生稿
把 288 个 L0 rows 写入学生稿
把 hard-excluded rows 展开成正文
把同类题 ID 自动扩成答案讲解
把 L3_candidate 写成完全锁定
RUN_ADDITIONAL_LANEB_AUDIT 目前不需要。Lane B Phase08 为 PASS_PHASE08_PROTOTYPE_AUDIT_WITH_WARNINGS，warnings 已 patch，post-patch Codex A、Governor、Confucius 均显示 review-only gate 可提交 GPT。下一轮 Lane B 应审 Phase09 学生稿草案是否越界，不需要先重跑 Phase08。
STOP_SOURCE_REPAIR_REQUIRED 也不成立。当前没有源证据 blocker，主要是学生稿阶段的内容表达风险与边界归类风险。

next-phase hard rules
Phase09 只写 29 行受控学生稿草案，必须逐条保留 question_id 到内部对照表。学生可见正文可以不显示内部状态，但审计表必须能回查每段来自哪个 question_id。
思维部分必须按 材料信号 -> 可写思维/方法 -> 为什么能想到 -> 答题动作 -> 答案落点 -> 易错陷阱 -> 同类题 转写，不能压缩成知识点摘要。
推理部分必须按 题型 -> 逻辑形式 -> 规则口诀 -> 有效式或错误式 -> 解题动作 -> 答案落点 -> 易错陷阱 -> 同类题 转写，不能变成题型总论。
交叉题必须保留双挂载。Phase09 可以减少重复表述，但必须在审计表中保留主挂载与次挂载，不能单挂。
所有同类题列表只能保留 question_id 或审计索引，不能展开 hard-excluded rows 的答案、选项、题型结论。
L3_candidate 题在学生稿草案中必须保留审稿状态标记到内部表，不得在正文语气上写成最终标准例题。L4 可以更稳定，但仍不能授权 final。
选择题必须显式写正确选项字母和组合，例如 选 C，②③，不得只写 ②③ 或只写答案理由。
主观题必须写考场可执行动作，不得只写知识名词。每条至少有一条可以直接搬到答题纸上的表达。
禁止出现内部词：Phase07、Phase08、packet、source locator、lane、Governor、Confucius、L3、L4、B-choice-signal、LOCKED_FOR_FUSION、文件路径、细则编号式残留。
Q11 错配硬锁继续生效。任何 Phase09 文件若把 Q-2024西城一模-11 写成 B=①④，直接回滚该文件。
Q12/Q13 不得进入 Phase09 正文。若作为同类题 ID 引用，只能保留 ID，不得写答案 D/C 或展开讲解。
Q-2026顺义一模-3 不得进入推理正文。若作为思维同类题引用，只能在思维侧出现。
Phase09 完成后必须先过 Codex A verification，再过 ClaudeCode Lane B audit，再过 Governor/Confucius，再提交 GPT review。通过这些 gate 之前，仍禁止 Word/PDF 和 final PASS。
