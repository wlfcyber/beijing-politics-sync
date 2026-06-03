# DEVELOPMENT_PLAN

1. Copy the Claude DOCX to a working DOCX.
2. Apply deterministic DOCX edits:
   - relabel all `2026丰台期末Q20` entries and same-question references to `2026丰台期末细则复练Q20`;
   - rewrite the conflicting Dongcheng Q19(3) entry under `中国扩大高水平对外开放与制度型开放`.
3. Audit the edited DOCX for:
   - field coverage;
   - core-point count;
   - template residue;
   - fake-page residue;
   - book-title residue;
   - forbidden backend labels;
   - remaining ordinary `2026丰台期末Q20` labels;
   - Dongcheng strong-chain conflict under the wrong core.
4. Open the final DOCX in Word to record live page count.
5. Export PDF if Word automation succeeds; if not, report that DOCX is final and PDF export is blocked by Word automation.

