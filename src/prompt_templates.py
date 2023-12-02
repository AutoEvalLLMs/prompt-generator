from prepare_seed_prompt_data import FormatSeedPromptData
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
import json 

class PromptTemplates:
    
    def __init__(self, seed_messages, seed_verbs, seed_variables, seed_likert_scales, verbs_output_file):
        self.seed_messages = seed_messages
        self.seed_verbs = seed_verbs
        self.seed_variables = seed_variables
        self.seed_likert_scales = seed_likert_scales
        self.verbs_output_file = verbs_output_file
    
    def modify_message_with_verbs(self, seed_messages, seed_verbs, verbs_output_file):
        formatter = FormatSeedPromptData()
        seed_verbs = self.seed_verbs
        with open(seed_verbs, 'r') as seed_verbs, open(verbs_output_file, 'w') as verbs_output_file:
            verbs = [line.strip() for line in seed_verbs]
            modified_messages_verbs = [template.format(*verbs) for template in seed_messages]
            print('modified_messages_verbs', modified_messages_verbs)
            verbs_output_file.write(json.dumps([modified_messages_verbs]) + '\n')
            return [modified_messages_verbs]
    
    def modify_message_with_variables(self, seed_messages, seed_verbs, seed_variables):
        modified_messages_verbs = self.modify_message_with_verbs(seed_messages, seed_verbs, verbs_output_file)
        verbs_output_file = 'output/verbs_output_file.jsonl'
        with open(verbs_output_file, 'r') as verbs_output_file,  open(variables_output_file, 'w') as variables_output_file:
            variables = [line.strip() for line in seed_variables]
            modified_messages_variables = [message.format(*variables) for message in modified_messages_verbs]
            print('modified_messages_variables',modified_messages_variables)
        # for message in modified_messages_variables:
        #     print('message',message)
        #     json_object = formatter.line_to_json_seed_data(message)
        #     if json_object:
        #         seed_messages_variables_output_file.write(json.dumps(json_object) + '\n')
        #         return seed_messages_variables_output_file
            variables_output_file.write(json.dumps([modified_messages_variables]) + '\n')
            return [modified_messages_variables]
    
    def generate_likert_scales_for_prompts(self, seed_messages, seed_verbs, seed_variables, seed_likert_scales):
        #formatter = FormatSeedPromptData()
        modified_messages_variables = self.modify_message_with_variables(seed_messages, seed_verbs, seed_variables)
        for message in modified_messages_variables:
            with open(seed_likert_scales, 'r') as seed_likert_scales, open(prompt_output_file, 'w') as prompt_output_file:
                likert_scales = [line.strip() for line in seed_likert_scales]
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
        