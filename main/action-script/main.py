import yaml
import json
import requests
from dotenv import load_dotenv
import os


load_dotenv()
api_key = os.getenv("EDENAI_PRODUCTION_KEY")
headers = {"Authorization": f"Bearer {api_key}"}


with open('main/temp-yml-storage/config.yml', 'r') as yamlfile:
    cfg = yaml.safe_load(yamlfile)

python_file_path = cfg['workflow']['input']['path']
prompt_path = cfg['workflow']['process']['script']  
output_file_path = cfg['workflow']['output']['path']


with open(python_file_path, 'r') as file:
    python_file_content = file.read()


with open(prompt_path, 'r') as file:
    prompt_content = file.read()


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
content = result['openai']['generated_text']


content = content.replace('```python\n', '', 1)  
content = content.replace('```', '', 1) 

with open(output_file_path, 'w') as file:
    file.write(content)
