from prepare_seed_prompt_data import FormatSeedPromptData
from prompt_templates import PromptTemplates

# Replace 'your_text_file.txt' with the path to your actual text file.
input_text_file = 'your_seed_data_text_file.txt'
output_jsonl_file = 'jsonl_output_file.jsonl'

# convert your seed_data.txt file to a .jsonl file
FormatSeedPromptData.convert_text_to_jsonl(input_file_path=input_text_file, output_file_path=output_jsonl_file)

# Replace 'your_message_templates.txt' with the path to your actual text file.
message_templates = 'your_message_templates_text_file.txt'
variables_file_path = 'your_variables_file.txt'                     # Replace with the path to your seed-data variables file.
message_output_jsonl_file = 'messages_output_file.jsonl'

# Replace 'your_likert_scale_text_file.txt' with the path to your actual text file.
likert_file_path = 'your_likert_scale_text_file.txt'
output_jsonl_file = 'output_file.jsonl'

# Get prompts to feed into LLM: 
prompts = PromptTemplates.generate_likert_scales_for_prompts(likert_file_path)
