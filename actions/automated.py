import yaml
import json
import requests
from dotenv import load_dotenv
import os
import sys

def process_file(file_path):
    load_dotenv()
    api_key = os.getenv("EDENAI_PRODUCTION_KEY")
    headers = {"Authorization": f"Bearer {api_key}"}

    # Assuming the instructions are static or could be retrieved from another source
    # For dynamic instructions based on the file, you'll need to adjust this part
    prompt_path = 'main/succesfull-prompts/openai4.txt'  # Example static prompt path

    # Read the content of the Python file
    with open(file_path, 'r') as file:
        python_file_content = file.read()

    # Read the prompt content (assuming it's text for now)
    with open(prompt_path, 'r') as file:
        prompt_content = file.read()

    # Prepare the API request payload
    url = "https://api.edenai.run/v2/text/code_generation"
    payload = {
        "providers": "openai",
        "prompt": python_file_content,
        "instruction": prompt_content,
        "temperature":0.1,
        "max_tokens": 1000,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)


    result = json.loads(response.text)
    content = result['openai']['generated_text']
    # Remove potential formatting strings if they are present in the output
    content = content.replace('```python\n', '', 1)  
    content = content.replace('```', '', 1)

    # Adjusted part: Create the output directory if it doesn't exist
    output_dir = "main/action-script/output/"
    os.makedirs(output_dir, exist_ok=True)

    # Define the output file path based on the input file name
    output_file_path = os.path.join(output_dir, os.path.basename(file_path))

    # Save the generated content to the output file
    with open(output_file_path, 'w') as file:
        file.write(content)

    print(f"Processed {file_path} and saved output to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("No file path provided.")
        sys.exit(1)

    file_path = sys.argv[1]  # Get the file path from the command line argument
    process_file(file_path)
