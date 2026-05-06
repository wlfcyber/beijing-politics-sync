# 制度型开放前台可见性补丁验收

time: 2026-05-04 15:31 CST
status: PASS
scope: 2026海淀一模 Q20 与六桶框架中 `制度型开放` 的学生前台可见性

## Trigger

用户指出：`2026海淀一模` 中 `制度型开放` 是重要且反复出现的细则词，但在最终框架里不容易看到。

## Local Evidence Check

- `SOURCE_LEDGER.csv` 已记录 2026海淀一模 Q20 抽到 `制度型开放、两个市场两种资源、全球经济治理规则制定`。
- 教师核查索引已有 2026海淀一模 Q20 两条主线：
  - `充分利用国内国际两个市场、两种资源，增强国内国际循环联动`
  - `建设开放型世界经济，参与全球经济治理和规则制定`
- 最终学生稿原本已在 2026海淀一模 Q20 的答案句与表述积累中写入 `扩大制度型开放 / 推进制度型开放`，但六桶总框架的前台核心名没有直接显示该高频细则词。

## Governor Decision

Verdict: PASS_AFTER_PATCH.

这是学生前台可见性问题，不是源证据缺失。处理原则：

- 不把 `制度型开放` 拆成孤立新桶，避免同核心重复。
- 不改教师索引和底层证据等级。
- 在学生前台显性保留高信息量细则词，让学生能在框架索引和题内闭环中看到它。

## Patch Applied

- 六桶总框架索引：
  - `建设开放型世界经济，参与全球经济治理和规则制定` 后新增可见说明：`含制度型开放 / 对标国际规则、规制、管理和标准`。
  - `充分利用国内国际两个市场、两种资源，增强国内国际循环联动` 后新增可见说明：`2026海淀一模等题会写成“扩大制度型开放 + 两个市场两种资源”`。
- 2026海淀一模 Q20 题内显示：
  - `扩大制度型开放；更好利用国内国际两个市场、两种资源，增强国内国际循环联动`
  - `参与全球经济治理和规则制定；推进制度型开放与国际标准规则共通`
- 六桶术语积累复盘新增 `常见抓手` 行，避免学生只看到抽象核心名。

## Confucius Artifact-Only Check

Verdict: PASS.

聪明但零基础学生现在可以在三处直接看到 `制度型开放`：

- 首页六桶框架索引的经济全球化部分。
- 2026海淀一模 Q20 的本题命中框架和条目拆解。
- 六桶术语积累复盘的 `常见抓手` 与 `答题点自身积累`。

## QA

- Markdown/DOCX/PDF regenerated: PASS.
- `document_generation_qa_最终闭环版_20260504.md`: 47 main training questions, 176 item chains, 177 answer variants, PDF 103 pages, forbidden-term scan PASS.
- DOCX text extraction confirms `扩大制度型开放`, `推进制度型开放与国际标准规则共通`, `常见抓手`, and `制度型开放 / 对标国际规则`.
- PDF text extraction confirms the same key strings.
- DOCX QuickLook fallback: `09_delivery/quicklook_after_institutional_opening_patch_docx/`.
- PDF QuickLook fallback: `09_delivery/quicklook_after_institutional_opening_patch_pdf/`.
- `render_docx.py`: not run as PASS because `soffice` is still not installed.

## External Model Note

No new GPT/Claude call was made for this narrow patch because it does not add scoring evidence or alter source adjudication; it only makes an already-audited rubric term visible in the student-facing framework. Local Governor and Confucius are sufficient for this bounded repair.
