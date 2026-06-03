# V52 Source-Backed Rehang Audit

timestamp: `2026-05-27T02:03:00+08:00`

verdict: `SOURCE_BACKED_REHANG_NOT_FINAL`

## Why V52 Exists

V51 correctly removed self-created framework nodes such as `方法更新` and `整体安排`, but it also over-retreated by withdrawing several source-backed multi-angle entries. V52 keeps the user's PDF framework as the only structure, then rehangs only entries supported by source materials or marking guidance.

## Fixed Framework Boundary

Thinking handbook H2 whitelist remains:

- Scientific thinking: `追求认识的客观性 / 结果具有预见性 / 结果具有可检验性`
- Dialectical thinking: `整体性 / 动态性 / 分析与综合 / 矛盾分析法 / 量变与质变 / 适度原则 / 辩证否定 / 认识发展历程`
- Innovative thinking: `特点与三新 / 联想思维 / 发散思维与聚合思维 / 逆向思维 / 超前思维`

V52 does not restore any of these forbidden or construction-stage nodes:

- `方法更新`
- `整体安排`
- `科学思维的综合运用`
- `辩证思维的综合运用`
- `整体性与系统观念`
- `动态性与质量互变`
- `改变条件与建立新联系`
- `特征与三新`

## Source-Backed Rehang Decisions

### 2025西城一模 第17题

Rehung to:

- `整体性`
- `特点与三新`

Basis:

- Source paper: `data/preprocessed_corpus/gpt_sources/2542f29bb04e2ae0_2025北京西城高三一模政治_教师版.md`
- Rubric: `data/preprocessed_corpus/gpt_sources/af675a5d751f41db_2025西城一模细则.md`
- Source content includes multi-element ecological construction: water forms, fish/insects/birds, absence of ordinary recreation facilities, river islands, deep pools and shallow beaches, retained farmland for birds and animals, and core-zone closure.
- Rubric gives dialectical thinking through connection/development/comprehensive view and overall planning, plus innovative thinking through new thinking, new method, new result or reverse thinking.

Decision:

- Keep `整体性`: the material connects water, farmland, wild space, closure, and ecological restoration as a functional whole.
- Keep `特点与三新`: the material shows new thinking, method, and result in park construction.
- Do not create `整体安排`.

### 2025门头沟一模 第21题第（1）问

Rehung to:

- `辩证否定`
- `超前思维`

Basis:

- Source paper: `data/preprocessed_corpus/gpt_sources/1d8a23fe11f59810_2025北京门头沟高三一模政治_教师版.md`
- Rubric: `data/preprocessed_corpus/gpt_sources/26d9b228064053c1_2025门头沟一模细则.md`
- Source content contrasts a thousand-year coal city with AI, computing power, algorithm service, large models, digital audiovisual industries, medicine, ecological resources, and integrated culture-tourism-agriculture development.
- Rubric permits dialectical negation, overallity/dynamicity, analysis and synthesis, comprehensive connection/development, and innovative methods such as association, divergent thinking, or advanced thinking.

Decision:

- Keep `辩证否定`: the material is not simple abandonment of the old coal city, but transformation and sublation of old foundations into new momentum.
- Keep `超前思维`: the material uses present constraints and future industrial trends to anticipate a new development direction.
- Do not place it under self-made `科学思维综合` nodes.

### 2025石景山一模 第19题

Rehung to:

- `特点与三新`

Basis:

- Source paper: `data/preprocessed_corpus/gpt_sources/fb8717be46dabe77_2025北京石景山高三一模政治_教师版.md`
- Rubric: `data/preprocessed_corpus/gpt_sources/0b97375f2f69e53d_2025石景山一模细则.md`
- Source content explicitly contains inspiration, creativity, imaginative ideas, urban construction collision, and novel suggestions.
- Rubric includes innovative thinking ability through inspiration and novel unique suggestions.

Decision:

- Keep `特点与三新`: the entry is not only scientific thinking three properties; it also has a source-backed innovative-thinking trigger.

### 2024丰台一模 第19题第（2）问

Rehung to:

- `发散思维与聚合思维`

Basis:

- Source/rubric: `data/preprocessed_corpus/gpt_sources/950d6b2d3cdda441_2024丰台一模细则.md`
- The question asks students to supplement research methods for a simulated CPPCC proposal on garbage classification signs.
- Acceptable methods include brainstorming, questionnaire, and interview; the solving chain can move from divergent collection of methods and information to convergent proposal formation.

Decision:

- Keep `发散思维与聚合思维`.
- Do not create `方法更新`.

### 2024丰台二模 第18题第（2）问

Rehung to:

- `矛盾分析法`

Basis:

- Source/rubric: `data/preprocessed_corpus/gpt_sources/71fcaa9e66afc5db_2024丰台二模细则.md`
- The evaluation must see both advantages/opportunities and weaknesses/shortcomings in ice-snow economic development.

Decision:

- Keep `矛盾分析法`: the material asks for a balanced evaluation of opportunities and constraints.
- Do not blend this entry with generic prevision or construction-style comprehensive nodes.

## QA Snapshot

- Thinking handbook: 82 entries, each with `材料触发点 / 设问 / 为什么能想到 / 答案落点`.
- Reasoning handbook: 83 entries, each with the same four-title structure.
- Thinking PDF: 33 pages.
- Reasoning PDF: 49 pages.
- Forbidden framework scan: no hits for `方法更新 / 整体安排 / 科学思维的综合运用 / 辩证思维的综合运用 / 整体性与系统观念 / 动态性与质量互变 / 改变条件 / 建立新联系 / 特征与三新`.
- Student-front text scan: no hits for `细则 / 参考答案 / 正式细则 / 评阅 / source-lock / A-formal / body_thinking / body_reasoning`.

## Remaining Blockers

V52 is fit for user content review, but it is not final:

- GPT Pro real review remains pending.
- Claude PASS remains pending.
- Fresh-context Confucius remains pending.
- Full question-by-question source recheck is not complete.
