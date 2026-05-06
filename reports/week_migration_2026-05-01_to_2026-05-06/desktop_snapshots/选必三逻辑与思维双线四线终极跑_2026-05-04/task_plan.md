# Task Plan

Goal: Run 选必三 逻辑与思维_思维部分哲学式重跑_推理部分题型归纳 through three lanes into a final teaching document: Codex leader, Codex production, and Claude Code independent rerun.

## Current Status

- status: complete
- current_phase: Phase 8 Final acceptance report

## Phase Boundary Rule

After each phase or substantial milestone: write a sanitized phase report, send it to GPT-5.5 Pro when available, save the raw commander advice, digest it into local tasks, and continue. If GPT/web/thread stalls, log the fallback and keep running authorized local work. Governor, not GPT, owns phase release; fallback phases need late review when GPT returns.

## GPT Content Review Rule

After each fixed trigger object (`outline`, `section_batch`, `final_markdown`, `word_pdf`): send the generated content itself to GPT-5.5 Pro in chunks, save raw review, digest concrete content corrections, locally verify substantive fixes, patch, and rerun until no unresolved `must_fix_content` remains and no `should_fix_transfer` blocks student transfer. Missing trigger objects need fallback/waiver. Markdown PASS and Word/PDF PASS are separate. Final PASS is blocked until this is complete unless the user disables it.

## Phases

- [x] Phase 0: Intake and user framework lock
- [x] Phase 1: Workspace, notebooks, and master requirements
- [x] Phase 2: Source inventory and evidence map
- [x] Phase 3: Three-lane production by suite/question
- [x] Phase 4: Advisor review and governor checks
- [x] Phase 5: Fusion into student artifact
- [x] Phase 6: Word production and visual QA
- [x] Phase 7: Confucius artifact-only learning verification
- [x] Phase 8: Final acceptance report

## Decisions Made

- 思维部分按必修四哲学式触发处理：材料信号、可写术语、答题动作、来源例题。
- 推理部分不按套卷堆叠，而按题型族群处理：三段论、假言推理、选言推理、联言判断、归纳、类比、求异法、周延/换质换位、逻辑三律。
- GPT 与 Claude 外部审稿只负责内容压力测试，题源真伪由本地证据负责。
- PDF 未作为正式交付物，Word 为最终版式交付物。


## Errors Encountered

| Attempt | Error/Symptom | Different Next Step | Resolution |
|---|---|---|---|
| PDF export | `cupsfilter` 无法识别 DOCX MIME，产生 0 字节测试 PDF | 不把 PDF 当正式交付物 | 改用 Microsoft Word 打开保存、Word 截图、QuickLook 缩略图验收 |
