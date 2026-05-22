# GPTPro V5.2 Review Capture

捕获时间：2026-05-21

来源：Safari 中 ChatGPT Pro 对话 `https://chatgpt.com/c/6a0c3288-938c-83ea-bca9-66b8db9d9326`。页面显示已完成回复，模型思考约 35 分 49 秒。复制回复按钮未写入系统剪贴板，本文件根据 Safari accessibility tree 可见文本完整记录关键裁定、表格和补丁指令。

## 结论

可以称为 `guarded v2 guarded core teaching version`，中文建议名为：

**Guarded v2 核心教学版**

但不能称为：

**65 题全部核心满分闭环版**

GPTPro 认可当前主账本：

- questions：65
- evidence：61 formal，4 reference_only，0 missing
- material atoms：482
- ask atoms：65
- rubric/answer atoms：377，其中 7 个 patch scoring atoms
- pressure：PASS 45，即 43 core + 2 boundary-gate；PARTIAL 20；FAIL 0
- baodian labels：43 core_full_score_supported，14 formal_open_container_partial，4 reference_only_demo，2 boundary_non_core，2 open_container_only

GPTPro 说明：旧进度包是 44 core + 2 boundary + 19 partial、370 rubric atoms、DOCX QA 未闭合；新 accepted progress 包已经改成 43 core + 2 boundary + 20 partial、377 atoms，并声明 Word/PDF QA 已完成。旧 review prompt 也明确要求保留 core/open/reference/boundary 两层结构，不能把 reference_only 或 open-container 升核心。

## ACCEPTABLE_PROGRESS

### 1. 65 题 corpus 可以作为当前事实基线

接受。

当前事实基线应写成：

`65 subjective-law rows 61 formal 4 reference_only 0 missing material atoms 482 ask atoms 65 rubric/answer atoms 377 after 7 patch scoring atoms`

### 2. guarded v2 可以作为当前教学基线

接受，但名称必须 guarded。

推荐表述：

`Guarded v2 is accepted as the current guarded core teaching version for the 65-question corpus. It is not accepted as a claim that all 65 questions are core transferable full-score templates.`

中文表述：

`guarded v2 可作为当前 65 题语料的核心教学版使用，但它不是 65 题全部核心满分闭环。`

### 3. 43 core + 2 boundary + 20 partial 是证据安全口径

接受。

正确解释是：

`PASS 45 = 43 core full-score supported + 2 boundary-gate pass PARTIAL 20 = 14 formal open-container partial + 4 reference_only demo + 2 open-container-only FAIL 0`

其中 2 个 boundary-gate pass 只能说明边界守门成功，不能当选必二满分模板。open-container 与 reference_only 也不能作为核心 code 支撑。

## P0 判断

### P0 证据层：基本闭合

GPTPro 对 P0 修复的判断：

| P0 项 | 判断 |
|---|---|
| CC0077、CC0084 只保留 scoring atoms | 通过 |
| CC0150 删除 21《当代国际政治与经济》，只保留 20 scoring chain | 通过 |
| CC0245 使用 3 个 patch scoring atoms，R02-R04 转 risk/teaching | 通过 |
| CC0251 使用 4 个 patch scoring atoms，R02-R16 转 risk/teaching/other-question | 通过 |
| CC0143 expansion_status 改为 CORE_CODEBOOK_SUPPORT_AFTER_CC0143_PATCH | 通过 |
| CODE_COWORK_007 拆成 007A、007B、007C、007D | 通过 |
| CC0380 改为 OPEN_CONTAINER_ONLY | 通过 |
| reference_only / boundary / open 保留非核心标签 | 通过 |
| forbidden-text scan 0 | 有条件通过 |
| DOCX Microsoft Word export + PDF render + PyMuPDF 114 pages + blank 0 | 报告口径通过 |

### 但仍有一个成稿层残留

典型残留包括：

`【细则原子覆盖草句】 18.无人机起飞如何系好"安全带"? 要约 实质性变更，新要约 承诺 【违约逻辑：合同成立+合同有效+存在违约行为 → 承担违约责任 4分】 【侵权逻辑：权利受保护+侵权要件齐备 → 承担侵权责任 3分】 1.只说合同成立/合同有效...`

GPTPro 判断：当前 forbidden scan 词表不够宽，扫到了 0，但没有覆盖：

`【细则原子覆盖草句】 题干拼贴 评分逻辑拼贴 原始讲解提示 “只说……也可给”`

因此裁定：

`P0 evidence cleanup: closed enough`

`P0 student-facing answer cleanliness: not fully closed until CC0244 is regenerated`

## DOCX / PDF QA 判断

### QA blocker 可以解除，但限定为报告接受

用户补充状态为：

`Microsoft Word opened DOCX Word exported PDF PyMuPDF rendered 114 pages blank-page detections 0`

GPTPro 认为这足以解除上一轮 DOCX visual QA blocker。

但 GPTPro 保留限定：本轮 accepted progress zip 里有 QA 报告，没有附带实际 `.docx` 和 Word-exported `.pdf` 文件本体。因此本轮不能独立重渲染，只能接受 QA 报告口径。

推荐最终 QA 口径：

`DOCX/PDF visual QA reported PASS: Microsoft Word export succeeded, PDF has 114 rendered pages, PyMuPDF blank-page detections = 0. This resolves the previous DOCX visual QA blocker, provided the distributed DOCX/PDF are the exact files covered by the report.`

## ROW_LEVEL_PATCH_TABLE

| question_id | current_label | decision | required_patch | evidence_needed | severity |
|---|---|---|---|---|---|
| CC0244_2026_东城_期末_18 | core_full_score_supported | patch_before_student_facing_final | 重新生成 full_score_sentence_generated 和 complete_answer_generated；删除题干拼贴、评分草句、内部标记、教学提示；只保留合同成立有效、违约责任、侵权责任、材料事实嵌入和责任结论 | 无需回源；用 R_CC0244_2026_东城_期末_18_03、R_CC0244_2026_东城_期末_18_05 等正向 scoring atoms；R08 若是教学提示则保留为 risk evidence | high_if_in_baodian_medium_if_csv_only |
| CC0077_2025_东城_一模_19 | core_full_score_supported | accept_after_trim | 已按 R02-R04 scoring atoms 输出；保持学生问题/建议不进满分句 | 无需新证据 | closed |
| CC0084_2025_东城_二模_19 | core_full_score_supported | accept_after_trim | 已按 R02-R05 scoring atoms 输出；保持学生问题/建议不进满分句 | 无需新证据 | closed |
| CC0150_2025_朝阳_二模_20 | core_full_score_supported | accept_after_trim | 已限于第 20 题法律与生活 scoring chain R05-R11；不得恢复第 21 题国际政治经济内容 | 无需新证据 | closed |
| CC0245_2026_东城_期末_18_2 | core_full_score_supported | accept_after_patch_atoms | 已使用 PATCH_CC0245_R01A_REMEDY_PATH、PATCH_CC0245_R01B_EVIDENCE_PREP、PATCH_CC0245_R01C_REASONABLE_REQUEST；R02-R04 不得回到 support | 无需新证据 | closed |
| CC0251_2026_丰台_一模_20 | core_full_score_supported | accept_after_patch_atoms | 已使用 PATCH_CC0251_R01A_COURT_ANCHOR、PATCH_CC0251_R01B_PUBLIC_PLACE_RULE、PATCH_CC0251_R01C_FACT_NO_FAULT、PATCH_CC0251_R01D_VALUE_BOUNDARY；R02-R16 不得回到 support | 无需新证据 | closed |
| CC0143_2025_朝阳_一模_19 | core_full_score_supported | accept_metadata_fixed | expansion_status 已改为 CORE_CODEBOOK_SUPPORT_AFTER_CC0143_PATCH；继续禁止 teaching-reflection atoms 进入 core support | 无需新证据 | closed |
| CC0380_2026_顺义_二模_18_2 | open_container_only | accept_non_core | 保持 OPEN_CONTAINER_ONLY；不得作为 AI 治理或人格权核心模板 | 无需新证据 | closed |
| CC0276_2026_房山_二模_17 | boundary_non_core | accept_boundary | 保持 boundary-gate pass；不得作为选必二核心满分模板 | 无需新证据 | closed |
| RECOVER_2026_西城_二模_18_3 | boundary_non_core | accept_boundary | 保持 boundary-gate pass；不得进入意义三层核心节点 | 无需新证据 | closed |
| reference_only_4_rows | reference_only_demo | accept_non_core | 继续只作 reference_only demo，不得支撑核心 code | 若要升级必须补 formal 细则 | closed |

## FRAMEWORK_PATCH_TABLE

| node_id_or_file | issue | required_patch | why | severity |
|---|---|---|---|---|
| FWV1_2_N06A/B/C/D | CODE_COWORK_007 已拆成四个子节点 | 接受拆分并固定命名：007A 法律边界识别与合规措施；007B 维权准备与诉讼请求；007C 调解方案与合同诚信理由；007D 公益诉讼与司法确认 | 四类题启动判断不同，不能继续用一个“程序维权三层”覆盖 | closed |
| FWV1_2_OPEN | CC0380 和 RECOVER_2026_西城_二模_18_2 为 open_container_only | 继续保留 open_container，不进入 core_node | 两题没有重复 formal 同型证据，且 AI/数字治理边界风险高 | closed |
| FWV1_2_GATE | CC0276 和 RECOVER_2026_西城_二模_18_3 为 boundary-gate | 继续保留 boundary_gate，不进入 core_node | 涉外法治、国家治理现代化容易必修三化 | closed |
| FWV1_2_N04 / CC0244 | 成稿输出仍残留题干和评分草句 | 重新生成 CC0244 在 runs 和宝典里的学生可写答案；同时从扫描词表中加入“细则原子覆盖草句”“只说”“也可给”“题干原文过长拼贴”等 | 当前 CSV 层仍不够干净，高概率影响学生版可信度 | high_if_propagated |
| full_score_sentence_bank | node_class 区分已存在 | 保留 core_node、boundary_gate、open_container 标识；不要把 open/boundary 句放入普通高频满分句 | 避免学生把开放容器和边界守门误用为核心模板 | closed |

## BAODIAN_PATCH_TABLE

| section_or_file | issue | required_patch | why | severity |
|---|---|---|---|---|
| 12_final_baodian/question_by_question_framework_runs.csv | CC0244 答案字段不干净 | 重写 CC0244 full_score_sentence_generated 和 complete_answer_generated；只保留得分表达 | 题干、评分草句、教学提示不能进入学生满分答案 | high |
| 12_final_baodian/选必二法律主观题满分宝典.docx | 本轮未附 docx 本体，只有 QA 报告 | 若 CC0244 污染已经进入 DOCX，必须替换后重新 Word 导出 PDF 并跑 114 页级 QA；若未进入 DOCX，仅同步 CSV 即可 | 保证最终发放物与 QA 报告一致 | conditional_high |
| 12_final_baodian/full_score_sentence_bank.csv | 当前已有 node_class，方向正确 | 继续保持 open/boundary 非核心标识，不改成普通满分句 | 防止非核心迁移 | closed |
| 12_final_baodian/DOCX_QA_GUARDED_V2.md | QA 报告显示 Word/PDF/PyMuPDF 通过 | 可解除上一轮 DOCX visual QA blocker；但报告不能改变证据标签 | 渲染通过不等于 65 题核心闭环 | closed |

## CAN_CONTINUE_TO_NEXT_STEP

`YES_WITH_GUARDS`

但 next step 不是继续扩框架，也不是宣布 65 题满分闭环。

Codex 下一步只做三件事：

1. 处理 CC0244 成稿残留：重新生成 CC0244 的 full_score_sentence_generated 与 complete_answer_generated。GPTPro 建议句式为：陈某与刘某之间合同依法成立并有效。刘某交付内部结构轻微损伤的展示机，未全面、诚信履行合同义务，构成违约，应承担相应违约责任。无人机因损伤失控坠毁并砸伤陈某，造成医疗费和商业损失，符合侵权责任的事实链，陈某可以依法请求赔偿医疗费、误工费或经营损失等合理损失。注意：这只是清洗方向，最终仍需严格绑定 CC0244 的 scoring atom，不要额外扩法考构成。
2. 扩大 forbidden scan：加入 `细则原子覆盖草句`、`只说`、`也可给`、`第X题原题拼贴`、`要约 实质性变更 新要约 承诺`、`【违约逻辑`、`【侵权逻辑`、`学生问题`、`教学建议`、`复练`、`当代国际政治与经济`。
3. 若 CC0244 出现在 DOCX/PDF 正文，重导出并重跑 QA。如果污染仅存在 CSV 审计文件，DOCX/PDF 可保持 QA pass；如果污染进入宝典正文，则必须替换后重新导出 PDF，并重新记录 114 页或新页数的 PyMuPDF 渲染结果。

## 最终可用表述

可以写：

`Guarded v2 accepted as guarded core teaching version. Current evidence baseline: 65 questions, 61 formal, 4 reference_only, 0 missing; 43 core full-score-supported rows, 2 boundary-gate pass rows, 20 partial/open/reference rows, FAIL 0. DOCX/PDF QA reported pass through Microsoft Word export and PyMuPDF page render.`

不能写：

- 65题全部满分闭环
- 65题全部核心模板
- open-container题已经形成稳定框架节点
- reference_only题可支撑核心code
- boundary-gate pass等于选必二核心满分答案

最终判断：**P0 主体通过，DOCX QA blocker 可解除；但 CC0244 成稿残留需要在学生可见版本发布前清干净。**
