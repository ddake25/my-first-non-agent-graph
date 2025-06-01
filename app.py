# Import packages
from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from view_graph_image import generate_graph_structure


# Create Agent State
class AgentState(TypedDict):
    name: str
    messages: list[dict]
    
# Create node to onboard user
def onboarding_node(state: AgentState):
    user_name = input("What is your name: ")
    state["name"] = user_name
    state["messages"] = f"Hey {state['name']} 🙂\n We are excited to have you join our department!"
    
    return state

# Create Graph
graph_builder = StateGraph(AgentState)

graph_builder.add_node("Onboarder", onboarding_node)
graph_builder.add_edge(START, "Onboarder")
graph_builder.add_edge("Onboarder", END)

graph = graph_builder.compile()

# Generate Graph Structure
generate_graph_structure(graph)