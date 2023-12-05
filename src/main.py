from prepare_seed_prompt_data import FormatSeedPromptData
from prompt_templates import PromptTemplates
from generate_prompts import generatePrompts
from dotenv import load_dotenv
from open_files import open_file

input_text_file = '/Users/skingsle/llm-class-term-project/data/seed_variables.txt'
output_jsonl_file = 'output/output_file.jsonl'
formatter = FormatSeedPromptData()

# Initialize getPromptTemplates class:
messages = PromptTemplates.getPromptTemplates()
print(messages)

systemPromptTemplates = PromptTemplates.getSystemPromptTemplates()
print(systemPromptTemplates)

# get prompts:
from generate_prompts import generatePrompts
getPrompts = generatePrompts.llm_request_prompt_generation()
print('getPrompts',getPrompts)




