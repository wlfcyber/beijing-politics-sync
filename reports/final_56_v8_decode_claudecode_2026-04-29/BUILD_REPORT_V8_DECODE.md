# V8 Decode 构建报告

- 运行名：v8_decode版
- 运行日期：2026-04-29
- 控制器宿主：本机 ClaudeCode；工作目录 `C:/bp_sync_visible/reports/final_56_v8_decode_claudecode_2026-04-29`。
- 输入控制：SUITE_ROSTER.csv（56 套）+ 08_OCR-needed重跑控制清单.md + ocr_rerun_claudecode_2026-04-28（仅 S003 三件套作证据）。
- 输出独立编号：v8 decode 版；不携带 v6 命名，不基于 v6 结论。

## 验收检查

1. SUITE_ROSTER.csv 套卷数：56（要求 56） — PASS
2. 学生版标题/正文中 'v6' 出现次数：0 — PASS
3. 错肢版标题/正文中 'v6' 出现次数：0 — PASS
4. 学生版工程残留 token 命中合计：0 — PASS
5. 学生版乱码 byte 命中：0 — PASS
6. 错肢版工程残留 token 命中合计：0 — PASS（错肢版仅承载 1-15 答案键索引与错肢类型例题）
7. 学生版阅卷/评分/教研残留 token 命中合计：0 — PASS
8. 修复队列处理：18 项均已标 merged 或 blocked-with-explicit-reason — PASS
9. 学生版章节按节点组织：5 单元 × 17 节点 — PASS
10. S003 已合并 ClaudeCode v5 OCR rerun 答案键 1C 2B 3A 4A 5D 6D 7A 8D 9B 10C 11A 12B 13D 14C 15C — PASS
11. 真 source-missing/answer-key-missing 套卷未进入学生版正文；只在 audit/COVERAGE_MATRIX 出现 — PASS

## 发布物清单

- outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.md
- outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_v8_decode版_学生版.docx
- outputs/北京高考政治选择题错肢总结_v8_decode版.md
- outputs/北京高考政治选择题错肢总结_v8_decode版.docx
- audit/V8_DECODE_AUDIT.md
- audit/V8_DECODE_COVERAGE_MATRIX.csv
- audit/V8_DECODE_CLEANLINESS_SCAN.txt
- audit/V8_DECODE_EXTRACTION.json
- audit/V8_DECODE_DROPPED_ENTRIES.json
- scripts/06_strip_student_residues.py
- BUILD_REPORT_V8_DECODE.md

## 已知边界

- 客观题 1-15 答案键解码覆盖率：完全解码 32/56 套；其余 24 套答案键格式异常或源缺失，详见 COVERAGE_MATRIX。
- 主观题节点匹配：基于关键词命中评分；高频节点（3.3 矛盾观、5.5 中华文明新形态、4.3 价值观）条目较多，部分节点（2.2 真理、2.3 认识反复无限上升）在三年模拟主观题中没有独立触发，仅为客观题考点。
- 文化与哲学的双触发题（如 2024东城一模 Q16）允许同时出现在 3.x 和 5.x 节点下，避免遗漏。
- 本轮 quality fix：23 个条目因完整设问不全或答案链仅含占位符，从学生版正文移除并记入 audit/V8_DECODE_DROPPED_ENTRIES.json；学生版章节仍按必修四原理-方法节点组织，不按试卷顺序。
- 本运行不修改任何 cache 源文件、不向外传输任何文件。
