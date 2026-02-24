from crewai import Agent
from crewai.llm import LLM
from tools import FinancialDocumentTool

llm = LLM(
    model="gpt-4o-mini",
    temperature=0.2
)

financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze financial documents and provide accurate investment insights",
    backstory="You are a CFA-certified analyst who relies only on provided data.",
    tools=[FinancialDocumentTool.read_data_tool],
    llm=llm,
    verbose=True
)
