# P2G017 Progress Log

> 小规模 source_id 级 P2 复核子任务，对单一 source `017_Desktop_2024模拟题_2024朝阳期中_试卷_试卷.pdf` 下三行 P2 choice_trap（Q7/Q8/Q10）执行源验证。

Run timestamp: 2026-05-07
Lane: ClaudeCode
Trigger: P2 全量复核多次 stall 后由 supervisor 切片到单 source 子组（详见 `claudecode_lane/p2_recheck/SUPERVISOR_PATCH_01_FULL_P2_STALL_SPLIT.md`）。
Prompt: `claudecode_lane/p2_recheck/CLAUDECODE_P2G017_PROMPT.md`。

## Step 1: 输入识读

- 读 `fusion/framework_first_fusion/RECHECK_MANIFEST_ENRICHED.csv` 第32-34行，定位 source_id=017 的三行 P2：
  - Q-2024朝阳期中-10（外延关系>属种关系，已 manifest 标 blocked_keep_out/answer_missing）
  - Q-2024朝阳期中-7（三段论第三格AAI式，covered_by_74_review_body）
  - Q-2024朝阳期中-8（必要条件假言判断三种等价表达式，covered_by_74_review_body）
- 读 `fusion/p2_recheck_sources/P2_SOURCE_TEXT_INDEX.csv` 第12-15行，定位 017 源四份提取文本（1 paper + 3 support）。

## Step 2: 题面（stem & options）核验

- 打开 paper.txt 全文：21 011 字节，含 Q1-Q15 完整客观题题面 + Q16-Q20 完整主观题题干。
- Q7（行65-73）、Q8（行74-81）、Q10（行90-96）三题 stem 与四个选项均能逐字核验。

## Step 3: 答案核验（关键失败路径）

- 检查 support 文件：
  - 评标docx.docx (12 818 字节)：完整文本仅含 16 题（范伟光组）/ 17 题（高捷组）/ 18 题（任会波组，含'楚王不完全归纳轻率概括'+'晏子类比推理'两段）/ 20 题（1）（2）（3）三个分组的主观题阅卷细则。**全文不出现 Q1-Q15 任何选择题答案。**
  - 评标2.docx (886 字节)：仅 7 行小组首页索引。
  - 期中1试题(1).pdf (21 011 字节)：与 paper.txt 同文副本，无答案表。
- 三份 support 文件 grep 关键词`答案`、`参考答案`、`选择题答案`、`^[1-9]\.\s*[A-D]`、`题号`，全部无命中。
- → 三行客观题答案在 017 源 support 范围内不存在。

## Step 4: 决策

按 P2 硬规则：
1. 'Verify stem/options and answer key before confirming choice-trap rows' → 三行无法 confirm。
2. 'If answer evidence is unavailable, mark source_insufficient and can_enter_fusion=no' → 三行同走 source_insufficient。
3. 'Do not invent options, answers, rubrics, or source files' → 三行的 patched_answer_sentence 不输出确定性答案。

## Step 5: 输出件落盘

| 文件 | 状态 |
|------|------|
| P2G017_RECHECK_DECISIONS.csv | 写 1 表头 + 3 数据行 ✅ |
| P2G017_RECHECK_PATCHES.jsonl | 写 3 行 JSON ✅ |
| P2G017_SOURCE_EVIDENCE.md | 写 ✅ |
| P2G017_RECHECK_ACCEPTANCE.md | 写（含 NOT_FINAL 声明） ✅ |
| P2G017_PROGRESS.md | 当前文件 ✅ |

## Step 6: 完成状态

- exact row count 3 ✅
- patch count 3 ✅
- no Word/PDF/delivery ✅
- 输出全部在 claudecode_lane/p2_recheck/ ✅
- 三行 decision 均为 source_insufficient ✅
- evidence_level 维持 manifest 原值 B-choice-signal ✅

## Notes & 待处理

- framework_first_fusion P1版第527/751/806行的 Q-2024朝阳期中-7/8/10 三处仍标'需 Codex 回源复核'；本任务结论应在后续独立 fusion patch 中落地（降级为 source_insufficient·暂不入正文），但该 patch 不在 P2G017 这一小规模子任务输出范围内。
- 若后续找到朝阳教研中心或官方教师版2024.11期中政治答案表，可改走 confirmed_with_patch 路径补回填——独立任务，不在本任务输出。
