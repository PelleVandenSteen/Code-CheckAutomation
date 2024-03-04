import yaml
import json
import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("EDENAI_PRODUCTION_KEY")
headers = {"Authorization": f"Bearer {api_key}"}

# Load YAML configuration
with open('main/temp-yml-storage/config.yml', 'r') as yamlfile:
    cfg = yaml.safe_load(yamlfile)

# Extract paths from YAML configuration
python_file_path = cfg['workflow']['input']['path']
prompt_path = cfg['workflow']['process']['script']  # Assuming this is the prompt path
output_file_path = cfg['workflow']['output']['path']

# Read the content of the input file
with open(python_file_path, 'r') as file:
    python_file_content = file.read()

# Assuming prompt_path is actually the path to the file containing the instruction
with open(prompt_path, 'r') as file:
    prompt_content = file.read()

# Configure the payload for the request
url = "https://api.edenai.run/v2/text/code_generation"
payload = {
    "providers": "openai",
    "prompt": python_file_content,
    "instruction": prompt_content,
    "temperature": 1,
    "max_tokens": 1000,
    "fallback_providers": ""
}

# Make the request
response = requests.post(url, json=payload, headers=headers)

# Process the response
result = json.loads(response.text)
content = result['openai']['generated_text']

# Clean up the content if necessary
content = content.replace('```python\n', '', 1)  # Remove the first occurrence of ```python\n
content = content.replace('```', '', 1)  # Remove the first occurrence of ```

# Write the result to the output file
with open(output_file_path, 'w') as file:
    file.write(content)
