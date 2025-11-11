import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from GenericLLM import GenericLLMStructureClass


load_dotenv()

class AzureOpenAIClass(GenericLLMStructureClass):
    
    def __init__(self) -> None:
        self.updateLLMConfig()
        
    def updateLLMConfig(self):
        self.OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
        self.OPENAI_DEPLOYMENT_ENDPOINT = os.getenv("AZURE_OPENAI_DEPLOYMENT_ENDPOINT")
        self.OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
        self.OPENAI_MODEL_NAME = os.getenv("AZURE_OPENAI_MODEL_NAME")
        self.OPENAI_DEPLOYMENT_VERSION = os.getenv("AZURE_OPENAI_DEPLOYMENT_VERSION")
    def getLLM(self):
        # Configure OpenAI API
        llm = AzureChatOpenAI(deployment_name=self.OPENAI_DEPLOYMENT_NAME,
                        model_name=self.OPENAI_MODEL_NAME,
                        azure_endpoint=self.OPENAI_DEPLOYMENT_ENDPOINT,
                        openai_api_version=self.OPENAI_DEPLOYMENT_VERSION,
                        openai_api_key=self.OPENAI_API_KEY,
                        openai_api_type="azure",
                        temperature=0.1,
                        streaming=False,
                        )
        return llm