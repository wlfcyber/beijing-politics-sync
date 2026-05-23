# ORDER_020_BIXIU4_NEXT

发令时间：2026-05-23 23:12 +08:00

## 总命令

必修四不得签 `STRICT_FINAL_ACCEPTED`。后续工作只允许在认可底稿最小插入版基础上做候选修补，不得覆盖 4.29 v6 认可底稿，不得继续使用已废弃的 `new_9_suite_integration` 重编排版作为底稿。

当前执行底稿：

`C:\Users\Administrator\Desktop\02_代码项目与工具\mac-thread-restore\beijing-politics-sync-visible\reports\bixiu4_philosophy_strict_v8_2026-05-23\minimal_insert_on_accepted_v6\必修四哲学材料-知识触发框架_v8_认可版仅插新增卷子.md`

## PATCH_CMD_01：补旧选择题 174 条

读取：

- `remaining_old_choice_presence_gaps_after_v7.csv`
- 对应 `data/preprocessed_corpus/gpt_suite_bundles/*.md`
- 必要时回原卷/答案键核题干、正确项和错肢。

输出候选包，不直接进学生正文：

- `old_choice_repair_candidates_batch_001.md`
- `old_choice_repair_matrix_batch_001.csv`

每题必须写成：

```text
节点名
来源题目：YYYY 区县 套别 第N题
完整题干：
正确项：
材料触发点 -> 正确项链：
错肢分析：A/B/C/D，每项标注错误类型（条件夸大、主体错位、因果倒置、范围错配、推断越界、模块越界、绝对化等）
证据状态：answer-key-confirmed / needs-source-check
```

第一批先处理 30 条，优先海淀、西城、东城、朝阳、丰台，再处理郊区。不得只写“触发知识/证据要点”。

## PATCH_CMD_02：返工旧主观 68 条质量失败项

读取：

- `old_subjective_rows_present_but_quality_failed_v8.csv`
- `STRICT_GATE_REPORT.md`
- 原 bundle 或原卷，补完整设问。

输出候选包：

- `old_subjective_quality_rewrite_batch_001.md`
- `old_subjective_quality_rewrite_matrix_batch_001.csv`

每条必须补齐：

```text
框架节点：
来源题目：
完整设问：
材料触发点：
为什么能想到这个原理：只能写材料信号 -> 原理逻辑，禁止写“评分细则把……列为给分角度”
答案落点：必须是本题可直接写进答卷的答案句，禁止“先点原理、再扣材料、最后回设问”
```

先处理 `STRICT_GATE_REPORT.md` 点名的 10 个抽检样本，抽检通过后再批量处理剩余 58 条。

## PATCH_CMD_03：清理认可底稿候选中的学生版元话术

只创建候选副本，不改原底稿：

- `student_clean_candidate_from_minimal_insert.md`

必须检查并处理学生正文中的继承性残留：

- `审计`
- `证据`
- `评标`
- `评标细则`
- `逻辑与思维`
- `参考答案`
- `CSV`

已知命中点包括第 7、523、1225、1523、1875、1943、2024、2136 行附近。处理原则：题干原句如确属跨书题，移到边界审计；流程说明和审计话术不得留在学生正文。

## PATCH_CMD_04：完成真实 GPT Pro 网页 review

读取：

- `04_review_packages/GPTPRO_WEB_BATCH_A_海西东朝主观题.md`
- `04_review_packages/GPTPRO_WEB_BATCH_B_郊区主观题.md`
- `04_review_packages/GPTPRO_WEB_BATCH_C_高风险原理.md`
- `04_review_packages/GPTPRO_WEB_BATCH_D_选择题海西东朝.md`
- `04_review_packages/GPTPRO_WEB_BATCH_E_选择题郊区.md`
- `04_review_packages/GPTPRO_WEB_BATCH_F_新增9套.md`

提交到 ChatGPT 网页版 GPT Pro。若自动化不可用，人工/半自动复制也可以，但必须保存真实网页端返回：

- `05_model_reviews/GPTPRO_WEB_BATCH_A_RESPONSE.md` 至 `F_RESPONSE.md`
- 如有截图或原始复制记录，放同目录。

禁止把 API、子智能体、本地 Codex 总结写成 GPT Pro review。

## PATCH_CMD_05：生成候选 Word/PDF 并跑最终 QA

只有 PATCH_CMD_01、02、03、04 完成后，才允许从候选 Markdown 生成：

- 学生版 DOCX
- 学生版 PDF
- PDF 抽页 PNG
- Word/PDF QA 报告

QA 必须至少覆盖：封面、目录、各大框架节点、旧主观返工样本、旧选择题样本、新增9套样本、边界排除说明。

## PATCH_CMD_06：Governor / Confucius 最终门禁

最终报告必须同时核：

- 旧主观 68 条是否全部从 FAIL 改为 PASS 或明确边界挂账。
- 旧选择题 174 条是否全部有完整题干、正确项链、错肢类型。
- 新增题是否仍保持 34 个最小插入块逻辑，未破坏认可底稿。
- GPT Pro 网页 review 是否真实完成，且意见已处置。
- Word/PDF/PNG QA 是否通过。

未全部通过时，只能写 `DELIVERED_WITH_GOVERNANCE_GAPS` 或 `CANDIDATE_DELIVERY_NEEDS_AUDIT`，不得写 `STRICT_FINAL_ACCEPTED`。
