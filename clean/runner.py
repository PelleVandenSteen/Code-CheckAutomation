import yaml
from gen_ai_wrapper import GenAIWrapper
from output import Output
import argparse

class Runner:
    def __init__(self, config_path, model, output_option):
        with open(config_path, 'r') as yamlfile:
            self.cfg = yaml.safe_load(yamlfile)
        self.model = model
        self.output_option = output_option

    def run(self):
        python_file_path = self.cfg['workflow']['input']['path']
        prompt_path = self.cfg['workflow']['process']['script']
        output_file_path = self.cfg['workflow']['output']['path']

        with open(python_file_path, 'r') as file:
            python_file_content = file.read()

        with open(prompt_path, 'r') as file:
            prompt_content = file.read()

        wrapper = GenAIWrapper(self.model)
        content = wrapper.call_ai_api(python_file_content, prompt_content)
        print(2)
        print(content)

        Output.write_output(content, output_file_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run the AI model with specified options.')
    parser.add_argument('--model', type=str, help='Model to use', default='gpt35')
    parser.add_argument('--output', type=str, help='Output format', default='annotation')
    
    args = parser.parse_args()
    config_path = 'config.yml'
    
    runner = Runner(config_path, args.model, args.output)
    runner.run()