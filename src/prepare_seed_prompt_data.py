class formatSeedPromptData(object):
    def jsonl_formatter(self, arg1, arg2):
        """
        Description of the function.

        :param arg1: Description of arg1.
        :type arg1: Type of arg1.
        :param arg2: Description of arg2.
        :type arg2: Type of arg2.
        :return: Description of the return value.
        :rtype: Type of the return value.
        """
        # Code for the function goes here
   
        # Define a function to convert line to a JSON object.
        def line_to_json(line):
            parts = line.strip().split(', ')
            if len(parts) < 3:
                return None
            return {
                'name': parts[0], 'age': parts[1], 'email': parts[2]}

        # Convert your text file to a .jsonl file.
        def convert_text_to_jsonl(input_file_path, output_file_path):
            with open(input_file_path, 'r') as text_file, open(output_file_path, 'w') as jsonl_file:
                for line in text_file:
                    json_object = line_to_json(line)
                    # Check if the json_object is not None
                    if json_object:
                        jsonl_file.write(json.dumps(json_object) + '\n')


