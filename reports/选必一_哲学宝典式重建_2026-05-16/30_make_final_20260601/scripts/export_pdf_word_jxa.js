#!/usr/bin/osascript -l JavaScript

const word = Application("Microsoft Word");
word.includeStandardAdditions = true;
word.open(Path("/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.docx"));
const doc = word.activeDocument;
const out = "/Users/wanglifei/Desktop/选必一_当代国际政治与经济_主观题术语宝典_最终版_20260601.pdf";
try {
  doc.exportAsFixedFormat({ outputFileName: out, exportFormat: 17 });
} catch (e1) {
  try {
    doc.exportAsFixedFormat({ outputFileName: out, exportFormat: "wdExportFormatPDF" });
  } catch (e2) {
    console.log(String(e1));
    console.log(String(e2));
    throw e2;
  }
}
doc.close({ saving: "no" });
