# Slice 044 Source Backcheck Notes

- scope: doc_order 216-220 only
- source_docx: `/Users/wanglifei/Desktop/选必一宝典-飞哥正志讲堂.docx`
- source_docx_sha256: `876e60959e88dfd72ec3c6834b59c4933822a3e347f8a6c82b3a8012b939ab7e`
- source package: `05_source_backcheck/slice_044/`
- source-ledger update needed: no new source rows; this slice reuses registered sources.
- note: 房山一模 Q19 text/rubric are copied from verified `slice_040` excerpts because those files are registered in `SOURCE_LEDGER.csv` and previous slice manifests but not in the global `source_backcheck_manifest.csv` extract list.

## Entry To Source Map

- Q0216 / doc_order 216 / 2025海淀期中Q16(2): `SRC_EXAM_2025_HAIDIAN_QIZHONG_Q16_2.txt` and `SRC_RUBRIC_2025_HAIDIAN_QIZHONG_Q16_2.txt`.
- Q0217 / doc_order 217 / 2026西城一模Q20(2): `SRC_EXAM_2026_XICHENG_YIMO_Q20_2.txt` and `SRC_RUBRIC_2026_XICHENG_YIMO_Q20_2.txt`.
- Q0218 / doc_order 218 / 2026西城一模Q20(2): same 西城一模 Q20(2) source pair as Q0217.
- Q0219 / doc_order 219 / 2026朝阳一模Q20: `SRC_EXAM_2026_CHAOYANG_YIMO_Q20.txt` and `SRC_RUBRIC_2026_CHAOYANG_YIMO_Q20.txt`.
- Q0220 / doc_order 220 / 2026房山一模Q19: `SRC_EXAM_2026_FANGSHAN_YIMO_Q19.txt` and `SRC_RUBRIC_2026_FANGSHAN_YIMO_Q19.txt`.

## Watchpoints For ClaudeCode

- Q0216: compare with Q0215. The desktop entry removes explicit `选必一部分2分`/`（6分）` and uses answer-chain training without fixed point values; verify whether this fixes the previous low-evidence score issue. Also check whether `应携手利用` should restore source wording `充分利用` and subject `我国政府和企业`.
- Q0217: source/rubric supports an 8-point four-layer structure. Check whether row-level core `多边贸易、多边主义与全球经济治理体系改革` is source-backed by the 综合意义 layer or over-compressed.
- Q0218: the entry admits `打破发达国家垄断` is not in the original material, while 同题组 says the rubric allows `提升发展中国家的代表性和发言权、打破发达国家规则制定中的垄断主导`. Verify whether answer landing should keep this as a rubric-level extension, not material fact.
- Q0219: verify that AI眼镜、开源大模型、创新药 support the `创新驱动/全球创新策源地/产业链供应链稳定` branch and whether the answer’s `当前国际竞争的实质...` is a必答点 from rubric.
- Q0220: verify that `二线管住`/零关税/加工增值/东南亚原料-海南加工-全国市场 chain supports global产业链供应链稳定; watch for repeating prior 一线/二线 confusion.
## Prompt Generation Note

- The first doc219 ClaudeCode attempt had empty source excerpts because the prompt generator expected embedded original line numbers, while the 朝阳 source files use actual file line numbers. That attempt is preserved as `04_claudecode/slice_044_doc219_attempt1_empty_source_*` and is not accepted. The retry prompt uses actual source line numbers and is accepted.
