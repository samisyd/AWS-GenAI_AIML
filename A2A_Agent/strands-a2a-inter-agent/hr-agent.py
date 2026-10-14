import os

import uvicorn
from strands import Agent
# from strands.models.anthropic import AnthropicModel
from strands_tools.a2a_client import A2AClientToolProvider
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from strands.models.litellm import LiteLLMModel  # Import LiteLLM model for lightweight LLM capabilities

#EMPLOYEE_AGENT_URL = os.environ.get("EMPLOYEE_AGENT_URL", "http://localhost:8001/")

EMPLOYEE_AGENT_URL = "http://localhost:8001/"

app = FastAPI(title="HR Agent API")

# Initialize the LiteLLM model provider configured for OpenAI
model = LiteLLMModel(
    model_id="openai/gpt-4o",  # LiteLLM format: 'openai/<model_name>'    
    params={
        "temperature": 0.2,
        "api_key": os.environ.get("OPENAI_API_KEY"), # Optional if set in environment
        "max_tokens": 1000
    }    
)

class QuestionRequest(BaseModel):
    question: str

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/inquire")
async def ask_agent(request: QuestionRequest):
    async def generate():
        provider = A2AClientToolProvider(known_agent_urls=[EMPLOYEE_AGENT_URL])

        agent = Agent(model=model, tools=provider.tools)

        stream_response = agent.stream_async(request.question)

        async for event in stream_response:
            if "data" in event:
                yield event["data"]

    return StreamingResponse(
        generate(),
        media_type="text/plain"
    )

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)