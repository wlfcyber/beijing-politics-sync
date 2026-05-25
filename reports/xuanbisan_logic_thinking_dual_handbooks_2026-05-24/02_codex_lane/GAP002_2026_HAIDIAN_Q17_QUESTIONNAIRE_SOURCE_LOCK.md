# GAP002 Source Lock: 2026海淀一模 Q17 问卷原文

Status: `closed_source_locked_pending_external_review`

This file closes GAP002 / BLK-005 at the local source-evidence level. It does not close GPT Pro, Claude V4, Governor, Confucius, or final delivery gates.

## Source

- paper: `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026海淀一模\试卷\2026海淀一模 试卷扫描版_去水印.pdf`
- rendered page: `C:\Users\Administrator\Desktop\beijing_politics_research\data\preprocessed_corpus\renders\03e0412bb80579d8\page_005.png`
- rubric: `gpt_sources/9b5ac8fd0cfe59cb_2026海淀一模细则.md:35-66`

The paper cache has no reliable text layer, so this lock is based on the rendered page image plus the paired scoring standard.

## Paper Text Locked From Rendered Page

17.（6分）

调查研究要讲求科学方法。某校“模拟政协”社团同学准备围绕本市无障碍环境建设情况展开调研。以下是同学们设计的调查问卷（节选）。

调查问卷（节选）

问题1. 您的身份（单选）：

- 老年人（60岁及以上）
- 残障人士
- 儿童（14岁以下）
- 普通在职职工
- 离退休人员
- 相关行业从业者（如城市管理、物业等）
- 其他______

问题2. 您认为本市无障碍设施存在的主要问题是（可多选）：

- 设计不合理
- 标识不清
- 相关部门维护不到位

设问：

运用《逻辑与思维》知识，指出上述调查问卷中的逻辑错误。（2分）为提高调研活动的科学性，提出具体可行的建议。（4分）

## Rubric Match

The paired scoring standard says the logical errors are:

- 划分标准不一
- 选言判断遗漏其他有选择价值的其他情况

The second task can use scientific thinking, logical-thinking rules, dialectical thinking, or innovative thinking, with two concrete matched suggestions for 4 points.

## Local Decision

Q0022 can now be taught with full questionnaire detail:

- Problem 1 mixes different classification standards in one single-choice identity list: age group, disability status, employment status, retirement status, industry role, and other. This supports “划分标准不一”.
- Problem 2 gives only three preset reasons and no “其他/补充说明” option, so the listed alternatives do not cover other valuable possibilities. This supports “选言判断遗漏”.

Teaching boundary:

- Q0022 is not a standard disjunctive-reasoning valid/invalid form. It is a questionnaire-design case about concept division and completeness of alternatives.
- Q0027/Q0028 remain the current samples for standard disjunctive reasoning.

## Files To Sync

- `01_source_inventory/COVERAGE_GAP.csv`: GAP002 -> `closed_source_locked_pending_external_review`
- `04_fusion/REASONING_BAODIAN_V2_BODY_DRAFT.md`: §10 includes the full questionnaire detail.
- `02_codex_lane/REASONING_FORM_LEDGER.csv`: RF0017/RF0018 logical structures are narrowed to the paper text.
- `10_packets/GPTPRO_REVIEW_PACKET_V7.md`: current GPT Pro packet supersedes V6.
