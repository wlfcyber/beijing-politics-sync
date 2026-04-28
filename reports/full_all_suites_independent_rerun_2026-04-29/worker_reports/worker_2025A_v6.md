# worker-2025A v6 报告

处理范围：SUITE_ROSTER.csv 中 year=2025 且 assigned_role=worker-2025A 的 16 套；不处理二模。

## 完成情况

- 处理套数：16
- 学生版条目数：46
- 审计 CSV 行数：52（不含表头）
- 客观题全处理套数：16
- 写入文件：
  - worker_outputs/2025A_v6_student_entries.md
  - worker_outputs/2025A_v6_audit_entries.csv
  - worker_outputs/2025A_v6_choice_review.md
  - worker_reports/worker_2025A_v6.md

## 证据口径

- 全部先读 SUITE_ROSTER.csv 的 bundle_path；本次 16 套均为 suite-bundle。
- 旧 worker_outputs/2025A_notes.md 仅作为定位线索，未作为 evidence_excerpt 或结论来源。
- 学生版不放路径、行号、OCR、source id；证据和状态只放审计 CSV。
- 高风险词只在细则或答案原文支撑时写入；否则降级为错肢、边界或阻塞。

## 补丁者预警处理

- 2025顺义一模16：学生版只写细则支撑的“双创、联系、发展”；未把“辩证否定/守正创新”写成评分细则明确要求。
- 2025石景山一模21：只做风险复核，不把设问词“破立”反推为辩证否定。
- 2025朝阳一模16：当前可见参考答案只给宽泛知识方向，未形成可细化的正式评分细则，审计 CSV 标 NEED_EVIDENCE，未进入学生版。

## 阻塞项

- S019 2025朝阳一模 第16题：NEED_EVIDENCE，需补清晰正式细则或阅卷截图后再入学生版。
- S022 2025房山一模 第16题：reference-only，答案明示“原卷无答案，本答案仅供参考”，不能作正式触发链。
- S037 2025丰台期末 第16题：reference-only，教师版示例明示“原题无答案，此答案仅供参考”，不能作正式触发链。
- S032 2025海淀期中：主观核心题为经济/国政经方向，按模块边界排除出学生版；客观题已全处理。