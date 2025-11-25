import os
from openai import OpenAI
from openai_agents.agent import Agent
from openai_agents.tool import Tool
from dotenv import load_dotenv

from tools import extract_pdf_text, cache_pdf_text, read_cached_pdf_text

load_dotenv()

client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY"),
)

model = "gemini-2.0-flash"

system_prompt = """You are a Study Assistant. Summarize academic PDFs and generate 
quizzes based strictly on the PDF content. When generating quizzes, 
DO NOT use the summary—use the full PDF text."""

tools = [
    Tool(extract_pdf_text),
    Tool(cache_pdf_text),
    Tool(read_cached_pdf_text),
]

agent = Agent(client=client, model=model, tools=tools, system_prompt=system_prompt)
