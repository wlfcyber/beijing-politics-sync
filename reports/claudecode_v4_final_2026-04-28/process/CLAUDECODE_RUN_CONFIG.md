# Claude Code v4 run config

- model: `claude-opus-4-7`
- effort: `max`
- note: CLI does not accept bare `opus4.7`; full model id is used.
- previous Sonnet partial outputs archived under `archive_sonnet_interrupted_*`.

## 2026-04-27 用户改正已传达

- Claude Code prompt 已加入学生触发链硬规则：trigger_logic 必须解释材料词句如何触发原理，不能写“细则提到所以入框架”。
- 学生终稿与审计证据分离：行号、路径、slide、entry id 只留审计版。
- 2026-04-27 追加刚性规则：终稿里的主观题设问必须抄全；材料只摘与触发相关的重点句。
- 2026-04-27 追加刚性规则：原理方法论必须回应设问，trigger_logic 要写成“材料触发点 -> 原理方法论 -> 回答设问”。
- 2026-04-27 追加刚性规则：回应设问必须写成具体“答案落点”，不能写“要回应设问/服务题目/转化为做法”这种空话。
- 后续从 S018 继续，模型 claude-opus-4-7，effort=max。
- 规则文件：outputs_v4/CLAUDECODE_USER_CORRECTIONS_20260427.md
