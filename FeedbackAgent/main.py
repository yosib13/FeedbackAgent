import os
import sys

module_dir = os.path.abspath(os.path.join(os.path.dirname(__file__)))

# Add the directory to sys.path
sys.path.insert(0, module_dir)

from dotenv import load_dotenv
load_dotenv(override=True)
from DataProcess import DataProcess
from LLMFactory import LLMFactory
from langchain_core.tools import tool
from PromptFactory import PromptFactory
from langchain_experimental.tools import PythonREPLTool
from langchain.agents import AgentExecutor, create_react_agent

dataProcess = DataProcess()

class FeedbackAnalyzer:
        
    def __init__(self):
        df = dataProcess.load_data_file(os.getenv("DATA_FILE_PATH"))
        self.df_relevant = dataProcess.preprocess_data(df)

        self.metadata = dataProcess.extract_metadata(df)

        self.llm = LLMFactory.get_llm_client(os.getenv('LLM_TYPE')).getLLM()

        self.python_repl = PythonREPLTool(description=PromptFactory.PythonREPLPrompt)
        self.python_repl.python_repl.globals['df'] = self.df_relevant
        
        self.tools = self.initTools()
        
        self.agent_executor = self.initAgentExecutor(self.llm, self.tools)


    def initTools(self):
        tools = [self.python_repl]
        return tools

    def initAgentExecutor(self, llm, tools):
        agent = create_react_agent(llm=llm, tools=tools, prompt=PromptFactory.BasePrompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)
        return agent_executor

    def generateAnswer(self, userInput: str):
        agent_out = self.agent_executor.invoke(
            {
                "metadata": self.metadata,
                "tools": self.tools,
                "input": userInput,
                "chat_history": ""
            })
        return agent_out['output'].strip("`")
        
    # while True:
    #     question = input("Enter your question: ")
    #     agent_out = agent_executor.invoke(
    #         {
    #             "metadata": metadata,
    #              "tools": tools,
    #             "input": question,
    #             "chat_history": ""
    #         })
    #     print("Response:", agent_out['output'])