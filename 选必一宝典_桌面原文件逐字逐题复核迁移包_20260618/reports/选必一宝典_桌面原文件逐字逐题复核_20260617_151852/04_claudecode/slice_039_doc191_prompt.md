你是 ClaudeCode 的独立复核 lane。请只复核给定 doc_order 的桌面原文件摘录，不要改写全文、不要声称全书完成。

任务：逐字逐题比对【桌面原文件条目】与【题源/细则摘录】，判断 8 个字段：术语/核心采分点、完整设问、细则位置、来源、材料触发、答案句、同类项合并、模块边界。

输出要求：
1. 先给总判定：PASS / NEEDS_FIX / LOW_EVIDENCE / PENDING_BOOK_LEVEL（如只有同类项书级待核，写 PASS with group hold）。
2. 分字段列出结论和依据，必须引用源文件显示的原始行号。
3. 明确必须修的原文点；若只是书级同类组未统一，不要把单题文本误判成硬错。
4. 明确边界：只审本 doc_order；不修改桌面 DOCX。

# Review Target

- doc_order: 191
- entry_id: Q0191
- question_ref: 2025海淀一模Q21
- question_title: 2025海淀一模Q21(2)
- bucket/sub_bucket: 经济全球化 / 兼：国内国际两种资源两个市场
- core_point: 中国市场红利推动互利共赢
- blocks: 2244-2254

# Desktop Original Excerpt

```text
2244: 1. 2025海淀一模Q21(2)
2245: 【材料触发点】 题面强调我国市场潜力不只在于人口规模，还在于消费增长和需求层次丰富，说明中国市场本身为全球贸易提供需求牵引和合作空间。
2246: 【设问】 结合材料，运用《当代国际政治与经济》知识，说明我国外贸为何能连上两个万亿级台阶。（6分）
2247: 【为什么能想到】 题面强调我国市场潜力不只在于人口规模，还包括消费增长、需求层次丰富——市场本身就是为全球贸易提供需求牵引的合作空间。问"外贸为何能连上台阶"——本条要从"我国市场对世界的吸引"切入，把"我国市场"翻为"世界市场"的逻辑写出。把消费增长和需求层次丰富归结为超大规模市场优势，再写为世界各国提供广阔市场，最终指向促进国际合作和互利共赢、支撑外贸增长。
2248: 【答案落点】 我国依托超大规模市场优势，为世界各国提供更加广阔的市场，促进国际合作、实现互利共赢，为外贸增长注入持续动力。
2249: 【同题组】 （按原题答题层次）
2250: · 答题层次：本题6分，围绕我国外贸连上两个万亿级台阶的原因，按绿色/数字贸易、开放平台与综合保税区、市场潜力三层组织，每层最高2分。
2251: · 绿色贸易、数字贸易（2分）：发展绿色贸易、数字贸易1分；推动货物贸易优化升级或打造产品出口竞争新优势1分；如果没有落到出口结构优化升级，最高1分。
2252: · 开放平台与综合保税区（2分）：贸易自由化便利化可作为完整2分；若只写降低贸易成本、优化营商环境、推进制度型开放或降低市场准入，按1分处理。
2253: · 市场潜力（2分）：超大规模市场优势1分；互利共赢、两个市场两种资源、国内国际双循环、提供机遇、共享，或推动经济全球化朝开放、包容、普惠、平衡、共赢方向发展1分。
2254: · 易错边界：中国智慧、中国方案、政治多极化、和平与发展、独立自主和平外交政策、产业结构优化升级、供给侧结构性改革等方向不要写；单纯抄材料或堆砌学科观点，最高2分；不分条阐释不能拿满。
```

# Current Ledger Field Skeleton

```text
- 术语/核心采分点: current_status=STRUCTURE_NEEDS_FIX_SOURCE_PENDING; audit_note=Mechanical full-document scan: current entry structure uses bucket/core heading plus 【同题组】, but lacks independent hard-rule field for this item; source/content audit still pending.
- 完整设问: current_status=PENDING; audit_note=(pending)
- 细则位置: current_status=STRUCTURE_NEEDS_FIX_SOURCE_PENDING; audit_note=Mechanical full-document scan: current entry structure uses bucket/core heading plus 【同题组】, but lacks independent hard-rule field for this item; source/content audit still pending.
- 来源: current_status=PENDING; audit_note=(pending)
- 材料触发: current_status=PENDING; audit_note=(pending)
- 答案句: current_status=PENDING; audit_note=(pending)
- 同类项合并: current_status=PENDING; audit_note=(pending)
- 模块边界: current_status=PENDING; audit_note=(pending)
```

# Unique-Question Group Context

```json
{"unique_id": "UQ0065", "normalized_question": "2025海淀一模Q21(2)", "count": "3", "doc_orders": "93;191;233", "buckets": "经济全球化", "core_points": "中国市场红利推动互利共赢;推进贸易和投资自由化便利化;数字贸易与数字经济跨境流通", "question_titles": "2025海淀一模Q21(2) || 2025海淀一模Q21(2) || 2025海淀一模Q21(2)"}
```

# Prior Same-Source Context

Prior same-source context: doc93 (same 2025海淀一模Q21(2)) was NEEDS_FIX only for the trade-facilitation row because it wrote 贸易投资自由化便利化 while rubric supports 贸易自由化便利化. This doc191 row is the separate market-dividend/mutual-benefit layer; judge independently.

# Codex Watchpoints To Verify, Not Blindly Accept

- Rubric lines 90-93 give three scoring layers: trade facilitation, green/digital trade, and super-large-market advantage/mutual benefit.
- Current core is 中国市场红利推动互利共赢; verify it is supported by rubric lines 92-93 and material lines 230-231.
- Do not transfer doc93 hard error about 投资 wording unless this row itself uses unsupported 投资 wording.
- UQ0065 remains book-level pending across doc_orders 93/191/233.

# Source / Rubric Excerpts

## SRC_EXAM_2025_HAIDIAN_YIMO_Q21_2.txt
```text
SOURCE_ID: SRC_EXAM_2025_HAIDIAN_YIMO_Q21_2
TITLE: 2025海淀一模Q21(2) 试卷
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025海淀一模/试卷/试卷.pdf
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/选必二重做_2026-04-30/claudecode_lane_B_full_rerun_2026-05-04/source_inventory/extracted/2025/2025海淀一模/2025各区一模__2025海淀一模__试卷__试卷.pdf.txt

## prompt/material lines 222-234
222: 21．（8分）
223: 外贸进出口是拉动经济增长的重要引擎。2024 年，我国外贸总量连续跨过 42、43 两个万亿级台阶，
224: 全年进出口总值达到 43.85 万亿元人民币，再创历史新高。这一成绩的取得，离不开新动能的巨大推动力。
225: ·绿色贸易领跑全球。我国绿色产品不仅丰富了全球供给，也为全球应对气候变化和绿色低碳转型作
226: 出了巨大贡献。
227: ·数字贸易蓬勃发展。2024年我国跨境电商进出口2.63万亿元，增长10.8％。
228: ·高水平开放平台带动作用明显。综合保税区是我国开放程度最高、优惠政策最集中、功能最齐全的
229: 海关特殊监管区域。我国现有 167 个综合保税区，分布在全国各地，在产业转型升级方面发挥了重要作用。
230: ·我国市场潜力不仅在于人口规模庞大，更在于消费增长迅速、需求层次丰富，不断为全球贸易注入
231: 新的活力。
232: （1）以“外贸进出口是拉动经济增长的重要引擎”为结论，写出一个正确的演绎推理。（2分）
233: （2）结合材料，运用《当代国际政治与经济》知识，说明我国外贸为何能连上两个万亿级台阶。（6
234: 分）
```
## SRC_RUBRIC_2025_HAIDIAN_YIMO_Q21_2.txt
```text
SOURCE_ID: SRC_RUBRIC_2025_HAIDIAN_YIMO_Q21_2
TITLE: 2025海淀一模Q21(2) 评分标准
ORIGINAL_SOURCE_PATH: /Users/wanglifei/Desktop/2025模拟题/2025各区一模/2025海淀一模/试卷/补充材料/EDU_1500334100000021014_61af1789-0742-472d-86cd-e6cb420b0ecb.pdf
TEXT_EXTRACT_PATH: /Users/wanglifei/Desktop/北京高考政治/claude_zero_run/extracted/8cf8c31e07b0__EDU_1500334100000021014_61af1789-0742-472d-86cd-e6cb420b0ecb.txt

## scoring standard header lines 1-5
1: ===== PAGE 1 =====
2: 1 
3:  
4: 2025 海淀一模评分标准 
5: 政 治

## Q21 scoring standard lines 71-93
71: 21．（8 分） 
72: （1）评分标准：符合演绎推理基本规则。（2 分） 
73: 
74: ===== PAGE 4 =====
75: 4 
76:  
77:  
78:  
79:  
80:  
81:  
82:  
83:  
84: 
85: ===== PAGE 5 =====
86: 5 
87:  
88:  
89:  
90: （2）实施更加积极主动的开放战略，以政策促进贸易自由化便利化，通过综合保税区等形式降
91: 低贸易成本，畅通国际贸易。发展绿色贸易、数字贸易，推动货物贸易优化升级，打造产
92: 品出口竞争新优势。依托我国超大规模市场优势，为世界各国提供更加广阔的市场，促进
93: 国际合作，实现互利共赢。（6 分）
```
