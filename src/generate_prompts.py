from prompt_templates import PromptTemplates
from llamaapi import LlamaAPI
import langchain, json, os, sys
from langchain.chains import create_tagging_chain
import langchain_experimental.llms
from langchain_experimental.llms import ChatLlamaAPI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()
llama_api_key = os.getenv('KEY') # get the key from the .env file
llama = LlamaAPI(llama_api_key) # create the API object

class generatePrompts:
    
    def __init__(self, systemPromptTemplates, prompt_templates):
        self.system_prompt = systemPromptTemplates
        self.messages = prompt_templates
    
    def llm_request_prompt_generation():
        import pandas as pd
        messages = PromptTemplates.getPromptTemplates() # get the prompts
        systemPromptTemplates = PromptTemplates.getSystemPromptTemplates() # get the system prompts
    
        generatedPrompts = [] # initialize the list of generated prompts

        model = ChatLlamaAPI(client=llama) # create the model
        
        for systemPrompt in systemPromptTemplates:
            for message in messages:
                api_request_json = {
                    "model": "llama-13b-chat",
                    "messages": [
                        {"role": "system", "content": str(systemPrompt)},
                        {"role": "user", "content":  str(message)}
                        ]
                    }
                response = llama.run(api_request_json) # run the model
                response=response.json() # convert the response to json
                response=response['choices'][0]['message']['content'] # get the response
                generatedPrompts.append(response) # append the response to the list of generated prompts
                genPrompts = pd.DataFrame(generatedPrompts)
                genPrompts.to_csv('output/generatedPrompts.csv')
        return generatedPrompts # return the list of generated prompts
                



            
    