# Confucius Acceptance

Confucius is the final harsh student-reader. This role exists because a document can look complete while still failing to teach a zero-baseline student how to answer a new question.

## Inputs

Use only the final student-facing artifact:

- final `.docx` rendered pages or exported PDF;
- final Markdown if Word extraction is needed;
- no audit files;
- no source packs;
- no model logs;
- no answer keys unless they are printed inside the student artifact.

## Pass 1: Full Harsh Read

Read from the first teaching entry to the last. Do not sample.

For every entry, check:

- The material signal is visible and concrete.
- The question prompt is the real task sentence, not a dumped material block.
- The explanation connects material signal to principle/method.
- The answer landing is a natural sentence or direction a student can write.
- The entry does not rely on audit terms, source paths, or hidden evidence.
- The formatting helps reading: labels, options, images, page breaks, and quotes are clean.

Mark each entry:

- `PASS`: readable and transferable.
- `SMALL_FIX`: understandable but wording/formatting weak.
- `FAIL`: cannot teach transfer, missing logic, wrong field, or hidden audit dependence.

Any `FAIL` returns the document to repair.

## Pass 2: Framework Coverage Exam

Build an exam that covers every framework node used in the final document.

For each node, give a fresh or held-out material signal and ask the student to choose the principle/method. Pass requires correct node selection and a reason that uses the material signal.

## Pass 3: High-Risk Confusion Exam

Test pairs that students commonly confuse, such as:

- material decision by reality vs subjective initiative;
- development vs认识发展;
- contact diversity vs system optimization;
- contradiction specialness vs concrete problem analysis;
- correct-option chain vs scoring-rubric trigger;
- book/module boundary overlaps.

Pass requires distinguishing the real trigger words and explaining why the rejected node is not the best landing.

## Pass 4: Blind Transfer Exam

Give only material trigger plus question prompt. Do not disclose book/module/node.

The answer must include:

- selected principle/method;
- material signal;
- explanation of why the material triggers it;
- natural answer landing.

## Invalidated PASS

Confucius PASS expires if the final Word is regenerated, entries are batch-rewritten, framework nodes are moved, material trigger chains change, images/options are restored, or the user requests substantive revisions. Re-run the harsh read and learning exams after such changes.

## Report

Write `audit/confucius/CONFUCIUS_ACCEPTANCE_REPORT.md` with:

- artifact path and timestamp;
- number of entries read;
- PASS/SMALL_FIX/FAIL counts;
- exam design and results;
- required repairs;
- final verdict.

