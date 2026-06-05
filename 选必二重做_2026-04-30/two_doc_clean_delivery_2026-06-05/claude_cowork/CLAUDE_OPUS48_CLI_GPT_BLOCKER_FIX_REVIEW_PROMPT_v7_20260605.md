# Claude Opus 4.8 GPT阻断项修复复核 v7

GPT-5.5 Pro 上轮分块终审第二段指出 v5 存在 5 个阻断项。Codex 已生成 v7，并做了本地渲染复核与硬噪音扫描。

请读取并复核：

- 汇编 Markdown：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/outputs/选必二法律与生活_试题细则汇编_学生可发版_v7.md`
- 宝典 Markdown：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/outputs/选必二法律与生活_AB双轴学生宝典_学生可发版_v7.md`
- QA：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/qa/TWO_DOC_CLEAN_DRAFT_QA_v7_20260605.md`
- 渲染复核记录：`/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/选必二重做_2026-04-30/two_doc_clean_delivery_2026-06-05/qa/RENDER_QA_v7_20260605.md`

## 请逐项判断 GPT 阻断项是否闭合

1. E032 `2025 · 海淀 · 二模 · 第18题`：材料 OCR/结构损坏。v7 已恢复原题图与完整材料，并保留 ①-⑨ 填空结构。
2. E045/E046 `2026 · 房山 · 一模 · 第17题第1问/第2问`：人名、AI、设问、细则题号错误。v7 已恢复“梁某”“AI 幻觉”，第2问设问改为“运用法治知识，分析该案例写入最高人民法院工作报告的意义”，细则文本改为 17(2)。第2问细则图已裁掉容易混淆的 `17（1）答案示例` 标头，只保留 `17.2 细则变通` 区域。
3. E039 `2026 · 东城 · 期末 · 第18题第1问`：答案落点曾是材料复述。v7 已改为合同成立/有效、刘某违约、侵权构成、产品责任边界、欺诈不成立等法律答点。
4. E037 `2025 · 顺义 · 一模 · 第19题第1问`：曾残留内部噪音 `存在问题：`。v7 已删除，并修正材料中的 `提起讼诉`。
5. E034 `2025 · 西城 · 期末 · 第19题`：曾有页脚和悬空提示残留。v7 已删除页脚，材料停止在案件事实，设问单独保留“唤醒词”问题。

## 同时请复扫

- 是否仍有学生稿工程痕迹、E0xx 编号、绝对路径、TODO/BLOCKED、source_id/SRC_、制作记录、三十秒速记。
- 是否还有 GPT 指出的乱码：`染某`、`AlI`、`辦杯`、`去治`、`写人`、`提起讼诉`、`存在问题：`、西城期末页脚、`唤醒词...` 悬空提示。
- 房山 17(2) 是否仍有题号混淆风险。
- 这 5 个阻断项是否足以允许重新送 GPT-5.5 Pro 分块终审。

## 输出格式

1. verdict：PASS / CONDITIONAL_PASS / FAIL
2. 是否允许继续 GPT-5.5 Pro 终审：YES / NO
3. 新必改项：如无写“无”
4. 五个阻断项逐项裁决
5. 如有非阻断提醒，请单列“非阻断提醒”
