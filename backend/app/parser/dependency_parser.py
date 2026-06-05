import re

IMS_NODES = [
    "P-CSCF",
    "I-CSCF",
    "S-CSCF",
    "HSS",
    "BGCF",
    "MGCF"
]

DEPENDENCY_KEYWORDS = [
    "DNS",
    "HSS",
    "ENUM",
    "Diameter",
    "SIP"
]


def extract_dependencies(text):

    dependencies = []

    lines = text.splitlines()

    for line in lines:

        for node in IMS_NODES:

            if node in line:

                found_dependencies = []

                for dep in DEPENDENCY_KEYWORDS:
                    if dep in line and dep != node:
                        found_dependencies.append(dep)

                if found_dependencies:

                    dependencies.append(
                        {
                            "node": node,
                            "dependencies": list(set(found_dependencies)),
                            "text": line.strip()
                        }
                    )

    return dependencies
