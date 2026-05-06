GO_TO_PHASE11_CONTROLLED_EXPANSION_OR_CONTENT_REVIEW_NO_WORD_NO_FINAL
verdict
Phase10 通过 polish/outline gate，可以进入 Phase11。Phase11 不得 Word/PDF，不得 final PASS，不得称终稿、最终稿、宝典成品。
Phase11 不应直接大规模扩成 74 行正文。正确路线是：

Phase11A：先对现有 29 行 polished student body 做逐题内容审查和风险修补
Phase11B：再从 74 evidence rows 中按本地 evidence gate 小批量 controlled expansion
理由：Phase10 已满足当前阶段边界要求，29 行未扩张，hard-excluded rows 没有展开，内部术语扫描为 0，Codex A 为 PASS_CODEXA_PHASE10_POLISH，Lane B 为 PASS_PHASE10_POLISH_AUDIT_WITH_WARNINGS 且无 blocker，C33 已 patch，C34 被接受为风格选择，Governor 与 Confucius 均给出 pending GPT 的 pass。
must-fix before Phase11 expansion
以下不是退回 Phase10 的 blocker，但在 Phase11 扩展到更多题前必须先锁住。
1. Q-2025顺义一模-7
当前 Phase10 保留了正确风险线：
真实错误：大项不当扩大
A 项错误：把它说成小项不当扩大
Phase11 必须继续保留 036 顺义参考答案 源迹。不得把它写回“小项不当扩大”。Phase10 risk register 已补 Audit Source Trace Pointers，指向 Phase09 risk register 中的 036 顺义参考答案摘录。
硬规则：

任何文件出现“Q-2025顺义一模-7 = 小项不当扩大”为正确结论，直接回滚。
2. Q-2025丰台期末-7
继续保持边界陷阱，不进入选必三思维主链。
固定处理：

主落点：哲学唯物论，从实际出发，从当下做起
选必三超前思维：干扰项
Phase10 已把它放在“边界陷阱”小节，Confucius gate 也确认该处理能防止学生把它误当超前思维正例。
3. Q-2026顺义一模-19-2
继续保持：
主讲线：科学思维三特征
辅助线：推理骨架
不得改写成典型三段论题。Phase10 已在正文中写明“主讲线是科学思维，不是典型三段论”，并在控制矩阵中保持 primary_mount=思维, secondary_mount=推理。
4. Q-2024朝阳二模-19-1 / 19-2
Phase11 继续保持无审稿味表达：
无细则编号
无文件编号
无来源页码
无审稿术语
统一使用第一空 / 第二空
Lane B 已确认 Phase10 中没有 audit/source/file wording，且“第一空/第二空”表达已保留。
5. Q-2024朝阳一模-20-1 / 20-2 与 Q-2026通州期末-19-2
充分条件、必要条件必须继续分开。
固定规则：

充分条件：肯定前件有效，否定后件有效
必要条件：肯定后件有效，否定前件有效；仅肯定前件不能肯定后件
Phase10 对这三题已保持充分/必要条件规则分离，Lane B 与 Governor 均确认该锁定。
6. Q-2026丰台一模-18-2
L4 hard sample 不得压缩。
必须保留完整链条：

甲：必要条件假言推理，肯定后件式，前提真实，正确
乙：三段论，大项在前提中不周延却在结论中周延，大项不当扩大，错误
不得简写为“甲正确、乙错误”。Phase10 已完整保留该链条。
7. Q-2025海淀二模-20
继续保持角度池写法：
辩证思维角度池
从角度池中选材料最顺的两个写深
不能写成三点全必答
不能写成 3 点固定赋分模板
Phase10 已保留 angle-pool 处理，Governor 与 Lane B 均确认没有回流“三点全必答”。
8. hard-excluded rows
以下题仍只能作为同类题索引或缺席，不能展开答案、选项、题型结论：
Q-2024西城一模-11
Q-2025海淀二模-12
Q-2025海淀二模-13
Q-2026顺义一模-3
Phase10 traceability backcheck 显示这些 hard-excluded rows 没有 visible heading、没有 raw QID 正文展开，状态为 PASS。
Phase11 should do
Phase11 建议命名：
Phase11 controlled content review and evidence-gated expansion
Phase11A：先审 29 行，不扩张
必须产出：
09_student_draft/phase11_29row_content_review_matrix.csv
09_student_draft/phase11_29row_patch_plan.md
09_student_draft/phase11_QID_lock_recheck.md
09_student_draft/phase11_internal_terms_scan.md
09_student_draft/phase11_same_type_index_no_expansion_check.md
逐题检查：
1. 每道思维题是否仍有材料信号、可写思维/方法、为什么能想到、答题动作、答案落点、易错陷阱、同类题。
2. 每道推理题是否仍有题型、逻辑形式、规则口诀、有效式或错误式、解题动作、答案落点、易错陷阱、同类题。
3. 每道交叉题是否保留主讲线与辅助线。
4. 选择题是否统一为“选 X，组合项”。
5. 主观题是否保留可直接写到答题纸上的答案落点。
6. hard-excluded rows 是否仍未展开。
Phase11B：再做受控扩张，不得一次性写满 74 行
允许从 74 evidence rows 中扩张，但必须分批：
Batch E1：L4 剩余可扩题
Batch E2：L3 中字段完整、无 answer locator risk、无 reasoning form risk 的思维题
Batch E3：L3 中字段完整、logical_form 完整的推理题
Batch E4：交叉题双挂载完整题
每批新增前必须生成：
05_coverage/phase11_expansion_candidate_gate.csv
05_coverage/phase11_expansion_candidate_source_check.md
09_student_draft/phase11_expansion_delta_control_matrix.csv
09_student_draft/phase11_expansion_delta_student_body_REVIEW_ONLY.md
每个新增题必须满足：
source locator exists
answer locator exists
full stem/options or rubric exists
module scope locked
thinking chain complete or reasoning chain complete
not L0
not hold
not hard-excluded
student_permission remains review_only
新增题不得来自：
45 hold rows
288 L0 rows
hard-excluded rows
old artifact conclusions
same-type index only references
boundary risks
1. 29 行 polish 质量通过，不等于 74 行可以自动入稿
当前 Phase10 只证明 29 行可控。Phase11 扩张必须逐题过 gate。不能把 74 evidence pool 一次性转成正文。
2. 同类题索引有“暗扩张”风险
同类题索引是学生可见的题目名称列表。Phase11 若把索引题自动展开，会绕过 evidence gate。必须继续保持：
same-type index = readable index only
not explanation
not answer
not option pairing
3. L3_candidate 不能伪装成 L4
29 行中 L3_candidate 占多数。Phase11 可以继续 polish，但不得在审计表或正文语气上把 L3 写成“完全锁定标准题”。
4. 去分值化是可接受风格，但不能损失答题长度提示
Lane B C34 指出 Phase10 去掉少量 (X分) 分值提示。Codex 接受为风格选择。Phase11 若继续去分值化，必须用“写两条”“分角度”“每条带材料事实”等表达弥补答题长度提示。
5. 边界陷阱不能被章节重排吞掉
Q-2025丰台期末-7 必须继续单列边界陷阱。若 Phase11 扩展章节结构，不得把它合入“超前思维”正例。
allowed next actions
允许：
1. 启动 Phase11。
2. 先做 29 行 content review。
3. 对 Phase10 29 行做微 patch。
4. 在本地 evidence gate 后，小批量扩展到 74 evidence rows 的一部分。
5. 建立 expansion candidate gate。
6. 继续让 Lane B 审 Phase11 输出是否越界。
7. 继续走 Governor / Confucius / GPT gate。
Phase11 可以申请的下一步最多是：
controlled expanded Markdown review
不能申请：
Word
PDF
final PASS
终稿
最终稿
宝典成品
still forbidden
继续禁止：
Word
PDF
final PASS
终稿
最终稿
宝典成品
一次性扩成 74 行正文
加入 45 hold rows
加入 288 L0 rows
展开 hard-excluded rows
把 same-type index 自动扩成解析
改变答案
改变 pairing
改变题型归属
改变交叉题主辅线
删除 QID traceability
local checks before any later final Markdown / Word stage
Codex 必须先跑：
1. row count check：正文行数、控制矩阵行数、QID set 一致。
2. no expansion check：新增题全部来自 expansion_candidate_gate。
3. hard-excluded scan：Q11/Q12/Q13/顺义一模3 不展开。
4. Q11 scan：不得出现 B=①④ 作为 Q11 正确 pairing。
5. internal terms scan：Phase、packet、source locator、lane、Governor、Confucius、L3、L4、B-choice-signal、路径、细则编号等在学生正文中为 0。
6. answer consistency check：选择题答案字母和组合项一致。
7. reasoning form check：推理题 logical_form、规则、有效式/错误式、解题动作不缺。
8. thinking chain check：思维题材料信号、可写方法、为什么能想到、答题动作、答案落点不缺。
9. cross mount check：交叉题主讲线、辅助线不丢。
10. traceability check：每个正文条目能回到 control matrix。
ClaudeCode Lane B 必须审：
1. Phase11 是否仍只含 29 行或经 gate 新增的题。
2. 新增题是否来自 74 evidence rows 且不是 hold/L0。
3. 新增题是否改变答案或 pairing。
4. hard-excluded rows 是否仍未展开。
5. 同类题是否仍只作索引。
6. 学生可见文本是否有内部词。
7. 推理部分是否又退化成题型总述。
8. 思维部分是否又退化成知识摘要。
Governor gate 必须审：
boundary
row count
source gate
hard locks
no Word/PDF/final
Confucius gate 必须审：
学习价值
触发链
解题动作
迁移性
边界陷阱
同类题索引是否有用
final line
GO_TO_PHASE11_CONTROLLED_EXPANSION_OR_CONTENT_REVIEW_NO_WORD_NO_FINAL

