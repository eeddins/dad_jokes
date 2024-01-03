import xml.etree.ElementTree as ET
import json
from bs4 import BeautifulSoup

def extract_description(file_path):
    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()

    # Find all 'description' elements and extract their text
    descriptions = []
    for desc in root.findall('.//description'):
        soup = BeautifulSoup(desc.text, 'html.parser')
        try:
            p_text = soup.find('p').text
            descriptions.append(p_text)
        except:
            pass

    # Convert the list to JSON
    json_descriptions = json.dumps(descriptions)

    return json_descriptions

# Use the function
file_path = 'dadjokes.xml'  # Replace with your file path
#print(extract_description(file_path))
json_descriptions = extract_description(file_path)

# Save the output to a file
with open('dadjokes.list', 'w') as f:
    f.write(json_descriptions)