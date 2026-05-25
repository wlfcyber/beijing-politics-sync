# GAP005/GAP006 V87 Suite Catch-up Source Lock

Status: `local_source_locked_pending_external_review`

Purpose: convert V86 suite-level zero-coverage findings into auditable local evidence rows where the current cache actually contains explicit 选必三 reasoning tasks. This file does not count as GPT Pro review, Claude review, final Governor pass, final Confucius pass, or student-facing release permission.

## Added Rows

- `Q0141` 2024东城二模 Q17(2): 科学归纳推理/求异法 + 类比推理.
- `Q0142` 2025东城二模 Q18(2): 充分条件假言推理前提真假辨析.
- `Q0143` 2025西城期末 Q17(2): 三段论构建.

## q0141-2024-dongcheng-ermo-q17-2

- Part: 推理宝典
- Framework node: 科学归纳推理 -> 求异法; 类比推理
- Evidence level: `A-formal`
- Status: `source_locked_suite_identity_conflict_pending_external_review`
- Source:
  - `gpt_sources/72fd64a3dddd2c89_17-2.md:22-39`
  - `gpt_sources/72fd64a3dddd2c89_17-2.md:44-49`

### Locked Prompt

The scoring file states that the item asks students to answer from the perspective of 推理 and explain how the scientific team found the crop alkali-tolerance "password".

### Trigger Chain

- The team compares genetic condition differences and tolerance results -> scientific induction and causal inquiry.
- The scoring rule accepts 求异法, 求同法, or 共变法 where the material analysis is matched; the stable local entry uses 求异法 because the file's reference answer foregrounds it.
- The team compares 高粱 AT1 and 水稻 GS3 by similar attributes -> 类比推理.

### Identity Guard

The source ledger path is under `2024东城二模\细则\2024东城二模细则\17题\17-2.docx`, but the extracted internal header says `一模`. Therefore the content is locally source-locked, while the suite identity is not allowed to become a final release claim without external verification.

## q0142-2025-dongcheng-ermo-q18-2

- Part: 推理宝典
- Framework node: 充分条件假言推理 -> 肯定前件式 / 前提真假
- Evidence level: `A-formal`
- Status: `source_locked_pending_external_review`
- Sources:
  - paper: `gpt_sources/9b287871f660f23d_2025北京东城高三二模政治_教师版.md:184-187`
  - teacher answer: `gpt_sources/9b287871f660f23d_2025北京东城高三二模政治_教师版.md:276-278`
  - rubric: `gpt_sources/606dbae1d5ce3e59_2025东城二模细则.md:107-118`
  - common errors: `gpt_sources/606dbae1d5ce3e59_2025东城二模细则.md:123-126`

### Locked Prompt

The item asks students to identify the inference type, judge correctness, and explain why. The student's inference is: good innovation ecology -> innovation development; current China has good innovation ecology; therefore China can surely realize innovation development.

### Trigger Chain

- "有良好的创新生态，就会实现创新发展" is written as a sufficient-condition hypothetical judgment.
- The student then affirms the antecedent and affirms the consequent; the structure is valid.
- The scoring rule says good innovation ecology is a necessary condition, not a sufficient condition; therefore the premise is false and the conclusion is wrong.

## q0143-2025-xicheng-qimo-q17-2

- Part: 推理宝典
- Framework node: 三段论构建
- Evidence level: `A-formal`
- Status: `source_locked_pending_external_review`
- Sources:
  - paper: `gpt_sources/6662da1c2772cc38_2025北京西城高三_上_期末政治_教师版.md:191-215`
  - teacher answer: `gpt_sources/6662da1c2772cc38_2025北京西城高三_上_期末政治_教师版.md:281-292`
  - rubric: `gpt_sources/89d264a31e348be6_2025西城期末细则.md:70-77`

### Locked Prompt

The item asks students to use "工业固废是放错了地方的资源" as the minor premise and write a rule-abiding syllogism.

### Trigger Chain

- Minor term: 工业固废.
- Middle term: 资源 / 放错了地方的资源.
- Major term: 可以通过适当的方式被重新利用, or 可以转化为有价值的产品.
- The formal rubric states that conforming to basic syllogism rules is worth 4 points.

## Boundary Notes

- `2024海淀期中`: current cache has a generic teaching-advice hit, "辩证思维--两点与重点的统一", but no locked explicit 选必三 question row in the current scan. It stays a boundary/no-release row.
- `2025朝阳期中`: source ledger year is 2025 because the paper is 2025.11; current coverage already carries this suite as `2026朝阳期中(2025-11)` through `Q0003` and `Q0014`. V87 treats this as an academic-year alias, not as a new uncovered hole.
- `2025/2026海淀期中`: current keyword scan over the cached source files did not surface a concrete logic/thinking candidate; it remains a manual-review candidate if a strict all-source exhaustion claim is later required.


## V92 Q0141 Source Identity Addendum

- `Q0141` source identity is locally resolved for Claude-review gating: the physical source path and prior source ledger both place `17-2.docx` under `2024东城二模/细则/17题/17-2.docx`.
- The internal document header says `高三政治一模阅卷总结 2024.4.10`, but the actual item text is `17（2）结合材料，从推理的角度，谈谈科学团队是如何找到作物耐碱“密码”的。`
- The true `2024东城一模` Q17(2)-related rubric slide checked separately is the `北极熊毛衣` item, not the AT1/GS3 crop alkali-tolerance item.
- Decision: keep the student/audit source identity as `2024东城二模 Q17(2)` and preserve this as a header-template typo boundary for Claude V63 review.
- This addendum only unlocks Claude V63 review; it is not final Governor, Confucius, Word, or PDF acceptance.
