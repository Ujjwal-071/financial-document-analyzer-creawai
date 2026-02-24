from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import os, uuid

from crewai import Crew, Process
from agents import financial_analyst
from task import analyze_financial_document

app = FastAPI(title="Financial Document Analyzer")

def run_crew(query: str, file_path: str):
    crew = Crew(
        agents=[financial_analyst],
        tasks=[analyze_financial_document],
        process=Process.sequential
    )

    return crew.kickoff(
        inputs={
            "query": query,
            "path": file_path
        }
    )

@app.post("/analyze")
async def analyze(
    file: UploadFile = File(...),
    query: str = Form("Analyze this financial document")
):
    try:
        os.makedirs("data", exist_ok=True)
        file_path = f"data/{uuid.uuid4()}.pdf"

        with open(file_path, "wb") as f:
            f.write(await file.read())

        result = run_crew(query, file_path)

        return {
            "status": "success",
            "analysis": str(result)
        }

    except Exception as e:
        raise HTTPException(500, str(e))

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
