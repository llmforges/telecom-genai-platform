import json

from app.parser.section_parser import extract_sections
from app.parser.telecom_parser import extract_entities
from app.parser.dependency_parser import extract_dependencies


def build_document_json(document_name, text):

    sections = extract_sections(text)

    entities = extract_entities(text)

    dependencies = extract_dependencies(text)

    output = {
        "document": document_name,
        "summary": {
            "nodes": entities["nodes"],
            "interfaces": entities["interfaces"],
            "ports": entities["ports"]
        },
        "dependencies": dependencies,
        "sections": sections
    }

    return output


def save_json(output, output_file):

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=4)
