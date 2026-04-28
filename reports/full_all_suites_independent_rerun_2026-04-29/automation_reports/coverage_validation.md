# Coverage Validation

初始校验时间：2026-04-29

## 结论

初始 roster 可执行：

- `SUITE_ROSTER.csv`: 56 行
- `COVERAGE_MATRIX.csv`: 56 行
- 2024: 15 套
- 2025: 22 套
- 2026: 19 套

## 分工计数

- `worker-2024`: 15 套
- `worker-2025A`: 16 套
- `worker-2025B`: 6 套
- `worker-2026A`: 10 套
- `worker-2026B`: 9 套

## 特殊边界

- `2024门头沟一模`: `cache_status=classification-bundle-supplement`。它不在 standalone suite bundle 中，使用分类汇编 bundle 与补源答案 PDF。主观题不能仅凭参考答案或等级描述升格为正式细则链。

## 当前阻塞

- 无初始化阻塞。
- 所有套卷仍等待 worker 输出，不能签最终 PASS。
