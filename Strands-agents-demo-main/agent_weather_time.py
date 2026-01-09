

from strands import Agent
#from strands.models.anthropic import AnthropicModel
from strands_tools import current_time, http_request, use_aws

# System prompt guiding the agent's behavior
WEATHER_SYSTEM_PROMPT = """You are a weather assistant with HTTP capabilities. You can:
1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data
3. Provide weather information for locations in the United States
4. After displaying the above do not repeat and stop.

When displaying responses:
- Format weather data in a human-readable way
- Highlight important information like temperature, precipitation, and alerts
- Handle errors appropriately
- Convert technical terms to user-friendly language

Always explain the weather conditions clearly and provide context for the forecast.

"""    

subject_expert = Agent(
    system_prompt=WEATHER_SYSTEM_PROMPT,
    tools=[current_time, http_request,use_aws]
)

# def invoke(payload):
#     # Test the agent with a query that might benefit from tools
query = """
    Answer the following questions:
    1. What is the current time in New York City, USA?
    2. What is the weather in New York City, USA?
    3. List the s3 buckets in my AWS account
    """

response = subject_expert(query)
print(response)

