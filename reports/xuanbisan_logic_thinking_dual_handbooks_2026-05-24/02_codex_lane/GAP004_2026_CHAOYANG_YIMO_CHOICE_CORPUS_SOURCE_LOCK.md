# GAP004 Source Lock: 2026朝阳一模 Q1-Q15 选择题语料

Status: `closed_choice_corpus_classified_pending_external_review`

This file closes GAP004 at the local source-evidence level only. It does not close GPT Pro, Claude V4/V5, Governor, Confucius, or final delivery gates.

## Source

- paper and teacher answer key cache: `gpt_sources/585b15124610aff7_2026北京朝阳高三一模政治_教师版.md:26-176,320-325`
- subjective rubric cache: `gpt_sources/3a11db4bade216d1_2026朝阳一模细则.md:20-49`
- raw paper / teacher version: `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026朝阳一模\试卷\2026北京朝阳高三一模政治（教师版）.pdf`
- raw subjective rubric: `C:\Users\Administrator\Desktop\2026各区模拟题\2026各区一模\2026朝阳一模\细则\2026朝阳一模细则.docx`

The teacher-version PDF contains the objective answer key. The rubric docx is a subjective-question marking rule and does not separately score Q1-Q15, so all promoted choice rows here are `B-choice-signal`.

Formal objective answer key for Q1-Q15:

| question | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| answer | B | A | D | B | D | D | C | A | C | C | B | A | B | C | C |

## Q1-Q15 Module Classification

| question | answer | local decision | reason |
|---|---|---|---|
| Q1 | B | exclude | 党史、实干精神与一切从实际出发，非选必三专门语料。 |
| Q2 | A | exclude | 审美与价值观、意识能动性边界，属哲学文化综合，非选必三主链。 |
| Q3 | D | promote as `Q0037` thinking choice-trap | “科普+文化/非遗”中科技赋能传统文化焕新，正确项含辩证否定；只能作 choice signal，不作为主观题评分链。 |
| Q4 | B | exclude | 中非人文交流与文化交流互鉴，非选必三。 |
| Q5 | D | promote as `Q0038` reasoning choice-trap | 选择题集中考否定全称误推出部分肯定、充分条件误写充要条件、列举部分误判划分不全、关系非传递性。 |
| Q6 | D | promote as `Q0039` thinking choice-trap | 坝河治理从单一功能到复合空间，并在水城之间建立新联系；正式答案键为 D。旧思维索引曾把 A 写成稳点，本轮以教师版答案键和错肢库 A/B/C 错误记录为准。 |
| Q7 | C | promote as `Q0040` thinking choice-trap | 月壤样品分析、化学组成重建、卫星遥感数据互证，训练科学思维证据可信度与超前思维误挂。 |
| Q8 | A | exclude | 人大代表、政协委员履职，属政治与法治。 |
| Q9 | C | exclude | 规划纲要法定程序与党的领导、人民当家作主、依法治国统一，属政治与法治。 |
| Q10 | C | exclude | 财产权、知识产权与担保，属法律与生活。 |
| Q11 | B | exclude | 道交纠纷多元化解，属政治/法律治理场景；“创新渠道”不是选必三创新思维题。 |
| Q12 | A | exclude | 智能经济实施路径，属经济与社会；传导错误只作经济错肢，不入选必三。 |
| Q13 | B | exclude | 制造业数据解读，属经济与社会。 |
| Q14 | C | exclude | 制度型开放，属当代国际政治与经济。 |
| Q15 | C | exclude | 全球倡议与全球治理，属当代国际政治与经济。 |

## Local Decisions To Ledger

### Q0037 2026朝阳一模 Q3

Evidence level: `B-choice-signal`

- correct answer: `D` (`②④`)
- usable signal: 科技赋能传统文化、非遗和科普融合，让传统文化在新场景中焕发新光彩。
- trap: ①“春节成为全民科学素养提升的主阵地”过度拔高；③把题意扯向民族文化与外来文化交融，材料不支持。
- boundary: This is a choice signal only. It must not be promoted as an A-formal subjective thinking chain.

### Q0038 2026朝阳一模 Q5

Evidence level: `B-choice-signal`

- correct answer: `D`
- usable reasoning signal: “1班赢2班，2班赢3班”不能推出“1班一定赢3班”，胜负关系属于非传递关系。
- traps:
  - A: “没参加全部三项”只是否定三项全参加，不能推出参加一项或两项。
  - B: “如果……那么……”通常表达充分条件假言判断，不等于充要条件假言判断。
  - C: 只列举足球、篮球两项，不等于作出完整划分，不能直接判为划分不全。

### Q0039 2026朝阳一模 Q6

Evidence level: `B-choice-signal`

- correct answer: `D`
- usable thinking signal: 坝河治理在水与城之间建立新联系，从排洪河道转为复合空间，可作为发散与聚合、系统化综合的选择题信号。
- trap:
  - A: “通过运用分析方法实现综合化”把综合化误写成单纯分析方法。
  - B: 把“变”与“不变”的对立统一误写成折中主义。
  - C: “生命之河”的类比可以形象表达价值，但不能直接说深刻揭示价值本质。
- conflict note: old thinking index described A as stable and D as trap; official teacher answer key gives D, and the wrong-option library identifies A/B/C as traps. The formal answer key governs.

### Q0040 2026朝阳一模 Q7

Evidence level: `B-choice-signal`

- correct answer: `C`
- usable thinking signal: 科学研究通过样品分析、化学组成重建和卫星遥感数据互证来增强结论可信度。
- trap:
  - A: 严谨判断、推理、论证揭示的是客观属性、本质和规律，不是“形象化特征”。
  - D: 样品分析与遥感验证不是对未来趋势作预测，不能硬套超前思维。

## Gate Decision

GAP004 can move from `open` to `closed_choice_corpus_classified_pending_external_review`: all Q1-Q15 items have been classified; Q3/Q5/Q6/Q7 produce local ledger rows; Q6 old-index conflict is recorded and held for external review.

This is still not release-ready. The additions must be included in the next GPT Pro packet and the next real Claude external-review packet.
