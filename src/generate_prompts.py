from prompt_templates import PromptTemplates
from llamaapi import LlamaAPI
import langchain, json, os, sys
from langchain.chains import create_tagging_chain
import langchain_experimental.llms
from langchain_experimental.llms import ChatLlamaAPI
from dotenv import load_dotenv

load_dotenv()

llama_api_key = os.getenv('KEY')


class generatePrompts:
    
    