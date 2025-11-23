from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool, FunctionTool, google_search
import logging



# 1. Research Agent: Its job is to use the google_search tool and present findings.



def research_agent() -> Agent:
    research_agent = Agent(
        name="ResearchAgent",
        model="gemini-2.5-flash-lite",
        instruction="""You are a specialized research agent. Your only job is to use the
        google_search tool to find 2-3 pieces of relevant information on the given topic and present the findings with citations.""",
        tools=[google_search],
        output_key="research_findings", # The result of this agent will be stored in the session state with this key.
    )
    return research_agent



# 1. Simple agent with internet
root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description='A helpful assistant for user questions.',
    # It's good practice to tell the agent when to use its tools
    instruction="""Answer user questions to the best of your knowledge.
                Use the research_agent tool if the user asks for real-time information, recent events, or specific facts you do not know.
                """,
    tools=[research_agent], # Pass the tool instance in a list
)
