# ORDER_058_PARTIAL_PROGRESS_STILL_GAPS_1309

时间：2026-05-24 13:09 +08

总判定：三线仍为 `DELIVERED_WITH_GOVERNANCE_GAPS`。本轮看到必修四、选必二有局部推进，但没有任何一线满足 `MASTER_REQUIREMENTS.md` 的硬验收。不得写入或宣称严格最终接受。

## 1. 选必一补丁命令

状态：12:39-13:09 未见新产物。继续执行 `ORDER_010_XUANBIYI_NEXT.md`，不得把旧候选说成最终。

必须补齐：

- `07_gpt_pro_fusion/GPT_PRO_WEB_RETRY_STATUS.md`
- `07_gpt_pro_fusion/coverage_blockers_after_independent_thick_draft.csv`
- 根目录覆盖阻塞矩阵 `coverage_blockers_after_independent_thick_draft.csv`
- `CONFUCIUS_ARTIFACT_CHECK.md`
- `WORD_PDF_RENDER_QA.md` 或同等渲染 QA 报告

硬要求：

- 继续盯 `BATCH_015`、12 个 `NEEDS_EVIDENCE`、2024 东城一模 Q16、题号/年份错配。
- 真实 GPT/Claude 复核必须有可核验记录；本地 Codex 或单线程自述不得替代。
- Governor 与 Confucius 必须独立落文件，且 Confucius 只看学生可见产物。

## 2. 必修四补丁命令

状态：本轮新增 ClaudeCode 二模厚卡/节点复核与 `build_overnight_v8_deliverables.py`，但这些仍只是修补输入，不是验收闭环。GPT Pro web review 仍未解决，`00_39_BLOCKER_STATUS.md` 和 `old_gap_closure_matrix_0039.csv` 仍缺。

必须把 ClaudeCode 复核意见转成正文补丁：

- 删除或明确降级顺义二模 21 的旧“主观深化卡”重复段，不能与新厚卡并存造成假覆盖。
- 顺义二模 21 中无依据的“价值观导向”必须改为有题源依据的“科学思维/四个自信”等表述。
- 房山二模 21 中无依据的“价值观导向”必须改为“长征精神/精神谱系”等题源可支撑表述。
- 丰台二模 22 的“两点论和重点论”必须说明其来源是从主要矛盾/矛盾方法论延伸，不得伪装成评分细则原词。
- 节点章旧标题 `## 2026年二模题例` 中实际混入期中期末题，必须改为 `## 2026年期中期末补充题例` 或并入节点。
- 石景山二模 20 不能只挂“系统思维”一个节点，至少补入“人民立场/制度优势/中国特色社会主义文化”中的一个受题源支撑节点。

必须生成：

- `00_39_BLOCKER_STATUS.md`
- `old_gap_closure_matrix_0039.csv`
- 补丁后的 Governor 报告
- 补丁后的 Confucius 学生视角报告
- 补丁后的 Word/PDF 渲染 QA

硬要求：

- GPT Pro web review 若仍因 Chrome extension 或提交失败而未完成，必须标记 `WAITING_FOR_WEB_GPTPRO_REVIEW`，不得写 final pass。
- 夜间 v8/v9/v10 只可称为候选或修补中版本，不能称严格最终。

## 3. 选必二补丁命令

状态：本轮刷新 v13.10 成品、治理、模型日志和渲染记录，但当前自述仍是 `v13_10_final_baodian_integrated_pdf_rendered_docx_generated_with_docx_render_caveat`。Word export 视觉 QA 重跑被记录为阻塞/不宣称通过；v13.11 尚未出现。

必须补齐：

- `V13_11_BLOCKER_STATUS.md`，明确列出 v13.11 未出现、无新增真实 GPT/Claude delta review、DOCX 直接渲染 caveat 仍在。
- 若要升级为严格通过，必须生成 `v13_11_delta_review`，并包含真实 GPT Pro 与 Claude Opus 对 v13.10 的差量复核记录。
- 若要消除 DOCX caveat，必须产出可核验的 Word/DOCX 直接渲染视觉 QA；否则只能称“DOCX 已生成、PDF 已渲染”，不能称 DOCX 渲染通过。
- 对齐 Word COM / QA 数字：当前附录中出现 45 页/1191 段的说法，而 QA 文件链路中曾出现 55 页/约 1684 段。必须用一个新文件说明以哪一次为准、为什么。

硬要求：

- 不得把 v13.10 直接改名为 v13.11。
- 不得用旧的真实 GPT/Claude 记录冒充 v13.11 差量复核。
- Governor 可以承认可用候选，但不能在 DOCX 直接渲染 caveat 和 v13.11 缺失时签严格最终。

## 4. 总管边界

- 本轮不允许写严格最终接受标记。
- 三线继续按 `ORDER_010_XUANBIYI_NEXT.md`、`ORDER_020_BIXIU4_NEXT.md`、`ORDER_030_XUANBIER_NEXT.md` 推进。
- 下一轮重点检查：选必一是否恢复产出；必修四是否落地 ClaudeCode MUST_FIX；选必二是否出现 v13.11 blocker/status 或真实差量复核。
