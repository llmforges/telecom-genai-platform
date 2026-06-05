from app.extraction.pdf_extractor import extract_text
from app.parser.telecom_parser import extract_entities

text = extract_text("../uploads/IMS_Deployment_Architecture_Guide.pdf")

result = extract_entities(text)

print(result)
