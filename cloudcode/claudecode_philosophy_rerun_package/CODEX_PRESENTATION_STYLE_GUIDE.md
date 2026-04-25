# Codex Philosophy Framework Presentation Style Guide

Claude Code must preserve this presentation style when rerunning the philosophy framework.

## Template Source

Use this file as the structural and stylistic mother draft:

`C:\Users\Administrator\.codex\skills\feige-politics-garden\assets\current-artifacts\必修四哲学材料-知识触发总框架_持续更新版_v2.md`

The rerun may correct, verify, add, move, or mark boundaries, but it must not replace this format with a new handbook style.

## Required Top-Level Shape

Keep these sections in this order:

1. Title and metadata
   - title
   - last update
   - purpose
   - framework source
2. 使用规则
3. 已纳入试卷
4. 课件总框架（便于后续增量更新时对齐）
5. 触发总表
6. 附录：套卷级三线闭环记录
7. 覆盖矩阵与证据边界

## Required Entry Format

Every framework entry must use this source-grounded format:

```markdown
1. **来源**：<年份北京区名考试阶段> 第<题号>（`<评分细则/阅卷报告/讲评/已确认来源文件>`）
   - 材料信息：<只写题目材料中真实出现的信息，不写泛泛背景>
   - 触发知识：<哲学原理/方法论/必要的跨模块边界>
   - 逻辑链：<材料信息为什么触发这个知识点；必须能解释从材料到评分点的传导>
```

Do not replace this with:

- `核心判断`
- `当材料里出现`
- `答题路径`
- generic textbook summaries
- broad lists of keywords without source entries

Those can appear only in a short appendix if useful, not as the main framework.

## Required Module Order

Keep the user's framework order:

1. 唯物论
2. 辩证法
3. 认识论
4. 历史唯物主义
5. 价值观 / 人生观

Within each module, keep existing knowledge-point headings where possible. Add new headings only when evidence does not fit any existing heading.

## What "Rerun" Means

Rerun means:

- re-check source coverage using the cache and raw files when needed,
- verify whether old entries are still evidence-supported,
- add omitted entries,
- move entries to better framework nodes when evidence requires,
- add boundary notes for non-philosophy or cross-module items,
- preserve source suite and question number.

Rerun does not mean:

- rewrite the whole document into a polished but less traceable guide,
- compress many source entries into three examples,
- remove old valid source-grounded findings,
- change the user's framework into a generic textbook outline,
- use ordinary reference answers as scoring rubrics.

## Word Rendering Style

When converting to Word:

- Keep the same logical sections and entry labels.
- Use heading levels that mirror the Markdown hierarchy.
- Use numbered source entries under each knowledge point.
- Use bold labels for `来源`、`材料信息`、`触发知识`、`逻辑链`.
- Avoid wide tables for dense Chinese content.
- Put coverage matrices and long suite-level logs in appendices.
- Render and inspect the DOCX before final delivery.
