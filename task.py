from crewai import Task
from agents import financial_analyst
from tools import FinancialDocumentTool

analyze_financial_document = Task(
    description="""
Analyze the uploaded financial document and answer the user's query.
Base your response strictly on the document content.
Provide:
- Key financial highlights
- Risks
- Investment outlook
""",
    expected_output="""
A structured financial analysis with:
1. Summary
2. Financial performance
3. Risks
4. Investment recommendation
""",
    agent=financial_analyst,
    tools=[FinancialDocumentTool.read_data_tool]
)
