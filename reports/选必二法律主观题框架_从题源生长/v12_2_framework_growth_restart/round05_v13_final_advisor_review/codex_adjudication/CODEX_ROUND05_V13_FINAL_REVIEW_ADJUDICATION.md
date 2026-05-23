# Codex Round05 v13 Final Review Adjudication

Date: 2026-05-23

Status: `round05_minor_patches_accepted_v13_1_created`

## Real Model Gate

| lane | result | evidence |
|---|---|---|
| GPT Pro web | pass | `model_outputs/gpt_round05_v13_final_review_pro_web_raw.md`; visible account/model evidence captured in the web session; verdict `ACCEPT_AFTER_MINOR_PATCHES` |
| Claude Opus 4.7 Adaptive web | pass | `model_outputs/claude_round05_v13_final_review_opus47_web_raw.md`; screenshot `model_outputs/claude_round05_v13_final_review_opus47_web_screenshot.png`; verdict `ACCEPT_AFTER_MINOR_PATCHES` |

No simulated GPT/Claude output is used in this adjudication.

## Accepted Patches

| question_id | adjudication |
|---|---|
| CC0213_2025_门头沟_一模_20 | A primary changed to A8; A5 retained only as reference/example secondary. |
| CC0238_2026_东城_二模_19 | A primary changed to A5; A9 and A8 remain secondary. |
| CC0244_2026_东城_期中_18 | B axis changed from B4 to B2 because the prompt asks legal responsibility and legal basis. |
| CC0180_2025_海淀_期末_20 | B axis changed from B5 to B1 because the prompt asks to complete a table by reference to an example. |
| CC0181_2025_海淀_期末_21 | B axis changed from B2 to B5 because the prompt asks the reason/value of竞业限制 and its limits. |
| CC0084_2025_东城_二模_19 | A5 secondary removed; business reputation remains under A2人格权益 without a competition relationship. |
| CC0332_2026_石景山_二模_19 | A10 secondary removed; public-law/minor-protection boundary note retained outside A10 support. |
| CC0364_2026_通州_期中_19_1 | A10 secondary replaced with A1/procedure-legality support; procedure fact is not dispute-resolution procedure. |
| CC0200_2025_西城_二模_18 | A9 primary retained; A1 dispositive-rule guardrail added for limited civil capacity, ratification, and responsibility sharing. |

## Framework Rule Patches

- Add A5/A9 boundary rule: when the harmed party is a competitor/operator/innovation subject and the scoring chain is commercial defamation, confusion, data scraping, IP, business secret, or unfair competition, use A5 before A9.
- Add A6 guardrail: A6 is primary only when a special tort responsibility rule is the scoring spine; otherwise it is a responsibility mode or secondary boundary.
- Add A10 guardrail: A10 is primary only when the dispute-resolution/procedure mechanism itself is scored; the mere fact of court, public-security, or administrative involvement does not create A10.
- Add conditional value-output rule: value/meaning language is written when B4/B5/B6 or the prompt explicitly asks for meaning, not as a default ending for every answer.

## Rejected Or Limited Suggestions

- No new A-axis trunk is added. Both real model lanes agreed the existing A2-A10 trunk can cover the 42 locked rows after minor boundary patches.
- A5 is not split into separate intellectual-property and unfair-competition trunks. Local row evidence and Claude's transfer-risk warning support keeping one combined trunk.
- Open-container/reference-only rows remain outside the 42 locked core and do not support v13.1 primary counts.

## Result

v13.1 is accepted as the current final patched candidate and supersedes v13.0. v13.0 remains a rollback baseline.

Current final label:

`v13_1_final_baodian_round05_patched_pdf_rendered_docx_generated_with_docx_render_caveat`
