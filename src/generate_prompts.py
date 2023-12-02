from prompt_templates import PromptTemplates
from llamaapi import LlamaAPI
import langchain, json, os, sys
from langchain.chains import create_tagging_chain
import langchain_experimental.llms
from langchain_experimental.llms import ChatLlamaAPI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate

load_dotenv()
llama_api_key = os.getenv('KEY') # get the key from the .env file
llama = LlamaAPI(llama_api_key)


class generatePrompts:
    
    def __init__(self, system_prompt, message):
        self.system_prompt = system_prompt
        self.message = message
        
    def llm_request_prompt_generation(self, system_prompt, message):
        #systemPromptList = []
        with open(system_prompt, 'r') as systemPrompt:
            system_prompt = [line.strip() for line in systemPrompt] 
            system_prompt = system_prompt[0]
            #systemPromptList.append(system_prompt)
        #userPromptList = []
        with open(message, 'r') as message:
            user_prompt = [line.strip() for line in message]
            message = user_prompt[0]
            #message = [line.strip() for line in message]
            #userPromptList.append(user_prompt)
        generatedPrompts = []
        #for message in userPromptList:
            #for systemPrompt in systemPromptList:
        model = ChatLlamaAPI(client=llama)
        api_request_json = {
            "model": "llama-13b-chat",
            "messages": [
                {"role": "system", "content": {systemPrompt}},
                {"role": "user", "content": {message}},
                ]
            }
        response = llama.run(api_request_json)
        response=response.json()
        response=response['choices'][0]['message']['content']
        generatedPrompts.append(response)
        return generatedPrompts
                



            
    