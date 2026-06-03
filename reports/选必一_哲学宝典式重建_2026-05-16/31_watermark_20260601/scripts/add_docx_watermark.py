from __future__ import annotations

import argparse
import html
import re
import shutil
import tempfile
import zipfile
from pathlib import Path

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
R = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
REL_NS = "http://schemas.openxmlformats.org/package/2006/relationships"
CT_NS = "http://schemas.openxmlformats.org/package/2006/content-types"
HEADER_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships/header"
HEADER_CT = "application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"


def qn(ns: str, tag: str) -> str:
    return f"{{{ns}}}{tag}"


def next_rid(rels_root: etree._Element) -> str:
    used = []
    for rel in rels_root:
        rid = rel.get("Id", "")
        match = re.fullmatch(r"rId(\d+)", rid)
        if match:
            used.append(int(match.group(1)))
    return f"rId{max(used, default=0) + 1}"


def next_header_name(names: set[str]) -> str:
    nums = []
    for name in names:
        match = re.fullmatch(r"word/header(\d+)\.xml", name)
        if match:
            nums.append(int(match.group(1)))
    return f"word/header{max(nums, default=0) + 1}.xml"


def watermark_paragraph(text: str, fillcolor: str, opacity: str) -> etree._Element:
    safe_text = html.escape(text, quote=True)
    xml = f"""
<w:p xmlns:w="{W}">
  <w:pPr>
    <w:pStyle w:val="Header"/>
  </w:pPr>
  <w:r>
    <w:rPr>
      <w:noProof/>
    </w:rPr>
    <w:pict xmlns:v="urn:schemas-microsoft-com:vml"
            xmlns:o="urn:schemas-microsoft-com:office:office"
            xmlns:w10="urn:schemas-microsoft-com:office:word">
      <v:shapetype id="_x0000_t136" coordsize="21600,21600" o:spt="136"
                   adj="10800" path="m@7,l@8,m@5,21600l@6,21600e">
        <v:formulas>
          <v:f eqn="sum #0 0 10800"/>
          <v:f eqn="prod #0 2 1"/>
          <v:f eqn="sum 21600 0 @1"/>
          <v:f eqn="sum 0 0 @2"/>
          <v:f eqn="sum 21600 0 @3"/>
          <v:f eqn="if @0 @3 0"/>
          <v:f eqn="if @0 21600 @1"/>
          <v:f eqn="if @0 0 @2"/>
          <v:f eqn="if @0 @4 21600"/>
          <v:f eqn="mid @5 @6"/>
          <v:f eqn="mid @8 @5"/>
          <v:f eqn="mid @7 @8"/>
          <v:f eqn="mid @6 @7"/>
          <v:f eqn="sum @6 0 @5"/>
        </v:formulas>
        <v:path textpathok="t" o:connecttype="custom"
                o:connectlocs="@9,0;@10,10800;@11,21600;@12,10800"
                o:connectangles="270,180,90,0"/>
        <v:textpath on="t" fitshape="t"/>
        <v:handles>
          <v:h position="#0,bottomRight" xrange="6629,14971"/>
        </v:handles>
        <o:lock v:ext="edit" text="t" shapetype="t"/>
      </v:shapetype>
      <v:shape id="PowerPlusWaterMarkObjectCodexFeige"
               o:spid="_x0000_s1025" type="#_x0000_t136"
               style="position:absolute;margin-left:0;margin-top:0;width:468pt;height:117pt;z-index:-251654144;mso-position-horizontal:center;mso-position-horizontal-relative:margin;mso-position-vertical:center;mso-position-vertical-relative:margin;rotation:315"
               fillcolor="{fillcolor}" stroked="f">
        <v:fill opacity="{opacity}"/>
        <v:textpath style="font-family:'Microsoft YaHei';font-size:1pt" string="{safe_text}"/>
        <w10:wrap anchorx="margin" anchory="margin"/>
      </v:shape>
    </w:pict>
  </w:r>
</w:p>
"""
    return etree.fromstring(xml.encode("utf-8"))


def add_content_type(content_types: etree._Element, part_name: str) -> None:
    normalized = "/" + part_name
    for override in content_types.findall(qn(CT_NS, "Override")):
        if override.get("PartName") == normalized:
            return
    override = etree.Element(qn(CT_NS, "Override"))
    override.set("PartName", normalized)
    override.set("ContentType", HEADER_CT)
    content_types.append(override)


def make_header_xml(text: str, fillcolor: str, opacity: str) -> bytes:
    root = etree.Element(qn(W, "hdr"), nsmap={"w": W, "r": R})
    root.append(watermark_paragraph(text, fillcolor, opacity))
    return etree.tostring(root, xml_declaration=True, encoding="UTF-8", standalone=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--text", required=True)
    parser.add_argument("--fillcolor", default="#7F7F7F")
    parser.add_argument("--opacity", default=".38")
    args = parser.parse_args()

    if not args.source.exists():
        raise FileNotFoundError(args.source)

    with tempfile.TemporaryDirectory() as tmpdir:
        tmp_path = Path(tmpdir) / "work.docx"
        shutil.copy2(args.source, tmp_path)

        with zipfile.ZipFile(tmp_path, "r") as zin:
            entries = {name: zin.read(name) for name in zin.namelist()}

        names = set(entries)
        document = etree.fromstring(entries["word/document.xml"])
        rels = etree.fromstring(entries["word/_rels/document.xml.rels"])
        content_types = etree.fromstring(entries["[Content_Types].xml"])

        header_name = next_header_name(names)
        rid = next_rid(rels)

        rel = etree.Element(qn(REL_NS, "Relationship"))
        rel.set("Id", rid)
        rel.set("Type", HEADER_REL)
        rel.set("Target", header_name.removeprefix("word/"))
        rels.append(rel)

        entries[header_name] = make_header_xml(args.text, args.fillcolor, args.opacity)
        add_content_type(content_types, header_name)

        ns = {"w": W, "r": R}
        for sect in document.xpath("//w:sectPr", namespaces=ns):
            existing = {
                ref.get(qn(W, "type"))
                for ref in sect.xpath("./w:headerReference", namespaces=ns)
            }
            needed = ["default"]
            if sect.xpath("./w:titlePg", namespaces=ns):
                needed.append("first")
            for header_type in reversed(needed):
                if header_type in existing:
                    continue
                ref = etree.Element(qn(W, "headerReference"))
                ref.set(qn(W, "type"), header_type)
                ref.set(qn(R, "id"), rid)
                sect.insert(0, ref)

        entries["word/document.xml"] = etree.tostring(
            document, xml_declaration=True, encoding="UTF-8", standalone=True
        )
        entries["word/_rels/document.xml.rels"] = etree.tostring(
            rels, xml_declaration=True, encoding="UTF-8", standalone=True
        )
        entries["[Content_Types].xml"] = etree.tostring(
            content_types, xml_declaration=True, encoding="UTF-8", standalone=True
        )

        args.output.parent.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(args.output, "w", compression=zipfile.ZIP_DEFLATED) as zout:
            for name, data in entries.items():
                zout.writestr(name, data)


if __name__ == "__main__":
    main()
