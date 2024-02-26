import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("EDENAI_PRODUCTION_KEY")

headers = {"Authorization": f"Bearer {api_key}"}


python_file_path = 'faulty-code/easycode.py'
with open(python_file_path, 'r') as file:
    python_file_content = file.read()

prompt_path = 'succesfull-prompts/openai4.txt'
with open(prompt_path, 'r') as file:
    prompt_content= file.read()



url = "https://api.edenai.run/v2/text/code_generation"
payload = {
    "providers": "openai",
    "prompt": python_file_content,
    "instruction": prompt_content,
    "temperature": 1,
    "max_tokens": 1000,
    "fallback_providers": ""
}

response = requests.post(url, json=payload, headers=headers)

result = json.loads(response.text)
content= result['openai']['generated_text']

output_file_path = 'results/test1.py'

content = content.replace('```python\n', '', 1)  # Replace the first occurrence of ```python\n with an empty string
content = content.replace('```\n', '', 1)  # Replace the first occurrence of ```python\n with an empty string

# Write the result to the specified file
with open(output_file_path, 'w') as file:
    file.write(content)