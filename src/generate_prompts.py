from prompt_templates import PromptTemplates
from llamaapi import LlamaAPI
import langchain, json, os, sys
from langchain.chains import create_tagging_chain
import langchain_experimental.llms
from langchain_experimental.llms import ChatLlamaAPI
from dotenv import load_dotenv

load_dotenv()
llama_api_key = os.getenv('KEY') # get the key from the .env file
llama = LlamaAPI(llama_api_key)


class generatePrompts:
    
    def __init__(self, prompt_template_output_file, seed_messages_variables_output_file):
        self.prompt_template_output_file = prompt_template_output_file
        self.seed_messages_variables_output_file = seed_messages_variables_output_file
        
    def llm_request_prompt_generation(self, prompt_template_output_file, seed_messages_variables_output_file):
        systemPromptList = []
        with open(prompt_template_output_file, 'r') as file:
            system_prompt = [line.strip() for line in file] 
            systemPromptList.append(system_prompt)
        userPromptList = []
        with open(seed_messages_variables_output_file, 'r') as file:
            user_prompt = [line.strip() for line in file]
            userPromptList.append(user_prompt)
        generatedPrompts = []
        for user_message in userPromptList:
            for sysPrompt in systemPromptList:
                model = ChatLlamaAPI(client=llama)
                api_request_json = {
                    "model": "llama-13b-chat",
                    "messages": [
                        {"role": "system", "content": "{sysPrompt}}"},
                        {"role": "user", "content": "{user_message}"},
                        ]
                    }
                response = llama.run(api_request_json)
                response=response.json()
                response=response['choices'][0]['message']['content']
                generatedPrompts.append(response)
                return generatedPrompts
                



            
    