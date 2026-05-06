# Batch 02 Source Locator Notes

Status: `locator_only_not_entries`

These notes were created by Codex leader while the Codex A worker subagent is independently processing Batch 02. They are source locator facts, not final term entries.

## 2026朝阳一模 Q20

Source ledger:

- `2026朝阳一模_Q20_SRC_ebbe85a1ee6f`: formal scoring DOCX candidate.
- `2026朝阳一模_Q20_SRC_fd08ca4014c0`: paper PDF.

Confirmed source files:

- Scoring: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026朝阳一模/细则/细则.docx`
- Paper: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026朝阳一模/试卷/试卷.pdf`

Scoring DOCX extraction found Q20:

- Full prompt: `结合材料，运用《当代国际政治与经济》知识，阐述中国为什么能为全球发展注入稳定性和正能量。`
- Required point: `当前国际竞争的实质是以经济和科技实力为基础的综合国力较量。中国坚持创新驱动战略...` 2分, `必答点`.
- Optional/other points include:
  - `大国责任与担当（义利观、智慧方案）` 1分
  - `推动构建人类命运共同体` 1分
  - `两个市场、两种资源` 1分
  - `推动贸易投资自由化便利化` 1分
  - `推动经济全球化朝着更加开放、包容、普惠、平衡、共赢的方向发展` 1分
  - `促进人才、商品、服务和生产要素在全球范围内流动` 1分

Paper PDF extraction found the full Q20 material on page 7:

- 镜头一：中国 AI、开源大模型、创新药等创新势能。
- 镜头二：鲁班工坊、菌草、分享中国式现代化经验。
- 镜头三：中国消费规模、制造业规模、货物贸易、自贸协定、免签、人才流商品流资金流。

Evidence note: scoring source is P0 formal DOCX. The paper PDF includes a reference-answer section later, but the term source must remain the scoring DOCX, not the paper reference answer.

## 2026顺义一模 Q20

Source ledger:

- `2026顺义一模_Q20_SRC_8d2be8df9cad`: scoring PPTX candidate.
- `2026顺义一模_Q20_SRC_1da70413b2d1`: paper PDF.

Confirmed source files:

- Scoring: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/细则/细则.pptx`
- Paper: `/Users/wanglifei/Desktop/2026模拟题/2026各区一模/2026顺义一模/试卷/试卷.pdf`

Scoring PPTX extraction found Q20 on slide 9:

- Full prompt: `结合材料，运用《当代国际政治与经济》知识，阐述科技小院成为南南合作典范的深层逻辑。`
- `共同利益` is marked as 1分, 必答.
- International-political angle: 3分.
- International-economic angle: 3分.
- Listed political expressions include:
  - `时代主题：和平和发展（世界大势）`
  - `外交思想：构建人类命运共同体`
  - replacements: independent peace diplomacy / diplomacy purpose / `义利观`
  - `新型国际关系：合作共赢 / 互利共赢 / 共享发展成果`
- Listed economic expression:
  - `经济全球化方向：普惠、平衡、共赢`

Paper PDF extraction found Q20 on page 11:

- Main topic: 科技小院成为全球南方国家农业合作创新范式.
- Material signals: 中国方案、多国落地、农业绿色发展、本土创新、生产成本降低、培养本土人才、开放合作网络、分享中国经验、贡献中国方案、南南合作典范.

Evidence note: scoring source is P0 formal PPTX/评标. The globalization direction must merge with the full high-information core `开放、包容、普惠、平衡、共赢`, not collapse into `经济全球化正确方向`.

## 2025海淀二模 Q21

Source ledger:

- `2025海淀二模_Q21_SRC_05a280b2e00d`: scoring DOCX.
- `2025海淀二模_Q21_SRC_5b0f1d77d036`: evaluation-record DOCX.
- `2025海淀二模_Q21_SRC_203635b75b25`: paper PDF.

Confirmed source files:

- Scoring: `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/细则/细则.docx`
- Evaluation record: `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/细则/补充材料/2025年海淀二模评标实录.docx`
- Paper: `/Users/wanglifei/Desktop/2025模拟题/2025各区二模/2025海淀二模/试卷/试卷.pdf`

Scoring DOCX extraction found:

- Question 21.
- `中国需要联合国`
  - UN's own status and role, 2分, any two.
  - UN contribution to China's opening and modernization, 1分.
- `联合国需要中国`
  - China's status, 1分: founding UN member / Security Council permanent member; largest developing country / important force in international political-economic pattern.
  - China supports UN work, 1分: maintain UN-centered international system; support UN reform; maintain UN Charter purposes and principles.
  - Contribution of Chinese wisdom and Chinese solution, 1分: global governance / new type of international relations / common values of humanity / correct义利观 / human community.

Evaluation-record DOCX confirms Q21 teaching/marking context:

- Background: UN 80th anniversary.
- Material one shows UN role through data.
- Material two includes Wang Yi quote and China's Security Council rotating presidency role.
- Note: the line about UN contribution to China need not be written verbatim by students, but the meaning should be understood.

Paper source:

- PDF text extraction returns no text; existing render/visual note confirms prompt:
  `结合材料，运用《当代国际政治与经济》知识，阐释“中国需要联合国，联合国也需要中国”。`

Evidence note: scoring DOCX plus evaluation record make this a high-priority P0 + evaluation-record source. The paper prompt relies on visual note because PDF text extraction is empty.

## 2025海淀期末 Q22

Source ledger:

- `2025海淀期末_Q22_SRC_61b68f14212d`: scoring PPTX candidate.
- `2025海淀期末_Q22_SRC_1bd40d845040`: paper DOCX.

Confirmed source files:

- Scoring/teaching source: `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期末/细则/细则.pptx`
- Paper: `/Users/wanglifei/Desktop/2025模拟题/2025各区期末/2025海淀期末/试卷/试卷.docx`

Paper DOCX extraction found Q22:

- Full prompt: `结合材料，综合运用所学，围绕“愚公移山”这一主题，自选角度，自拟题目，撰写一篇短文。`
- Requirement: viewpoint clear, knowledge accurate, logical, about 200 Chinese characters.
- Materials include Mao Zedong 1945 speech, 1981 historical resolution, and Xi Jinping 2014 speech on connectivity partnership.

Scoring PPTX extraction:

- Slide 60: Q22 can use angles including `人类命运共同体`.
- Slide 61: `22.细则`; short-essay form 3分, knowledge 4分, other 2分.
- Slide 62: optional knowledge list includes `选必一：人类命运共同体、中国智慧中国方案`.

Evidence note: this remains P2 teaching/lecture source unless a formal scoring/marking file is found. It is useful as user-allowed supplementary source, but cannot inflate P0 frequency or appear as ordinary 选必一主观题 rubrics without a P2 label in audit layer.

