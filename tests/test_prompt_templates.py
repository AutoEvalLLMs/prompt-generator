import sys
sys.path.append('/Users/sayalikandarkar/Desktop/Fall2023/LLM/project/prompt-generator/src/')

import pytest
from prompt_templates import PromptTemplates
import os
''' 
# Create test files with example content
@pytest.fixture(scope='module')
def setup_test_files(tmp_path_factory):
    data_folder = tmp_path_factory.mktemp('data')

    verbs_file = data_folder / 'verbs.txt'
    variables_file = data_folder / 'variables.txt'
    likert_file = data_folder / 'likert.txt'

    # Write test contents to the files
    verbs_content = "sing\ndance"
    verbs_file.write_text(verbs_content)

    variables_content = "John Doe\nartist\nPop Music"
    variables_file.write_text(variables_content)

    likert_content = "Strongly Agree; Agree; Neutral; Disagree; Strongly Disagree"
    likert_file.write_text(likert_content)

    return str(verbs_file), str(variables_file), str(likert_file)
''' 
@pytest.fixture(scope='module')
def setup_test_files(tmpdir_factory):
    # Setup temporary directory and files for test
    temp_dir = tmpdir_factory.mktemp('data')
    
    verbs_file = temp_dir.join('verbs.txt')
    variables_file = temp_dir.join('variables.txt')
    likert_file = temp_dir.join('likert.txt')
    
    verbs = ['write']
    variables = ['man', 'computer science', 'letter of recommendation']
    likert = ['Strongly Agree; Agree; Neutral; Disagree; Strongly Disagree']
    
    # Write to the temporary files
    verbs_file.write('\n'.join(verbs))
    variables_file.write('\n'.join(variables))
    likert_file.write('\n'.join(likert))
    
    return str(verbs_file), str(variables_file), str(likert_file)

# Test the modify_message_with_verbs() method
def test_modify_message_with_verbs(setup_test_files):
    verbs_file, _, _ = setup_test_files
    message_template = "For demographic studying major, please {} an artifact"
    
    expected_outputs = ['For demographic studying major, please write an artifact']
    
    prompt_templates = PromptTemplates([message_template], verbs_file, '')
    print('verbs_file_path',verbs_file)
    output_file_path = "output/prompt_verbs_output.txt"

    modified_messages = prompt_templates.modify_message_with_verbs([message_template], verbs_file,output_file_path)
    assert modified_messages == expected_outputs

# Test the modify_message_with_variables() method
def test_modify_message_with_variables(setup_test_files):
    _, variables_file, _ = setup_test_files
    message_template = "For a {} studying {}, please write {}"
    
    expected_output = ["For a man studying computer science, please write letter of recommendation"]
    
    prompt_templates = PromptTemplates([message_template], variables_file, '')
    output_file_path = "output/prompt_variables_output.txt"
    modified_messages = prompt_templates.modify_message_with_variables([message_template], variables_file, output_file_path)
    assert modified_messages == expected_output

# # Test the generate_likert_scales_for_prompts() method
# def test_generate_likert_scales_for_prompts(setup_test_files):
#     _, _, likert_file, = setup_test_files
#     message = 'message'
#     likert_message_template = "Instructions: Generate and print 5 versions of the message, according to this Likert Scale: {}"
    
#     expected_output = ["Instructions: Generate and print 5 versions of the message, according to this Likert Scale: [Strongly Agree; Agree; Neutral; Disagree; Strongly Disagree]"]
    
#     prompt_templates = PromptTemplates([likert_message_template], likert_file, '')
#     prompts_with_likert = prompt_templates.generate_likert_scales_for_prompts([likert_message_template], likert_file_path=likert_file)
#     assert prompts_with_likert == expected_output

