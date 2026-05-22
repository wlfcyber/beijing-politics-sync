# V7.1 Source-Card Repair Queue

- generated_at: 2026-05-21T09:27:16
- purpose: block V7.1 from final sealing until empty ask rows and high-risk source cards are repaired or downgraded.
- canonical evidence baseline remains: 65 subjective questions, 61 formal, 4 reference_only, 0 missing.

## Counts

- source_confirm_required: 10
- repair_now: 6
- downgrade_insurance_box: 1
- split_subquestion_only: 1
- reference_only_lock: 1
- clean_source_card_before_core: 1
- clean_rubric_atoms_before_core: 1
- split_atoms_before_core: 1

## Student-Core Gate

- allowed_in_student_core=no: 9
- allowed_in_student_core=conditional: 11
- allowed_in_student_core=yes_after_cleaning: 2

## Decisions

### CC0019_2024_朝阳_一模_19
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: no
- reason: 虽有诚信原则/民法典信号，但缺真实设问，不能直接进入学生核心逐题示范
- next_action: 回源定位试卷页与答案/细则页，确认是不是法律主观题及问法

### CC0077_2025_东城_一模_19
- problem_type: ask_text_missing
- decision: repair_now
- allowed_in_student_core: conditional
- repaired_ask: 阅读材料，完成下表。
- reason: 题面出现三个案例与表格任务，设问功能稳定；需补入 ask_text 后再逐格拆分
- next_action: 将设问写入修补表；后续按表格列名回源补齐空格

### CC0084_2025_东城_二模_19
- problem_type: ask_text_missing
- decision: repair_now
- allowed_in_student_core: conditional
- repaired_ask: 阅读材料，完成下表。
- reason: 题面为案例+表格补全，学生入口是按表格列填法律判断
- next_action: 将设问写入修补表；检查表头/空格是否完整

### CC0092_2025_东城_期末_19_1
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: no
- reason: 充电桩方案可能是法律/治理混合题，缺题面前不能进入核心归纳
- next_action: 回源找原试题第19题第1问材料和设问

### CC0131_2025_房山_一模_19
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: conditional
- reason: 知识产权/不正当竞争信号强，但设问可能是意义类，需原题确认防止答案倒推
- next_action: 回源确认材料、设问和评分细则对应关系

### CC0157_2025_朝阳_期末_20
- problem_type: ask_text_missing
- decision: repair_now
- allowed_in_student_core: conditional
- repaired_ask: 了解案件，分析事实，印证法理，参考示例，完成下表。
- reason: 题面直接给出任务句，属于程序/举证/裁判理由表格型
- next_action: 修 ask_text；继续拆列名、示例、空格对应的得分点

### CC0180_2025_海淀_期末_20
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: no
- reason: 产品责任/无过错责任信号明确，但缺题面，不能只用答案生成学生示范
- next_action: 回源确认原题是否为主观题以及具体设问

### CC0189_2025_石景山_一模_20
- problem_type: ask_text_missing
- decision: repair_now
- allowed_in_student_core: conditional
- repaired_ask: 阅读材料，参考示例，完成下表。
- reason: 题面明确案例+示例+表格，适合纳入表格门
- next_action: 修 ask_text；回源补全表格列和每格空白

### CC0195_2025_西城_一模_20
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: conditional
- reason: 劳动集体合同信号强，但不能用答案代替设问
- next_action: 回源找第20题材料、设问、细则，确认劳动关系/集体协商入口

### CC0213_2025_门头沟_一模_20
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: conditional
- repaired_ask: 请结合以下案例，参照所给示例完成下表。
- reason: 虽然能看出表格设问，但之前检索提示该题答案/细则块可能错位，需回源核对
- next_action: 回源确认案例、表头、示例和 rubric 是否同一题

### CC0214_2025_门头沟_一模_20_2
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: no
- reason: 可能应作为 CC0213 的子问/细则拆分，不应独立成一张污染题卡
- next_action: 回源后决定并入 CC0213、拆分为子问，或保留为细则原子

### CC0245_2026_东城_期末_18_2
- problem_type: ask_text_missing
- decision: repair_now
- allowed_in_student_core: conditional
- repaired_ask: 维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？
- reason: 这是 CC0244 的维权策略子问，应作为同题子问处理
- next_action: 修 ask_text，并与 CC0244 合并为同题双问运行

### CC0276_2026_房山_二模_17
- problem_type: ask_text_missing
- decision: downgrade_insurance_box
- allowed_in_student_core: no
- reason: 更像必修三/综合法治价值，不适合支撑法律主观题核心框架
- next_action: 进入保险箱或待确认，不推动核心节点

### CC0277_2026_房山_二模_18
- problem_type: ask_text_missing
- decision: split_subquestion_only
- allowed_in_student_core: conditional
- repaired_ask: 18（1）法律边界及应对措施。
- reason: 只保留法律小问进入选必二，非法律部分移出，不整题吞入
- next_action: 只以 18(1) 修补；其余小问不进法律宝典核心

### CC0317_2026_海淀_期末_18
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: no
- reason: 住房租赁格式条款信号强，但题卡需回源，避免答案倒推题面
- next_action: 回源确认合同条款材料、设问与细则

### CC0318_2026_海淀_期末_18_2
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: no
- reason: 可能是 CC0317 子问，不应独立污染核心结构
- next_action: 回源后并入第18题或保留为子问

### CC0319_2026_海淀_期末_19
- problem_type: ask_text_missing
- decision: source_confirm_required
- allowed_in_student_core: no
- reason: 反不正当竞争信号强，但缺题面，不得直接写逐题满分示范
- next_action: 回源确认原题材料、设问、细则

### CC0325_2026_石景山_一模_18
- problem_type: ask_text_missing
- decision: repair_now
- allowed_in_student_core: conditional
- repaired_ask: 阅读材料，参考示例，分析案件中举证责任的分配方式及理由，完成下表。
- reason: 题面明确表格任务，是程序/举证责任门核心样题；但需补真实空格
- next_action: 修 ask_text；回源补全表格空白和列名

### CC0353_2026_西城_期末_17
- problem_type: ask_text_missing_reference_only
- decision: reference_only_lock
- allowed_in_student_core: no
- reason: 只可练表达或作低强度旁证，不能支撑核心框架或满分闭环
- next_action: 锁定为 reference_only 保险箱，不进核心证据

### CC0223_2025_顺义_一模_19
- problem_type: high_risk_source_card
- decision: clean_source_card_before_core
- allowed_in_student_core: conditional
- repaired_ask: 运用《法律与生活》知识，分析上述案例是如何解决纠纷的。案例1：案例2：
- reason: 可用 F0098/F0314 清洁题面与 F0097 细则，但必须剔除答案化材料原子
- next_action: 生成清洁题卡；价值问若未锁原设问则进保险箱

### CC0150_2025_朝阳_二模_20
- problem_type: high_risk_rubric_contamination
- decision: clean_rubric_atoms_before_core
- allowed_in_student_core: yes_after_cleaning
- repaired_ask: （1）结合材料，运用《法律与生活》知识，分析上述案例。（2）假如你是人民调解员，提出解决上述纠纷的建议。
- reason: 隐私权/相邻关系题可作核心，但必须硬切掉 Q21 周边工作/人类命运共同体原子
- next_action: 清理 rubric atoms 与句库，不让 Q21 进入法律答案

### CC0244_2026_东城_期末_18
- problem_type: high_risk_oversized_atom
- decision: split_atoms_before_core
- allowed_in_student_core: yes_after_cleaning
- repaired_ask: （1）运用《法律与生活》知识，分析本案涉及的法律责任及法律依据。（2）维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？
- reason: 这是 V7 三责任链和三归责档核心题，但必须拆为合同链、侵权链、维权准备链
- next_action: 拆细则原子并更新教师证据说明；学生稿保留责任链写法

## Gate Decision

V7.1 may continue as a candidate draft and source-repair lane, but must not be called final. Rows marked `repair_now`, `clean_*`, or `split_*` can be patched into a teacher/evidence draft. Rows marked `source_confirm_required`, `downgrade_insurance_box`, or `reference_only_lock` cannot support core full-score closure until source confirmation changes the status.
