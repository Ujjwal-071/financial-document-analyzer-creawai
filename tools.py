from pypdf import PdfReader

class FinancialDocumentTool:
    @staticmethod
    def read_data_tool(path: str) -> str:
        reader = PdfReader(path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
