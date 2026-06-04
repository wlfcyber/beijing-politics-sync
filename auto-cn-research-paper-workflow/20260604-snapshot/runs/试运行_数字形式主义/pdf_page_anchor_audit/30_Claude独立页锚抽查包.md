# Independent PDF Page Anchor Audit Pack

- run_id: 试运行_数字形式主义
- generated_at: 2026-06-04T18:18:39.737551+00:00
- pdf_pack: /Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/30_Claude独立页锚抽查包.pdf
- audited_rows: 45, 47, 48, 49, 50
- audit_status: page_images_rendered_from_recorded_source_pdfs

## Rows

| No. | Source | Anchor | Pages | Source PDF SHA256 |
| --- | --- | --- | --- | --- |
| 45 | S-013 | p.7-p.11 | p.7, p.8, p.9, p.10, p.11 | e9179c795656a6cb367822c57c88a57b73686dc0934d0e3480e92422b4563266 |
| 47 | S-010 | p.1, p.4, p.7, p.14-p.15 | p.1, p.4, p.7, p.14, p.15 | 638510eccc4ee7dfc44d402de8925d3690d11ca813b2f496c4075a128b382516 |
| 48 | S-005 | p.2, p.4 | p.2, p.4 | 1491b0608b3f99a9538851fb907c52926954a59912cf53a78d5708b7bab20301 |
| 49 | S-014 | p.1, p.5, p.8-p.11 | p.1, p.5, p.8, p.9, p.10, p.11 | 30f3fe168ad26d15f14c69fd31549dde5fa60edfa2d10151816830e3f8e61737 |
| 50 | S-007 | p.1-p.2, p.5-p.9 | p.1, p.2, p.5, p.6, p.7, p.8, p.9 | 65ce73b50876224a4a243be161fce45cb3f3e931fc1f219505decc2e1c4917b4 |

## Review Instruction

This pack is for independent page-level spot checking. The PDF pack contains a metadata sheet for each citation row, followed by original pages copied from the recorded source PDF. A reviewer should compare the citation context with the visible source pages before deciding whether the anchor can be treated as independently checked.

## Machine Manifest

```json
[
  {
    "no": 45,
    "ref": "[13]",
    "source": "S-013",
    "anchor": "p.7-p.11",
    "pages": [
      7,
      8,
      9,
      10,
      11
    ],
    "source_pdf": "/Users/wanglifei/Documents/论文写作/current_formal_sources/gu_limei_yiwangtongguan_2023.pdf",
    "sha256": "e9179c795656a6cb367822c57c88a57b73686dc0934d0e3480e92422b4563266",
    "rendered_pngs": [
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_045_S-013_p007.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_045_S-013_p008.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_045_S-013_p009.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_045_S-013_p010.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_045_S-013_p011.png"
    ]
  },
  {
    "no": 47,
    "ref": "[10]",
    "source": "S-010",
    "anchor": "p.1, p.4, p.7, p.14-p.15",
    "pages": [
      1,
      4,
      7,
      14,
      15
    ],
    "source_pdf": "/Users/wanglifei/Documents/论文写作/current_formal_sources/fu_liping_technical_governance_township_cadres_2021.pdf",
    "sha256": "638510eccc4ee7dfc44d402de8925d3690d11ca813b2f496c4075a128b382516",
    "rendered_pngs": [
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_047_S-010_p001.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_047_S-010_p004.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_047_S-010_p007.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_047_S-010_p014.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_047_S-010_p015.png"
    ]
  },
  {
    "no": 48,
    "ref": "[5]",
    "source": "S-005",
    "anchor": "p.2, p.4",
    "pages": [
      2,
      4
    ],
    "source_pdf": "/Users/wanglifei/Documents/论文写作/current_formal_sources/数字乡村建设形式主义的生成机理与治理策略_沈费伟.pdf",
    "sha256": "1491b0608b3f99a9538851fb907c52926954a59912cf53a78d5708b7bab20301",
    "rendered_pngs": [
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_048_S-005_p002.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_048_S-005_p004.png"
    ]
  },
  {
    "no": 49,
    "ref": "[14]",
    "source": "S-014",
    "anchor": "p.1, p.5, p.8-p.11",
    "pages": [
      1,
      5,
      8,
      9,
      10,
      11
    ],
    "source_pdf": "/Users/wanglifei/Documents/论文写作/current_formal_sources/chen_tianxiang_yuexiu_digital_governance_2021.pdf",
    "sha256": "30f3fe168ad26d15f14c69fd31549dde5fa60edfa2d10151816830e3f8e61737",
    "rendered_pngs": [
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_049_S-014_p001.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_049_S-014_p005.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_049_S-014_p008.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_049_S-014_p009.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_049_S-014_p010.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_049_S-014_p011.png"
    ]
  },
  {
    "no": 50,
    "ref": "[7]",
    "source": "S-007",
    "anchor": "p.1-p.2, p.5-p.9",
    "pages": [
      1,
      2,
      5,
      6,
      7,
      8,
      9
    ],
    "source_pdf": "/Users/wanglifei/Documents/论文写作/current_formal_sources/乡村治理现代化中“数治负能”的消解逻辑——基于东部Z镇的经验研究_何晓龙.pdf",
    "sha256": "65ce73b50876224a4a243be161fce45cb3f3e931fc1f219505decc2e1c4917b4",
    "rendered_pngs": [
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_050_S-007_p001.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_050_S-007_p002.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_050_S-007_p005.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_050_S-007_p006.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_050_S-007_p007.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_050_S-007_p008.png",
      "/Users/wanglifei/Documents/论文写作/workflows/auto-cn-research-paper-workflow/20260604-snapshot/runs/试运行_数字形式主义/pdf_page_anchor_audit/rendered_pages/row_050_S-007_p009.png"
    ]
  }
]
```
