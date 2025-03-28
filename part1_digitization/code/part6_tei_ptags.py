def wrap_paragraphs_para(text):
  paragraphs = text.strip().split("\n\n")  # Split text into paragraphs using double newlines
  wrapped_paragraphs = [f"<p>{paragraph.strip()}</p>" for paragraph in paragraphs]
  return "\n\n".join(wrapped_paragraphs)  # Join paragraphs with double newlines

def wrap_paragraphs_tags(text):
    paragraphs = text.strip().split("\n\n")  # Split text into paragraphs using double newlines
    wrapped_paragraphs = [f"\t<p>{paragraph.strip()}</p>" for paragraph in paragraphs]  # Add tab before <p>
    return "\t".join(wrapped_paragraphs)  


text = """
        The Political Status Education Coordinting Commission
wishes to thank Governor Joseph F. Ada, the 20th Guam Legisla-
ture and the Commission on Self-Determination for their commit-
ment to the teaching and learning of Guam's political history
and political quest.

        We are thankful also to the many government agencies and
employees, and private firms, who took personal interest in our
project and devoted time to our effort, especially to Senator Fran-
cisco R. Santos, Chairman, Committee on Federal and Foreign Affairs,
22nd Guam Legislature; Senator Carl Gutierrez, Chairman, Commit-
tee on Ways and Means, 22nd Guam Legislature; Dr. Franklin Quitugua,
Director, Department of Education; Dr. Wilfred P. Leon Guerrero,
President, University of Guam; Mr. John T. Cruz, President, Guam
Community College; Mr. Leland Bettis, Executive Director, the Com-
mission on Self-Determination; Mr. Wilson Ng; Mr. Frank C. Perez of
the Chamorro Studies and Special Projects Divsion, Department of
Education; Richard Biolchino, Brian Bell, Mike Shafer, Tom Shafer,
and Kathy Duenas of Graphic Center; Mr. Steven Serville of M.1.
Instant Print; Ms. Cherie Wegner of Marianas Electronics; the Historic
Preservation Office, Department of Parks and Recreation; Ms. Carmen
C. Santos; Sister Ignacia Sanchez; Mr. Frank San Agustin, Territorial
Librarian; Mrs. Marjorie Driver, Associate Professor, Spanish Docu-
ments Collections, Micronesian Area Research Center, University of
Guam; Ms. Lou Pangelinan, Governor's chief of staff; Mr. Joaquin D.
Perez, Senator Santos' chief of staff; the Governor's Washington
Liaison Office, Terrence Villaverde; Mr. Bettis' secretary, Mary L.
Flores; and to the former members of the Commission, Dr. Robert
Underwood, Ms. Ernestina A. Cruz and Mr. Pete Perez, Jr.

        The Commission also honors the memory of former member,
the late Pete Perez, Sr., whose unfaltering enthusiasm for this project
was inspirational. Tun Pete did not live to see the fulfillment of our
work, but we know he was always with us in spirit.
The Political Status Education Coordinating Commission

Mr. Antonio Palomo

Chairman

Community Member

Senator Pilar Cruz Lujan

Commission on Self-Determination

John C. Salas, PhD

University of Guam

Mrs. Terry Duenas Hagen

Guam Community College

Mr. BiII Paulino

Mrs. Hope Alvarez Cristobal

Mr•. Carmen Artero Kaspcrbauer

Department of Education




Katherine B. Aguon, PhD

Executive Director

Catherine Sablan Gault

ResearcherfW riter

Jeannine Diaz Muna                                    

Vicente M. Diaz, PhD

Administrative Assistant                              

Historian

Annie Flores                   

Arlina Santos Potts    

Frances T. Lujan

Artist                         

Curriculum Writer      

Production Designer


Creating Ihe Wustratio,..for this book presented challenges because of conflicting descriptions
of Chamorro. As far (U we know, tlae Chamorro wore no clothing. We have used discretion
10 present them without offending those who may object to nudity in a children' book.

COVER ILLUSTRATION BY FRANK C. PEREZ


Printed entirely in Guam by Cruphic Ccnu~r.lnc .• MAite"""


new_text = wrap_paragraphs_para(text)

with open("texts_to_copy.txt", "w", encoding="utf8") as output_file:
  output_file.write(new_text)

print('done')