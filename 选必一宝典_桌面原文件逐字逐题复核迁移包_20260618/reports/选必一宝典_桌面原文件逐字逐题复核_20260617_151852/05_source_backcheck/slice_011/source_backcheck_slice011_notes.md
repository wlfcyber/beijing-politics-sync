# Slice 011 Codex Source Backcheck Notes

- run_id: 选必一宝典_桌面原文件逐字逐题复核_20260617_151852
- source_docx: /Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx
- source_sha256: 876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e
- slice_scope: doc_order 51-55 only
- backcheck_time: 2026-06-17T18:01:51+0800

## Overall Finding

Slice 011 source evidence is available for all five entries. The entries remain repair-needed because they still lack independent hard-rule `术语/核心采分点` and `细则位置` fields, and several rows misstate the scoring role of a source-backed idea.

Key distinctions:

- Q0051 and Q0054 are the same 2025东城一模Q21 10-point comprehensive education question. The source has a 2+6+2 structure. `人才与国际竞争力` belongs to the optional `为什么` layer, while `科教兴国人才强国战略` belongs to the 2-point `怎么做` layer. These should not become two isolated fixed main points.
- Q0052 is the 2026石景山二模Q18 China-ASEAN cooperation question. The formal source says `国家利益和国家实力` plus economic globalization/common interests, not `当前国际竞争的实质`.
- Q0053 has formal support for `国际竞争的实质` as the first item in a 4-point chain, but the desktop answer is too short and omits the rest of that chain.
- Q0055 reuses 2024西城二模Q17. `科教兴国战略，强化现代化建设人才支撑` is one available angle in a 9-point level-scored question, not an independent fixed score.

## Q0051 doc_order=51

- desktop blocks: 626-636
- question: 2025东城一模Q21
- source evidence:
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q21.txt:205-220` confirms the 10-point education prompt and material.
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q21.txt:191-208` confirms the 2+6+2 structure.
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q21.txt:196-205` places `人才与国际竞争力` in the optional `为什么` layer, but does not say `当前国际竞争的实质是以经济和科技实力为基础的综合国力较量`.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The desktop core is over-specific; the source supports talent/international-competitiveness relation, not the exact international-competition-essence formula.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact note: optional `为什么` layer, not independent fixed score.
- `来源`: NEEDS_FIX. Local source is found, but the desktop file lacks formal source identity and position.
- `材料触发`: PASS. Material two's world turbulence/major-power competition plus education strategic support legitimately triggers international competitiveness.
- `答案句`: NEEDS_FIX. Block 630 is usable as an education-effect answer, but it does not match the exact desktop core term and should be tied to the `为什么` layer.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. The same entry mixes education as上层建筑, employment/income, cultural inheritance, public service and 选必一 competitiveness; these need module labels.

## Q0052 doc_order=52

- desktop blocks: 637-645
- question: 2026石景山二模Q18
- source evidence:
  - `SRC_EXAM_2026_SHIJINGSHAN_ERMO_Q18.txt:103-108` confirms the prompt and materials.
  - `SRC_RUBRIC_2026_SHIJINGSHAN_ERMO_Q18.txt:49-50` confirms the full 8-point answer: basis 4 and significance 4.
  - `SRC_EXAM_2026_SHIJINGSHAN_ERMO_Q18.txt:125-126` mirrors the teacher answer structure.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The formal source uses `国家利益和国家实力是影响国际关系的决定性因素`; it does not use `当前国际竞争的实质`.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact source position for basis 4 / significance 4 and removal or demotion of `国际竞争实质`.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: NEEDS_FIX. Digital infrastructure facts may show capability, but the source scoring is about cooperation basis and significance, not international-competition essence.
- `答案句`: NEEDS_FIX. Block 641 should be rewritten around `国家利益和国家实力` plus cooperation/economic-globalization logic.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. The significance layer contains `两个市场、两种资源`, economic transformation, people-benefit, region/world effects; it needs clear source-layer labels.

## Q0053 doc_order=53

- desktop blocks: 646-655
- question: 2025房山一模Q18(2)
- source evidence:
  - `SRC_EXAM_2025_FANGSHAN_YIMO_Q18.txt:181-189` confirms the DeepSeek/open-source prompt.
  - `SRC_RUBRIC_2025_FANGSHAN_YIMO_Q18.txt:95-100` confirms the formal 4+3+1 structure.
  - `SRC_RUBRIC_2025_FANGSHAN_YIMO_Q18.txt:96-97` gives the exact first chain: `国际竞争的实质 -> 高水平对外开放 -> 以科学技术的发展推动建设创新型、开放型世界经济 -> 促进经济全球化发展`.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The term is source-backed, but the desktop still lacks independent `术语` and exact `细则位置`.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: first 4-point chain, with the two不可替代 parts.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. DeepSeek/open-source technology facts do trigger the first chain.
- `答案句`: NEEDS_FIX. Block 650 only states the opening of the chain and omits high-level opening, innovative/open world economy, and economic globalization.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. The row mixes international competition, high-level opening, open world economy, UN framework, HMC, correct义利观, and global governance; each must stay in source-layer position.

## Q0054 doc_order=54

- desktop blocks: 657-667
- question: 2025东城一模Q21
- source evidence:
  - `SRC_EXAM_2025_DONGCHENG_YIMO_Q21.txt:205-220` confirms the prompt and material.
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q21.txt:191-208` confirms the 2+6+2 structure.
  - `SRC_RUBRIC_2025_DONGCHENG_YIMO_Q21.txt:206-208` places `科教兴国人才强国战略` in the 2-point `怎么做` layer.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The term is source-backed, but it is the `怎么做` layer, not an isolated main answer.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs exact position: `怎么做` 1个角度 2分.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. Education/talent data plus major-power competition can trigger talent-strength reasoning.
- `答案句`: NEEDS_FIX. Block 661 explains talent advantage and international competitiveness but does not clearly write the `怎么做` strategy point from the source.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. Because this is the same cross-module Q21 as Q0051, the row must label education/superstructure, employment/income, cultural, government/public-service and 选必一 competitiveness layers.

## Q0055 doc_order=55

- desktop blocks: 668-681
- question: 2024西城二模Q17
- source evidence:
  - `SRC_EXAM_2024_XICHENG_ERMO_Q17.txt:101-103` confirms the prompt and material.
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:19-23` lists available answer angles including `实施科教兴国战略，强化现代化建设人才支撑`.
  - `SRC_RUBRIC_2024_XICHENG_ERMO_Q17.txt:66-76` confirms the 9-point level-scored table.

Codex judgment:

- `术语/核心采分点`: NEEDS_FIX. The term is source-backed as an available angle, not an independent fixed score.
- `完整设问`: PASS.
- `细则位置`: NEEDS_FIX. Needs level-scored wording and available-angle caveat.
- `来源`: NEEDS_FIX. Local source is found, but desktop entry lacks formal source identity and position.
- `材料触发`: PASS. The material's education-technology-talent cycle supports this angle.
- `答案句`: NEEDS_FIX. Block 672 is close, but `引领新一轮科技革命` overstates the source; it should be framed as talent support for the role of the largest developing country.
- `同类项合并`: PENDING_BOOK_LEVEL.
- `模块边界`: NEEDS_FIX. The same-question group mixes new quality productive forces, economic globalization, national security, theory support, and talent strategy; the talent strategy must remain a level-question angle.
