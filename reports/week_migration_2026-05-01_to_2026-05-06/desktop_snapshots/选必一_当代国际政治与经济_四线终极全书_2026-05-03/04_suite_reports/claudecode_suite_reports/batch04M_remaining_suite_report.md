# Batch04M Remaining — ClaudeCode Lane B Suite Report

Run: `选必一_当代国际政治与经济_四线终极全书_2026-05-03`
Date anchor: 2026-05-04
Lane: ClaudeCode B (independent verification)
Coverage: 15 remaining suites — 2026海淀期末, 2024丰台一模/二模, 2024石景山一模, 2024顺义二模, 2025丰台一模/期末, 2025延庆一模, 2025房山一模, 2025昌平二模, 2025石景山一模, 2025顺义一模, 2026丰台期末, 2024模块分类汇编, 2026石景山期末.

## Executive Summary

| Decision class | Suites | Atom yield |
|---|---|---|
| Promotable clean (P0 + per-pt or chain) | 7 (FT24E, FT25E, YQ25Y, FS25Y, SJS25Y, SY25Y; partially CP25E) | 38 atoms |
| Promotable guarded (cap-tier / 缺标签 / fallback) | 3 (FT24Y, FT25Y fallback, CP25E selnec-exclusive) | 11 atoms |
| Reference-only NOT promoted | 2 (SJS24Y Q19(2), SY24E Q19(2)) | 7 boundary fragments |
| Prompt-only blocker | 1 (FT26E Q20 LAC 五大工程) | 0 (placeholder only) |
| Suite-level boundary / excluded | 3 (HD26E, 2024模块分类汇编, SJS26E) | 0 |

**Total promotable atoms (clean + guarded)**: 49 (excluding meta-rubric atoms).
**Total boundary fragments + placeholders**: ~20.

## Per-Suite Decisions

### 1. 2026海淀期末 — boundary suite (no Xuanbiyi)
- Source: `SRC_93d2077755f7` (PDF 细则 1678 chars).
- Verified Q16-21 全部 必修一/二/三/四 + 选必二/三 (matrix/意识/民法典/反不正当竞争/假言推理/超前思维/党的领导).
- User pre-confirmed; lane B independent verification CONFIRMS.
- **Decision**: no atoms; suite excluded from Xuanbiyi matrix.

### 2. 2024丰台一模 Q20 (7 分) — promotable guarded (cap-tier)
- Source: `SRC_04f136a5f8d1` 细则.docx (12944 chars; rubric L96-102).
- Cap-tier scoring: 4 aspect (基础设施/金融创新/平台贸易投资自由化便利化/数字化绿色低碳) + closure (经济全球化合作共赢); 3-of-4 → 6-7 / 2 → 4-5 / 1 → 2-3.
- 5 atoms (aspect bundles + closure) + 1 rubric meta. Tier `P0_scoring_pdf_guarded`.

### 3. 2024丰台二模 Q19 (6 分) — promotable clean
- Source: `SRC_8cabfb2a5c95` 细则.docx (10641 chars; rubric L64-77).
- Clean 3×2pt 做法+效果 双匹配 (负责任大国 / 南南合作 / 区域合作-HMC) + 拓展替代项 (完善全球治理 / 共商共建共享 / 合作共赢) + 显式负向 (经济全球化/国际关系民主化偏离主题扣分).
- 4 atoms + 1 negative atom. Tier `P0_scoring_docx`.

### 4. 2024石景山一模 Q19(2) (8 分) — NOT_PROMOTED
- Source: `SRC_f887d1b620c6` 细则.pptx (29902 chars but is **教研讲座 PPTX**, not 阅卷标准).
- 仅含答案 + 答题模板图，无评分标准说明 / 等级 / 必采点 / 分值切分.
- 3 reference fragments (经济全球化/比较优势/合作共赢) listed as boundary; **NOT promotable** per project rule.
- Recommendation: source hunt for 区阅卷标准 doc/pdf.

### 5. 2024顺义二模 Q19(2) (8 分) — NOT_PROMOTED
- Source: `SRC_0eb74816f25f` 细则.docx (5832 chars - **仅参考答案**, 无评分标准说明 / 分值切分).
- Q18 + Q19(2) 题面均明示《政治与法治》+《当代国际政治与经济》混合.
- Q19(2) 选必一段含 4 术语 (国际竞争实质 / 国家利益 / 世界多极化 / HMC); Q18 选必一 thread 极弱.
- 4 reference fragments listed as boundary; **NOT promotable** per project rule.

### 6. 2025丰台一模 Q20 (8 分) — guarded fallback only
- Source: `SRC_066dbcf5b765` 细则.docx (rubric L106-124).
- 题面双模块《经济与社会》+《当代国际政治与经济》.
- Primary 4×2pt（便利投资/便利贸易/吸引人才/优惠政策）属 经济与社会 主码 → excluded_from_xuanbiyi_main.
- Selnec only via macro fallback (1-3 分): 国内国际两个市场两种资源 + 双循环新发展格局.
- **Hard negative-list** (line 124): 堆积新型国际关系 / HMC / 推动经济全球化发展 → **不给分**. Strong cross-batch guard signal.
- 1 fallback atom + 1 hard negative atom + 4 经济与社会 boundary atoms. Tier `P0_scoring_docx_guarded`.

### 7. 2025丰台期末 Q20 (8 分) — promotable clean
- Source: `SRC_86fc00424d39` 细则.pptx (rubric L281-289).
- 题面明示《当代国际政治与经济》(中非合作论坛战略性共识).
- Clean 8 atoms: 时代主题(1) + 国家间共同利益(1) + 平等互利(1) + 共商共建共享全球治理观(1) + 新型国际关系(1单形/2具体) + 国际关系民主化替代(1) + 中非携手推进现代化(1) + HMC(1).
- Tier `P0_scoring_pptx`.

### 8. 2025延庆一模 Q20(2) (8 分) — promotable clean
- Source: `SRC_4572acf26cdb` 细则.docx (rubric L45-48).
- 题面明示《当代国际政治与经济》(链博会外交部发言人回应).
- Clean 5 atoms: 共同利益+时代主题(2) + 经济全球化五字方向(2) + 多极化+合理关切(2) + HMC(2) + 替代项(国家利益/国际关系/多边主义不重复).
- Tier `P0_scoring_pdf`.

### 9. 2025房山一模 Q18(2) (8 分) — promotable clean (chain logic)
- Source: `SRC_8ee813c0b52e` 细则.pdf (rubric L86-102).
- 题面明示《当代国际政治与经济》(DeepSeek 中国开源战略 → 全球合作新模式).
- Chain rubric: chain1=4 (国际竞争实质 → 高水平对外开放 [可替代国策] → 创新型开放型世界经济 [不可替代] → 经济全球化发展); chain2=3 (和平与发展国际潮流 → 联合国宗旨原则框架 [不可替代] → HMC + 国际交流合作 [可替代义利观] → 全球治理); 逻辑分=1.
- 10 atoms (含 chain anchor + replaceable + irreplaceable + terminal + 逻辑). Tier `P0_scoring_pdf`. **首次出现 chain rubric 结构**, 与 cap-tier / per-pt 并列.

### 10. 2025昌平二模 Q21 (8 分) — guarded admit (无模块标签)
- Source: `SRC_2df7863ec9eb` 细则.pptx (rubric L116-128).
- 题面**未明示**《当代国际政治与经济》或任一模块.
- Rubric 注 (2) 把"国内国际两个市场两种资源 / 加强贸易合作 / 推动经济全球化发展 / 对外开放型经济发展水平" 标记为 cross-material 通用知识点.
- Lane B admit guarded: 4 选必一-exclusive atoms (两个市场两种资源 / 全球经济治理话语权 / 开放包容全球经济格局 / 推动经济全球化发展) + 4 boundary atoms (营商环境 / 现代化产业体系 / 放宽市场准入 / 知识产权免签) - 双码或经济与社会主码.
- Tier `P0_scoring_pptx_guarded`. 待 Codex A 裁定 admit 决议（参 conflicts C5）.

### 11. 2025石景山一模 Q17(2) (8 分) — promotable clean
- Source: `SRC_700c0fe3ebe1` 细则.doc (rubric L28-43).
- 题面明示《当代国际政治与经济》(完善全球治理的"中国主张").
- Clean 4×2pt: 共商共建共享全球治理观+各国共商(2) + 国家平等+国际关系民主化(2) + 普惠包容经济全球化+共同发展繁荣(2) + 真正多边主义+联合国为核心+国际法为基础(2).
- Rubric meta: 采点采意 + 4 点得 8 分 + 其他角度言之成理上限 4.
- Tier `P0_scoring_docx`.

### 12. 2025顺义一模 Q20 (8 分) — promotable clean
- Source: `SRC_6087ed54082b` 细则.docx (rubric L65-69).
- 题面明示《当代国际政治与经济》("小而美"项目促进国际合作).
- Clean 4×2pt: 创新优势(2) + 当地价值(2) + 我国意义(2 - 文明互鉴/义利观/共商共建共享/大国担当/独立自主和平外交/开放型经济多选 1-2) + 世界贡献(2 - HMC/公正合理国际经济秩序中国方案/经济全球化开放包容普惠/国际关系民主化多选 1-2) + 材料分(1).
- Tier `P0_scoring_docx`.

### 13. 2026丰台期末 Q20 (8 分) — prompt_only_blocker
- Source: `SRC_45c50fff4444` 试卷分析 deck (PPTX/PDF, 25899 chars).
- LAC "五大工程" Q20 prompt **YES** — deck p.64 / L406-424.
- LAC Q20 rubric **NO** — deck p.65 起跳到 9 分综合"五年规划"题; 2022 北京卷"四大全球倡议"rubric (p.50-63) 是教学 anchor 不是 LAC rubric.
- Companion paper file `SRC_371641aaa3a7` (107 B - 抽取失败).
- **Decision**: `prompt_only_blocker`; **不入主表**. 9 个候选学科用语 placeholder（联合国为核心+国际法为基础/全球发展倡议/多边贸易体制/全球安全倡议/全球文明倡议/全人类共同价值/新型国际关系/利益汇合点/中拉命运共同体）仅术语层登记.
- Recommendation: source hunt for independent 评分细则.

### 14. 2024模块分类汇编 — source-bundle boundary
- Sources (per `01_source_inventory/SOURCE_INVENTORY.csv`): 7 个聚合 docx (选必1 + 必修1-4 + 选必2/3), 全部 `P3_candidate_paper`.
- 无独立 P0 评分细则; 选必1 包仅是各区一模题面聚合.
- **Decision**: `suite_boundary_no_promotion`. Defer to per-district P0 sources (已在 04A-04L 各批中分别处理).

### 15. 2026石景山期末 — excluded (no P0)
- Sources (per `01_source_inventory/SOURCE_INVENTORY.csv`): 仅 `SRC_7324e07095f8` 路径含 `已放弃/`, 文件名《答案及评分参考.pdf》, tag `P1_candidate_reference_answer`. 无 P0.
- **Decision**: per user rule "fully excluded unless a new formal scoring source is found" → `suite_excluded_per_user_rule`. 无原子，无 fusion 介入.

## Cross-Suite Term Family Frequency

| Term family | Suite count | 主要套件 |
|---|---|---|
| 人类命运共同体 | 6 + (2 reference + 1 negative + 1 prompt-only) | FT24E A3, FT25E A07, YQ25Y A04, FS25Y A07, SJS25Y boundary, SY25Y A4 |
| 共商共建共享(全球治理观/原则) | 5 | FT24E ext, FT25E A04, SJS25Y A01, SY25Y A3 |
| 经济全球化 (各方向变体) | 7 | FT24Y A5 closure, FT24E NEG, YQ25Y A02, FS25Y A04, SJS25Y A03, CP25E A06, SY25Y A4 |
| 和平与发展时代主题 | 4 | FT25E A01, YQ25Y A01, FS25Y A05, SJS25Y 间接 |
| 新型国际关系 | 3 (1 negative + 1 prompt-only) | FT25E A05, FT25Y NEG, FT26E placeholder |
| 国际关系民主化 | 4 | FT25E A05b 替代, SJS25Y A02, SY25Y A4, SY24E reference |
| 联合国/多边主义/国际法 | 3 + (1 prompt-only) | FS25Y A06, SJS25Y A04, FT26E placeholder |
| 国家利益/共同利益 | 4 | FT25E A02, YQ25Y A01, SY24E reference, FT26E placeholder |
| 世界多极化 | 2 | YQ25Y A03, SY24E reference |
| 国际竞争(实质=综合国力) | 2 | FS25Y A01, SY24E reference |
| 高水平对外开放/开放型世界经济 | 3 | FS25Y A02-A03, CP25E (隐含), SY25Y A3 |
| 两个市场两种资源 | 2 | FT25Y FALLBACK, CP25E A01 |
| 中国方案/中国智慧 | 2 | FT24E A2, SY25Y A4 |
| 义利观(正确义利观) | 2 | FS25Y A08 替代, SY25Y A3 |
| 大国担当/负责任大国 | 3 | FT24E A1, YQ25Y A03, SY25Y A3 |
| 独立自主和平外交政策 | 1 | SY25Y A3 |
| 文明互鉴/全人类共同价值 | 2 (1 prompt-only) | SY25Y A3, FT26E placeholder |

## Structural Findings (rubric typology)

Three distinct P0 rubric structures observed in this batch:

1. **Cap-tier**: 4 aspect → score band（FT24Y）.
2. **Per-point**: 1/2 分 独立计分（FT24E, FT25E, SJS25Y, SY25Y, YQ25Y, CP25E meta, 04L 04J 04K 04I 04H..）.
3. **Chain logic**: 链式赋分（FS25Y）— 起点 + 不可替代节点 + 可替代节点 + 终点 = chain total. 首次在本运行批次中出现.

Recommendation: fusion schema must distinguish these three structures (see conflicts C9).

## Boundary Identity Notes

- 本批与 04L (2026石景山一模) 不同：04L 是 2026 一模，本批的 SJS25Y 是 2025 一模，SJS26E（2026 期末）是 excluded.
- FT24Y / FT24E / FT25Y / FT25E / FT26E — 五个不同 丰台 套件年份；本批共处理 4 套（FT24Y/FT24E/FT25Y/FT25E）+ 1 blocker（FT26E）.
- SY24E (2024顺义二模) 与 SY25Y (2025顺义一模) 是不同年份不同模考；前者 reference-only 后者 P0_docx clean.

## Output Files

- `claudecode_lane/progress_batch04M.md`
- `claudecode_lane/batch04M_remaining_matrix.csv` (~70 atom rows)
- `claudecode_lane/batch04M_remaining_entries.md` (verbatim rubrics + atom commentary)
- `claudecode_lane/batch04M_missing_blockers.md`
- `claudecode_lane/batch04M_conflicts_for_codex.md`
- `04_suite_reports/claudecode_suite_reports/batch04M_remaining_suite_report.md` (this file)

No files written outside lane B's writable scope. Codex A fusion / 学生稿 / 全局 ledger / DECISION_LOG / FINAL_ACCEPTANCE_REPORT untouched.
