from prepare_seed_prompt_data import FormatSeedPromptData
from prompt_templates import PromptTemplates

# Replace 'your_text_file.txt' with the path to your actual text file.
input_text_file = '/Users/skingsle/llm-class-term-project/prompt-generator/data/seed-data'
output_jsonl_file = '/Users/skingsle/llm-class-term-project/prompt-generator/output/output_file.jsonl'

# convert your seed_data.txt file to a .jsonl file
#FormatSeedPromptData.convert_text_to_jsonl(input_file_path=input_text_file, output_file_path=output_jsonl_file)
formatter = FormatSeedPromptData()
formatter.convert_text_to_jsonl(input_text_file, output_jsonl_file)

# Replace 'your_message_templates.txt' with the path to your actual text file.
message_templates = '/Users/skingsle/llm-class-term-project/prompt-generator/data/seed_messages'  # Replace with the path to your seed-data variables file.
message_output_jsonl_file = 'messages_output_file.jsonl'
variables_file_path = '/Users/skingsle/llm-class-term-project/prompt-generator/output/output_file.jsonl'
#'/Users/skingsle/llm-class-term-project/prompt-generator/data/seed-data'                    
verbs_file_path = '/Users/skingsle/llm-class-term-project/prompt-generator/data/verbs'                         # Replace with the path to your verbs file.



seed_messages_verbs_path = '/Users/skingsle/llm-class-term-project/prompt-generator/output/seed_messages_verbs'
seed_messages_variables_path = '/Users/skingsle/llm-class-term-project/prompt-generator/output/seed_messages_variables'
seed_messages_variables_output_file = '/Users/skingsle/llm-class-term-project/prompt-generator/output/seed_messages_variables'
seed_messages_verbs_output_file=seed_messages_verbs_path

# Replace 'your_likert_scale_text_file.txt' with the path to your actual text file.
likert_file_path = '/Users/skingsle/llm-class-term-project/prompt-generator/data/likert_scale_dict'
prompt_output_file_path = '/Users/skingsle/llm-class-term-project/prompt-generator/output/prompt_output_file.jsonl'

# Get prompts to feed into LLM: 
promptsTemplateGenerator = PromptTemplates(message_templates, verbs_file_path, variables_file_path)
modified_messages_verbs = promptsTemplateGenerator.modify_message_with_verbs(message_templates, verbs_file_path, seed_messages_verbs_path)

modified_messages_variables = promptsTemplateGenerator.modify_message_with_variables(seed_messages_verbs_output_file, variables_file_path, seed_messages_variables_output_file)
                                                                               

promptsTemplateGenerator.generate_likert_scales_for_prompts(seed_messages_variables_output_file, likert_file_path, prompt_output_file_path)
#message_templates, verbs_file_path, variables_file_path