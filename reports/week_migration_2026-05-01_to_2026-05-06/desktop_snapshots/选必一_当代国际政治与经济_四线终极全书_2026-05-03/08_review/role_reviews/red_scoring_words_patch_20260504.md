# Red Scoring Words Patch - 2026-05-04 15:55 CST

## User Request

用户要求不只给答案句，还要标出“写出哪些词可以踩分”；并要求在六桶框架里也用红色标出踩分点。

## Patch Scope

- 不重跑证据母表，不提升新来源结论。
- 基于现有已审定的 `fusion/all_scoring_atoms_combined_20260504.csv` 与六桶融合结果，抽取每个条目的核心术语、细则原词和高信息量表述。
- 更新生成器，让每道主线题在 `本题踩分点汇总` 中显示：
  - 红色核心框架名；
  - `踩分词`；
  - 带红色关键词的 `卷面句`。
- 更新六桶总框架索引、每题 `本题命中框架`、条目 `框架落点`、术语积累复盘，全部显示红色核心踩分词。
- 更新 DOCX/PDF 生成器，使 Markdown 内联红色标记在 Word 和 PDF 中渲染为真实红色文字。
- 清理学生版不应出现的内部审计词，如 `非累计`、`替代表述`、`同一评分位置`、`同槽`、`fallback`。

## Local Governor Check

PASS.

- 47 道主线题均保留 `本题踩分点汇总`。
- 176 个条目链均保留 `材料触发`、`框架落点`、`踩分词`、`答题点自身积累`、`卷面答案句`。
- 六桶框架前台已标红核心踩分词。
- `2026海淀一模 Q20` 可见 `扩大制度型开放`、`推进制度型开放与国际标准规则共通`、`两个市场两种资源`。

## Confucius Artifact-Only Check

PASS.

从学生视角看，每题先读红色 `踩分词`，再看红色词如何嵌入 `卷面句` 和六桶框架，能区分“必须写出的术语/短语”和“把术语连成答案的句子”。

## Document QA

- Structure QA: PASS.
- Main training questions: 47.
- `本题踩分点汇总`: 47.
- `踩分词`: 352 in mainline structure count.
- Red scoring marks: 4219 in mainline QA count; 4647 total Markdown red spans.
- DOCX red runs: 4647.
- Markdown red span balance: 4647 open / 4647 close; nested red span: false.
- Forbidden-term scan: PASS.
- PDF pages after red scoring-word expansion: 135.
- QuickLook DOCX preview: `09_delivery/quicklook_after_red_scoring_words_docx/`.
- QuickLook PDF preview: `09_delivery/quicklook_after_red_scoring_words_pdf/`.

## Verdict

PASS_AFTER_RED_SCORING_WORDS_PATCH.
