# v3 全来源复核汇总

## 范围

- 框架触发条目：496
- 框架不同来源键：310
- 错肢库来源行：1583
- 旧题源清单套卷行：56

## 框架条目最终证据等级

- A: 126
- B: 143
- C: 186
- D: 12
- E: 29

## 框架条目最终状态

- A_scoring_source_trigger_not_text_matched: 44
- A_verified_scoring_source: 82
- B_angle_or_scoring_source: 143
- C_verified_by_worker_report: 6
- C_verified_choice_source: 180
- D_reference_only: 12
- E_choice_key_or_stem_not_confirmed: 17
- E_ocr_needed_or_unsynced_render: 6
- E_user_supplement_not_in_workspace: 6

## 错肢库来源状态

- C_verified_choice_source: 1434
- C_worker_report_source: 23
- E_choice_key_not_detected: 126

## 题源清单 v3 判定

- closed-with-angle-boundary: 23
- closed-with-reference-boundary: 3
- confirmed-excluded: 2
- old-closed-needs-boundary-or-evidence: 8
- source-reviewed: 20

## 需降级/补证/边界标注的框架条目前 120 条

| audit_id | final_grade | final_status | recommended_action | source | support_path | support_note | support_trigger_hits |
|---|---|---|---|---|---|---|---|
| V3-FW-0002 | E | E_user_supplement_not_in_workspace | needs-user-supplement-or-downgrade | 2026北京西城高三（上）期末 第16题第（2）问（用户补充评分页截图） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026西城期末.md | 2026各区期末和期中\2026西城期末\其他材料\西城高三期末评标.pptx |  |
| V3-FW-0003 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京朝阳高三二模 第16题（2）（2024年朝阳二模主观题阅卷总结.pdf） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024朝阳二模.md | 2024各区二模\2024朝阳二模\细则\2024朝阳二模细则.pdf |  |
| V3-FW-0004 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx | 一切从实际出发 |
| V3-FW-0005 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 一切从实际出发;实事求是 |
| V3-FW-0013 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京西城高三（上）期末 第21题（西城高三期末评标.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026西城期末.md | 2026各区期末和期中\2026西城期末\其他材料\西城高三期末评标.pptx | 实事求是 |
| V3-FW-0016 | E | E_ocr_needed_or_unsynced_render | needs-ocr-before-formal-use | 2026北京朝阳高三（上）期末 第16题（2026朝阳期末细则.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | 2026各区期末和期中\2026朝阳期末\细则\2026朝阳期末细则.pdf |  |
| V3-FW-0018 | E | E_user_supplement_not_in_workspace | needs-user-supplement-or-downgrade | 2025北京朝阳高三一模 第16题（用户补充评分截图） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区一模__2025朝阳一模.md | 2025各区一模\2025朝阳一模\其他材料\20250329高3阅卷总结17 1题 具身智能 任会波组 阐释论证.doc |  |
| V3-FW-0019 | E | E_choice_key_or_stem_not_confirmed | needs-choice-answer-key | 2026北京朝阳高三（上）期末 第4题 | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | answer-key-not-detected |  |
| V3-FW-0021 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2025北京东城高三二模 第16题 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025东城二模.md | 2025各区二模\2025东城二模\细则\2025东城二模细则.pdf |  |
| V3-FW-0024 | E | E_user_supplement_not_in_workspace | needs-user-supplement-or-downgrade | 2025北京东城高三（上）期末 第16题（用户补充讲评PDF答案细则） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025东城期末.md | 2025各区期末\2025东城期末\其他材料\2025。1东城讲评 修改.pdf | 主观能动性 |
| V3-FW-0025 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京海淀高三（上）期末 第16题（用户确认PPT给分口径） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025海淀期末.md | 2025各区期末\2025海淀期末\细则\2025海淀期末细则.pptx | 主观能动性 |
| V3-FW-0026 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx | 主观能动性;意识的能动作用 |
| V3-FW-0033 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2025北京东城高三二模 第16题 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025东城二模.md | 2025各区二模\2025东城二模\细则\2025东城二模细则.pdf |  |
| V3-FW-0034 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0036 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京朝阳高三二模 第16题（2）（2024年朝阳二模主观题阅卷总结.pdf） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024朝阳二模.md | 2024各区二模\2024朝阳二模\细则\2024朝阳二模细则.pdf |  |
| V3-FW-0037 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三二模 第16题第（1）问（讨论定稿-答案细则 -25.5西城高三政治二模-1.docx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025西城二模.md | 2025各区二模\2025西城二模\细则\2025西城二模细则.docx |  |
| V3-FW-0038 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京东城高三二模 第16题（阅卷总结/16题/16题二模阅卷总结.docx、16题评分细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024东城二模.md | 2024各区二模\2024东城二模\细则\2024东城二模细则\16题\16题二模阅卷总结.docx |  |
| V3-FW-0040 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京朝阳高三期中 第17题（2024.11期中政治朝阳评标docx.docx、阅卷细则总.rtf） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区期中__2024朝阳期中.md | 2024各区期中\2024朝阳期中\其他材料\2024.11期中政治朝阳评标2.docx |  |
| V3-FW-0041 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx |  |
| V3-FW-0042 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0043 | E | E_ocr_needed_or_unsynced_render | needs-ocr-before-formal-use | 2026北京朝阳高三（上）期末 第16题（2026朝阳期末细则.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | 2026各区期末和期中\2026朝阳期末\细则\2026朝阳期末细则.pdf |  |
| V3-FW-0044 | E | E_ocr_needed_or_unsynced_render | needs-ocr-before-formal-use | 2026北京朝阳高三（上）期末 第16题（正式细则PDF页图人工核定） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | 2026各区期末和期中\2026朝阳期末\细则\2026朝阳期末细则.pdf |  |
| V3-FW-0045 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2025北京顺义高三一模 第16题（教师版 + 评分细则） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区一模__2025顺义一模.md | 2025各区一模\2025顺义一模\细则\2025顺义一模细则.docx |  |
| V3-FW-0048 | E | E_user_supplement_not_in_workspace | needs-user-supplement-or-downgrade | 2025北京东城高三（上）期末 第16题（用户补充讲评PDF答案细则） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025东城期末.md | 2025各区期末\2025东城期末\其他材料\2025。1东城讲评 修改.pdf |  |
| V3-FW-0049 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京海淀高三（上）期末 第16题（用户确认PPT给分口径） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025海淀期末.md | 2025各区期末\2025海淀期末\细则\2025海淀期末细则.pptx | 联系的观点 |
| V3-FW-0051 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 联系的观点 |
| V3-FW-0052 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 联系的观点 |
| V3-FW-0062 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京丰台高三二模 第20题（丰台政治二模阅卷评标.docx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024丰台二模.md | 2024各区二模\2024丰台二模\细则\2024丰台二模细则.docx |  |
| V3-FW-0064 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三二模 第16题第（1）问 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025西城二模.md | 2025各区二模\2025西城二模\细则\2025西城二模细则.docx |  |
| V3-FW-0065 | E | E_choice_key_or_stem_not_confirmed | needs-choice-answer-key | 2025北京海淀高三二模 第9题 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025海淀二模.md | answer-key-not-detected |  |
| V3-FW-0071 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx | 系统观念 |
| V3-FW-0072 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 系统观念 |
| V3-FW-0077 | E | E_choice_key_or_stem_not_confirmed | needs-choice-answer-key | 2026北京朝阳高三（上）期末 第2题 | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | answer-key-not-detected |  |
| V3-FW-0081 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2025北京东城高三二模 第16题 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025东城二模.md | 2025各区二模\2025东城二模\细则\2025东城二模细则.pdf |  |
| V3-FW-0082 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三二模 第16题第（1）问 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025西城二模.md | 2025各区二模\2025西城二模\细则\2025西城二模细则.docx |  |
| V3-FW-0083 | E | E_user_supplement_not_in_workspace | needs-user-supplement-or-downgrade | 2025北京东城高三（上）期末 第16题（用户补充讲评PDF答案细则） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025东城期末.md | 2025各区期末\2025东城期末\其他材料\2025。1东城讲评 修改.pdf |  |
| V3-FW-0084 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京海淀高三（上）期末 第16题（用户确认PPT给分口径） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025海淀期末.md | 2025各区期末\2025海淀期末\细则\2025海淀期末细则.pptx | 发展的观点 |
| V3-FW-0085 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三（上）期末 第18题（用户确认答案解析可用） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025西城期末.md | 2025各区期末\2025西城期末\细则\2025西城期末细则.pdf | 新事物发展 |
| V3-FW-0086 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 发展的观点 |
| V3-FW-0087 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 发展的观点 |
| V3-FW-0090 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京西城高三（上）期末 第21题（西城高三期末评标.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026西城期末.md | 2026各区期末和期中\2026西城期末\其他材料\西城高三期末评标.pptx | 发展的观点 |
| V3-FW-0092 | E | E_ocr_needed_or_unsynced_render | needs-ocr-before-formal-use | 2026北京朝阳高三（上）期末 第16题（2026朝阳期末细则.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | 2026各区期末和期中\2026朝阳期末\细则\2026朝阳期末细则.pdf |  |
| V3-FW-0095 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京海淀高三（上）期末 第17题（2）（用户确认PPT给分口径） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025海淀期末.md | 2025各区期末\2025海淀期末\细则\2025海淀期末细则.pptx |  |
| V3-FW-0096 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx | 适度原则 |
| V3-FW-0100 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京丰台高三二模 第21题（丰台政治二模阅卷评标.docx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024丰台二模.md | 2024各区二模\2024丰台二模\细则\2024丰台二模细则.docx |  |
| V3-FW-0101 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京海淀高三（上）期末 第17题（2）（用户确认PPT给分口径） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025海淀期末.md | 2025各区期末\2025海淀期末\细则\2025海淀期末细则.pptx |  |
| V3-FW-0102 | E | E_ocr_needed_or_unsynced_render | needs-ocr-before-formal-use | 2026北京朝阳高三（上）期末 第16题（2026朝阳期末细则.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | 2026各区期末和期中\2026朝阳期末\细则\2026朝阳期末细则.pdf |  |
| V3-FW-0104 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京海淀高三（上）期末 第16题（用户确认PPT给分口径） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025海淀期末.md | 2025各区期末\2025海淀期末\细则\2025海淀期末细则.pptx | 辩证否定 |
| V3-FW-0105 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0106 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 守正创新 |
| V3-FW-0118 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2026北京海淀高三（上）期末 第16题（评分标准） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026海淀期末.md | 2026各区期末和期中\2026海淀期末\细则\2026海淀期末细则.pdf |  |
| V3-FW-0119 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三（上）期末 第18题（用户确认答案解析可用） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025西城期末.md | 2025各区期末\2025西城期末\细则\2025西城期末细则.pdf | 矛盾就是对立统一 |
| V3-FW-0120 | E | E_choice_key_or_stem_not_confirmed | needs-choice-answer-key | 2025北京海淀高三二模 第12题 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025海淀二模.md | answer-key-not-detected |  |
| V3-FW-0123 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京西城高三（上）期末 第16题第（2）问（西城高三期末评标.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026西城期末.md | 2026各区期末和期中\2026西城期末\其他材料\西城高三期末评标.pptx |  |
| V3-FW-0124 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京延庆高三一模 第16题（教师版 + 答案细则合并文件） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区一模__2025延庆一模.md | 2025各区一模\2025延庆一模\细则\2025延庆一模细则.docx |  |
| V3-FW-0125 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京房山高三一模 第16题第（1）问（教师版 + 参考答案细则） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区一模__2025房山一模.md | 2025各区一模\2025房山一模\细则\2025房山一模细则.pdf |  |
| V3-FW-0126 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2025北京海淀高三一模 第16题（教师版 + 评分标准） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区一模__2025海淀一模.md | 2025各区一模\2025海淀一模\细则\2025海淀一模细则.docx |  |
| V3-FW-0127 | E | E_user_supplement_not_in_workspace | needs-user-supplement-or-downgrade | 2026北京东城高三（上）期末 第16题（用户补充评分页截图） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026东城期末.md | 2026各区期末和期中\2026东城期末\细则\2026东城期末细则.pptx |  |
| V3-FW-0129 | E | E_ocr_needed_or_unsynced_render | needs-ocr-before-formal-use | 2026北京朝阳高三（上）期末 第16题（2026朝阳期末细则.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | 2026各区期末和期中\2026朝阳期末\细则\2026朝阳期末细则.pdf |  |
| V3-FW-0130 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京丰台高三二模 第20题（丰台政治二模阅卷评标.docx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024丰台二模.md | 2024各区二模\2024丰台二模\细则\2024丰台二模细则.docx |  |
| V3-FW-0131 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京朝阳高三期中 第17题（2024.11期中政治朝阳评标docx.docx、阅卷细则总.rtf） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区期中__2024朝阳期中.md | 2024各区期中\2024朝阳期中\其他材料\2024.11期中政治朝阳评标2.docx |  |
| V3-FW-0132 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三（上）期末 第18题（用户确认答案解析可用） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025西城期末.md | 2025各区期末\2025西城期末\细则\2025西城期末细则.pdf | 承认矛盾 |
| V3-FW-0134 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx | 矛盾的特殊性 |
| V3-FW-0135 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 具体问题具体分析 |
| V3-FW-0138 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三二模 第16题第（1）问（讨论定稿-答案细则 -25.5西城高三政治二模-1.docx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025西城二模.md | 2025各区二模\2025西城二模\细则\2025西城二模细则.docx | 矛盾的特殊性;具体问题具体分析 |
| V3-FW-0140 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京西城高三二模 第18题第（4）问（高三模拟测试思想政治答案细则.docx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024西城二模.md | 2024各区二模\2024西城二模\细则\2024西城二模细则.docx |  |
| V3-FW-0142 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三二模 第16题第（3）问 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025西城二模.md | 2025各区二模\2025西城二模\细则\2025西城二模细则.docx | 具体问题具体分析 |
| V3-FW-0144 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2025北京石景山高三一模 第16题（教师版 + 评分细则） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区一模__2025石景山一模.md | 2025各区一模\2025石景山一模\细则\2025石景山一模细则.doc |  |
| V3-FW-0146 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0148 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2024北京朝阳高三一模 第16题（2024朝阳一模政治评标.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区一模__2024朝阳一模.md | 2024各区一模\2024朝阳一模\其他材料\202404朝阳高三政治一模试卷讲评.pptx |  |
| V3-FW-0149 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京顺义高三一模 第21题（2026年顺义一模 细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区一模__2026顺义一模.md | 2026各区一模\2026顺义一模\细则\2026顺义一模细则.pptx | 内外因 |
| V3-FW-0150 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx | 实践与认识 |
| V3-FW-0151 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0153 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2026北京朝阳高三（上）期中 第18题（用户提供正式阅卷细则） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期中.md | 2026各区期末和期中\2026朝阳期中\其他材料\2025.11朝阳期中政治评标.docx |  |
| V3-FW-0154 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三一模 第16题（教师版 + 细则） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区一模__2025西城一模.md | 2025各区一模\2025西城一模\细则\2025西城一模细则.docx |  |
| V3-FW-0156 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京海淀高三（上）期末 第17题（2）（用户确认PPT给分口径） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025海淀期末.md | 2025各区期末\2025海淀期末\细则\2025海淀期末细则.pptx | 实践是认识的基础;实践是认识发展的动力;实践是检验认识真理性的唯一标准 |
| V3-FW-0159 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx |  |
| V3-FW-0161 | E | E_choice_key_or_stem_not_confirmed | needs-choice-answer-key | 2025北京海淀高三二模 第10题 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025海淀二模.md | answer-key-not-detected |  |
| V3-FW-0166 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京海淀高三（上）期末 第17题（2）（用户确认PPT给分口径） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025海淀期末.md | 2025各区期末\2025海淀期末\细则\2025海淀期末细则.pptx | 无限性;上升性 |
| V3-FW-0167 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三（上）期末 第18题（用户确认答案解析可用） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025西城期末.md | 2025各区期末\2025西城期末\细则\2025西城期末细则.pdf |  |
| V3-FW-0169 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0175 | E | E_choice_key_or_stem_not_confirmed | needs-choice-answer-key | 2026北京朝阳高三（上）期末 第3题 | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026朝阳期末.md | answer-key-not-detected |  |
| V3-FW-0176 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京丰台高三二模 第20题（丰台政治二模阅卷评标.docx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024丰台二模.md | 2024各区二模\2024丰台二模\细则\2024丰台二模细则.docx |  |
| V3-FW-0178 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx | 认识对实践的反作用 |
| V3-FW-0179 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0180 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0182 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京西城高三（上）期末 第16题第（2）问（西城高三期末评标.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026西城期末.md | 2026各区期末和期中\2026西城期末\其他材料\西城高三期末评标.pptx | 追求真理 |
| V3-FW-0183 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0186 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京东城高三一模 第20题（东城一模评标细则（勿传）/20.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区一模__2026东城一模.md | 2026各区一模\2026东城一模\细则\2026东城一模细则\20.pptx |  |
| V3-FW-0190 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2024北京东城高三一模 第18题第（1）问（2024东城一模政治评标1.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区一模__2024东城一模.md | 2024各区一模\2024东城一模\细则\2024东城一模细则.pptx | 改革 |
| V3-FW-0191 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京西城高三二模 第17题（高三模拟测试思想政治答案细则.docx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024西城二模.md | 2024各区二模\2024西城二模\细则\2024西城二模细则.docx |  |
| V3-FW-0193 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第17题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx | 人民群众是历史的创造者;群众观点 |
| V3-FW-0194 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 人民群众;群众观点 |
| V3-FW-0195 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx | 人民群众;人民立场 |
| V3-FW-0197 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京东城高三一模 第20题（东城一模评标细则（勿传）/20.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区一模__2026东城一模.md | 2026各区一模\2026东城一模\细则\2026东城一模细则\20.pptx | 人民立场 |
| V3-FW-0198 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京西城高三（上）期末 第16题第（2）问（西城高三期末评标.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026西城期末.md | 2026各区期末和期中\2026西城期末\其他材料\西城高三期末评标.pptx | 群众观点 |
| V3-FW-0202 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2026北京海淀高三（上）期末 第16题（评分标准） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026海淀期末.md | 2026各区期末和期中\2026海淀期末\细则\2026海淀期末细则.pdf |  |
| V3-FW-0203 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三（上）期末 第18题（用户确认答案解析可用） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025西城期末.md | 2025各区期末\2025西城期末\细则\2025西城期末细则.pdf |  |
| V3-FW-0208 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京昌平高三二模 第16题 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025昌平二模.md | 2025各区二模\2025昌平二模\细则\2025昌平二模细则.pptx | 价值观的导向作用 |
| V3-FW-0210 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2025北京丰台高三二模 第16题第（1）问 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025丰台二模.md | 2025各区二模\2025丰台二模\细则\2025丰台二模细则\2025丰台二模评标细则\16.(1).doc |  |
| V3-FW-0211 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京丰台高三（上）期末 第16题（丰台期末细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025丰台期末.md | 2025各区期末\2025丰台期末\细则\2025丰台期末细则.pptx |  |
| V3-FW-0212 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0213 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第22题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0214 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京西城高三（上）期末 第16题第（2）问（西城高三期末评标.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026西城期末.md | 2026各区期末和期中\2026西城期末\其他材料\西城高三期末评标.pptx |  |
| V3-FW-0215 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三二模 第16题第（1）问（讨论定稿-答案细则 -25.5西城高三政治二模-1.docx） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025西城二模.md | 2025各区二模\2025西城二模\细则\2025西城二模细则.docx | 价值观的导向作用;生态价值观 |
| V3-FW-0216 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京东城高三二模 第16题（阅卷总结/16题/16题二模阅卷总结.docx、16题评分细则.pptx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024东城二模.md | 2024各区二模\2024东城二模\细则\2024东城二模细则\16题\16题二模阅卷总结.docx |  |
| V3-FW-0220 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京西城高三（上）期末 第18题（用户确认答案解析可用） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025西城期末.md | 2025各区期末\2025西城期末\细则\2025西城期末细则.pdf |  |
| V3-FW-0221 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京朝阳高三（上）期末 第16题（朝阳期末评标.pdf扫描页读图核定） | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区期末__2025朝阳期末.md | 2025各区期末\2025朝阳期末\其他材料\朝阳高三期末2025.pptx |  |
| V3-FW-0222 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2026北京海淀高三（上）期末 第16题（2025-2026海淀期末政治评分标准(1).pdf） | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区期末和期中__2026海淀期末.md | 2026各区期末和期中\2026海淀期末\细则\2026海淀期末细则.pdf |  |
| V3-FW-0223 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京西城高三二模 第18题第（4）问（高三模拟测试思想政治答案细则.docx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024西城二模.md | 2024各区二模\2024西城二模\细则\2024西城二模细则.docx |  |
| V3-FW-0224 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京朝阳高三期中 第17题（2024.11期中政治朝阳评标docx.docx、阅卷细则总.rtf） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区期中__2024朝阳期中.md | 2024各区期中\2024朝阳期中\其他材料\2024.11期中政治朝阳评标2.docx |  |
| V3-FW-0225 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2025北京昌平高三二模 第16题 | data/preprocessed_corpus/gpt_suite_bundles/2025各区模拟题__2025各区二模__2025昌平二模.md | 2025各区二模\2025昌平二模\细则\2025昌平二模细则.pptx | 实现人生价值 |
| V3-FW-0230 | A | A_scoring_source_trigger_not_text_matched | keep-source-but-chain-needs-human-check | 2024北京丰台高三二模 第21题（丰台政治二模阅卷评标.docx） | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024丰台二模.md | 2024各区二模\2024丰台二模\细则\2024丰台二模细则.docx |  |
| V3-FW-0241 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2024北京顺义高三二模 第20（2）题 | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024顺义思政二模.md | 2024各区二模\2024顺义思政二模\细则\2024顺义思政二模细则.docx | 一切从实际出发 |
| V3-FW-0242 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京东城高三一模 第16题 | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区一模__2026东城一模.md | 2026各区一模\2026东城一模\细则\2026东城一模细则\16.pptx | 人民群众;矛盾主次方面;系统观点 |
| V3-FW-0243 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2024北京顺义高三二模 第16（1）题 | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024顺义思政二模.md | 2024各区二模\2024顺义思政二模\细则\2024顺义思政二模细则.docx |  |
| V3-FW-0244 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2024北京顺义高三二模 第16（1）题 | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024顺义思政二模.md | 2024各区二模\2024顺义思政二模\细则\2024顺义思政二模细则.docx |  |
| V3-FW-0245 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2024北京顺义高三二模 第16（1）题 | data/preprocessed_corpus/gpt_suite_bundles/2024各区模拟题__2024各区二模__2024顺义思政二模.md | 2024各区二模\2024顺义思政二模\细则\2024顺义思政二模细则.docx |  |
| V3-FW-0246 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京东城高三一模 第20题 | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区一模__2026东城一模.md | 2026各区一模\2026东城一模\细则\2026东城一模细则\20.pptx | 实践决定认识;认识反作用于实践;认识上升性;发展观;人民立场;上层建筑反作用经济基础 |
| V3-FW-0248 | B | B_angle_or_scoring_source | keep-as-angle-list-or-organizer-chain | 2026北京丰台高三一模 第16题 | data/preprocessed_corpus/gpt_suite_bundles/2026各区模拟题__2026各区一模__2026丰台一模.md | 2026各区一模\2026丰台一模\细则\2026丰台一模细则.pptx | 两点论与重点论;系统观念;辩证否定 |

## 需改写闭环口径的题源清单行

| year | district | stage | old_closed_state | v3_suite_verdict | recommended_action | framework_statuses | wrong_option_statuses |
|---|---|---|---|---|---|---|---|
| 2024 | 东城 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:9;C_verified_choice_source:4 | C_verified_choice_source:34 |
| 2024 | 朝阳 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:8;C_verified_choice_source:7 | C_verified_choice_source:35 |
| 2024 | 门头沟 | 一模 | 已闭环 | closed-with-reference-boundary | downgrade-closed-wording | C_verified_by_worker_report:6 | C_worker_report_source:23 |
| 2024 | 海淀 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:4;C_verified_choice_source:5 | C_verified_choice_source:35 |
| 2024 | 丰台 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:8;C_verified_choice_source:4 | C_verified_choice_source:35 |
| 2024 | 石景山 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:7;C_verified_choice_source:4 | C_verified_choice_source:26 |
| 2024 | 海淀 | 期中 | 明确排除 | confirmed-excluded | keep-exclusion |  |  |
| 2024 | 海淀 | 二模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:6;C_verified_choice_source:5 | C_verified_choice_source:36 |
| 2024 | 顺义 | 二模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:4;C_verified_choice_source:4 | C_verified_choice_source:35 |
| 2025 | 延庆 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:1;C_verified_choice_source:2 | C_verified_choice_source:31 |
| 2025 | 房山 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:1;C_verified_choice_source:5 | C_verified_choice_source:37 |
| 2025 | 朝阳 | 一模 | 已闭环 | old-closed-needs-boundary-or-evidence | do-not-call-unqualified-closed | C_verified_choice_source:3;E_user_supplement_not_in_workspace:1 | C_verified_choice_source:30 |
| 2025 | 西城 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:1;C_verified_choice_source:3 | C_verified_choice_source:33 |
| 2025 | 昌平 | 二模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:2;C_verified_choice_source:6 | C_verified_choice_source:7 |
| 2025 | 海淀 | 二模 | 已闭环 | old-closed-needs-boundary-or-evidence | do-not-call-unqualified-closed | A_verified_scoring_source:4;E_choice_key_or_stem_not_confirmed:3 | E_choice_key_not_detected:28 |
| 2025 | 西城 | 二模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:6;C_verified_choice_source:3 | C_verified_choice_source:6 |
| 2025 | 东城 | 期末 | 已闭环 | old-closed-needs-boundary-or-evidence | do-not-call-unqualified-closed | A_scoring_source_trigger_not_text_matched:2;A_verified_scoring_source:2;C_verified_choice_source:2;E_user_supplement_not_in_workspace:3 | C_verified_choice_source:29 |
| 2025 | 丰台 | 期末 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:11;C_verified_choice_source:2 | C_verified_choice_source:31 |
| 2025 | 朝阳 | 期末 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:22;C_verified_choice_source:3 | C_verified_choice_source:34 |
| 2025 | 海淀 | 期中 | 明确排除 | confirmed-excluded | keep-exclusion |  |  |
| 2025 | 海淀 | 期末 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:10;C_verified_choice_source:5 | C_verified_choice_source:33 |
| 2025 | 西城 | 期末 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:9;C_verified_choice_source:3 | C_verified_choice_source:29 |
| 2026 | 东城 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:4;C_verified_choice_source:3 | C_verified_choice_source:11 |
| 2026 | 丰台 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:1;C_verified_choice_source:3 | C_verified_choice_source:30 |
| 2026 | 房山 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:2;C_verified_choice_source:3 | C_verified_choice_source:34 |
| 2026 | 石景山 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:1;C_verified_choice_source:3 | C_verified_choice_source:27 |
| 2026 | 西城 | 一模 | 已闭环 | old-closed-needs-boundary-or-evidence | do-not-call-unqualified-closed | A_verified_scoring_source:2;E_choice_key_or_stem_not_confirmed:4 | E_choice_key_not_detected:34 |
| 2026 | 门头沟 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:3;C_verified_choice_source:3 | C_verified_choice_source:29 |
| 2026 | 顺义 | 一模 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:3;C_verified_choice_source:1 | C_verified_choice_source:32 |
| 2026 | 东城 | 期末 | 已闭环 | old-closed-needs-boundary-or-evidence | do-not-call-unqualified-closed | C_verified_choice_source:2;E_user_supplement_not_in_workspace:1 | C_verified_choice_source:35 |
| 2026 | 丰台 | 期末 | 已闭环 | old-closed-needs-boundary-or-evidence | do-not-call-unqualified-closed | B_angle_or_scoring_source:7;E_choice_key_or_stem_not_confirmed:4 | E_choice_key_not_detected:32 |
| 2026 | 朝阳 | 期末 | 已闭环 | old-closed-needs-boundary-or-evidence | do-not-call-unqualified-closed | E_choice_key_or_stem_not_confirmed:6;E_ocr_needed_or_unsynced_render:6 | E_choice_key_not_detected:32 |
| 2026 | 海淀 | 期中 | 已闭环 | closed-with-reference-boundary | downgrade-closed-wording | D_reference_only:4 | C_verified_choice_source:31 |
| 2026 | 石景山 | 期末 | 已闭环 | closed-with-reference-boundary | downgrade-closed-wording | C_verified_choice_source:5;D_reference_only:8 | C_verified_choice_source:34 |
| 2026 | 西城 | 期末 | 已闭环 | old-closed-needs-boundary-or-evidence | do-not-call-unqualified-closed | B_angle_or_scoring_source:6;C_verified_choice_source:3;E_user_supplement_not_in_workspace:1 | C_verified_choice_source:32 |
| 2026 | 通州 | 期末 | 已闭环 | closed-with-angle-boundary | keep-but-mark-B-boundary | B_angle_or_scoring_source:7;C_verified_choice_source:4 | C_verified_choice_source:35 |

## 结论口径

- 本报告完成的是“来源层复核”：每条旧框架来源键、每条错肢库来源行、每个旧题源清单套卷行都已给出 v3 来源状态。
- A/B/C 可作为继续修订草案的输入；D 只能作 reference-only 或方向边界；E 不得进入正式框架，必须补 OCR/补用户截图/补原件后再使用。
- `全来源复核_边界与缺口清单.md` 汇总了需要降级、补证和改写闭环口径的条目；完整逐行结果见同目录 CSV。
- 本报告不直接覆盖正式总框架和错肢库；下一步如要交付 v3 正文，应按本表生成 diffable draft。
