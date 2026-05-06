# Phase 02 Hard Sample Entries - Internal Evidence Only

Status: Codex lane A first-pass evidence extraction.

Hard rule: this file is not student-facing. It may contain rubric, scoring, and audit language. Student-facing drafts must rewrite from locked evidence only after GPT, ClaudeCode, Governor, and Confucius gates pass.

## HS01 - 2026 顺义一模 Q19(2)

- Target: 思维部分 / 科学思维特征
- Source status: paper text extracted; rubric PPTX text extracted.
- Paper anchor: `HS01__paper__试卷.txt:351-365`
- Rubric anchor: `HS01__rubric__细则.txt:75-79`
- Question ask: 结合材料二，运用《逻辑与思维》知识，说明该企业具身机器人的研发是如何体现科学思维特征的。
- Material signal:
  - 走进社区、养老院，蹲点观察老人真实生活习惯。
  - 围绕安全照护、健康提醒、情感陪伴三大需求。
  - 追踪老龄化、护理短缺、养老服务应用空间。
  - 多轮应用测试、打磨与迭代。
- Locked knowledge:
  - 科学思维追求认识的客观性。
  - 科学思维结果具有预见性。
  - 科学思维结果具有可检验性。
- Evidence level: A, because paper ask and scoring answer both directly name the module and subpoints.
- Student-doc future action: can become a locked "科学思维特征" full-chain entry after ClaudeCode independent cross-check.

## HS02 - 2025 海淀二模 Q20

- Target: 思维部分 / 辩证思维
- Source status: paper PDF text layer failed; paper visually reviewed from rendered page; rubric DOCX text extracted.
- Paper visual anchor: `02_extraction/hard_samples/renders/HS02__paper__试卷_all/page_07.png`
- Rubric anchor: `HS02__rubric__2025年海淀二模评标实录.txt:25-28`
- Additional scoring anchors:
  - `priority_queue_sources/text/009_...2025海淀二模_细则_细则.docx.txt:67-72`
  - `priority_queue_sources/text/011_...2025届二模考试讲评0510.pdf.txt:514-541`
- Question ask from visual review: 结合材料，运用辩证思维知识，谈谈如何更好地坚持共享发展理念推进共同富裕。
- Material signal from visual review:
  - 共享发展理念继承发展传统文化思想，并回应现实问题。
  - 全民共享、全面共享、共建共享、渐进共享。
  - 渐进共享强调从低级到高级、从不均衡到均衡。
- Locked knowledge:
  - 辩证思维的整体性。
  - 辩证思维的动态性。
  - 辩证否定。
- Scoring boundary:
  - 主细则/讲评显示为“三个角度选择两个，每个角度按知识1分+阐述2分赋分”。
  - 因此三条都是可写角度池，不应误写成三条全部必答。
  - 评标实录确认“辩证否定”有效，且辩证思维特征角度可以替代给分。
- Boundary note: paper OCR/text extraction cannot be treated as complete; visual transcription must be rechecked by ClaudeCode or another visual pass before final locking.
- Evidence level: A- pending visual cross-check, because rubric directly names the points but paper source is image-reviewed.
- Student-doc future action: do not write final entry until visual cross-check closes.

## HS03 - 2026 朝阳期中 Q21(2)

- Target: 思维部分 / 创新思维
- Source status: paper text extracted; rubric DOCX and supplement text extracted.
- Paper anchor: `HS03__paper__试卷.txt:286-295`
- Rubric anchor: `HS03__rubric__细则.txt:117-130`
- Question ask: 结合材料二，运用《逻辑与思维》知识，说明该市是如何运用创新思维将人文底蕴转化为经济发展优势的。
- Material signal:
  - 从传统工业城市向网红旅游目的地跃迁。
  - 以冰雪文化为核心，将冷资源转化为热经济。
  - 冰雕艺术从单一观赏升级为沉浸式体验。
  - 历史街区、数字艺术、社群共创形成复合型文化空间。
  - 静态建筑转化为动态文化场景。
- Locked knowledge:
  - 超前思维。
  - 联想思维。
  - 转换性思考 / 逆向思维。
  - 创新思维的三新特征。
  - 发散思维与聚合思维相结合。
- Scoring boundary:
  - 三新加简单分析仅 3 分。
  - 三新加分析再加至少两个创新解决办法可满分。
  - 无三新时，三种不同思维方式也可满分。
  - 发散与聚合只写一方只能给半点。
- Evidence level: A, because paper ask and scoring rule directly bind innovation-thinking subpoints.
- Student-doc future action: can become a locked "创新思维选点和材料对应" full-chain entry after cross-check.

## HS04 - 2026 通州期末 Q11

- Target: 思维选择题 / 感性具体、思维抽象、思维具体
- Source status: paper text extracted; answer key text extracted from same paper and rubric PPTX.
- Paper anchor: `HS04__paper__试卷.txt:149-155`
- Answer key anchor: `HS04__paper__试卷.txt:332-344`
- Question ask: 此“河-合-和”理念的诠释过程。
- Full options:
  - A. 实现了对运河文化从感性认识到理性认识的迁移和飞跃
  - B. 展现了从分析到综合、从普遍一特殊一普遍的思维进阶
  - C. 体现了从感性具体到思维抽象再到思维具体的发展过程
  - D. 呈现了对“水脉一文脉一人脉”进行类比推理与系统整合
- Locked answer: C.
- Reasoning attachment:
  - 材料从大运河具体文化现象出发。
  - 对“河”“合”“和”进行抽象提炼。
  - 再回到文化之河、生态之河、发展之河、民生之河的整体诠释。
- Evidence level: A for choice-question capture, because full stem, full options, and answer key are present.
- Student-doc future action: reasoning-choice trap entry must include all four options and why B/D look tempting but miss the precise thinking path.

## HS05 - 2026 东城期末 Q17(2)

- Target: 推理部分 / 形式逻辑综合主观题
- Source status: paper text extracted; rubric PPTX text extracted.
- Paper anchor: `HS05__paper__试卷.txt:238-246`
- Rubric anchor: `HS05__rubric__细则.txt:377-416`
- Question ask: 运用形式逻辑知识，论证三项主张是否符合逻辑。
- Material claims:
  - 主张1: 完整保留历史街巷的一砖一瓦，同时对不适应现代需要部分进行拆除和改造。
  - 主张2: 要提升垃圾分类效率，必须引入智能垃圾箱；如果引入智能垃圾箱，垃圾分类效率就能得到提升。
  - 主张3: 有些科学民主的更新方案采用某模式；某具体方案通过此模式制定；因此该具体方案科学民主。
- Locked reasoning:
  - 主张1: 违反矛盾律；也可从联言判断不能同真、不相容关系等角度说明。
  - 主张2: 将充分条件假言判断误推为肯后必肯前，混淆充分条件和必要条件；也可指出轻率概括。
  - 主张3: 三段论推理中项不周延。
- Scoring boundary:
  - 只写判断或推理不符合逻辑、没有理由，不给分。
  - 只写逻辑规则错误而无材料解释，酌情扣 1-2 分。
- Evidence level: A, because prompt and scoring rule directly name formal logic rules.
- Student-doc future action: this belongs in the reasoning-part typology chapter, not in thinking-method principle chapter.
