from abc import ABC, abstractmethod

class GenericLLMStructureClass(ABC):
    @abstractmethod
    def __init__(self, config) -> None:
        pass

    @abstractmethod
    def updateLLMConfig(self):
        pass

    @abstractmethod
    def getLLM(self):
        pass