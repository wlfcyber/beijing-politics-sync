# 监管检查表（必修四哲学从0重跑）

> 本表反映 2026-05-02 收尾阶段的实际状态。SOURCE_LEDGER 共 54 套，全部已交付 entries 与 suite_reports，2026_石景山_期末 按 SKILL 用户确认排除并已在 COVERAGE_MATRIX 标记为 `excluded-by-skill-rule`。学生版 346 条目。

## 通用

- [x] 学生版按飞哥框架节点组织，不按套卷流水账（synthesize 输出 5 大类 33 节点）
- [x] 学生版主观题在前、选择题在后；同类按 海淀-西城-东城-朝阳-丰台-其他区
- [x] 学生版字段顺序 `材料触发点 → 设问 → 为什么能想到 → 答案落点`
- [x] 学生版无来源路径、line/file/slide id、OCR/debug、`yes/pass/filled/correct_option_chain`、审计/答案来源话术（`scripts/quality_check.py` 0 issues；学生版 MD 独立 `rg` 0 命中；WordSaved.docx 段落扫描 0 命中）
- [x] 设问栏只装真正问句；材料正文留在材料触发点栏
- [x] 答案落点为可入答案的句子，不是 "回应设问/服务设问/可从某角度作答" 等元话术
- [x] 高风险哲学词（辩证否定/量变质变/两点论与重点论/主次矛盾/矛盾主次方面/价值观导向）有评分原文等值表述
- [x] 证据等级不得虚标（boundary_note 已记录；普通参考答案不冒充 rubric-formal）
- [x] 文化题/纯文化原理一律边界排除，不进入哲学主框架

## 硬样本

- [x] `2026_海淀_一模` 第16题进入「物质决定意识」节点，仅写 "物质决定意识/必要性"，不写 "意识反作用于物质"
- [x] 同题独立进入「主观能动性 / 意识的能动作用」节点
- [x] 第16题设问栏只装 "有人说，人文学科在人工智能时代具有不可替代的价值。结合材料，运用《哲学与文化》知识，谈谈对这一观点的认识。"
- [x] `2024_东城_一模` 第18题第（3）问（传统产业-未来产业）进入「辩证否定 / 守正创新」（target_node=辩证法/辩证否定 / 守正创新；boundary_note 含《逻辑与思维》模块边界注释）

## 套卷闭环

- [x] SOURCE_LEDGER 54 套全部交付 entries（`audit/entries/*.jsonl` 54 个）
- [x] SOURCE_LEDGER 54 套全部交付 suite_reports（`suite_reports/*.md` 54 个）
- [x] `COVERAGE_MATRIX.csv` 350 行已映射 ledger 54 套；新增 1 行 `2026_石景山_期末` 标 `excluded-by-skill-rule`，唯一套卷数 55
- [x] `audit/证据索引.csv`、`audit/覆盖验收表.csv`、`audit/问题与边界清单.md` 与 entries 交叉一致
- [x] 边界状态使用受控词：`included` / `module-boundary-excluded` / `reference-only` / `objective-key-only` / `excluded-by-skill-rule`
- [x] `PROGRESS.md` 已更新为收尾终态

## 最终交付

- [x] `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.md` 同步存在
- [x] `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.docx` 同步存在
- [x] `outputs/2026北京高考政治哲学宝典---三年模拟全触发全链条_学生版.WordSaved.docx` 同步存在（Microsoft Word 打开+保存后副本）
- [x] Word 首页只有标题与"飞哥正志讲堂"署名（python-docx 抽检 5/14 段段位锁定）
- [x] Word 第二页留前言空位（"（此页留位，由飞哥本人填写。）"）
- [x] `audit/word_validation/claude_student.WordSaved.docx` 与 `audit/word_validation/quicklook/claude_student.docx.png` 在位
- [ ] Word 导出 PDF 未成功（AppleEvent 超时）— 按督工补丁 C 该项不作为硬阻塞
- [x] 漫画/图片题嵌入：以 entries `image_path` 与 source_excerpts 留索引；学生版按文字触发链落地（无可嵌入漫画原图的硬要求未达项）

## 收尾门槛

- [x] `python3 scripts/quality_check.py` 扫描 346 条 0 issues
- [x] 学生版 Markdown 独立禁词 `rg` 0 命中
- [x] WordSaved.docx 段落级独立禁词扫描 0 命中
- [x] SOURCE_LEDGER / audit/entries / suite_reports / COVERAGE_MATRIX 套卷集合对齐（ledger 54 == entries 54 == reports 54；coverage 含 ledger 54 + 1 excluded）
- [x] `FINAL_ACCEPTANCE_REPORT.md` 已重写为本轮真实终态
