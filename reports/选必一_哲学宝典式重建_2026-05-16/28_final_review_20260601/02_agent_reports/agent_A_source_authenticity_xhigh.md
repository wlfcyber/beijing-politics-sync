# Agent A 来源真实性复核报告

- agent: A
- role: 只核查来源真实性
- generated_at: 2026-06-01
- target_docx: `/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_终极版_20260531.docx`
- evidence_cards: `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/27_from_zero_source_locked_rebuild_20260531/02_source_cards/raw_cards`
- supporting_audit_outputs:
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/28_final_review_20260601/01_audit/FINAL_REVIEW_ENTRY_AUDIT.csv`
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/28_final_review_20260601/01_audit/FINAL_REVIEW_SOURCE_PATHS.csv`
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/选必一_哲学宝典式重建_2026-05-16/28_final_review_20260601/01_audit/FINAL_REVIEW_AUDIT_SUMMARY.md`

## 总判断

CONDITIONAL PASS

判断口径：终审 DOCX 中已经出现的 461 条宝典条目，均能解析出题源/题号并映射到证据卡；55 个被 DOCX 实际引用的证据卡均存在，`RAW_CARD_INDEX.csv` 中均为 `RAW_CARD_READY`，且 `paper_found=YES`、`rubric_found=YES`；证据卡内 1102 次 `FOUND*` 原始路径引用均指向当前桌面实际存在文件，未发现 DOCX 条目指向不存在证据卡、虚构路径或缺失原卷/细则路径。

保留条件：本证据卡目录使用 `RAW_CARD_READY` 作为可用状态，不使用字面 `PASS`；若主流程要求统一为 `PASS`，需要另做状态归一化。另有两条用户点名重点源没有出现在终审 DOCX 和证据卡索引中，不能在本报告内证明其已被终稿覆盖。若它们本应进入终稿，需要主线程补建证据卡后再修订正文。

## 全查范围与证据链

- DOCX 解析范围：461 条条目，55 个唯一题源证据卡。
- 证据卡索引范围：`RAW_CARD_INDEX.csv` 中 55 个 `RAW_CARD_READY` 卡被终稿引用；另有 1 个 `BLOCKED_SOURCE_GAP` 卡 `2026_海淀_期中_Q22_1`，未被当前 DOCX 引用。
- 原始路径核验：从被引用证据卡抽取 1102 次 `FOUND*` 路径引用，去重后 114 个桌面原始文件路径，全部 `exists=YES` 且位于 `/Users/wanglifei/Desktop/` 下。
- DOCX 设问到证据卡核验：429 条 `EXACT`，32 条 `PARTIAL`，0 条 `NO_MATCH`。`PARTIAL` 为压缩匹配，未构成来源缺失。
- 未发现：`CARD_NOT_FOUND`、`CARD_PATH_MISSING`、`SOURCE_PATH_MISSING`、`CARD_ID_PARSE_FAIL`。

## 逐条风险

| 宝典条目标题 | 证据卡文件 | 原始试卷/细则路径 | 问题类型 | 建议处理 |
| --- | --- | --- | --- | --- |
| 无，终审 DOCX 未出现 `2025海淀期末Q22` | 无，`RAW_CARD_INDEX.csv` 无 `2025_海淀_期末_Q22` | 无 | 用户点名重点源缺席，无法证明终稿已覆盖该来源；这不是已出现条目的虚构风险，而是覆盖/遗漏风险 | 主线程确认 `2025海淀期末Q22` 是否应进入终稿；若应进入，回原卷和细则补建证据卡，再补入或修订 DOCX |
| 无，终审 DOCX 未出现 `2026房山二模Q20`；终稿实际出现的是 `2026房山一模Q19` | 无，`RAW_CARD_INDEX.csv` 无 `2026_房山_二模_Q20`；已有 `2026_房山_一模_Q19.md` | 已有一模路径：`/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026房山一模/试卷/试卷.pdf`；`/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026房山一模/细则/细则.docx` | 用户点名题源与终稿题源命名不一致，可能是题源遗漏或用户重点源名与当前终稿不同步 | 主线程确认是否确有 `2026房山二模Q20` 应处理；若是，不能用一模 Q19 代替，应另建二模 Q20 证据链 |
| `2024顺义思政二模Q19(2)` 下 4 条：国际竞争实质、维护国家利益、全球南方联合自强、人类命运共同体 | `2024_顺义_二模_Q19_2.md` | `/Users/wanglifei/Desktop/2024模拟题/顺义思政二模/试卷/试卷.docx`；`/Users/wanglifei/Desktop/2024模拟题/顺义思政二模/细则/细则.docx` | 命名规范化风险：DOCX 写 `顺义思政二模`，card_id 规范化为 `顺义_二模`，来源真实但名称有压缩 | 建议在证据卡或索引中保留 alias：`2024顺义思政二模Q19(2)`，避免后续 Agent 误判为不一致 |
| `2026朝阳期末Q20` 下 12 条：和平与发展、共同利益、维护国家利益、开放型世界经济、人类命运共同体等 | `2026_朝阳_期末_Q20.md` | `FOUND_BY_HINT`：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/试卷/试卷.pdf`；`FOUND`：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026朝阳期末/细则/细则.pdf` | 原卷为提示命中且卡片含扫描标记；路径存在，来源不虚构，但证据卡属于视觉/扫描来源，复核风险高于普通文本源 | 保留为 CONDITIONAL PASS；若后续改动这些条目，应回 PDF 页面图或 OCR 文本复核题干和细则原文 |
| `2026东城一模Q19(3)` 下 9 条：自力更生和对外开放、开放型世界经济、制度型开放、国际规则话语权、产业链供应链等 | `2026_东城_一模_Q19_3.md` | `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026东城一模/试卷/补充材料/2026东城一模 原卷扫描版.pdf`；`/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026东城一模/试卷/试卷.pdf`；`/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026东城一模/细则/分题细则/东城一模评标细则（勿传）/19（3）.pptx` | 扫描/OCR 标记明显，并有若干非本题分题细则 `NOT_FOUND` 残留；本题所需试卷和 19(3) 细则路径存在 | 保留本题来源；建议清理卡片中的非本题 `NOT_FOUND` 残留，并把 19(3) 作为唯一细则定位写明 |
| `2026丰台一模Q19` 下 9 条：共同利益、全球治理观、真正多边主义、人类命运共同体、2030 可持续发展议程等 | `2026_丰台_一模_Q19.md` | `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/试卷/试卷.pdf`；`/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026丰台一模/细则/细则.pptx` | 卡片含扫描标记；路径存在，来源不虚构，但属于扫描/OCR敏感源 | 后续修订时回 PPT/原卷页面复核，不要只依赖卡片摘录 |
| `2025丰台二模Q20` 下 13 条：全球治理观、公正合理国际秩序、人类命运共同体、南南合作、中国国际地位等 | `2025_丰台_二模_Q20.md` | `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025丰台二模/试卷/试卷.pdf`；`/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025丰台二模/细则/分题细则/2025丰台二模评标细则/2025丰台二模评标细则/20题.docx` | 卡片含扫描标记，且有非 Q20 分题细则 `NOT_FOUND` 残留；本题 Q20 细则路径存在 | 保留来源；建议把卡片证据聚焦到 `20题.docx`，非本题缺失项不作为风险来源继续传播 |
| `2025昌平二模Q21` 下 7 条：贸易投资自由化便利化、经济全球化正确方向、开放型经济、两个市场两种资源、国际规则话语权等 | `2025_昌平_二模_Q21.md` | `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025昌平二模/试卷/试卷.pdf`；`/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025昌平二模/细则/细则.pptx` | 卡片含图片/视觉来源标记；路径存在，来源不虚构 | 保留来源；若条目内容再改，应回 PPT 原图或渲染页检查细则词 |
| `2026西城期末Q20` 下 6 条：全球治理观、公正合理国际秩序、中国智慧中国方案、绿色低碳转型、巴黎协定、负责任大国 | `2026_西城_期末_Q20.md` | `FOUND_VISUAL_DESKTOP_RESTORED_ORIGINAL`：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末/试卷/2026北京西城高三上期末政治教师版.pdf`；`FOUND`：`/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026西城期末/细则/细则.pdf`；另有参考答案 PDF | 卡片含 `FOUND_VISUAL_DESKTOP_RESTORED_ORIGINAL` 和一个评标 PPT `NOT_FOUND` 残留；所用原卷、细则、参考答案路径均存在 | 保留来源；建议标明正式依据优先使用 `细则.pdf`，参考答案只作辅助，缺失的评标 PPT 不作为引用依据 |
| `2024东城二模Q20` 下 7 条：国际关系民主化、人类命运共同体、全球发展/安全/文明倡议、民心相通、《联合国宪章》 | `2024_东城_二模_Q20.md` | `/Users/wanglifei/Desktop/2024模拟题/东城二模/试卷/试卷.pdf`；`/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/分题细则/阅卷总结/21题/20小题二模阅卷总结.docx`；`/Users/wanglifei/Desktop/2024模拟题/东城二模/细则/补充材料/细则.pdf` | 用户重点源通过路径核验，但卡片中残留多条其他题号 `NOT_FOUND`；这些不是当前 Q20 的已用证据，但会增加误读风险 | 保留来源；建议清理卡片，只保留 Q20 相关的 `20小题二模阅卷总结.docx` 和总细则 PDF |
| `2025东城期末Q20` 下 10 条：维护国家利益、资源配置、贸易投资自由化、多边贸易体制、贸易保护主义、互利共赢等 | `2025_东城_期末_Q20.md` | `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025东城期末/试卷/试卷.pdf`；`/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025东城期末/细则/细则.pdf` | 有一个补充材料 `东城期末.pptx` 的 `NOT_FOUND` 残留；正式试卷和细则路径存在 | 保留来源；建议删除或注释缺失补充材料，避免后续误以为有 PPT 细则依据 |
| `2025海淀二模Q21` 下 14 条：新型国际关系、全球治理体系、人类命运共同体、中国国际地位、联合国作用等 | `2025_海淀_二模_Q21.md` | `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/试卷/试卷.pdf`；`/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/细则/细则.docx` | 细则为 `FOUND_BY_HINT`，另有评标实录 `NOT_FOUND` 残留；正式试卷和细则路径存在 | 保留来源；建议后续如涉及评分细化，回 `细则.docx` 精确定位，不使用缺失的评标实录 |

## 重点题源核查结果

| 用户点名源 | DOCX 条目数 | 证据卡状态 | 原卷/细则路径结论 | Agent A 判断 |
| --- | ---: | --- | --- | --- |
| 2026通州期末Q20 | 13 | `RAW_CARD_READY` | 试卷 PDF、细则 PPTX 均存在 | 通过来源真实性 |
| 2026通州期末Q21 | 3 | `RAW_CARD_READY` | 试卷 PDF、细则 PPTX 均存在 | 通过来源真实性 |
| 2026丰台期末Q20 | 11 | `RAW_CARD_READY` | 试卷 PDF、细则 PDF 均存在 | 通过来源真实性 |
| 2024顺义思政二模Q19(2) | 4 | `RAW_CARD_READY` | 试卷 DOCX、细则 DOCX 均存在 | 通过来源真实性；建议保留 alias |
| 2025海淀期末Q22 | 0 | 无卡 | 未在终稿/索引中出现 | 覆盖风险，需主线程确认是否遗漏 |
| 2025延庆一模Q20(2) | 11 | `RAW_CARD_READY` | 试卷 PDF、细则 DOCX 均存在 | 通过来源真实性 |
| 2026海淀一模Q20 | 7 | `RAW_CARD_READY` | 试卷 PDF、细则 PDF 均存在 | 通过来源真实性 |
| 2026房山二模Q20 | 0 | 无卡 | 未在终稿/索引中出现 | 覆盖或命名风险，需主线程确认 |
| 2026朝阳期末Q20 | 12 | `RAW_CARD_READY` | 试卷 PDF、细则 PDF 均存在 | 条件通过，扫描/提示命中源需保守 |
| 2026顺义二模Q20 | 12 | `RAW_CARD_READY` | 试卷 PDF、评标 DOC 均存在 | 通过来源真实性 |
| 2024海淀期中Q16(2) | 1 | `RAW_CARD_READY` | 试卷 PDF、细则 PDF 均存在 | 来源真实性通过；模块边界不属于本报告判断 |
| 2024东城二模Q20 | 7 | `RAW_CARD_READY` | 试卷 PDF、Q20 阅卷总结 DOCX、总细则 PDF 均存在 | 来源真实性通过；卡片需清理无关 `NOT_FOUND` |
| 2026西城期末Q20 | 6 | `RAW_CARD_READY` | 试卷 PDF、细则 PDF、参考答案 PDF 均存在 | 条件通过；正式依据应优先细则 PDF |

## 未列为风险的事项

- `RAW_CARD_READY`：本目录索引中没有字面 `PASS` 状态；55 个被终稿引用的卡均为 `RAW_CARD_READY`，且纸面/细则路径都存在，因此按本 run 现有 schema 视为可用。
- `答案落点 NO_MATCH`：本报告只核查来源真实性，不判断答案句是否逐字在卡片中出现；答案句常为学生化改写，不能作为来源真实性失败依据。
- `MISSING_WHY`、同题组和序号类 flags：这些属于 Agent B/C 的题号、同题组、可读性或结构问题，不作为 Agent A 来源真实性风险。

## 建议处理顺序

1. 先确认 `2025海淀期末Q22` 和 `2026房山二模Q20` 是否应进入终稿；若应进入，补建证据卡后再改 DOCX。
2. 对扫描/提示命中源，尤其 `2026朝阳期末Q20`、`2026东城一模Q19(3)`、`2026丰台一模Q19`、`2025丰台二模Q20`、`2025昌平二模Q21`，后续修订前回原卷渲染页或 PPT/PDF 页面确认。
3. 清理证据卡中的非本题 `NOT_FOUND` 残留，避免后续 Agent 把“找不到其他题的分题细则”误读为当前条目来源缺失。
