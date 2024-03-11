class Output:
    @staticmethod
    def write_output(content, output_file_path):
        content = content.replace('```python\n', '', 1)
        content = content.replace('```', '', 1)
        with open(output_file_path, 'w') as file:
            file.write(content)
