
class prompt_templates:
    
    def modify_message_with_variables(self, message_templates, variables_file_path):
        # Read the variables from the file
        with open(variables_file_path, 'r') as file:
            variables = [line.strip() for line in file]

        # Replace the placeholders in the template with the actual variables
        modified_messages = message_templates.format(*variables)

        return modified_messages
     
    def generate_likert_scales_for_prompts(self, likert_file_path):
        messages= self.modify_message_with_variables(self.message_templates, self.variables_file_path)
        for message in messages:
        # Read the likert scales from the file
            with open(likert_file_path, 'r') as file:
                likert_scales = [line.strip() for line in file]

            # Create a prompt template for each Likert scale
            prompt_templates = [
                "How would you rate your experience with our service? [{}]".format(scale)
                for scale in likert_scales
            ]
            return prompt_templates