# Codex A Governor - External P0 Patch Regate

运行目录：`/Users/wanglifei/Desktop/北京高考政治/选必一_当代国际政治与经济_四线终极全书_2026-05-03`

门禁对象：
- `07_student_doc/by_question_view_draft_20260503.md`
- `07_student_doc/six_bucket_to_question_crosswalk_draft.md`
- `08_review/external_by_question_p0_patch_log_20260503.md`

本轮职责：只判断 P0 补丁后的两个学生预览文件是否可进入“内部学生预览下一版”。本门禁不放行学生终稿，不放行 Word/PDF，不放行 FINAL_ACCEPTANCE，不放行 coverage close。

## 结论

**PASS_WITH_GUARD：允许进入“内部学生预览下一版”。**

允许范围仅限内部学生预览流转、继续审稿、继续做学会性和覆盖复核。当前版本已经处理外部二审提出的主要 P0 阻断点，且两个学生预览文件未发现后台路径、内部模型名、证据层级标签、P0/P1/P2 标签等学生污染。

**继续阻断：final / Word / PDF / FINAL_ACCEPTANCE / coverage closed。**

原因：当前仍是 preview draft；full-source exhaustion、coverage matrix 回填、Confucius 零基础迁移验收尚未完成，不能把预览稿当成最终可交付件。

## 污染扫描结论

学生预览文件检查结果：
- 未发现 `P0/P1/P2`、`GPT/Claude/Codex/Governor/Patcher/worker/fusion/atom` 等内部标签进入学生稿。
- 未发现 `/Users/...`、本地路径、SOURCE/LEDGER/COVERAGE/FINAL_ACCEPTANCE 等后台文件或流程词进入学生稿。
- 未发现 Word/PDF/DOCX/final 等终稿交付词误入学生预览正文。
- 检出的“模型缺陷”“大模型”属于题目材料/学科语境词，不属于后台 model 污染。
- `08_review/external_by_question_p0_patch_log_20260503.md` 作为内部补丁日志可保留 P0/审稿/patch 等标签，但不得并入学生版。

判定：**学生污染扫描通过。**

## P0 补丁复查

1. 顺义一模 Q20：已补回“和平与发展仍是时代主题”的材料触发、核心判断和答案表达，当前可作为内部预览。
2. 海淀期中 Q16(2)：已把“全球经济治理/规则制定”归回经济全球化桶，并区分企业动作、产业链动作、政府/治理动作，普通答案未被冒充为细则。
3. 海淀期中 Q21(2)：已补入“新中国成立初期、改革开放后、新时代”分阶段外交背景，预览稿表达可读。
4. 通州期末 Q20：已改成学生可用表达“中国把全球治理倡议作为重要国际公共产品贡献给世界”，避免后台化措辞。
5. 朝阳一模 Q20：第四段已改为“可选扫尾”，没有把边界性升华句写成必答核心。
6. 海淀二模 Q21：新型国际关系被放在可选表达/桥接位置，未替代联合国主线结构。
7. 西城期末 Q20：已压缩概念堆叠，主写人类命运共同体与真正多边主义；联合国表达已收窄到气候治理框架。
8. 2024东城一模 Q16/Q20、2025海淀期末 Q22：已进入拓展迁移区，标为“选必一可用片段”，未伪装成固定答题卡模板。
9. 六桶交叉表：已同步桥接逻辑和使用条件，能支撑内部预览版继续核对。

判定：**P0 补丁已达到内部预览下一版门槛。**

## 仍禁止动作

- 禁止生成或宣布学生终稿。
- 禁止生成 Word/PDF/DOCX 正式交付。
- 禁止写 FINAL_ACCEPTANCE 或任何等价闭环验收结论。
- 禁止宣布 coverage closed。
- 禁止把 P1/P2、边界题、迁移片段、普通参考答案升级为 P0 必答核心或高频计频依据。
- 禁止把 GPT/Claude 外部意见作为事实来源；外部意见只能触发本地证据复核。

## 下一步必须任务

### Confucius

- 用学生稿自身做 artifact-only 学会性验收，不回看后台表。
- 测试零基础学生是否能从材料信号选出主桶、可选表达和禁用提醒。
- 对 8 个答题卡题和 3 个拓展迁移题分别做盲写迁移检查。
- 专查“概念堆叠”“跨模块误入”“万能句替代材料逻辑”三类风险。

### Coverage

- 将按题稿、六桶交叉表、scoring atom 表、SOURCE_LEDGER、COVERAGE_MATRIX 逐项对齐。
- 核查每个题号是否有来源、细则/证据等级、材料触发、答案句和边界说明。
- P1/P2、图片确认、普通参考答案、边界题只能按其原证据等级记录，不得计作 P0 高频闭合。
- coverage 只能进入继续复核状态，不得 close。

### Full-source

- 继续处理未读完或未完成定位的源文件和套卷。
- 对普通参考答案、教师版参考答案、评分细则、评标、阅卷/讲评口径继续做来源分层。
- 对海淀、朝阳、通州、西城等已入稿题目做二次源复核，确认没有遗漏同题更高等级证据。
- 新增来源只能先进入 worker/fusion/patcher/governor 链路，不能直接写入学生终稿。

## Governor 最终判定

`INTERNAL_STUDENT_PREVIEW_NEXT_VERSION: PASS_WITH_GUARD`

`FINAL_STUDENT_VERSION: BLOCK`

`WORD_PDF_DELIVERY: BLOCK`

`FINAL_ACCEPTANCE: BLOCK`

`COVERAGE_CLOSE: BLOCK`
