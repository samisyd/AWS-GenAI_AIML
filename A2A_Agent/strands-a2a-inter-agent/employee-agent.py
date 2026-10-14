import os
#  OLD Code
# from mcp.client.streamable_http import streamablehttp_client
from mcp.client.streamable_http import streamable_http_client


from strands import Agent
from strands.tools.mcp.mcp_client import MCPClient
from strands.multiagent.a2a import A2AServer
from urllib.parse import urlparse
# from strands.models.anthropic import AnthropicModel
from strands.models.litellm import LiteLLMModel  # Import LiteLLM model for lightweight LLM capabilities

# Define URLs correctly - do not use os.environ.get() for literal values
EMPLOYEE_INFO_URL = "http://localhost:8002/mcp/"
EMPLOYEE_AGENT_URL = "http://localhost:8001/"

# Create the MCP client
employee_mcp_client = MCPClient(lambda: streamable_http_client(EMPLOYEE_INFO_URL))

# Initialize the LiteLLM model provider configured for OpenAI
model = LiteLLMModel(
    model_id="openai/gpt-4o",  # LiteLLM format: 'openai/<model_name>'    
    params={
        "temperature": 0.2,
        "api_key": os.environ.get("OPENAI_API_KEY"), # Optional if set in environment
        "max_tokens": 1000        
    }    
)

# Using the MCP client within a context
with employee_mcp_client:
    tools = employee_mcp_client.list_tools_sync()
    
    # Create a Strands agent
    employee_agent = Agent(
        model=model,
        name="Employee Agent",
        description="Answers questions about employees",
        tools=tools,
        system_prompt="you must abbreviate employee first names and list all their skills"        
    )
    
    # Create A2A server
    a2a_server = A2AServer(
        agent=employee_agent, 
        host=urlparse(EMPLOYEE_AGENT_URL).hostname, 
        port=int(urlparse(EMPLOYEE_AGENT_URL).port)
    )
    
    # Start the server
    if __name__ == "__main__":
        a2a_server.serve(host="localhost", port=8001)