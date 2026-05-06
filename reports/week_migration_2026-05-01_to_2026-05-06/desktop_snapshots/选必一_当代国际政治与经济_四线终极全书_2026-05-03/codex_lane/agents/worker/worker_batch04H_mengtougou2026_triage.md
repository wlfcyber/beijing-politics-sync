# Worker Triage - Batch04H 2026门头沟一模

time: 2026-05-03 22:58 CST
scope: 2026门头沟一模 Q20; Q21 boundary check
student_doc_touched: no
cross_thread_guard: active

## Verdict

Promote `2026门头沟一模 Q20` to prelim fusion.

Keep `2026门头沟一模 Q21` as `boundary_only_expression_accumulation` for now. It has a formal scoring source, but the scoring is a composite level-scored argument question. Its 当代国际政治与经济 chunk is 4 points with examples such as `大国担当`、`互利共赢的开放战略`、`构建人类命运共同体`; it is useful for expression accumulation but not stable enough to become independent frequency atoms without further Governor permission.

## Evidence

- P0 scoring source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026门头沟一模/细则/细则.docx`.
- P3 paper source: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026门头沟一模/试卷/试卷.pdf`.
- The paper prompt for Q20 asks: `结合材料，运用《当代国际政治与经济》知识，分析海南自贸港全岛封关为何能为中国经济发展注入新动能、为世界经济开放发展注入新活力。`

## Q20 Scoring Structure

| component | scoring structure | decision |
|---|---|---|
| 原因 | `对外开放基本国策`、`互利共赢战略`、`经济全球化`、`高水平对外开放`等术语综合阐释，2分 | promote as theory/cause atom |
| 中国意义 | 从材料提取封关运作对中国经济新动能的作用；四选二得2分 | promote as China-side material trigger family |
| 世界意义 | 从材料提取封关运作对世界经济开放发展的作用；四选二得2分 | promote as world-side economic globalization family |
| 逻辑 | 表述清晰、分角度、逻辑连贯，1分 | keep as answer-structure warning, not a knowledge atom |

## Q20 Required Guards

- If only the China side or only the world side is answered, the scoring source caps the answer at 4.
- If the answer only recites textbook theory and does not connect to Hainan Free Trade Port closure, the scoring source caps the answer at 5.
- Keep high-information expressions: `高水平制度型开放`、`贸易自由化便利化`、`开放型世界经济`、`国内国际双循环`、`国内国际两种市场两种资源联动`.
- Do not reduce `开放型世界经济` to generic `经济全球化正确方向`; the full expression must remain visible.
