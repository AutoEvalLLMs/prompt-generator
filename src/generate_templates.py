
class PromptTemplates:
    
    def __init__(self, message_templates, verbs_file_path, variables_file_path):
        self.message_templates = message_templates
        self.verbs_file_path = verbs_file_path
        self.variables_file_path = variables_file_path
    
    def modify_message_with_verbs(self, message_templates, verbs_file_path):
        with open(verbs_file_path, 'r') as file:
            verbs = [line.strip() for line in file]
        modified_messages = [template.format(*verbs) for template in message_templates]
        return modified_messages
    
    def modify_message_with_variables(self, message_templates, variables_file_path):
        messages_with_verbs = self.modify_message_with_verbs(message_templates, self.verbs_file_path)
        with open(variables_file_path, 'r') as file:
            variables = [line.strip() for line in file]
        modified_messages = [message.format(*variables) for message in messages_with_verbs]
        return modified_messages
    
    def generate_likert_scales_for_prompts(self, likert_file_path):
        messages_with_variables = self.modify_message_with_variables(self.message_templates, self.variables_file_path)
        all_prompts = []
        with open(likert_file_path, 'r') as file:
            likert_scales = [line.strip() for line in file]
            for message in messages_with_variables:
                for scale in likert_scales:
                    prompt = "Instructions: Generate and print 5 versions of {message} according to this Likert Scale: [{}]".format(scale)
                    all_prompts.append(prompt)
        return all_prompts