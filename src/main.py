from prepare_seed_prompt_data import FormatSeedPromptData
from prompt_templates import PromptTemplates
from generate_prompts import generatePrompts
from dotenv import load_dotenv
from open_files import open_file

# Replace 'your_text_file.txt' with the path to your actual text file.
#with open_file('data/seed-data') as f:
    #input_text_file = f.read()
    
#with open_file('output/output_file.jsonl') as f:
    #output_jsonl_file = f.read()
    
#input_text_file = '/Users/skingsle/llm-class-term-project/prompt-generator/data/seed_variables'
#output_jsonl_file = 'output/output_file.jsonl'

# formatter = FormatSeedPromptData()
# formatter.convert_text_to_jsonl('input_file.txt', 'output_file.jsonl')

# convert your seed_data.txt file to a .jsonl file
#FormatSeedPromptData.convert_text_to_jsonl(input_file_path=input_text_file, output_file_path=output_jsonl_file)
#formatter = FormatSeedPromptData()
#seed_variables = formatter.convert_text_to_jsonl(input_text_file, output_jsonl_file)

# Replace 'your_message_templates.txt' with the path to your actual text file.
#with open_file('data/seed-data') as f:
    #input_text_file = f.read()

# define the seed_verbs input and output file paths:
seed_verbs = '/Users/skingsle/llm-class-term-project/prompt-generator/data/verbs'  # Replace with the path to your seed-data variables file.
verbs_output_file = 'output/verbs_output_file.jsonl'


# define the seed_messages input file path:
seed_messages = '/Users/skingsle/llm-class-term-project/prompt-generator/data/seed_messages'  # Replace with the path to your seed-data variables file.

# convert the seed_variable input TEXT file to a .jsonl file
input_text_file = '/Users/skingsle/llm-class-term-project/prompt-generator/data/seed_variables'
output_jsonl_file = 'output/output_file.jsonl'
formatter = FormatSeedPromptData()
seed_variables = formatter.convert_text_to_jsonl(input_text_file, output_jsonl_file)

# define the seed_likert_scales input file path:
seed_likert_scales = '/Users/skingsle/llm-class-term-project/prompt-generator/data/likert_scale_dict'

# Get prompt TEMPLATES to feed into LLM: 
#### initialize PromptTemplates class:
promptsTemplateGenerator = PromptTemplates(seed_messages, seed_verbs, seed_variables, seed_likert_scales, verbs_output_file)

# generate modified messages with verbs:
#modified_messages_verbs = promptsTemplateGenerator.modify_message_with_verbs(message_templates, verbs_file_path, seed_messages_verbs_path)

# generate modified messages with variables:
#modified_messages_variables = promptsTemplateGenerator.modify_message_with_variables(seed_messages_verbs_output_file, variables_file_path, seed_messages_variables_output_file)
                                                                               
# generate likert scales for prompts:
#promptTemplates = promptsTemplateGenerator.generate_likert_scales_for_prompts(seed_messages_variables_output_file, likert_file_path, prompt_output_file_path)

# generate SYSTEM Prompte TEMPLATES:
system_prompt_templates = promptsTemplateGenerator.generate_likert_scales_for_prompts(seed_messages, seed_verbs, seed_variables, seed_likert_scales)

system_prompt = 'output/final_prompt_output.txt'
message = 'output/variables_output_file.txt'


# Initialize generatePrompts class:
promptsGenerator = promptsTemplateGenerator.generatePrompts(system_prompt, message)

# get prompts:
getPrompts = promptsGenerator.llm_request_prompt_generation(system_prompt, message)
print('getPrompts',getPrompts)




