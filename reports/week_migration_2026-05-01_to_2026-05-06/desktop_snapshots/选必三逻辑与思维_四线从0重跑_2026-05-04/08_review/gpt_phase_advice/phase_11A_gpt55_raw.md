MUST_FIX_PHASE11A_CONTENT_NO_EXPANSION
verdict
Phase11A 当前 29 行正文不能直接进入 Phase11B 扩张。原因不是源证据缺口，而是正文里至少有 1 个概念性错误必须先修：2025 丰台期末第8题 把思维基本单元表述成概念，放在形象思维语境下会误导学生。其余硬锁总体保持：2025顺义一模第7题 保持大项不当扩大，2025丰台期末第7题 保持边界陷阱，2026顺义一模第19题第(2)问 保持科学思维主讲，hard-excluded rows 未展开为正文。
issues
1
QID or visible title: 2025 丰台期末第8题（选择题）(现代诗解读)
Severity: must_fix_content
Problem: 易错陷阱写为“①把想象当作思维的基本单元，基本单元是概念，不是想象”。这句话在当前题目语境下有概念风险。该题正在讲“发散思维 + 形象思维”，形象思维的基本单元应落在感性形象/具体形象上；概念是抽象思维的基本单元。把“基本单元是概念”泛化给“思维”会误导学生。
Concrete correction or local verification needed: 改为：①错在把想象当作形象思维的基本单元。形象思维依托感性形象，抽象思维的基本单元才是概念；本诗主要通过具体意象展开，不属于抽象思维。
Whether this blocks Phase11B controlled expansion: yes。这是正文概念错误，必须先 patch Phase11A，再进入扩张。
2
QID or visible title: 2024 朝阳二模第19题第(1)问（主观题）
Severity: should_fix_transfer
Problem: 主讲线写“类比推理 + 联言判断作辅助；本题要求填动态性 + 类比推理”。这一行会让学生误以为第(1)问也考联言判断。正文后面实际写的是第一空动态性、第二空类比推理，联言判断主要对应第(2)问。
Concrete correction or local verification needed: 将题型行改为：题型：填空组合题，第一空考辩证思维动态性，第二空考类比推理。 联言判断留到第(2)问，不在第(1)问题型名中出现。
Whether this blocks Phase11B controlled expansion: no，但应与第1项一起 patch，避免扩张后题型归档被污染。
3
QID or visible title: 2024 西城一模第19题第(5)问（主观题）
Severity: should_fix_transfer
Problem: 当前放在“推理题型”下，题型写为“综合推理题(实践调研 + 矛盾分析 + 推理想象 + 超前思维)”。这会把超前思维、矛盾分析、实践调研等思维方法链误读成形式推理题型。若后续推理部分扩张，很容易再次退化成泛泛分类。
Concrete correction or local verification needed: 保留在当前 29 行中可以，但标题建议改成：综合方法链：调研实践 + 因果分析 + 矛盾分析 + 推理想象 + 超前思维。若仍归推理章，必须单列为“综合方法链/超前思维链”，不得放入三段论、假言推理、联言/选言等形式逻辑同类题下。
Whether this blocks Phase11B controlled expansion: no，但阻断其进入形式逻辑题型归档正例。
4
QID or visible title: 2024 海淀二模第17题第(1)问（主观题）
Severity: optional_style
Problem: Phase10 去掉分值提示后，当前仍写“三个角度分别展开”，但没有给学生答题长度控制。弱学生可能不知道每个角度写到什么程度。
Concrete correction or local verification needed: 在答案落点后补一句学生可执行提示：每个角度至少写“材料动作 + 思维方法 + 作用结论”一组，不要只列方法名。
Whether this blocks Phase11B controlled expansion: no
5
QID or visible title: 2024 海淀二模第17题第(2)问（主观题）
Severity: optional_style
Problem: 当前表达正确，但“调查了解→感性具体；分析研究→思维抽象和思维具体”对弱学生仍偏抽象。
Concrete correction or local verification needed: 可补一句：先拿到杂多表象，再抽出本质联系，最后回到完整认识。
Whether this blocks Phase11B controlled expansion: no
cleared hard-lock checks
以下关键风险在 Phase11A 正文中暂未发现硬错误：
2025 顺义一模第7题：正文保持“真实错误应是大项不当扩大，A 项错在说成小项不当扩大”，符合当前硬锁。
2025 丰台期末第7题：仍在边界陷阱小节，未作为选必三超前思维正例。
2026 顺义一模第19题第(2)问：主讲线仍是科学思维三特征，推理侧只作辅助。
2024 朝阳二模第19题第(1)/(2)问：正文使用第一空/第二空，没有审稿编号、源文件编号、路径或评标痕迹。
2024 朝阳一模第20题第(1)/(2)问 与 2026 通州期末第19题第(2)问：充分条件与必要条件规则仍分开写。
2026 丰台一模第18题第(2)问：保留甲必要条件假言推理肯定后件式正确、乙三段论大项不当扩大错误。
2025 海淀二模第20题：仍是角度池写法，没有回流为三点全必答。
hard-excluded rows：2024西城一模第11题、2025海淀二模第12题、2025海淀二模第13题、2026顺义一模第3题 未展开为正文题条目。
required patch before next gate
Codex A 先执行一个小补丁，不扩张：
1. 修正 2025 丰台期末第8题的“基本单元”表述。
2. 修正 2024 朝阳二模第19题第(1)问题型名，移除“联言判断作辅助”。
3. 将 2024 西城一模第19题第(5)问标为“综合方法链/超前思维链”，不得归入形式逻辑同类题正例。
4. 重新生成 Phase11A patched body。
5. 重新跑 internal terms scan、hard-excluded scan、29-row count check、QID traceability check。
补丁后可再次提交一个短包：
phase11A_content_patch_resolution.md
phase11A_student_body_PATCHED_REVIEW_ONLY.md
phase11A_codex_local_recheck.md
next-phase hard rules after patch
Phase11B 只能做 controlled expansion，不得一次性扩成 74 行正文。
新增题必须来自 evidence rows，且不得来自 45 hold rows、288 L0 rows、hard-excluded rows。
同类题索引仍只作索引，不得自动展开答案、选项、题型结论。
推理扩张必须按题型归档：三段论、假言推理、联言/选言、归纳/类比、概念/判断等分别建节点，每题必须有逻辑形式、规则、有效式或错误式、解题动作。
思维扩张必须按触发链归档：材料信号、可写思维/方法、为什么能想到、答题动作、答案落点、易错陷阱。
交叉题继续保留主讲线与辅助线，不能单挂。
学生正文继续禁止内部词、源路径、评标、参考答案、pass、packet、lane、Governor、Confucius、L3、L4。
Word、PDF、final PASS、终稿、最终稿、宝典成品继续全部阻断。
