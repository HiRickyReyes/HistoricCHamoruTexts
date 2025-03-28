import re
import os
from bs4 import BeautifulSoup as bs

tei_header = """<TEI xmlns="http://www.tei-c.org/ns/1.0">
  <teiHeader>
    <fileDesc>
      <titleStmt>
        <title>A Marianas Mosaic: Signs and Shifts in Contemporary Island Life</title>
        <editor role="lead">Ajani Burrell</editor>
        <editor role="collection">Kimberly Bunts-Anderson</editor>
        <sponsor>Northern Marianas Humanities Council</sponsor>
        <sponsor>National Endowment for the Humanities</sponsor>
        <sponsor>Northern Marianas College</sponsor>
      </titleStmt>
      <publicationStmt>
        <publisher>Proa Publications (An Imprint of University of Guam Press)</publisher>
        <pubPlace>Richard F. Taitano Micronesian Area Research Center (MARC)</pubPlace>
        <date when="2022">2022</date>
        <availability>
          <p>Copyright © 2022 by University of Guam Press. All rights reserved.</p>
          <p>Copyright is meant to respect the research, hard work, imagination, and artistry that go into bringing a text to life. Please respect all copyright laws by not reproducing this resource in any manner without permission from the publisher except in brief quotations used for research, private studies, critical texts, or reviews.</p>
        </availability>
        <idno type="ISBN-13">978-1-935198-66-6</idno>
        <idno type="LCCN">2022940607</idno>
      </publicationStmt>
      <sourceDesc>
        <biblStruct>
          <monogr>
            <title>A Marianas Mosaic: Signs and Shifts in Contemporary Island Life</title>
            <editor role="lead">Ajani Burrell</editor>
            <editor role="collection">Kimberly Bunts-Anderson</editor>
            <imprint>
              <publisher>University of Guam Press</publisher>
              <pubPlace>Guam</pubPlace>
              <date>2022</date>
            </imprint>
          </monogr>
        </biblStruct>
      </sourceDesc>
    </fileDesc>
    <encodingDesc>
      <editorialDecl>
        <p>Orthography Note: This publication includes work from authors throughout the Mariana Islands. Work contributed by authors from Guåhan adhere to the Guåhan CHamoru orthography, while authors from the Commonwealth of the Northern Mariana Islands (CNMI) adhere to the CNMI Chamorro and Refaluwasch orthographies. In some instances, authors have opted to use older or more unique spelling variations as a form of creative expression.</p>
      </editorialDecl>
      <projectDesc>
        <p>This project was made possible with support from the Northern Marianas Humanities Council, a nonprofit, private corporation funded in part by the National Endowment for the Humanities. Support was also provided through matching funds from the Northern Marianas College.</p>
      </projectDesc>
    </encodingDesc>
    <profileDesc>
      <creation>
        <date>2022</date>
        <respStmt>
          <resp>Editors</resp>
          <name>Ajani Burrell</name>
          <name>Kimberly Bunts-Anderson</name>
        </respStmt>
        <respStmt>
          <resp>Orthography Editors</resp>
          <name>Joseph D. Franquez (Guåhan CHamoru)</name>
          <name>Patrick Romolor (CNMI Refaluwasch)</name>
          <name>Manuel Flores Borja (CNMI Chamorro)</name>
        </respStmt>
      </creation>
      <langUsage>
        <language ident="ch">Chamorro</language>
        <language ident="en">English</language>
        <language ident="cr">Refaluwasch</language>
      </langUsage>
    </profileDesc>
    <revisionDesc>
      <change when="2022-12-31" who="#UOGPress">First publication</change>
    </revisionDesc>
  </teiHeader>
  <text>
    <front>
      <div type="toc">
        <head>Table of Contents</head>
        <list>
          <item><title>Introduction</title><author>Ajani Burrell</author></item>
          <item><title>CHamoru Leadership Lessons</title><author>Mary Therese Perez Hattori</author></item>
          <item><title>Repping the Marianas: Cultural Pride and the Rise of Mariana Islands-Inspired Clothing Brands</title><author>Ajani Burrell</author></item>
          <item><title>From Exotica to Erotica: Historical Fiction or Fictional History in Mariana Islands Novels, 2012-2017</title><author>Anne Perez Hattori</author></item>
          <item><title>Mamåhlao: Negotiating Space for Indigenous Culturing</title><author>Royce Camacho</author></item>
          <item><title>Fourth Day</title><author>Gerard van Gils</author></item>
          <item><title>The Halo Halo (‘Mix Mix’) Generation</title><author>Tabitha Caser Espina</author></item>
          <item><title>Poetry from a Son of the Marianas</title><author>Craig Santos Perez</author></item>
          <item><title>Intersection of Identity in Three Generations of CHamoritas and Filipinas in Guam</title><author>Sharleen Santos-Bamba</author><author>Tabitha Caser Espina</author></item>
          <item><title>Bridging Cultures</title><author>Mary Therese Perez Hattori</author></item>
          <item><title>Discovering Saipan Community Art Values</title><author>Angelyn Labadan</author></item>
          <item><title>The Thai Community in Saipan</title><author>Poonsri Algaier</author></item>
          <item><title>Family Violence, Historical Trauma, and the CHamoru Manggåfa (the Family)</title><author>Lisa Linda S. Natividad</author></item>
          <item><title>Ti Siña Ma Funas Ham: Shapes of CHamoru Erasure in Guam</title><author>Kenneth Gofigan Kuper</author></item>
          <item><title>Language Change in Saipan: Attitudes and Visions</title><author>Dominique B. Hess</author></item>
          <item><title>What Saved Me</title><author>Victoria-Lola M. Leon Guerrero</author></item>
          <item><title>Contemporary Dynamics of Traditional Healing in Guam and the Commonwealth of the Northern Mariana Islands</title><author>Tricia Lizama</author></item>
          <item><title>Fanachu Famalåo'an: Women are Emerging as Leaders in the Community-wide Resistance to Militarization in the Commonwealth of the Northern Mariana Islands</title><author>Sylvia C. Frain</author></item>
          <item><title>May I Borrow Some Soy Sauce? The Changing Dynamics of Neighborly Interactions in Rota</title><author>Ajani Burrell</author></item>
          <item><title>Militarism and Sovereignty in the Contemporary Northern Mariana Islands</title><author>Theresa “Isa” Arriola</author></item>
          <item><title>The Evolution of Respeto (Respect) as Viewed through Three Generations of Refaluwasch (Carolinian) Families</title><author>Cinta Matagolai Kaipat</author></item>
          <item><title>Misan Ánimasan Åsuli: field notes and conversations from the Talakhaya Watershed, Luta</title><author>Malcolm Johnson</author></item>
          <item><title>Hågu, Guåhu, yan Hita (You, Me, and We): What Does it Mean to be Part of Guåhan’s (Guam’s) Multi-faceted Community?</title><author>Kelly G. Marsh-Taitano</author></item>
          <item><title>Notes</title></item>
          <item><title>Contributors</title></item>
          <item><title>References</title></item>
        </list>
      </div>
    </front>"""

filepath = "/Users/ricky/digital_texts/corpus/files/1_up_to_date/marianas_mosaic_fully_cleaned.txt"

tei_body = ""
in_the_body = False
in_div = False
in_para = False

with open(filepath, encoding="utf8") as input_file:
    for line in input_file:
        line = line.strip()
        if not in_the_body and "***Introduction (Ajani Burrell)***" in line:
            in_the_body = True
            tei_body += "<body>\n"
        if in_the_body:
            if re.search(r"\*\*\*(.*?)\*\*\*", line):
                if in_div:
                    tei_body += "</div>\n"
                tei_body += f"<div><head>{line}</head>\n"
                in_div = True
                in_para = False
            elif re.search(r"\w", line):
                if not in_para:
                    tei_body += "<p>\n"
                    in_para = True
                tei_body += f"{line} "
            elif line == "" and in_para:
                tei_body += "</p>\n"
                in_para = False
    if in_para:
        tei_body += "</p>\n"
    if in_div:
        tei_body += "</div>\n"
    tei_body += "</body>\n</text>\n</TEI>"

tei = f"{tei_header}\n{tei_body}"

soup = bs(tei, "xml")

output_filepath = "marianas_mosaic.tei"
with open(output_filepath, "w", encoding="utf8") as output_file:
    output_file.write(soup.prettify())

print(f"TEI file successfully saved as {output_filepath}")
