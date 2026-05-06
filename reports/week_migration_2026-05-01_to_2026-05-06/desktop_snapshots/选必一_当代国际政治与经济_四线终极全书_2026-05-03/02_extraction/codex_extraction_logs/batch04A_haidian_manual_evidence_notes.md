# Batch04A Haidian Manual Evidence Notes

time: 2026-05-03 20:52 CST

Scope: uncovered Haidian suites from original 2024-2026 source roots, after the mechanical term scan. This is source triage only; it does not promote student final entries.

## Candidate Rows To Add To Coverage

### 2024海淀一模 Q18(1)

- source: `/Users/wanglifei/Desktop/2024模拟题/2024海淀一模/细则/细则.docx`
- source level: direct scoring-answer file with detailed replacement table; usable as high-confidence source after Patcher/Governor review.
- prompt: 便利中外人员往来，服务高水平对外开放；预测举措对服务高水平对外开放的积极影响。
- candidate terms:
  - 促进贸易投资便利化、自由化。
  - 吸引全球资源要素自由流动。
  - 充分利用国际国内两种资源、两个市场。
  - 推进高水平对外开放，发展更高水平开放型经济。
  - table variant: 开放、包容、普惠、共赢 / 互利共赢 / 国内国际双循环.
- boundary: Q17 also has a loose `推进高水平对外开放` phrase, but Q18(1) is the direct 选必一 answer chain.

### 2024海淀二模 Q18(1)

- source: `/Users/wanglifei/Desktop/2024模拟题/海淀二模/细则/细则.docx`
- source level: answer appears inside scoring/answer file, but Q18(1) has only broad answer angles and no detailed scoring subpoints in extracted text.
- prompt: 民主是人类文明发展进步的重要标志，是全人类共同价值；任选议题，运用《当代国际政治与经济》写时政述评。
- candidate terms:
  - 时代主题。
  - 世界多极化。
  - 人类命运共同体。
  - 国际组织。
- boundary: open commentary task. Treat as transfer/open-question material, not strict high-frequency scoring atom unless later visual review finds detailed rubric.

### 2025海淀一模 Q21(2)

- source: `/Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025海淀一模/试卷/试卷.pdf`
- source level: reference answer in paper extraction plus marking-warning file; not a full scoring rubric.
- prompt: 外贸进出口是拉动经济增长的重要引擎。
- candidate terms:
  - 实施更加积极主动的开放战略。
  - 以政策促进贸易自由化便利化。
  - 综合保税区降低贸易成本，畅通国际贸易。
  - 发展绿色贸易、数字贸易，推动货物贸易优化升级。
  - 依托超大规模市场优势，为世界各国提供更广阔市场，促进国际合作，实现互利共赢。
- boundary: `2025海淀一模/细则/细则.docx` mainly提供学生问题提醒：不要学科观点堆砌政治多极化、独立自主等。 It does not by itself promote those wrong directions.

### 2026海淀一模 Q20

- source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026海淀一模/细则/细则.pdf`
- source level: structured answer in scoring/answer PDF; paper PDF text extraction was empty, then Codex rendered and visually checked paper page 7 in this run.
- prompt: 国际标准是全球产业界的“通用语言”；中国标准走出国门，融入全球产业发展体系，中国与世界深度互动、共享发展。设问为：结合材料，运用《当代国际政治与经济》知识，谈谈中国标准走出国门的意义。
- candidate terms:
  - 扩大制度型开放。
  - 增强我国产品、服务乃至产业链在全球的竞争力。
  - 推进高水平对外开放。
  - 更好利用国内国际两个市场、两种资源。
  - 参与全球经济治理和规则制定，推动全球治理体制向更加公正合理方向发展。
- visual file: `02_extraction/screenshots/batch04A_2026海淀一模_Q20_paper/page_07.png`
- boundary: paper prompt visual check is now done; still not closed until Worker/Patcher/Governor process this into entries.

### 2026海淀期中 Q22

- source: `/Users/wanglifei/Desktop/2026模拟题/2026各区期末和期中/2026海淀期中/试卷/试卷.docx`
- source level: paper/answer document only; no formal scoring source located in this pass.
- prompt: 全球治理倡议。
- candidate terms:
  - 顺应和平与发展的时代潮流。
  - 奉行主权平等、遵守国际法治、践行多边主义、倡导以人为本、注重行动导向。
  - 捍卫联合国宪章宗旨和原则。
  - 共商共建共享的全球治理观。
  - 推动建设更加公正合理的全球治理体系。
- boundary: reference-only until formal scoring/rubric source is located. If none exists, it may serve as transfer example, not frequency proof.

## Naming Conflict Note

The `2024海淀期中` source under the 2024 root appears to overlap the already-covered `2025海淀期中` row in the current matrix. It should not be double-counted until suite naming is reconciled. The original PDF source is useful for source-strength support and student-error notes, not a separate new row yet.
