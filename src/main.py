from prepare_seed_prompt_data import convert_text_to_jsonl

# Replace 'your_text_file.txt' with the path to your actual text file.
input_text_file = 'your_text_file.txt'
output_jsonl_file = 'output_file.jsonl'

convert_text_to_jsonl(input_text_file, output_jsonl_file)