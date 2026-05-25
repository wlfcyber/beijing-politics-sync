# GAP008 Disjunctive Reasoning Source Lock

Status: `source_locked_after_claude_v3_pending_external_review`

Purpose: close the P0 gap that Q0022 only covered disjunctive-judgment omission, not standard disjunctive-reasoning forms.

## Q0027 2025海淀一模 Q21(1)

Evidence level: `A-formal`

Source:

- Paper: `gpt_sources/7ebce670784d805e_2025北京海淀高三一模政治_教师版.md:255-266`
- Rubric: `gpt_sources/506347bd4a7061dd_2025海淀一模细则.md:56-64`

Question prompt: 以“外贸进出口是拉动经济增长的重要引擎”为结论，写出一个正确的演绎推理。

Rubric-supported sample:

> 选言推理：外贸进出口要么影响国内大循环，要么是拉动经济增长的重要引擎。外贸进出口不影响国内大循环。所以，外贸进出口是拉动经济增长的重要引擎。

Reasoning form:

- Type: 不相容选言推理有效式
- Structure: `p xor q; not p; therefore q`
- Student rule: 如果题干或答案把两种可能处理成“要么……要么……”，否定其中一个选言支，就可以肯定另一个选言支。

## Q0028 2025丰台期末 Q9

Evidence level: `B-choice-signal`

Source:

- Paper and answer explanation: `gpt_sources/89765092a6f26242_2025北京丰台高三_上_期末政治_教师版.md:120-130,386-392`

Question focus: 某中学设计陕西、贵州、甘肃、湖南等研学路线，每个学生都选择了一条研学路线。选项 B 声称：由“小张或者去甘肃游学，或者去湖南游学”为真，能推出“小张去甘肃游学”为真。

Answer source says Q9 correct option is D, and explains B is wrong because the disjunctive judgment only supports either “甘肃且非湖南” or “非甘肃且湖南”; it cannot directly identify the 甘肃支 as true.

Reasoning form:

- Type: 不相容选言推理无效式陷阱
- Structure: `p xor q is true; therefore p`
- Student rule: 只知道不相容选言判断为真，只能知道两个选言支有且只有一个为真，不能直接指定哪一个为真。

## Candidate Notes

- 2025顺义一模 Q17(1) contains a useful 相容选言判断 condition in the rubric, but the main task is three judgments being true at once. It is a support index, not the primary GAP008 standard-form sample.
- 2025朝阳期末 Q5 contains a useful “或者……为假 -> 既不……也不……” item, but the current cache did not expose a matched answer explanation, so it is not promoted here.

## Gate Decision

GAP008 can move from `open` to `closed_source_locked_pending_external_review`: the current run now has one A-formal valid disjunctive-reasoning sample and one B-choice-signal invalid-trap sample. It is still not release-ready until GPT Pro and Claude V4 review these additions.
