# Merge Audit Report

generated_at: 2026-05-19T10:56:58+08:00

## Verdict

CONDITIONAL_PASS.

This report corrects the over-narrow first reasoner packet. The earlier 35-question packet has been reclassified as `formal_core_trial_35` and must not be used as the official full reasoner gate.

## Counts

- Merged canonical candidates: 74
- Official full-context reasoner candidates: 74
- Observation-eligible candidates: 57
- Strong formal/user_confirmed candidates: 54
- Weak reference_only candidates: 3
- Missing-evidence candidates: 17
- Material atoms in full-context packet: 1025
- Ask atoms in full-context packet: 74
- Rubric/answer atoms in full-context packet: 426

## Evidence Level Counts

- formal: 54
- missing: 17
- reference_only: 3

## Merge Status Counts

- keep: 36
- pending_evidence: 17
- pending_locator_check: 21

## Corrected Reasoner Rule

1. `formal` and `user_confirmed` observations may support strong observations when they include question_id, rubric_atom_id, and material_atom_id.
2. `reference_only` observations may only support weak observations and may not independently support a core code.
3. `missing` questions are included as full-context and补证清单 only; they must not support observations because they lack usable rubric evidence.
4. `pending_locator_check` questions remain in the packet, but any observation using them must mark locator risk and should enter source-check if the locator matters.
5. The full-context packet is required because the project target is not merely a high-confidence formal core; it must audit and pressure-test the whole subjective-law candidate universe.

## Still Forbidden

Do not output a framework yet. This corrected packet only authorizes GPT-5.5 Pro and Claude Opus to produce open observations. Codebook, candidate framework, validation, final framework, and baodian remain gated.
