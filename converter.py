import json
import yaml
import xmltodict

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        if file_path.endswith('.json'):
            return json.load(file)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            return yaml.safe_load(file)
        elif file_path.endswith('.xml'):
            return xmltodict.parse(file.read())
        else:
            raise ValueError("Unsupported file format")

def write_file(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        if file_path.endswith('.json'):
            json.dump(data, file, indent=4)
        elif file_path.endswith('.yaml') or file_path.endswith('.yml'):
            yaml.dump(data, file, allow_unicode=True, default_flow_style=False)
        elif file_path.endswith('.xml'):
            xml_data = xmltodict.unparse(data, pretty=True)
            file.write(xml_data)
        else:
            raise ValueError("Unsupported file format")

def convert_file(input_path, output_path):
    data = read_file(input_path)
    write_file(data, output_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: converter.py input_path output_path")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    convert_file(input_path, output_path)