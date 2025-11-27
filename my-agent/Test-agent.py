from google.adk.agents import LlmAgent, SequentialAgent

# Agent 1: Collects data from the user
agent1 = LlmAgent(
    name="DataCollector",
    model="gemini-2.5-flash",
    instruction="Collect the user's name and store it in state['username'].",
    output_key="username"   # Will be accessible as state['username']
)

# Agent 2: Processes the data
agent2 = LlmAgent(
    name="Processor",
    model="gemini-2.5-flash",
    instruction="Say hello to the user using the name stored in {username}."
)

# Sequential pipeline: agent1's output available to agent2
pipeline = SequentialAgent(
    name="UserGreetingPipeline",
    sub_agents=[agent1, agent2]
)

# When pipeline runs, it asks the user for their name (agent1), then greets them (agent2)
response = pipeline.ask("Please enter your name.")
print(response.text)
