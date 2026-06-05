from app.extraction.pdf_extractor import extract_text
from app.parser.json_builder import (
    build_document_json,
    save_json
)

PDF_FILE = "../uploads/IMS_Deployment_Architecture_Guide.pdf"

text = extract_text(PDF_FILE)

document_json = build_document_json(
    "IMS_Deployment_Architecture_Guide.pdf",
    text
)

save_json(
    document_json,
    "../extracted/ims_deployment.json"
)

print("JSON generated successfully")
print(document_json)
