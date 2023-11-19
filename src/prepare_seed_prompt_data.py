import json

class FormatSeedPromptData:
    def __init__(self):
        pass
    
    @staticmethod
    def line_to_json(line):
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
        return {'name': parts[0], 'age': parts[1], 'email': parts[2]}

    def convert_text_to_jsonl(input_file_path, output_file_path):
        """
        Convert a text file where each line is an entry separated by commas
        into a JSON Lines (jsonl) file where each line is a JSON object.

        :param input_file_path: The path to the input text file.
        :type input_file_path: str
        :param output_file_path: The path to the output jsonl file.
        :type output_file_path: str
        """
        with open(input_file_path, 'r') as text_file, open(output_file_path, 'w') as jsonl_file:
            for line in text_file:
                json_object = self.line_to_json(line)
                if json_object:
                    jsonl_file.write(json.dumps(json_object) + '\n')

# Example usage:
# formatter = FormatSeedPromptData()
# formatter.convert_text_to_jsonl('input_file.txt', 'output_file.jsonl')
