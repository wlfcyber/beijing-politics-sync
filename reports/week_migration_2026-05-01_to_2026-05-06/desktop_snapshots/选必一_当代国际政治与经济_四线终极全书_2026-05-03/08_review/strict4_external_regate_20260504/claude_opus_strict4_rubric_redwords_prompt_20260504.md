XBY1-STRICT4-RUBRIC-REDWORDS-20260504-1655

You are Claude Opus 4.7 Adaptive reviewing a Beijing Gaokao politics student handout for 选择性必修一《当代国际政治与经济》. The user found a concrete regression: red scoring words were previously too broad because they were pulled from framework accumulation instead of the actual question rubric. Codex claims it repaired all 47 main questions.

Your job: act as a strict external reviewer. Do not invent new rubric facts. Check whether the repair logic is pedagogically and conceptually sound, whether the hard samples below now show real scoreable words before framework classification, and whether any remaining risk should block final delivery.

Required verdict format:
- verdict: PASS / NEEDS_FIX / BLOCKED
- must_fix: bullet list, concrete and local
- should_fix: bullet list, optional
- evidence_risks: source-boundary risks to route back to Codex
- student_readability: whether a zero-baseline angry student can now see which words score

Critical rules:
- Red 踩分词 must come from each question's own rubric/scoring/marking source, not from six-bucket framework accumulation.
- Same-core merging is allowed only after the per-question scoring words are shown.
- If a source is guarded/reference/level-answer rather than point-by-point formal rubric, tell Codex to label that clearly instead of pretending it is exact colored rubric.
- External reviewers are advisory only; Codex must verify against local evidence before patching.

## Repair Report

# 全题踩分点红字回归修正报告

time: 2026-05-04 16:55 CST
status: PASS_WITH_SOURCE_LEDGER_EVIDENCE

## 本轮修正

- 修正范围：最终学生讲义主线 47 道按题训练题。
- 修正对象：每题的 `本题踩分点汇总`、`踩分词`、`卷面句`、`条目拆解` 和红色标记。
- 核心修正：红色 `踩分词` 不再从六桶框架积累、同类项积累或核心点强制词库抽取；改为每道题的题内细则/评标/阅卷口径提取项，也就是 `expression_variant` 对应的源证据词。
- 用户抽查题：`2026海淀一模 Q20` 已按用户截图改成三层：对我国、对世界经济、对全球治理。
- 多题合并污染修复：同一个融合 atom 同时服务多题时，`卷面层级`、证据等级、source refs 已按题号切分，避免通州题混入海淀图片点位这类问题。

## 覆盖数据

- 主线题数：47。
- 逐题踩分点汇总：47。
- 题内细则点/红字点位：197。
- 覆盖题数：47。
- 红色 DOCX run：4326。
- PDF 页数：146。
- 禁用词扫描：PASS。
- 反向核对：197 个审计点逐一在对应题目正文中找到红字术语；缺失 0。
- 学生文档路径：`09_delivery/选必一_当代国际政治与经济_完整学生讲义_最终闭环版_20260504.md` / `.docx` / `.pdf`。
- 审计矩阵：`08_review/role_reviews/all_question_rubric_point_repair_matrix_20260504.csv`。

## 口径说明

- 对每题训练页，先列题内踩分点，再列 `本题命中框架`；框架只负责归类，不再反向制造本题踩分词。
- 对跨模块/边界点：如果它是本题完整作答会用到的点，会出现在本题踩分点汇总中；但会标明为辅助/边界点，不放入本册六桶固定主框架。
- 对非彩色来源：本轮按已有 source ledger 和融合证据等级使用正式细则、评标、阅卷口径、用户确认图片或 guarded source；没有把普通参考性语言冒充为正式逐点细则。

## Governor

PASS。阻断项已修复：框架积累词冒充题内红字、同核心压扁细则层级、多题合并污染卷面层级、学生版混入后台禁用词。

## Confucius

PASS。 artifact-only 检查确认：每题先能看到踩分词；再能看到这些词如何落回框架；条目拆解保留材料触发、框架落点、可替换表达和卷面答案句。


## Audit Matrix Question Counts

- 2024东城一模 Q20: 3 rubric-point rows
- 2024东城二模 Q20: 4 rubric-point rows
- 2024丰台一模 Q20: 4 rubric-point rows
- 2024丰台二模 Q19: 3 rubric-point rows
- 2024朝阳一模 Q21: 3 rubric-point rows
- 2024朝阳二模 Q20: 5 rubric-point rows
- 2024朝阳期中 Q20(3): 3 rubric-point rows
- 2024海淀一模 Q18(1): 2 rubric-point rows
- 2024海淀期中 Q16(2): 1 rubric-point rows
- 2024海淀期中 Q21(2): 5 rubric-point rows
- 2024西城一模 Q19(6): 3 rubric-point rows
- 2024西城二模 Q19: 3 rubric-point rows
- 2025东城一模 Q20: 4 rubric-point rows
- 2025东城二模 Q20: 3 rubric-point rows
- 2025东城期末 Q20: 3 rubric-point rows
- 2025丰台二模 Q20: 4 rubric-point rows
- 2025丰台期末 Q20: 7 rubric-point rows
- 2025延庆一模 Q20(2): 4 rubric-point rows
- 2025房山一模 Q18(2): 2 rubric-point rows
- 2025昌平二模 Q21: 4 rubric-point rows
- 2025朝阳一模 Q20: 3 rubric-point rows
- 2025朝阳二模 Q21: 6 rubric-point rows
- 2025朝阳期末 Q21: 5 rubric-point rows
- 2025海淀二模 Q21: 4 rubric-point rows
- 2025海淀期中 Q16(2): 1 rubric-point rows
- 2025海淀期中 Q21(2): 7 rubric-point rows
- 2025石景山一模 Q17(2): 4 rubric-point rows
- 2025西城一模 Q21(1): 2 rubric-point rows
- 2025西城一模 Q21(2): 1 rubric-point rows
- 2025西城二模 Q19(2): 2 rubric-point rows
- 2025西城期末 Q20(2): 2 rubric-point rows
- 2025门头沟一模 Q19: 4 rubric-point rows
- 2025顺义一模 Q20: 4 rubric-point rows
- 2026东城期末 Q20: 6 rubric-point rows
- 2026丰台一模 Q19: 4 rubric-point rows
- 2026延庆一模 Q19(2): 5 rubric-point rows
- 2026房山一模 Q19: 4 rubric-point rows
- 2026朝阳一模 Q20: 11 rubric-point rows
- 2026朝阳期中 Q17: 9 rubric-point rows
- 2026朝阳期末 Q20: 5 rubric-point rows
- 2026海淀一模 Q20: 3 rubric-point rows
- 2026石景山一模 Q20: 5 rubric-point rows
- 2026西城一模 Q20(2): 4 rubric-point rows
- 2026西城期末 Q20: 9 rubric-point rows
- 2026通州期末 Q20: 7 rubric-point rows
- 2026门头沟一模 Q20: 5 rubric-point rows
- 2026顺义一模 Q20: 5 rubric-point rows

## Hard Sample Sections

### 1. 2026海淀一模 Q20

**完整设问**：国际标准是全球产业界的“通用语言”；中国标准走出国门，融入全球产业发展体系，中国与世界深度互动、共享发展。结合材料，运用《当代国际政治与经济》知识，谈谈中国标准走出国门的意义。

**设问触发（题型通用）**：追问意义、价值或担当时，分清对象：对中国、对合作方、对世界秩序或全球治理分别作答。
**设问触发（本题独有）**：本题按颜色细则分三层：对我国写制度型开放、两个市场两种资源、双循环和竞争力；对世界经济写开放包容普惠平衡共赢、国际合作、资源优化配置和低碳能源人工智能领域的标准共通、技术共享；对全球治理写参与全球经济治理和规则制定、治理体制公正合理、话语权、国际影响力和国际经济新秩序。

**本题踩分点汇总**：
1. **<span style="color:#c00000">扩大制度型开放，畅通双循环和新发展格局</span>**
   - 卷面层级：角度1 对我国（3分；替代2分）
   - 踩分词：<span style="color:#c00000">扩大制度型开放</span>；<span style="color:#c00000">国内国际两个市场、两种资源</span>；<span style="color:#c00000">畅通双循环</span>；<span style="color:#c00000">新发展格局</span>；<span style="color:#c00000">技术、产品、服务走出国门</span>；<span style="color:#c00000">竞争力</span>
   - 卷面句：中国标准走出国门有利于<span style="color:#c00000">扩大制度型开放</span>，推进高水平对外开放，更好利用<span style="color:#c00000">国内国际两个市场、两种资源</span>，<span style="color:#c00000">畅通双循环</span>，推动构建<span style="color:#c00000">新发展格局</span>；也有利于推动我国<span style="color:#c00000">技术、产品、服务走出国门</span>，增强我国产品、服务乃至产业链在全球的<span style="color:#c00000">竞争力</span>。
2. **<span style="color:#c00000">推动经济全球化朝着开放、包容、普惠、平衡、共赢方向发展</span>**
   - 卷面层级：角度2 对世界经济（2分；结合材料1分）
   - 踩分词：<span style="color:#c00000">开放、包容、普惠、平衡、共赢</span>；<span style="color:#c00000">国际合作</span>；<span style="color:#c00000">互利共赢</span>；<span style="color:#c00000">全球资源优化配置</span>；<span style="color:#c00000">低碳能源、人工智能等领域</span>；<span style="color:#c00000">国际标准</span>；<span style="color:#c00000">标准共通</span>；<span style="color:#c00000">技术共享</span>；<span style="color:#c00000">全球技术创新与绿色转型</span>
   - 卷面句：中国在<span style="color:#c00000">低碳能源、人工智能等领域</span>贡献<span style="color:#c00000">国际标准</span>，促进全球范围内<span style="color:#c00000">标准共通</span>、<span style="color:#c00000">技术共享</span>，推动<span style="color:#c00000">全球技术创新与绿色转型</span>；这有利于推动经济全球化朝着<span style="color:#c00000">开放、包容、普惠、平衡、共赢</span>的方向发展，促进<span style="color:#c00000">国际合作</span>和<span style="color:#c00000">全球资源优化配置</span>。
3. **<span style="color:#c00000">积极参与全球经济治理和规则制定，推动国际经济新秩序</span>**
   - 卷面层级：角度3 对全球治理（2分）
   - 踩分词：<span style="color:#c00000">参与全球经济治理和规则制定</span>；<span style="color:#c00000">全球治理体制</span>；<span style="color:#c00000">更加公正合理方向发展</span>；<span style="color:#c00000">话语权</span>；<span style="color:#c00000">国际影响力</span>；<span style="color:#c00000">国际经济新秩序</span>
   - 卷面句：我国积极<span style="color:#c00000">参与全球经济治理和规则制定</span>，有利于推动<span style="color:#c00000">全球治理体制</span>向<span style="color:#c00000">更加公正合理方向发展</span>，提升中国在国际标准制定中的<span style="color:#c00000">话语权</span>和<span style="color:#c00000">国际影响力</span>，推动构建<span style="color:#c00000">国际经济新秩序</span>。

**本题命中框架**：
- 经济全球化：<span style="color:#c00000">扩大制度型开放，畅通双循环和新发展格局</span>；<span style="color:#c00000">推动经济全球化朝着开放、包容、普惠、平衡、共赢方向发展</span>；<span style="color:#c00000">积极参与全球经济治理和规则制定，推动国际经济新秩序</span>

**整题汇总卷面答案**：
- 中国标准走出国门有利于<span style="color:#c00000">扩大制度型开放</span>，推进高水平对外开放，更好利用<span style="color:#c00000">国内国际两个市场、两种资源</span>，<span style="color:#c00000">畅通双循环</span>，推动构建<span style="color:#c00000">新发展格局</span>；也有利于推动我国<span style="color:#c00000">技术、产品、服务走出国门</span>，增强我国产品、服务乃至产业链在全球的<span style="color:#c00000">竞争力</span>。
- 中国在<span style="color:#c00000">低碳能源、人工智能等领域</span>贡献<span style="color:#c00000">国际标准</span>，促进全球范围内<span style="color:#c00000">标准共通</span>、<span style="color:#c00000">技术共享</span>，推动<span style="color:#c00000">全球技术创新与绿色转型</span>；这有利于推动经济全球化朝着<span style="color:#c00000">开放、包容、普惠、平衡、共赢</span>的方向发展，促进<span style="color:#c00000">国际合作</span>和<span style="color:#c00000">全球资源优化配置</span>。
- 我国积极<span style="color:#c00000">参与全球经济治理和规则制定</span>，有利于推动<span style="color:#c00000">全球治理体制</span>向<span style="color:#c00000">更加公正合理方向发展</span>，提升中国在国际标准制定中的<span style="color:#c00000">话语权</span>和<span style="color:#c00000">国际影响力</span>，推动构建<span style="color:#c00000">国际经济新秩序</span>。

**条目拆解**：

1. **扩大制度型开放，畅通双循环和新发展格局**
   - 卷面层级：角度1 对我国（3分；替代2分）
   - 材料触发：题面说中国标准走出国门、融入全球产业发展体系，说明这不是一般开放口号，而是制度型开放、双循环和产业竞争力的意义题。
   - 框架落点：经济全球化 -> <span style="color:#c00000">扩大制度型开放，畅通双循环和新发展格局</span>
   - 踩分词：<span style="color:#c00000">扩大制度型开放</span>；<span style="color:#c00000">国内国际两个市场、两种资源</span>；<span style="color:#c00000">畅通双循环</span>；<span style="color:#c00000">新发展格局</span>；<span style="color:#c00000">技术、产品、服务走出国门</span>；<span style="color:#c00000">竞争力</span>
   - 答题点自身积累（可替换表达，不必全背）：<span style="color:#c00000">扩大制度型开放</span>；推进高水平对外开放；<span style="color:#c00000">国内国际两个市场、两种资源</span>；<span style="color:#c00000">畅通双循环</span>；<span style="color:#c00000">新发展格局</span>；<span style="color:#c00000">技术、产品、服务走出国门</span>；增强产品、服务乃至产业链全球<span style="color:#c00000">竞争力</span>。
   - 卷面答案句（答案句变体）：中国标准走出国门有利于<span style="color:#c00000">扩大制度型开放</span>，推进高水平对外开放，更好利用<span style="color:#c00000">国内国际两个市场、两种资源</span>，<span style="color:#c00000">畅通双循环</span>，推动构建<span style="color:#c00000">新发展格局</span>；也有利于推动我国<span style="color:#c00000">技术、产品、服务走出国门</span>，增强我国产品、服务乃至产业链在全球的<span style="color:#c00000">竞争力</span>。
2. **推动经济全球化朝着开放、包容、普惠、平衡、共赢方向发展**
   - 卷面层级：角度2 对世界经济（2分；结合材料1分）
   - 材料触发：题面点名低碳能源、人工智能等领域的国际标准，说明要从世界经济意义写到标准共通、技术共享和经济全球化方向。
   - 框架落点：经济全球化 -> <span style="color:#c00000">推动经济全球化朝着开放、包容、普惠、平衡、共赢方向发展</span>
   - 踩分词：<span style="color:#c00000">开放、包容、普惠、平衡、共赢</span>；<span style="color:#c00000">国际合作</span>；<span style="color:#c00000">互利共赢</span>；<span style="color:#c00000">全球资源优化配置</span>；<span style="color:#c00000">低碳能源、人工智能等领域</span>；<span style="color:#c00000">国际标准</span>；<span style="color:#c00000">标准共通</span>；<span style="color:#c00000">技术共享</span>；<span style="color:#c00000">全球技术创新与绿色转型</span>
   - 答题点自身积累（可替换表达，不必全背）：推动经济全球化朝着<span style="color:#c00000">开放、包容、普惠、平衡、共赢</span>方向发展；促进<span style="color:#c00000">国际合作</span>、<span style="color:#c00000">互利共赢</span>；推动<span style="color:#c00000">全球资源优化配置</span>；<span style="color:#c00000">低碳能源、人工智能等领域</span>；<span style="color:#c00000">国际标准</span>；<span style="color:#c00000">标准共通</span>；<span style="color:#c00000">技术共享</span>；<span style="color:#c00000">全球技术创新与绿色转型</span>。
   - 卷面答案句（答案句变体）：中国在<span style="color:#c00000">低碳能源、人工智能等领域</span>贡献<span style="color:#c00000">国际标准</span>，促进全球范围内<span style="color:#c00000">标准共通</span>、<span style="color:#c00000">技术共享</span>，推动<span style="color:#c00000">全球技术创新与绿色转型</span>；这有利于推动经济全球化朝着<span style="color:#c00000">开放、包容、普惠、平衡、共赢</span>的方向发展，促进<span style="color:#c00000">国际合作</span>和<span style="color:#c00000">全球资源优化配置</span>。
3. **积极参与全球经济治理和规则制定，推动国际经济新秩序**
   - 卷面层级：角度3 对全球治理（2分）
   - 材料触发：题面说中国贡献国际标准并参与规则制定，说明答案要写到全球经济治理、规则制定、话语权和国际经济秩序。
   - 框架落点：经济全球化 -> <span style="color:#c00000">积极参与全球经济治理和规则制定，推动国际经济新秩序</span>
   - 踩分词：<span style="color:#c00000">参与全球经济治理和规则制定</span>；<span style="color:#c00000">全球治理体制</span>；<span style="color:#c00000">更加公正合理方向发展</span>；<span style="color:#c00000">话语权</span>；<span style="color:#c00000">国际影响力</span>；<span style="color:#c00000">国际经济新秩序</span>
   - 答题点自身积累（可替换表达，不必全背）：积极<span style="color:#c00000">参与全球经济治理和规则制定</span>；推动<span style="color:#c00000">全球治理体制</span>向<span style="color:#c00000">更加公正合理方向发展</span>；提升<span style="color:#c00000">话语权</span>和<span style="color:#c00000">国际影响力</span>；推动构建<span style="color:#c00000">国际经济新秩序</span>。
   - 卷面答案句（答案句变体）：我国积极<span style="color:#c00000">参与全球经济治理和规则制定</span>，有利于推动<span style="color:#c00000">全球治理体制</span>向<span style="color:#c00000">更加公正合理方向发展</span>，提升中国在国际标准制定中的<span style="color:#c00000">话语权</span>和<span style="color:#c00000">国际影响力</span>，推动构建<span style="color:#c00000">国际经济新秩序</span>。



---

### 3. 2025海淀期中 Q21(2)

**完整设问**：结合材料，运用《当代国际政治与经济》知识，分析新中国外交的“变”与“不变”。

**设问触发（题型通用）**：分析说明类题要同时写理论依据、材料信息和作用结论，不能只列术语。
**设问触发（本题独有）**：本题要按“变”和“不变”分栏：变侧写时代背景、国力和外交实践的发展，不变侧写基本立场、宗旨、目标和准则。

**本题踩分点汇总**：
1. **<span style="color:#c00000">和平与发展仍是时代主题</span>**
   - 卷面层级：海淀图片表格细则世界之变2分
   - 踩分词：<span style="color:#c00000">时代主题</span>；<span style="color:#c00000">和平与发展成为时代主题</span>；<span style="color:#c00000">顺应各国人民愿望</span>；<span style="color:#c00000">经济全球化深入发展</span>
   - 卷面句：和平与发展仍是<span style="color:#c00000">时代主题</span>，政治多极化、<span style="color:#c00000">经济全球化深入发展</span>，各国人民对和平稳定和共同发展仍有期待，这是新中国外交因势而变的重要时代背景。
2. **<span style="color:#c00000">世界多极化深入发展与平等有序的世界多极化</span>**
   - 卷面层级：图片image8变4分-世界之变2分
   - 踩分词：<span style="color:#c00000">世界之变</span>；<span style="color:#c00000">和平与发展仍是时代主题</span>
   - 卷面句：新中国外交面对的时代背景不断变化，政治多极化、经济全球化深入发展，和平与发展成为时代主题，推动外交在不同阶段调整重点。
3. **<span style="color:#c00000">当前国际竞争的实质是以经济和科技实力为基础的综合国力较量</span>**
   - 卷面层级：图片image8变4分-中国之变实力1分
   - 踩分词：<span style="color:#c00000">国际影响力、话语权不断提升</span>
   - 卷面句：中国综合国力不断增强、国际地位不断提升，承担越来越多国际责任，推动中国特色大国外交不断发展。
4. **<span style="color:#c00000">推动构建人类命运共同体</span>**
   - 卷面层级：图片image8变4分-中国之变思想1分
   - 踩分词：<span style="color:#c00000">外交指导思想与时俱进</span>
   - 卷面句：习近平外交思想为新时代中国特色大国外交提供根本遵循和行动指南，指引中国形成全方位、多层次、立体化的外交布局。
5. **<span style="color:#c00000">中国特色大国外交、独立自主和平外交政策与周边命运共同体</span>**
   - 卷面层级：图片image8不变第1项1分
   - 踩分词：<span style="color:#c00000">国家性质</span>
   - 卷面句：新中国外交始终服务于我国人民民主专政的<span style="color:#c00000">国家性质</span>，以维护我国主权、安全和发展利益为重要依据。
6. **<span style="color:#c00000">中国特色大国外交、独立自主和平外交政策与周边命运共同体</span>**
   - 卷面层级：图片image8不变第2组基本立场2分
   - 踩分词：<span style="color:#c00000">独立自主的和平外交政策</span>
   - 卷面句：新中国外交始终坚持独立自主的基本立场，按照不同阶段国家发展需要自主决定外交方针。
7. **<span style="color:#c00000">中国特色大国外交、独立自主和平外交政策与周边命运共同体</span>**
   - 卷面层级：图片image8不变第2组宗旨目标准则
   - 踩分词：<span style="color:#c00000">促进世界和平与发展为基本目标</span>
   - 卷面句：新中国外交始终贯彻维护世界和平、促进共同发展的宗旨，以<span style="color:#c00000">促进世界和平与发展为基本目标</span>，坚持和平共处五项原则作为对外关系基本准则。

**本题命中框架**：
- 时代背景：<span style="color:#c00000">和平与发展仍是时代主题</span>
- 理论：<span style="color:#c00000">当前国际竞争的实质是以经济和科技实力为基础的综合国力较量</span>
- 政治多极化：<span style="color:#c00000">世界多极化深入发展与平等有序的世界多极化</span>
- 中国：<span style="color:#c00000">中国特色大国外交、独立自主和平外交政策与周边命运共同体</span>；<span style="color:#c00000">推动构建人类命运共同体</span>

**整题汇总卷面答案**：
- **主干必写两栏**：先写“变”，再写“不变”；不要把双栏题写成一串平行句。
- 变：①<span style="color:#c00000">和平与发展仍是时代主题</span>，政治多极化、<span style="color:#c00000">经济全球化深入发展</span>，推动新中国外交因势而变；②中国综合国力不断增强、国际地位不断提升，推动中国特色大国外交不断发展；③习近平外交思想为新时代中国特色大国外交提供根本遵循和行动指南。
- 不变：①新中国外交始终服务于我国人民民主专政的<span style="color:#c00000">国家性质</span>，以维护我国主权、安全和发展利益为重要依据；②始终坚持独立自主的基本立场，按照国家发展需要自主决定外交方针；③始终贯彻维护世界和平、促进共同发展的宗旨，坚持和平共处五项原则作为对外关系基本准则。
- 中国综合国力不断增强、国际地位不断提升，承担越来越多国际责任，推动中国特色大国外交不断发展。
- 习近平外交思想为新时代中国特色大国外交提供根本遵循和行动指南，指引中国形成全方位、多层次、立体化的外交布局。
- 新中国外交始终坚持独立自主的基本立场，按照不同阶段国家发展需要自主决定外交方针。
- 新中国外交始终贯彻维护世界和平、促进共同发展的宗旨，以<span style="color:#c00000">促进世界和平与发展为基本目标</span>，坚持和平共处五项原则作为对外关系基本准则。

**条目拆解**：

1. **和平与发展仍是时代主题**
   - 卷面层级：海淀图片表格细则世界之变2分
   - 材料触发：题目追问新中国外交的变，材料呈现不同阶段世界格局和时代主题变化，就要想到和平与发展仍是时代主题及其对外交重点的影响。
   - 框架落点：时代背景 -> <span style="color:#c00000">和平与发展仍是时代主题</span>
   - 踩分词：<span style="color:#c00000">时代主题</span>；<span style="color:#c00000">和平与发展成为时代主题</span>；<span style="color:#c00000">顺应各国人民愿望</span>；<span style="color:#c00000">经济全球化深入发展</span>
   - 白话提醒：看到合作、倡议、中国方案为什么有现实必要，先判断是不是在问当今世界大背景。
   - 答题点自身积累（可替换表达，不必全背）：和平与发展仍是<span style="color:#c00000">时代主题</span>；顺应和平与发展的世界大势；中国做法符合和平与发展<span style="color:#c00000">时代主题</span>；各国人民渴望和平稳定和共同发展；回应治理赤字和共同挑战。
   - 卷面答案句（答案句变体）：和平与发展仍是<span style="color:#c00000">时代主题</span>，政治多极化、<span style="color:#c00000">经济全球化深入发展</span>，各国人民对和平稳定和共同发展仍有期待，这是新中国外交因势而变的重要时代背景。
2. **世界多极化深入发展与平等有序的世界多极化**
   - 卷面层级：图片image8变4分-世界之变2分
   - 材料触发：设问分析新中国外交的变，材料按历史阶段呈现中国面对的外部世界变化，就要想到世界格局与时代主题变化。
   - 框架落点：政治多极化 -> <span style="color:#c00000">世界多极化深入发展与平等有序的世界多极化</span>
   - 踩分词：<span style="color:#c00000">世界之变</span>；<span style="color:#c00000">和平与发展仍是时代主题</span>
   - 答题点自身积累（可替换表达，不必全背）：世界多极化深入发展与平等有序的世界多极化；政治多极化；经济全球化深入发展，和平与发展成为时代主题；<span style="color:#c00000">世界之变</span>；<span style="color:#c00000">和平与发展仍是时代主题</span>；国际局势变乱交织，面临诸多问题和挑战；局部动荡不断。
   - 卷面答案句（答案句变体）：新中国外交面对的时代背景不断变化，政治多极化、经济全球化深入发展，和平与发展成为时代主题，推动外交在不同阶段调整重点。
3. **当前国际竞争的实质是以经济和科技实力为基础的综合国力较量**
   - 卷面层级：图片image8变4分-中国之变实力1分
   - 材料触发：材料从站起来、富起来、强起来展示中国实力和地位变化，回答外交的变要说明中国自身实力基础变化。
   - 框架落点：理论 -> <span style="color:#c00000">当前国际竞争的实质是以经济和科技实力为基础的综合国力较量</span>
   - 踩分词：<span style="color:#c00000">国际影响力、话语权不断提升</span>
   - 答题点自身积累（可替换表达，不必全背）：中国综合国力不断增强，国际地位不断提升，承担越来越多国际责任；国际影响力；话语权不断提升；当前国际竞争的实质是以经济和科技实力为基础的综合国力较量；坚持创新驱动战略；综合国力较量；经济和科技实力。
   - 卷面答案句（答案句变体）：中国综合国力不断增强、国际地位不断提升，承担越来越多国际责任，推动中国特色大国外交不断发展。
4. **推动构建人类命运共同体**
   - 卷面层级：图片image8变4分-中国之变思想1分
   - 材料触发：材料写新时代外交理论和实践创新，形成习近平外交思想，说明外交指导思想随着中国和世界发展而变。
   - 框架落点：中国 -> <span style="color:#c00000">推动构建人类命运共同体</span>
   - 踩分词：<span style="color:#c00000">外交指导思想与时俱进</span>
   - 答题点自身积累（可替换表达，不必全背）：推动构建人类命运共同体；人类命运共同体理念；建设持久和平、普遍安全、共同繁荣、开放包容、清洁美丽的世界；四大全球倡议围绕发展、安全、文明、治理系统发力；同球共济；命运与共；周边命运共同体。
   - 卷面答案句（答案句变体）：习近平外交思想为新时代中国特色大国外交提供根本遵循和行动指南，指引中国形成全方位、多层次、立体化的外交布局。
5. **中国特色大国外交、独立自主和平外交政策与周边命运共同体**
   - 卷面层级：图片image8不变第1项1分
   - 材料触发：题目追问说明不变，材料虽然呈现外交任务变化，但外交服务国家性质和国家根本利益的基础没有变。
   - 框架落点：中国 -> <span style="color:#c00000">中国特色大国外交、独立自主和平外交政策与周边命运共同体</span>
   - 踩分词：<span style="color:#c00000">国家性质</span>
   - 答题点自身积累（可替换表达，不必全背）：中国特色大国外交；习近平外交思想；独立自主和平外交政策；维护世界和平、促进共同发展；和平共处五项原则；主权、安全、发展利益；周边命运共同体。
   - 卷面答案句（答案句变体）：新中国外交始终服务于我国人民民主专政的<span style="color:#c00000">国家性质</span>，以维护我国主权、安全和发展利益为重要依据。
6. **中国特色大国外交、独立自主和平外交政策与周边命运共同体**
   - 卷面层级：图片image8不变第2组基本立场2分
   - 材料触发：材料里的各阶段外交重点不同，但都体现中国自主决定对外方针，就要想到独立自主基本立场。
   - 框架落点：中国 -> <span style="color:#c00000">中国特色大国外交、独立自主和平外交政策与周边命运共同体</span>
   - 踩分词：<span style="color:#c00000">独立自主的和平外交政策</span>
   - 答题点自身积累（可替换表达，不必全背）：中国特色大国外交；习近平外交思想；独立自主和平外交政策；维护世界和平、促进共同发展；和平共处五项原则；主权、安全、发展利益；周边命运共同体。
   - 卷面答案句（答案句变体）：新中国外交始终坚持独立自主的基本立场，按照不同阶段国家发展需要自主决定外交方针。
7. **中国特色大国外交、独立自主和平外交政策与周边命运共同体**
   - 卷面层级：图片image8不变第2组宗旨目标准则
   - 材料触发：题目追问分析外交不变，材料里的不同阶段都围绕和平、发展、和平共处展开，就要想到中国外交政策宗旨、目标和基本准则。
   - 框架落点：中国 -> <span style="color:#c00000">中国特色大国外交、独立自主和平外交政策与周边命运共同体</span>
   - 踩分词：<span style="color:#c00000">促进世界和平与发展为基本目标</span>
   - 答题点自身积累（可替换表达，不必全背）：中国特色大国外交；习近平外交思想；独立自主和平外交政策；维护世界和平、促进共同发展；和平共处五项原则；主权、安全、发展利益；周边命运共同体。
   - 卷面答案句（答案句变体）：新中国外交始终贯彻维护世界和平、促进共同发展的宗旨，以<span style="color:#c00000">促进世界和平与发展为基本目标</span>，坚持和平共处五项原则作为对外关系基本准则。



---

### 8. 2026西城期末 Q20

**完整设问**：结合材料，运用《国际政治与经济》知识，阐释参与全球气候治理的中国实践。

**设问触发（题型通用）**：分析说明类题要同时写理论依据、材料信息和作用结论，不能只列术语。
**设问触发（本题独有）**：本题是全球气候治理题，答案分成共同利益、全球治理框架、中国行动三层；同一组理念不要一口气堆成一句。

**本题踩分点汇总**：
1. **<span style="color:#c00000">中国作为负责任大国积极参与全球气候治理</span>**
   - 卷面层级：角度一“中国实践是什么”第1点1分
   - 踩分词：<span style="color:#c00000">建设者</span>；<span style="color:#c00000">引领者</span>；<span style="color:#c00000">做负责任的大国</span>
   - 卷面句：中国积极参与全球气候治理，是全球气候治理的<span style="color:#c00000">建设者</span>、<span style="color:#c00000">引领者</span>，展现负责任大国担当。
2. **<span style="color:#c00000">坚持绿色发展理念，发挥有为政府和有效市场作用推进绿色低碳转型</span>**
   - 卷面层级：角度一“中国实践是什么”第2点1分
   - 使用边界：本题辅助点：用于完整理解本题，不放入本册六桶固定主框架。
   - 踩分词：<span style="color:#c00000">坚持绿色发展</span>；<span style="color:#c00000">新发展理念</span>；<span style="color:#c00000">有为政府+有效市场</span>
   - 卷面句：中国围绕能源结构、碳汇、减排、绿色交通、市场机制和气候适应推进NDC目标，<span style="color:#c00000">坚持绿色发展</span>理念，发挥有为政府和有效市场作用。
3. **<span style="color:#c00000">和平与发展仍是时代主题</span>**
   - 卷面层级：角度二“为什么参与”4选3第1项1分
   - 踩分词：<span style="color:#c00000">和平发展合作共赢是时代潮流</span>；<span style="color:#c00000">非传统安全威胁</span>
   - 卷面句：气候变化是需要各国共同应对的全球性问题，中国参与气候治理顺应和平、发展、合作、共赢的时代潮流。
4. **<span style="color:#c00000">国家间共同利益是国家合作的基础</span>**
   - 卷面层级：角度二“为什么参与”4选3第2项1分
   - 踩分词：<span style="color:#c00000">共同利益</span>
   - 卷面句：气候变化关系各国生存发展和可持续发展，国家间<span style="color:#c00000">共同利益</span>是合作的基础，各方需要在<span style="color:#c00000">共同利益</span>上推动全球气候治理合作。
5. **<span style="color:#c00000">共商共建共享的全球治理观</span>**
   - 卷面层级：角度二“为什么参与”4选3第3项1分
   - 踩分词：<span style="color:#c00000">命运共同体</span>；<span style="color:#c00000">全人类共同价值</span>；<span style="color:#c00000">正确义利观</span>；<span style="color:#c00000">共商共建共享</span>；<span style="color:#c00000">践行真正的多边主义</span>；<span style="color:#c00000">坚持互利共赢</span>
   - 卷面句：中国参与全球气候治理坚持<span style="color:#c00000">共商共建共享</span>，推动各方在联合国和《巴黎协定》框架下协商合作、共同应对气候变化。
6. **<span style="color:#c00000">自觉履行国际义务，遵循国际法，承担国际责任</span>**
   - 卷面层级：角度二“为什么参与”4选3第4项1分
   - 踩分词：<span style="color:#c00000">履行国际义务</span>；<span style="color:#c00000">遵循国际法</span>；<span style="color:#c00000">承担国际责任</span>
   - 卷面句：中国向联合国提交并落实NDC目标，是自觉<span style="color:#c00000">履行国际义务</span>、<span style="color:#c00000">遵循国际法</span>、<span style="color:#c00000">承担国际责任</span>的表现。
7. **<span style="color:#c00000">促进全球可持续发展，建设清洁世界</span>**
   - 卷面层级：角度三“效果怎么样”第1点1分
   - 使用边界：本题补充表达：可写进卷面结果或语言积累，不作为本册稳定核心点单独背。
   - 踩分词：<span style="color:#c00000">促进全球可持续发展</span>；<span style="color:#c00000">建设清洁世界</span>
   - 卷面句：中国气候治理实践有利于<span style="color:#c00000">促进全球可持续发展</span>，推动建设清洁美丽世界。
8. **<span style="color:#c00000">在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善</span>**
   - 卷面层级：角度三“效果怎么样”第2点1分
   - 踩分词：<span style="color:#c00000">维护联合国的核心作用</span>；<span style="color:#c00000">完善全球治理体系</span>
   - 卷面句：中国在联合国和《巴黎协定》框架下参与全球气候治理，有利于维护多边气候治理机制，推动全球气候治理体系完善。
9. **<span style="color:#c00000">贡献中国智慧、中国方案、中国力量与全球倡议体系</span>**
   - 卷面层级：角度三“效果怎么样”第3点1分
   - 踩分词：<span style="color:#c00000">贡献中国智慧</span>；<span style="color:#c00000">贡献中国力量</span>
   - 卷面句：中国以自身气候治理行动为全球治理<span style="color:#c00000">贡献中国智慧</span>和中国力量。

**本题命中框架**：
- 时代背景：<span style="color:#c00000">和平与发展仍是时代主题</span>
- 理论：<span style="color:#c00000">国家间共同利益是国家合作的基础</span>
- 政治多极化：<span style="color:#c00000">共商共建共享的全球治理观</span>
- 中国：<span style="color:#c00000">中国作为负责任大国积极参与全球气候治理</span>；<span style="color:#c00000">自觉履行国际义务，遵循国际法，承担国际责任</span>；<span style="color:#c00000">贡献中国智慧、中国方案、中国力量与全球倡议体系</span>
- 联合国：<span style="color:#c00000">在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善</span>
- 本题辅助/边界点：<span style="color:#c00000">中国 -> 促进全球可持续发展，建设清洁世界</span>；<span style="color:#c00000">中国 -> 坚持绿色发展理念，发挥有为政府和有效市场作用推进绿色低碳转型</span>

**整题汇总卷面答案**：
- **主干必写三层**：共同利益与共商共建共享；联合国和《巴黎协定》框架下的多边气候治理；中国提交并落实NDC（国家自主贡献目标）、贡献中国智慧中国方案。
- 气候变化关系各国生存发展和可持续发展，国家间<span style="color:#c00000">共同利益</span>是合作基础，中国坚持<span style="color:#c00000">共商共建共享</span>，推动各方协商合作、共同应对气候变化。
- 中国自觉履行《巴黎协定》下的国际义务，<span style="color:#c00000">遵循国际法</span>，在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善。
- 中国向联合国提交并落实2035年NDC（国家自主贡献目标），推进绿色低碳转型，积极参与全球气候治理，以自身行动<span style="color:#c00000">贡献中国智慧</span>、中国方案和中国力量。
- 中国积极参与全球气候治理，是全球气候治理的<span style="color:#c00000">建设者</span>、<span style="color:#c00000">引领者</span>，展现负责任大国担当。
- 中国围绕能源结构、碳汇、减排、绿色交通、市场机制和气候适应推进NDC目标，<span style="color:#c00000">坚持绿色发展</span>理念，发挥有为政府和有效市场作用。
- 气候变化是需要各国共同应对的全球性问题，中国参与气候治理顺应和平、发展、合作、共赢的时代潮流。
- 中国参与全球气候治理坚持<span style="color:#c00000">共商共建共享</span>，推动各方在联合国和《巴黎协定》框架下协商合作、共同应对气候变化。
- 中国气候治理实践有利于<span style="color:#c00000">促进全球可持续发展</span>，推动建设清洁美丽世界。
- 中国在联合国和《巴黎协定》框架下参与全球气候治理，有利于维护多边气候治理机制，推动全球气候治理体系完善。

**条目拆解**：

1. **中国作为负责任大国积极参与全球气候治理**
   - 卷面层级：角度一“中国实践是什么”第1点1分
   - 材料触发：题目问参与全球气候治理的中国实践，材料写中国向联合国提交2035年NDC目标并总结气候行动进展，就要想到中国在全球气候治理中的角色定位。
   - 框架落点：中国 -> <span style="color:#c00000">中国作为负责任大国积极参与全球气候治理</span>
   - 踩分词：<span style="color:#c00000">建设者</span>；<span style="color:#c00000">引领者</span>；<span style="color:#c00000">做负责任的大国</span>
   - 白话提醒：只在NDC、《巴黎协定》、绿色低碳转型、气候治理责任等材料信号明确时使用。
   - 答题点自身积累（可替换表达，不必全背）：中国作为负责任大国积极参与全球气候治理；积极履行气候治理国际责任；提交NDC行动目标；支持多边气候治理机制；推动绿色低碳转型。
   - 卷面答案句（答案句变体）：中国积极参与全球气候治理，是全球气候治理的<span style="color:#c00000">建设者</span>、<span style="color:#c00000">引领者</span>，展现负责任大国担当。
2. **坚持绿色发展理念，发挥有为政府和有效市场作用推进绿色低碳转型**
   - 卷面层级：角度一“中国实践是什么”第2点1分
   - 使用边界：本题辅助点：用于完整理解本题，不放入本册六桶固定主框架。
   - 材料触发：NDC表格呈现能源结构、碳汇、减排、绿色交通、市场机制和气候适应等实践，要求把具体治理行动概括为绿色发展和治理机制。
   - 框架落点：中国 -> <span style="color:#c00000">坚持绿色发展理念，发挥有为政府和有效市场作用推进绿色低碳转型</span>
   - 踩分词：<span style="color:#c00000">坚持绿色发展</span>；<span style="color:#c00000">新发展理念</span>；<span style="color:#c00000">有为政府+有效市场</span>
   - 答题点自身积累（可替换表达，不必全背）：<span style="color:#c00000">坚持绿色发展</span>理念，发挥有为政府和有效市场作用推进绿色低碳转型；<span style="color:#c00000">坚持绿色发展</span>；<span style="color:#c00000">新发展理念</span>；<span style="color:#c00000">有为政府+有效市场</span>。
   - 卷面答案句（答案句变体）：中国围绕能源结构、碳汇、减排、绿色交通、市场机制和气候适应推进NDC目标，<span style="color:#c00000">坚持绿色发展</span>理念，发挥有为政府和有效市场作用。
3. **和平与发展仍是时代主题**
   - 卷面层级：角度二“为什么参与”4选3第1项1分
   - 材料触发：材料把NDC置于巴黎协定和全球气候治理框架下，说明气候变化不是单一国家内部问题，而是需要合作应对的全球治理问题。
   - 框架落点：时代背景 -> <span style="color:#c00000">和平与发展仍是时代主题</span>
   - 踩分词：<span style="color:#c00000">和平发展合作共赢是时代潮流</span>；<span style="color:#c00000">非传统安全威胁</span>
   - 白话提醒：看到合作、倡议、中国方案为什么有现实必要，先判断是不是在问当今世界大背景。
   - 答题点自身积累（可替换表达，不必全背）：和平与发展仍是时代主题；顺应和平与发展的世界大势；中国做法符合和平与发展时代主题；各国人民渴望和平稳定和共同发展；回应治理赤字和共同挑战。
   - 卷面答案句（答案句变体）：气候变化是需要各国共同应对的全球性问题，中国参与气候治理顺应和平、发展、合作、共赢的时代潮流。
4. **国家间共同利益是国家合作的基础**
   - 卷面层级：角度二“为什么参与”4选3第2项1分
   - 材料触发：NDC和《巴黎协定》说明气候治理关系各国生存发展和可持续发展，各国存在共同利益。
   - 框架落点：理论 -> <span style="color:#c00000">国家间共同利益是国家合作的基础</span>
   - 踩分词：<span style="color:#c00000">共同利益</span>
   - 答题点自身积累（可替换表达，不必全背）：国家间<span style="color:#c00000">共同利益</span>是国家合作的基础；<span style="color:#c00000">共同利益</span>；<span style="color:#c00000">共同利益</span>是国家合作的基础；理念蕴含普遍价值，能够形成共识并促成合作和发展；理念蕴含普遍价值；全人类共同价值；人类<span style="color:#c00000">共同利益</span>。
   - 卷面答案句（答案句变体）：气候变化关系各国生存发展和可持续发展，国家间<span style="color:#c00000">共同利益</span>是合作的基础，各方需要在<span style="color:#c00000">共同利益</span>上推动全球气候治理合作。
5. **共商共建共享的全球治理观**
   - 卷面层级：角度二“为什么参与”4选3第3项1分
   - 材料触发：全球气候治理需要在联合国和《巴黎协定》框架下协商合作，各国共同参与而不是单方主导。
   - 框架落点：政治多极化 -> <span style="color:#c00000">共商共建共享的全球治理观</span>
   - 踩分词：<span style="color:#c00000">命运共同体</span>；<span style="color:#c00000">全人类共同价值</span>；<span style="color:#c00000">正确义利观</span>；<span style="color:#c00000">共商共建共享</span>；<span style="color:#c00000">践行真正的多边主义</span>；<span style="color:#c00000">坚持互利共赢</span>
   - 白话提醒：不要只背六个字，卷面上要写出各国共同讨论、共同建设、共同分享治理成果。
   - 答题点自身积累（可替换表达，不必全背）：<span style="color:#c00000">共商共建共享</span>的全球治理观；共同商量、共同建设、共同分享；各国平等参与全球治理；建立公平合理的全球治理体系。
   - 卷面答案句（答案句变体）：中国参与全球气候治理坚持<span style="color:#c00000">共商共建共享</span>，推动各方在联合国和《巴黎协定》框架下协商合作、共同应对气候变化。
6. **自觉履行国际义务，遵循国际法，承担国际责任**
   - 卷面层级：角度二“为什么参与”4选3第4项1分
   - 材料触发：题干说明NDC是巴黎协定核心且缔约方每五年提交行动目标，中国提交2035目标体现对国际机制和国际承诺的履行。
   - 框架落点：中国 -> <span style="color:#c00000">自觉履行国际义务，遵循国际法，承担国际责任</span>
   - 踩分词：<span style="color:#c00000">履行国际义务</span>；<span style="color:#c00000">遵循国际法</span>；<span style="color:#c00000">承担国际责任</span>
   - 答题点自身积累（可替换表达，不必全背）：自觉<span style="color:#c00000">履行国际义务</span>，<span style="color:#c00000">遵循国际法</span>，<span style="color:#c00000">承担国际责任</span>；<span style="color:#c00000">履行国际义务</span>；<span style="color:#c00000">遵循国际法</span>；<span style="color:#c00000">承担国际责任</span>。
   - 卷面答案句（答案句变体）：中国向联合国提交并落实NDC目标，是自觉<span style="color:#c00000">履行国际义务</span>、<span style="color:#c00000">遵循国际法</span>、<span style="color:#c00000">承担国际责任</span>的表现。
7. **促进全球可持续发展，建设清洁世界**
   - 卷面层级：角度三“效果怎么样”第1点1分
   - 使用边界：本题补充表达：可写进卷面结果或语言积累，不作为本册稳定核心点单独背。
   - 材料触发：NDC目标覆盖能源、碳汇、减排、交通、市场机制和适应气候变化，材料指向全球生态文明和可持续发展效果。
   - 框架落点：中国 -> <span style="color:#c00000">促进全球可持续发展，建设清洁世界</span>
   - 踩分词：<span style="color:#c00000">促进全球可持续发展</span>；<span style="color:#c00000">建设清洁世界</span>
   - 答题点自身积累（可替换表达，不必全背）：<span style="color:#c00000">促进全球可持续发展</span>，<span style="color:#c00000">建设清洁世界</span>；<span style="color:#c00000">促进全球可持续发展</span>；<span style="color:#c00000">建设清洁世界</span>。
   - 卷面答案句（答案句变体）：中国气候治理实践有利于<span style="color:#c00000">促进全球可持续发展</span>，推动建设清洁美丽世界。
8. **在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善**
   - 卷面层级：角度三“效果怎么样”第2点1分
   - 材料触发：NDC属于《巴黎协定》框架下的气候行动目标，中国提交目标体现对多边气候治理机制的支持。
   - 框架落点：联合国 -> <span style="color:#c00000">在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善</span>
   - 踩分词：<span style="color:#c00000">维护联合国的核心作用</span>；<span style="color:#c00000">完善全球治理体系</span>
   - 答题点自身积累（可替换表达，不必全背）：在联合国和《巴黎协定》框架下维护多边气候治理机制，推动全球治理体系完善；<span style="color:#c00000">维护联合国的核心作用</span>；<span style="color:#c00000">完善全球治理体系</span>。
   - 卷面答案句（答案句变体）：中国在联合国和《巴黎协定》框架下参与全球气候治理，有利于维护多边气候治理机制，推动全球气候治理体系完善。
9. **贡献中国智慧、中国方案、中国力量与全球倡议体系**
   - 卷面层级：角度三“效果怎么样”第3点1分
   - 材料触发：中国提出NDC目标并推进低碳转型、市场机制和气候适应，说明中国用行动为全球气候治理提供方案和支撑。
   - 框架落点：中国 -> <span style="color:#c00000">贡献中国智慧、中国方案、中国力量与全球倡议体系</span>
   - 踩分词：<span style="color:#c00000">贡献中国智慧</span>；<span style="color:#c00000">贡献中国力量</span>
   - 答题点自身积累（可替换表达，不必全背）：<span style="color:#c00000">贡献中国智慧</span>、中国方案、中国力量与全球倡议体系；<span style="color:#c00000">贡献中国智慧</span>；中国方案；勇于大国担当；中国智慧；大国担当；大国责任与担当。
   - 卷面答案句（答案句变体）：中国以自身气候治理行动为全球治理<span style="color:#c00000">贡献中国智慧</span>和中国力量。



---

### 38. 2026通州期末 Q20

**完整设问**：结合材料，运用《当代国际政治与经济》知识，谈谈你对“全球治理倡议正逢其时、指引方向、彰显担当”的理解。

**设问触发（题型通用）**：追问意义、价值或担当时，分清对象：对中国、对合作方、对世界秩序或全球治理分别作答。
**设问触发（本题独有）**：本题设问自带三层：正逢其时看时代背景，指引方向看国际秩序和全球治理，彰显担当看中国方案与大国责任，三层不要合写。

**本题踩分点汇总**：
1. **<span style="color:#c00000">共商共建共享的全球治理观</span>**
   - 卷面层级：作答方向第1点1分
   - 踩分词：<span style="color:#c00000">共商共建共享的全球治理观</span>
   - 卷面句：全球治理倡议秉持<span style="color:#c00000">共商共建共享的全球治理观</span>，推动各国平等参与全球治理体系改革和建设，为完善全球治理提供中国方向。
2. **<span style="color:#c00000">和平与发展仍是时代主题</span>**
   - 卷面层级：通州作答方向第2点2分
   - 踩分词：<span style="color:#c00000">时代主题</span>；<span style="color:#c00000">和平与发展成为时代主题</span>；<span style="color:#c00000">顺应各国人民愿望</span>；<span style="color:#c00000">经济全球化深入发展</span>
   - 卷面句：和平与发展仍是<span style="color:#c00000">时代主题</span>，世界各国面对治理赤字和共同挑战，需要主权平等、国际法治、多边主义和以人为本的治理方向；全球治理倡议回应这种时代需要，因而正逢其时。
3. **<span style="color:#c00000">《联合国宪章》宗旨和原则</span>**
   - 卷面层级：作答方向第3点1分
   - 踩分词：<span style="color:#c00000">符合《联合国宪章》</span>
   - 卷面句：全球治理倡议<span style="color:#c00000">符合《联合国宪章》</span>宗旨和原则，在维护国际和平与安全、促进国际合作上具有正当性基础。
4. **<span style="color:#c00000">推动国际关系民主化，坚持真正的多边主义，推动国际秩序朝公正合理方向发展</span>**
   - 卷面层级：作答方向第4点任一点1分共2分
   - 踩分词：<span style="color:#c00000">推动构建更加公正合理的国际新秩序</span>；<span style="color:#c00000">国际关系民主化</span>；<span style="color:#c00000">多边主义</span>
   - 卷面句：全球治理倡议倡导<span style="color:#c00000">国际关系民主化</span>、践行<span style="color:#c00000">多边主义</span>，<span style="color:#c00000">推动构建更加公正合理的国际新秩序</span>，使全球治理体系朝公平合理方向发展。
5. **<span style="color:#c00000">坚持正确义利观，在发展合作中义利相兼、互利共赢</span>**
   - 卷面层级：通州作答方向第4点可选组
   - 踩分词：<span style="color:#c00000">正确义利观</span>；<span style="color:#c00000">兼顾他国合理关切</span>
   - 卷面句：全球治理倡议坚持<span style="color:#c00000">正确义利观</span>，既回应国际社会共同治理需求，又兼顾各方合理利益，展现中国义利相兼、互利共赢的担当。
6. **<span style="color:#c00000">推动构建人类命运共同体</span>**
   - 卷面层级：通州作答方向第5点1分
   - 踩分词：<span style="color:#c00000">人类命运共同体</span>
   - 卷面句：全球治理倡议回应治理赤字和共同挑战，服务于推动构建<span style="color:#c00000">人类命运共同体</span>，为完善全球治理贡献中国力量。
7. **<span style="color:#c00000">贡献中国智慧、中国方案、中国力量与全球倡议体系</span>**
   - 卷面层级：作答方向第6点1分
   - 踩分词：<span style="color:#c00000">中国智慧</span>；<span style="color:#c00000">中国方案</span>；<span style="color:#c00000">大国担当</span>
   - 卷面句：全球治理倡议作为中国提供的重要国际公共产品，贡献<span style="color:#c00000">中国智慧</span>、<span style="color:#c00000">中国方案</span>，展现中国勇于承担国际责任的<span style="color:#c00000">大国担当</span>。

**本题命中框架**：
- 时代背景：<span style="color:#c00000">和平与发展仍是时代主题</span>
- 政治多极化：<span style="color:#c00000">共商共建共享的全球治理观</span>；<span style="color:#c00000">推动国际关系民主化，坚持真正的多边主义，推动国际秩序朝公正合理方向发展</span>
- 中国：<span style="color:#c00000">坚持正确义利观，在发展合作中义利相兼、互利共赢</span>；<span style="color:#c00000">推动构建人类命运共同体</span>；<span style="color:#c00000">贡献中国智慧、中国方案、中国力量与全球倡议体系</span>
- 联合国：<span style="color:#c00000">《联合国宪章》宗旨和原则</span>

**整题汇总卷面答案**：
- 全球治理倡议秉持<span style="color:#c00000">共商共建共享的全球治理观</span>，推动各国平等参与全球治理体系改革和建设，为完善全球治理提供中国方向。
- 和平与发展仍是<span style="color:#c00000">时代主题</span>，世界各国面对治理赤字和共同挑战，需要主权平等、国际法治、多边主义和以人为本的治理方向；全球治理倡议回应这种时代需要，因而正逢其时。
- 全球治理倡议<span style="color:#c00000">符合《联合国宪章》</span>宗旨和原则，在维护国际和平与安全、促进国际合作上具有正当性基础。
- 全球治理倡议倡导<span style="color:#c00000">国际关系民主化</span>、践行<span style="color:#c00000">多边主义</span>，<span style="color:#c00000">推动构建更加公正合理的国际新秩序</span>，使全球治理体系朝公平合理方向发展。
- 全球治理倡议坚持<span style="color:#c00000">正确义利观</span>，既回应国际社会共同治理需求，又兼顾各方合理利益，展现中国义利相兼、互利共赢的担当。
- 全球治理倡议回应治理赤字和共同挑战，服务于推动构建<span style="color:#c00000">人类命运共同体</span>，为完善全球治理贡献中国力量。
- 全球治理倡议作为中国提供的重要国际公共产品，贡献<span style="color:#c00000">中国智慧</span>、<span style="color:#c00000">中国方案</span>，展现中国勇于承担国际责任的<span style="color:#c00000">大国担当</span>。
- 主干必写：先写3到4个最稳层次；可选补充看分值和材料；时间不足时删重复材料句，保留术语、材料对接和回扣设问。

**条目拆解**：

1. **共商共建共享的全球治理观**
   - 卷面层级：作答方向第1点1分
   - 材料触发：设问追问全球治理倡议为什么能指引方向，材料把倡议定位为完善全球治理的中国方案，就要想到全球治理应该由各国共同商量、共同建设、共同分享这一治理观。
   - 框架落点：政治多极化 -> <span style="color:#c00000">共商共建共享的全球治理观</span>
   - 踩分词：<span style="color:#c00000">共商共建共享的全球治理观</span>
   - 白话提醒：不要只背六个字，卷面上要写出各国共同讨论、共同建设、共同分享治理成果。
   - 答题点自身积累（可替换表达，不必全背）：<span style="color:#c00000">共商共建共享的全球治理观</span>；共同商量、共同建设、共同分享；各国平等参与全球治理；建立公平合理的全球治理体系。
   - 卷面答案句（答案句变体）：全球治理倡议秉持<span style="color:#c00000">共商共建共享的全球治理观</span>，推动各国平等参与全球治理体系改革和建设，为完善全球治理提供中国方向。
2. **和平与发展仍是时代主题**
   - 卷面层级：通州作答方向第2点2分
   - 材料触发：设问第一层是“正逢其时”，材料围绕全球治理倡议回应治理赤字、倡导主权平等、国际法治、多边主义和以人为本，就要先写和平与发展时代主题和共同治理需求。
   - 框架落点：时代背景 -> <span style="color:#c00000">和平与发展仍是时代主题</span>
   - 踩分词：<span style="color:#c00000">时代主题</span>；<span style="color:#c00000">和平与发展成为时代主题</span>；<span style="color:#c00000">顺应各国人民愿望</span>；<span style="color:#c00000">经济全球化深入发展</span>
   - 白话提醒：看到合作、倡议、中国方案为什么有现实必要，先判断是不是在问当今世界大背景。
   - 答题点自身积累（可替换表达，不必全背）：和平与发展仍是<span style="color:#c00000">时代主题</span>；顺应和平与发展的世界大势；中国做法符合和平与发展<span style="color:#c00000">时代主题</span>；各国人民渴望和平稳定和共同发展；回应治理赤字和共同挑战。
   - 卷面答案句（答案句变体）：和平与发展仍是<span style="color:#c00000">时代主题</span>，世界各国面对治理赤字和共同挑战，需要主权平等、国际法治、多边主义和以人为本的治理方向；全球治理倡议回应这种时代需要，因而正逢其时。
3. **《联合国宪章》宗旨和原则**
   - 卷面层级：作答方向第3点1分
   - 材料触发：材料把全球治理倡议同联合国宪章宗旨和原则相连，设问追问倡议的方向性和正当性，就要想到联合国宪章框架。
   - 框架落点：联合国 -> <span style="color:#c00000">《联合国宪章》宗旨和原则</span>
   - 踩分词：<span style="color:#c00000">符合《联合国宪章》</span>
   - 答题点自身积累（可替换表达，不必全背）：《联合国宪章》宗旨和原则；<span style="color:#c00000">符合《联合国宪章》</span>宗旨和原则；<span style="color:#c00000">符合《联合国宪章》</span>；坚定维护以联合国为核心的国际体系；维护《联合国宪章》宗旨和原则；支持联合国工作；支持联合国改革。
   - 卷面答案句（答案句变体）：全球治理倡议<span style="color:#c00000">符合《联合国宪章》</span>宗旨和原则，在维护国际和平与安全、促进国际合作上具有正当性基础。
4. **推动国际关系民主化，坚持真正的多边主义，推动国际秩序朝公正合理方向发展**
   - 卷面层级：作答方向第4点任一点1分共2分
   - 材料触发：设问中的指引方向要求回答全球治理秩序应朝哪里走，材料里的主权平等、国际法治和多边主义就要想到国际秩序方向术语。
   - 框架落点：政治多极化 -> <span style="color:#c00000">推动国际关系民主化，坚持真正的多边主义，推动国际秩序朝公正合理方向发展</span>
   - 踩分词：<span style="color:#c00000">推动构建更加公正合理的国际新秩序</span>；<span style="color:#c00000">国际关系民主化</span>；<span style="color:#c00000">多边主义</span>
   - 答题点自身积累（可替换表达，不必全背）：推动<span style="color:#c00000">国际关系民主化</span>，坚持真正的<span style="color:#c00000">多边主义</span>，推动国际秩序朝公正合理方向发展；推动构建国际新秩序；倡导<span style="color:#c00000">国际关系民主化</span>；践行<span style="color:#c00000">多边主义</span>；<span style="color:#c00000">推动构建更加公正合理的国际新秩序</span>；<span style="color:#c00000">国际关系民主化</span>；<span style="color:#c00000">多边主义</span>。
   - 卷面答案句（答案句变体）：全球治理倡议倡导<span style="color:#c00000">国际关系民主化</span>、践行<span style="color:#c00000">多边主义</span>，<span style="color:#c00000">推动构建更加公正合理的国际新秩序</span>，使全球治理体系朝公平合理方向发展。
5. **坚持正确义利观，在发展合作中义利相兼、互利共赢**
   - 卷面层级：通州作答方向第4点可选组
   - 材料触发：全球治理倡议既回应国际社会共同治理需求，又强调兼顾各方合理利益，就要想到正确义利观和义利相兼、互利共赢。
   - 框架落点：中国 -> <span style="color:#c00000">坚持正确义利观，在发展合作中义利相兼、互利共赢</span>
   - 踩分词：<span style="color:#c00000">正确义利观</span>；<span style="color:#c00000">兼顾他国合理关切</span>
   - 白话提醒：义是国际道义和共同责任，利是各方合理利益；这点常用来防止答案写成中国单方施予。
   - 答题点自身积累（可替换表达，不必全背）：坚持<span style="color:#c00000">正确义利观</span>；义利相兼、互利共赢；<span style="color:#c00000">兼顾他国合理关切</span>；在国际合作中既讲共同利益又重国际道义。
   - 卷面答案句（答案句变体）：全球治理倡议坚持<span style="color:#c00000">正确义利观</span>，既回应国际社会共同治理需求，又兼顾各方合理利益，展现中国义利相兼、互利共赢的担当。
6. **推动构建人类命运共同体**
   - 卷面层级：通州作答方向第5点1分
   - 材料触发：全球治理倡议回应治理赤字和共同挑战，并把中国方案提供给国际社会，就要想到推动构建人类命运共同体。
   - 框架落点：中国 -> <span style="color:#c00000">推动构建人类命运共同体</span>
   - 踩分词：<span style="color:#c00000">人类命运共同体</span>
   - 答题点自身积累（可替换表达，不必全背）：推动构建<span style="color:#c00000">人类命运共同体</span>；<span style="color:#c00000">人类命运共同体</span>理念；建设持久和平、普遍安全、共同繁荣、开放包容、清洁美丽的世界；四大全球倡议围绕发展、安全、文明、治理系统发力；同球共济；命运与共；周边命运共同体。
   - 卷面答案句（答案句变体）：全球治理倡议回应治理赤字和共同挑战，服务于推动构建<span style="color:#c00000">人类命运共同体</span>，为完善全球治理贡献中国力量。
7. **贡献中国智慧、中国方案、中国力量与全球倡议体系**
   - 卷面层级：作答方向第6点1分
   - 材料触发：材料把全球治理倡议写成中国向世界提供的重要公共产品，设问中的彰显担当就要想到中国智慧、中国方案和大国担当。
   - 框架落点：中国 -> <span style="color:#c00000">贡献中国智慧、中国方案、中国力量与全球倡议体系</span>
   - 踩分词：<span style="color:#c00000">中国智慧</span>；<span style="color:#c00000">中国方案</span>；<span style="color:#c00000">大国担当</span>
   - 答题点自身积累（可替换表达，不必全背）：贡献<span style="color:#c00000">中国智慧</span>、<span style="color:#c00000">中国方案</span>、中国力量与全球倡议体系；贡献<span style="color:#c00000">中国智慧</span>；<span style="color:#c00000">中国方案</span>；勇于<span style="color:#c00000">大国担当</span>；<span style="color:#c00000">中国智慧</span>；<span style="color:#c00000">大国担当</span>；大国责任与担当。
   - 卷面答案句（答案句变体）：全球治理倡议作为中国提供的重要国际公共产品，贡献<span style="color:#c00000">中国智慧</span>、<span style="color:#c00000">中国方案</span>，展现中国勇于承担国际责任的<span style="color:#c00000">大国担当</span>。

