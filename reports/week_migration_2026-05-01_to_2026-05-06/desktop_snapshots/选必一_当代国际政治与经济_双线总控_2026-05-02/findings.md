# Findings

Record source discoveries here, especially after PDF/image/browser/OCR/visual reads.

## Source Findings

- 2026-05-02 22:14: `2026西城期末 Q20` full prompt was not in the Desktop source root, but was recovered from synced teacher PDF `/Users/wanglifei/GaokaoPolitics/2026各区模拟题/2026各区期末和期中/2026西城期末/2026北京西城高三（上）期末政治（教师版）.pdf`, rendered page 8. This resolves the prior `blocked_missing_full_prompt` state.
- 2026-05-02 22:17: Governor boundary scan kept `2026朝阳期中 Q17` development-side scoring phrase under `处理好发展和安全的关系`, not as an independent 必修二 node.

- 2026-05-02: Loaded router skill, 选必一 branch skill, current-user-requirements, xuanbiyi-term-protocol, and local notebook `选必一_交付要求记事本.md`.
- 2026-05-02: Existing local 选必一 artifacts include old classroom/frequency/v12 files and user correction ledgers under `选必一复查_2026-04-29`; these are useful as hard-rule memory but not sufficient source evidence for this run.
- 2026-05-02: Raw source roots found on Desktop: `2024模拟题`, `2025模拟题`, `2026模拟题`; initial max-depth scan found Word, PDF, PPT/PPTX source types, including scoring-rule folders and lecture materials.
- 2026-05-02: Local Word is scriptable; document pipeline should use Markdown canonical source, generated DOCX, OOXML checks, and Microsoft Word open/save validation.
- 2026-05-02: Built `SOURCE_LEDGER.csv` with 173 source files plus 4 control/root entries. Inventory covers 58 suites/directories and includes `docx/doc/pdf/pptx/ppt` sources.
- 2026-05-02: Source inventory summary written to `codex_lane/source_inventory_summary.md`; heavy rubric clusters include `东城二模`, `2026东城一模`, and `2025丰台二模`, so extraction must support nested分题细则 and PPT/PPTX.
- 2026-05-02: ClaudeCode Phase 2 report was generated but hit `error_max_budget_usd`; Codex reviewed it in `claudecode_lane/phase2_supervisor_review.md`.
- 2026-05-02: Priority extraction confirmed 2024东城一模 PPTX contains Q16 cross-book international relation/common-community scoring points and Q20 制度型开放/经济全球化/两个市场两种资源 scoring points.
- 2026-05-02: Priority extraction confirmed 2026通州期末 Q20 six-point scoring rule, 2026朝阳期中 Q17 total/subpoint scoring, and 2025海淀期末 Q22 xuanbiyi short-essay angle.
- 2026-05-02: Visual read of 2025海淀期中 embedded media confirmed Q16(2) supplement and Q21(2) table-form scoring rules; see `audit/visual_read_2025海淀期中_media.md`.
- 2026-05-02: Drafted 6 entries for 2026通州期末 Q20 and 9 entries for 2026朝阳期中 Q17, each with full prompt, source location, trigger logic, and answer-sheet sentence.
- 2026-05-02: Drafted 2 entries for 2025海淀期中 Q16(2) and 7 entries for Q21(2), preserving the visual scoring table's `变/不变` layers.
- 2026-05-02: Textutil extraction of 2025海淀期末 paper confirmed Q22 full short-essay prompt; PPTX rubric slide 62 confirms optional 选必一 angles `人类命运共同体` and `中国智慧中国方案`.
- 2026-05-02: `pypdf` could not extract usable text from 2024东城一模 paper PDF, so Codex rendered the PDF to PNG with PyMuPDF and visually transcribed Q16/Q20 prompts in `audit/visual_read_2024东城一模_试卷.md`.
- 2026-05-02: Drafted 2 entries for 2025海淀期末 Q22 and 3 entries for 2024东城一模 Q16/Q20; Q16 is marked cross-book confirmed, and Q20 excludes 必修二 boundary terms from the 选必一 main chain.
- 2026-05-02: Phase 3 expansion extraction found clean text/rubric evidence for 2026东城期末 Q20, 2026朝阳一模 Q20, 2026顺义一模 Q20, and 2025丰台期末 Q20; 2026西城期末细则 PDF, 2026丰台一模 paper PDF, and 2025海淀二模 paper PDF still need visual/OCR if included.
- 2026-05-02: Drafted 6 entries for 2026东城期末 Q20, preserving four global-initiative sublayers plus system/practice layers.
- 2026-05-02: Drafted 8 entries for 2026朝阳一模 Q20, preserving the必答 international competition/innovation point and excluding `扩大高水平对外开放` from术语位.
- 2026-05-02: Drafted 5 entries for 2026顺义一模 Q20 and 7 entries for 2025丰台期末 Q20, preserving `共同利益`, `共商共建共享`, `新型国际关系`, and人类命运共同体 evidence.
- 2026-05-02: Visual read of 2026丰台一模 paper confirmed Q19 full prompt on China's大国情怀与担当 in global sustainable development; rubric slide 42 confirms `人类命运共同体的理念`, `联合国宪章的宗旨和原则`, `正确义利观`, `真正的多边主义`, `合作共赢`, and `共商共建共享的全球治理观`.
- 2026-05-02: Visual read of 2025海淀二模 paper confirmed Q21 full prompt: `阐释“中国需要联合国，联合国也需要中国”`; rubric and评标实录 confirm the two-sided scoring structure.
- 2026-05-02: Visual read of 2026西城期末细则 confirmed strong climate-governance 选必一 rubric terms, but current source root lacks the full Q20 prompt. Logged as blocked rather than drafting incomplete entries.
- 2026-05-02: Validation after adding 2026丰台一模 Q19 and 2025海淀二模 Q21 passed required-field counts for all 11 entry files and found no `答案句` meta-language hits. Boundary scan still flags the pre-existing `2026朝阳期中_Q17` `高质量发展` term for later Governor decision.
- 2026-05-02: 2026 unprocessed-source extraction processed 32 high-confidence sources and found 19 with 选必一 keyword hits. Clear text-closed suites include 2026延庆一模、2026石景山一模、2026西城一模、2026门头沟一模.
- 2026-05-02: Visual read of 2026延庆一模 paper confirmed Q19(2) full prompt ending `理论逻辑和价值意蕴`; draft entries separate theory logic from value implication.
- 2026-05-02: Drafted 5 entries each for 2026延庆一模 Q19(2), 2026石景山一模 Q20, 2026西城一模 Q20(2), and 2026门头沟一模 Q20.
- 2026-05-02: Validation after second 2026 expansion batch passed all 15 entry files and 89 entries for required-field completeness. No `答案句` meta-language hits; boundary scan still flags only the pre-existing `2026朝阳期中_Q17` `高质量发展` line.
