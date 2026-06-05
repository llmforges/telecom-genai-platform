from app.extraction.pdf_extractor import extract_text
from app.parser.section_parser import extract_sections

text = extract_text("../uploads/IMS_Deployment_Architecture_Guide.pdf")

sections = extract_sections(text)

for section in sections:
    print("=" * 50)
    print(section["section"])
    print(section["content"][:200])
