# V7.1 Teacher Evidence Patch

- generated_at: 2026-05-21T09:29:12
- scope: rows that can be used in a V7.1 teacher/evidence draft after source-card guardrails. This file does not patch canonical CSVs by itself.
- hard gate: source_confirm_required rows are excluded from this patch.

## Patch Rows

### V7P01｜CC0077_2025_东城_一模_19
- patch_type: ask_text_patch
- student_core_policy: conditional_after_table_or_subquestion_check
- patched_ask_text: 阅读材料，完成下表。
- teacher_evidence_note: 补入真实/题面可见设问：阅读材料，完成下表。。仍需按原题表头或空格做逐格核对。
- next_verification: 将设问写入修补表；后续按表格列名回源补齐空格

### V7P02｜CC0084_2025_东城_二模_19
- patch_type: ask_text_patch
- student_core_policy: conditional_after_table_or_subquestion_check
- patched_ask_text: 阅读材料，完成下表。
- teacher_evidence_note: 补入真实/题面可见设问：阅读材料，完成下表。。仍需按原题表头或空格做逐格核对。
- next_verification: 将设问写入修补表；检查表头/空格是否完整

### V7P03｜CC0157_2025_朝阳_期末_20
- patch_type: ask_text_patch
- student_core_policy: conditional_after_table_or_subquestion_check
- patched_ask_text: 了解案件，分析事实，印证法理，参考示例，完成下表。
- teacher_evidence_note: 补入真实/题面可见设问：了解案件，分析事实，印证法理，参考示例，完成下表。。仍需按原题表头或空格做逐格核对。
- next_verification: 修 ask_text；继续拆列名、示例、空格对应的得分点

### V7P04｜CC0189_2025_石景山_一模_20
- patch_type: ask_text_patch
- student_core_policy: conditional_after_table_or_subquestion_check
- patched_ask_text: 阅读材料，参考示例，完成下表。
- teacher_evidence_note: 补入真实/题面可见设问：阅读材料，参考示例，完成下表。。仍需按原题表头或空格做逐格核对。
- next_verification: 修 ask_text；回源补全表格列和每格空白

### V7P05｜CC0245_2026_东城_期末_18_2
- patch_type: ask_text_patch
- student_core_policy: conditional_after_table_or_subquestion_check
- patched_ask_text: 维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？
- teacher_evidence_note: 补入真实/题面可见设问：维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？。仍需按原题表头或空格做逐格核对。
- next_verification: 修 ask_text，并与 CC0244 合并为同题双问运行

### V7P06｜CC0277_2026_房山_二模_18
- patch_type: legal_subquestion_split_patch
- student_core_policy: conditional_law_subquestion_only
- patched_ask_text: 18（1）法律边界及应对措施。
- teacher_evidence_note: 只保留法律小问进入选必二；其他模块小问不得进入法律主干或满分句库。
- next_verification: 只以 18(1) 修补；其余小问不进法律宝典核心

### V7P07｜CC0325_2026_石景山_一模_18
- patch_type: ask_text_patch
- student_core_policy: conditional_after_table_or_subquestion_check
- patched_ask_text: 阅读材料，参考示例，分析案件中举证责任的分配方式及理由，完成下表。
- teacher_evidence_note: 补入真实/题面可见设问：阅读材料，参考示例，分析案件中举证责任的分配方式及理由，完成下表。。仍需按原题表头或空格做逐格核对。
- next_verification: 修 ask_text；回源补全表格空白和列名

### V7P08｜CC0223_2025_顺义_一模_19
- patch_type: clean_material_and_ask_patch
- student_core_policy: conditional_after_clean_card
- patched_ask_text: 运用《法律与生活》知识，分析上述案例是如何解决纠纷的。案例1：案例2：
- teacher_evidence_note: 使用 V7 cleaned source-card preview 的干净材料原子和设问；剔除答案化价值句作为材料事实。
- next_verification: 生成清洁题卡；价值问若未锁原设问则进保险箱

### V7P09｜CC0150_2025_朝阳_二模_20
- patch_type: rubric_contamination_exclusion_patch
- student_core_policy: yes_after_cleaning
- patched_ask_text: （1）结合材料，运用《法律与生活》知识，分析上述案例。（2）假如你是人民调解员，提出解决上述纠纷的建议。
- teacher_evidence_note: 保留 Q20 隐私权/相邻关系/建议措施细则；硬切 Q21 周边工作、人类命运共同体等选必一内容。
- next_verification: 清理 rubric atoms 与句库，不让 Q21 进入法律答案

### V7P10｜CC0244_2026_东城_期末_18
- patch_type: rubric_atom_resplit_patch
- student_core_policy: yes_after_cleaning
- patched_ask_text: （1）运用《法律与生活》知识，分析本案涉及的法律责任及法律依据。（2）维权成功需要做好充分准备和策略选择。你认为陈某需要做好哪些工作？
- teacher_evidence_note: 拆成合同链、销售者一般过错侵权链、生产者产品责任/无过错链、维权准备链和错误责任警告。
- next_verification: 拆细则原子并更新教师证据说明；学生稿保留责任链写法

## Exclusion Rule

The following row types remain outside this patch: `source_confirm_required`, `downgrade_insurance_box`, `reference_only_lock`. They may appear in a teacher risk appendix, but not as core full-score evidence.
