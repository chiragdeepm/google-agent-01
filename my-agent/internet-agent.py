from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool, FunctionTool, google_search
import logging


# 1. Create the agent and pass the tools to it
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions.',
    # It's good practice to tell the agent when to use its tools
    instruction='Answer user questions to the best of your knowledge. '
                'Use the GoogleSearch tool if the user asks for real-time information, '
                'recent events, or specific facts you do not know.',
    tools=[google_search], # Pass the tool instance in a list
)