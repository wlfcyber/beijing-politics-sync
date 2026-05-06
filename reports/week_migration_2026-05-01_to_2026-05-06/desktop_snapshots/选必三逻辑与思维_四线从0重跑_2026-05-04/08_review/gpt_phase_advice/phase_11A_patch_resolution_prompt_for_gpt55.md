# Phase11A Patch-Resolution Check For GPT-5.5 Pro

You previously returned `MUST_FIX_PHASE11A_CONTENT_NO_EXPANSION`. Codex A has patched the exact must-fix and the should/optional transfer fixes, with no expansion. Claude/ClaudeCode remain suspended by user membership constraint; please do not require those lanes here.

Please return exactly one verdict:

1. `GO_PHASE11B_CONTROLLED_EXPANSION_NO_WORD_NO_FINAL` if the must-fix is closed and controlled expansion/source repair may begin.
2. `MUST_FIX_PHASE11A_PATCH_STILL_OPEN` if any patch is still wrong.
3. `HOLD_NEEDS_SOURCE_REPAIR_BEFORE_PHASE11B` if you need a concrete source check before controlled expansion.

Do not authorize Word/PDF/final PASS/终稿/宝典成品.

## Patch Resolution

```md
# Phase11A Content Patch Resolution

Status: `PATCHED_AFTER_GPT_MUST_FIX_NO_EXPANSION`

## GPT Verdict

- GPT verdict: `MUST_FIX_PHASE11A_CONTENT_NO_EXPANSION`
- Raw reply: `08_review/gpt_phase_advice/phase_11A_gpt55_raw.md`

## Patch Resolution

- Replace student-facing `路径` with `链条` in Q-2026通州期末-19-2 to satisfy strict internal-term scan without changing knowledge content.
- Normalize Q-2026顺义一模-19-2 primary thinking line by adding `可写思维/方法` and `为什么能想到` fields from its existing material/action content; no new source claim.
- GPT must-fix: correct Q-2025丰台期末-8 so 形象思维 depends on 感性形象 and 概念 is only abstract thinking's basic unit.
- GPT optional transfer patch: add answer-length control to Q-2024海淀二模-17(1).
- GPT optional transfer patch: add weak-student explanation to Q-2024海淀二模-17(2).
- GPT should-fix: mark Q-2024西城一模-19(5) as a 综合方法链/超前思维链, not a formal logic type.
- GPT should-fix: state Q-2024西城一模-19(5) is not a formal logic positive example.
- GPT should-fix: remove 联言判断 from Q-2024朝阳二模-19(1) type name and leave it to Q19(2).

## Recheck

- reviewed_rows: 29
- PASS rows: 29
- REVIEW rows: 0
- FAIL rows: 0
- post_patch_internal_term_hits: 0
- same_type_accidental_expansions: 0
- hard_lock_failure: False
- expansion: none
- Word/PDF/final: still forbidden
- Claude/ClaudeCode: still suspended by user membership constraint

```

## Local Recheck

```md
# Phase11A Codex Local Verification

Verdict: `PASS_CODEX_PHASE11A_29ROW_CONTENT_REVIEW_NO_EXPANSION`

- control rows: 29
- review rows: 29
- patched body: `09_student_draft/phase11A_student_body_REVIEW_ONLY.md`
- post-patch internal term hits: 0
- same-type accidental expansions: 0
- hard-lock failure: False
- Claude/ClaudeCode: suspended by user membership constraint.
- Word/PDF/final: still forbidden.

```

## Patched Sections Only

```md
### 2024 海淀二模第17题第(1)问（主观题）

- 材料信号：全国时间利用调查围绕个人生理必需活动、有酬劳动、无酬劳动、个人自由支配活动等多类时间投入，目的是全面、真实、准确反映居民生活质量与生活模式。
- 可写思维/方法：科学思维、辩证思维、创新思维三角度并列；具体可调用客观性、整体性、发散与聚合、超前思维以及思维抽象/思维具体/感性具体。
- 为什么能想到：本题要求从三个角度分别展开，科学思维对应客观性与预见性，创新思维对应“三新”与发散聚合、超前，辩证思维对应整体性与分析综合；每一角度都要落到时间利用调查的具体动作上。
- 答题动作：按三个角度拆开：科学思维看客观性、预见性；创新思维看“三新”、发散聚合、超前；辩证思维看整体性、分析综合；每个角度都必须结合材料分析。
- 答案落点：逐角度一句话作答，每条带“调查内容/调查动作 + 思维方法 + 作用结论”。每个角度至少写一组“材料动作 + 思维方法 + 作用结论”，不要只列方法名。
- 易错陷阱：只列知识点而不结合材料，只能停留在浅层作答；混淆角度归属(把“整体性”写到科学思维下、把“客观性”写到创新思维下)会丢分。
- 同类题索引：2024 朝阳二模第7题；2024 朝阳期中第19题；2024 海淀二模第17题第(2)问；2025 海淀期末第17题第(1)问；2026 顺义一模第19题第(1)问；2026 顺义一模第19题第(2)问。

### 2024 海淀二模第17题第(2)问（主观题）

- 材料信号：同一调查的两阶段任务——“调查了解居民时间利用情况”对应感性具体阶段；“分析研究居民时间利用情况”对应思维抽象再到思维具体阶段。
- 可写思维/方法：科学思维(认识论维度)；感性具体、思维抽象、思维具体三层。
- 为什么能想到：题目把“调查了解”和“分析研究”区分开，正是“杂多现象→抽出核心概念→回到完整整体图景”链条；严禁把方向写反。
- 答题动作：调查了解对应感性具体；分析研究对应思维抽象和思维具体；两阶段相互依赖、不可割裂。先拿到杂多表象，再抽出本质联系，最后回到完整认识。
- 答案落点：按“调查了解→感性具体→获得对象的整体表象；分析研究→思维抽象抓住本质→思维具体重建完整图景；两阶段相互依赖共同形成科学认识”作答。
- 易错陷阱：把感性具体和思维具体的方向颠倒不给分；用“实践决定认识”替代具体环节只能作补充，不能代替三环节本身。
- 同类题索引：2024 朝阳二模第7题；2024 朝阳期中第19题；2024 海淀二模第17题第(1)问；2025 海淀期末第17题第(1)问；2026 顺义一模第19题第(1)问；2026 顺义一模第19题第(2)问。

### 2025 丰台期末第8题（选择题）(现代诗解读)

- 材料信号：《和平是一棵树》以白天鹅翅膀、湖水云影、门、红酒、灯等多个具体形象层层展开，从不同方向表达对和平的向往。
- 可写思维/方法：发散思维 + 形象思维。
- 为什么能想到：多个具体意象向同一主题“和平”发散，正是发散思维；以白天鹅翅膀、门、红酒等具体形象触及和平本质，正是形象思维。
- 答题动作：选 D，②④。②运用发散思维表达人们对和平的向往与追求；④以形象思维触及和平的本质特征。
- 答案落点：选 D，②④。诗歌从多个意象发散表达，并以具体形象触及和平本质。
- 易错陷阱：①错在把“想象”当作形象思维的基本单元；形象思维依托感性形象，抽象思维的基本单元才是概念。③错在把本诗当作抽象思维；本诗主要通过具体意象展开，不属于抽象思维。
- 同类题索引：2026 顺义一模第5题。

### 2024 西城一模第19题第(5)问（主观题）

- 题型：综合方法链 / 超前思维链(调研实践 + 因果分析 + 矛盾分析 + 推理想象 + 超前思维)。
- 逻辑形式：这不是形式逻辑题型正例，而是由实践→因果规律→矛盾分析→由过去现在推未来→超前思维的综合方法链。
- 规则口诀：以实践为导向调研 → 把握状况因果规律 → 善用矛盾分析(内在矛盾/外在矛盾) → 运用推理与想象由过去现在推未来 → 超前思维。
- 有效式或错误式：整体框架按“调研→因果→矛盾→推理想象→超前”顺序展开；可补充强调实践基础、超前思维和内外矛盾。
- 解题动作：① 立足实践调研当前状况；② 把握因果规律；③ 拆内外矛盾；④ 用推理与想象由过去/现在推未来；⑤ 用超前思维做前瞻判断。
- 答案落点：每条带“环节 + 材料事实 + 作用结论”，最后落到超前思维的前瞻判断。
- 易错陷阱：只罗列概念无材料分析丢分；漏“实践”基础扣分。
- 同类题索引：2024 西城一模第19题第(2)问；2024 西城一模第19题第(3)问。

### 2024 朝阳二模第19题第(1)问（主观题）

#### 主讲线：推理结构
- 题型：填空组合题，第一空考辩证思维动态性，第二空考类比推理。联言判断留到第(2)问，不在第(1)问题型名中出现。
- 逻辑形式：第一空考辩证思维动态性，第二空考类比推理。
- 规则口诀：动态性=用变化发展观点看问题；类比推理=由两类对象在某些属性上相同，推出在另外的属性上也相同。
- 有效式或错误式：第一空写“动态性”；第二空必须写“类比推理”，不要改写成相近词。
- 解题动作：看到“生生不息、日新、革新、不断充实”，第一空锁定动态性；看到由一个对象经验迁移到另一个对象，第二空锁定类比推理。
- 答案落点：第一空写“动态性”，第二空写“类比推理”。
- 易错陷阱：第一空填“整体性/质量互变”丢分；第二空把“类比”改写为其他词不给分。

#### 辅助线：思维方法
- 题型：辩证思维 · 动态性。
- 材料信号：中华文明“生生不息”“日新”“革新”“不断充实”等表述呈现持续变化与革新。
- 答题动作：用“变化发展观点看问题”理解中华优秀传统文化的革新性。
- 易错陷阱：误填整体性、质量互变、矛盾运动等丢分。
- 同类题索引：2024 朝阳二模第19题第(2)问。
```
