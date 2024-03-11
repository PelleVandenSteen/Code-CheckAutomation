import requests
import json
from dotenv import load_dotenv
import os

class GenAIWrapper:
    def __init__(self, model):
        load_dotenv()
        self.model = model

    def call_ai_api(self, python_file_content, prompt_content):
        function_map = {
            'gpt35': self._call_gpt35,
            'gpt4': self._call_gpt4,
            'edendummy': self._call_eden_dummy,
            'eden':self._call_eden
            
        }
        
        if self.model in function_map:
            return function_map[self.model](python_file_content, prompt_content)
        else:
            raise ValueError(f"Model {self.model} not supported.")

    def _call_eden_dummy(self,python_file_content, prompt_content):

        url= "https://api.edenai.run/v2/text/code_generation"
        self.api_key = os.getenv("EDENAI_DUMMY_KEY")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = self._generate_payload(python_file_content, prompt_content, additional_params={"providers": "openai"})
        return self._perform_request(url,payload)

    def _call_eden(self,python_file_content,prompt_content):

        url= "https://api.edenai.run/v2/text/code_generation"
        self.api_key =os.getenv("EDENAI_PRODUCTION_KEY")
        self.headers = {"Authorization": f"Bearer {self.api_key}"}
        payload = self._generate_payload(python_file_content, prompt_content, additional_params={"providers": "openai"})
        return self._perform_request(url,payload)


    

    def _call_gpt35(self, python_file_content, prompt_content):
        url = "https://api.example.com/gpt35"
        payload = self._generate_payload(python_file_content, prompt_content, additional_params={"model": "gpt-3.5-turbo"})
        return self._perform_request(url, payload)

    def _call_gpt4(self, python_file_content, prompt_content):
        url = "https://api.example.com/gpt4"
        payload = self._generate_payload(python_file_content, prompt_content, additional_params={"model": "gpt-4"})
        return self._perform_request(url, payload)

    def _generate_payload(self, python_file_content, prompt_content, additional_params=None):
        payload = {
            "prompt": python_file_content,
            "instruction": prompt_content,
            "temperature": 0.1,
            "max_tokens": 1000,
            "fallback_providers": ""
        }
        if additional_params:
            payload.update(additional_params)
        return payload

    def _perform_request(self, url, payload):
        response = requests.post(url, json=payload, headers=self.headers)
        result = json.loads(response.text)
        content = result['openai']['generated_text']
        return content
