from app.extraction.pdf_extractor import extract_text
from app.parser.dependency_parser import extract_dependencies

text = extract_text("../uploads/IMS_Deployment_Architecture_Guide.pdf")

results = extract_dependencies(text)

for result in results:
    print(result)
