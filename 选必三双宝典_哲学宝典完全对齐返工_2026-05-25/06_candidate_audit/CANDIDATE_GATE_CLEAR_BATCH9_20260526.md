# CANDIDATE_GATE_CLEAR_BATCH9_20260526

- timestamp: 2026-05-26T03:32:00+08:00
- scope: 推理宝典候选稿，三段论补大前提、三段论小项不当扩大、三段论有效性与前提真实性
- verdict: `BATCH_PASS_FINAL_STILL_BLOCKED`

## 本批处理条目

1. `2026东城期末 Q6`
   - 清理点：三段论补大前提、中项周延、四概念边界。
   - 正文修订：把程序化规则句改为“已知小前提 + 目标结论 + 缺一座能覆盖本题对象的桥”的学生触发链。
   - 错项补齐：A 不能由纯净无辐射推出绿色前景；C 的“有的”不能覆盖本题对象；D 引入生物成矿矿物，范围太散。
2. `2024朝阳二模 Q7`
   - 清理点：小项不当扩大、归纳推理能力扩张、必要条件误推。
   - 正文修订：把“娱乐工具”从谓项到结论全称主项的范围突变讲成学生可见触发点。
   - 错项补齐：A 小项不当扩大；B 学过概念不等于具备推出一般结论和新知识体系的能力；C 只满足必要条件的一边，不能推出关系判断能力。
3. `2024东城一模 Q7`
   - 清理点：演绎推理形式有效与前提真实性分层。
   - 正文修订：把“形式有效但大前提为假”改写为两层判断：先看结构，再看事实前提。
   - 错项补齐：③把形式有效误当结论必真；④把前提不真误判为四概念。

## 回源证据

- Source lock:
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/xuanbisan_logic_thinking_dual_handbooks_2026-05-24/02_codex_lane/B_ADDITIONS_BACKCHECK_Q0013_Q0017.md`
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/xuanbisan_logic_thinking_dual_handbooks_2026-05-24/02_codex_lane/GAP001_2024_CHAOYANG_ERMO_Q7_SOURCE_LOCK.md`
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/xuanbisan_logic_thinking_dual_handbooks_2026-05-24/02_codex_lane/GAP006_2024_DONGCHENG_YIMO_Q6_Q7_Q8_SOURCE_LOCK.md`
- Direct source excerpts:
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/gpt_sources/15664381470d8300_2026北京东城高三_上_期末政治_教师版.md:71-82` 锁定东城期末 Q6 题面与选项。
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/gpt_sources/e4d67789c91d1b92_2026东城期末细则.md:553-570` 与 `:595-596` 锁定东城期末 Q6=B 与错项解析。
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/gpt_sources/9223488a4b5e6f80_003202405朝阳高三二模政治试题.md:96-114` 锁定朝阳二模 Q7 题面与选项。
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/data/preprocessed_corpus/gpt_sources/f7c4cc4ac52ecefd_004202405朝阳高三政治质量检测二参考答案_以PDF为准.md:24-44` 锁定朝阳二模 Q7=D。
  - `/Users/wanglifei/GaokaoPolitics/beijing-politics-sync/reports/xuanbisan_logic_thinking_dual_handbooks_2026-05-24/02_codex_lane/GAP006_2024_DONGCHENG_YIMO_Q6_Q7_Q8_SOURCE_LOCK.md:35-54` 锁定东城一模 Q7=A 与本地逐项判定。

## 复测

- 推理候选稿 `候选稿门禁`: 27 -> 25。
- 推理候选稿 `本题规则要点是`: 47 -> 44。
- 推理候选稿 `看到题目把前提和结论组织成`: 21，未变。
- 推理候选稿 `再结合材料判断它属于`: 21，未变。

## 继续阻断

- 当前仍只是 Markdown 候选稿；没有生成 DOCX/PDF。
- 推理候选稿仍有 25 条 `候选稿门禁`，且仍有 44 条 `本题规则要点是` 程序化句式。
- 思维候选稿仍有 25 条 `候选稿门禁`。
- 真实 GPT Pro / Claude 对齐审查、Word/PDF 视觉 QA、Governor/Confucius 最终 artifact-only 验收均未完成。
