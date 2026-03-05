from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
# import openai

import os
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup GROQ API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables")


## Financial agent
finance_agent=Agent(
    name="Groq Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile", api_key=api_key),
    tools=[
        YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,
                      company_news=True),
    ],
    instructions=[
        "Delegate financial queries to the 'Finance AI Agent'.",
        "Use tables to display the data"],
    show_tool_calls=True,
    markdown=True
)

finance_agent.print_response("Compare NVDA and TSLA stock performance", stream=True)
