# 必修四从0重跑进度（按套卷滚动）

## 启动阶段

- [x] 控制文件就绪（SOURCE_LEDGER 54 套卷、COVERAGE_MATRIX、DECISION_LOG、GOVERNOR_CHECKLIST、FINAL_ACCEPTANCE_REPORT、audit 三件套）
- [x] 读完 SKILL/小本本/philosophy-trigger-standards/TASK_BRIEF/SUPERVISOR_DIRECTIVE/MASTER_REQUIREMENTS/督工补丁一/督工补丁二
- [x] 主线脚本就绪：`extract_text` / `synthesize_student` / `synthesize_word` / `quality_check` / `build_audit_files` / `finalize` / `codex_supervisor_repair`

## 套卷处理（按优先级）

### 已完成

| 年份 | 阶段 | 套卷 |
|------|------|-----|
| 2026 | 一模 | 海淀 / 西城 / 东城 / 朝阳 / 丰台 / 石景山 / 房山 / 延庆 / 门头沟 |
| 2026 | 期末 | 海淀 / 西城 / 朝阳 / 丰台 / 通州（石景山按 SKILL 排除） |
| 2026 | 期中 | 海淀 / 朝阳（其余按 ledger 决定） |
| 2025 | 一模 | 海淀 / 西城 / 东城 / 朝阳 / 丰台 / 石景山 / 房山 / 延庆 / 门头沟 / 顺义 |
| 2025 | 二模 | 海淀 / 西城 / 东城 / 朝阳 / 丰台 / 昌平 |
| 2025 | 期末 | 海淀 / 西城 / 东城 / 朝阳 / 丰台（其余按 ledger 决定） |
| 2024 | 一模 | 海淀 / 西城 / 东城 / 朝阳 / 丰台 / 石景山 |
| 2024 | 二模 | 海淀 / 西城 / 东城 / 朝阳 / 丰台 / 顺义 |
| 2024 | 期中 | 海淀 / 朝阳（其余按 ledger 决定） |

> 完整套卷集合见 `SOURCE_LEDGER.csv`（54 套）。每套对应 `audit/entries/<suite>.jsonl` 与 `suite_reports/<suite>.md`。

### 已排除

- `2026_石景山_期末`：用户已确认无可用评分细则，整套从所有模块主链排除。`COVERAGE_MATRIX.csv` 已记录 `excluded-by-skill-rule` 边界行。

## 控制文件 / 输出

- [x] `audit/entries/<suite>.jsonl` × 54
- [x] `suite_reports/<suite>.md` × 54
- [x] `SOURCE_LEDGER.csv` × 54 套
- [x] `COVERAGE_MATRIX.csv` 350 数据行（含 1 行 `2026_石景山_期末` 边界占位），唯一套卷 55
- [x] `audit/证据索引.csv`（与 entries 同步）
- [x] `audit/覆盖验收表.csv`（按套卷聚合）
- [x] `audit/问题与边界清单.md`
- [x] `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.md`
- [x] `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.docx`
- [x] `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.WordSaved.docx`
- [x] `audit/word_validation/claude_student.WordSaved.docx`
- [x] `audit/word_validation/quicklook/claude_student.docx.png`

## 质量校验

- [x] `python3 scripts/quality_check.py`：扫描 346 条 entries，0 个问题
- [x] 学生版 Markdown 独立 `rg` 禁词检查（`细则 / 评标 / 参考答案 / 答案写 / 答案核 / 答案/补充 / 可从.*角度 / /Users/ / .pdf / .docx / .pptx / OCR / debug / slide / line id / file id / PASS / correct_option_chain / filled`）：0 命中
- [x] WordSaved.docx 段落级独立禁词扫描：0 命中
- [x] 硬样本 1（2026 海淀一模 Q16）：物质决定意识/必要性 + 主观能动性 双节点入；未写"意识反作用"
- [x] 硬样本 2（2024 东城一模 Q18(3)）：辩证否定 / 守正创新；boundary_note 含模块边界注释

## 收尾边界

- Word 导出 PDF：尝试两次 AppleScript 均超时（AppleEvent timeout，rc=1，-1712）；按督工补丁 C 不作为硬阻塞，QuickLook PNG 已替代承担版式留证。
- 漫画原图嵌入：未达成自动批量嵌入，已在 entries 与 source_excerpts 留索引，学生版以文字触发链落地。

## 终态

- [x] FINAL_ACCEPTANCE_REPORT.md 已重写为本轮真实终态。
