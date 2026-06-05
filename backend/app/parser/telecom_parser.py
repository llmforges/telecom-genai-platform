import re

IMS_NODES = [
    "P-CSCF",
    "I-CSCF",
    "S-CSCF",
    "HSS",
    "BGCF",
    "MGCF"
]

INTERFACES = [
    "Diameter",
    "SIP",
    "DNS",
    "ENUM"
]


def extract_entities(text):

    nodes = []
    interfaces = []

    for node in IMS_NODES:
        if node in text:
            nodes.append(node)

    for interface in INTERFACES:
        if interface in text:
            interfaces.append(interface)

    ports = re.findall(r'\b\d{4,5}\b', text)

    return {
        "nodes": list(set(nodes)),
        "interfaces": list(set(interfaces)),
        "ports": list(set(ports))
    }
