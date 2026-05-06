# GPT Content Review Template

Use this after every fixed trigger object: `outline`, `section_batch`, `final_markdown`, and `word_pdf`. Send generated content itself in chunks; do not send accounts, local absolute paths, full source files, or large raw exam/scoring passages. A missing trigger object needs fallback or user waiver.

- trigger_object:
- artifact:
- chunk_id:
- title_path:
- book_scope:
- user_framework_summary:
- target_student:
- evidence_fusion_status_summary:
- content_sent_to_gpt:
- questions_for_content_review:

Ask GPT for: conceptual mistakes, missing material triggers, unsupported answer landings, weak transfer chains, incomplete choice-question logic, contradictions, misleading wording, and concrete rewrites. `must_fix_content` blocks final PASS; `should_fix_transfer` blocks student-facing final PASS when it breaks transfer; `style_or_readability` may be fast-fixed only when it does not change facts.
