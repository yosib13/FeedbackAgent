import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from GenericLLM import GenericLLMStructureClass


load_dotenv()

class OpenAIClass(GenericLLMStructureClass):
    
    def __init__(self) -> None:
        self.updateLLMConfig()
        
    def updateLLMConfig(self):
        self.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
        self.OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("OPENAI_DEPLOYMENT_ENDPOINT")
        self.OPENAI_MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

    def getLLM(self):
        # Configure OpenAI API
        llm = ChatOpenAI(
                        openai_api_key=self.OPENAI_API_KEY,
                        openai_api_base=self.OPENAI_DEPLOYMENT_ENDPOINT,
                        model=self.OPENAI_MODEL_NAME,
                        temperature=0.1
                        )
        return llm