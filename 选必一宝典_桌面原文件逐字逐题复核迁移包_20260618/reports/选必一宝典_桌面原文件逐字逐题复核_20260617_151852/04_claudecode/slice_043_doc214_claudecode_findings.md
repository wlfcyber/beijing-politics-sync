<!-- doc_order=214; returncode=0; duration_seconds=125.7; model=claude-opus-4-8; result_is_error=False; stop=end_turn; stream=slice_043_doc214_stream.jsonl; debug=slice_043_doc214_debug.log -->
## 总判定：NEEDS_FIX（单题轻微）with UQ0067 group hold

8 字段内容与题源/细则逐字基本吻合，主语、设问、6 分、四角度均可锁定；仅 **2523 答案落点多出"合法"二字**偏离源，需修；结构上仍缺独立硬规则字段（沿用 skeleton 标记）；同类项合并为书级待核，本 lane 不裁决。

---

**1. 术语/核心采分点 — PASS(content) / 结构待补**
core_point「利用规则维权角度」逐字对应 RUBRIC 180-181、EXAM 416。doc214 取四角度首条，符合 UQ0067 按 core_point 拆分。skeleton 标 STRUCTURE_NEEDS_FIX（缺独立硬规则字段）仍需补，但内容已由 source 锁定，状态建议升为 SOURCE_VERIFIED / STRUCTURE_PENDING。

**2. 完整设问 — PASS**
2521 vs EXAM 316-317 逐字一致（仅 PDF 空格差）。主语「中国汽车企业」、「（6 分）」均确认。Codex 关于 enterprise 主语 / 6 分 prompt 验证通过。

**3. 细则位置 — PASS(content) / 结构待补**
细则实存 RUBRIC 167-190；2525「答题层次」、2531「答题提醒」分别对应 RUBRIC 177-178 / 186 / 190。状态建议同字段 1。

**4. 来源 — PASS**
question_ref 2025西城期末Q20 ↔ SRC_EXAM / SRC_RUBRIC 之 Q20(2) 一致；PATH 注明 试卷.pdf / 细则.pdf。

**5. 材料触发 — PASS（可接受推断）**
2520 将反补贴税定性为贸易摩擦/壁垒，有 RUBRIC 188「克服贸易壁垒」支撑；「从国际规则/国际组织权利出发依法维权」与 doc214 角度一致，未引入政府/治理主语，满足 Codex 警戒。属解释性触发点而非材料原文，可保留。

**6. 答案句 — NEEDS_FIX（轻微）**
2523「积极维护自身合法权益」较源 EXAM 416 / RUBRIC 180-181「积极维护自身权益」多「合法」二字；「通过对话磋商」加连接词可接受。注 2526 作「自身权益」无误，故漂移仅在 2523。

**7. 同类项合并 — PASS with group hold**
2526-2530 四角度+其他逐条对应 RUBRIC 180-189，rubric typo 已修正（提高要素资源利用率 / 面向市场满足需求），列举完整。UQ0067 将同一小题拆为 doc_order 195/202/214（core_point 不同），是否合并属书级裁决 → group hold，本 lane 不判硬错。

**8. 模块边界 — PASS**
bucket 经济全球化 / 全球经济治理与规则权益；正文 2520-2523 全程企业主语，未越界到「政府全球治理」叙述，Codex 警戒满足。仅提示 sub_bucket 标签「全球经济治理」措辞偏治理向，建议书级核对标签语义；无 in-text 漂移，非硬错。

---

## Must-fix（本 doc_order 214）
- **[硬·轻微] 2523**：「自身合法权益」→「自身权益」，对齐 EXAM 416 / RUBRIC 180-181；或显式标注为转述。
- **[结构] 补独立「术语硬规则 / 细则位置」字段**（沿 skeleton）：内容已由 RUBRIC 167-190 锁定，可将该两字段状态由 `..._SOURCE_PENDING` 升为 `SOURCE_VERIFIED`，仅保留结构补写项。

## 边界声明
仅审 doc_order 214 / Q0214；不改写全文、不声称全书完成；不修改桌面 DOCX。UQ0067（195;202;214）合并系书级同类组，本 lane 仅标 **group hold**，不裁决拆/并。
