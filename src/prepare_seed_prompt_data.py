import json

class FormatSeedPromptData:
    
    @staticmethod
    def line_to_json_seed_data(line):
        """
        Convert a line of text into a JSON object.

        :param line: The line from the text file.
        :type line: str
        :return: A JSON object representing the line or None if the line is invalid.
        :rtype: dict or None
        """
        parts = line.strip().split(', ')
        if len(parts) < 3:
            return None
        return {'demographic': parts[0], 'major': parts[1], 'format': parts[2]}

    
    
    def line_to_json_seed_verbs(line):
        """
        Convert a line of text into a JSON object.

        :param line: The line from the text file.
        :type line: str
        :return: A JSON object representing the line or None if the line is invalid.
        :rtype: dict or None
        """
        #parts = line.strip().split(', ')
        #if len(parts) < 3:
           # return None
        return {'verb': parts[0]}
    
    def convert_text_to_jsonl(self, input_path, output_path):
        variables_list = []
        with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
            for line in input_file:
                line = line.strip()
                if line:  # Make sure the line is not empty
                    try:
                        json_data = json.loads(line)
                        variables_list.append(json_data)
                        output_file.write(line + '\n')
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}, Line: {line}")
                        # Handle the error as required, maybe skip the line or exit
        return variables_list
    
    '''
    def convert_text_to_jsonl(self, input_path, output_path):
        with open(input_path, 'r') as input_file, open(output_path, 'w') as output_file:
            variables = [json.loads(line.strip()) for line in input_file]  # Assuming each line is a valid JSON
            for variable in variables:
                output_file.write(json.dumps(variable) + '\n')
        return variables

    def convert_text_to_jsonl(self, input_file_path, output_file_path):
        """
        Convert a text file where each line is an entry separated by commas
        into a JSON Lines (jsonl) file where each line is a JSON object.

        :param input_file_path: The path to the input text file.
        :type input_file_path: str
        :param output_file_path: The path to the output jsonl file.
        :type output_file_path: str
        """
        with open(input_file_path, 'r') as text_file, open(output_file_path, 'w') as output_jsonl_file:
            for line in text_file:
                json_object = self.line_to_json_seed_data(line)
                if json_object:
                    output_jsonl_file.write(json.dumps(json_object) + '\n')
'''

# Example usage:
# formatter = FormatSeedPromptData()
# formatter.convert_text_to_jsonl('input_file.txt', 'output_file.jsonl')
