from AzureOpenAIAdaptor import AzureOpenAIClass
from GenericLLM import GenericLLMStructureClass
from OpenAIAdaptor import OpenAIClass

class LLMFactory:
    @staticmethod
    def get_llm_client(client_type: str) -> GenericLLMStructureClass:
        if client_type == 'Azure':
            return AzureOpenAIClass()
        if client_type == 'OpenAI':
            return OpenAIClass()
        else:
            raise ValueError(f"Unsupported client type: {client_type}")