import re

def extract_sections(text):
    pattern = r'(\d+\.\s+[^\n]+)'

    matches = list(re.finditer(pattern, text))

    sections = []

    for i, match in enumerate(matches):
        title = match.group(1)

        start = match.end()

        if i + 1 < len(matches):
            end = matches[i + 1].start()
        else:
            end = len(text)

        content = text[start:end].strip()

        sections.append({
            "section": title,
            "content": content
        })

    return sections
