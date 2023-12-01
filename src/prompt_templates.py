from prepare_seed_prompt_data import FormatSeedPromptData
import json 

class PromptTemplates:
    
    def __init__(self, message_templates, verbs_file_path, variables_file_path):
        self.message_templates = message_templates
        self.verbs_file_path = verbs_file_path
        self.variables_file_path = variables_file_path
        #self.likert_file_path = likert_file_path
    
    def modify_message_with_verbs(self, message_templates, verbs_file_path, seed_messages_verbs_output_file_path):
        formatter = FormatSeedPromptData()
        with open(verbs_file_path, 'r') as verbs_input_file, open(seed_messages_verbs_output_file_path, 'w') as output_file:
            verbs = [line.strip() for line in verbs_input_file]
            modified_messages_verbs = [template.format(*verbs) for template in message_templates]
            print('modified_messages_verbs',modified_messages_verbs)
        #for message in modified_messages_verbs:
            #json_object = formatter.line_to_json_02(message)  # Assuming that this method exists
            #if json_object:
            output_file.write(json.dumps(modified_messages_verbs) + '\n')
            return modified_messages_verbs
    
    def modify_message_with_variables(self, seed_messages_verbs_output_file, variables_file_path, seed_messages_variables_output_file):
        formatter = FormatSeedPromptData()
        with open(variables_file_path, 'r') as file,  open(seed_messages_variables_output_file, 'w') as seed_messages_variables_output_file:
            variables = [line.strip() for line in file]
            modified_messages_variables = [message.format(*variables) for message in seed_messages_verbs_output_file]
            print('modified_messages_variables',modified_messages_variables)
        # for message in modified_messages_variables:
        #     print('message',message)
        #     json_object = formatter.line_to_json_seed_data(message)
        #     if json_object:
        #         seed_messages_variables_output_file.write(json.dumps(json_object) + '\n')
        #         return seed_messages_variables_output_file
            seed_messages_variables_output_file.write(json.dumps(modified_messages_variables) + '\n')
            return modified_messages_variables
    
    def generate_likert_scales_for_prompts(self, seed_messages_variables_output_file, likert_file_path, prompt_output_file_path):
        formatter = FormatSeedPromptData()
        for message in seed_messages_variables_output_file:
            with open(likert_file_path, 'r') as input_file, open(prompt_output_file_path, 'w') as prompt_output_file:
                likert_scales = [line.strip() for line in input_file]
                # text = "Instructions: {message} [{scale}]"
                text = "{message} [{scale}]"
                #for message in modified_messages_variables:
                for scale in likert_scales:
                    formatted_prompt = text.format(message=message, scale=scale)
                    # json_object = formatter.line_to_json_02(formatted_prompt)
                    # if json_object:
                    print('formatted_prompt',formatted_prompt)
                    prompt_output_file.write(json.dumps([formatted_prompt]) + '\n')
                    return [formatted_prompt]
        