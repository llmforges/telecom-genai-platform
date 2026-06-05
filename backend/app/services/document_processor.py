from app.extraction.pdf_extractor import extract_text
from app.parser.json_builder import (
    build_document_json,
    save_json
)

from pathlib import Path


def process_document(pdf_path):

    pdf_path = Path(pdf_path)

    text = extract_text(str(pdf_path))

    document_json = build_document_json(
        pdf_path.name,
        text
    )

    output_file = (
        Path("../extracted")
        / f"{pdf_path.stem}.json"
    )

    save_json(
        document_json,
        str(output_file)
    )

    return str(output_file)
