# Worker Batch04D 朝阳扩展 Triage

role: Codex A / 劳动者
scope: Batch04D 朝阳扩展 source triage and candidate extraction
status: prelim_written_for_patcher_governor

## 执行说明

- 真实 Worker 子线程 `019ded69-e4de-7cb1-b80d-64b55bacdd62` 在本轮不可用；`send_input` 返回 not found，`resume_agent` 因 thread limit 失败。
- 为避免停工，Codex A 本地执行劳动者角色，并把证据、边界和候选写成可审计文件。
- 本轮没有修改 `07_student_doc/`，没有生成 Word/PDF，没有宣布 final。
- ClaudeCode B 已用 `xuanbiyi_claudecode_batch04D_20260503` screen 重新启动，作为独立 B 线继续处理朝阳扩展；本文件是 Codex A 本地劳动者线。

## 强候选

### 2025朝阳二模 Q21

- paper_source_id: `SRC_d411e2158d47`
- scoring_source_id: `SRC_436f84dc1edf`
- evidence: P0 formal scoring docx + P3 paper text
- full_prompt_anchor: `21.(8分) 努力开创周边工作新局面……结合材料，运用《当代国际政治与经济》知识，说明我国为什么要努力开创周边工作新局面。`
- scoring_anchor:
  - 中国的发展需要 3分：周边国家众多；实现发展繁荣；维护国家安全；运筹外交全局；推动构建人类命运共同体。
  - 区域的发展需要 3分：共同利益或独立自主和平外交政策；区域经济融合、区域贸易和投资自由化便利化；维护地区和平稳定、周边国家命运共同体。
  - 世界的发展需要 2分：合作共赢新型国际关系、国际关系民主化、真正的多边主义、全球治理变革；全球自由贸易、多边贸易、经济全球化开放包容普惠平衡共赢方向。
- recommended_action: candidate_with_fixes
- boundary_risk: 同一个关键词不重复给分；周边工作不要拆成过多虚假频次。

### 2024朝阳二模 Q20

- paper_source_id: `SRC_4de874d0f669`
- scoring_source_id: `SRC_df323259ba77` / `SRC_8802a640c1e2`
- evidence: P0 formal scoring PDF/docx + P3 paper text
- full_prompt_anchor: `结合研讨背景，运用《当代国际政治与经济》知识，完成下表。`
- scoring_anchor:
  - 基本原则 2分：平等；开放。替代表述包括公平、公正、多边主义、协商一致、合作、共享、共赢、包容、求同存异、共商共建。
  - 共识背景 1分：气候变化是全球性挑战，气候治理成为全球治理重要议题。
  - 如何完善全球气候治理 5分：公平合理、合作共赢的全球气候治理体系；共商共建共享全球治理观；公平正义、合作共赢的新型国际关系；共同利益是国家合作的基础；推动构建人类命运共同体；共同但有区别的责任；企业绿色低碳技术创新。
- recommended_action: candidate_with_fixes
- boundary_risk: 企业绿色技术创新属于本题第三角度，暂作结果/边界，不当作选必一主链核心术语。

### 2024朝阳一模 Q21

- paper_source_id: `SRC_d3b447f0ea3a`
- scoring_source_id: `SRC_4fc81e818683` / `SRC_8a924a245316`
- evidence: P0 scoring PPTX/docx + P3 paper text
- full_prompt_anchor: `结合上述资料，在分析我国当前经济形势的基础上，运用《当代国际政治与经济》知识，谈谈如何推动中国经济在变局中开新局。`
- scoring_anchor:
  - 5分：学生需要从政治多极化、经济全球化两个维度分析如何应对风险挑战、发挥优势，推动经济高质量发展。
  - 参考示例包含：和平共处五项原则，维护主权安全发展利益，合作共赢，推动建设新型国际关系，推动构建人类命运共同体；两个市场两种资源，深度参与全球产业分工和合作；坚持独立自主。
- recommended_action: candidate_with_fixes_boundary_guard
- boundary_risk: 新发展理念、新发展格局、高水平对外开放、自主创新等混模块词不得直接计入选必一主链频次。

## 视觉定位后新增候选

### 2025朝阳一模 Q20

- paper_source_id: `SRC_832947a8c994`
- scoring_source_id: `SRC_c3d1aea637c9`
- visual_evidence: `02_extraction/screenshots/batch04D_2025朝阳一模_scoring/page_02.png` and `page_03.png`
- evidence: P0 scanned scoring PDF visually verified + P3 paper text
- full_prompt_anchor: `结合材料，运用《当代国际政治与经济》知识，说明我国应如何应对全球产业链供应链新态势，在全球产业变革中赢得主动。`
- scoring_anchor:
  - 多元化布局：鼓励和支持有实力的跨国公司全球分散投资、利用世界各地优势组织生产经营、顺应经济全球化趋势；效果为推进产业链供应链多元化布局、维护多元稳定国际经济格局和经贸关系、维护产业链供应链安全。
  - 区域化合作：深化区域经济合作、亲诚惠容外交理念、与周边国家和地区经济合作、区域投资和贸易自由化便利化、一带一路；推动区域产业链供应链深度融合。
  - 绿色化转型：绿色发展理念、绿色技术研发、对接国际规则与标准、环境政策。
  - 数字化加速：产业数字化、数字技术与实体经济深度融合。
  - 总结：积极参与全球经济治理和规则制定，维护多边贸易体系，发展更高水平开放型经济，推动构建开放型世界经济、人类命运共同体。
- recommended_action: candidate_with_fixes
- boundary_risk: 绿色技术、数字化、现代产业体系属于混模块结果，不作为独立选必一主链核心；产业链供应链安全稳定可并入既有供应链安全核心。

### 2026朝阳期末 Q20

- paper_source_id: `SRC_0056d930a7a9`
- scoring_source_id: `SRC_e80d35a6d904`
- visual_evidence: `02_extraction/screenshots/batch04D_2026朝阳期末_paper/page_07.png` and `02_extraction/screenshots/batch04D_2026朝阳期末_scoring/page_03.png`
- evidence: P0 scanned scoring PDF visually verified + P3 paper visual prompt
- full_prompt_anchor: `结合材料，运用《当代国际政治与经济》知识，分析中国特色大国外交为什么要更有作为。`
- scoring_anchor:
  - 和平发展：和平与发展是当今时代主题；命运共同体、共同利益、国际新秩序、全球治理。
  - 政治：多极化、单边主义、霸权强权；提升发展中国家代表性话语权、维护发展中国家利益、全球南方联合自强。
  - 经济：全球化、贸易保护主义；开放型世界经济、世界经济共同繁荣、互利共赢、开放合作、共享成果。
  - 国家利益：主权、安全、发展利益是国家核心利益；国家利益是国际关系的决定性因素；维护国家利益是主权国家对外活动的出发点和落脚点；维护人民利益和中国式现代化。
- recommended_action: candidate_with_fixes
- boundary_risk: “更有作为”总句不单独赋分；四角度每角背景+目标，不得只抽总帽。

### 2024朝阳期中 Q20(3)

- paper_source_id: `SRC_34231242a333` / `SRC_611ed7564625`
- scoring_source_id: `SRC_3d4cd35f4494` / `SRC_b706c444e16d` / `SRC_486fe5ba720a`
- evidence: P0 scoring docx/rtf + P3 paper text
- full_prompt_anchor: `结合材料，运用《当代国际政治与经济》知识，以“数字驱动 商通全球”为主题撰写一篇短评。`
- scoring_anchor:
  - 能运用经济全球化、提高开放型经济水平、完善全球治理等知识作答。
  - 三段材料分别点评：汇集新产品；打造新平台；带来新机遇。
  - 总评可写：推动经济全球化朝着更加开放、包容、普惠、平衡、共赢方向发展；体现中国平等开放、合作共享的全球治理理念。
- recommended_action: candidate_with_fixes_boundary_guard
- boundary_risk: 短评题含表达和结构分；前两问是《经济与社会》，不能把整题都计入选必一；只处理 Q20(3)。

## 降级或排除

- `2025朝阳期末 Q21`: 试卷题面是选必一，但评分 PDF 视觉核读只见等级答案式宽口径，写作方向为习近平外交思想、人类命运共同体、外交政策、世界多极化、全球治理体系、经济全球化等；没有细化采分点。暂定 `reference_only_or_level_answer`，不升 P0 主链频次。
- `2025朝阳一模 Q17/Q18/Q19`: 分别为逻辑、政治与法治、法律与生活，排除。
- `2025朝阳二模 Q16-Q20/Q22`: 除 Q21 外，题面为哲学文化、逻辑、经济与社会、政治与法治、法律或综合题，排除或边界记录。
- `2026朝阳期末 Q19`: 经济与社会海南自贸港政策制度题，排除。
- `2026朝阳期末 Q21`: 综合运用所学谈四大优势，不是选必一主观题，排除。

## 下一步

送 Patcher 和 Governor 检查：

1. `2024朝阳期中 Q20(3)` 是否应从低优先边界上调为 candidate_with_fixes_boundary_guard。
2. `2025朝阳一模 Q20` 的产业链供应链、绿色、数字化混模块边界是否过宽。
3. `2026朝阳期末 Q20` 四角度是否需要进一步拆分，尤其和平发展总帽与政治/经济/国家利益的功能差异。
4. 所有经济全球化完整五词必须合并到同一核心，不得拆成多个近义项。
