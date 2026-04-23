# Governor Board

## Current Status
- organizer: passed for 2026 one-model main-question slice and 2025二模 choice-question follow-up.
- file_reader: passed; re-opened the user-supplied 2026朝阳一模主观题阅卷细则docx with raw OOXML extraction and confirmed 第16题 is present at the start of the file without a numeric heading.
- file_reader_2025_ermo: passed; extracted 2025二模 teacher papers and rubric/commentary files to `C:\Users\Administrator\Desktop\beijing_politics_research\data\extracted_text\2025_ermo`; rendered scanned 海淀二模 paper pages to `C:\Users\Administrator\Desktop\beijing_politics_research\data\ocr_pages\2025_ermo_haidian_paper`.
- mapper: passed for 2026东城16/20、朝阳16、丰台16、延庆16、房山16(2)/18(1)、海淀16、石景山17(1)、西城16/21、门头沟16/18(2)/21、顺义16/21.
- choice_mapper: passed for 2026东城一模哲学相关选择题首轮 and 2025二模选择题首轮; 42 reusable wrong-option patterns are now in the library.
- summarizer: passed; merged 16 source-labeled 2026一模主观题 logic chains into `C:\Users\Administrator\Desktop\必修四哲学材料-知识触发总框架_持续更新版_v2.md`; updated `C:\Users\Administrator\Desktop\北京高考政治错肢库_持续更新版.md` with 2025二模 additions.
- governor_decision: passed after correction. The previous blocker for 2026朝阳一模第16题 is withdrawn.

## Correction Log
- Corrected miss: 2026朝阳一模第16题 rubric was not absent. It was hidden by document structure because the rubric begins directly with “结合材料。运用《哲学与文化》知识，分析中国农历所蕴含的独特智慧” instead of a “16.” heading.
- Evidence used: user-supplied `chat_file_1040g3c831um895dphu105n2bsq04dit0lj2bojo_202604朝阳高三政治一模阅卷细则(1).docx`.
- Framework update: added the 朝阳16 material-to-knowledge chain under “2026一模已处理映射（细则支持）”.

## Failures To Rerun
- none for the corrected 2026朝阳一模第16题 slice.

## Remaining Blockers
- 2025海淀期中: no usable 必修四哲学 rubric found; not merged into the main framework.
- 2025海淀二模客观题: paper is scan-only and has been rendered; available lecture/rubric files do not contain a reliable choice-answer table, so no inferred choice answers were written into the wrong-option library.
- 2026二模: no local folder or zip found under `C:\Users\Administrator\Desktop` or `C:\Users\Administrator\Desktop\2026各区模拟题`.

## Checks
- no unresolved scan-only or hard-to-read file was left without tool handling in this slice.
- no teacher/reference answer was used as rubric for 朝阳16; the entry is based on the user-supplied 主观题阅卷细则docx.
- every newly merged logic chain names source suite and question number.
- 朝阳16 logic chain includes material trigger, rubric-supported knowledge, and transmission path.
- previous false blocker for 2026朝阳一模16 has been removed from the framework.
- 2025二模 new wrong-option entries all include source suite and question number.
- 2025海淀二模 choice items were not entered because the answer basis is not reliable enough.
