# Patcher Review

## Scope read

角色：补丁者/Patcher。

本轮为“预补丁审查”：当前目录中尚未出现最终合并稿或新版框架正式成稿，`threads/` 下只有 `framework_architect_findings.md`。因此本报告不做最终验收，只检查旧课件框架与候选新框架中容易遗漏的迁移风险，尤其是：

- 一则材料同时触发多个答题点，却被新版框架只放进一个教材目录节点。
- 案例横跨实体法、程序法、法治意义、主体关系和救济路径，却被按章节硬切。
- 只按教材目录堆叠，导致学生遇到新材料时不能完成“材料事实 -> 法律关系 -> 规则要件 -> 责任/救济 -> 法治意义”的迁移。

证据边界：当前只针对用户提供的去年课件 PDF、PDF 文本抽取、页图和已出现的框架候选稿做审查。本阶段完成条件不应要求完整北京真题题库闭环、官方评分细则穷尽、错肢库闭环或 district corpus 全覆盖；但这些都应作为后续验证边界记录，不能在最终稿中被虚假宣称已经完成。

## Files inspected

- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\USER_FRAMEWORK.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\pdf_text_by_page.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\contact_sheets\contact_sheet_1.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\contact_sheets\contact_sheet_2.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_04.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_16.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_22.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_23.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_25.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_26.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_30.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_31.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\sources\page_images\page_35.png`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\threads\framework_architect_findings.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\TASK_BRIEF.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\PROGRESS.md`
- `C:\Users\Administrator\Desktop\飞哥的政治庄园\reports\law_life_framework_2026-04-25_1407\DECISION_LOG.md`

## Findings

1. `USER_FRAMEWORK.md` 目前只是占位说明，没有保存可直接迁移的用户原始框架文本。实际旧框架只能从 PDF 课件、页图和架构师报告还原。新版合并时必须明确“旧框架来源是课件 PDF”，不能伪称已经有完整用户文字框架。

2. 旧框架的真实强项不是教材目录本身，而是“法条基础 + 法治意义”的双入口。p5-p8 显示课件反复强调高考难点在二者组合；新版不能把“法治意义”放成尾部口号库，而要做成每个案例都能回扣材料事实的触发轴。

3. p23 东城期末滑梯案是一材多点的典型：物业同意、公共区域、免费玩耍、雨后积水、摔伤、健康权、因果关系、过错、法院判决、在法内/法外、社会公正均在同一材料内。若只归入“侵权责任”，会漏掉法治意义、司法公正、社会公德和行为评价层。

4. p30 海淀一模虚拟数字人案不能只归入“知识产权”。同一材料至少触发著作权、侵权、不正当竞争、虚假/引人误解宣传、企业竞争秩序、保护创作和激发创新。候选新框架如保留“知识产权与创新秩序”，还必须建立与“不正当竞争/市场经营”的交叉索引。

5. p31 西城二模食品安全案不能只归入“消费者权益”。同一材料同时触发食品安全法、消费者知情权/安全消费权、经营者依法诚信经营、惩罚性赔偿边界、合理消费需求、市场秩序、社会公共利益和社会主义核心价值观。新版要把“赔偿边界”和“意义层”并列处理。

6. p35 老旧社区纠纷“三聚焦”工作法横跨基层治理、人民调解、法律工作室、司法赋能、法治思维、德治法治、基层民主、多元共治和矛盾纠纷化解机制。若只放在“多元纠纷解决机制”末尾，会漏掉《法律与生活》与基层治理/法治社会意义的迁移接口。

7. p04 交通事故材料同时触发机动车交通事故责任、好意同乘/减责、侵权损害赔偿和现实意义。它不是单纯“侵权构成”例题，必须提示学生先区分责任成立，再判断是否减轻责任，最后回到公平、友善、互助等社会效果。

8. p22 环境污染案体现“侵权构成 + 无过错责任 + 举证责任倒置 + 因果关系抗辩”。新版若只写“一般侵权四要件”，会把特殊侵权题的得分路径压平；应单列特殊归责和证明责任触发条件。

9. p16 合同诉状示例把合同履行、合同变更/单方变更、违约责任和民事诉讼表达放在一起。新版不能把程序法只放在最后一章；凡是要求写起诉状、诉讼请求、事实与理由的材料，都要在实体规则旁挂接“程序表达”节点。

10. p25-p26 家庭养老/模拟庭审材料并非纯家庭法。它同时触发成年子女赡养义务、老人合法权益、诉讼代理人角色、传统美德、核心价值观、法律对道德建设的促进作用、社会公平正义和家庭和谐。新版必须避免把“家庭”封闭成亲属法目录。

11. 旧课件中“企业”不是稳定法律分类，而是场景入口。企业与劳动者、消费者、其他企业分别对应劳动争议、消费者权益、不正当竞争/知识产权。候选稿如果保留“劳动、消费与市场经营”板块，应明确企业只是主体/场景，不是唯一归位标准。

12. 当前候选稿已经提出“一核三轴五步”和“材料触发链”，方向正确；但最终合并时还缺一个可操作的“多点触发清单”：每个典型材料至少记录主归位、辅归位、意义归位、程序归位、错项风险，防止主线合并时又退回目录堆叠。

13. PDF 文本层质量不稳定，p04、p16、p22 等关键页文本抽取不足或空白，必须以页图为准。最终稿引用这些页时，应标注“页图核对”或保留页面证据，不应只依赖 `pdf_text_by_page.md`。

14. PDF 中出现“答案”“细则”样式材料，但当前证据来源仍是课件 PDF，不是独立官方评分细则库。可以用于框架迁移、课堂样例和得分结构启发，不能作为“已验证正式评分规则”。

## Merge candidates

建议主线程在合并新版框架时补入以下结构，而不是只合并章节目录：

1. 增加“材料多点触发登记表”。字段建议为：页码/案例、材料事实、主归位、辅归位、程序归位、法治意义归位、易错点、证据状态。

2. 在每个知识板块下加入“触发条件”，不要只列知识点。例如：环境污染/产品责任/动物致害触发无过错或特殊举证；写诉状触发诉讼请求和事实理由；涉及公共利益和规则效果时触发法治意义。

3. 建立跨模块索引：
   - 知识产权 <-> 不正当竞争 <-> 市场秩序。
   - 消费者权益 <-> 食品安全 <-> 惩罚性赔偿 <-> 诚信经营。
   - 家庭赡养 <-> 诉讼角色 <-> 传统美德/核心价值观。
   - 侵权责任 <-> 特殊归责 <-> 举证责任 <-> 法治意义。
   - 多元纠纷解决 <-> 基层治理 <-> 法治与德治。

4. 将“法治意义”改造成事实触发库。每个意义点都要回答：保护谁的权益、维护哪类秩序、平衡哪些利益、体现哪种治理效果或价值，而不是泛写“维护公平正义”。

5. 将“选择题错项库入口”并入框架：主体错、权利名错、要件错、归责原则错、证明责任错、程序角色错、救济方式错、意义脱离材料。旧课件已有疑难点，但还需要系统化。

6. 给答案/细则样式材料加证据标签：`课件样例`、`答案样式`、`细则样式`、`非独立官方评分细则`。后续题库验证前，不得把这些内容写成正式 rubric 来源。

7. 新版框架正式稿中应保留“本阶段边界”段落：本稿完成的是课件 PDF 内部框架重建与迁移，不等于全题库、全区模、官方评分细则闭环。

## Blockers

1. 最终合并稿尚未出现，当前只能做预补丁审查，不能判定最终框架 pass。

2. `USER_FRAMEWORK.md` 未包含真实用户框架正文，旧框架复原依赖 PDF 页图和架构师报告；主线程合并时必须补记来源边界。

3. 当前证据只覆盖课件 PDF。完整题库闭环、正式评分细则验证、错肢库迁移、学生作答样本反向验证均未进入本阶段范围；这不是本阶段失败条件，但必须在最终验收中记录为证据边界。

4. PDF 文本抽取质量不足，若主线程后续只读 `pdf_text_by_page.md`，会漏掉 p04、p16、p22、p23、p30、p31、p35 等页图中的关键批注和细则结构。

## Decision: needs-merge

理由：候选新框架方向可用，但最终合并稿尚未出现；且新版必须补入“一材多点触发登记表”、跨模块索引、事实触发式法治意义库和证据标签，才能避免再次变成教材目录堆叠。当前不应判定 pass，也不构成 blocked；主线程应先合并上述补丁，再交由监管者做证据边界和验收判断。
