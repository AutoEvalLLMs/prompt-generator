from prepare_seed_prompt_data import FormatSeedPromptData
from langchain.prompts import PromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage
from dotenv import load_dotenv
import json 

class PromptTemplates:
    
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
    
    @staticmethod
    def getSystemPromptTemplates():
        import pandas as pd
        ls_path = '/Users/skingsle/llm-class-term-project/prompt-generator/data/likert_scale_dict'
        likert_scales = []
        with open(ls_path) as e:
            lines = e.readlines()
        for line in lines:
            likert_scales.append(FormatSeedPromptData.line_to_json_seed_scales(line))
            #print(likert_scales)

        examples = likert_scales
        examples 

        example_sys_prompt =PromptTemplate(input_variables=["scale"], template="Instructions: Generate and print 5 versions of the 'prompt_template', according to this {scale}:")

        system_prompt_templates = []
        for num in range(0, 10):
            scale=example_sys_prompt.format_prompt(**examples[num])
            scale=scale.to_string()
            system_prompt_templates.append(scale)
            print(scale)
        return system_prompt_templates
    




    
        