import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("EDENAI_DUMMY_KEY")

headers = {"Authorization": f"Bearer {api_key}"}

url = "https://api.edenai.run/v2/text/code_generation"
payload = {
    "providers": "openai",
    "prompt": "",
    "instruction": "have fun bro",
    "temperature": 0,
    "max_tokens": 500,
    "fallback_providers": ""
}

response = requests.post(url, json=payload, headers=headers)

result = json.loads(response.text)
content= result['openai']['generated_text']
print(content)

output_file_path = 'results/test1.py'

# Write the result to the specified file
with open(output_file_path, 'w') as file:
    file.write(content)