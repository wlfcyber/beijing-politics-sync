# V5.8 GPTPro × Claude Opus 终审门禁比较

生成时间：2026-05-21 04:35 CST

## 总结

- GPTPro：PASS / YES_WITH_GUARDS。
- Claude Opus：PASS / YES_WITH_GUARDS。
- Codex 裁决：允许进入 Word/PDF 候选成稿，但必须先执行门禁补丁；最终口径只能是“27 核心满分训练 + 38 保分/边界/回源索引”，不能写成 65 题全部核心满分闭环。
- P0：双方均无。
- P1：Claude 认为无未修 P1；GPTPro 把 CSV 残留、CC0223 材料污染、边界必修三化列为 P1/成稿前问题。Codex 按更保守口径处理：这些必须在 Word/PDF 前修完。

## 对照表

| 项目 | GPTPro | Claude | Codex 裁决 | 执行动作 |
|---|---|---|---|---|
| 总裁定 | PASS | PASS | keep | 允许进入 Word/PDF 候选，但不得声称 65 题全部核心满分闭环。 |
| Word/PDF 门禁 | YES_WITH_GUARDS | YES_WITH_GUARDS | keep_with_guards | 封面和正文保留 27 核心 + 38 保分/边界/回源索引口径；PDF 必须显示红线。 |
| P0 | 无 P0 | 无 P0 | pass | 无阻断；继续做收尾修补。 |
| 核心入口 P1 | 学生稿已修；CSV minimum_judgment 残留旧多卡写法列为 P1 | V5.7 P1 已修；CSV 字段未同步列为 P2 | patch_before_word_pdf | 生成 V5.9 CSV，将 minimum_judgment 改成 主卡/辅卡 + 具体先判句，禁止旧 X+Y 字段再生稿。 |
| 低频题视觉红线 | 要求非核心红线在 PDF 视觉可见 | 点名 5 道 low-frequency 缺视觉红线块 | patch_before_word_pdf | 给 CC0011、CC0254、CC0332、CC0340、RECOVER_2024_东城_一模_19 补 LOW-FREQUENCY 提示块。 |
| 27 核心细则对账 | 允许核心进入候选；建议保留证据清洗与 QA | P2：27 核心全量 rubric 对账留痕 | completed_mechanical_trace_manual_semantic_pending | 已生成机械追踪；17 个 PASS_WITH_MANUAL_CHECK 后续在 Word/PDF 前语义确认。 |
| CC0150 跨模块原子 | 未列为主要问题 | P2：R12-R24 串入选必一/国际政治经济原子 | patch_cleaned_copy | 生成清洗版 rubric atoms 和剔除报告，学生稿仍只用法律原子 R03-R11。 |
| CC0223 材料触发污染 | P1：material trigger 混入原卷无答案/分析/详解 | 未点名；12 题中未误升核心 | patch_before_word_pdf | 生成 V5.9 CSV 清理 material_trigger；生成 cleaned material atoms，把 M09-M24 标为 audit/non-material。 |
| 边界题必修三化风险 | 点名 RECOVER_2026_西城_二模_18_3 需改“只背综合边界最低句”并删泛政治话术 | 边界题保持非核心，不误升核心 | patch_before_word_pdf | V5.9 学生稿改边界句，避免依法行政/规范权力运行等必修三化。 |
| source-check 数量口径 | 24 个 source_check_pending，其中 23 个 SOURCE-CHECK 红线，1 个 CC0245 为 DUPLICATE-CROSSREF | 封面口径 23 source-check + 1 duplicate-crossref；38 非核心总数正确 | patch_wording | 在成稿说明中写清 24/23/1 关系，避免前后矛盾。 |
| 最终发布前盲测 | 建议 5 核心 + 3 source-check + reference_only/boundary/transfer 抽样盲测 | 12 题抽测已通过，但 Word/PDF 前仍需红线视觉 QA | future_gate | V5.9 Word/PDF 生成后再做一次盲测和视觉 QA。 |

## 立即执行补丁

1. 生成 V5.9 学生稿：补低频红线、修边界题表述、修 CC0103 裸法治中国风险、替换 AI 题“侵权构成要件”表述。
2. 生成 V5.9 逐题运行 CSV：同步 `minimum_judgment`，清理 CC0223 material_trigger。
3. 生成清洗版证据底座副本：CC0150 剔除 R12-R24 跨模块 rubric atoms；CC0223 将 M09-M24 标为 audit/non-material。
4. 更新 governor，不生成最终 PDF 前必须完成视觉 QA 和抽样盲测。
