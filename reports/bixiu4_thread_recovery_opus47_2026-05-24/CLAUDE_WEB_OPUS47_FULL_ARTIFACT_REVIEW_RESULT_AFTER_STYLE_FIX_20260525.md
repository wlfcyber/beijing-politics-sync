# Claude Web Opus 4.7 Full Artifact Review Result After Style Fix

status: `REAL_CLAUDE_WEB_OPUS47_REVIEW_CAPTURED_PASS_WITH_OPEN_GATES`

Captured: 2026-05-25 19:48 +08

Chat URL: `https://claude.ai/chat/36005659-2dac-47c5-9ece-037fb0fcc908`

Visible model/session evidence:

- Direct route used: `https://claude.ai`.
- Google login path used: `no`.
- Signed-in UI was visible before submission: account `LaceyFitzgerald`, `Max plan`.
- Composer model button before and during the response: `Opus 4.7 Adaptive`.
- Attached latest DOCX/PDF, matrix, risk audit, style audit, render manifest, model ledger, sonnet invalidation ledger, Governor report, and review packet.
- Screenshot evidence: `CLAUDE_WEB_OPUS47_FULL_ARTIFACT_REVIEW_RESULT_AFTER_STYLE_FIX_20260525.png`.

Evidence boundary:

- This file is a real captured Claude web/app answer, not a local Codex paraphrase.
- This review gives `pass_with_open_gates`; it does not close GPTPro, ClaudeCode model-confirmation, full thickness, or every-page visual review gates.
- Sonnet, Haiku, and model-unknown outputs remain excluded from qualified evidence.

## Captured Answer

external_result: pass_with_open_gates

Coverage And Placement

矩阵规模口径自洽。MATRIX_EVIDENCE_RISK_AUDIT_20260525 报告 1537 行已审，558 行标为 in-book/body，生成风险行 0、body 风险行 0；risk_queue_closed 仅作为 triage 队列关闭，不是行级正式关闭。这是其自述边界，我接受这一定位，而不接受将其作为行级最终证据。

Body 行与模块边界行已在证据等级分布中可区分：模块边界类条目如官方答案键+模块边界 102、选择题官方答案键+模块边界 38、模块边界明确 18、模块边界/题干边界 11 等，在命名上与正文强证据如强细则 93、正式细则 50、正式评分标准 49、正式评分细则 34、正式阅卷细则 14 等显著区隔，未发现将 boundary 等级混入 body 强证据列的痕迹。

选择题口径正确。所有选择题官方答案键相关行均在标签中显式标注非主观题评分细则或选择题边界已明示，与 boundary 段第 4 条规则一致，未在该路径上发现把客观键当主观评分细则使用的情况。

但 placement 边界仍有需要点名的灰色区：

- `formal_rubric_optional_angle` 3 行命名本身处于“正式但仅角度提示”的边缘语义，从外审视角无法仅凭标签判定它是否真的进了 body 强证据列，需要给出这 3 行的行号与 suite 名以便核对。
- `证据不足：不单独成条` 2 行与 `缺直接证据` 1 行已经在分类上承认证据不足，这没有问题；但需要确认其当前 disposition 是“已撤出正文”而不是“以弱证据继续支撑正文”。
- `COVERED_OR_PATCHED` 22 行、`COVERED_OR_PATCHED_WITH_ROW_REVIEW` 5 行、`SUPERSEDED_BY_ROW_LEVEL_REPAIR` 2 行、`SUITE_LEVEL_SUMMARY_RECHECKED_NO_OPEN_ROW_RISK` 13 行等流程性标签合计约 40 余行，本身不是证据等级，而是处理状态，需要在最终行级证据列另行落到具体的正式细则或正式答案键。

教师版系列与参考答案系列在 boundary 段第 3 条已明确为非细则支持，这是正确的边界写法；但 boundary 段是文本声明，不是行级强制。审计本体没有展示一个机器化的“教师版/参考答案不得作为 body 强证据”的反向检查计数，这是当前 placement 证据的一个结构性弱点。

顶部 Risk Type Distribution 与 Top Risk Rows 表格在 md 中保留为空表头，与风险行 0 自洽，但同时意味着外审无法从该文件直接抽样 spot-check；若要外审给出更强结论，需要补一份零风险的反向抽样，随机若干行的行级证据快照。

Formatting And Render

风格一致性 audit 自身口径硬：question entries 721；插入条目 415 + 遗留条目 306 = 721，与总数自洽；heading_ppr_variant_count / heading_rpr_variant_count / inserted_heading_ppr/rpr_variant_count / legacy_heading_ppr/rpr_variant_count 全部为 1，意味着插入段与遗留段在段落与文字属性层级已合并到同一风格，这是“新旧条目结构一致”的最直接证据。

四类标签计数完全对齐：【材料触发点】、【设问】、【为什么能想到】、【答案落点】各 721，first-run 风格变体均为 1。missing label 0，duplicate label 0，ledger 与当前 DOCX 之间无缺失标题。

渲染端 cross-check 通过：render_manifest.json 中 pdf_pages = 290，rendered_png_count = 290，docx_label_count = 2891，pdf_label_count = 2891，blank_like_pages_excluding_cover_foreword = []。DOCX/PDF 标签计数严格相等，这是支持“渲染落地无丢失”的硬证据。

4 x 721 = 2884，与 2891 差 7，差值方向合理，疑似封面/前言/分册扉页若干额外标签，但 audit 与 manifest 都未把这 7 条显式列出，建议在下一版 manifest 中加一行 `extra_label_breakdown` 把这 7 条逐一定位，以闭合标签账目。

contact sheet 抽样页 p19/34/44/81/112/133/153/173/209/221/251/280 显示四标签结构在二模一模新增条目与遗留条目上视觉一致，行间距、缩进、标签字号未见跳变，与 audit 的“1 个变体”结论一致。

边界：audit 自身在 boundary 段明确“不替代每页人工视审”，这是诚实的写法，但意味着 formatting 仅在结构层级 PASS，视觉层级仍是开口。

Thickness / Student Use

从 contact sheet 抽样看，可见条目的【答案落点】具备分点结构与显性原理回扣；【为什么能想到】给出从材料到原理的检索路径，这是面向零基础学生的可用结构。

但本外审包不包含正文逐题文本快照，也不包含一份“零基础学生答题链路”的代表性抽样清单。外审仅凭 12 页缩略图无法判断 721 条目在全量层面的厚度均匀性，尤其无法判断：

- 二模/一模漏项补强条目 415 条插入在【答案落点】上的论证密度是否与遗留 306 条对齐。
- 是否存在某些只剩单点的“轻条目”，典型表现为【答案落点】仅 1 行结论性句子。
- 哲学链条在跨模块综合题里的衔接句是否到位，这是这一科最容易薄的位置，而本次补强主题正涉及“必修四漏项”。

audit 自身在 boundary 段已声明需要 GPTPro/Claude Opus 外部内容厚度评审，我把这一点保留为本次外审未关闭的核心开口。

我没有发现明显的“弱逻辑被通过”的迹象，但也无法基于现有证据宣告厚度通过，这是本结论选择 `pass_with_open_gates` 而非更强档位的主要原因。

Open Gates

- 内容厚度逐题人工/外审复核，全量 721 条目，不只是抽样 12 页。
- 替代版 Opus 4.7 max-effort / adaptive-thinking ClaudeCode 重跑，以替换被 SONNET_INVALIDATION_LEDGER 作废的两次 sonnet 调用；在重跑写入 MODEL_EVIDENCE_LEDGER.md 之前，ClaudeCode lane 视为未关闭。
- GPTPro 网页/应用版正式外审尚未在本包中以“已捕获正文回答”的形态呈现；若 GPTPro 侧只有本地转述而无原始回答 artifact，GPTPro gate 保持开口。
- 本条 Claude 网页 Opus 4.7 外审需要被该项目以“已捕获的真实 web/app 回答”形式归档；若仅以本地摘要替代，Claude 网页 gate 亦不应被宣告关闭。
- 矩阵风险行的反向抽样证据，随机抽 N 行展示其行级正式证据指针，未在本包中给出；triage 队列关闭不等于行级最终关闭。
- 视觉层每页人工审阅尚未提供日志或对照表，formatting 仅在结构层关闭。
- 标签账目尾差 7 条需要 manifest 一行显式列出来源。

Required Corrections Before Final Acceptance

- 补一份行级反向抽样证据包：随机抽取若干 body 行，逐行展示其正式细则/正式答案键的源指针快照，以把 triage 级 0 风险升级为行级 0 风险。
- 对 `formal_rubric_optional_angle`、`证据不足：不单独成条`、`缺直接证据`、`COVERED_OR_PATCHED*`、`SUPERSEDED_BY_ROW_LEVEL_REPAIR`、`SUITE_LEVEL_SUMMARY_*` 这些非证据等级的处理状态标签，逐行落到具体的正式证据指针或显式标记为“已撤出正文”。
- 在 audit 中增加一项机器化反向检查：教师版、参考答案、模型摘要等类目不得作为 body 强证据列出现，并给出计数为 0 的自检结果。
- 完成对 415 条新增插入条目的【答案落点】厚度逐条复核，并对其中哲学必修四主链题给出单独的厚度抽样报告。
- 用一次确认为 Opus 4.7 max-effort / adaptive-thinking 的 ClaudeCode 重跑，产出替换 SONNET_INVALIDATION_LEDGER 中两条作废调用的等价证据，并在 MODEL_EVIDENCE_LEDGER.md 留痕。
- 把本次 Claude 网页 Opus 4.7 外审与一次正式 GPTPro 网页外审分别以原始回答 artifact 形式归档，而非以本地复述形式归档。
- 视觉层补一次每页人工审阅日志，可与 290 页 png contact sheet 并列，关闭 formatting 视觉口。
- manifest 增补 `extra_label_breakdown`，解释 2891 与 4 x 721 之间的 7 条尾差来源。
