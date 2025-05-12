import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Make sure SERPAPI_API_KEY and OPENAI_API_KEY are in your .env file
serpapi_api_key = os.getenv("SERPAPI_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

if not serpapi_api_key:
    raise ValueError("SERPAPI_API_KEY not found in environment variables")
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Initialize the language model
llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

# Create the search tool
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func=search.run,
        description="Useful for when you need to answer questions about current events or specific factual information. Input should be a search query."
    )
]

# Create a ReAct agent
# The ReAct approach combines reasoning and acting in an iterative process
react_template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:"""

prompt = PromptTemplate.from_template(react_template)

agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(
    agent=agent, 
    tools=tools, 
    verbose=True,
    handle_parsing_errors=True
)

# Run the agent with the example
result = agent_executor.invoke({"input": "How many kids do the band members of Metallica have?"})
print("\nFinal Answer:", result["output"])