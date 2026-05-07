# P2G017 Source Evidence — 017_Desktop_2024模拟题_2024朝阳期中_试卷_试卷.pdf

Source group recheck for the three P2 choice_trap rows tied to北京朝阳区2024~2025学年度第一学期期中质量检测·高三思想政治试卷（2024.11）。

## 0. Source files inventory

From `fusion/p2_recheck_sources/P2_SOURCE_TEXT_INDEX.csv` row source_id=`017_Desktop_2024模拟题_2024朝阳期中_试卷_试卷.pdf`：

| kind | text_path | what it contains |
|------|-----------|------------------|
| paper | `fusion/p2_recheck_sources/017_*__paper.txt` (21 011 字节) | 完整试卷OCR文本，含Q1-Q15客观题（每题3分，共45分）+ Q16-Q20主观题题干 |
| support | `fusion/p2_recheck_sources/017_*__support__2024.11期中政治朝阳评标2.docx.txt` (886 字节) | 7行小组首页索引：'20241109高3阅卷总结16/17/18/20（1）/（2）/（3）题组+20240708高2阅卷总结22题' |
| support | `fusion/p2_recheck_sources/017_*__support__2024.11期中政治朝阳评标docx.docx.txt` (12 818 字节) | 16-20题主观题阅卷细则（16题范伟光组/17题高捷组/18题任会波组/20题（1）（2）（3）李丽莲/汤桃玲/代超组），覆盖唯物史观/哲学与文化/逻辑与思维主观题/经济信息+经济与社会+当代国际政治与经济。**全文不出现Q1-Q15客观题答案。** |
| support | `fusion/p2_recheck_sources/017_*__support__202411朝阳高三政治_期中1试题(1).pdf.txt` (21 011 字节) | 与paper.txt逐字相同的试卷副本，无答案表 |

> 关键事实：本源所有support文件均只覆盖16-20题主观题（约55分卷面）阅卷细则，**未提供Q1-Q15共15道客观题（每题3分共45分）的任何答案表或选项标注**。这是本次P2复核全部走向source_insufficient的根本原因。

## 1. Q-2024朝阳期中-7（三段论·第三格AAI式·北京中轴线）

### 1.1 Stem & options（paper.txt 行65-73 逐字）

> 7. 2024年7月,联合国教科文组织第46届世界遗产大会通过决议,将"北京中轴线———中国理想都城秩序的杰作"列入《世界遗产名录》。据此,小刘同学写出了以下四个判断
> ①"北京中轴线"是由世界遗产委员会确认的世界遗产
> ②"北京中轴线"是不可替代的文化遗产
> ③有些由世界遗产委员会确认的世界遗产是不可替代的文化遗产
> ④有些不可代替的文化遗产是由世界遗产委员会确认的世界遗产
> 从以上四个判断中选取三个,依次作为大前提、小前提、结论,下列选项中符合三段论推理规则的是
> A. ①-③-④   B. ②-①-③   C. ③-②-④   D. ④-②-①

### 1.2 Source-grounded form-logic features

- ①②为单称肯定（SAP）；③④为特称肯定（IAP/PIN）。
- 三段论判第几格须先定中项M在两前提中的位置：M为两前提主项→第三格；M为两前提谓项→第二格；M大前提主项+小前提谓项→第一格；M大前提谓项+小前提主项→第四格。
- 第三格的有效式之一为AAI（两全称肯定前提推出特称肯定结论），符合"特称肯定结论"端项处理规则。
- 端项周延校验：小项在前提中不周延→结论中也不能周延（小项不当扩大），大项同理。

### 1.3 Answer-key search outcome

| support file | grep 关键词 | 命中 |
|--------------|------------|------|
| 评标docx.docx | "7. "/"第7题"/"答案"/"参考答案"/"选择题答案" | 0 |
| 评标2.docx | 同上 | 0 |
| 期中1试题(1).pdf | 同上 | 0 |

→ **Q7正确选项无法从017号源核实。**

### 1.4 Decision

`source_insufficient` · `can_enter_fusion=no`。framework_first_fusion P1版第527行Q-2024朝阳期中-7条目应降级。

---

## 2. Q-2024朝阳期中-8（必要条件假言判断·三种等价表达式·调查研究）

### 2.1 Stem & options（paper.txt 行74-81 逐字）

> 8. 调查研究是谋事之基、成事之道,没有调查就没有发言权,没有调查就没有决策权;正确的决策离不开调查研究,正确的贯彻落实同样也离不开调查研究。据此,依照逻辑规则,下列选项一定为真的是
> ①调查研究是谋事和成事的充分必要条件
> ②除非进行了调查研究,否则没有发言权和决策权
> ③没有做出正确的决策,是因为没有进行调查研究
> ④只有进行了调查研究,才能有正确的贯彻落实
> A.①③ B.①④ C.②③ D.②④

### 2.2 Source-grounded form-logic features

- 题干句式信号：'没有X就没有Y'/'Y离不开X'即必要条件假言判断核心标志（'p是q的必要条件'⇔'非p则非q'）。
- 必要条件假言判断三种等价表达式：'除非p否则非q'='只有p才q'='非p则非q'。
- 候选判断分类：
  - ①'充分必要条件'：题干仅给必要条件信号，未给充分条件信号→强读为充要超出题干。
  - ②'除非……否则不'：必要条件标准式之一。
  - ③'没有做出正确的决策，是因为没有进行调查研究'：'结果反推原因为唯一原因'，把非p作为唯一可能解释，是因果倒推（充分条件读法），与题干给出的必要条件结构不相符。
  - ④'只有……才'：必要条件标准式之一。

### 2.3 Answer-key search outcome

同上：三份support文件均不出现Q8答案。

### 2.4 Decision

`source_insufficient` · `can_enter_fusion=no`。framework_first_fusion P1版第751行Q-2024朝阳期中-8条目应降级。

---

## 3. Q-2024朝阳期中-10（概念外延关系·属种关系·中国式现代化）

### 3.1 Stem & options（paper.txt 行90-96 逐字）

> 10. 中国式现代化是人与自然和谐共生的现代化。良好的生态环境是最普惠的民生福祉,是人心所盼。要还老百姓蓝天白云、繁星闪烁,要为老百姓留住鸟语花香田园风光,这些美好愿景如今正在变成现实。下列选项正确的是
> A. "中国式现代化"和"现代化"是属种关系
> B. "良好的生态环境"和"民生福祉"在外延上是一致的
> C. "留住鸟语花香田园风光",此处的"留住"关系为对称关系
> D. "如今正在变成现实",说明要把握好事物发展过程中量变与质变的关系

### 3.2 Source-grounded form-logic features

- A考查属种关系（'中国式现代化'⊂'现代化'，前者为种、后者为属）。
- B考查全同关系（外延完全相等）：'良好的生态环境'与'民生福祉'外延差异显著（民生福祉范围更广，含医保/教育/养老等）。
- C考查关系判断性质（对称/反对称、传递/反传递）：'留住'语义上为单向动作关系，不构成对称结构。
- D考查跨册诱饵：把'量变与质变'（必修四唯物辩证法范畴）塞入选必三概念外延关系考查中。

### 3.3 Answer-key search outcome

同上：三份support文件均不出现Q10答案。**且manifest第32行已对该行作前置标记**：phase12_action=blocked_keep_out / phase12_category=answer_missing / note='题干显然涉及概念外延/关系判断，但本轮只找到试卷题面，未找到可靠选择题答案表；不得逻辑猜答案'。

### 3.4 Decision

`source_insufficient` · `can_enter_fusion=no`。维持manifest的blocked_keep_out判断；framework_first_fusion P1版第806行Q-2024朝阳期中-10条目应降级。

---

## 4. Cross-row source-evidence consistency

| question_id | stem-options 可核 | answer 可核 | manifest前置标记 | decision |
|-------------|------------------|------------|-----------------|----------|
| Q-2024朝阳期中-7 | yes（行65-73） | no | covered_by_74_review_body（即原已入review正文） | source_insufficient |
| Q-2024朝阳期中-8 | yes（行74-81） | no | covered_by_74_review_body（即原已入review正文） | source_insufficient |
| Q-2024朝阳期中-10 | yes（行90-96） | no | blocked_keep_out / answer_missing / 不得逻辑猜答案 | source_insufficient |

> 三行的核心证据状态一致：题干与选项 paper.txt 可核，但选择题答案在017源 support 范围内不存在；按硬规则三行同走 `source_insufficient`。Q7/Q8 之前虽以 covered_by_74_review_body 进入 review 正文，但 P2 源级复核要求重新对答案表做源验证，未通过则降级；Q10 已是 manifest 显标的 answer_missing，本次维持。

## 5. What this evidence does NOT establish

- 不能确认 Q7 正确选项究竟是 A/B/C/D 中哪一个（framework_first_fusion P1的 B 假设无源根据，待官方答案补入后再回填）。
- 不能确认 Q8 正确选项究竟是 A/B/C/D 中哪一个（framework_first_fusion P1的 D 假设无源根据，待官方答案补入后再回填）。
- 不能确认 Q10 正确选项究竟是 A/B/C/D 中哪一个（framework_first_fusion P1的 A 假设无源根据，待官方答案补入后再回填）。
- 不能由学生侧基于 form-logic 推算正确选项后替换源材料，因为 P2 硬规则明令'不得逻辑猜答案'。

## 6. Recommended downstream action（不在本任务执行范围内）

- 后续若获得朝阳教研中心或官方教师版2024.11期中政治答案表，可由独立 patch 按 confirmed_with_patch 路径回填；当前回填动作不在 P2G017 这一小规模复核任务的输出范围内。
- framework_first_fusion P1版第527/751/806行三处 Codex 待复核标记，后续 patch 工作应按 source_insufficient 处理（保留卷面识别要素与答题要点训练价值，但不输出确定性答案句）。
