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
    
#input_text_file = 'data/seed-data'
#output_jsonl_file = 'output/output_file.jsonl'

# convert your seed_data.txt file to a .jsonl file
#FormatSeedPromptData.convert_text_to_jsonl(input_file_path=input_text_file, output_file_path=output_jsonl_file)
# formatter = FormatSeedPromptData()
# formatter.convert_text_to_jsonl(input_text_file, output_jsonl_file)

# Replace 'your_message_templates.txt' with the path to your actual text file.
#with open_file('data/seed-data') as f:
    #input_text_file = f.read()
    
    
seed_messages = 'data/seed_messages'  # Replace with the path to your seed-data variables file.
seed_verbs = 'data/seed_verbs'  # Replace with the path to your seed-data variables file.
seed_variables = 'data/seed_variables'  # Replace with the path to your seed-data variables file.
seed_likert_scales = 'data/likert_scale_dict'

#seed_message_output = 'messages_output_file.jsonl'

#variables_file_path = 'output/output_file.jsonl'

#verbs_file_path = 'data/verbs'                         # Replace with the path to your verbs file.



#seed_messages_verbs_path = 'output/seed_messages_verbs'
#seed_messages_variables_path = 'output/seed_messages_variables'
#seed_messages_variables_output_file = 'output/seed_messages_variables'
#seed_messages_verbs_output_file=seed_messages_verbs_path

# Replace 'your_likert_scale_text_file.txt' with the path to your actual text file.
#seed_likert_scales = 'data/likert_scale_dict'


#prompt_output_file_path = 'output/prompt_output_file.jsonl'


# Get prompt TEMPLATES to feed into LLM: 

# initialize PromptTemplates class:
promptsTemplateGenerator = PromptTemplates(seed_messages, seed_verbs, seed_variables, seed_likert_scales)

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




