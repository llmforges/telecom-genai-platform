from app.extraction.pdf_extractor import extract_text

#pdf_file = "../uploads/ISIPE.pdf"
pdf_file = "../uploads/IMS_Deployment_Architecture_Guide.pdf"

content = extract_text(pdf_file)

print(content[:500])
