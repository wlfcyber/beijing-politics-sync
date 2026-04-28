# Evidence Governor

状态：临时主线程监管者。独立监管者线程因当前 agent 线程数上限暂未开出，待任一 worker 完成后补开。

## 当前裁决

本轮不得签最终 PASS。理由：

- 56 套仅完成 roster 与分工，worker 输出尚未全部返回。
- `2024门头沟一模` 是分类汇编补源套卷，不是 standalone suite bundle，必须单独审证据边界。
- 旧三大 artifact 与旧 governor 只能作为待审对象，不能替代本轮行级证据。

## 验收规则

- 主观题只有细则、评标、阅卷总结或明确评分来源可签 `included/PASS`。
- 普通答案、教师版、讲评 PPT 只能签 `reference-only` 或 `NEED_EVIDENCE`，不得写成“评分细则要求”。
- 选择题必须同时有题面和可靠答案键，才可分析错肢与正确项触发；不得猜答案。
- 高风险词 `辩证否定/量变质变/主次矛盾/矛盾主次方面/两点论重点论/主流支流/价值观导向` 必须有源文或标准同义支撑。
- Governor PASS 不能代替行级证据。

## 待审输入

- `worker_reports/worker_2024.md`
- `worker_reports/worker_2025A_yimo_qimo.md`
- `worker_reports/worker_2025B_ermo.md`
- `worker_reports/worker_2026A_yimo.md`
- `worker_reports/worker_2026B_qizhong_qimo.md`
- `patcher_reports/multipoint_patch_review.md`

## 下一步

1. 等待 worker 输出。
2. 补开独立监管者线程。
3. 用 `governor_matrix.csv` 对每套签 `PASS/REJECT/NEED_EVIDENCE`。
