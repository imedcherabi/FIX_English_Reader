import xml.etree.ElementTree as ET

def load_fix_dictionary(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    tag_names = {}
    tag_values = {}

    for field in root.findall("./fields/field"):
        number = field.attrib['number']
        name = field.attrib['name']
        tag_names[number] = name

        values = {}
        for value in field.findall("value"):
            enum = value.attrib.get('enum')
            description = value.attrib.get('description')
            if enum and description:
                values[enum] = description
        if values:
            tag_values[number] = values

    return tag_names, tag_values

def parse_fix_message(fix_message, tag_names, tag_values):
    fix_message = fix_message.replace('|', '\x01')
    parts = fix_message.strip().split('\x01')

    for part in parts:
        if '=' not in part:
            continue
        tag, val = part.split('=', 1)
        tag_name = tag_names.get(tag, f"UnknownTag({tag})")
        val_meaning = tag_values.get(tag, {}).get(val, val)
        print(f"{tag} ({tag_name}) = {val_meaning}")

if __name__ == "__main__":
    tag_names, tag_values = load_fix_dictionary("FIX44.xml")

    while True:
        fix_msg = input("Enter FIX message :\n")
        parse_fix_message(fix_msg, tag_names, tag_values)
        print()  # blank line after each message
