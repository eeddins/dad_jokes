import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import json
import urllib3

# Disable the warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extract_description(url):
    # Send a GET request to the URL
    response = requests.get(url, verify=False)

    # Parse the XML response
    tree = ET.ElementTree(ET.fromstring(response.content))
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
url = 'https://jokesoftheday.net/jokes-feed/'  # Replace with your URL
json_descriptions = extract_description(url)

# Save the output to a file
with open('dadjokes.list', 'w') as f:
    f.write(json_descriptions)