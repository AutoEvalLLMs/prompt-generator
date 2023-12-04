from prepare_seed_prompt_data import FormatSeedPromptData
from langchain.prompts import PromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import json 

class PromptTemplates:
    
    #def __init__(self, seed_messages, seed_verbs, seed_variables, seed_likert_scales):
        #self.seed_messages = seed_messages
        #self.seed_verbs = seed_verbs
        #self.seed_variables = seed_variables
        #self.seed_likert_scales = seed_likert_scales
    
    @staticmethod
    def getPromptTemplates():
        seed_verbs = '/Users/skingsle/llm-class-term-project/prompt-generator/data/verbs'
        with open(seed_verbs) as d:
            seed_verbs = d.readlines()

        import pandas as pd
        seed_verbs=pd.Series(seed_verbs).to_json()

        seed_variables = '/Users/skingsle/llm-class-term-project/prompt-generator/data/seed_variables.txt'
        with open(seed_variables) as e:
            lines = e.readlines()
            seed_variables = []
            for line in lines:
                variable=FormatSeedPromptData.line_to_json_seed_data(line)
                seed_variables.append(variable)
                
        examples = seed_variables
        examples 

        example_prompt =PromptTemplate(input_variables=["demographic", "major", "verb", "format"], template="For {demographic} studying {major}, please provide {format}")

        prompt_templates = []
        for num in range(0, 48):
            ugh=example_prompt.format_prompt(**examples[num])
            ugh=ugh.to_string()
            prompt_templates.append(ugh)
            print(ugh)
        return prompt_templates


'''   
    def promptTemplates(self, seed_messages, seed_verbs, seed_variables, seed_likert_scales):
        self.seed_messages = seed_messages
        self.seed_verbs = seed_verbs
        self.seed_variables = seed_variables
        self.seed_likert_scales = seed_likert_scales
        
        promptTemplateList = []
        for message in seed_messages:
            prompt_template = PromptTemplate.from_template(message)
            promptTemplateList.append(prompt_template)
        for template in promptTemplateList:
            for verb in seed_verbs:
                template.add_verb(verb)
            for variable in seed_variables:
                template.format(demographic=variable[0], )
            template.format()

 
    def modify_message_with_verbs(self, seed_messages, seed_verbs):
        formatter = FormatSeedPromptData()
        #seed_verbs = '/Users/skingsle/llm-class-term-project/prompt-generator/data/verbs'
        #verbs_output_file = 'output/verbs_output_file.jsonl' # Added this line to define verbs_output_file
        data = '/Users/skingsle/llm-class-term-project/prompt-generator/data/verbs'
        with open(data) as f:
            lines = f.readlines()
        verbs = []
        for line in lines:
            verbs.append(FormatSeedPromptData.line_to_json_seed_verbs(str(lines)))
        #with open(seed_verbs, 'r') as seed_verbs_file, open(verbs_output_file, 'w') as verbs_output:
       #with open('output/verbs_output_file.txt', 'w') as verbs_output:
        modified_messages_verbs = [template.format(*verbs) for template in seed_messages]
        print('modified_messages_verbs', modified_messages_verbs)
            #verbs_output.write(json.dumps(modified_messages_verbs) + '\n')
        return modified_messages_verbs
    

    def modify_message_with_variables(self, seed_messages, seed_verbs, seed_variables):
        formatter = FormatSeedPromptData()
        modified_messages_verbs = self.modify_message_with_verbs(seed_messages, seed_verbs)
        variables_output_file = 'output/variables_output_file.jsonl'
        modified_messages_variables = []
        

        try:
            with open(variables_output_file, 'w') as variables_output:
                for variable in seed_variables:  # Assuming seed_variables is a list of dictionaries
                    for message in modified_messages_verbs:
                        modified_message = message.format(**variable)  # Note: Dict unpacking
                        modified_messages_variables.append(modified_message)
                        variables_output.write(json.dumps(modified_message) + '\n')
        except TypeError as e:
            print(f"Error formatting message: {e}")

        return modified_messages_variables


    def generate_likert_scales_for_prompts(self, seed_messages, seed_verbs, seed_variables, seed_likert_scales):
            formatter = FormatSeedPromptData()
            verbs_output_file = 'output/verbs_output_file.jsonl'
            variables_output_file = 'output/variables_output_file.jsonl' 
            prompt_output_file = 'output/variables_output_file.jsonl' 
            modified_messages_variables = self.modify_message_with_variables(seed_messages, seed_verbs, seed_variables)
            for message in modified_messages_variables:
                with open(seed_likert_scales, 'r') as seed_likert_scales, open(prompt_output_file, 'w') as prompt_output:
                    likert_scales = [line.strip() for line in seed_likert_scales]
                    # text = "Instructions: {message} [{scale}]"
                    text = "{message} [{scale}]"
                    #for message in modified_messages_variables:
                    for scale in likert_scales:
                        formatted_prompt = text.format(message=message, scale=scale)
                        # json_object = formatter.line_to_json_02(formatted_prompt)
                        # if json_object:
                        print('formatted_prompt',formatted_prompt)
                        prompt_output.write(json.dumps([formatted_prompt]) + '\n')
                        return [formatted_prompt]



    def modify_message_with_verbs(self, seed_messages, seed_verbs):
        formatter = FormatSeedPromptData()
        seed_verbs = '/Users/skingsle/llm-class-term-project/prompt-generator/data/verbs'
        verbs_output_file = 'output/verbs_output_file.jsonl' # Added this line to define verbs_output_file
        with open(seed_verbs, 'r') as seed_verbs_file, open(verbs_output_file, 'w') as verbs_output:
            #for line in seed_verbs:
                #verbs=formatter.line_to_json_seed_verbs(line)
            verbs = [line.strip() for line in seed_verbs_file]
            modified_messages_verbs = [template.format(*verbs) for template in seed_messages]
            print('modified_messages_verbs', modified_messages_verbs)
            verbs_output.write(json.dumps(modified_messages_verbs) + '\n')
        return modified_messages_verbs


    def modify_message_with_variables(self, seed_messages, seed_verbs, seed_variables):
        input_text_file = '/Users/skingsle/llm-class-term-project/prompt-generator/data/seed_variables'
        output_jsonl_file = 'output/output_file.jsonl'
        formatter = FormatSeedPromptData()
        with open(input_text_file, 'r') as input, open(output_jsonl_file, 'w') as output:
            for line in input_text_file:
                seed_variables_formatted=formatter.convert_text_to_jsonl(line) 
        modified_messages_verbs = self.modify_message_with_verbs(seed_messages, seed_verbs)
        
        verbs_output_file = 'output/verbs_output_file.jsonl'
        variables_output_file = 'output/variables_output_file.jsonl' 
        with open(input_text_file , 'r') as input, open(output_jsonl_file, 'w') as output:
            # for line in input_text_file:  # incorrect
            for line in input:  # correct
                seed_variables_formatted = formatter.line_to_json_seed_data(line)
                modified_messages_variables = [message.format(*seed_variables_formatted) for message in modified_messages_verbs]
                output.write(json.dumps(modified_messages_variables) + '\n')
        # You must return seed_variables from this function
        return modified_messages_variables #seed_variables_formatted

    def modify_message_with_variables(self, seed_messages, seed_verbs, seed_variables):
        input_text_file = '/Users/skingsle/llm-class-term-project/prompt-generator/data/seed_variables'
        output_jsonl_file = 'output/output_file.jsonl'
        formatter = FormatSeedPromptData()
        with open(input_text_file, 'r') as input, open(output_jsonl_file, 'w') as output:
            for line in input_text_file:
                seed_variables_formatted=formatter.line_to_json_seed_data(line)
 
        #seed_verbs = self.seed_verbs   
        
        modified_messages_verbs = self.modify_message_with_verbs(seed_messages, seed_verbs)
        
        verbs_output_file = 'output/verbs_output_file.jsonl'
        variables_output_file = 'output/variables_output_file.jsonl' 
        
        with open(verbs_output_file, 'r') as verbs_output,  open(variables_output_file, 'w') as variables_output:
            variables = [line.strip() for line in seed_variables]
            modified_messages_variables = [message.format(*variables) for message in verbs_output]
            print('modified_messages_variables',modified_messages_variables)
            variables_output.write(json.dumps(modified_messages_variables) + '\n')
            return modified_messages_variables
'''
    
    
        